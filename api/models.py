from django.db import models


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    telegram_id = models.CharField(max_length=20, unique=True, null=True)  # noqa: WPS432
    login = models.CharField(max_length=20, unique=True, null=True)  # noqa: WPS432
    email = models.CharField(max_length=30, unique=True, null=False)  # noqa: WPS432

    class Meta:
        db_table = 'users'

    def __str__(self) -> str:
        return f'User: {self.login}, email: {self.email}'


class Generation(models.Model):
    uid = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    prompt = models.CharField(max_length=100, null=False)
    status = models.CharField(max_length=20, null=False)  # noqa: WPS432

    class Meta:
        db_table = 'generations'

    def __str__(self) -> str:
        return f'{self.prompt} {self.status}'


class Images(models.Model):
    uid = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=30, null=False)  # noqa: WPS432
    generation_id = models.ForeignKey(Generation, on_delete=models.CASCADE)

    class Meta:
        db_table = 'images'

    def __str__(self) -> str:
        return self.url
