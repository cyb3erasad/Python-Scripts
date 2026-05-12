from faker import Faker
from typing import List
import json

fake = Faker(['it_IT', 'en_US', 'ja_JP'])

def generate_fake_profiles(num_profiles: int) -> list[dict]:
    profiles = []
    for _ in range(num_profiles):
        profile = {
            "locale": fake.locales,
            "Name": fake.name(),
            "Email": fake.email(),
            "SSN": fake.ssn(),
            "Address": fake.address(),
            "Latitude": fake.latitude(),
            "Longitude": fake.longitude(),
            "Url": fake.url()
        }
        profiles.append(profile)
    return profiles

def  display_profiles(profiles: List[dict]):
    for index, profile in enumerate(profiles, start=1):
        print(f"\n### Faker Profile {index} ###")
        print(f"Locale : {', '.join(profile['Locale'])}")
        print(f"Name : {profile['Name']}")
        print(f"Email : {profile['Email']}")
        print(f"Social Security Number : {profile['SSN']}")
        print(f"Address : {profile['Address']}")
        print(f"Location : {profile['Latitude']}, {profile['Longitude']}")
        print(f"Url : {profile['Url']}")
        print("-" * 40)
