

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EntityHistoryExecutionStatusTimeStratifiedInfosItemYearsItemQuartersItem(UniversalBaseModel):
    quarter: typing.Optional[int] = None
    values: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Aggregated values for the quarter.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
