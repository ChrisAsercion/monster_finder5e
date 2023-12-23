from django.db import models

class Monster(models.Model):
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    armor_class = models.IntegerField()
    hit_points = models.IntegerField()
    hit_dice = models.CharField(max_length=255)
    speed = models.JSONField()  # Use JSONField for complex data like speed
    strength = models.IntegerField()
    dexterity = models.IntegerField()
    constitution = models.IntegerField()
    intelligence = models.IntegerField()
    wisdom = models.IntegerField()
    charisma = models.IntegerField()
    skills = models.JSONField()
    damage_vulnerabilities = models.CharField(max_length=255)
    damage_resistances = models.CharField(max_length=255)
    damage_immunities = models.CharField(max_length=255)
    condition_immunities = models.CharField(max_length=255)
    challenge_rating = models.CharField(max_length=10)
    actions = models.JSONField()
    special_abilities = models.JSONField()
    spell_list = models.JSONField()
    page_no = models.IntegerField()
    environments = models.JSONField()
    img_main = models.URLField()

    def __str__(self):
        return self.name
