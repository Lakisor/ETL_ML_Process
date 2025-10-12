IMAGE_NAME=etl_process

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm \
	  --network pet_projects_default \
	  -v $(PWD)/data:/app/data \
	  etl_process

shell:
	docker run -it --rm -v $(PWD)/data:/app/data $(IMAGE_NAME) bash

clean:
	docker rmi -f $(IMAGE_NAME) || true
