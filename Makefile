check_quality:
	@./scripts/quality.sh

release:
	@./scripts/release.sh

make_messages:
	@django-admin makemessages -l en -l ru --no-location
