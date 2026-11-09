

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .customise_type import CustomiseType


class Customise(UniversalBaseModel):
    """
    Admin customise data object
    """

    key: typing.Optional[str] = pydantic.Field(default=None)
    """
    field key
    """

    value: typing.Optional[str] = pydantic.Field(default=None)
    """
    field value
    """

    type: typing.Optional[CustomiseType] = pydantic.Field(default=None)
    """
    field type
    """

    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    field label
    """

    group_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    group name for the field
    """

    group_order: typing.Optional[int] = pydantic.Field(default=None)
    """
    group order of the field
    """

    option_value: typing.Optional[str] = pydantic.Field(default=None)
    """
    If type is 'dropdown', provide options in format op1{val1}|op2{val2}|...
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
