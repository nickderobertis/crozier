

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .data_type_result import DataTypeResult


class DataType(UniversalBaseModel):
    """
    a known field data type.
    """

    type: str = pydantic.Field()
    """
    the type name.
    """

    isbits: bool = pydantic.Field()
    """
    true when the length is in bits.
    """

    isadjustable: typing.Optional[bool] = pydantic.Field(default=None)
    """
    whether the length is adjustable.
    """

    isignored: typing.Optional[bool] = pydantic.Field(default=None)
    """
    whether the result is ignored.
    """

    isreverse: typing.Optional[bool] = pydantic.Field(default=None)
    """
    whether the symbols are in reverse order (most significant byte first).
    """

    length: float = pydantic.Field()
    """
    the field length in bytes (-1 for remainder, number of bits when isbits is true).
    """

    result: typing.Optional[DataTypeResult] = pydantic.Field(default=None)
    """
    the result type.
    """

    divisor: typing.Optional[float] = pydantic.Field(default=None)
    """
    the divisor for numeric types (only if applicable, positive for divisor, negative for reciprocal i.e. 1/-divisor).
    """

    precision: typing.Optional[float] = pydantic.Field(default=None)
    """
    the precision (number of fraction digits) when divisor is >1.
    """

    min: typing.Optional[float] = pydantic.Field(default=None)
    """
    the minimum allowed value.
    """

    max: typing.Optional[float] = pydantic.Field(default=None)
    """
    the maximum allowed value.
    """

    step: typing.Optional[float] = pydantic.Field(default=None)
    """
    the smallest step value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
