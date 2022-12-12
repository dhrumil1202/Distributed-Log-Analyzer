VERSION=v1
DOCKERUSER=rzpav21

build:
	docker build -f Dockerfile -t logger .

push:
	docker tag logger $(DOCKERUSER)/logger:$(VERSION)
	docker push $(DOCKERUSER)/logger:$(VERSION)
	docker tag logger $(DOCKERUSER)/logger:latest
	docker push $(DOCKERUSER)/logger:latest