.PHONY: local

# Generate an image of the models in the system.
graph:
	python3 manage.py graph_models
