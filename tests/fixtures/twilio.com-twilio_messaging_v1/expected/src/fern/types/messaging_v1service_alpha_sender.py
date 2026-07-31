

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessagingV1ServiceAlphaSender(UniversalBaseModel):
    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the AlphaSender resource.
    """

    alpha_sender: typing.Optional[str] = pydantic.Field(default=None)
    """
    The Alphanumeric Sender ID string.
    """

    capabilities: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    An array of values that describe whether the number can receive calls or messages. Can be: `SMS`.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    service_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Service](https://www.twilio.com/docs/chat/rest/service-resource) the resource is associated with.
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that we created to identify the AlphaSender resource.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the AlphaSender resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
