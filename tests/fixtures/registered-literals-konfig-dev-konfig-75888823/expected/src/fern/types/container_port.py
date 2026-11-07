

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transport_type import TransportType


class ContainerPort(UniversalBaseModel):
    """
    A container port object represents the transport configruations for how your server will listen.
    """

    transport_type: typing_extensions.Annotated[
        TransportType, FieldMetadata(alias="transportType"), pydantic.Field(alias="transportType")
    ]
    port: int
    name: str = pydantic.Field()
    """
    Readable name for the port.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
