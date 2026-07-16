

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cash_drawer_device import CashDrawerDevice
from .money import Money


class CashDrawerShift(UniversalBaseModel):
    """
    This model gives the details of a cash drawer shift.
    The cash_payment_money, cash_refund_money, cash_paid_in_money,
    and cash_paid_out_money fields are all computed by summing their respective
    event types.
    """

    cash_paid_in_money: typing.Optional[Money] = None
    cash_paid_out_money: typing.Optional[Money] = None
    cash_payment_money: typing.Optional[Money] = None
    cash_refunds_money: typing.Optional[Money] = None
    closed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the shift was closed, in ISO 8601 format.
    """

    closed_cash_money: typing.Optional[Money] = None
    closing_employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the employee that closed the cash drawer shift by auditing
    the cash drawer contents.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The free-form text description of a cash drawer by an employee.
    """

    device: typing.Optional[CashDrawerDevice] = None
    employee_ids: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The IDs of all employees that were logged into Square Point of Sale at any
    point while the cash drawer shift was open.
    """

    ended_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the shift ended, in ISO 8601 format.
    """

    ending_employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the employee that ended the cash drawer shift.
    """

    expected_cash_money: typing.Optional[Money] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The shift unique ID.
    """

    opened_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The time when the shift began, in ISO 8601 format.
    """

    opened_cash_money: typing.Optional[Money] = None
    opening_employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the employee that started the cash drawer shift.
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    The shift current state.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
