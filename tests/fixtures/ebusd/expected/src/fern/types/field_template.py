

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FieldTemplate(UniversalBaseModel):
    """
    a single field template.
    """

    name: str = pydantic.Field()
    """
    the field name.
    """

    type: str = pydantic.Field()
    """
    the field type.
    """

    isbits: bool = pydantic.Field()
    """
    true when the length is in bits.
    """

    length: float = pydantic.Field()
    """
    the field length in bytes (-1 for remainder, number of bits when isbits is true).
    """

    divisor: typing.Optional[float] = pydantic.Field(default=None)
    """
    the divisor for numeric types (only if applicable, positive for divisor, negative for reciprocal i.e. 1/-divisor).
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    the constant value (only if applicable).
    """

    verify: typing.Optional[bool] = pydantic.Field(default=None)
    """
    whether the constant value is verified when decoding (only if applicable).
    """

    values: typing.Optional[typing.Dict[str, str]] = pydantic.Field(default=None)
    """
    the raw numeric value to name assignments (only if applicable).
    """

    unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    the field unit.
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    the field comment.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
