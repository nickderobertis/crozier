

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .feature_flags_get_response_flags_item_default_enabled import FeatureFlagsGetResponseFlagsItemDefaultEnabled
from .feature_flags_get_response_flags_item_enabled import FeatureFlagsGetResponseFlagsItemEnabled


class FeatureFlagsGetResponseFlagsItem(UniversalBaseModel):
    key: str
    label: str
    enabled: FeatureFlagsGetResponseFlagsItemEnabled
    default_enabled: typing_extensions.Annotated[
        FeatureFlagsGetResponseFlagsItemDefaultEnabled,
        FieldMetadata(alias="defaultEnabled"),
        pydantic.Field(alias="defaultEnabled"),
    ]
    description: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
