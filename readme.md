# MLOps - Quantum Finance

A Startup QuantumFinance é uma Fintech que está entrando no mercado para competir com grandes players da área.

Durante nosso MBA Data Science & Artificial Intelligence aplicaremos ciência de dados e inteligência artificial para fomentar a expansão da Startup, em seus diversos segmentos e áreas de negócios.

## Configurando e testando o ambiente de Containers
1. Para criar a imagem do modelo para testarmos, na pasta raiz, execute:
```bash
docker build -t defaultpropensityapi -f part_1/dockerbuilds/Dockerfile part_1/docker/
```
2. Você pode rodar individualmente um container da seguinte forma:
```bash
docker run -p 8080:8080 --name defaultpropensityapi defaultpropensityapi
```
3. Após testar que o modelo funciona corretamente, execute o setup de ambiente com:
```bash
bash setup.sh
```