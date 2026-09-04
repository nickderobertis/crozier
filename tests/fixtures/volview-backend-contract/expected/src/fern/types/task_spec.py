

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .task_spec_outputs_item import TaskSpecOutputsItem
from .task_spec_parameters_item import TaskSpecParametersItem


class TaskSpec(UniversalBaseModel):
    spec_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="specVersion"), pydantic.Field(alias="specVersion")
    ]
    id: str
    title: str
    description: typing.Optional[str] = None
    parameters: typing.List[TaskSpecParametersItem]
    outputs: typing.List[TaskSpecOutputsItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
