all: clean build copy
build:
	docker build -t dev/json2raw .
copy:
	docker run -d --rm --name dev-json2raw-copy dev/json2raw sleep 100
	docker cp dev-json2raw-copy:/usr/src/app/dist/json2raw ./bin/json2raw
	docker stop dev-json2raw-copy
test:
	docker run --rm -v `pwd`/examples/json:/examples dev/json2raw /bin/json2raw /examples/helloworldenv.json
clean:
	docker rmi -f dev/json2raw
	rm -f ./bin/*
env:
	docker run -it --rm -v `pwd`/src:/usr/src/app -v `pwd`/examples/json:/examples dev/json2raw /bin/bash
