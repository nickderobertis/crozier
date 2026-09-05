

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .retention_object_type import RetentionObjectType


class ProjectAutomationConfigRetention(UniversalBaseModel):
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
