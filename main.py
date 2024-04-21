import argparse
from models.people import People
from services.xml_service import get_root
from services.data_service import filter_people


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gender')
    parser.add_argument('--rank')
    parser.add_argument('--salary-range', nargs=2, type=float,
                        metavar=('min_salary', 'top_salary'), dest='salary_range')
    parser.add_argument('--age-range', nargs=2, type=int,
                        metavar=('min_age', 'top_age'), dest='age_range')
    args = parser.parse_args()

    root = get_root('data/people.xml')
    people = People(root)

    filtered_people = filter_people(people.people_list, age_range=args.age_range, gender=args.gender,
                                    rank=args.rank, salary_range=args.salary_range)

    for person in filtered_people:
        print(vars(person))


if __name__ == "__main__":
    main()
