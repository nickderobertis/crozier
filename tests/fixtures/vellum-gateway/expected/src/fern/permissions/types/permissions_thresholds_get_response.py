

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .permissions_thresholds_get_response_autonomous import PermissionsThresholdsGetResponseAutonomous
from .permissions_thresholds_get_response_headless import PermissionsThresholdsGetResponseHeadless
from .permissions_thresholds_get_response_interactive import PermissionsThresholdsGetResponseInteractive


class PermissionsThresholdsGetResponse(UniversalBaseModel):
    interactive: PermissionsThresholdsGetResponseInteractive
    autonomous: PermissionsThresholdsGetResponseAutonomous
    headless: PermissionsThresholdsGetResponseHeadless

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
