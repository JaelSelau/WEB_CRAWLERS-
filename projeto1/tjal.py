import scrapy 
from bs4 import BeautifulSoup

class tjAL_Spider(scrapy.Spider):
    
    name = 'tjal'
    allowed_domains = 'https://www2.tjal.jus.br/cpopg/open.do'
    def start_requests(self):
        start_url= 'https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=01000I1FT0000&processo.foro=1&processo.numero=0731425-82.2014.8.02.0001&uuidCaptcha=sajcaptcha_c5664276eff7498b870cb4c7e2944f9c'        
        
        yield scrapy.Request(start_url,callback=self.parse,dont_filter=True)
                 
    def parse(self,response):
        soup = BeautifulSoup(response.text,"html.parser")
        
        area =soup.find("span","labelClass").parent.text.strip()

        juiz = soup.find("label",string="Juiz:").parent.find_next_sibling("td").text.strip()

        parte = soup.find("table",id="tableTodasPartes").find_all("tr",class_="fundoClaro")

        partes = [] 
            
        for par in parte:
            tipo = par.find("span",class_="mensagemExibindo").text.strip()
            name = par.find("td").find_next_sibling("td").text.strip()
            partes.append({
                "nome":name,
                "tipo":tipo,
            })
        

        movimentacao = soup.find("tbody",id="tabelaTodasMovimentacoes").find_all("tr")
       
        indice = len(movimentacao)
        movimentacoes = []

        for mov in movimentacao:
                
            if mov.find("td").find_next("td").find_next("span"):
                data = mov.find("td").text.strip()
                descricao = mov.find("td").find_next("td").find_next("span").text.strip()       
                nomeOriginal = mov.find("td").find_next("td").find_next("td").contents[0]
               
                nomeOriginal= nomeOriginal.replace('\n\t','')
                nomeOriginal = nomeOriginal.strip()
                movimentacoes.append({
                    "data": data,
                    "indice": indice,
                    "descricao":descricao,
                    "eMovimento":"true",
                    "nomeOriginal":[    nomeOriginal    ]
                })
            else:
                nomeOriginal = mov.find("td").find_next("td").find_next("td").contents[0]
               
                nomeOriginal= nomeOriginal.replace('\n\t','')
                nomeOriginal = nomeOriginal.strip()
                data = mov.find("td").text.strip()
                movimentacoes.append({
                    "data": data,
                    "indice": indice,
                    "eMovimento":"true",
                    "nomeOriginal":[    nomeOriginal    ]
                })
            indice -= 1

        
        
        valorCausa= []
        
        moeda= soup.find("label",string="Valor da ação:").parent.find_next_sibling("td").find("span").text.split()[0]
        
        valor= soup.find("label",string="Valor da ação:").parent.find_next_sibling("td").find("span").text.split()[1]
        
        valorCausa.append({
            "moeda":moeda,
            "valor":valor

        })

        assuntosCNJ= []
        assunto = soup.find("label",string="Assunto:").parent.find_next_sibling("td").find("span").text.strip()
        assuntosCNJ.append({
            "titulo": assunto,

        })
        outrosAssuntos=soup.find("label",string="Outros assuntos:").parent.find_next_sibling("td").find("span").text.split(",")[0]
        assuntosCNJ.append({
            "titulo": outrosAssuntos

        })
        outrosAssuntos1=soup.find("label",string="Outros assuntos:").parent.find_next_sibling("td").find("span").text.split(",")[1]
        assuntosCNJ.append({
            "titulo": outrosAssuntos1

        })

        grauProcesso =" ".join(soup.find("h1",class_="esajTituloPagina").text.split()[-2:])

        orgaoJulgador = soup.find("label",string="Distribuição:").find_parent("tr").find_next_sibling("tr").text.strip().split("-")[0]

        unidadeOrigem = soup.find("label", string="Distribuição:").find_parent("tr").find_next_sibling("tr").text.strip().split("-")[1]

        classeProcedual = soup.find("label", string="Classe:").parent.find_next_sibling("td").text.strip()
      
        dataDistribuicao = soup.find("label", string="Distribuição:").parent.find_next_sibling("td").text.strip()
       
        statusObservacao = soup.find("label",string="Processo:").parent.find_next_sibling("td").find_all("span")[2].text.strip()

        numeroProcessoUnico=  soup.find("label",string="Processo:").parent.find_next_sibling("td").find_all("span")[0].text.strip()
        
        yield{
            "uf": "AL",
            "area":area,
            "juiz":juiz,
            "partes":partes,
            "sistema": "ESAJ-TJAL",
            "segmento": "JUSTICA ESTADUAL",
            "tribunal": "TJ-AL",
            "movimentos": movimentacoes,
            "valorCausa": valorCausa,
            "assuntosCNJ":assuntosCNJ,
            "urlProcesso":response.url,
            "grauProcesso":grauProcesso,
            "orgaoJulgador":orgaoJulgador,
            "unidadeOrigem":unidadeOrigem,
            "classeProcedual":classeProcedual,
            "dataDistribuicao":dataDistribuicao,
            "statusObservacao":statusObservacao,
            "numeroProcessoUnico": numeroProcessoUnico
        }



        
        
   
 
        