

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .attribute_type import AttributeType
from .remote_attribute_value import RemoteAttributeValue


class RemoteAttribute(UniversalBaseModel):
    value: typing.Optional[RemoteAttributeValue] = None
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
