

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.retention_object_type import RetentionObjectType
from .patch_project_automation_config_object_type_event_type import PatchProjectAutomationConfigObjectTypeEventType


class PatchProjectAutomationConfigObjectType(UniversalBaseModel):
    event_type: PatchProjectAutomationConfigObjectTypeEventType = pydantic.Field()
    """
    The type of automation.
    """

    object_type: RetentionObjectType
    retention_days: float = pydantic.Field()
    """
    The number of days to retain the object
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
