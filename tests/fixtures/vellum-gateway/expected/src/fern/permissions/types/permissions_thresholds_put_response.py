

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .permissions_thresholds_put_response_autonomous import PermissionsThresholdsPutResponseAutonomous
from .permissions_thresholds_put_response_headless import PermissionsThresholdsPutResponseHeadless
from .permissions_thresholds_put_response_interactive import PermissionsThresholdsPutResponseInteractive


class PermissionsThresholdsPutResponse(UniversalBaseModel):
    interactive: PermissionsThresholdsPutResponseInteractive
    autonomous: PermissionsThresholdsPutResponseAutonomous
    headless: PermissionsThresholdsPutResponseHeadless

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
