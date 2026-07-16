

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class KafkaConfig(UniversalBaseModel):
    """
    The configuration for kafka access
    """

    key_pass: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="keyPass")] = pydantic.Field(
        default=None
    )
    """
    Optional keypass
    """

    key_store: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="keyStore")] = pydantic.Field(
        default=None
    )
    """
    Optional path to keystore
    """

    servers: typing.List[str] = pydantic.Field()
    """
    URLs of the kafka servers
    """

    topic: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional kafka topic (otoroshi-events by default)
    """

    trustore: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional path to trustore
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
