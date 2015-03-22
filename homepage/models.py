__author__ = 'Zach'

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):

    # is_staff = models.BooleanField(default=False)

    # is_superuser = models.BooleanField(default=False)

    # is_active = models.BooleanField(default=True)

    security_question = models.TextField(null=True, blank=True)

    security_answer = models.TextField(null=True, blank=True)

    phone = models.TextField(max_length=20)

    organizationType = models.TextField(max_length=50)

    is_agent = models.NullBooleanField(null=True, blank=True)

    appointmentDate = models.DateField(null=True)


class Photograph(models.Model):

    dateTaken = models.DateField(null=True, blank=True)

    placeTaken = models.TextField(null=True, blank=True)

    image = models.TextField()

    photographer = models.ForeignKey(User)


class PhotographableThing(models.Model):

    Photo = models.ManyToManyField(Photograph)


class Rental(models.Model):

    rentalTime = models.DateField()

    dueDate = models.DateField()

    discountPercent = models.IntegerField(null=True, blank=True)

    returnTime = models.DateField(null=True)

    returned = models.NullBooleanField(null=True, blank=True)

    feesPaid = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    customer = models.ForeignKey(User, related_name='+', null=True)

    agent = models.ForeignKey(User, related_name='+', null=True)

    def __str__(self):
        return (self.rentableItem, self.returnTime)


class RentableItem(models.Model):

    condition = models.TextField()

    newDamage = models.TextField(null=True, blank=True)

    damageFee = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    lateFee = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    rental = models.ManyToManyField(Rental, related_name='+', null=True)


class Item(models.Model):

    name = models.TextField()

    description = models.TextField()

    value = models.TextField()

    standardPrice = models.DecimalField(max_digits=10, decimal_places=2)

    rentableItem = models.ForeignKey(RentableItem, related_name='+', null=True)

    person = models.ForeignKey(User, related_name='+', null=True)


class WardrobeItem(models.Model):

    size = models.IntegerField()

    sizeMod = models.TextField(max_length=50)

    gender = models.TextField(max_length=10)

    color = models.TextField(max_length=50)

    pattern = models.TextField(max_length=50)

    startYear = models.TextField(max_length=50)

    endYear = models.TextField(max_length=50)

    note = models.TextField(null=True, blank=True)

    rentableItem = models.ForeignKey(RentableItem, related_name='+', null=True)

    item = models.ForeignKey(Item, related_name='+', null=True)


class Event(models.Model):

    startDate = models.DateField()

    endDate = models.DateField()

    mapName = models.TextField()

    venueName = models.TextField(null=True, blank=True)


class Address(models.Model):

    address1 = models.TextField(max_length=100)

    address2 = models.TextField(max_length=100, null=True, blank=True)

    city = models.TextField(max_length=50)

    state = models.TextField(max_length=20)

    ZIP = models.TextField(max_length=10)

    user = models.OneToOneField(User, null=True)

    event = models.ForeignKey(Event, related_name='+', null=True)

    def __str__(self):
        Address = self.address1 + self.address2 + self.city + self.state + self.ZIP
        return (Address)


class Area(models.Model):

    name = models.TextField(max_length=50)

    description = models.TextField(null=True, blank=True)

    placeNum = models.TextField(max_length=20)

    supervisor = models.ForeignKey(User, related_name='+', null=True)

    coordinator = models.ForeignKey(User, related_name='+', null=True)

    event = models.ForeignKey(Event, related_name='+', null=True)


class Participant(models.Model):

    sketch = models.TextField(null=True, blank=True)

    contactRel = models.TextField(null=True, blank=True)

    IDphoto = models.TextField(null=True, blank=True)

    roleName = models.TextField(null=True, blank=True)

    roleType = models.TextField(null=True, blank=True)

    person = models.ForeignKey(User, related_name='+', null=True)

    area = models.ManyToManyField(Area, related_name='+', null=True)


class SaleItem(models.Model):

    description = models.TextField(null=True, blank=True)

    lowPrice = models.DecimalField(max_digits=10, decimal_places=2)

    highPrice = models.DecimalField(max_digits=10, decimal_places=2)

    location = models.ForeignKey(Area, related_name='+', null=True)


class PublicEvent(models.Model):

    name = models.TextField(max_length=50)

    description = models.TextField()

    event = models.ForeignKey(Event, related_name='+', null=True)


class Order(models.Model):

    orderDate = models.DateField()

    phone = models.TextField(max_length=15)

    datePacked = models.DateField()

    datePaid = models.DateField()

    dateShipped = models.DateField()

    trackingNum = models.TextField()

    qty = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    shippedBy = models.ForeignKey(User, related_name='+', null=True)

    customer = models.ForeignKey(User, related_name='+', null=True)


class Product(models.Model):

    name = models.TextField(max_length=50)

    description = models.TextField(null=True, blank=True)

    category = models.TextField(max_length=50)

    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)

    qtyOnHand = models.IntegerField()

    pictureFileName = models.TextField(max_length=100)

    company = models.ForeignKey(User, related_name='+', null=True)

    order = models.ForeignKey(Order, related_name='+', null=True)



# class ProductPicture(models.Model):
#
#     picture = models.TextField()
#
#     caption = models.TextField()
#
#     product = models.ForeignKey(Product, related_name='+', null=True)


