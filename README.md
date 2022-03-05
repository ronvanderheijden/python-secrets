# Python Secrets using GnuPG

## docker

### using the image
```sh
docker build -t secrets .
docker run -ti \
    --volume $(pwd)/src:/home \
    --env SECRETS_PUBLIC_KEY=/home/public.asc \
    --env SECRETS_PRIVATE_KEY=/home/private.asc \
    secrets [COMMAND]
```

### using docker-compose
```sh
docker-compose up --build -d
docker-compose exec secrets [COMMAND]
```

## commands
```sh
# enter the container
bash

# generate a new keypair
genkeys

# run the test
runtest

# encrypt using the public key, asks for secret
encrypt

# decrypt using the private key, asks for secret
decrypt
```
