

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .contributor_get_top_contributors_response_contributors_item import (
    ContributorGetTopContributorsResponseContributorsItem,
)


class ContributorGetTopContributorsResponse(UniversalBaseModel):
    contributors: typing.List[ContributorGetTopContributorsResponseContributorsItem]
    next_cursor: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="nextCursor"), pydantic.Field(alias="nextCursor")
    ] = None
    total_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="totalCount"), pydantic.Field(alias="totalCount")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
