

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Customer(UniversalBaseModel):
    billing_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The primary billing account account's id.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the customer object's creation.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the customer.
    """

    invoice_notification_preference: typing.Optional[str] = pydantic.Field(default=None)
    """
    The preferred notification type for invoices.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the customer object's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
