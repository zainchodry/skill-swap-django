from django.contrib import admin
from . models import *
from django.contrib.auth.admin import UserAdmin



admin.site.register(User, UserAdmin)
admin.site.register(Skill)
admin.site.register(SkillOffer)
admin.site.register(SkillRequest)
admin.site.register(Match)
admin.site.register(Review)