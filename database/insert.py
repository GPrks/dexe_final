import sqlalchemy.exc as data_error
from datetime import datetime


def insert_classified_object(engine, classified, class_):
    try:
        class_['date_created_at'] = datetime.strptime(class_['created_at'][:-2], "%Y-%m-%dT%H:%M:%S.%f").date()
        class_['time_created_at'] = datetime.strptime(class_['created_at'][:-2], "%Y-%m-%dT%H:%M:%S.%f").time()
        with engine.connect() as connection:
            try:
                connection.execute(classified.insert(), class_)
            except data_error.IntegrityError as error:
                print(error)

    except KeyError as error:
        print(error)
