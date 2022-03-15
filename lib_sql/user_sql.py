import email


class UserSQL():

    def __init__(self, cursor):
        self.cursor = cursor


    def create_table_user(self):
        query = """
            CREATE TABLE [IF NOT EXISTS] users(
            id INTEGER PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL
            );
        """
        self.cursor.execute(query)


    def add_new_user(self, name, email, password):
        query = f"""
        INSERT INTO users (name, email, password) VALUES 
        ('{name}', '{email}', '{password}');
        """
        
        self.cursor.execute(query)
        print("New user have been added successfully")
    
    def get_user(self, id):
        query = f"""
        SELECT * FROM users WHERE id={id};
        """
        self.cursor.execute(query)
        return self.cursor.fetchone() 

    
    def get_all_users(self):
        query = f"""
        SELECT * FROM users;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def delete_user(self, id):
        query = f"""
        DELETE FROM users WHERE id={id};
        """
        self.cursor.execute(query)
        print(f"User with id {id} have been deleted successfully")

    
    def update_user_name(self, id, new_name):
        query = f"""
        UPDATE users SET name='{new_name}' WHERE id={id};
        """
        self.cursor.execute(query)
        print('Name have been changed successlully')
    

    def update_user_email(self, id, new_email):
        query = f"""
        UPDATE users SET email='{new_email}' WHERE id={id};
        """
        self.cursor.execute(query)
        print('Email have been changed successlully')


    def update_user_password(self, id, new_password):
        query = f"""
        UPDATE users SET password='{new_password}' WHERE id={id};
        """
        self.cursor.execute(query)
        print('Password have been changed successlully')

    
    # def update_user_data(self, id, new_name=None, new_email=None, new_password=None):
    #     name = ''
    #     email = ''
    #     password = ''
    #     if new_name is not None:
    #         name = f"name='{new_name}'"
    #     if new_email != None:
    #         email = f"email='{new_email}'"
    #     if new_password != None:
    #         password = f"password='{new_password}'"
    #     if name != '' and email != '':
    #         name += ','
    #     if name != '' and email != '' and password != '':
    #         email += ','
    #     query = """
    #     UPDATE users SET {name}{email}{password} 
    #     """
