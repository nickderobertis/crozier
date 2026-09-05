

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SubmitPodcastForm(UniversalBaseModel):
    email: typing.Optional[str] = pydantic.Field(default=None)
    """
    A valid email address. If **email** is specified, then we'll notify this email address once the podcast is accepted.
    """

    rss: str = pydantic.Field()
    """
    A valid podcast rss url.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
