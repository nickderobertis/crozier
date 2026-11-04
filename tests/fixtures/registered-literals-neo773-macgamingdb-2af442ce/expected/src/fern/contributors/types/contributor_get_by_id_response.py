

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .contributor_get_by_id_response_reviews_item import ContributorGetByIdResponseReviewsItem


class ContributorGetByIdResponse(UniversalBaseModel):
    id: str
    name: str
    joined_at: typing_extensions.Annotated[str, FieldMetadata(alias="joinedAt"), pydantic.Field(alias="joinedAt")]
    review_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="reviewCount"), pydantic.Field(alias="reviewCount")
    ]
    unique_games_count: typing_extensions.Annotated[
        float, FieldMetadata(alias="uniqueGamesCount"), pydantic.Field(alias="uniqueGamesCount")
    ]
    reviews: typing.List[ContributorGetByIdResponseReviewsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
