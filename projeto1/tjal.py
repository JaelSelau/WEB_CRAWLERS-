import scrapy
from bs4 import BeautifulSoup
from datetime import datetime
import tjalparser
import parser2


class tjAL_Spider(scrapy.Spider):

    name = "tjal"
    allowed_domains = "tjal.jus.br"

    def _init_(self, process=None, *args, **kwargs):
        super(tjAL_Spider, self)._init_(*args, **kwargs)

    def start_requests(self):
        start_url = "https://www2.tjal.jus.br/cpopg/open.do"
        yield scrapy.Request(url=start_url, callback=self.find_page, dont_filter=True)

    def find_page(self, response):
        try:
            response = response.url.replace(
                "open.do",
                f'search.do?conversationId=&dadosConsulta.localPesquisa.cdLocal=-1&cbPesquisa=NUMPROC&dadosConsulta.tipoNuProcesso=UNIFICADO&numeroDigitoAnoUnificado={self.process.split(".")[1][2]}&foroNumeroUnificado={self.process.split(".")[3]}&dadosConsulta.valorConsultaNuUnificado={self.process}&dadosConsulta.valorConsulta=&uuidCaptcha=',
            )
        except:
            print("Url is none!")
        yield scrapy.Request(
            url=response,
            callback=tjalparser.parse,
            dont_filter=True,
            headers=parser2.http,
        )
