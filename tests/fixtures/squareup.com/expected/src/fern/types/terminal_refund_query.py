

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .terminal_refund_query_filter import TerminalRefundQueryFilter
from .terminal_refund_query_sort import TerminalRefundQuerySort


class TerminalRefundQuery(UniversalBaseModel):
    """ """

    filter: typing.Optional[TerminalRefundQueryFilter] = None
    sort: typing.Optional[TerminalRefundQuerySort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
