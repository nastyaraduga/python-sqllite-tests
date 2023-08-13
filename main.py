from myapp.mymodule.clientdb import *

def main():
    database = r"C:\sqlLite\pythonsqlite.db"
    create_database(database)
    
if __name__ == '__main__':
    main()