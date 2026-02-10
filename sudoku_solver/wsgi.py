"""
WSGI config for sudoku_solver project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sudoku_solver.settings")

application = get_wsgi_application()
