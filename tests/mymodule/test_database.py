import pytest

from myapp.mymodule.clientdb import *


def get_database_path():
    return r"C:\sqlLite\pythonsqlite.db"


def truncate_client_table(conn):
    sql_truncate_client_table = """ DELETE FROM client; """
    with conn:
        truncate_table(conn, sql_truncate_client_table)


@pytest.mark.create_client
def test_create_client():
    database = get_database_path()
    conn = create_connection(database)
    with conn:
        truncate_client_table(conn)
        name = 'Jane Smith'
        date = '2015-01-01'
        new_client = (name, date)
        client_id = create_client(conn, new_client)
        selectclient = (str(client_id))
        clients = select_client(conn, selectclient)
        assert len(clients) == 1
        assert clients[0][1] == name
        assert clients[0][2] == date


@pytest.mark.update_client
def test_update_client():
    database = get_database_path()
    conn = create_connection(database)
    with conn:
        truncate_client_table(conn)
        name = 'Jane Smith'
        date = '2015-01-01'
        new_client = (name, date)
        client_id = create_client(conn, new_client)
        updated_name = 'Edward Norton'
        updated_date = '2023-08-06'
        update_client(conn, (updated_name, updated_date, client_id))
        selectclient = (str(client_id))
        clients = select_client(conn, selectclient)
        assert len(clients) == 1
        assert clients[0][1] == updated_name
        assert clients[0][2] == updated_date


@pytest.mark.delete_client
def test_delete_client():
    database = get_database_path()
    conn = create_connection(database)
    with conn:
        truncate_client_table(conn)
        name = 'Jane Smith'
        date = '2015-01-01'
        new_client = (name, date)
        client_id = create_client(conn, new_client)
        deleteclient = (str(client_id))
        delete_client(conn, deleteclient)
        selectclient = (str(client_id))
        clients = select_client(conn, selectclient)
        assert len(clients) == 0
