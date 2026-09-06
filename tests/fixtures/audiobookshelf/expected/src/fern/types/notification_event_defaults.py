

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class NotificationEventDefaults(UniversalBaseModel):
    title: typing.Optional[str] = pydantic.Field(default=None)
    """
    The default title template for notifications using the notification event.
    """

    body: typing.Optional[str] = pydantic.Field(default=None)
    """
    The default body template for notifications using the notification event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
