SHELL=./make-venv
export RABBITMQ_CONFIG_FILE=rabbitmq.conf

all: env static server

# List all commands
.PHONY: ls
ls:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$' | xargs

.PHONY: shell
shell:
	python3 manage.py shell

.PHONY: heroku
heroku:
	heroku local

.PHONY: install
install:
	sh scripts/start_db.sh
	sh scripts/create_db.sh
	python3 -m venv venv
	make post-install

.PHONY: post-install
post-install:
	pip install -U pip
	pip install -r requirements.txt
	make migrate
	make groups
	make static
	make stopenv

.PHONY: static
static:
	python3 manage.py collectstatic -c --no-input

.PHONY: server
server:
	python3 manage.py runserver

.PHONY: env
env:
	sh scripts/start_db.sh
ifeq ($(USER),vscode)
	sudo rabbitmq-server -detached
else
	rabbitmq-server -detached
endif
	@echo "RabbitMQ Status: Online"

.PHONY: stopenv
stopenv:
ifeq ($(USER),vscode)
	sudo rabbitmqctl stop --idempotent
else
	rabbitmqctl stop --idempotent
endif
	@echo "RabbitMQ Status: Offline"
	sh scripts/stop_db.sh

.PHONY: migrate
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

.PHONY: celery
celery:
	celery worker -A reboot --without-gossip --without-heartbeat

.PHONY: clean
clean:
	rm -rf venv
	rm -rf staticfiles

.PHONY: groups
groups:
	python3 manage.py creategroups

.PHONY: codespace
codespace:
	initdb /usr/local/var/postgres
	sudo cp ./rabbitmq-devcontainer.conf /etc/rabbitmq/rabbitmq.conf
	make .env
	make .git/hooks/pre-commit
	make install

.PHONY: test
test:
	coverage run --source=./app ./manage.py test

.PHONY: coverage
coverage:
	coverage report

.env:
	cp .env.sample .env

.git/hooks/pre-commit:
	cp hooks/pre-commit .git/hooks/pre-commit
