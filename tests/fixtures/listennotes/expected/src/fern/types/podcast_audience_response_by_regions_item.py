

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PodcastAudienceResponseByRegionsItem(UniversalBaseModel):
    ratio: typing.Optional[str] = pydantic.Field(default=None)
    """
    percentage of audience from this specific region
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    2-letter country code of a region.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
