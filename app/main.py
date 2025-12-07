#poetry run python -m app.main
#docker exec -it todolist-db psql -U mehr -d todolist


from .cli.console import run_cli



if __name__ == "__main__":
    run_cli()