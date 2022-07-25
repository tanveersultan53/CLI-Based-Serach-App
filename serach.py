from cgitb import reset
import json

def read_file(file_name='users'):
    file_object = open(f'{file_name}.json')
    data = json.load(file_object)
    return data

while True:
    print("""
        Welcome to zendesk Search!
            * Select Search option.
            * -> Press 1 for Search Zendesk.
            * -> Press 2 for view Search Field.
            * -> Press quit to exit.
        """)
    answer = input('Enter your Option---> : ')
    
    if answer  == '1':
        result = []
        print("""
            * Select option. 1.) User 2.) Tickets 3.) Organization
        """)
        search_db = input('Select Search Database ---> : ')
        if search_db == '1':
            file_name = 'users'
            data =read_file(file_name)
            print(f"""
            {data[0].keys()}
            """)
            field_name = input("Enter field name to implement search!")
            field_value = str(input("Enter field value to search!:"))
            for item in data:
                if field_name in item.keys():
                    result = [x for x in data if field_value in str(x[field_name])]
            print(json.dumps(result, indent=4, sort_keys=True))
        elif search_db =='2':
            file_name = 'tickets'
            data =read_file(file_name)
            print(f"""
            {data[0].keys()}
            """)
            field_name = input("Enter field name to implement search!")
            field_value = str(input("Enter field value to search!:"))
            for item in data:
                if field_name in item.keys():
                    result = [x for x in data if field_value in str(x[field_name])]
            print(json.dumps(result, indent=4, sort_keys=True))
        elif search_db  == '3':
            file_name ='organizations'
            data =read_file(file_name)
            print(f"""
            {data[0].keys()}
            """)
            field_name = input("Enter field name to implement search!")
            field_value = str(input("Enter field value to search!:"))
            for item in data:
                if field_name in item.keys():
                    result = [x for x in data if field_value in str(x[field_name])]
            print(json.dumps(result, indent=4, sort_keys=True))
        else:
            print("select invalid option")
    elif answer  == '2':
        print("""
                * Select option. 1.) User 2.) Tickets 3.) Organization
            """)
        search_db = input('Select Search Database ---> : ')
        if search_db == '1':
            file_name = 'users'
            data =read_file(file_name)
            print(f"""
            {data[0].keys()}
            """)
        elif search_db =='2':
            file_name = 'tickets'
            data =read_file(file_name)
            print(f"""
            {data[0].keys()}
            """)
        elif search_db  == '3':
            file_name ='organizations'
            data =read_file(file_name)
            print(f"""
            {data[0].keys()}
            """)
        else:
            print("select invalid option")
    elif answer.lower() == 'quit':
        print("""
        Thanks using Zendesk Search.
        """)
        exit()
