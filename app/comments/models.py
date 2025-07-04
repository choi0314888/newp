from django.db import models
from common.models import CommonModel

# - User: FK
# - Video: FK
# - content
# - like
# - dislike

class Comment(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)  # Circular import Error 방지
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE, related_name='comments')  # Circular import Error 방지

    content = models.TextField()
    like = models.PositiveIntegerField(default=0)
    dislike = models.PositiveIntegerField(default=0)


    # 대댓글
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)