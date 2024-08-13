from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField, TextChoices, ForeignKey, CASCADE, IntegerField, FloatField, DateTimeField
from django.utils.timezone import now


# Create your models here.
class User(AbstractUser):
    class Role(TextChoices):
        USER = 'user', 'User'
        ADMIN = 'admin', 'Admin'

    role = CharField(max_length=20, choices=Role.choices, db_default=Role.USER)


class Product(Model):
    class Payment(TextChoices):
        PAID = 'paid', 'Paid'
        UNPAID = 'unpaid', 'Unpaid'

    class Drive(TextChoices):
        AIR = 'air', 'Air'
        VAN = 'van', 'Van'
        TRUCK = 'truck', 'Truck'

    class Status(TextChoices):
        FINISHED = 'finished', 'Finished'
        EXPECTANT = 'expectant', 'Expectant'
        ON_WAY = 'on_way', 'On way'
        IN_CHINA = 'in_china', 'In China warehouse'
        IN_UZB = 'in_uzb', 'In Uzbekistan warehouse'

    payment = CharField("Type Payment", max_length=10, choices=Payment.choices, db_default=Payment.UNPAID)
    transport = CharField("Transport", max_length=15, choices=Drive.choices)
    status = CharField("Status", max_length=255, choices=Status.choices, db_default=Status.EXPECTANT)

    price = IntegerField("Price", db_default=0, default=0)
    debt = IntegerField("Debt")

    name = CharField("Name", max_length=255)
    place = CharField("Place", max_length=255)
    current_place = CharField("Current Place", max_length=255)
    view = CharField("View", max_length=5)
    cube = IntegerField("Cube", db_default=0, default=0)
    kg = IntegerField("Kg", db_default=0, default=0)
    cube_kg = FloatField("Cube kg", db_default=0.0, default=0.0)
    owner = ForeignKey('apps.User', CASCADE, related_name='products')
    created_at = DateTimeField("Created at", auto_now=True, db_default=now())
    updated_at = DateTimeField("Updated at", auto_now_add=True, db_default=now())

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.debt = self.price
        super().save(force_insert, force_update, using, update_fields)
