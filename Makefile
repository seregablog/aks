lint:
	docker-compose exec aks python3 -m flake8 aks

tests:
	docker-compose exec aks python3 test.py

table:
	docker-compose exec aks python3 table.py

