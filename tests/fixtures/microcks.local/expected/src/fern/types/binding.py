

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .binding_type import BindingType


class Binding(UniversalBaseModel):
    """
    Protocol binding details for asynchronous operations
    """

    destination_name: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="destinationName"),
        pydantic.Field(
            alias="destinationName", description="Name of destination for asynchronous messages of this operation"
        ),
    ]
    """
    Name of destination for asynchronous messages of this operation
    """

    destination_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="destinationType"),
        pydantic.Field(
            alias="destinationType", description="Type of destination for asynchronous messages of this operation"
        ),
    ] = None
    """
    Type of destination for asynchronous messages of this operation
    """

    key_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="keyType"),
        pydantic.Field(alias="keyType", description="Type of key for Kafka messages"),
    ] = None
    """
    Type of key for Kafka messages
    """

    method: typing.Optional[str] = pydantic.Field(default=None)
    """
    HTTP method for WebSocket binding
    """

    persistent: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Persistent attribute for MQTT binding
    """

    qo_s: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="qoS"),
        pydantic.Field(alias="qoS", description="Quality of Service attribute for MQTT binding"),
    ] = None
    """
    Quality of Service attribute for MQTT binding
    """

    type: BindingType = pydantic.Field()
    """
    Protocol binding identifier
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
