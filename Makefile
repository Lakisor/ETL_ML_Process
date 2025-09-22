IMAGE_NAME=etl_process

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm -v $(PWD)/data:/app/data $(IMAGE_NAME)

shell:
	docker run -it --rm -v $(PWD)/data:/app/data $(IMAGE_NAME) bash

clean:
	docker rmi -f $(IMAGE_NAME) || true
