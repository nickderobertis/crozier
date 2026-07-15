

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .source_configuration import SourceConfiguration
from .source_id import SourceId


class SourceUpdate(UniversalBaseModel):
    connection_configuration: typing_extensions.Annotated[
        SourceConfiguration, FieldMetadata(alias="connectionConfiguration")
    ]
    name: str
    source_id: typing_extensions.Annotated[SourceId, FieldMetadata(alias="sourceId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
