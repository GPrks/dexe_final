import config
from database import insert
from json import loads, decoder
from database import initialize
from consumer import create_consumer

if __name__ == '__main__':

    # initialize db if tables don't exist
    try:
        engine, cls = initialize.init_db(config)
    except TypeError as error:
        print('Failed to connect with Database. <', error, '>')
    consumer = create_consumer(config)
    try:
        # print(consumer.config)
        for message in consumer:
            # print(message)
            try:
                message = loads(message.value)
                try:
                    insert.insert_classified_object(engine, cls, message)
                except NameError as error:
                    print('Failed to connect with Database. <', error, '>')
                    exit()
            # catch errors in JSON format of the message.value
            except decoder.JSONDecodeError as e:
                print(e)
    except TypeError as error:
        print(error, '\n\tconsumer is: ', consumer)
