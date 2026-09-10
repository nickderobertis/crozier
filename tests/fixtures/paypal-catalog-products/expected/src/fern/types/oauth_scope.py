

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    HTTPS_URI_PAYPAL_COM_SERVICES_SUBSCRIPTIONS = "https://uri.paypal.com/services/subscriptions"
    """
    Create and manage products
    """

    def visit(self, https_uri_paypal_com_services_subscriptions: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.HTTPS_URI_PAYPAL_COM_SERVICES_SUBSCRIPTIONS:
            return https_uri_paypal_com_services_subscriptions()
