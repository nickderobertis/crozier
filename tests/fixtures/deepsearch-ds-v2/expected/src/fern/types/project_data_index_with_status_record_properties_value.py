

import typing

from .elastic_index_property_object import ElasticIndexPropertyObject
from .elastic_index_property_primitive import ElasticIndexPropertyPrimitive

ProjectDataIndexWithStatusRecordPropertiesValue = typing.Union[
    ElasticIndexPropertyPrimitive, ElasticIndexPropertyObject
]
