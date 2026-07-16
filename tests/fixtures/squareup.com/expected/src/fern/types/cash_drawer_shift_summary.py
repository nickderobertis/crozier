

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class CashDrawerShiftSummary(UniversalBaseModel):
    """
    The summary of a closed cash drawer shift.
    This model contains only the money counted to start a cash drawer shift, counted
    at the end of the shift, and the amount that should be in the drawer at shift
    end based on summing all cash drawer shift events.
    """

    closed_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The shift close time in ISO 8601 format.
    """

    closed_cash_money: typing.Optional[Money] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    An employee free-text description of a cash drawer shift.
    """

    ended_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The shift end time in ISO 8601 format.
    """

    expected_cash_money: typing.Optional[Money] = None
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The shift unique ID.
    """

    opened_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The shift start time in ISO 8601 format.
    """

    opened_cash_money: typing.Optional[Money] = None
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
