from bs4 import BeautifulSoup
from datetime import datetime


def parse(response):
    try:
        soup = BeautifulSoup(response.text, "html.parser")
    except:
        print("Erro no parser dos dados!")

    yield {
        "uf": "AL",
        "area": _build_area(soup),
        "juiz": _build_judge(soup),
        "partes": _build_parties(soup),
        "sistema": "ESAJ-TJAL",
        "segmento": "JUSTICA ESTADUAL",
        "tribunal": "TJ-AL",
        "movimentos": _build_mov(soup),
        "valorCausa": _build_value(soup),
        "assuntosCNJ": _build_subjects(soup),
        "urlProcesso": response.url,
        "grauProcesso": _build_degree(soup),
        "orgaoJulgador": _build_org(soup),
        "unidadeOrigem": _build_origin(soup),
        "classeProcessual": {"nome": _build_classP(soup)},
        "dataDistribuicao": _build_date(soup),
        "eProcessoDigital": "true",
        "statusObservacao": _build_obs(soup),
        "numeroProcessoUnico": _build_numP(soup),
    }


def _build_area(soup):
    area = soup.find("span", "labelClass").parent.text.strip().split(" ")[1]
    if area is None:
        return "Não possui area!"
    else:
        return area.upper()


def _build_judge(soup):
    juiz = (
        soup.find("label", string="Juiz:").parent.find_next_sibling("td").text.strip()
    )
    if juiz is None:
        return "Juiz is none"
    else:
        return juiz.upper()


def _build_parties(soup):

    parte = soup.find("table", id="tableTodasPartes").find_all(
        "tr", class_="fundoClaro"
    )

    partes = []

    for par in parte:
        tipo = par.find("td").find("span").text.strip().split(":")[0]
        tipo_adv = (
            par.find("td")
            .find_next_sibling("td")
            .find("span", class_="mensagemExibindo")
        )
        nome = par.find("td").find_next_sibling("td").contents[0].strip()
        advg = [
            {"nome": adv.upper(), "tipo": tipo_adv.text.strip().split(":")[0].upper()}
            for adv in par.find("td").find_next_sibling("td").stripped_strings
            if adv != nome
            if adv != "Defensor P:"
            if adv != "Advogado:"
            if adv != "Advogada:"
        ]
        if nome:
            if tipo != "Testemunha":
                partes.append(
                    {"nome": nome.upper(), "tipo": tipo.upper(), "Advogado(s)": advg}
                )
            else:
                partes.append(
                    {
                        "nome": nome.upper(),
                        "tipo": tipo.upper(),
                    }
                )

    return partes


def _build_mov(soup):
    movimentacao = soup.find("tbody", id="tabelaTodasMovimentacoes").find_all("tr")

    indice = len(movimentacao)
    movimentacoes = []

    for mov in movimentacao:
        data = mov.find("td").text.strip()
        date = datetime.strptime(data, "%j/%m/%Y").date().strftime("%Y-%m-%jT%H:%M:%S")
        descricao = (
            mov.find("td")
            .find_next("td")
            .find_next("span")
            .text.replace("\r\n", "")
            .strip()
        )
        nomeOriginal = mov.find("td").find_next("td").find_next("td").contents[0]
        nomeOriginal = nomeOriginal.replace("\n\t", "")
        nomeOriginal = nomeOriginal.strip()
        if descricao:
            movimentacoes.append(
                {
                    "data": date,
                    "indice": indice,
                    "descricao": descricao.upper(),
                    "eMovimento": "true",
                    "nomeOriginal": [nomeOriginal.upper()],
                }
            )
        else:
            movimentacoes.append(
                {
                    "data": date,
                    "indice": indice,
                    "eMovimento": "true",
                    "nomeOriginal": [nomeOriginal.upper()],
                }
            )
        indice -= 1
    if movimentacoes is None:
        return "NÃO POSSUI MOVIMENTAÇÕES NO MOMENTO!"
    else:
        return movimentacoes


def _build_subjects(soup):
    assuntosCNJ = []
    assunto = (
        soup.find("label", string="Assunto:")
        .parent.find_next_sibling("td")
        .find("span")
        .text.strip()
    )
    assuntosCNJ.append(
        {
            "titulo": assunto.upper(),
        }
    )
    outrosAssuntos = (
        soup.find("label", string="Outros assuntos:")
        .parent.find_next_sibling("td")
        .find("span")
        .text.split(",")[0]
    )
    assuntosCNJ.append({"titulo": outrosAssuntos.upper()})
    outrosAssuntos1 = (
        soup.find("label", string="Outros assuntos:")
        .parent.find_next_sibling("td")
        .find("span")
        .text.split(",")[1]
    )
    assuntosCNJ.append({"titulo": outrosAssuntos1.upper()})
    if assuntosCNJ is None:
        return "Assuntos is none!"
    else:
        return assuntosCNJ


def _build_value(soup):
    valorCausa = []

    moeda = (
        soup.find("label", string="Valor da ação:")
        .parent.find_next_sibling("td")
        .find("span")
        .text.split()[0]
    )

    valor = (
        soup.find("label", string="Valor da ação:")
        .parent.find_next_sibling("td")
        .find("span")
        .text.split()[1]
    )

    valorCausa.append({"moeda": moeda, "valor": valor})
    if valorCausa is None:
        return "Valor is none"
    return valorCausa


def _build_degree(soup):
    grauProcesso = " ".join(
        soup.find("h1", class_="esajTituloPagina").text.split()[-2:]
    )
    if grauProcesso is None:
        return "Degree is none"
    else:
        return grauProcesso.upper()


def _build_org(soup):
    orgaoJulgador = (
        soup.find("label", string="Distribuição:")
        .find_parent("tr")
        .find_next_sibling("tr")
        .text.strip()
        .split("-")[0]
    )
    if orgaoJulgador is None:
        return "OrgaoJulgador is none"
    else:
        return orgaoJulgador.upper()


def _build_origin(soup):
    unidadeOrigem = (
        soup.find("label", string="Distribuição:")
        .find_parent("tr")
        .find_next_sibling("tr")
        .text.strip()
        .split("-")[1]
    )
    if unidadeOrigem is None:
        return "Origin is none"
    else:
        return unidadeOrigem.upper()


def _build_classP(soup):
    classeProcessual = (
        soup.find("label", string="Classe:").parent.find_next_sibling("td").text.strip()
    )
    if classeProcessual is None:
        return "classeProcessual is none"
    else:
        return classeProcessual.upper()


def _build_date(soup):
    buscaData = (
        soup.find("label", string="Distribuição:")
        .parent.find_next_sibling("td")
        .text.strip()
        .split(" ")[0]
    )
    if buscaData is None:
        return "Date is none"
    else:
        dataDistribuicao = (
            datetime.strptime(buscaData, "%j/%m/%Y")
            .date()
            .strftime("%Y-%m-%jT%H:%M:%S")
        )
        return dataDistribuicao


def _build_obs(soup):
    statusObservacao = (
        soup.find("label", string="Processo:")
        .parent.find_next_sibling("td")
        .find_all("span")[2]
        .text.strip()
    )
    if statusObservacao is None:
        return "Não encontrado!"
    else:
        return statusObservacao.upper()


def _build_numP(soup):
    numeroProcessoUnico = (
        soup.find("label", string="Processo:")
        .parent.find_next_sibling("td")
        .find_all("span")[0]
        .text.strip()
    )
    return numeroProcessoUnico
