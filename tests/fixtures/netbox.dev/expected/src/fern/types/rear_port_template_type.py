

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rear_port_template_type_label import RearPortTemplateTypeLabel
from .rear_port_template_type_value import RearPortTemplateTypeValue


class RearPortTemplateType(UniversalBaseModel):
    label: RearPortTemplateTypeLabel
    value: RearPortTemplateTypeValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
