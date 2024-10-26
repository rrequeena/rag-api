build:
	docker-compose -f docker-compose.yml build

compose:
	docker-compose -f docker-compose.yml up

# Enter to bash of the image api called rag-api
api_image_bash:
	docker run -it --rm --entrypoint /bin/bash rag-api
