<h1> Teste de Admissão : Projeto 1 </h1>

<p> Este projeto refere ao teste admissional da empresa Predictus, e tem como objetivo a extração de dados da web 'TJ-AL', utilizando a linguagem python com a biblioteca Scrapy e BeautifulSoup4. </p>

<h2> Requisitos: </h2>

<ul> 
    <li>Python versão 3.8.1 ou superior. </li>
    <li>Biblioteca Scrapy 2.4.1 ou superior</li>
    <li>Biblioteca BeatifulSoup4</li>
</ul>

<h3>Input</h3>

<p> scrapy runspider tjal.py -o tjal.json </p>

<h3>Output</h3>

<p>[
  [
    {
      "uf": "AL",
      "area": "CÍVEL",
      "juiz": "JOSÉ CÍCERO ALVES DA SILVA",
      "partes": [
        {
          "nome": "MARIA EDITE DOS SANTOS",
          "tipo": "AUTORA",
          "Advogado(s)": [
            {
              "nome": "DEFENSORIA PÚBLICA DO ESTADO DE ALAGOAS",
              "tipo": "DEFENSOR P"
            }
          ]
        },
        {
          "nome": "HIPERCARD BANCO MULTIPLO S/A",
          "tipo": "RÉU",
          "Advogado(s)": [
            {
              "nome": "RAONI SOUZA DRUMMOND",
              "tipo": "ADVOGADO"
            },
            {
              "nome": "EDUARDO FRAGA",
              "tipo": "ADVOGADO"
            },
            {
              "nome": "ANDREA FREIRE TYNAN",
              "tipo": "ADVOGADO"
            }
          ]
        },
        {
          "nome": "W. DOS S. F.",
          "tipo": "TESTEMUNHA"
        },
        {
          "nome": "P. V. R. DE L.",
          "tipo": "TESTEMUNHA"
        }
      ],
      "sistema": "ESAJ-TJAL",
      "segmento": "JUSTICA ESTADUAL",
      "tribunal": "TJ-AL",
      "movimentos": [
        {
          "data": "2020-01-019T00:00:00",
          "indice": 89,
          "eMovimento": "true",
          "nomeOriginal": [
            "REMETIDO RECURSO ELETRÔNICO AO TRIBUNAL DE JUSTIÇA/TURMA DE RECURSO"
          ]
        },
        {
          "data": "2020-01-010T00:00:00",
          "indice": 88,
          "descricao": "Nº PROTOCOLO: WMAC.20.70030322-7TIPO DA PETIÇÃO: CONTRARRAZÕESDATA: 10/02/2020 18:44",
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2020-01-007T00:00:00",
          "indice": 87,
          "descricao": "RELAÇÃO :0009/2020DATA DA PUBLICAÇÃO: 08/01/2020NÚMERO DO DIÁRIO: 2501",
          "eMovimento": "true",
          "nomeOriginal": [
            "ATO PUBLICADO"
          ]
        },
        {
          "data": "2020-01-006T00:00:00",
          "indice": 86,
          "descricao": "RELAÇÃO: 0009/2020TEOR DO ATO: INTERPOSTO RECURSO DE APELAÇÃO PELA PARTE AUTORA, INTIME-SE A PARTE RECORRIDA PARA APRESENTAR CONTRARRAZÕES, NO PRAZO DE 15 (QUINZE) DIAS, CONFORME O ART. 1010,§ 1º DO CPC. SE APRESENTADA APELAÇÃO ADESIVA PELA PARTE RECORRIDA (ART.997, §2º DO CPC), INTIME-SE A PARTE CONTRÁRIA PARA CONTRARRAZÕES, NO PRAZO DE 15 (QUINZE) DIAS, NOS TERMOS DO ART. 1010, §2º DO CPC. CASO AS CONTRARRAZÕES DO RECURSO PRINCIPAL OU DO ADESIVO VENTILEM MATÉRIAS ELENCADAS NO ART.1009, §1º DO CPC, INTIME-SE O RECORRENTE PARA SE MANIFESTAR SOBRE ELAS NO PRAZO DE 15(QUINZE) DIAS, CONFORME O ART. 1009, § 2º, DO CPC. APÓS AS PROVIDÊNCIAS ACIMA, REMETAM-SE OS AUTOS AO EGRÉGIO TRIBUNAL DE JUSTIÇA. MACEIÓ, 06 DE JANEIRO DE 2020. SANDRA BUARQUE NUNES DE LIMA ANALISTAADVOGADOS(S): ANDREA FREIRE TYNAN (OAB 10699/BA), EDUARDO FRAGA (OAB 10658/BA), RAONI SOUZA DRUMMOND (OAB 10120A/AL)",
          "eMovimento": "true",
          "nomeOriginal": [
            "ENCAMINHADO AO DJ ELETRÔNICO"
          ]
        },
        {
          "data": "2020-01-006T00:00:00",
          "indice": 85,
          "descricao": "INTERPOSTO RECURSO DE APELAÇÃO PELA PARTE AUTORA, INTIME-SE A PARTE RECORRIDA PARA APRESENTAR CONTRARRAZÕES, NO PRAZO DE 15 (QUINZE) DIAS, CONFORME O ART. 1010,§ 1º DO CPC. SE APRESENTADA APELAÇÃO ADESIVA PELA PARTE RECORRIDA (ART.997, §2º DO CPC), INTIME-SE A PARTE CONTRÁRIA PARA CONTRARRAZÕES, NO PRAZO DE 15 (QUINZE) DIAS, NOS TERMOS DO ART. 1010, §2º DO CPC. CASO AS CONTRARRAZÕES DO RECURSO PRINCIPAL OU DO ADESIVO VENTILEM MATÉRIAS ELENCADAS NO ART.1009, §1º DO CPC, INTIME-SE O RECORRENTE PARA SE MANIFESTAR SOBRE ELAS NO PRAZO DE 15(QUINZE) DIAS, CONFORME O ART. 1009, § 2º, DO CPC. APÓS AS PROVIDÊNCIAS ACIMA, REMETAM-SE OS AUTOS AO EGRÉGIO TRIBUNAL DE JUSTIÇA. MACEIÓ, 06 DE JANEIRO DE 2020. SANDRA BUARQUE NUNES DE LIMA ANALISTAVENCIMENTO: 03/02/2020",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2019-01-012T00:00:00",
          "indice": 84,
          "descricao": "Nº PROTOCOLO: WMAC.19.70281888-5TIPO DA PETIÇÃO: RECURSO DE APELAÇÃODATA: 12/12/2019 10:32",
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2019-01-006T00:00:00",
          "indice": 83,
          "descricao": "CERTIDÃO DE INTIMAÇÃO - PORTAL ELETRÔNICO - DEFENSORIA PÚBLICA DO ESTADO DE ALAGOAS - DPEAL",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2019-01-026T00:00:00",
          "indice": 82,
          "descricao": "RELAÇÃO :0899/2019DATA DA PUBLICAÇÃO: 27/11/2019NÚMERO DO DIÁRIO: 2473",
          "eMovimento": "true",
          "nomeOriginal": [
            "ATO PUBLICADO"
          ]
        },
        {
          "data": "2019-01-026T00:00:00",
          "indice": 81,
          "descricao": "RELAÇÃO :0899/2019DATA DA PUBLICAÇÃO: 27/11/2019NÚMERO DO DIÁRIO: 2473",
          "eMovimento": "true",
          "nomeOriginal": [
            "ATO PUBLICADO"
          ]
        },
        {
          "data": "2019-01-025T00:00:00",
          "indice": 80,
          "eMovimento": "true",
          "nomeOriginal": [
            "VISTA À DEFENSORIA PÚBLICA - PORTAL ELETRÔNICO"
          ]
        },
        {
          "data": "2019-01-025T00:00:00",
          "indice": 79,
          "descricao": "CERTIDÃO DE REMESSA DE CITAÇÃO E INTIMAÇÃO PARA O PORTAL - DEFENSORIA PÚBLICA DO ESTADO DE ALAGOAS - DPEAL",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2019-01-025T00:00:00",
          "indice": 78,
          "descricao": "RELAÇÃO: 0899/2019TEOR DO ATO: ATO ORDINATÓRIO: EM CUMPRIMENTO AO PROVIMENTO Nº 13/2009, DA CORREGEDORIA-GERAL DA JUSTIÇA DO ESTADO DE ALAGOAS, DÊ-SE CIÊNCIA À DEFENSORIA PÚBLICA SOBRE A SENTENÇA PROFERIDA NOS PRESENTES AUTOS. MACEIÓ, 25 DE NOVEMBRO DE 2019. LOUISE MELO DA COSTA LEÃO ANALISTA JUDICIÁRIOADVOGADOS(S): ANDREA FREIRE TYNAN (OAB 10699/BA), EDUARDO FRAGA (OAB 10658/BA), RAONI SOUZA DRUMMOND (OAB 10120A/AL), DEFENSORIA PÚBLICA DO ESTADO DE ALAGOAS (OAB B/AL)",
          "eMovimento": "true",
          "nomeOriginal": [
            "ENCAMINHADO AO DJ ELETRÔNICO"
          ]
        },
        {
          "data": "2019-01-025T00:00:00",
          "indice": 77,
          "descricao": "RELAÇÃO: 0899/2019TEOR DO ATO: ANTE O EXPOSTO, JULGO IMPROCEDENTE O PEDIDO INICIAL, COM FUNDAMENTO NO ARTIGO 373, I DO CPC, RESOLVENDO O MÉRITO NOS TERMOS DO ART. 487, I, DO CPC. CONDENO OS AUTORES AO PAGAMENTO DAS DESPESAS PROCESSUAIS E HONORÁRIOS ADVOCATÍCIOS. CONSIDERANDO QUE O LOCAL DE PRESTAÇÃO DE SERVIÇOS NÃO APRESENTA ELEVADO CUSTO, QUE O GRAU DE ZELO DO PATRONO SE MOSTRA DENTRO DA NORMALIDADE, QUE A CAUSA NÃO APRESENTA GRANDE COMPLEXIDADE E QUE O VALOR ATUALIZADO DA CAUSA SE MOSTRA CAPAZ DE SERVIR COMO BASE DE CÁLCULO ADEQUADA PARA AS VERBAS SUCUMBENCIAIS, FIXO OS HONORÁRIOS ADVOCATÍCIOS EM 15% (DEZ POR CENTO) DO VALOR DA ATUALIZADO DA CAUSA (ART. 85, §2º, CPC), SUSPENSA A EXIGIBILIDADE, DIANTE DA GRATUIDADE DE JUSTIÇA DEFERIDA À PARTE AUTORA. PUBLIQUE-SE. REGISTRE-SE. INTIMEM-SE. TRANSITADO EM JULGADO E ENCAMINHADA CERTIDÃO DE CUSTAS AO FUNJURIS, ARQUIVE-SE COM A DEVIDA BAIXA. MACEIÓ,14 DE NOVEMBRO DE 2019. HENRIQUE GOMES DE BARROS TEIXEIRA JUIZ DE DIREITOADVOGADOS(S): ANDREA FREIRE TYNAN (OAB 10699/BA)",
          "eMovimento": "true",
          "nomeOriginal": [
            "ENCAMINHADO AO DJ ELETRÔNICO"
          ]
        },
        {
          "data": "2019-01-025T00:00:00",
          "indice": 76,
          "descricao": "ATO ORDINATÓRIO: EM CUMPRIMENTO AO PROVIMENTO Nº 13/2009, DA CORREGEDORIA-GERAL DA JUSTIÇA DO ESTADO DE ALAGOAS, DÊ-SE CIÊNCIA À DEFENSORIA PÚBLICA SOBRE A SENTENÇA PROFERIDA NOS PRESENTES AUTOS. MACEIÓ, 25 DE NOVEMBRO DE 2019. LOUISE MELO DA COSTA LEÃO ANALISTA JUDICIÁRIO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2019-01-025T00:00:00",
          "indice": 75,
          "eMovimento": "true",
          "nomeOriginal": [
            "REGISTRO DE SENTENÇA"
          ]
        },
        {
          "data": "2019-01-018T00:00:00",
          "indice": 74,
          "descricao": "ANTE O EXPOSTO, JULGO IMPROCEDENTE O PEDIDO INICIAL, COM FUNDAMENTO NO ARTIGO 373, I DO CPC, RESOLVENDO O MÉRITO NOS TERMOS DO ART. 487, I, DO CPC. CONDENO OS AUTORES AO PAGAMENTO DAS DESPESAS PROCESSUAIS E HONORÁRIOS ADVOCATÍCIOS. CONSIDERANDO QUE O LOCAL DE PRESTAÇÃO DE SERVIÇOS NÃO APRESENTA ELEVADO CUSTO, QUE O GRAU DE ZELO DO PATRONO SE MOSTRA DENTRO DA NORMALIDADE, QUE A CAUSA NÃO APRESENTA GRANDE COMPLEXIDADE E QUE O VALOR ATUALIZADO DA CAUSA SE MOSTRA CAPAZ DE SERVIR COMO BASE DE CÁLCULO ADEQUADA PARA AS VERBAS SUCUMBENCIAIS, FIXO OS HONORÁRIOS ADVOCATÍCIOS EM 15% (DEZ POR CENTO) DO VALOR DA ATUALIZADO DA CAUSA (ART. 85, §2º, CPC), SUSPENSA A EXIGIBILIDADE, DIANTE DA GRATUIDADE DE JUSTIÇA DEFERIDA À PARTE AUTORA. PUBLIQUE-SE. REGISTRE-SE. INTIMEM-SE. TRANSITADO EM JULGADO E ENCAMINHADA CERTIDÃO DE CUSTAS AO FUNJURIS, ARQUIVE-SE COM A DEVIDA BAIXA. MACEIÓ,14 DE NOVEMBRO DE 2019. HENRIQUE GOMES DE BARROS TEIXEIRA JUIZ DE DIREITO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-024T00:00:00",
          "indice": 73,
          "eMovimento": "true",
          "nomeOriginal": [
            "CONCLUSOS"
          ]
        },
        {
          "data": "2018-01-010T00:00:00",
          "indice": 72,
          "descricao": "DESPACHO VISTO EM CORREIÇÃO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-013T00:00:00",
          "indice": 71,
          "eMovimento": "true",
          "nomeOriginal": [
            "CONCLUSOS"
          ]
        },
        {
          "data": "2018-01-012T00:00:00",
          "indice": 70,
          "descricao": "CERTIDÃO DE IMPORTAÇÃO DE ARQUIVOS MULTIMÍDIA",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-012T00:00:00",
          "indice": 69,
          "descricao": "CERTIDÃO DE IMPORTAÇÃO DE ARQUIVOS MULTIMÍDIA",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-012T00:00:00",
          "indice": 68,
          "eMovimento": "true",
          "nomeOriginal": [
            "AUDIÊNCIA REALIZADA"
          ]
        },
        {
          "data": "2018-01-023T00:00:00",
          "indice": 67,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE MANDADO"
          ]
        },
        {
          "data": "2018-01-023T00:00:00",
          "indice": 66,
          "descricao": ".CM - ATO POSITIVO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-023T00:00:00",
          "indice": 65,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE MANDADO"
          ]
        },
        {
          "data": "2018-01-023T00:00:00",
          "indice": 64,
          "descricao": ".CM - ATO POSITIVO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-019T00:00:00",
          "indice": 63,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE MANDADO"
          ]
        },
        {
          "data": "2018-01-019T00:00:00",
          "indice": 62,
          "descricao": ".CM - ATO POSITIVO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-011T00:00:00",
          "indice": 61,
          "descricao": "OCORREU O RECEBIMENTO DE UM MANDADO PELA CENTRAL DE MANDADOS.",
          "eMovimento": "true",
          "nomeOriginal": [
            "MANDADO RECEBIDO NA CENTRAL DE MANDADOS"
          ]
        },
        {
          "data": "2018-01-011T00:00:00",
          "indice": 60,
          "descricao": "MANDADO Nº: 001.2018/029832-2 SITUAÇÃO: CUMPRIDO - ATO POSITIVO EM 23/04/2018 LOCAL: OFICIAL DE JUSTIÇA - KARINA NOBRE DE ARAÚJO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-011T00:00:00",
          "indice": 59,
          "descricao": "OCORREU O RECEBIMENTO DE UM MANDADO PELA CENTRAL DE MANDADOS.",
          "eMovimento": "true",
          "nomeOriginal": [
            "MANDADO RECEBIDO NA CENTRAL DE MANDADOS"
          ]
        },
        {
          "data": "2018-01-011T00:00:00",
          "indice": 58,
          "descricao": "MANDADO Nº: 001.2018/029829-2 SITUAÇÃO: CUMPRIDO - ATO POSITIVO EM 23/04/2018 LOCAL: OFICIAL DE JUSTIÇA - KARINA NOBRE DE ARAÚJO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-011T00:00:00",
          "indice": 57,
          "descricao": "OCORREU O RECEBIMENTO DE UM MANDADO PELA CENTRAL DE MANDADOS.",
          "eMovimento": "true",
          "nomeOriginal": [
            "MANDADO RECEBIDO NA CENTRAL DE MANDADOS"
          ]
        },
        {
          "data": "2018-01-011T00:00:00",
          "indice": 56,
          "descricao": "MANDADO Nº: 001.2018/029819-5 SITUAÇÃO: CUMPRIDO - ATO POSITIVO EM 19/04/2018 LOCAL: OFICIAL DE JUSTIÇA - MOACIRA MARIA FERREIRA LIMA",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-026T00:00:00",
          "indice": 55,
          "descricao": "CERTIDÃO DE INTIMAÇÃO - PORTAL ELETRÔNICO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-023T00:00:00",
          "indice": 54,
          "descricao": "Nº PROTOCOLO: WMAC.18.70056501-6TIPO DA PETIÇÃO: MANIFESTAÇÃO DO DEFENSOR PÚBLICODATA: 23/03/2018 15:30",
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2018-01-015T00:00:00",
          "indice": 53,
          "descricao": "RELAÇÃO :0086/2018DATA DA PUBLICAÇÃO: 16/03/2018NÚMERO DO DIÁRIO: 2065",
          "eMovimento": "true",
          "nomeOriginal": [
            "ATO PUBLICADO"
          ]
        },
        {
          "data": "2018-01-015T00:00:00",
          "indice": 52,
          "descricao": "RELAÇÃO :0084/2018DATA DA PUBLICAÇÃO: 16/03/2018NÚMERO DO DIÁRIO: 2065",
          "eMovimento": "true",
          "nomeOriginal": [
            "ATO PUBLICADO"
          ]
        },
        {
          "data": "2018-01-014T00:00:00",
          "indice": 51,
          "descricao": "RELAÇÃO: 0086/2018TEOR DO ATO: EM CUMPRIMENTO AO PROVIMENTO Nº 13/2009, DA CORREGEDORIA-GERAL DA JUSTIÇA DO ESTADO DE ALAGOAS, ABRO VISTA A DEFENSORIA PÚBLICA DA DATA DA AUDIÊNCIA DESIGNADA NOS PRESENTE AUTOS.MACEIÓ, 14 DE MARÇO DE 2018SANDRA DE LIMA BUARQUEANALISTAADVOGADOS(S): ANDREA FREIRE TYNAN (OAB 10699/BA), EDUARDO FRAGA (OAB 10658/BA), RAONI SOUZA DRUMMOND (OAB 10120A/AL), DEFENSORIA PÚBLICA DO ESTADO DE ALAGOAS (OAB B/AL)",
          "eMovimento": "true",
          "nomeOriginal": [
            "ENCAMINHADO AO DJ ELETRÔNICO"
          ]
        },
        {
          "data": "2018-01-014T00:00:00",
          "indice": 50,
          "eMovimento": "true",
          "nomeOriginal": [
            "VISTA À DEFENSORIA PÚBLICA - PORTAL ELETRÔNICO"
          ]
        },
        {
          "data": "2018-01-014T00:00:00",
          "indice": 49,
          "descricao": "CERTIDÃO DE REMESSA DE CITAÇÃO E INTIMAÇÃO PARA O PORTAL",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-014T00:00:00",
          "indice": 48,
          "descricao": "EM CUMPRIMENTO AO PROVIMENTO Nº 13/2009, DA CORREGEDORIA-GERAL DA JUSTIÇA DO ESTADO DE ALAGOAS, ABRO VISTA A DEFENSORIA PÚBLICA DA DATA DA AUDIÊNCIA DESIGNADA NOS PRESENTE AUTOS.MACEIÓ, 14 DE MARÇO DE 2018SANDRA DE LIMA BUARQUEANALISTA",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-014T00:00:00",
          "indice": 47,
          "descricao": "RELAÇÃO: 0084/2018TEOR DO ATO: AUTOS Nº 0731425-82.2014.8.02.0001 AÇÃO: PROCEDIMENTO ORDINÁRIO AUTOR: MARIA EDITE DOS SANTOS RÉU: HIPERCARD BANCO MULTIPLO S/A CERTIDÃO DE DESIGNAÇÃO DE AUDIÊNCIACERTIFICO QUE FOI DESIGNADO O PRÓXIMO DIA 12/06/2018, ÀS 16:30H, PARA REALIZAÇÃO DE AUDIÊNCIA INSTRUÇÃO E JULGAMENTO, CONFORME DETERMINAÇÃO DO MM. JUIZ DE DIREITOO REFERIDO É VERDADE, DO QUE DOU FÉ.MACEIÓ, 06 DE MARÇO DE 2018.JOZINETE SANTOS GONÇALVES MELO CHEFE DE SECRETARIA JUDICIALADVOGADOS(S): ANDREA FREIRE TYNAN (OAB 10699/BA), EDUARDO FRAGA (OAB 10658/BA), RAONI SOUZA DRUMMOND (OAB 10120A/AL), DEFENSORIA PÚBLICA DO ESTADO DE ALAGOAS (OAB B/AL)",
          "eMovimento": "true",
          "nomeOriginal": [
            "ENCAMINHADO AO DJ ELETRÔNICO"
          ]
        },
        {
          "data": "2018-01-006T00:00:00",
          "indice": 46,
          "descricao": "AUTOS Nº 0731425-82.2014.8.02.0001 AÇÃO: PROCEDIMENTO ORDINÁRIO AUTOR: MARIA EDITE DOS SANTOS RÉU: HIPERCARD BANCO MULTIPLO S/A CERTIDÃO DE DESIGNAÇÃO DE AUDIÊNCIACERTIFICO QUE FOI DESIGNADO O PRÓXIMO DIA 12/06/2018, ÀS 16:30H, PARA REALIZAÇÃO DE AUDIÊNCIA INSTRUÇÃO E JULGAMENTO, CONFORME DETERMINAÇÃO DO MM. JUIZ DE DIREITOO REFERIDO É VERDADE, DO QUE DOU FÉ.MACEIÓ, 06 DE MARÇO DE 2018.JOZINETE SANTOS GONÇALVES MELO CHEFE DE SECRETARIA JUDICIAL",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2018-01-006T00:00:00",
          "indice": 45,
          "descricao": "INSTRUÇÃO E JULGAMENTODATA: 12/06/2018 HORA 16:30LOCAL: SALA DE AUDIÊNCIASITUACÃO: REALIZADA",
          "eMovimento": "true",
          "nomeOriginal": [
            "AUDIÊNCIA DESIGNADA"
          ]
        },
        {
          "data": "2018-01-005T00:00:00",
          "indice": 44,
          "descricao": "AÇÃO: PROCEDIMENTO ORDINÁRIO AUTOR: MARIA EDITE DOS SANTOS RÉU: HIPERCARD BANCO MULTIPLO S/A CERTIDÃO DE DESIGNAÇÃO DE AUDIÊNCIACERTIFICO QUE FOI DESIGNADO O PRÓXIMO DIA 18/07/2018, ÀS 15:30H, PARA REALIZAÇÃO DE AUDIÊNCIA INSTRUÇÃO E JULGAMENTO, CONFORME DETERMINAÇÃO DO MM. JUIZ DE DIREITO .O REFERIDO É VERDADE, DO QUE DOU FÉ.MACEIÓ, 05 DE MARÇO DE 2018.JOZINETE SANTOS GONÇALVES MELO CHEFE DE SECRETARIA JUDICIAL",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2017-01-001T00:00:00",
          "indice": 43,
          "descricao": "DESPACHO VISTO EM CORREIÇÃO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2017-01-017T00:00:00",
          "indice": 42,
          "descricao": "DESPACHO GENÉRICO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2017-01-020T00:00:00",
          "indice": 41,
          "descricao": "Nº PROTOCOLO: WMAC.17.70086607-4TIPO DA PETIÇÃO: PEDIDO DE JUNTADA DE DOCUMENTO(S)DATA: 20/06/2017 15:39",
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2017-01-012T00:00:00",
          "indice": 40,
          "descricao": "RELAÇÃO :0180/2017DATA DA DISPONIBILIZAÇÃO: 12/06/2017DATA DA PUBLICAÇÃO: 13/06/2017NÚMERO DO DIÁRIO: 1883PÁGINA: 14/17",
          "eMovimento": "true",
          "nomeOriginal": [
            "ATO PUBLICADO"
          ]
        },
        {
          "data": "2017-01-009T00:00:00",
          "indice": 39,
          "descricao": "RELAÇÃO: 0180/2017TEOR DO ATO: DESPACHO 1.COMPULSANDO-SE OS AUTOS, APÓS UMA ANÁLISE DO ESTADO PROCESSUAL, DETERMINO A INTIMAÇÃO DAS PARTES, EM PRAZO COMUM DE CINCO DIAS, PARA, QUERENDO, MANIFESTAREM-SE ACERCA DAS PROVAS QUE PRETENDEM PRODUZIR, ALÉM DAS JÁ EXISTENTES NOS AUTOS. 2.CASO HAJA INTENÇÃO DE PRODUZIR PROVA TESTEMUNHAL, QUE APRESENTEM O ROL DE TESTEMUNHAS E NOTICIEM SE ELAS COMPARECERÃO AO ATO INDEPENDENTEMENTE DE INTIMAÇÃO.3.CUMPRA-SE. DÊ-SE CIÊNCIA. MACEIÓ(AL), 17 DE MAIO DE 2017.HENRIQUE GOMES DE BARROS TEIXEIRA JUIZ DE DIREITOADVOGADOS(S): EDUARDO FRAGA (OAB 10658/BA), RAONI SOUZA DRUMMOND (OAB 10120A/AL)",
          "eMovimento": "true",
          "nomeOriginal": [
            "ENCAMINHADO AO DJ ELETRÔNICO"
          ]
        },
        {
          "data": "2017-01-006T00:00:00",
          "indice": 38,
          "eMovimento": "true",
          "nomeOriginal": [
            "CONCLUSOS"
          ]
        },
        {
          "data": "2017-01-006T00:00:00",
          "indice": 37,
          "descricao": "Nº PROTOCOLO: WMAC.17.70078950-9TIPO DA PETIÇÃO: ROL DE TESTEMUNHASDATA: 06/06/2017 13:07",
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2017-01-001T00:00:00",
          "indice": 36,
          "descricao": "CERTIDÃO DE INTIMAÇÃO - PORTAL ELETRÔNICO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2017-01-019T00:00:00",
          "indice": 35,
          "eMovimento": "true",
          "nomeOriginal": [
            "VISTA À DEFENSORIA PÚBLICA - PORTAL ELETRÔNICO"
          ]
        },
        {
          "data": "2017-01-019T00:00:00",
          "indice": 34,
          "descricao": "CERTIDÃO DE REMESSA DE CITAÇÃO E INTIMAÇÃO PARA O PORTAL",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2017-01-019T00:00:00",
          "indice": 33,
          "descricao": "DESPACHO 1.COMPULSANDO-SE OS AUTOS, APÓS UMA ANÁLISE DO ESTADO PROCESSUAL, DETERMINO A INTIMAÇÃO DAS PARTES, EM PRAZO COMUM DE CINCO DIAS, PARA, QUERENDO, MANIFESTAREM-SE ACERCA DAS PROVAS QUE PRETENDEM PRODUZIR, ALÉM DAS JÁ EXISTENTES NOS AUTOS. 2.CASO HAJA INTENÇÃO DE PRODUZIR PROVA TESTEMUNHAL, QUE APRESENTEM O ROL DE TESTEMUNHAS E NOTICIEM SE ELAS COMPARECERÃO AO ATO INDEPENDENTEMENTE DE INTIMAÇÃO.3.CUMPRA-SE. DÊ-SE CIÊNCIA. MACEIÓ(AL), 17 DE MAIO DE 2017.HENRIQUE GOMES DE BARROS TEIXEIRA JUIZ DE DIREITO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2016-01-005T00:00:00",
          "indice": 32,
          "eMovimento": "true",
          "nomeOriginal": [
            "CONCLUSOS"
          ]
        },
        {
          "data": "2016-01-028T00:00:00",
          "indice": 31,
          "descricao": "DECISÕES INTERLOCUTÓRIAS - GENÉRICO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2016-01-015T00:00:00",
          "indice": 30,
          "eMovimento": "true",
          "nomeOriginal": [
            "CONCLUSOS"
          ]
        },
        {
          "data": "2016-01-008T00:00:00",
          "indice": 29,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2016-01-008T00:00:00",
          "indice": 28,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2016-01-008T00:00:00",
          "indice": 27,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2016-01-023T00:00:00",
          "indice": 26,
          "descricao": "CERTIDÃO DO OFICIAL DE JUSTIÇA",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2016-01-018T00:00:00",
          "indice": 25,
          "descricao": "CERTIDÃO DO OFICIAL DE JUSTIÇA",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2016-01-027T00:00:00",
          "indice": 24,
          "descricao": "ASSENTADA",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2016-01-006T00:00:00",
          "indice": 23,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE MANDADO"
          ]
        },
        {
          "data": "2015-01-018T00:00:00",
          "indice": 22,
          "descricao": "RELAÇÃO :0550/2015DATA DA DISPONIBILIZAÇÃO: 17/11/2015DATA DA PUBLICAÇÃO: 18/11/2015NÚMERO DO DIÁRIO: ED.1514PÁGINA: 78",
          "eMovimento": "true",
          "nomeOriginal": [
            "ATO PUBLICADO"
          ]
        },
        {
          "data": "2015-01-017T00:00:00",
          "indice": 21,
          "descricao": "RELAÇÃO: 0550/2015TEOR DO ATO: EM CUMPRIMENTO AO PROVIMENTO Nº 13/2009 DA CGJ, FICA DESIGNADA AUDIÊNCIA DE TENTATIVA DE CONCILIAÇÃO PARA O DIA 26 DE JANEIRO DE 2016 ÀS 15H30MIN NESTE CENTRO JUDICIÁRIO - CJUS PROCESSUAL (SALA 301, 3º ANDAR DO FÓRUM DO BARRO DURO). INTIMAÇÕES NECESSÁRIAS.ADVOGADOS(S): EDUARDO FRAGA (OAB 10658/BA), RAONI SOUZA DRUMMOND (OAB 10120AA/L)",
          "eMovimento": "true",
          "nomeOriginal": [
            "ENCAMINHADO AO DJ ELETRÔNICO"
          ]
        },
        {
          "data": "2015-01-016T00:00:00",
          "indice": 20,
          "descricao": "MANDADO Nº: 001.2015/078735-0 SITUAÇÃO: CUMPRIDO - ATO POSITIVO EM 08/03/2016 LOCAL: CENTRO DE SOLUÇÃO DE CONFLITOS JUDICIÁRIOS-CJUS",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2015-01-011T00:00:00",
          "indice": 19,
          "descricao": "EM CUMPRIMENTO AO PROVIMENTO Nº 13/2009 DA CGJ, FICA DESIGNADA AUDIÊNCIA DE TENTATIVA DE CONCILIAÇÃO PARA O DIA 26 DE JANEIRO DE 2016 ÀS 15H30MIN NESTE CENTRO JUDICIÁRIO - CJUS PROCESSUAL (SALA 301, 3º ANDAR DO FÓRUM DO BARRO DURO). INTIMAÇÕES NECESSÁRIAS.",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2015-01-011T00:00:00",
          "indice": 18,
          "descricao": "CONCILIAÇÃODATA: 26/01/2016 HORA 15:30LOCAL: SALA DE AUDIÊNCIA - GABINETESITUACÃO: REALIZADA",
          "eMovimento": "true",
          "nomeOriginal": [
            "AUDIÊNCIA DESIGNADA"
          ]
        },
        {
          "data": "2015-01-028T00:00:00",
          "indice": 17,
          "eMovimento": "true",
          "nomeOriginal": [
            "PROCESSO RECEBIDO PELO CJUS"
          ]
        },
        {
          "data": "2015-01-028T00:00:00",
          "indice": 16,
          "eMovimento": "true",
          "nomeOriginal": [
            "PROCESSO ENCAMINHADO PARA CJUS"
          ]
        },
        {
          "data": "2015-01-023T00:00:00",
          "indice": 15,
          "descricao": "CERTIDÃO DE IMPORTAÇÃO DE ARQUIVOS MULTIMÍDIA",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2015-01-023T00:00:00",
          "indice": 14,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE PETIÇÃO"
          ]
        },
        {
          "data": "2015-01-008T00:00:00",
          "indice": 13,
          "eMovimento": "true",
          "nomeOriginal": [
            "CONCLUSOS"
          ]
        },
        {
          "data": "2015-01-008T00:00:00",
          "indice": 12,
          "descricao": "Nº PROTOCOLO: WMAC.15.70101535-1TIPO DA PETIÇÃO: RÉPLICADATA: 07/09/2015 20:06",
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2015-01-024T00:00:00",
          "indice": 11,
          "descricao": "RELAÇÃO :0141/2015DATA DA DISPONIBILIZAÇÃO: 24/08/2015DATA DA PUBLICAÇÃO: 25/08/2015NÚMERO DO DIÁRIO: 1457PÁGINA: 15/19",
          "eMovimento": "true",
          "nomeOriginal": [
            "ATO PUBLICADO"
          ]
        },
        {
          "data": "2015-01-021T00:00:00",
          "indice": 10,
          "descricao": "RELAÇÃO: 0141/2015TEOR DO ATO: EM CUMPRIMENTO AO PROVIMENTO Nº 13/2009, DA CORREGEDORIA-GERAL DA JUSTIÇA DO ESTADO DE ALAGOAS, MANIFESTE-SE A PARTE AUTORA SOBRE A CONTESTAÇÃO E DOCUMENTOS ACOSTADOS, QUERENDO, EM 10 (DEZ) DIAS. MACEIÓ, 09 DE JUNHO DE 2015. SANDRA DE LIMA BUARQUE ANALISTA JUDICIÁRIOADVOGADOS(S): RAONI SOUZA DRUMMOND (OAB 10120AA/L), LUCIANA MARTINS DE FARO (OAB 6804B/AL)",
          "eMovimento": "true",
          "nomeOriginal": [
            "ENCAMINHADO AO DJ ELETRÔNICO"
          ]
        },
        {
          "data": "2015-01-020T00:00:00",
          "indice": 9,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2015-01-016T00:00:00",
          "indice": 8,
          "descricao": "GENÉRICO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2015-01-016T00:00:00",
          "indice": 7,
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTO"
          ]
        },
        {
          "data": "2015-01-009T00:00:00",
          "indice": 6,
          "descricao": "EM CUMPRIMENTO AO PROVIMENTO Nº 13/2009, DA CORREGEDORIA-GERAL DA JUSTIÇA DO ESTADO DE ALAGOAS, MANIFESTE-SE A PARTE AUTORA SOBRE A CONTESTAÇÃO E DOCUMENTOS ACOSTADOS, QUERENDO, EM 10 (DEZ) DIAS. MACEIÓ, 09 DE JUNHO DE 2015. SANDRA DE LIMA BUARQUE ANALISTA JUDICIÁRIO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2015-01-009T00:00:00",
          "indice": 5,
          "descricao": "Nº PROTOCOLO: WMAC.15.70065611-6TIPO DA PETIÇÃO: CONTESTAÇÃODATA: 09/06/2015 13:50",
          "eMovimento": "true",
          "nomeOriginal": [
            "JUNTADA DE DOCUMENTOS"
          ]
        },
        {
          "data": "2015-01-022T00:00:00",
          "indice": 4,
          "descricao": "CITAÇÃO POR CARTA RITO ORDINÁRIO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2015-01-016T00:00:00",
          "indice": 3,
          "descricao": "1NO MOMENTO DEIXO DE APRECIAR O PEDIDO DE ANTECIPAÇÃO DE TUTELA, SENDO IMPRESCINDÍVEL A CHAMADA DA PARTE REQUERIDA AOS AUTOS (CITAÇÃO), PARA UM BOM DESENROLAR DA MARCHA PROCESSUAL. 2. CITE-SE O RÉU, ATRAVÉS DE SEU REPRESENTANTE LEGAL PARA, QUERENDO, CONTESTAR O TERMOS DO PEDIDO, NO PRAZO DE 15 (QUINZE) DIAS, ADVERTINDO-A DOS EFEITOS DA REVELIA. 3. CUMPRA-SE. MACEIÓ(AL), 13 DE ABRIL DE 2015. HENRIQUE GOMES DE BARROS TEIXEIRA JUIZ DE DIREITO",
          "eMovimento": "true",
          "nomeOriginal": [
            ""
          ]
        },
        {
          "data": "2014-01-024T00:00:00",
          "indice": 2,
          "eMovimento": "true",
          "nomeOriginal": [
            "CONCLUSOS"
          ]
        },
        {
          "data": "2014-01-024T00:00:00",
          "indice": 1,
          "eMovimento": "true",
          "nomeOriginal": [
            "DISTRIBUÍDO POR SORTEIO"
          ]
        }
      ],
      "valorCausa": [
        {
          "moeda": "R$",
          "valor": "15.000,00"
        }
      ],
      "assuntosCNJ": [
        {
          "titulo": "CARTÃO DE CRÉDITO"
        },
        {
          "titulo": "DANO MORAL"
        },
        {
          "titulo": "INCLUSÃO INDEVIDA EM CADASTRO DE INADIMPLENTES"
        }
      ],
      "urlProcesso": "https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=01000I1FT0000&processo.foro=1&processo.numero=0731425-82.2014.8.02.0001&uuidCaptcha=sajcaptcha_6f3323ec4c8147b2909997d567cc7b92",
      "grauProcesso": "1º GRAU",
      "orgaoJulgador": "3ª VARA CÍVEL DA CAPITAL ",
      "unidadeOrigem": " FORO DE MACEIÓ",
      "classeProcedual": {
        "nome": "PROCEDIMENTO COMUM CÍVEL"
      },
      "dataDistribuicao": "2016-01-009T00:00:00",
      "eProcessoDigital": "true",
      "statusObservacao": "EM GRAU DE RECURSO",
      "numeroProcessoUnico": "0731425-82.2014.8.02.0001"
    }
  ] </p>