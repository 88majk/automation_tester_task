import xml.etree.ElementTree as ET
from models.person import Person


class People:

    def __init__(self, element_tree: ET):
        self.people_list = []
        if element_tree is not None:
            for person in element_tree.findall('./person'):
                self.people_list.append(Person(
                    person.find('name').text,
                    person.find('surname').text,
                    int(person.find('age').text),
                    person.find('gender').text,
                    person.find('rank').text,
                    float(person.find('salary').text))
                )
