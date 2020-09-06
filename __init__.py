from flask_restplus import Api
from flask import Blueprint

from .main.controller.auth_controller import api as auth_ns
from .main.controller.type_controller import api as type_ns
from .main.controller.area_controller import api as area_ns
from .main.controller.user_controller import api as user_ns
from .main.controller.status_controller import api as status_ns
from .main.controller.city_gml_controller import api as city_gml_ns
from .main.controller.buildings_controller import api as buildings_ns
from .main.controller.monitoring_controller import api as monitoring_ns
from .main.controller.monitoring_controller import api_photo as monitoring_photo_ns
from .main.controller.monitoring_controller import api_video as monitoring_video_ns
from .main.controller.cityobject_controller import api as cityobject_ns

blueprint = Blueprint('api', __name__)


authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}

api = Api(blueprint,
          title='FLASK RESTPLUS API FOR 4D PARTICIPATORY',
          version='1.0',
          description='a flask restplus web service for 4d participatory app',
          authorizations=authorizations,
          security='apikey',
          )

api.add_namespace(auth_ns)
api.add_namespace(type_ns, path='/type')
api.add_namespace(area_ns, path='/area')
api.add_namespace(user_ns, path='/user')
api.add_namespace(status_ns, path='/status')
api.add_namespace(city_gml_ns, path='/city_gml')
api.add_namespace(buildings_ns, path='/buildings')
api.add_namespace(monitoring_ns, path='/monitoring/')
api.add_namespace(monitoring_photo_ns, path='/monitoring/')
api.add_namespace(monitoring_video_ns, path='/monitoring/')
api.add_namespace(cityobject_ns, path='/cityobject')
