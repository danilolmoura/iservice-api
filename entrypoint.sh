#!/bin/sh

# Apply migrations in dev database
alembic upgrade head

# Apply migrations in test database
# cp alembic_test.ini alembic.ini
# alembic upgrade head
# cp alembic_test.ini alembic.ini

run tests
pytest tests/

# start application
python app.py