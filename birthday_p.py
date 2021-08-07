import datetime
import random


def getBirthdays(numberOfBirthdays):
    """ Returns a list birthday date objects"""
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        # random day
        randomDay = datetime.timedelta(random.randint(0, 364))

        # random birthday
        birthday = startOfYear + randomDay
        birthdays.append(birthday)
    return birthdays


def get_match(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None  # No duplicate birthdays

    for a, birthdayA in enumerate(birthdays):
      for b, birthdayB in enumerate(birthdays[a + 1 : ]):
        if birthdayA == birthdayB:
          return birthdayA


print(get_match(getBirthdays(10)))
