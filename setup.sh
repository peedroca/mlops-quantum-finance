echo "Let's setup our enviroment!"

echo "Creating docker images for all containers"
docker build -t defaultpropensityapi -f part_1/dockerbuilds/Dockerfile part_1/docker/
docker build -t customerclusteringapi -f part_2/dockerbuilds/Dockerfile part_2/docker/
docker build -t modelmanager -f part_3/dockerbuilds/Dockerfile part_3/docker/
docker build -t frontendstreamlit -f part_4/dockerbuilds/Dockerfile part_4/docker/

echo "Creating network"
docker network create plat_network

echo "Deploying containers for predictions"
docker run -d --restart always --network plat_network --name defaultpropensityapi defaultpropensityapi
docker run -d --restart always --network plat_network --name customerclusteringapi customerclusteringapi

echo "Updating microservices.json for expose APIs for predicting"
bash ./part_3/update_config.sh

echo "Config model manager"
docker run -d --restart always --network plat_network -v $(pwd)/part_3/docker/config:/myServer/config -v $(pwd)/part_3/docker/log:/myServer/log --name modelmanager modelmanager

echo "Updating microservices.json for access API from Frontend"
bash ./part_4/update_config.sh

echo "Config FrontEnd"
docker run -d --restart always --network plat_network -p 80:8501 -v $(pwd)/part_4/docker/config:/myServer/config --name frontendstreamlit frontendstreamlit
