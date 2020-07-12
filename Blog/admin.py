from django.contrib import admin

# Register your models here.
from Blog.models import Python, Java, Csharp, Html

admin.site.register(Python)
admin.site.register(Java)
admin.site.register(Csharp)
admin.site.register(Html)

