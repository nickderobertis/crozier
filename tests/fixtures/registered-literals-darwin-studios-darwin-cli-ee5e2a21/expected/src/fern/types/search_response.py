

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability import Capability
from .search_response_degraded_reason import SearchResponseDegradedReason


class SearchResponse(UniversalBaseModel):
    results: typing.List[Capability]
    next_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextCursor"), pydantic.Field(alias="nextCursor")
    ] = None
    degraded: typing.Optional[bool] = None
    degraded_reason: typing_extensions.Annotated[
        typing.Optional[SearchResponseDegradedReason],
        FieldMetadata(alias="degradedReason"),
        pydantic.Field(alias="degradedReason"),
    ] = None
    partial_hydration: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="partialHydration"), pydantic.Field(alias="partialHydration")
    ] = None
    ranking_version: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rankingVersion"), pydantic.Field(alias="rankingVersion")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
