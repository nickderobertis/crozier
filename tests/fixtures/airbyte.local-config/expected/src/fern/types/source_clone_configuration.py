

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_configuration import SourceConfiguration


class SourceCloneConfiguration(UniversalBaseModel):
    connection_configuration: typing_extensions.Annotated[
        typing.Optional[SourceConfiguration],
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
