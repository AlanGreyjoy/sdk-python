VENV_NAME?=venv

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	@test -d $(VENV_NAME) || python3 -m virtualenv --clear $(VENV_NAME)

linter:
	. $(VENV_NAME)/bin/activate; flake8 ./apidaze

linter-fix:
	. $(VENV_NAME)/bin/activate; autopep8 --in-place --aggressive --aggressive -r apidaze/

clean:
	@rm -rf $(VENV_NAME) build/ dist/

.PHONY: venv clean
