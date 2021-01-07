import scrapy 
from bs4 import BeautifulSoup

class tjpi_spider(scrapy.Spider):

    name= 'tjpi'
    allowed_domains = 'https://tjpi.pje.jus.br/1g/ConsultaPublica/DetalheProcessoConsultaPublica/listView.seam'
    
    
    def start_requests(self):
        start_url = 'https://tjpi.pje.jus.br/1g/ConsultaPublica/DetalheProcessoConsultaPublica/listView.seam?ca=54e9eb2ffeb3f2d804ffff5785fd8ddb1ea7a8292a12b8d5'                                                                                                                                                                            
        yield scrapy.Request(start_url,callback=self.parse)

    
    def parse(self,response):
        soup = BeautifulSoup(response.text,"html.parser")
        
        partes = []

        cnpj = soup.find("span",id="j_id140:processoPartesPoloAtivoResumidoList:0:j_id287").find("div").text.strip().split(":")[1].split(" ")[1]
        nome = soup.find("span",id="j_id140:processoPartesPoloAtivoResumidoList:0:j_id287").find("div").text.strip().split("-")[0]
        polo = soup.find("span",id="j_id140:processoPartesPoloAtivoResumidoList:0:j_id311").find("div").text.strip()
        tipo = soup.find("span",class_="text-bold").text.split(" ")[6].replace("("," ").replace(")"," ").strip()
        partes.append({
            "cnpj": cnpj,
            "nome": nome,
            "polo": polo,
            "tipo": tipo

        })

        parte = soup.find("tbody",id="j_id140:processoPartesPoloPassivoResumidoList:tb").find_all("tr",class_="rich-table-row")
        
        for par in parte:
                tipo = par.find("td",class_="rich-table-cell").find_next("div").find("span").parent.text.split("(")[1].replace(")"," ").strip()

                if tipo != 'ADVOGADO':
                    cpf = par.find("td",class_="rich-table-cell").find_next("div").find("span").parent.text.split(":")[1].split("(")[0].strip()
                    nome = par.find("td",class_="rich-table-cell").find_next("div").find("span").parent.text.split("-")[0].strip()
                    partes.append({
                    "cpf": cpf,
                    "nome": nome,
                    "polo": "PASSIVO",
                    "tipo": tipo
                })
                else:
                    cpf = par.find("td",class_="rich-table-cell").find_next("div").find("span").parent.text.split(":")[1].split("(")[0].strip()
                    nome = par.find("td",class_="rich-table-cell").find_next("div").find("span").parent.text.split("-")[0].strip()
                    numeroOAB =par.find("td",class_="rich-table-cell").find_next("div").find("span").parent.text.split("-")[1].split("I")[1].strip()
                    partes.append({
                            "cpf": cpf,
                            "oab":{
                            "uf":"PI",
                            "numero": numeroOAB
                        },
                        "nome": nome,
                        "tipo": tipo

                    })

        movimentos = []

        tam_indice = soup.find("tbody",id="j_id140:processoEvento:tb").find_all("span")
        indice = len(tam_indice)

        movimentacao = soup.find("tbody",id="j_id140:processoEvento:tb").find_all("div",class_="col-sm-12")

        for mov in movimentacao:

            data = mov.find("span").text.split("-")[0]
            nomeOriginal = mov.find("span").text.split("-")[1]
            movimentos.append({
                "data": data,
                "indice": indice,
                "eMovimento": "true",
                "nomeOriginal":[    nomeOriginal    ]

            })
            indice -=1
           
        assuntosCNJ = []

        titulo = soup.find("span",id="j_id140:processoTrfViewView:j_id180").find_all("div")[2].text.strip().split("(")[0]
        codigoCNJ = soup.find("span",id="j_id140:processoTrfViewView:j_id180").find_all("div")[2].text.split("(")[1].split(" ")[0].replace(")","").strip()
        assuntosCNJ.append({
            "titulo": titulo,
            "codigoCNJ": codigoCNJ
        })

        orgaoJulgador = soup.find("span",id="j_id140:processoTrfViewView:j_id217").find_all("div")[2].text.strip()

        unidadeOrigem = soup.find("span",id="j_id140:processoTrfViewView:j_id193").find_all("div")[2].text.strip()

        classeProcedual = []
        nome = soup.find("span",id="j_id140:processoTrfViewView:j_id169").find_all("div")[2].text.strip().split("(")[0]
        codigoCNJ = soup.find("span",id="j_id140:processoTrfViewView:j_id169").find_all("div")[2].text.split("(")[1].replace(")","").strip()
        classeProcedual.append({
            "nome": nome,
            "codigoCNJ":codigoCNJ

        })

        dataDistribuicao = soup.find("span",id="j_id140:processoTrfViewView:j_id158").find_all("div")[2].text.strip()

        numeroProcessoUnico = soup.find("div",class_="value col-sm-12").text.strip()

        yield{
            "uf": "PI",
            "partes:": partes,
            "sistema": "PJE-TJPI",
            "segmento": "JUSTICA ESTADUAL",
            "tribunal": "TJ-PI",
            "movimentos":movimentos,
            "assuntosCNJ": assuntosCNJ,
            "urlProcesso": response.url,
            "grauProcesso": "1",
            "orgaoJulgador": orgaoJulgador,
            "unidadeOrigem": unidadeOrigem,
            "classeProcedual": classeProcedual,
            "dataDistribuicao": dataDistribuicao,
            "numeroProcessoUnico": numeroProcessoUnico
        }
    

 