
echo '{                                                     ' >  $(pwd)/part_4/docker/config/microservices.json
echo '  "model_manager": {                                         ' >> $(pwd)/part_4/docker/config/microservices.json
echo '    "endpoint": "http://'$(sudo docker inspect modelmanager | python3 -c "import sys, json; print(json.load(sys.stdin)[0]['NetworkSettings']['Networks']
['plat_network']['IPAddress'])")':8080"          ' >> $(pwd)/part_4/docker/config/microservices.json
echo '  }                                                   ' >> $(pwd)/part_4/docker/config/microservices.json
echo '}                                                     ' >> $(pwd)/part_4/docker/config/microservices.json

echo "[PART 4] Arquivo de configuração atualizado com sucesso. Veja seu conteúdo: "

cat $(pwd)/part_4/docker/config/microservices.json