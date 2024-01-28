from django.contrib import admin


from.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('email',)

    def get_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ('email', 'password', 'avatar', 'phone', 'country', 'is_active', 'is_staff', 'is_superuser',
                    'email_verification_token', 'last_login', 'date_joined', 'groups',)

        elif obj:
            return ('is_active',)
        else:
            return ()

    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user.has_perm('users.can_change_user_is_active'):
            return True
        return super().has_change_permission(request, obj)
