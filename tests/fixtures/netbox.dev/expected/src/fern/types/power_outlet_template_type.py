

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .power_outlet_template_type_label import PowerOutletTemplateTypeLabel
from .power_outlet_template_type_value import PowerOutletTemplateTypeValue


class PowerOutletTemplateType(UniversalBaseModel):
    label: PowerOutletTemplateTypeLabel
    value: PowerOutletTemplateTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
