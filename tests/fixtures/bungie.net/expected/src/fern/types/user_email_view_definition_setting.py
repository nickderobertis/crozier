

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .user_e_mail_setting_localization import UserEMailSettingLocalization
from .user_email_subscription_definition import UserEmailSubscriptionDefinition


class UserEmailViewDefinitionSetting(UniversalBaseModel):
    localization: typing.Optional[typing.Dict[str, UserEMailSettingLocalization]] = pydantic.Field(default=None)
    """
    A dictionary of localized text for the EMail setting, keyed by the locale.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The identifier for this UI Setting, which can be used to relate it to custom strings or other data as desired.
    """

    opt_in_aggregate_value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="optInAggregateValue"),
        pydantic.Field(
            alias="optInAggregateValue",
            description="The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting.",
        ),
    ] = None
    """
    The OptInFlags value to set or clear if this setting is set or cleared in the UI. It is the aggregate of all underlying opt-in flags related to this setting.
    """

    set_by_default: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="setByDefault"),
        pydantic.Field(
            alias="setByDefault",
            description="If true, this setting should be set by default if the user hasn't chosen whether it's set or cleared yet.",
        ),
    ] = None
    """
    If true, this setting should be set by default if the user hasn't chosen whether it's set or cleared yet.
    """

    subscriptions: typing.Optional[typing.List[UserEmailSubscriptionDefinition]] = pydantic.Field(default=None)
    """
    The subscriptions to show as children of this setting, if any.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
