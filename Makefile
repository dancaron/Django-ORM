update-dependencies:
	mkdir -p requirements
	poetry update
	poetry export -f requirements.txt > requirements/local.txt --without-hashes --dev
	poetry export -f requirements.txt > requirements/production.txt --without-hashes

layer:update-dependencies
	mkdir -p python
	pip install -r requirements/production.txt -t python
	zip -r9 layer.zip python
	@rm -r python
