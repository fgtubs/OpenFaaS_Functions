
## Build
docker build --tag DOCKER_USER/payload-echo:v0.0.1 .
docker push DOCKER_USER/payload-echo:v0.0.1

## Deploy
faas deploy --image DOCKER_USER/payload-echo:v0.0.1 --name payload-echo --fprocess "python index.py"

## Test
curl http://127.0.0.1:31112/function/payload-echo -d "test"