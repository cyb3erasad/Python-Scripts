from faker import Faker
from typing import List
import json

fake = Faker(['it_IT', 'en_US', 'ja_JP'])

def generate_fake_profiles(num_profiles: int) -> list[dict]:
    profiles = []
    for _ in range(num_profiles):
        profile = {
            "Locale": fake.locales,
            "Name": fake.name(),
            "Email": fake.email(),
            "SSN": fake.ssn(),
            "Address": fake.address(),
            "Latitude": float(fake.latitude()),
            "Longitude": float(fake.longitude()),
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

def save_profiles_to_file(profiles: List[dict], filename: str) -> None:
    try:
        with open(filename, "w") as file:
            json.dump(profiles, file, indent=4)
            print(f"Profiles successfully saved to {filename}")
    except Exception as e:
        print(f"Error while saving profiles in file: {e}")
        
def main():
    print("====== Faker Profile Generator ======")
    try:
        num_profiles = int(input("Enter number of profiles to generate: "))
        if num_profiles < 1:
            raise ValueError("Number of profiles must be greater than 0")
        
        profiles = generate_fake_profiles(num_profiles)
        display_profiles(profiles)

        save_option = input("Do you want to save the profiles to a file? (y/n): ").strip().lower()
        if save_option == "y":
            filename = input("Enter a filename (e.g., profiles.json): ").strip()
            save_profiles_to_file(profiles, filename)

        print("\n Process completed successfully")
    except ValueError as ve:
        print(f"Invalid error: {ve}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")        

if __name__ == "__main__":
    main()