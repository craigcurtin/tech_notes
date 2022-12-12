
docker run --rm -t \
-v $(pwd):/specs:ro \
openapitools/openapi-diff:latest \
--info /specs/original.json /specs/age.json
