

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sort_by import SortBy


class SortByFilter(UniversalBaseModel):
    sort_by: typing_extensions.Annotated[
        typing.Optional[SortBy], FieldMetadata(alias="sortBy"), pydantic.Field(alias="sortBy")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
