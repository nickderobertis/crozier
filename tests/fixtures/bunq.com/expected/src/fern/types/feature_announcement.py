

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .avatar import Avatar


class FeatureAnnouncement(UniversalBaseModel):
    avatar: typing.Optional[Avatar] = pydantic.Field(default=None)
    """
    The Avatar of the event overview.
    """

    sub_title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event overview subtitle of the feature display
    """

    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event overview title of the feature display
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of the feature announcement so apps can override with their own stuff if desired
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
