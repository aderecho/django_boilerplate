class PostTransformer:
    @staticmethod
    def transform(post):
        return {
            "id": post.id,
            "title": post.title,
            "slug": post.slug,
            "content": post.content,
            "status": post.status,
            "published_at": post.published_at,
            "created_at": post.created_at,
            "updated_at": post.updated_at,
            "author": {
                "id": post.author.id,
                "name": post.author.name,
                "email": post.author.email,
            },
        }

    @staticmethod
    def transform_many(posts):
        return [PostTransformer.transform(post) for post in posts]
