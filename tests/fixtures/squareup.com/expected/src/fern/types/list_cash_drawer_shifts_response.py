

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cash_drawer_shift_summary import CashDrawerShiftSummary
from .error import Error


class ListCashDrawerShiftsResponse(UniversalBaseModel):
    """ """

    cursor: typing.Optional[str] = pydantic.Field(default=None)
    """
    Opaque cursor for fetching the next page of results. Cursor is not
    present in the last page of results.
    """

    errors: typing.Optional[typing.List[Error]] = pydantic.Field(default=None)
    """
    Any errors that occurred during the request.
    """

    items: typing.Optional[typing.List[CashDrawerShiftSummary]] = pydantic.Field(default=None)
    """
    A collection of CashDrawerShiftSummary objects for shifts that match
    the query.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
