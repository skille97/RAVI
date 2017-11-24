from django.contrib import admin

from board.models import *
from django.db.models import get_app, get_models



app = get_app("board")
for model in get_models(app):
	if not model.__name__ in [ "VærdiModel"]:
		admin.site.register(model)
