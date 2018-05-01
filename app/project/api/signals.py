from project.user.feed.models import ProfileUser


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = ProfileUser.objects.create(user=kwargs['instance'])
        return user_profile
