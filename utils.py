from faker import Faker
import pytest
import random


class Utils:
    def my_email():
        return "Danila_Stepanov_53_140@yandex.ru"

    def my_password():
        return "1234q!"

    def generate_name():
        return Faker().name()

    def generate_email(): 
        return f"{Faker().user_name()}@yandex.ru" 

    def generate_password():
        return Faker().password()

    def generate_password_length_lower_than_6():
        return Faker().password(length=random.randint(4,5))