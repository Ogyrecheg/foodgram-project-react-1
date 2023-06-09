from django.contrib import admin

from .models import Subscription, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = (
        'pk',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
    )
    search_fields = ('username',)
    list_filter = ('email', 'username',)
    empty_value_display = '-пусто-'


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):

    list_display = ('pk', 'user', 'author',)
