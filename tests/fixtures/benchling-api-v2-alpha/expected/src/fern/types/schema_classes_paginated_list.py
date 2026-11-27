

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .schema_classes_list import SchemaClassesList


class SchemaClassesPaginatedList(SchemaClassesList):
    next_token: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextToken"), pydantic.Field(alias="nextToken")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
