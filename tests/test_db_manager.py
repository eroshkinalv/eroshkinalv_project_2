def test_db_init(db_a):

    assert db_a._host == "localhost"
    assert db_a._port == "5432"
    assert db_a._database == "test"
    assert db_a._user == "postgres"
    assert db_a._password == "123zaq"
