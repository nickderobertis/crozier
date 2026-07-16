

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class FeaturesConfigAsyncApi(UniversalBaseModel):
    """
    Asynchronous feature properties
    """

    default_binding: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="default-binding"), pydantic.Field(alias="default-binding")
    ] = None
    enabled: typing.Optional[str] = None
    endpoint_amqp: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endpoint-AMQP"), pydantic.Field(alias="endpoint-AMQP")
    ] = None
    endpoint_googlepubsub: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="endpoint-GOOGLEPUBSUB"),
        pydantic.Field(alias="endpoint-GOOGLEPUBSUB"),
    ] = None
    endpoint_kafka: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endpoint-KAFKA"), pydantic.Field(alias="endpoint-KAFKA")
    ] = None
    endpoint_mqtt: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endpoint-MQTT"), pydantic.Field(alias="endpoint-MQTT")
    ] = None
    endpoint_nats: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endpoint-NATS"), pydantic.Field(alias="endpoint-NATS")
    ] = None
    endpoint_ws: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endpoint-WS"), pydantic.Field(alias="endpoint-WS")
    ] = None
    frequencies: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
