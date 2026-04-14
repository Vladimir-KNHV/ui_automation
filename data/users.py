from models.user import User
from faker import Faker

fake = Faker('ru_RU')

TEST_USER_1 = User(
    name=fake.first_name(),
    phone=fake.msisdn()[:10],
    city = "г Саратов, Саратовская обл.",
    address = fake.street_address(),
    comment = fake.text(max_nb_chars=20),
    email=fake.email()
)