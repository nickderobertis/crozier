

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .components_schemas_channel_properties_from_one_of3content_type import (
    ComponentsSchemasChannelPropertiesFromOneOf3ContentType,
)
from .components_schemas_channel_properties_from_one_of3headers import (
    ComponentsSchemasChannelPropertiesFromOneOf3Headers,
)


class ComponentsSchemasChannelPropertiesFromOneOf3(UniversalBaseModel):
    """
    Connect to a Websocket
    """

    content_type: typing_extensions.Annotated[
        ComponentsSchemasChannelPropertiesFromOneOf3ContentType,
        FieldMetadata(alias="content-type"),
        pydantic.Field(alias="content-type"),
    ]
    headers: typing.Optional[ComponentsSchemasChannelPropertiesFromOneOf3Headers] = pydantic.Field(default=None)
    """
    Details of the Websocket you want to connect to
    """

    type: str = pydantic.Field()
    """
    The type of connection. Must be `websocket`
    """

    uri: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
