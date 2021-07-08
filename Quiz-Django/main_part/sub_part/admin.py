from . models import createQ, staff_reg, stu_rec, stud_reg, stud_res
from django.contrib import admin

# Register your models here.

admin.site.register(staff_reg)
admin.site.register(stud_reg)
admin.site.register(createQ)
admin.site.register(stu_rec)
admin.site.register(stud_res)