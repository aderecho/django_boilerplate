from django.utils import timezone
from app.models.post import Post
from app.services.base_service import BaseService

class PostService(BaseService):
    @staticmethod
    def create(author, validated_data):
        if validated_data.get("status") == Post.STATUS_PUBLISHED and not validated_data.get("published_at"):
            validated_data["published_at"] = timezone.now()
        post = Post.objects.create(author=author, **validated_data)
        return PostService.success(data=post, message="Post created successfully.", status_code=201)

    @staticmethod
    def update(post, validated_data):
        for key, value in validated_data.items():
            setattr(post, key, value)

        if post.status == Post.STATUS_PUBLISHED and not post.published_at:
            post.published_at = timezone.now()

        post.save()
        return PostService.success(data=post, message="Post updated successfully.")

    @staticmethod
    def delete(post):
        post.delete()
        return PostService.success(message="Post deleted successfully.", status_code=204)
