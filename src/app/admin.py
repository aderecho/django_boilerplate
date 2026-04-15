from django.contrib import admin
from app.models.user import User
from app.models.post import Post
from app.models.token_blacklist import RefreshTokenBlacklist

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "first_name", "last_name", "is_active", "is_staff")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("-id",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "author", "created_at")
    search_fields = ("title", "slug", "content")
    list_filter = ("status", "created_at")
    ordering = ("-id",)

@admin.register(RefreshTokenBlacklist)
class RefreshTokenBlacklistAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "jti", "expires_at", "created_at")
    search_fields = ("jti", "user__email")
