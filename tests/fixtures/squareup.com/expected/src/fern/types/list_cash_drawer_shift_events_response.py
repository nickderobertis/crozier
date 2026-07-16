

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cash_drawer_shift_event import CashDrawerShiftEvent
from .error import Error


class ListCashDrawerShiftEventsResponse(UniversalBaseModel):
    """ """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Opaque cursor for fetching the next page. Cursor is not present in
    the last page of results.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    events: typing.Optional[typing.List[CashDrawerShiftEvent]] = pydantic.Field(default=None)
    """
    All of the events (payments, refunds, etc.) for a cash drawer during
    the shift.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
