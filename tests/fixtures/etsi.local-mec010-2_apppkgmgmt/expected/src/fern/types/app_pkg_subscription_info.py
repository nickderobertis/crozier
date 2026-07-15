

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_pkg_subscription_info_id import AppPkgSubscriptionInfoId
from .app_pkg_subscription_info_links import AppPkgSubscriptionInfoLinks
from .app_pkg_subscription_type import AppPkgSubscriptionType
from .callback_uri import CallbackUri


class AppPkgSubscriptionInfo(UniversalBaseModel):
    """
    'The data type represents a subscription to notification of application package management for the onboarding, or operational state change of application package'
    """

    links: typing_extensions.Annotated[AppPkgSubscriptionInfoLinks, FieldMetadata(alias="_links")]
    callback_uri: typing_extensions.Annotated[CallbackUri, FieldMetadata(alias="callbackUri")]
    id: AppPkgSubscriptionInfoId
    subscription_type: typing_extensions.Annotated[AppPkgSubscriptionType, FieldMetadata(alias="subscriptionType")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
