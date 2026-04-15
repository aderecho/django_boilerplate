from django.core.management.base import BaseCommand
from app.models.user import User
from app.models.post import Post

class Command(BaseCommand):
    help = "Seed demo data"

    def handle(self, *args, **options):
        user, created = User.objects.get_or_create(
            email="admin@example.com",
            defaults={
                "first_name": "Admin",
                "last_name": "User",
                "is_staff": True,
                "is_superuser": True,
            }
        )
        if created:
            user.set_password("Admin@12345")
            user.save()

        for idx in range(1, 6):
            Post.objects.get_or_create(
                slug=f"sample-post-{idx}",
                defaults={
                    "author": user,
                    "title": f"Sample Post {idx}",
                    "content": f"This is sample post number {idx}.",
                    "status": Post.STATUS_PUBLISHED,
                }
            )

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully."))
