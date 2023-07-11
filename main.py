import psycopg2


def create_table(cur):
    cur.execute("""
        CREATE table IF NOT EXISTS contacts(
            id_contacts SERIAL PRIMARY KEY,
            name VARCHAR(25),
            lastname VARCHAR(25),
            email VARCHAR(40)
        );""")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS numbers(
        number VARCHAR(20) UNIQUE,
        id_number INTEGER REFERENCES contacts(id_contacts));    
         """)


def new_client(cur, name, lastname, email):
    cur.execute("""
    INSERT INTO contacts (name, lastname, email) values(%s, %s, %s)
    ;""", (name, lastname, email))


def new_number(cur, id_number, number):
    cur.execute("""
    INSERT INTO numbers (id_number, number) VALUES(%s, %s);    
    """, (id_number, number))

def change_contact():
    print(f'Для изменения данных о сотруднике выберите пункт:'
          f'1 - имя'
          f'2 - фамилия'
          f'3 - email'
          f'4 - номер телефона ')
    while True:
        choice = int(input())
        if choice == 1:
            input_id = input (f'введите id сотрудника')
            change_name = input(f'Введите новое имя сотрудника')
            cur.execute("""
            UPDATE contacts SET name=%s WHERE id_contacts=%s;
            """, (change_name, input_id))
            break
        elif choice == 2:
            input_id = input (f'введите id сотрудника')
            change_lastname = input(f'введите фамилию сотрудника')
            cur.execute("""
            UPDATE contact SET lastname=%s WHERE id=%s;
            """, (change_lastname, input_id))
            break
        elif choice == 3:
            input_id = input (f'введите id сотрудника')
            change_email = input(f'Введите почту сотрудника')
            cur.execute("""
            UPDATE contact SET email=%s WHERE id=%s;
            """, (change_email, input_id))
            break

        elif choice == 4:
            input_id = input(f'введите id сотрудника')
            change_number = input(f'Введите телефон сотрудника')
            cur.execute("""
            UPDATE numbers SET number=%s WHERE number=%s;
            """, (change_number, input_id))
            break

        else:
            print(f'Введите корректное значение')


def delete_number():
    input_id_del_number = input(f'Введите id сотрудника для удаления номера')
    input_del_number = input(f'Введите номер для удаления')
    cur.execute("""
    DELETE FROM numbers WHERE number=%s AND id_number = %s;
    """, (input_del_number, input_id_del_number))

def delete_client():
    input_id_for_deleting_client = input("Введите id клиента которого хотите удалить: ")
    input_client_lastname_for_deleting = input("Введите фамилию клиента которого хотите удалить: ")
    with conn.cursor() as cur:
        cur.execute("""
        DELETE FROM numbers WHERE id_number=%s
        """, (input_id_for_deleting_client,))
        cur.execute("""
        DELETE FROM contacts WHERE id_contacts=%s AND lastname=%s
        """, (input_id_for_deleting_client, input_client_lastname_for_deleting))


def search_contact():
    print(f" Введите значение соответствующее критерию поиска:\n"
    f'1 - поиск по ID,\n'
    f' 2- поиск по имени,\n'
    f' 3 - поиск по фамилии,\n'
    f' 4 - поиск по email,\n'
    f' 5 - поиск по телефону')
    while True:
        meaning_search = int(input(f'Введите значение'))
        if meaning_search == 1:
            input_id_contact = input(f'Введите id контакта ')
            cur.execute('''
            SELECT id_contacts, name, lastname, email, number
            FROM contacts AS c
            JOIN numbers AS n ON n.id_number = c.id_contacts
            WHERE id_contacts = %s     
            ''', (input_id_contact,))
            print(cur.fetchall())

        elif meaning_search == 2:
            input_name = input(f'Введите имя контакта')
            cur.execute('''
                        SELECT id_contacts, name, lastname, email, number
                        FROM contacts AS c
                        JOIN numbers AS n ON n.id_number = c.id_contacts
                        WHERE name = %s     
                        ''', (input_name,))
            print(cur.fetchall())


        elif meaning_search == 3:
            input_lastname = input(f'Введите фамилию контакта')
            cur.execute('''
                        SELECT id_contacts, name, lastname, email, number
                        FROM contacts AS c
                        JOIN numbers AS n ON n.id_number = c.id_contacts
                        WHERE lastname = %s     
                        ''', (input_lastname,))
            print(cur.fetchall())


        elif meaning_search == 4:
            input_email = input(f'Введите почту контакта')
            cur.execute('''
                        SELECT id_contacts, name, lastname, email, number
                        FROM contacts AS c
                        JOIN numbers AS n ON n.id_numbers = c.id_contacts
                        WHERE email = %s     
                        ''', (input_email,))
            print(cur.fetchall())


        elif meaning_search == 5:
            input_number = input(f'Введите номер телефона контакта')
            cur.execute('''
                        SELECT id_contacts, name, lastname, email, number
                        FROM contacts AS c
                        JOIN numbers AS n ON n.id_numbers = c.id_contacts
                        WHERE number = %s     
                        ''', (input_number,))
            print(cur.fetchall())


        elif meaning_search == 2:
            input_name = input(f'Введите имя контакта')
            cur.execute('''
                        SELECT id_contacts, name, lastname, email, number
                        FROM contacts AS c
                        JOIN numbers AS n ON n.id_number = c.id_contacts
                        WHERE name = %s     
                        ''', (input_name,))
            print(cur.fetchall())

        else:
            print(f'Введите корректное значение')



def demonstration(cur):
    cur.execute('''
    SELECT * FROM contacts   
    ''')
    print(cur.fetchall())
    cur.execute('''
    SELECT * FROM numbers
    ''')
    print(cur.fetchall())


with psycopg2.connect(database="contacts", user="postgres", password="McDonalds106") as conn:
    with conn.cursor() as cur:
        create_table(cur)
        demonstration(cur)
        new_client(cur, 'Сергей', 'Лавров', 'lavrov@mail.ru')
        new_client(cur, 'Леха', 'Спириденков', 'leha@yandex.ru')
        new_client(cur, 'Наталья', 'Чалова', 'chalova@rambler.ru')
        new_number(cur, 1, '11111111111')
        new_number(cur, 2, '22222222222')
        new_number(cur, 3, '33333333333')
        change_contact()
        delete_number()
        delete_client()
        search_contact()


conn.close()




