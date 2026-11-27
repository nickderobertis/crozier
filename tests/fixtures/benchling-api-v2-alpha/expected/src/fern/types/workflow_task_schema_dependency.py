

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .schema_base_dependency import SchemaBaseDependency
from .workflow_task_schema_dependency_output import WorkflowTaskSchemaDependencyOutput
from .workflow_task_schema_dependency_type import WorkflowTaskSchemaDependencyType


class WorkflowTaskSchemaDependency(SchemaBaseDependency):
    output: typing.Optional[WorkflowTaskSchemaDependencyOutput] = None
    type: typing.Optional[WorkflowTaskSchemaDependencyType] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
