

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Payment(UniversalBaseModel):
    """
    A sparse row containing only the selected fields. Default fields: payment_id, family_id, family_name, transaction_date, amount, total_amount, state.
    """

    payment_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Payment id.
    """

    transaction_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Transaction id.
    """

    school_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    School id.
    """

    family_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Family id.
    """

    family_name: typing.Optional[str] = None
    transaction_date: typing.Optional[dt.date] = None
    amount: typing.Optional[float] = None
    fee_amount: typing.Optional[float] = None
    total_amount: typing.Optional[float] = None
    balance: typing.Optional[float] = None
    state: typing.Optional[str] = None
    receipt_number: typing.Optional[str] = None
    payment_mode: typing.Optional[str] = None
    payment_method_sub_kind: typing.Optional[str] = None
    description: typing.Optional[str] = None
    is_posted: typing.Optional[bool] = None
    payd_online: typing.Optional[bool] = None
    auto_billing: typing.Optional[bool] = None
    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    Local timestamp in YYYY-MM-DD HH:mm:ss format; no timezone suffix.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
