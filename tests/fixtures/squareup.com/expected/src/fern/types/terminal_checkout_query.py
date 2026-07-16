

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .terminal_checkout_query_filter import TerminalCheckoutQueryFilter
from .terminal_checkout_query_sort import TerminalCheckoutQuerySort


class TerminalCheckoutQuery(UniversalBaseModel):
    """ """

    filter: typing.Optional[TerminalCheckoutQueryFilter] = None
    sort: typing.Optional[TerminalCheckoutQuerySort] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
