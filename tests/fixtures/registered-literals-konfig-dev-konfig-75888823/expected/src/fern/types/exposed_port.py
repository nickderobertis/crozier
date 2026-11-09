

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .transport_type import TransportType


class ExposedPort(UniversalBaseModel):
    """
    Connection details for an active process.
    """

    transport_type: typing_extensions.Annotated[
        TransportType, FieldMetadata(alias="transportType"), pydantic.Field(alias="transportType")
    ]
    port: int
    host: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
