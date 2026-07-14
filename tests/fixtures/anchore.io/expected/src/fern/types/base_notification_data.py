

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BaseNotificationData(UniversalBaseModel):
    """
    Every notification has a payload, which follows this basic structure
    """

    notification_type: typing.Optional[str] = None
    notification_user: typing.Optional[str] = None
    notification_user_email: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
