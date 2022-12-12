VERSION=v1
DOCKERUSER=rzpav21

build:
	docker build -f Dockerfile -t analyzer .
push:
	docker tag analyzer $(DOCKERUSER)/analyzer:$(VERSION)
	docker push $(DOCKERUSER)/analyzer:$(VERSION)
	docker tag analyzer $(DOCKERUSER)/analyzer:latest
	docker push $(DOCKERUSER)/analyzer:latest