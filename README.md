# Project: XML file service 

### This project aims to parse an XML file containing data about people and enable filtering them by given criteria.

### To start the program type the following commands in the console: 
- `python main.py` - to return the whole data from XML file
- `python main.py --gender "gender"` - to return only people with selected gender
- `python main.py --rank "rank"` - to return only people with selected rank
- `python main.py --salary-range "min_salary" "max_salary"` - to return only people whose salary is within the selected range
- `python main.py --age-range "min_age" "max_age"` - to return only people whose age is within the selected range
#### For example: 
`python main.py --rank "Manager"` - to return people whose rank is manager  
`python main.py --age-range 45000 60000` - to return people whose salary is within the 45000 and 60000

### To run unit tests type the following commands in the console:
- `pytest -s tests/xml_tests.py` - to run tests on functions that process XML files
- `pytest -s tests/data_tests.py` - to run tests on functions that filters people

### If your environment has not already installed needed requirements, you can install them using pip: Run command:  
`pip install -r requirements.txt`

### In the `data` directory you will find a sample XML file named `people.xml`. You can customize it according to your needs, keeping in mind the correct structure of the file.

### If you have any questions, comments or suggestions about this program, please contact me:
- E-mail: mikolaj19gr@gmail.com
- GitHub: [88majk](https://github.com/88majk)