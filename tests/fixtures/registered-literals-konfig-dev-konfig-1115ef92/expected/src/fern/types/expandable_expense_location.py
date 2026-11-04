

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExpandableExpenseLocation(UniversalBaseModel):
    """
    The location associated with the expense.
    """

    id: str = pydantic.Field()
    """
    The unique identifier for the location.
    """

    name: str = pydantic.Field()
    """
    The name of the location.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
