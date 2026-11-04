

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .expandable_expense import ExpandableExpense


class PageExpandableExpense(UniversalBaseModel):
    next_cursor: typing.Optional[str] = None
    items: typing.List[ExpandableExpense]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
