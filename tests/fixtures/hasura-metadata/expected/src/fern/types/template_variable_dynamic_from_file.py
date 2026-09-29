

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .template_variable_dynamic_from_file_type import TemplateVariableDynamicFromFileType


class TemplateVariableDynamicFromFile(UniversalBaseModel):
    filepath: str
    type: TemplateVariableDynamicFromFileType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
