import sqlalchemy as db
from database.create import create_table
from sqlalchemy.exc import OperationalError


def init_db(config):
    try:
        engine = db.create_engine('mysql://' + config.MYSQL['user'] + ':' + config.MYSQL[
            'pass'] + '@' + config.MYSQL['host'] + '/' + config.MYSQL['schema'])
        metadata = db.MetaData(engine)
        for tn in ['Classifieds', 'AvgMarginHourly']:
            if not engine.dialect.has_table(engine, tn):
                create_table(metadata, tn)
                print('Table ' + "'" + tn + "',was created Successfully!")
        cls = db.Table('Classifieds', metadata, autoload=True, autoload_with=engine)
        return engine, cls
    except OperationalError as error:
        print(error)
