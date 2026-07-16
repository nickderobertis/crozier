

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .custom_field_ui_visibility_label import CustomFieldUiVisibilityLabel
from .custom_field_ui_visibility_value import CustomFieldUiVisibilityValue


class CustomFieldUiVisibility(UniversalBaseModel):
    label: CustomFieldUiVisibilityLabel
    value: CustomFieldUiVisibilityValue

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
