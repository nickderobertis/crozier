

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .simple_form_field_option_value import SimpleFormFieldOptionValue


class SimpleFormFieldOption(UniversalBaseModel):
    label: typing.Optional[str] = None
    value: typing.Optional[SimpleFormFieldOptionValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
