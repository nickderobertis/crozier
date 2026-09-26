

from __future__ import annotations

import typing

from .elastic_index_property_object import ElasticIndexPropertyObject

if typing.TYPE_CHECKING:
    from .elastic_index_property_primitive import ElasticIndexPropertyPrimitive
ElasticIndexPropertyPrimitivePropertiesValue = typing.Union["ElasticIndexPropertyPrimitive", ElasticIndexPropertyObject]
