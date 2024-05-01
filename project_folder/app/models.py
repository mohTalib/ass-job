# app/models.py
from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=100)
    role = fields.CharField(max_length=50)


class Doctor(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    patients = fields.ManyToManyField("models.Patient", related_name="doctors")

class Patient(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    medical_info = fields.TextField()
