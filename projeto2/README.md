<h1> Teste de Admissão : Projeto 2 </h1>

<p> Este projeto refere ao teste admissional da empresa Predictus, e tem como objetivo a extração de dados da web 'TJ-PI', utilizando a linguagem python com a biblioteca Scrapy e BeautifulSoup4. </p>

<h2> Requisitos: </h2>

<ul> 
    <li>Python versão 3.8.1 ou superior. </li>
    <li>Biblioteca Scrapy 2.4.1 ou superior</li>
    <li>Biblioteca BeatifulSoup4</li>
</ul>

<h3>Input</h3>

<p> scrapy runspider tjpi.py -o tjpi.json </p>

<h3>Output</h3>

<p>[
  {
    "uf": "PI",
    "partes:": [
      {
        "cnpj": "05.805.924/0001-89",
        "nome": "MINISTÉRIO PÚBLICO ESTADUAL ",
        "polo": "Ativo",
        "tipo": "AUTOR"
      },
      {
        "cpf": "832.043.773-34",
        "nome": "GETULIO GOMES MACIEL",
        "polo": "PASSIVO",
        "tipo": "REU"
      },
      {
        "cpf": "927.580.103-72",
        "oab": {
          "uf": "PI",
          "numero": "5809"
        },
        "nome": "GRACIANE PIMENTEL DE SOUSA",
        "tipo": "ADVOGADO"
      },
      {
        "cpf": "989.763.463-00",
        "oab": {
          "uf": "PI",
          "numero": "11240"
        },
        "nome": "ANA PAULA LEITE DE SOUSA",
        "tipo": "ADVOGADO"
      },
      {
        "cpf": "18.519.123/0001-07",
        "nome": "ALCENOR LOPES MARTINS ME",
        "polo": "PASSIVO",
        "tipo": "REU"
      },
      {
        "cpf": "015.170.753-78",
        "oab": {
          "uf": "PI",
          "numero": "7946"
        },
        "nome": "FRANCISCO FELIPE SOUSA SANTOS",
        "tipo": "ADVOGADO"
      },
      {
        "cpf": "028.585.963-36",
        "oab": {
          "uf": "PI",
          "numero": "15653"
        },
        "nome": "LUCAS RAFAEL DE ALENCAR MOTA SILVA",
        "tipo": "ADVOGADO"
      },
      {
        "cpf": "622.704.273-00",
        "nome": "ALCENOR LOPES MARTINS",
        "polo": "PASSIVO",
        "tipo": "REU"
      },
      {
        "cpf": "015.170.753-78",
        "oab": {
          "uf": "PI",
          "numero": "7946"
        },
        "nome": "FRANCISCO FELIPE SOUSA SANTOS",
        "tipo": "ADVOGADO"
      },
      {
        "cpf": "028.585.963-36",
        "oab": {
          "uf": "PI",
          "numero": "15653"
        },
        "nome": "LUCAS RAFAEL DE ALENCAR MOTA SILVA",
        "tipo": "ADVOGADO"
      }
    ],
    "sistema": "PJE-TJPI",
    "segmento": "JUSTICA ESTADUAL",
    "tribunal": "TJ-PI",
    "movimentos": [
      {
        "data": "19/11/2020 10:25:59 ",
        "indice": 30,
        "eMovimento": "true",
        "nomeOriginal": [
          " Juntada de Petição de manifestação"
        ]
      },
      {
        "data": "19/11/2020 10:25:59 ",
        "indice": 29,
        "eMovimento": "true",
        "nomeOriginal": [
          " Juntada de Petição de manifestação"
        ]
      },
      {
        "data": "15/11/2020 03:50:40 ",
        "indice": 28,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS ME  "
        ]
      },
      {
        "data": "15/11/2020 03:50:40 ",
        "indice": 27,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS ME  "
        ]
      },
      {
        "data": "15/11/2020 03:50:40 ",
        "indice": 26,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS em 21/10/2020 23:59:59."
        ]
      },
      {
        "data": "15/11/2020 03:50:40 ",
        "indice": 25,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS em 21/10/2020 23:59:59."
        ]
      },
      {
        "data": "15/11/2020 03:50:40 ",
        "indice": 24,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de GETULIO GOMES MACIEL em 21/10/2020 23:59:59."
        ]
      },
      {
        "data": "15/11/2020 03:50:40 ",
        "indice": 23,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de GETULIO GOMES MACIEL em 21/10/2020 23:59:59."
        ]
      },
      {
        "data": "13/11/2020 01:34:53 ",
        "indice": 22,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS ME  "
        ]
      },
      {
        "data": "13/11/2020 01:34:53 ",
        "indice": 21,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS ME  "
        ]
      },
      {
        "data": "13/11/2020 01:34:53 ",
        "indice": 20,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de GETULIO GOMES MACIEL em 21/09/2020 23:59:59."
        ]
      },
      {
        "data": "13/11/2020 01:34:53 ",
        "indice": 19,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de GETULIO GOMES MACIEL em 21/09/2020 23:59:59."
        ]
      },
      {
        "data": "13/11/2020 01:34:53 ",
        "indice": 18,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS em 21/09/2020 23:59:59."
        ]
      },
      {
        "data": "13/11/2020 01:34:53 ",
        "indice": 17,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS em 21/09/2020 23:59:59."
        ]
      },
      {
        "data": "09/11/2020 00:19:25 ",
        "indice": 16,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de LUCIVALDO DE SOUSA MONTEIRO em 19/08/2020 23:59:59."
        ]
      },
      {
        "data": "09/11/2020 00:19:25 ",
        "indice": 15,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de LUCIVALDO DE SOUSA MONTEIRO em 19/08/2020 23:59:59."
        ]
      },
      {
        "data": "08/11/2020 05:48:26 ",
        "indice": 14,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS ME  "
        ]
      },
      {
        "data": "08/11/2020 05:48:26 ",
        "indice": 13,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS ME  "
        ]
      },
      {
        "data": "08/11/2020 05:48:26 ",
        "indice": 12,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de GETULIO GOMES MACIEL em 19/08/2020 23:59:59."
        ]
      },
      {
        "data": "08/11/2020 05:48:26 ",
        "indice": 11,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de GETULIO GOMES MACIEL em 19/08/2020 23:59:59."
        ]
      },
      {
        "data": "08/11/2020 05:48:20 ",
        "indice": 10,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS em 19/08/2020 23:59:59."
        ]
      },
      {
        "data": "08/11/2020 05:48:20 ",
        "indice": 9,
        "eMovimento": "true",
        "nomeOriginal": [
          " Decorrido prazo de ALCENOR LOPES MARTINS em 19/08/2020 23:59:59."
        ]
      },
      {
        "data": "03/11/2020 23:05:20 ",
        "indice": 8,
        "eMovimento": "true",
        "nomeOriginal": [
          " Expedição de Outros documentos."
        ]
      },
      {
        "data": "03/11/2020 23:05:20 ",
        "indice": 7,
        "eMovimento": "true",
        "nomeOriginal": [
          " Expedição de Outros documentos."
        ]
      },
      {
        "data": "21/10/2020 12:51:29 ",
        "indice": 6,
        "eMovimento": "true",
        "nomeOriginal": [
          " Audiência Instrução realizada para 21/10/2020 11:00 Vara Cível da Comarca de Valença do Piauí."
        ]
      },
      {
        "data": "21/10/2020 12:51:29 ",
        "indice": 5,
        "eMovimento": "true",
        "nomeOriginal": [
          " Audiência Instrução realizada para 21/10/2020 11:00 Vara Cível da Comarca de Valença do Piauí."
        ]
      },
      {
        "data": "02/10/2020 11:15:44 ",
        "indice": 4,
        "eMovimento": "true",
        "nomeOriginal": [
          " Juntada de Petição de manifestação"
        ]
      },
      {
        "data": "02/10/2020 11:15:44 ",
        "indice": 3,
        "eMovimento": "true",
        "nomeOriginal": [
          " Juntada de Petição de manifestação"
        ]
      },
      {
        "data": "02/10/2020 09:56:15 ",
        "indice": 2,
        "eMovimento": "true",
        "nomeOriginal": [
          " Audiência Instrução redesignada para 21/10/2020 11:00 Vara Cível da Comarca de Valença do Piauí."
        ]
      },
      {
        "data": "02/10/2020 09:56:15 ",
        "indice": 1,
        "eMovimento": "true",
        "nomeOriginal": [
          " Audiência Instrução redesignada para 21/10/2020 11:00 Vara Cível da Comarca de Valença do Piauí."
        ]
      }
    ],
    "assuntosCNJ": [
      {
        "titulo": "DIREITO ADMINISTRATIVO E OUTRAS MATÉRIAS DE DIREITO PÚBLICO ",
        "codigoCNJ": "9985"
      }
    ],
    "urlProcesso": "https://tjpi.pje.jus.br/1g/ConsultaPublica/DetalheProcessoConsultaPublica/listView.seam?ca=54e9eb2ffeb3f2d804ffff5785fd8ddb1ea7a8292a12b8d5",
    "grauProcesso": "1",
    "orgaoJulgador": "1ª Vara da Comarca de Valença do Piauí",
    "unidadeOrigem": "Comarca de Valença do Piauí",
    "classeProcedual": [
      {
        "nome": "AÇÃO CIVIL DE IMPROBIDADE ADMINISTRATIVA ",
        "codigoCNJ": "64"
      }
    ],
    "dataDistribuicao": "05/02/2020",
    "numeroProcessoUnico": "0000989-95.2017.8.18.0078"
  }
]
</p>