from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, MasterDetailView, ModelRestApi

from app.models import Dataset, Attribute, DataQualityRule
from . import appbuilder, db


class AttributeView(ModelView):
    datamodel = SQLAInterface(Attribute)
    add_columns = ['dataset', 'name', 'rules']
    edit_columns = ['name', 'rules']
    #    show_columns = ['dataset', 'name']
    list_columns = ['dataset', 'name']


class DataQualityRuleView(ModelView):
    datamodel = SQLAInterface(DataQualityRule)
    related_views = [AttributeView]
    add_columns = ['name']
    edit_columns = ['name']
    #    show_columns = ['name']
    list_columns = ['name']


class DataSetView(ModelView):
    datamodel = SQLAInterface(Dataset)
    related_views = [AttributeView]
    add_columns = ['id', 'logs_id', 'name']
    edit_columns = ['name']
    #    show_columns = ['name']
    list_columns = ['id', 'name', 'created_on', 'changed_on']


class DataSetApi(ModelRestApi):
    datamodel = SQLAInterface(Dataset)


appbuilder.add_api(DataSetApi)
"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()

appbuilder.add_view(
    DataSetView,
    "Datasets",
    icon="fa-folder-open-o",
    category="Dataset",
    category_icon="fa-envelope"
)

appbuilder.add_view(
    AttributeView,
    "Attributes",
    icon="fa-envelope",
    category="Dataset"
)

appbuilder.add_view(
    DataQualityRuleView,
    "Rules",
    icon="fa-envelope",
    category="Data Quality"
)
