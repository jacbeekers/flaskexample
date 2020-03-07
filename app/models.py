from dateutil.utils import today
from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Boolean, Table
from sqlalchemy.orm import relationship
from flask_appbuilder.models.mixins import AuditMixin

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class Dataset(AuditMixin, Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=False, nullable=False)
    logs_id = Column(Integer, unique=True, nullable=False)

    def __repr__(self):
        return self.name


class DataQualityRule(Model, AuditMixin):
    id = Column(String(36), primary_key=True)
    name = Column(String(384), unique=True, nullable=False)
    project_name = Column(String(765), nullable=False)
    rule_type = Column(String(22), nullable=False)
    rule_description = Column(String(4000), nullable=True)

    def __repr__(self):
        return self.name


assoc_attribute_rule = Table('attribute_rule', Model.metadata, Column('id', Integer, primary_key=True),
                             Column('attribute_id', String(36), ForeignKey('attribute.id')),
                             Column('rule_id', String(36), ForeignKey('data_quality_rule.id'))
                             )


class Attribute(Model, AuditMixin):
    id = Column(String(36), primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    rules = relationship('DataQualityRule', secondary=assoc_attribute_rule, backref='attribute')
    dataset_id = Column(Integer, ForeignKey('dataset.id'), nullable=False)
    dataset = relationship("Dataset")

    def __repr__(self):
        return self.name
