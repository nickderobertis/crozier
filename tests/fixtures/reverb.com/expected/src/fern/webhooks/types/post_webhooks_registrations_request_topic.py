

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PostWebhooksRegistrationsRequestTopic(str, enum.Enum):
    """
    Valid values: listings/update, listings/publish, listings/bumps-ran-out, orders/create, orders/update, payments/create, payments/update, app/uninstalled
    """

    LISTINGS_UPDATE = "listings/update"
    LISTINGS_PUBLISH = "listings/publish"
    LISTINGS_BUMPS_RAN_OUT = "listings/bumps-ran-out"
    ORDERS_CREATE = "orders/create"
    ORDERS_UPDATE = "orders/update"
    PAYMENTS_CREATE = "payments/create"
    PAYMENTS_UPDATE = "payments/update"
    APP_UNINSTALLED = "app/uninstalled"

    def visit(
        self,
        listings_update: typing.Callable[[], T_Result],
        listings_publish: typing.Callable[[], T_Result],
        listings_bumps_ran_out: typing.Callable[[], T_Result],
        orders_create: typing.Callable[[], T_Result],
        orders_update: typing.Callable[[], T_Result],
        payments_create: typing.Callable[[], T_Result],
        payments_update: typing.Callable[[], T_Result],
        app_uninstalled: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostWebhooksRegistrationsRequestTopic.LISTINGS_UPDATE:
            return listings_update()
        if self is PostWebhooksRegistrationsRequestTopic.LISTINGS_PUBLISH:
            return listings_publish()
        if self is PostWebhooksRegistrationsRequestTopic.LISTINGS_BUMPS_RAN_OUT:
            return listings_bumps_ran_out()
        if self is PostWebhooksRegistrationsRequestTopic.ORDERS_CREATE:
            return orders_create()
        if self is PostWebhooksRegistrationsRequestTopic.ORDERS_UPDATE:
            return orders_update()
        if self is PostWebhooksRegistrationsRequestTopic.PAYMENTS_CREATE:
            return payments_create()
        if self is PostWebhooksRegistrationsRequestTopic.PAYMENTS_UPDATE:
            return payments_update()
        if self is PostWebhooksRegistrationsRequestTopic.APP_UNINSTALLED:
            return app_uninstalled()
