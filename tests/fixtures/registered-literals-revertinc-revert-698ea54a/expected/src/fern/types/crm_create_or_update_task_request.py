

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .common_task_write import CommonTaskWrite


class CrmCreateOrUpdateTaskRequest(CommonTaskWrite):
    additional: typing.Any

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
