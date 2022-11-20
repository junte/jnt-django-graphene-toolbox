lint:
	black --check .
	mypy .
	flake8 .
	xenon --max-absolute A \
        --max-modules A \
        --max-average A \
        --exclude src/jnt_django_graphene_toolbox/helpers/values.py,src/jnt_django_graphene_toolbox/fields/model_connection.py,src/jnt_django_graphene_toolbox/types/model.py \
        .
	poetry check
	pip check
	safety check --bare --full-report

test:
	@pytest

make-messages:
	@django-admin makemessages -l en -l ru --no-location

pre-commit-install:
	@pre-commit install
	@pre-commit install --hook-type commit-msg
