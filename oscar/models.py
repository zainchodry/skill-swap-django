from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    is_verified = models.BooleanField(default=False)



class Skill(models.Model):
    name = models.CharField(max_length = 100, null=False, blank=False)

    def __str__(self):
        return self.name
    


class SkillOffer(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='skill_offers')
    skill = models.ForeignKey(Skill, on_delete = models.CASCADE, related_name='skill_offers')
    available_time = models.CharField(max_length = 100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} offers {self.skill.name} at {self.available_time}"
    


class SkillRequest(models.Model):
    requester = models.ForeignKey(User, on_delete = models.CASCADE, related_name='skill_requests')
    skill = models.ForeignKey(Skill, on_delete = models.CASCADE, related_name='skill_requests')
    description = models.TextField()
    status = models.CharField(max_length = 20, default = 'open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.requester.username} requests {self.skill.name} - Status: {self.status}"
    


class Match(models.Model):
    offer = models.ForeignKey(SkillOffer, on_delete = models.CASCADE, related_name='matches')
    request = models.ForeignKey(SkillRequest, on_delete = models.CASCADE, related_name='matches')
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Match between {self.offer.user.username} and {self.request.requester.username} for {self.offer.skill.name}"
    


class Review(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='given_reviews')
    matched_user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='received_reviews')
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"Review by {self.user.username} for {self.matched_user.username} - Rating: {self.rating}"
    



