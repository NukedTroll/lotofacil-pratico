# Lotofácil Prático: publicar na internet (grátis)

1. Crie uma conta em github.com e um repositório PÚBLICO novo (ex.: lotofacil-pratico).
2. Em "Add file > Upload files", envie TODOS os arquivos desta pasta (inclusive a pasta .github).
3. Em Settings > Pages: Source = "Deploy from a branch", Branch = main, pasta "/ (root)". Salve.
   Em 1 a 2 minutos o site abre em https://SEU-USUARIO.github.io/lotofacil-pratico/
4. Teste o atualizador: aba Actions > "Atualizar resultados" > Run workflow. Abra o log:
   - Se mostrar "novos: 0" ou "novos: N", está funcionando e roda sozinho todo dia.
   - Se der erro de acesso (403/timeout), a Caixa bloqueou os servidores do GitHub.
     Alternativa: no seu computador, abra o terminal na pasta e rode `python atualizar.py`,
     depois envie o resultados.json atualizado ao repositório. O site continua igual.
