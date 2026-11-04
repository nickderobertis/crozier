

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .available_settings_result import AvailableSettingsResult


class SkuInfoResult(UniversalBaseModel):
    available_settings: typing_extensions.Annotated[
        typing.Optional[AvailableSettingsResult],
        FieldMetadata(alias="availableSettings"),
        pydantic.Field(alias="availableSettings"),
    ] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None
    name: typing.Optional[str] = None
    os: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
