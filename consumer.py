# this is the consumer
from kafka import KafkaConsumer, errors, BrokerConnection


def create_consumer(config):
    consumer = KafkaConsumer(
        config.KAFKA['topic'],
        bootstrap_servers=[config.KAFKA['host']],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        api_version=(1, 0, 0),
        group_id='m-group')
    return consumer
