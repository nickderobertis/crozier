

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ItemStatusLastWebhook(UniversalBaseModel):
    """
    Information about the last webhook fired for the Item.
    """

    code_sent: typing.Optional[str] = pydantic.Field(default=None)
    """
    The last webhook code sent.
    """

    sent_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    [ISO 8601](https://wikipedia.org/wiki/ISO_8601) timestamp of when the webhook was fired.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
