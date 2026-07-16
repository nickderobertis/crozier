

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .front_port_template_type_label import FrontPortTemplateTypeLabel
from .front_port_template_type_value import FrontPortTemplateTypeValue


class FrontPortTemplateType(UniversalBaseModel):
    label: FrontPortTemplateTypeLabel
    value: FrontPortTemplateTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
