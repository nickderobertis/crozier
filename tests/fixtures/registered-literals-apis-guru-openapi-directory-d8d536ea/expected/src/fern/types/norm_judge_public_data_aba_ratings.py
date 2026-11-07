

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NormJudgePublicDataAbaRatings(UniversalBaseModel):
    """
    American Bar Association (ABA) Rating of the Judge.
    """

    rating: typing.Optional[str] = pydantic.Field(default=None)
    """
    rating
    """

    year: typing.Optional[int] = pydantic.Field(default=None)
    """
    Year when Rating was recieved.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
