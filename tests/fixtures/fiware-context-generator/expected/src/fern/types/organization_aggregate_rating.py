

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class OrganizationAggregateRating(UniversalBaseModel):
    """
    The average rating based on multiple ratings or reviews. Privacy:'low'
    """

    item_reviewed: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemReviewed"),
        pydantic.Field(alias="itemReviewed", description="Relationship. The item that is being reviewed/rated. "),
    ] = None
    """
    Relationship. The item that is being reviewed/rated. 
    """

    rating_count: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="ratingCount"), pydantic.Field(alias="ratingCount")
    ] = None
    review_count: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="reviewCount"), pydantic.Field(alias="reviewCount")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
