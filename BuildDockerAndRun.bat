docker stop hackyeah-ml
docker rm hackyeah-ml
docker rmi hackyeah-ml
docker build -t hackyeah-ml .
docker run -d -p 7000:105 --name hackyeah-ml hackyeah-ml