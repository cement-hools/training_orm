from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
        )


class Station(models.Model):
    station_name = models.TextField()

    def __str__(self):
        return self.station_name

class Operator(models.Model):
    name = models.TextField()
    # station = models.ForeignKey(
    #     Station, on_delete=models.CASCADE, related_name="station")

    def __str__(self):
        return self.name

class Work_in_station(models.Model):
    operator = models.ForeignKey(
        Operator, on_delete=models.CASCADE, related_name="operator")
    station = models.ForeignKey(
        Station, on_delete=models.CASCADE, related_name="station")

    def __str__(self):
        name = (f"{self.operator}: {self.station}")
        return name
