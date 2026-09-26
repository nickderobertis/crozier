

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReviewAutopilotResponse(UniversalBaseModel):
    enabled: bool = pydantic.Field()
    """
    Whether the review-reply autopilot is enabled (default false).
    """

    min_rating: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="minRating"),
        pydantic.Field(
            alias="minRating",
            description="The minimum star rating that may be auto-published (default 4 when\nunset; always at least 4).",
        ),
    ]
    """
    The minimum star rating that may be auto-published (default 4 when
    unset; always at least 4).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
