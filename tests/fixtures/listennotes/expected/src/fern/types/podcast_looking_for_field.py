

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PodcastLookingForField(UniversalBaseModel):
    cohosts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this podcast is looking for cohosts.
    """

    cross_promotion: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this podcast is looking for cross promotion opportunities with other podcasts.
    """

    guests: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this podcast is looking for guests.
    """

    sponsors: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether this podcast is looking for sponsors.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
