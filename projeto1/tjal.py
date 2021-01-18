import scrapy 
from bs4 import BeautifulSoup
from datetime import datetime

class tjAL_Spider(scrapy.Spider):
    
    name = 'tjal'
    allowed_domains = 'tjal.jus.br'

    def start_requests(self):
        start_url= 'https://www2.tjal.jus.br/cpopg/open.do'        
        
        yield scrapy.Request(url=start_url,callback=self.find_page, dont_filter= True)

    def find_page(self,response):
        try:
            response = response.url.replace('open.do','search.do?conversationId=&dadosConsulta.localPesquisa.cdLocal=-1&cbPesquisa=NUMPROC&dadosConsulta.tipoNuProcesso=UNIFICADO&numeroDigitoAnoUnificado=0731425-82.2014&foroNumeroUnificado=0001&dadosConsulta.valorConsultaNuUnificado=0731425-82.2014.8.02.0001&dadosConsulta.valorConsulta=&uuidCaptcha=')
        except:
            print("Url is none!")

        http = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "Connection": "keep-alive",
        "Host": "www2.tjal.jus.br",
        "Referer": 'https://www2.tjal.jus.br/cpopg/open.do',
        "Upgrade-Insecure-Requests": 1,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        
        yield scrapy.Request(url=response,callback=self.parse, dont_filter= True,headers=http)
                 
    def parse(self,response):
        try:
            soup = BeautifulSoup(response.text,"html.parser")
        except:
            print("Erro no parser dos dados!")

        area =soup.find("span","labelClass").parent.text.strip().split(" ")[1]

        juiz = soup.find("label",string="Juiz:").parent.find_next_sibling("td").text.strip()

        parte = soup.find("table",id="tableTodasPartes").find_all("tr",class_="fundoClaro")
       
        partes = [] 
            
        for par in parte:
            tipo = par.find("td").find("span").text.strip().split(':')[0]
            tipo_adv =  par.find("td").find_next_sibling("td").find("span",class_="mensagemExibindo")
            nome = par.find("td").find_next_sibling("td").contents[0].strip()
            advg =[{"nome": adv.upper(),"tipo":tipo_adv.text.strip().split(':')[0].upper()}
            for adv in par.find("td").find_next_sibling("td").stripped_strings if adv != nome if adv != 'Defensor P:' if adv != 'Advogado:' if adv != 'Advogada:']
            if nome != '':
                if tipo != 'Testemunha':
                    partes.append({
                        "nome": nome.upper(),
                        "tipo": tipo.upper(),
                        "Advogado(s)": advg
                        })
                else:
                    partes.append({
                        "nome": nome.upper(),
                        "tipo": tipo.upper(),
                    })
        

        movimentacao = soup.find("tbody",id="tabelaTodasMovimentacoes").find_all("tr")
       
        indice = len(movimentacao)
        movimentacoes = []

        for mov in movimentacao:
            data = mov.find("td").text.strip()
            date = datetime.strptime(data, '%j/%m/%Y').date().strftime('%Y-%m-%jT%H:%M:%S')
            descricao = mov.find("td").find_next("td").find_next("span").text.replace("\r\n","").strip()       
            nomeOriginal = mov.find("td").find_next("td").find_next("td").contents[0]  
            nomeOriginal= nomeOriginal.replace('\n\t','')
            nomeOriginal = nomeOriginal.strip()
            if descricao != '':
                movimentacoes.append({
                        "data": date,
                        "indice": indice,
                        "descricao":descricao.upper(),
                        "eMovimento":"true",
                        "nomeOriginal":[    nomeOriginal.upper()    ]
                })
            else:
                movimentacoes.append({
                    "data": date,
                    "indice": indice,
                    "eMovimento":"true",
                    "nomeOriginal":[    nomeOriginal.upper()    ]
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
            "titulo": assunto.upper(),

        })
        outrosAssuntos=soup.find("label",string="Outros assuntos:").parent.find_next_sibling("td").find("span").text.split(",")[0]
        assuntosCNJ.append({
            "titulo": outrosAssuntos.upper()

        })
        outrosAssuntos1=soup.find("label",string="Outros assuntos:").parent.find_next_sibling("td").find("span").text.split(",")[1]
        assuntosCNJ.append({
            "titulo": outrosAssuntos1.upper()

        })

        grauProcesso =" ".join(soup.find("h1",class_="esajTituloPagina").text.split()[-2:])

        orgaoJulgador = soup.find("label",string="Distribuição:").find_parent("tr").find_next_sibling("tr").text.strip().split("-")[0]

        unidadeOrigem = soup.find("label", string="Distribuição:").find_parent("tr").find_next_sibling("tr").text.strip().split("-")[1]

        classeProcedual = soup.find("label", string="Classe:").parent.find_next_sibling("td").text.strip()
      
        buscaData = soup.find("label", string="Distribuição:").parent.find_next_sibling("td").text.strip().split(" ")[0]
        dataDistribuicao = datetime.strptime(buscaData, '%j/%m/%Y').date().strftime('%Y-%m-%jT%H:%M:%S')

        statusObservacao = soup.find("label",string="Processo:").parent.find_next_sibling("td").find_all("span")[2].text.strip()
        
        numeroProcessoUnico=  soup.find("label",string="Processo:").parent.find_next_sibling("td").find_all("span")[0].text.strip()
        yield{
            "uf": "AL",
            "area":area.upper(),
            "juiz":juiz.upper(),
            "partes":partes,
            "sistema": "ESAJ-TJAL",
            "segmento": "JUSTICA ESTADUAL",
            "tribunal": "TJ-AL",
            "movimentos": movimentacoes,
            "valorCausa": valorCausa,
            "assuntosCNJ":assuntosCNJ,
            "urlProcesso":response.url,
            "grauProcesso":grauProcesso.upper(),
            "orgaoJulgador":orgaoJulgador.upper(),
            "unidadeOrigem":unidadeOrigem.upper(),
            "classeProcedual":{"nome":classeProcedual.upper()},
            "dataDistribuicao":dataDistribuicao,
            "eProcessoDigital": "true",
            "statusObservacao":statusObservacao.upper(),
            "numeroProcessoUnico": numeroProcessoUnico
        }



        
        
   
 
        