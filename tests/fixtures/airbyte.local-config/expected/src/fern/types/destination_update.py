

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_configuration import DestinationConfiguration
from .destination_id import DestinationId


class DestinationUpdate(UniversalBaseModel):
    connection_configuration: typing_extensions.Annotated[
        DestinationConfiguration, FieldMetadata(alias="connectionConfiguration")
    ]
    destination_id: typing_extensions.Annotated[DestinationId, FieldMetadata(alias="destinationId")]
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
