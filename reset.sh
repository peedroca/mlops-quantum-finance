echo "Let's reset our enviroment!"

docker stop defaultpropensityapi
docker stop customerclusteringapi
docker stop modelmanager
docker stop frontendstreamlit

docker rm defaultpropensityapi
docker rm customerclusteringapi
docker rm modelmanager
docker rm frontendstreamlit

docker network rm plat_network
