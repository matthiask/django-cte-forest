#!/bin/sh
PYTHONPATH=. coverage run --branch --include="*cte_forest/*" cte_forest_test/manage.py test -v 2
coverage report -m
