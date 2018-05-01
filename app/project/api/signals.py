from project.user.feed.models import User


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = User.objects.create(user=kwargs['instance'])
        return user_profile
