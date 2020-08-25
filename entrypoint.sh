#!/bin/sh

set -e

# Apply migrations in dev database
alembic upgrade head

# Apply migrations in test database
# cp alembic_test.ini alembic.ini
# alembic upgrade head
# cp alembic_test.ini alembic.ini

sleep 5
# run tests
pytest tests/

# start application
python app.py