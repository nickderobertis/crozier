

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SkuPropertiesDisabledReason(enum.StrEnum):
    """
    Reason why the Sku is disabled.
    """

    NONE = "None"
    COUNTRY = "Country"
    REGION = "Region"
    FEATURE = "Feature"
    OFFER_TYPE = "OfferType"
    NO_SUBSCRIPTION_INFO = "NoSubscriptionInfo"

    def visit(
        self,
        none: typing.Callable[[], T_Result],
        country: typing.Callable[[], T_Result],
        region: typing.Callable[[], T_Result],
        feature: typing.Callable[[], T_Result],
        offer_type: typing.Callable[[], T_Result],
        no_subscription_info: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SkuPropertiesDisabledReason.NONE:
            return none()
        if self is SkuPropertiesDisabledReason.COUNTRY:
            return country()
        if self is SkuPropertiesDisabledReason.REGION:
            return region()
        if self is SkuPropertiesDisabledReason.FEATURE:
            return feature()
        if self is SkuPropertiesDisabledReason.OFFER_TYPE:
            return offer_type()
        if self is SkuPropertiesDisabledReason.NO_SUBSCRIPTION_INFO:
            return no_subscription_info()
