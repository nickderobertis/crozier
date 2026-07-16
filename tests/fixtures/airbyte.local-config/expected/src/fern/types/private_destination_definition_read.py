

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destination_definition_read import DestinationDefinitionRead


class PrivateDestinationDefinitionRead(UniversalBaseModel):
    destination_definition: typing_extensions.Annotated[
        DestinationDefinitionRead,
        FieldMetadata(alias="destinationDefinition"),
        pydantic.Field(alias="destinationDefinition"),
    ]
    granted: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
