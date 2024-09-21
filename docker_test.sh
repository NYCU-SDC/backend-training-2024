#!/bin/bash
echo "Check Files Change..."
./.github/scripts/check_files.sh

docker exec -t -w "/mnt" fastapi_app rm -rf test
docker exec -t -w "/mnt" fastapi_app mkdir -p test
docker exec -t -w "/mnt" fastapi_app cp -r app/* test/
docker exec -t -w "/mnt" fastapi_app cp -r .github/scripts/* test/
docker exec -t -w "/mnt/test" fastapi_app pytest