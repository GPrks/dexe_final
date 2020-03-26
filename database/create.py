import sqlalchemy as db


def create_table(metadata, name):
    if name == 'Classifieds':
        cls_table = db.Table(name, metadata,
                             db.Column('id', db.String(40), primary_key=True, nullable=False),
                             db.Column('date_created_at', db.Date, index=True),
                             db.Column('time_created_at', db.Time, index=True),
                             db.Column('customer_id', db.String(40)),
                             db.Column('ad_type', db.String(16)),
                             db.Column('text', db.Text), db.Column('price', db.Float),
                             db.Column('currency', db.String(16)),
                             db.Column('payment_type', db.String(16)), db.Column('payment_cost', db.Float))
        db.Index('idx_date_time', cls_table.c.date_created_at, cls_table.c.time_created_at)
        metadata.create_all

    elif name == 'AvgMarginHourly':
        amh_table = db.Table(name, metadata,
                             db.Column('id', db.Integer, primary_key=True, nullable=False, autoincrement=True),
                             db.Column('time', db.Integer, index=True),
                             db.Column('date', db.Date, index=True),
                             db.Column('margin_avg', db.Float),
                             db.Column('payment_type', db.String(16)), db.Column('ad_type', db.String(16)))
        db.Index('idx_date_time', amh_table.c.date, amh_table.c.time)
        metadata.create_all()
    else:
        print('Invalid Name of table')
