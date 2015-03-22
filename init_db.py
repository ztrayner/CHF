#!/usr/bin/env python3


# initialize django
import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'firstProject.settings'
import django

django.setup()
import homepage.models as hmod

from django.db import connection
import subprocess
# ########### DROP DATABASE, RECREATE IT, THEN MIGRATE IT ################ #

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

# drop the tables


# create users
u = hmod.User()
u.first_name = "Zach"
u.last_name = "Trayner"
u.set_password("admin")
u.username = "admin"
u.is_superuser = True
u.save()

u = hmod.User()
u.first_name = "Michael"
u.last_name = "Tyson"
u.set_password("sony")
u.username = "sony"
u.is_superuser = True
u.save()

u = hmod.User()
u.first_name = "Jackie"
u.last_name = "Chan"
u.set_password("jackie")
u.username = "jackie"
u.is_superuser = False
u.save()

u = hmod.User()
u.first_name = "test"
u.last_name = "test"
u.set_password("test")
u.username = "test"
u.is_superuser = False
u.save()

# create photos
for data in [
    ["2015-04-11", "Sierra Park", "Bacon", "1"],
    ["2015-06-29", "Timpanogos", "Chicken", "1"],
]:
    p = hmod.Photograph()
    p.dateTaken = data[0]
    p.placeTaken = data[1]
    p.image = data[2]
    p.photographer_id = data[3]
    p.save()

# create photographable thing
for data in [
    ["1"],
    ["2"],
]:
    p = hmod.PhotographableThing()
    p.Photo_id = data[0]
    p.save()

# create rentals
for data in [
    ["2015-04-11", "2015-05-11", "50", "2015-04-29", True, "10.97", "2", "3"],
    ["2015-06-29", "2015-08-11", "70", "2015-07-29", True, "280.99", "2", "1"],
]:
    r = hmod.Rental()
    r.rentalTime = data[0]
    r.dueDate = data[1]
    r.discountPercent = data[2]
    r.returnTime = data[3]
    r.returned = data[4]
    r.feesPaid = data[5]
    r.customer_id = data[6]
    r.agent_id = data[7]
    r.save()

# create rentable items
for data in [
    ["new", "none", "0.0", "10.97", "1"],
    ["used", "yes, ripped.", "280.99", "5.99", "2"],
]:
    r = hmod.RentableItem()
    r.condition = data[0]
    r.newDamage = data[1]
    r.damageFee = data[2]
    r.lateFee = data[3]
    r.rental_id = data[4]
    r.save()

# create items
for data in [
    ["knife", "big", "20", "10.97"],
    ["saddle", "brown, long coat", "250", "100"],
    ["coat", "brown, long coat", "50", "25"],
    ["skit", "full length", "75", "60"],
]:
    r = hmod.Item()
    r.name = data[0]
    r.description = data[1]
    r.value = data[2]
    r.standardPrice = data[3]
    r.save()

# create Wardrobe items
for data in [
    ["34", "none", "M", "Brown", "None", "1830", "1850"],
    ["6", "none", "F", "Brown", "None", "1830", "1850"],
]:
    r = hmod.WardrobeItem()
    r.size = data[0]
    r.sizeMod = data[1]
    r.gender = data[2]
    r.color = data[3]
    r.pattern = data[4]
    r.startYear = data[5]
    r.endYear = data[6]
    r.save()

# create Event
for data in [
    ["2016-03-14", "2016-03-16", "Kiwana", "Party"],
    ["2016-04-06", "2016-04-09", "Park", "Colonial"],
]:
    r = hmod.Event()
    r.startDate = data[0]
    r.endDate = data[1]
    r.mapName = data[2]
    r.venueName = data[3]
    r.save()

# create Product
for data in [
    ["keychain", "gold knife", "bulk", "5", "100", "keychain.jpg"],
    ["cup", "with CHF on it", "bulk", "25", "50", "cup.jpg"],
]:
    r = hmod.Product()
    r.name = data[0]
    r.description = data[1]
    r.category = data[2]
    r.unitPrice = data[3]
    r.qtyOnHand = data[4]
    r.pictureFileName = data[5]
    r.save()