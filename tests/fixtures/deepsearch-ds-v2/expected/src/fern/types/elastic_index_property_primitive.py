

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class ElasticIndexPropertyPrimitive(UniversalBaseModel):
    properties: typing.Dict[str, "ElasticIndexPropertyPrimitivePropertiesValue"]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .elastic_index_property_primitive_properties_value import ElasticIndexPropertyPrimitivePropertiesValue

update_forward_refs(
    ElasticIndexPropertyPrimitive,
    ElasticIndexPropertyPrimitivePropertiesValue=ElasticIndexPropertyPrimitivePropertiesValue,
)
