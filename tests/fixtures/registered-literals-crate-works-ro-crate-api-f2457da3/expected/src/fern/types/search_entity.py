

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .search_entity_search_extra import SearchEntitySearchExtra


class SearchEntity(UniversalBaseModel):
    """
    Contains additional information returned in search contexts.
    """

    search_extra: typing_extensions.Annotated[
        typing.Optional[SearchEntitySearchExtra],
        FieldMetadata(alias="searchExtra"),
        pydantic.Field(alias="searchExtra", description="Extra search-related metadata."),
    ] = None
    """
    Extra search-related metadata.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
