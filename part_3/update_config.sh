
echo '{                                                     ' >  $(pwd)/part_3/docker/config/microservices.json
echo '  "models": {                                         ' >> $(pwd)/part_3/docker/config/microservices.json
echo '    "default_propensity": {                                     ' >> $(pwd)/part_3/docker/config/microservices.json
echo '      "version": "V01",                               ' >> $(pwd)/part_3/docker/config/microservices.json
echo '      "url": "http://'$(sudo docker inspect defaultpropensityapi | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['plat_network']['IPAddress'])")':8080/predict"          ' >> $(pwd)/part_3/docker/config/microservices.json
echo '    },                                                ' >> $(pwd)/part_3/docker/config/microservices.json
echo '    "customer_clustering": {                                     ' >> $(pwd)/part_3/docker/config/microservices.json
echo '      "version": "V01",                               ' >> $(pwd)/part_3/docker/config/microservices.json
echo '      "url": "http://'$(sudo docker inspect customerclusteringapi | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['plat_network']['IPAddress'])")':8080/predict"          ' >> $(pwd)/part_3/docker/config/microservices.json
echo '    }                                                 ' >> $(pwd)/part_3/docker/config/microservices.json
echo '  }                                                   ' >> $(pwd)/part_3/docker/config/microservices.json
echo '}                                                     ' >> $(pwd)/part_3/docker/config/microservices.json

echo "Arquivo de configuração atualizado com sucesso. Veja seu conteúdo: "

cat $(pwd)/part_3/docker/config/microservices.json