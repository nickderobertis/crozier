

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attribute_type import AttributeType
from .attribute_value import AttributeValue


class Attribute(UniversalBaseModel):
    type: AttributeType = pydantic.Field()
    """
    3 attributes type:
    
    |Attribute-type|Role|
    |----------|-------------|
    |Header|-Will be add as http header extension "x-######:"|
    |Body|-Will be simply add to event body map attribute (see monitor event definition in template document)|
    |Query|-Will set as http query parameter when invoking the Webhook|
    """

    key: str
    value: AttributeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
