

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.task_directive_object import TaskDirectiveObject
from ...types.taskforce_object import TaskforceObject
from ...types.workflow_object import WorkflowObject


class PostV1WorkflowsResponse(UniversalBaseModel):
    workflow: WorkflowObject
    task_directives: typing.List[TaskDirectiveObject]
    taskforces: typing.List[TaskforceObject]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
