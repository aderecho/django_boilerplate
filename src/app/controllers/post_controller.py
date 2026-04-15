from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from rest_framework.response import Response

from app.models.post import Post
from app.serializers.post_serializer import PostSerializer
from app.services.post_service import PostService
from app.transformers.post_transformer import PostTransformer

class PostListCreateController(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author").all()
    filterset_fields = ["status", "author_id"]
    search_fields = ["title", "slug", "content"]
    ordering_fields = ["id", "title", "created_at", "updated_at", "published_at"]

    @extend_schema(tags=["Posts"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=["Posts"])
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = PostService.create(request.user, serializer.validated_data)
        return Response(
            {
                "success": result["success"],
                "message": result["message"],
                "data": PostTransformer.transform(result["data"]),
            },
            status=result["status_code"],
        )

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            return self.get_paginated_response(PostTransformer.transform_many(page))

        return Response({
            "success": True,
            "message": "Posts fetched successfully.",
            "data": PostTransformer.transform_many(queryset),
        })

class PostDetailController(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.select_related("author").all()
    lookup_field = "id"

    @extend_schema(tags=["Posts"])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(tags=["Posts"])
    def put(self, request, *args, **kwargs):
        post = self.get_object()
        serializer = self.get_serializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        result = PostService.update(post, serializer.validated_data)
        return Response(
            {
                "success": result["success"],
                "message": result["message"],
                "data": PostTransformer.transform(result["data"]),
            },
            status=result["status_code"],
        )

    @extend_schema(tags=["Posts"])
    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        result = PostService.delete(post)
        return Response(
            {
                "success": result["success"],
                "message": result["message"],
            },
            status=result["status_code"],
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        return Response({
            "success": True,
            "message": "Post fetched successfully.",
            "data": PostTransformer.transform(instance),
        })
