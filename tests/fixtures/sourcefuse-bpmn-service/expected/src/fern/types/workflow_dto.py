

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WorkflowDto(UniversalBaseModel):
    name: str
    bpmn_file: typing_extensions.Annotated[str, FieldMetadata(alias="bpmnFile"), pydantic.Field(alias="bpmnFile")]
    input_schema: typing_extensions.Annotated[
        typing.Dict[str, typing.Any], FieldMetadata(alias="inputSchema"), pydantic.Field(alias="inputSchema")
    ]
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
