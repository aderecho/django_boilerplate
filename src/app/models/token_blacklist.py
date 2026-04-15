from django.conf import settings
from django.db import models

class RefreshTokenBlacklist(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blacklisted_refresh_tokens")
    jti = models.CharField(max_length=255, unique=True)
    expires_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "refresh_token_blacklists"
        ordering = ["-created_at"]

    def __str__(self):
        return self.jti
