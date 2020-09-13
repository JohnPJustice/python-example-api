GIT_COMMIT=$(shell git rev-parse HEAD)
GIT_DIRTY=$(shell test -n "`git status --porcelain`" && echo "+CHANGES" || true)
BUILD_DATE=$(shell date '+%Y-%m-%d-%H:%M:%S')
IMAGE_NAME := "supermagicpowerman/python-api"

default: test

help:
	@echo 'Management commands for python-api:'
	@echo
	@echo 'Usage:'
	@echo '    make build           Compile the project.'
	@echo '    make run             runs api.'
	@echo

build:
	docker build -t ${IMAGE_NAME} .

run:
	docker run -d -p 3000:3000 ${IMAGE_NAME}
