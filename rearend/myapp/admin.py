from django.contrib import admin

# Register your models here.
from .models import Router,Port


class PortInfo(admin.TabularInline):
    model = Port
    extra = 4


@admin.register(Router)
class RouterAdmin(admin.ModelAdmin):

    # 给列名字换成中文
    def paiming(self):
        return self.pk
    paiming.short_description = '排序'

    def mingzi(self):
        return self.rname
    mingzi.short_description = '名字'

    # 把port创建添加到路由器创建中
    inlines = [PortInfo]

    #  列表页属性
    list_display = [paiming,mingzi,'rdate','rposition','rnumberport','IsDelete']
    list_filter = ['rname']
    list_per_page = 5
    search_fields = ['rname']

    #  添加修改页属性
    #fields =
    fieldsets = [
        ('standard', {'fields': ['rname', 'rdate']}),
        ('deluxe', {'fields': ['rposition', 'rnumberport']})
    ]

    # 把执行动作栏放到下面
    actions_on_bottom = True
    actions_on_top = False


@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    list_display = ['pk','pname','paddress','pstatus',
                    'pvlan','prouter','IsDelete']
    list_filter = ['pname']
    search_fields = ['pname']
    fieldsets = [
        ('standard',{'fields':['pname','paddress','pstatus']}),
        ('deluxe',{'fields':['pvlan','prouter']})
    ]


# admin.site.register(Router, RouterAdmin)
# admin.site.register(Port,PortAdmin)