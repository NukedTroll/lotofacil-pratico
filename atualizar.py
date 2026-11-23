"""Atualiza resultados.json com os concursos novos da Lotofácil (só biblioteca padrão)."""
import json, time, urllib.request
from datetime import datetime, timezone

BASE = "https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil"
ARQ = "resultados.json"


def baixar(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0", "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def converter(j):
    d, m, a = map(int, j["dataApuracao"].split("/"))
    t = int(datetime(a, m, d, 12, tzinfo=timezone.utc).timestamp() * 1000)
    n = sorted(int(x) for x in j["listaDezenas"])
    r = {}
    for f in j.get("listaRateioPremio") or []:
        k = int(str(f["descricaoFaixa"]).split()[0])
        if 11 <= k <= 15:
            r[str(k)] = float(f.get("valorPremio") or 0)
    return {"c": int(j["numero"]), "t": t, "n": n, "r": r}


def main():
    dados = json.load(open(ARQ, encoding="utf-8"))
    ultimo = dados[-1]["c"]
    atual = int(baixar(BASE)["numero"])
    novos = 0
    for c in range(ultimo + 1, atual + 1):
        dados.append(converter(baixar(f"{BASE}/{c}")))
        novos += 1
        time.sleep(1)
    if novos:
        json.dump(dados, open(ARQ, "w", encoding="utf-8"), separators=(",", ":"))
    print(f"Último no arquivo: {ultimo} | último na Caixa: {atual} | novos: {novos}")


if __name__ == "__main__":
    main()
