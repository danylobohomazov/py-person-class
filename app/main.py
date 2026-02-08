class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        need_person = find_person(result_list, person["name"])
        if "wife" in person and person["wife"] is not None:
            need_person.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            need_person.husband = Person.people[person["husband"]]
    return result_list


def find_person(persons: list[Person], name: str) -> (Person, None):
    for person in persons:
        if person.name == name:
            return person
    return None
