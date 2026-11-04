

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExpandableExpenseBudget(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Unique ID for the Budget.
    """

    name: str = pydantic.Field()
    """
    Name for the Budget.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
