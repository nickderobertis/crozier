

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .config_item_votes_struct import ConfigItemVotesStruct


class ConfigItem(UniversalBaseModel):
    app_id: typing.Optional[int] = None
    app_id_string: typing.Optional[str] = pydantic.Field(default=None)
    """
    AppID as string or name for Non-Steam Games
    """

    controller_native: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Unsure
    """

    controller_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of controller this configuration is designed for
    """

    controller_type_nice: typing.Optional[str] = pydantic.Field(default=None)
    """
    Human-friendly name of the controller type
    """

    creator_id: str = pydantic.Field()
    """
    Steam User ID of the configuration creator
    """

    description: typing.Optional[str] = None
    file_id: typing.Optional[int] = None
    file_name: typing.Optional[str] = None
    file_size: typing.Optional[int] = pydantic.Field(default=None)
    """
    File size in bytes
    """

    file_url: typing.Optional[str] = None
    lifetime_playtime_seconds: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total playtime in seconds
    """

    lifetime_playtime_sessions: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of playtime sessions
    """

    subscriptions: typing.Optional[int] = pydantic.Field(default=None)
    """
    Total number of Downloads
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of tags associated with the configuration
    """

    time_created: dt.datetime
    time_updated: dt.datetime
    title: typing.Optional[str] = None
    votes: typing.Optional[ConfigItemVotesStruct] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
