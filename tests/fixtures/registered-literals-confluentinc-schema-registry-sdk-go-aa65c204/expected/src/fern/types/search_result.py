

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .atlas_entity_header import AtlasEntityHeader
from .search_params import SearchParams


class SearchResult(UniversalBaseModel):
    search_parameters: typing_extensions.Annotated[
        typing.Optional[SearchParams], FieldMetadata(alias="searchParameters"), pydantic.Field(alias="searchParameters")
    ] = None
    types: typing.Optional[typing.List[str]] = None
    entities: typing.Optional[typing.List[AtlasEntityHeader]] = None
    referred_entities: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, AtlasEntityHeader]],
        FieldMetadata(alias="referredEntities"),
        pydantic.Field(alias="referredEntities"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
