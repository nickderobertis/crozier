

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CompanySettingsItem(UniversalBaseModel):
    setting_key: typing_extensions.Annotated[str, FieldMetadata(alias="settingKey"), pydantic.Field(alias="settingKey")]
    setting_value: typing_extensions.Annotated[
        str, FieldMetadata(alias="settingValue"), pydantic.Field(alias="settingValue")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
