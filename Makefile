build:
	docker-compose -f docker-compose.yml build

compose:
	docker-compose -f docker-compose.yml up

api_image_bash:
	docker run -it --rm --entrypoint /bin/bash rag-api
