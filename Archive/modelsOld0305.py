__author__ = 'Zach'

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):

    # INHERITED
    # password
    # last_login
    # username
    # first_name
    # last_name
    # email
    # is_staff
    # help_text
    # is_active
    # date_joined
    security_question = models.TextField(null=True, blank=True)
    security_answer = models.TextField(null=True, blank=True)
    is_customer = models.NullBooleanField(null=True, blank=True)


class LegalEntity(models.Model):

    givenName = models.TextField(max_length=100)

    creationDate = models.DateField()

    address1 = models.TextField(max_length=200)

    address2 = models.TextField(max_length=200)

    city = models.TextField(max_length=50)

    state = models.TextField(max_length=20)

    Zip = models.TextField(max_length=20)

    email = models.TextField(max_length=50)

    phone = models.TextField(max_length=50)

    user = models.OneToOneField(User)

    familyName = models.TextField(max_length=100)

    organizationType = models.TextField(max_length=50)


class Photograph(models.Model):

    dateTaken = models.DateField()

    placeTaken = models.TextField()

    image = models.TextField()

    photographer = models.ForeignKey(LegalEntity)


class PhotographableThing(models.Model):

    Photo = models.ManyToManyField(Photograph)


class Agent(LegalEntity):

    appointmentDate = models.DateField()


class Return(models.Model):

    returnTime = models.DateField()

    feesPaid = models.DecimalField(max_digits=10, decimal_places=2)

    agent = models.ForeignKey(Agent)


class Rental(models.Model):

    rentalTime = models.DateField()

    dueDate = models.DateField()

    discountPercent = models.IntegerField()

    rentalItems = models.ManyToManyField('RentableItem', related_name='+')

    organization = models.ForeignKey(LegalEntity, related_name='+')

    customer = models.ForeignKey(LegalEntity, related_name='+')

    agent = models.ForeignKey(Agent, related_name='+')


class RentableItem(models.Model):

    condition = models.TextField()

    newDamage = models.TextField()

    damageFee = models.DecimalField(max_digits=10, decimal_places=2)

    lateFee = models.DecimalField(max_digits=10, decimal_places=2)

    returns = models.ForeignKey(Return)

    rental = models.ManyToManyField(Rental, related_name='+')


class Item(models.Model):

    name = models.TextField()

    description = models.TextField()

    value = models.TextField()

    standardPrice = models.DecimalField(max_digits=10, decimal_places=2)

    rentableItem = models.ForeignKey(RentableItem, related_name='+')

    person = models.ForeignKey(LegalEntity, related_name='+')


class WardrobeItem(models.Model):

    size = models.IntegerField()

    sizeMod = models.TextField(max_length=50)

    gender = models.TextField(max_length=10)

    color = models.TextField(max_length=50)

    pattern = models.TextField(max_length=50)

    startYear = models.DateField()

    endYear = models.DateField()

    note = models.TextField()

    item = models.ForeignKey(Item, related_name='+')


class Event(models.Model):

    startDate = models.DateField()

    endDate = models.DateField()

    mapName = models.TextField()


class Area(models.Model):

    name = models.TextField(max_length=50)

    description = models.TextField()

    placeNum = models.TextField(max_length=20)

    supervisor = models.ForeignKey(Agent, related_name='+')

    coordinator = models.ForeignKey(Agent, related_name='+')

    event = models.ForeignKey(Event, related_name='+')


class Participant(LegalEntity):

    sketch = models.TextField()

    contactRel = models.TextField()

    IDphoto = models.TextField()

    roleName = models.TextField()

    roleType = models.TextField()

    person = models.ForeignKey(LegalEntity, related_name='+')

    area = models.ManyToManyField(Area, related_name='+')


class SaleItem(models.Model):

    description = models.TextField()

    lowPrice = models.DecimalField(max_digits=10, decimal_places=2)

    highPrice = models.DecimalField(max_digits=10, decimal_places=2)

    location = models.ForeignKey(Area, related_name='+')


class PublicEvent(models.Model):

    name = models.TextField(max_length=50)

    description = models.TextField()

    event = models.ForeignKey(Event, related_name='+')


class Venue(models.Model):

    name = models.TextField(max_length=50)

    address = models.TextField(max_length=100)

    city = models.TextField(max_length=25)

    state = models.TextField(max_length=25)

    Zip = models.TextField(max_length=25)

    event = models.ForeignKey(Event, related_name='+')


class Order(models.Model):

    orderDate = models.DateField()

    phone = models.TextField(max_length=15)

    datePacked = models.DateField()

    datePaid = models.DateField()

    dateShipped = models.DateField()

    trackingNum = models.TextField()

    qty = models.IntegerField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    shippedBy = models.ForeignKey(Agent, related_name='+')

    processedBy = models.ForeignKey(Agent, related_name='+')

    packedBy = models.ForeignKey(Agent, related_name='+')


class Product(models.Model):

    name = models.TextField(max_length=50)

    description = models.TextField()

    category = models.TextField(max_length=50)

    unitPrice = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:

        abstract = True


class BulkProduct(Product):

    qtyOnHand = models.IntegerField()

    order = models.ManyToManyField(Order, related_name='+')


class IndividualProduct(Product):

    dateMade = models.DateField()

    order = models.ForeignKey(Order, related_name='+')


class PersonalProduct(Product):

    orderFormName = models.TextField()

    productionTime = models.DateField()

    orderFile = models.TextField()


class ProductPicture(models.Model):

    picture = models.TextField()

    caption = models.TextField()

    bulkProduct = models.ForeignKey(BulkProduct, related_name='+')

    individualProduct = models.ForeignKey(IndividualProduct, related_name='+')

    personalProduct = models.ForeignKey(PersonalProduct, related_name='+')
