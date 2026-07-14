

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .task_instance_reference import TaskInstanceReference


class TaskInstanceReferenceCollection(UniversalBaseModel):
    task_instances: typing.Optional[typing.List[TaskInstanceReference]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
