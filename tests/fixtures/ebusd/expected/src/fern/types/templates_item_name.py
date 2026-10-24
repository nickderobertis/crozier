

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .field_template import FieldTemplate


class TemplatesItemName(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    the template set name.
    """

    sequence: typing.List[FieldTemplate] = pydantic.Field()
    """
    the sequence of fields.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
