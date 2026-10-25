

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .field_value import FieldValue


class Field(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    the field name.
    """

    value: typing.Optional[FieldValue] = pydantic.Field(default=None)
    """
    the field value.
    """

    unit: typing.Optional[str] = pydantic.Field(default=None)
    """
    the field unit (only with verbose).
    """

    comment: typing.Optional[str] = pydantic.Field(default=None)
    """
    the field comment (only with verbose).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
