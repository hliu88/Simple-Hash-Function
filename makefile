LINTER = flake8

FORCE:

prod: tests #github

dev_env: FORCE
	#enable virtual env
	pip install -r requirements.txt

tests: unit #lint

unit: FORCE
	python tests.py
# 	nosetests --with-coverage --cover-package=$(APP_DIR)

# lint: FORCE
# 	$(LINTER) $(APP_DIR)/*.py