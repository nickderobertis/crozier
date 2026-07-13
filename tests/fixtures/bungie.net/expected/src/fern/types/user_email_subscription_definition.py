

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .user_e_mail_setting_subscription_localization import UserEMailSettingSubscriptionLocalization


class UserEmailSubscriptionDefinition(UniversalBaseModel):
    """
    Defines a single subscription: permission to send emails for a specific, focused subject (generally timeboxed, such as for a specific release of a product or feature).
    """

    localization: typing.Optional[typing.Dict[str, UserEMailSettingSubscriptionLocalization]] = pydantic.Field(
        default=None
    )
    """
    A dictionary of localized text for the EMail Opt-in setting, keyed by the locale.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier for this subscription.
    """

    value: typing.Optional[int] = pydantic.Field(default=None)
    """
    The bitflag value for this subscription. Should be a unique power of two value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
