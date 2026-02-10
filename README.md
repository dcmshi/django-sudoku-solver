# django-sudoku-solver

A Django web app that solves Sudoku puzzles. Enter a puzzle, click Solve, and get the answer instantly. Can also generate random puzzles automatically.

## How it works

The solver is written in Python and uses a backtracking algorithm with constraint satisfaction heuristics (Most Constrained Variable, Least Constraining Values). The puzzle generator creates valid boards and removes clues while ensuring a unique solution remains.

## Tech stack

- Python 3.12
- Django 5.2
- Jinja2 templates
- Bootstrap 3

## Local development

Requires [uv](https://docs.astral.sh/uv/).

```bash
git clone https://github.com/dcmshi/django-sudoku-solver
cd django-sudoku-solver
uv sync
uv run python manage.py runserver
```

Open http://127.0.0.1:8000/

## Deployment

The app is ready to deploy to [Render](https://render.com) or [Railway](https://railway.app) — both have free tiers and detect the `Procfile` automatically.

Set one environment variable before deploying:

```
SECRET_KEY=<generate with the command below>
```

```bash
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## Open source

- [Django project](https://github.com/dcmshi/django-sudoku-solver)
- [Original Python solver](https://github.com/dcmshi/sudoku-solver)

## License

See [LICENSE](LICENSE).
