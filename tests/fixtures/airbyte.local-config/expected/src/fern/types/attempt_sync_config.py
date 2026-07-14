

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .connection_state import ConnectionState
from .destination_configuration import DestinationConfiguration
from .source_configuration import SourceConfiguration


class AttemptSyncConfig(UniversalBaseModel):
    destination_configuration: typing_extensions.Annotated[
        DestinationConfiguration, FieldMetadata(alias="destinationConfiguration")
    ]
    source_configuration: typing_extensions.Annotated[SourceConfiguration, FieldMetadata(alias="sourceConfiguration")]
    state: typing.Optional[ConnectionState] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
