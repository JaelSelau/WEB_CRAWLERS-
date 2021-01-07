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

<p> [
  {
    "uf": "AL",
    "area": "Área: Cível",
    "juiz": "Henrique Gomes de Barros Teixeira",
    "partes": [
      {
        "nome": "Maria Edite dos Santos\n\t\t\t\t\n\t\t\t\n\n\t\t\t\n\t\t  \n\t\t\t\nDefensor P: \n\t\t\tDefensoria Pública do Estado de Alagoas",
        "tipo": "Autora:"
      },
      {
        "nome": "Hipercard Banco Multiplo S/A\n\t\t\t\t\n\t\t\t\n\n\t\t\t\n\t\t  \n\t\t\t\nAdvogado: \n\t\t\tRaoni Souza Drummond \n   \t \t\n\t\t\n\t\t\t\nAdvogado: \n\t\t\tEduardo Fraga \n   \t \t\n\t\t\n\t\t\t\nAdvogada: \n\t\t\tAndrea Freire Tynan",
        "tipo": "Réu:"
      },
      {
        "nome": "W. dos S. F.",
        "tipo": "Testemunha:"
      },
      {
        "nome": "P. V. R. de L.",
        "tipo": "Testemunha:"
      }
    ],
    "sistema": "ESAJ-TJAL",
    "segmento": "JUSTICA ESTADUAL",
    "tribunal": "TJ-AL",
    "movimentos": [
      {
        "data": "19/02/2020",
        "indice": 89,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Remetido recurso eletrônico ao Tribunal de Justiça/Turma de recurso"
        ]
      },
      {
        "data": "10/02/2020",
        "indice": 88,
        "descricao": "Nº Protocolo: WMAC.20.70030322-7\r\nTipo da Petição: Contrarrazões\r\nData: 10/02/2020 18:44",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "07/01/2020",
        "indice": 87,
        "descricao": "Relação :0009/2020\r\nData da Publicação: 08/01/2020\r\nNúmero do Diário: 2501",
        "eMovimento": "true",
        "nomeOriginal": [
          "Ato Publicado"
        ]
      },
      {
        "data": "06/01/2020",
        "indice": 86,
        "descricao": "Relação: 0009/2020\r\nTeor do ato: Interposto recurso de apelação pela parte autora, intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 06 de janeiro de 2020. Sandra Buarque Nunes de Lima Analista\r\nAdvogados(s): Andrea Freire Tynan (OAB 10699/BA), Eduardo Fraga (OAB 10658/BA), Raoni Souza Drummond (OAB 10120A/AL)",
        "eMovimento": "true",
        "nomeOriginal": [
          "Encaminhado ao DJ Eletrônico"
        ]
      },
      {
        "data": "06/01/2020",
        "indice": 85,
        "descricao": "Interposto recurso de apelação pela parte autora, intime-se a parte recorrida para apresentar contrarrazões, no prazo de 15 (quinze) dias, conforme o art. 1010,§ 1º do CPC. Se apresentada Apelação Adesiva pela parte recorrida (art.997, §2º do CPC), intime-se a parte contrária para contrarrazões, no prazo de 15 (quinze) dias, nos termos do Art. 1010, §2º do CPC. Caso as contrarrazões do recurso principal ou do adesivo ventilem matérias elencadas no art.1009, §1º do CPC, intime-se o recorrente para se manifestar sobre elas no prazo de 15(quinze) dias, conforme o art. 1009, § 2º, do CPC. Após as providências acima, remetam-se os autos ao Egrégio Tribunal de Justiça. Maceió, 06 de janeiro de 2020. Sandra Buarque Nunes de Lima AnalistaVencimento: 03/02/2020",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "12/12/2019",
        "indice": 84,
        "descricao": "Nº Protocolo: WMAC.19.70281888-5\r\nTipo da Petição: Recurso de Apelação\r\nData: 12/12/2019 10:32",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "06/12/2019",
        "indice": 83,
        "descricao": "Certidão de Intimação - Portal Eletrônico - Defensoria Pública do Estado de Alagoas - DPEAL",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "26/11/2019",
        "indice": 82,
        "descricao": "Relação :0899/2019\r\nData da Publicação: 27/11/2019\r\nNúmero do Diário: 2473",
        "eMovimento": "true",
        "nomeOriginal": [
          "Ato Publicado"
        ]
      },
      {
        "data": "26/11/2019",
        "indice": 81,
        "descricao": "Relação :0899/2019\r\nData da Publicação: 27/11/2019\r\nNúmero do Diário: 2473",
        "eMovimento": "true",
        "nomeOriginal": [
          "Ato Publicado"
        ]
      },
      {
        "data": "25/11/2019",
        "indice": 80,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Vista à Defensoria Pública - Portal Eletrônico"
        ]
      },
      {
        "data": "25/11/2019",
        "indice": 79,
        "descricao": "Certidão de Remessa de Citação e Intimação para o Portal - Defensoria Pública do Estado de Alagoas - DPEAL",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "25/11/2019",
        "indice": 78,
        "descricao": "Relação: 0899/2019\r\nTeor do ato: Ato Ordinatório: Em cumprimento ao Provimento nº 13/2009, da Corregedoria-Geral da Justiça do Estado de Alagoas, dê-se ciência à Defensoria Pública sobre a sentença proferida nos presentes autos. Maceió, 25 de novembro de 2019. Louise Melo da Costa Leão Analista Judiciário\r\nAdvogados(s): Andrea Freire Tynan (OAB 10699/BA), Eduardo Fraga (OAB 10658/BA), Raoni Souza Drummond (OAB 10120A/AL), Defensoria Pública do Estado de Alagoas (OAB B/AL)",
        "eMovimento": "true",
        "nomeOriginal": [
          "Encaminhado ao DJ Eletrônico"
        ]
      },
      {
        "data": "25/11/2019",
        "indice": 77,
        "descricao": "Relação: 0899/2019\r\nTeor do ato: Ante o exposto, JULGO IMPROCEDENTE O PEDIDO INICIAL, com fundamento no artigo 373, I do CPC, resolvendo o mérito nos termos do art. 487, I, do CPC. Condeno os autores ao pagamento das despesas processuais e honorários advocatícios. Considerando que o local de prestação de serviços não apresenta elevado custo, que o grau de zelo do patrono se mostra dentro da normalidade, que a causa não apresenta grande complexidade e que o valor atualizado da causa se mostra capaz de servir como base de cálculo adequada para as verbas sucumbenciais, fixo os honorários advocatícios em 15% (dez por cento) do valor da atualizado da causa (art. 85, §2º, CPC), suspensa a exigibilidade, diante da gratuidade de justiça deferida à parte autora. Publique-se. Registre-se. Intimem-se. Transitado em julgado e encaminhada certidão de custas ao FUNJURIS, arquive-se com a devida baixa. Maceió,14 de novembro de 2019. Henrique Gomes de Barros Teixeira Juiz de Direito\r\nAdvogados(s): Andrea Freire Tynan (OAB 10699/BA)",
        "eMovimento": "true",
        "nomeOriginal": [
          "Encaminhado ao DJ Eletrônico"
        ]
      },
      {
        "data": "25/11/2019",
        "indice": 76,
        "descricao": "Ato Ordinatório: Em cumprimento ao Provimento nº 13/2009, da Corregedoria-Geral da Justiça do Estado de Alagoas, dê-se ciência à Defensoria Pública sobre a sentença proferida nos presentes autos. Maceió, 25 de novembro de 2019. Louise Melo da Costa Leão Analista Judiciário",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "25/11/2019",
        "indice": 75,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Registro de Sentença"
        ]
      },
      {
        "data": "18/11/2019",
        "indice": 74,
        "descricao": "Ante o exposto, JULGO IMPROCEDENTE O PEDIDO INICIAL, com fundamento no artigo 373, I do CPC, resolvendo o mérito nos termos do art. 487, I, do CPC. Condeno os autores ao pagamento das despesas processuais e honorários advocatícios. Considerando que o local de prestação de serviços não apresenta elevado custo, que o grau de zelo do patrono se mostra dentro da normalidade, que a causa não apresenta grande complexidade e que o valor atualizado da causa se mostra capaz de servir como base de cálculo adequada para as verbas sucumbenciais, fixo os honorários advocatícios em 15% (dez por cento) do valor da atualizado da causa (art. 85, §2º, CPC), suspensa a exigibilidade, diante da gratuidade de justiça deferida à parte autora. Publique-se. Registre-se. Intimem-se. Transitado em julgado e encaminhada certidão de custas ao FUNJURIS, arquive-se com a devida baixa. Maceió,14 de novembro de 2019. Henrique Gomes de Barros Teixeira Juiz de Direito",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "24/10/2018",
        "indice": 73,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Conclusos"
        ]
      },
      {
        "data": "10/10/2018",
        "indice": 72,
        "descricao": "DESPACHO VISTO EM CORREIÇÃO",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "13/06/2018",
        "indice": 71,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Conclusos"
        ]
      },
      {
        "data": "12/06/2018",
        "indice": 70,
        "descricao": "Certidão de Importação de Arquivos Multimídia",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "12/06/2018",
        "indice": 69,
        "descricao": "Certidão de Importação de Arquivos Multimídia",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "12/06/2018",
        "indice": 68,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Audiência Realizada"
        ]
      },
      {
        "data": "23/04/2018",
        "indice": 67,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Mandado"
        ]
      },
      {
        "data": "23/04/2018",
        "indice": 66,
        "descricao": ".CM - Ato positivo",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "23/04/2018",
        "indice": 65,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Mandado"
        ]
      },
      {
        "data": "23/04/2018",
        "indice": 64,
        "descricao": ".CM - Ato positivo",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "19/04/2018",
        "indice": 63,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Mandado"
        ]
      },
      {
        "data": "19/04/2018",
        "indice": 62,
        "descricao": ".CM - Ato positivo",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "11/04/2018",
        "indice": 61,
        "descricao": "Ocorreu o recebimento de um Mandado pela Central de Mandados.",
        "eMovimento": "true",
        "nomeOriginal": [
          "Mandado Recebido na Central de Mandados"
        ]
      },
      {
        "data": "11/04/2018",
        "indice": 60,
        "descricao": "Mandado nº: 001.2018/029832-2 \r\nSituação: Cumprido - Ato positivo em 23/04/2018 \r\nLocal: Oficial de justiça - Karina Nobre de Araújo",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "11/04/2018",
        "indice": 59,
        "descricao": "Ocorreu o recebimento de um Mandado pela Central de Mandados.",
        "eMovimento": "true",
        "nomeOriginal": [
          "Mandado Recebido na Central de Mandados"
        ]
      },
      {
        "data": "11/04/2018",
        "indice": 58,
        "descricao": "Mandado nº: 001.2018/029829-2 \r\nSituação: Cumprido - Ato positivo em 23/04/2018 \r\nLocal: Oficial de justiça - Karina Nobre de Araújo",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "11/04/2018",
        "indice": 57,
        "descricao": "Ocorreu o recebimento de um Mandado pela Central de Mandados.",
        "eMovimento": "true",
        "nomeOriginal": [
          "Mandado Recebido na Central de Mandados"
        ]
      },
      {
        "data": "11/04/2018",
        "indice": 56,
        "descricao": "Mandado nº: 001.2018/029819-5 \r\nSituação: Cumprido - Ato positivo em 19/04/2018 \r\nLocal: Oficial de justiça - Moacira Maria Ferreira Lima",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "26/03/2018",
        "indice": 55,
        "descricao": "Certidão de Intimação - Portal Eletrônico",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "23/03/2018",
        "indice": 54,
        "descricao": "Nº Protocolo: WMAC.18.70056501-6\r\nTipo da Petição: Manifestação do defensor público\r\nData: 23/03/2018 15:30",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "15/03/2018",
        "indice": 53,
        "descricao": "Relação :0086/2018\r\nData da Publicação: 16/03/2018\r\nNúmero do Diário: 2065",
        "eMovimento": "true",
        "nomeOriginal": [
          "Ato Publicado"
        ]
      },
      {
        "data": "15/03/2018",
        "indice": 52,
        "descricao": "Relação :0084/2018\r\nData da Publicação: 16/03/2018\r\nNúmero do Diário: 2065",
        "eMovimento": "true",
        "nomeOriginal": [
          "Ato Publicado"
        ]
      },
      {
        "data": "14/03/2018",
        "indice": 51,
        "descricao": "Relação: 0086/2018\r\nTeor do ato: Em cumprimento ao Provimento nº 13/2009, da Corregedoria-Geral da Justiça do Estado de Alagoas, abro vista a Defensoria Pública da data da audiência designada nos presente autos.Maceió, 14 de março de 2018Sandra de Lima BuarqueAnalista\r\nAdvogados(s): Andrea Freire Tynan (OAB 10699/BA), Eduardo Fraga (OAB 10658/BA), Raoni Souza Drummond (OAB 10120A/AL), Defensoria Pública do Estado de Alagoas (OAB B/AL)",
        "eMovimento": "true",
        "nomeOriginal": [
          "Encaminhado ao DJ Eletrônico"
        ]
      },
      {
        "data": "14/03/2018",
        "indice": 50,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Vista à Defensoria Pública - Portal Eletrônico"
        ]
      },
      {
        "data": "14/03/2018",
        "indice": 49,
        "descricao": "Certidão de Remessa de Citação e Intimação para o Portal",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "14/03/2018",
        "indice": 48,
        "descricao": "Em cumprimento ao Provimento nº 13/2009, da Corregedoria-Geral da Justiça do Estado de Alagoas, abro vista a Defensoria Pública da data da audiência designada nos presente autos.Maceió, 14 de março de 2018Sandra de Lima BuarqueAnalista",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "14/03/2018",
        "indice": 47,
        "descricao": "Relação: 0084/2018\r\nTeor do ato: Autos nº 0731425-82.2014.8.02.0001 Ação: Procedimento Ordinário Autor: Maria Edite dos Santos Réu: Hipercard Banco Multiplo S/A CERTIDÃO DE DESIGNAÇÃO DE AUDIÊNCIACERTIFICO que foi designado o próximo dia 12/06/2018, às 16:30h, para realização de audiência Instrução e Julgamento, conforme determinação do MM. Juiz de DireitoO referido é verdade, do que dou fé.Maceió, 06 de março de 2018.Jozinete Santos Gonçalves Melo Chefe de Secretaria Judicial\r\nAdvogados(s): Andrea Freire Tynan (OAB 10699/BA), Eduardo Fraga (OAB 10658/BA), Raoni Souza Drummond (OAB 10120A/AL), Defensoria Pública do Estado de Alagoas (OAB B/AL)",
        "eMovimento": "true",
        "nomeOriginal": [
          "Encaminhado ao DJ Eletrônico"
        ]
      },
      {
        "data": "06/03/2018",
        "indice": 46,
        "descricao": "Autos nº 0731425-82.2014.8.02.0001 Ação: Procedimento Ordinário Autor: Maria Edite dos Santos Réu: Hipercard Banco Multiplo S/A CERTIDÃO DE DESIGNAÇÃO DE AUDIÊNCIACERTIFICO que foi designado o próximo dia 12/06/2018, às 16:30h, para realização de audiência Instrução e Julgamento, conforme determinação do MM. Juiz de DireitoO referido é verdade, do que dou fé.Maceió, 06 de março de 2018.Jozinete Santos Gonçalves Melo Chefe de Secretaria Judicial",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "06/03/2018",
        "indice": 45,
        "descricao": "Instrução e Julgamento\r\nData: 12/06/2018 Hora 16:30\r\nLocal: Sala de Audiência\r\nSituacão: Realizada",
        "eMovimento": "true",
        "nomeOriginal": [
          "Audiência Designada"
        ]
      },
      {
        "data": "05/03/2018",
        "indice": 44,
        "descricao": "Ação: Procedimento Ordinário Autor: Maria Edite dos Santos Réu: Hipercard Banco Multiplo S/A CERTIDÃO DE DESIGNAÇÃO DE AUDIÊNCIACERTIFICO que foi designado o próximo dia 18/07/2018, às 15:30h, para realização de audiência Instrução e Julgamento, conforme determinação do MM. Juiz de Direito .O referido é verdade, do que dou fé.Maceió, 05 de março de 2018.Jozinete Santos Gonçalves Melo Chefe de Secretaria Judicial",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "01/12/2017",
        "indice": 43,
        "descricao": "DESPACHO VISTO EM CORREIÇÃO",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "17/10/2017",
        "indice": 42,
        "descricao": "Despacho Genérico",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "20/06/2017",
        "indice": 41,
        "descricao": "Nº Protocolo: WMAC.17.70086607-4\r\nTipo da Petição: Pedido de juntada de documento(s)\r\nData: 20/06/2017 15:39",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "12/06/2017",
        "indice": 40,
        "descricao": "Relação :0180/2017\r\nData da Disponibilização: 12/06/2017\r\nData da Publicação: 13/06/2017\r\nNúmero do Diário: 1883\r\nPágina: 14/17",
        "eMovimento": "true",
        "nomeOriginal": [
          "Ato Publicado"
        ]
      },
      {
        "data": "09/06/2017",
        "indice": 39,
        "descricao": "Relação: 0180/2017\r\nTeor do ato: DESPACHO 1.Compulsando-se os autos, após uma análise do estado processual, determino a intimação das partes, em prazo comum de cinco dias, para, querendo, manifestarem-se acerca das provas que pretendem produzir, além das já existentes nos autos. 2.Caso haja intenção de produzir prova testemunhal, que apresentem o rol de testemunhas e noticiem se elas comparecerão ao ato independentemente de intimação.3.Cumpra-se. Dê-se ciência. Maceió(AL), 17 de maio de 2017.Henrique Gomes de Barros Teixeira Juiz de Direito\r\nAdvogados(s): Eduardo Fraga (OAB 10658/BA), Raoni Souza Drummond (OAB 10120A/AL)",
        "eMovimento": "true",
        "nomeOriginal": [
          "Encaminhado ao DJ Eletrônico"
        ]
      },
      {
        "data": "06/06/2017",
        "indice": 38,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Conclusos"
        ]
      },
      {
        "data": "06/06/2017",
        "indice": 37,
        "descricao": "Nº Protocolo: WMAC.17.70078950-9\r\nTipo da Petição: Rol de Testemunhas\r\nData: 06/06/2017 13:07",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "01/06/2017",
        "indice": 36,
        "descricao": "Certidão de Intimação - Portal Eletrônico",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "19/05/2017",
        "indice": 35,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Vista à Defensoria Pública - Portal Eletrônico"
        ]
      },
      {
        "data": "19/05/2017",
        "indice": 34,
        "descricao": "Certidão de Remessa de Citação e Intimação para o Portal",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "19/05/2017",
        "indice": 33,
        "descricao": "DESPACHO 1.Compulsando-se os autos, após uma análise do estado processual, determino a intimação das partes, em prazo comum de cinco dias, para, querendo, manifestarem-se acerca das provas que pretendem produzir, além das já existentes nos autos. 2.Caso haja intenção de produzir prova testemunhal, que apresentem o rol de testemunhas e noticiem se elas comparecerão ao ato independentemente de intimação.3.Cumpra-se. Dê-se ciência. Maceió(AL), 17 de maio de 2017.Henrique Gomes de Barros Teixeira Juiz de Direito",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "05/12/2016",
        "indice": 32,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Conclusos"
        ]
      },
      {
        "data": "28/11/2016",
        "indice": 31,
        "descricao": "Decisões Interlocutórias - Genérico",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "15/03/2016",
        "indice": 30,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Conclusos"
        ]
      },
      {
        "data": "08/03/2016",
        "indice": 29,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "08/03/2016",
        "indice": 28,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "08/03/2016",
        "indice": 27,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "23/02/2016",
        "indice": 26,
        "descricao": "Certidão do Oficial de Justiça",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "18/02/2016",
        "indice": 25,
        "descricao": "Certidão do Oficial de Justiça",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "27/01/2016",
        "indice": 24,
        "descricao": "Assentada",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "06/01/2016",
        "indice": 23,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Mandado"
        ]
      },
      {
        "data": "18/11/2015",
        "indice": 22,
        "descricao": "Relação :0550/2015\r\nData da Disponibilização: 17/11/2015\r\nData da Publicação: 18/11/2015\r\nNúmero do Diário: ED.1514\r\nPágina: 78",
        "eMovimento": "true",
        "nomeOriginal": [
          "Ato Publicado"
        ]
      },
      {
        "data": "17/11/2015",
        "indice": 21,
        "descricao": "Relação: 0550/2015\r\nTeor do ato: Em cumprimento ao Provimento nº 13/2009 da CGJ, fica designada audiência de tentativa de conciliação para o dia 26 de JANEIRO de 2016 às 15h30min neste Centro Judiciário - CJUS PROCESSUAL (Sala 301, 3º andar do Fórum do Barro Duro). Intimações necessárias.\r\nAdvogados(s): Eduardo Fraga (OAB 10658/BA), Raoni Souza Drummond (OAB 10120AA/L)",
        "eMovimento": "true",
        "nomeOriginal": [
          "Encaminhado ao DJ Eletrônico"
        ]
      },
      {
        "data": "16/11/2015",
        "indice": 20,
        "descricao": "Mandado nº: 001.2015/078735-0 \r\nSituação: Cumprido - Ato positivo em 08/03/2016 \r\nLocal: Centro de Solução de Conflitos Judiciários-CJUS",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "11/11/2015",
        "indice": 19,
        "descricao": "Em cumprimento ao Provimento nº 13/2009 da CGJ, fica designada audiência de tentativa de conciliação para o dia 26 de JANEIRO de 2016 às 15h30min neste Centro Judiciário - CJUS PROCESSUAL (Sala 301, 3º andar do Fórum do Barro Duro). Intimações necessárias.",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "11/11/2015",
        "indice": 18,
        "descricao": "Conciliação\r\nData: 26/01/2016 Hora 15:30\r\nLocal: Sala de Audiência - Gabinete\r\nSituacão: Realizada",
        "eMovimento": "true",
        "nomeOriginal": [
          "Audiência Designada"
        ]
      },
      {
        "data": "28/10/2015",
        "indice": 17,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Processo recebido pelo CJUS"
        ]
      },
      {
        "data": "28/10/2015",
        "indice": 16,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Processo encaminhado para CJUS"
        ]
      },
      {
        "data": "23/10/2015",
        "indice": 15,
        "descricao": "Certidão de Importação de Arquivos Multimídia",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "23/10/2015",
        "indice": 14,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Petição"
        ]
      },
      {
        "data": "08/09/2015",
        "indice": 13,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Conclusos"
        ]
      },
      {
        "data": "08/09/2015",
        "indice": 12,
        "descricao": "Nº Protocolo: WMAC.15.70101535-1\r\nTipo da Petição: Réplica\r\nData: 07/09/2015 20:06",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "24/08/2015",
        "indice": 11,
        "descricao": "Relação :0141/2015\r\nData da Disponibilização: 24/08/2015\r\nData da Publicação: 25/08/2015\r\nNúmero do Diário: 1457\r\nPágina: 15/19",
        "eMovimento": "true",
        "nomeOriginal": [
          "Ato Publicado"
        ]
      },
      {
        "data": "21/08/2015",
        "indice": 10,
        "descricao": "Relação: 0141/2015\r\nTeor do ato: Em cumprimento ao Provimento nº 13/2009, da Corregedoria-Geral da Justiça do Estado de Alagoas, manifeste-se a parte autora sobre a contestação e documentos acostados, querendo, em 10 (dez) dias. Maceió, 09 de junho de 2015. Sandra de Lima Buarque Analista Judiciário\r\nAdvogados(s): Raoni Souza Drummond (OAB 10120AA/L), Luciana Martins de Faro (OAB 6804B/AL)",
        "eMovimento": "true",
        "nomeOriginal": [
          "Encaminhado ao DJ Eletrônico"
        ]
      },
      {
        "data": "20/08/2015",
        "indice": 9,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "16/07/2015",
        "indice": 8,
        "descricao": "Genérico",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "16/07/2015",
        "indice": 7,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documento"
        ]
      },
      {
        "data": "09/06/2015",
        "indice": 6,
        "descricao": "Em cumprimento ao Provimento nº 13/2009, da Corregedoria-Geral da Justiça do Estado de Alagoas, manifeste-se a parte autora sobre a contestação e documentos acostados, querendo, em 10 (dez) dias. Maceió, 09 de junho de 2015. Sandra de Lima Buarque Analista Judiciário",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "09/06/2015",
        "indice": 5,
        "descricao": "Nº Protocolo: WMAC.15.70065611-6\r\nTipo da Petição: Contestação\r\nData: 09/06/2015 13:50",
        "eMovimento": "true",
        "nomeOriginal": [
          "Juntada de Documentos"
        ]
      },
      {
        "data": "22/04/2015",
        "indice": 4,
        "descricao": "Citação por Carta Rito Ordinário",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "16/04/2015",
        "indice": 3,
        "descricao": "1No momento deixo de apreciar o pedido de antecipação de tutela, sendo imprescindível a chamada da parte requerida aos autos (citação), para um bom desenrolar da marcha processual. 2. Cite-se o réu, através de seu representante legal para, querendo, contestar o termos do pedido, no prazo de 15 (quinze) dias, advertindo-a dos efeitos da revelia. 3. Cumpra-se. Maceió(AL), 13 de abril de 2015. Henrique Gomes de Barros Teixeira Juiz de Direito",
        "eMovimento": "true",
        "nomeOriginal": [
          ""
        ]
      },
      {
        "data": "24/11/2014",
        "indice": 2,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Conclusos"
        ]
      },
      {
        "data": "24/11/2014",
        "indice": 1,
        "descricao": "",
        "eMovimento": "true",
        "nomeOriginal": [
          "Distribuído por Sorteio"
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
        "titulo": "Cartão de Crédito"
      },
      {
        "titulo": "Dano Moral"
      },
      {
        "titulo": "Inclusão Indevida em Cadastro de Inadimplentes"
      }
    ],
    "urlProcesso": "https://www2.tjal.jus.br/cpopg/show.do?processo.codigo=01000I1FT0000&processo.foro=1&processo.numero=0731425-82.2014.8.02.0001&uuidCaptcha=sajcaptcha_c5664276eff7498b870cb4c7e2944f9c",
    "grauProcesso": "1º Grau",
    "orgaoJulgador": "3ª Vara Cível da Capital ",
    "unidadeOrigem": " Foro de Maceió",
    "classeProcedual": "Procedimento Comum Cível",
    "dataDistribuicao": "09/03/2016 às 14:40 - Prevenção",
    "statusObservacao": "Em grau de recurso",
    "numeroProcessoUnico": "0731425-82.2014.8.02.0001"
  }
]</p>