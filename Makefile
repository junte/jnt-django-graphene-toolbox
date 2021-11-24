lint:
	@./scripts/lint.sh

test:
	@pytest

release:
	@./scripts/release.sh

make_messages:
	@django-admin makemessages -l en -l ru --no-location

pre_commit_install:
	@ pre-commit install && pre-commit install --hook-type commit-msg
