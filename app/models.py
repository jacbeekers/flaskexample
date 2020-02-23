from dateutil.utils import today
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Table
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""

class Dataset(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = False, nullable=False)

    def __repr__(self):
        return self.name


class DataQualityRule(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_attribute_rule = Table('attribute_rule', Model.metadata, Column('id', Integer, primary_key=True),
                             Column('attribute_id', Integer, ForeignKey('attribute.id')),
                             Column('rule_id', Integer, ForeignKey('data_quality_rule.id'))
        )


class Attribute(Model):
    id = Column(Integer, primary_key=True)
    name =  Column(String(150), unique = True, nullable=False)
    rules = relationship('DataQualityRule', secondary=assoc_attribute_rule, backref='attribute')
    dataset_id = Column(Integer, ForeignKey('dataset.id'), nullable=False)
    dataset = relationship("Dataset")

    def __repr__(self):
        return self.name

