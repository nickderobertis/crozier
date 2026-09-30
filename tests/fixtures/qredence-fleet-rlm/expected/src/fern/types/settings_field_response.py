

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .json_value import JsonValue
from .settings_field_response_editor import SettingsFieldResponseEditor
from .settings_field_response_origin import SettingsFieldResponseOrigin


class SettingsFieldResponse(UniversalBaseModel):
    path: str
    group: str
    label: str
    value: JsonValue
    editor: SettingsFieldResponseEditor
    choices: typing.Optional[typing.List[str]] = None
    environment_overridden: typing.Optional[bool] = None
    origin: typing.Optional[SettingsFieldResponseOrigin] = None
    can_reset: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
