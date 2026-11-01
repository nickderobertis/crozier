

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ValidationInputRequestValidationType(enum.StrEnum):
    """
    Identifies the type of validation request.
    """

    VALIDATE_ADDRESS = "ValidateAddress"
    VALIDATE_DATA_DESTINATION_DETAILS = "ValidateDataDestinationDetails"
    VALIDATE_SUBSCRIPTION_IS_ALLOWED_TO_CREATE_JOB = "ValidateSubscriptionIsAllowedToCreateJob"
    VALIDATE_PREFERENCES = "ValidatePreferences"
    VALIDATE_CREATE_ORDER_LIMIT = "ValidateCreateOrderLimit"
    VALIDATE_SKU_AVAILABILITY = "ValidateSkuAvailability"

    def visit(
        self,
        validate_address: typing.Callable[[], T_Result],
        validate_data_destination_details: typing.Callable[[], T_Result],
        validate_subscription_is_allowed_to_create_job: typing.Callable[[], T_Result],
        validate_preferences: typing.Callable[[], T_Result],
        validate_create_order_limit: typing.Callable[[], T_Result],
        validate_sku_availability: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValidationInputRequestValidationType.VALIDATE_ADDRESS:
            return validate_address()
        if self is ValidationInputRequestValidationType.VALIDATE_DATA_DESTINATION_DETAILS:
            return validate_data_destination_details()
        if self is ValidationInputRequestValidationType.VALIDATE_SUBSCRIPTION_IS_ALLOWED_TO_CREATE_JOB:
            return validate_subscription_is_allowed_to_create_job()
        if self is ValidationInputRequestValidationType.VALIDATE_PREFERENCES:
            return validate_preferences()
        if self is ValidationInputRequestValidationType.VALIDATE_CREATE_ORDER_LIMIT:
            return validate_create_order_limit()
        if self is ValidationInputRequestValidationType.VALIDATE_SKU_AVAILABILITY:
            return validate_sku_availability()
