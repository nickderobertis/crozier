

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .field_template import FieldTemplate


class FieldDef(FieldTemplate):
    """
    a single field definition.
    """

    slave: bool = pydantic.Field()
    """
    whether the field is part of the slave data.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
