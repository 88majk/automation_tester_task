# Function that filters people depending on the value and type of argument given in the function call.
# Return the whole data from XML for zero given arguments.
def filter_people(people, **kwargs):
    filtered_people = []
    if all(value is None for key, value in kwargs.items()):
        return people
    else:
        for key, value in kwargs.items():
            if key == 'gender' and value is not None:
                filtered_people = [person for person in people if person.gender == value]
            if key == 'rank' and value is not None:
                filtered_people = [person for person in people if person.rank == value]
            elif key == 'salary_range' and value is not None:
                min_salary, top_salary = value
                if min_salary <= top_salary:
                    filtered_people = [person for person in people if top_salary >= person.salary >= min_salary]
                else:
                    print("Incorrect salary range!")
                    filtered_people = []
            elif key == 'age_range' and value is not None:
                min_age, top_age = value
                if min_age <= top_age:
                    filtered_people = [person for person in people if top_age >= person.age >= min_age]
                else:
                    print('Incorrect age range!')
                    filtered_people = []

    if len(filtered_people) == 0:
        print("No person meeting the selected criteria.")
        return filtered_people
    else:
        return filtered_people
