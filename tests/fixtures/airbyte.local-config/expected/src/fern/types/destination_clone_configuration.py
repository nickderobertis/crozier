

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_configuration import DestinationConfiguration


class DestinationCloneConfiguration(UniversalBaseModel):
    connection_configuration: typing_extensions.Annotated[
        typing.Optional[DestinationConfiguration],
        FieldMetadata(alias="connectionConfiguration"),
        pydantic.Field(alias="connectionConfiguration"),
    ] = None
    name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
