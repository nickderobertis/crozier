

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .money import Money


class CashDrawerShiftEvent(UniversalBaseModel):
    """ """

    created_at: typing.Optional[str] = pydantic.Field(default=None)
    """
    The event time in ISO 8601 format.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional description of the event, entered by the employee that
    created the event.
    """

    employee_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the employee that created the event.
    """

    event_money: typing.Optional[Money] = None
    event_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The type of cash drawer shift event.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique ID of the event.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
