from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from project.api.serializers.comments import CommentSerializer
from project.restaurant.feed.models import Review


class CreateCommentOnReviewView(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = CommentSerializer
    queryset = Review.objects.all()

    def post(self, request):
        review = self.get_object()
        print('review', review)
        serializer = self.get_serializer(
            data=request.data,
            context={
                'request': request,
                'review': review,
            },
        )
        print('review')
        serializer.is_valid(raise_exception=True)
        comment = serializer.create(serializer.validated_data)
        return Response(CommentSerializer(comment).data)


class DeleteCommentOnReviewView(GenericAPIView):
    permission_classes = [
        IsAuthenticated,
    ]

    queryset = Review.objects.all()

    def delete(self, request, **kwargs):
        comment = self.get_object()
        comment.delete()
        return Response('OK')
