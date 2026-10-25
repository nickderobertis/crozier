

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .condition_value_item import ConditionValueItem


class Condition(UniversalBaseModel):
    """
    a single condition.
    """

    name: str = pydantic.Field()
    """
    name of the condition.
    """

    message: str = pydantic.Field()
    """
    name of the referenced message.
    """

    circuit: typing.Optional[str] = pydantic.Field(default=None)
    """
    name of the referenced circuit.
    """

    zz: typing.Optional[int] = pydantic.Field(default=None)
    """
    the circuit slave address.
    """

    field: typing.Optional[str] = pydantic.Field(default=None)
    """
    the field name in the referenced message.
    """

    value: typing.Optional[typing.List[ConditionValueItem]] = pydantic.Field(default=None)
    """
    the value ranges for the condition.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
