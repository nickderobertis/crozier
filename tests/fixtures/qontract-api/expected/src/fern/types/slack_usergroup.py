

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .slack_usergroup_config import SlackUsergroupConfig


class SlackUsergroup(UniversalBaseModel):
    """
    A single Slack usergroup with its handle and configuration.
    """

    config: SlackUsergroupConfig = pydantic.Field()
    """
    Usergroup configuration
    """

    handle: str = pydantic.Field()
    """
    Usergroup handle/name (unique identifier)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
