import datasette


@datasette.hookimpl
def startup(datasette):
    db = datasette.get_internal_database()
    datasette.add_database(db, name="_internal", route="_internal")
