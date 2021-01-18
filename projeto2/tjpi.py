import scrapy 
from bs4 import BeautifulSoup
from datetime import datetime

class tjpi_spider(scrapy.Spider):

    name= 'tjpi'
    allowed_domains = 'tjpi.pje.jus.br'
    
    
    def start_requests(self):
        start_url = 'https://tjpi.pje.jus.br/1g/ConsultaPublica/listView.seam'                                                                                                                                                                            
        yield scrapy.Request(url=start_url,callback=self.find_page, dont_filter= True)

    def find_page(self,response):
        try:
            response = response.url.replace('listView.seam', 'DetalheProcessoConsultaPublica/listView.seam?ca=d14c9df5acdd634c44cc590d639a7b231ea7a8292a12b8d5')
        except:
            print("Url is none!")
        http = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "Connection": "keep-alive",
            "Host": "tjpi.pje.jus.br",
            "Referer": "https://tjpi.pje.jus.br/1g/ConsultaPublica/listView.seam",
            "Upgrade-Insecure-Requests": 1,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
        }

        yield scrapy.Request(url=response,callback=self.parse,dont_filter= True,headers=http)
    def parse(self,response):
        try:
            soup = BeautifulSoup(response.text,"html.parser")
        except:
            print("Erro no parser dos dados!")

        partes = []

        cnpj = soup.find("span",id="j_id140:processoPartesPoloAtivoResumidoList:0:j_id287").find("div").text.strip().split(":")[1].split(" ")[1]
        nome = soup.find("span",id="j_id140:processoPartesPoloAtivoResumidoList:0:j_id287").find("div").text.strip().split("-")[0]
        polo = soup.find("span",id="j_id140:processoPartesPoloAtivoResumidoList:0:j_id311").find("div").text.strip()
        tipo = soup.find("span",class_="text-bold").text.split(" ")[6].replace("("," ").replace(")"," ").strip()
        partes.append({
            "cnpj": cnpj,
            "nome": nome,
            "polo": polo.upper(),
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
            date = datetime.strptime(data, '%j/%m/%Y %H:%M:%S ').date().strftime('%Y-%m-%jT%H:%M:%S')
            nomeOriginal = mov.find("span").text.split("-")[1]
            movimentos.append({
                "data": date,
                "indice": indice,
                "eMovimento": "true",
                "nomeOriginal":[    nomeOriginal.upper()    ]

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

        buscaData = soup.find("span",id="j_id140:processoTrfViewView:j_id158").find_all("div")[2].text.strip()
        dataDistribuicao = datetime.strptime(buscaData, '%j/%m/%Y').date().strftime('%Y-%m-%jT%H:%M:%S')
        
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
            "orgaoJulgador": orgaoJulgador.upper(),
            "unidadeOrigem": unidadeOrigem.upper(),
            "classeProcedual": classeProcedual,
            "dataDistribuicao": dataDistribuicao,
            "eProcessoDigital": "true",
            "numeroProcessoUnico": numeroProcessoUnico
        }
    

 