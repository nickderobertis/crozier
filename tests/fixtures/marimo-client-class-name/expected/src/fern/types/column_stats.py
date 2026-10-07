

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ColumnStats(UniversalBaseModel):
    """
    Represents stats for a column in a data table.
    """

    false: typing.Optional[int] = None
    max: typing.Optional[typing.Any] = None
    mean: typing.Optional[typing.Any] = None
    median: typing.Optional[typing.Any] = None
    min: typing.Optional[typing.Any] = None
    nulls: typing.Optional[int] = None
    p25: typing.Optional[typing.Any] = None
    p5: typing.Optional[typing.Any] = None
    p75: typing.Optional[typing.Any] = None
    p95: typing.Optional[typing.Any] = None
    std: typing.Optional[typing.Any] = None
    total: typing.Optional[int] = None
    true: typing.Optional[int] = None
    unique: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
