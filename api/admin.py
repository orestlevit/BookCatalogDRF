from django.contrib import admin

from .models import models

for model in models:
    admin.site.register(model)


