

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagingV1DomainConfig(UniversalBaseModel):
    callback_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL to receive click events to your webhook whenever the recipients click on the shortened links.
    """

    config_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that we created to identify the Domain config (prefix ZK).
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date this Domain Config was created.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Date that this Domain Config was last updated.
    """

    domain_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that we created to identify the Domain resource.
    """

    fallback_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Any requests we receive to this domain that do not match an existing shortened message will be redirected to the fallback url. These will likely be either expired messages, random misdirected traffic, or intentional scraping.
    """

    url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
