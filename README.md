# Python Template
Use as a template for python repos.


## Run the tests
```bash
python -m pytest
```



## Using the Dockerfile to create an image

Follwo these steps:

```
# Find the docker file
cd /.devcontainer

# To build the image
docker build -t phoughton/python-dev-main

# Login to existing account
docker login

# Upload
docker push phoughton/python-dev-main
```
