

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .camera_rig import CameraRig
from .filter_grade import FilterGrade
from .get_settings_response_light import GetSettingsResponseLight
from .lens_spec import LensSpec
from .shot_size import ShotSize
from .take_mark import TakeMark


class GetSettingsResponse(UniversalBaseModel):
    mode: ShotSize
    lens: typing.Optional[LensSpec] = None
    light: typing.Optional[GetSettingsResponseLight] = None
    takes: typing.Optional[typing.List[TakeMark]] = None
    filters: typing.Optional[typing.Dict[str, FilterGrade]] = None
    rig: typing.Optional[CameraRig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
