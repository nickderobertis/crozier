

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateNotificationChannelRequestConfig_Webhook(UniversalBaseModel):
    """
    Configuration specific to the channel type.
    """

    type: typing.Literal["webhook"] = "webhook"
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateNotificationChannelRequestConfig_Rss(UniversalBaseModel):
    """
    Configuration specific to the channel type.
    """

    type: typing.Literal["rss"] = "rss"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CreateNotificationChannelRequestConfig = typing_extensions.Annotated[
    typing.Union[CreateNotificationChannelRequestConfig_Webhook, CreateNotificationChannelRequestConfig_Rss],
    pydantic.Field(discriminator="type"),
]
