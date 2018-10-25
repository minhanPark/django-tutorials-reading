from django.contrib import admin
from .models import Book, Wisesaying

# # 제목 바꾸기
admin.site.site_header = "runningwater django-app"

# admin.site.register(Book)
# admin.site.register(Wisesaying)

# 두번째 코드
# 어드민을 커스텀하려면 모델 어드민을 통해서 클래스를 상속받아서 하면 되고, 레지스터에 전달하면 됨
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('name', 'author', 'introduction')
#
# admin.site.register(Book, BookAdmin)
# admin.site.register(Wisesaying)

# 세번째 코드
# admin.register 데코레이터를 통해서도 똑같이 가능
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('name', 'author', 'introduction')
#
# admin.site.register(Wisesaying)

# 네번째 코드
# 1:N관계에 있는 것을 하나로 합칠 수 있다.
# 합치면 admin.site.register(Wisesaying)은 사라짐

class WisesayingInline(admin.StackedInline):
    model = Wisesaying
    extra = 2

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'introduction')
    # 필드셋을 추가했습니다.
    fieldsets = [
    ('Book Name', {'fields': ['name','author']}),
    ('Introduction', {'fields': ['introduction']}),
    ]
    inlines = [WisesayingInline]

# 필드셋은 마지막으로 커스텀하는 것으로 보여주면 될듯
