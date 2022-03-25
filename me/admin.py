from django.contrib import admin

from me.models import (
    About as AboutsModel,
    Tag as TagsModel,
    Work as WorksModel,
)

admin.site.register(AboutsModel)
admin.site.register(TagsModel)
admin.site.register(WorksModel)
