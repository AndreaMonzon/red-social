from django.contrib import admin
from .models import Post,Profile,Relationship

# Register your models here.


from .models import Post,Profile

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)
