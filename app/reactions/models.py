from django.db import models
from common.models import CommonModel
from django.db.models import Q, Count
# - User: FK
# - Video: FK
# - reaction(like, dislike, cancel)

class Reaction(CommonModel):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE) # Circular import Error 방지
    video = models.ForeignKey('videos.Video', on_delete=models.CASCADE) # Circular import Error 방지

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES= (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No Reaction')
    )

    # like(1), dislike(-1), no_reaction(0)
    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION,
    )

    @staticmethod
    def get_video_reactions(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction = Reaction.LIKE)),
            dislikes_count=Count('pk', filter=Q(reaction=Reaction.DISLIKE)),
        )

        return reactions