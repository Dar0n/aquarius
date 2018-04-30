from django.db import models

from django.conf import settings
from django.utils import timezone

from django_countries.fields import CountryField
from django.core.validators import RegexValidator, MaxValueValidator

# This class is used for keeping track of updates history for reviews
from django_extensions.db.models import TimeStampedModel


class ReviewUpdateHistory(models.Model):
    review = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,

    )
    updated = models.DateTimeField(
        verbose_name='last_update',
    )


class Review(TimeStampedModel):
    content = models.TextField(
        verbose_name="content"
    )
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",  # backwords relation - with this reference we can get all the posts from user
        null=True
    )
    rating_validator = MaxValueValidator(5, message='The rating must be an integer number between 1 and 5.')
    rating = models.DecimalField(
        verbose_name='Rating',
        validators=[rating_validator, ],
        max_digits=1,
        decimal_places=0,
        null=True
    )
    restaurant = models.ForeignKey(
        verbose_name="restaurant",
        to="restaurant.Restaurant",  # appname.modelname - without precise internal structure
        on_delete=models.CASCADE,
        related_name="review",
        null=True,
        blank=True,
    )

    # created = models.DateTimeField(
    #     verbose_name="created",
    #     auto_now_add=True,
    # )
    # comment = ...
    # M:1 relation with Comment, specified on Comment model

    # review_like = ...
    # M:1 relation with ReviewLike, specified on ReviewLike model

    # TODO! make sure we don't need 'created' field when using ReviewUpdateHistory model

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'  # overwriting defaults
        unique_together = [
            ('restaurant', 'user'),
            # ('review_like', 'user'),
        ]
        # ordering = ["-created"]  # now we dont need to make descending order when calling posts in views

    def __str__(self):
        return self.content[:50]

    # This part here is to automatically create new ReviewUpdateHistory ovject every time there are changes to
    # the model. Explanation here: https://stackoverflow.com/questions/19232352/django-multiple-update-dates-in-one-
    # field?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    def save(self, *args, **kwargs):
        super(Review, self).save(*args, **kwargs)
        ReviewUpdateHistory.objects.create(review=self, updated=timezone.now())


class ReviewLike(models.Model):
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_review_likes",
        null=True
    )
    review = models.ForeignKey(
        verbose_name="review",
        to="restaurant.Review",  # appname.modelname - without precise internal structure
        on_delete=models.CASCADE,
        related_name="review_likes",
    )

    class Meta:
        verbose_name = "Review like"
        verbose_name_plural = "Review likes"  # overwriting defaults
        unique_together = [
            ("user", "review"),
        ]


class Restaurant(models.Model):
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_restaurants",
        null=True
    )

    name = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = CountryField()
    zip = models.CharField(
        max_length=9,
        verbose_name='ZIP',
        null=True
    )
    website = models.URLField('Website', max_length=150, null=True)
    # next line is creating validator for regex which will be then used for phone number charfiled.
    # This will make sure that the entered value will follow desired pattern
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # validators should be a list
    email = models.EmailField('Email', max_length=70, blank=True)
    image = models.ImageField(upload_to='restaurants/', null=True, blank=True)
    category = models.ForeignKey(
        verbose_name='category',
        to='restaurant.Category',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    # opening_hours
    # Price level

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# This class is used for keeping track of updates history for comments
class CommentUpdateHistory(models.Model):
    comment = models.ForeignKey(
        'Comment',
        on_delete=models.CASCADE,

    )
    updated = models.DateTimeField(
        verbose_name='last_update',
    )


class Comment(models.Model):
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_comments",
        null=True
    )
    review = models.ForeignKey(
        verbose_name="review",
        to='restaurant.Review',
        on_delete=models.CASCADE,
        related_name="comment",
        null=True
    )
    content = models.TextField(
        verbose_name="content"
    )

    def __str__(self):
        return self.content[:50]


class CommentLike(models.Model):
    user = models.ForeignKey(
        verbose_name="user",
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="user_comment_likes",
        null=True
    )
    comment = models.ForeignKey(
        verbose_name="comment",
        to="restaurant.Comment",  # appname.modelname - without precise internal structure
        on_delete=models.CASCADE,
        related_name="comment_likes",
    )

    class Meta:
        verbose_name = "Comment like"
        verbose_name_plural = "Comment likes"  # overwriting defaults
