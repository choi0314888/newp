from rest_framework import serializers
from .models import Video
from users.serializers import UserInfoSerializer
from comments.serializers import CommentSerializer
from reactions.models import Reaction
class VideoListSerializer(serializers.ModelSerializer):
    # Video:User => Video(FK) -> User
    user = UserInfoSerializer(read_only=True) # Video(FK)

    class Meta:
        model = Video
        fields = "__all__"



class VideoDetailSerializer(serializers.ModelSerializer):

    # Video:User => Video(FK) -> User
    user = UserInfoSerializer(read_only=True) # Video(FK)

    # Video:Comment -> Video -> Comment(FK)
    # 부모가 자녀를 찾을 때 ->_set으로 부모에 속한 자녀들을 모두 찾을 수 있다.
    comments = CommentSerializer(many=True, read_only=True)

    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = "__all__"

    def get_reactions(self, video):
        return Reaction.get_video_reactions(video)

# docker-compose run --rm app sh -c 'python manage.py makemigrations'
# docker-compose run --rm app sh -c 'python manage.py migrate'