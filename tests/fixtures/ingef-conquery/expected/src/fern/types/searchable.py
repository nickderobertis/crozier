

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Searchable(UniversalBaseModel):
    search_min_suffix_length: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="searchMinSuffixLength"),
        pydantic.Field(alias="searchMinSuffixLength"),
    ] = None
    generate_search_suffixes: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="generateSearchSuffixes"),
        pydantic.Field(alias="generateSearchSuffixes"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
