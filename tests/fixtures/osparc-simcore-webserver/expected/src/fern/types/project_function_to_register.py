

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project_function_to_register_input_schema import ProjectFunctionToRegisterInputSchema
from .project_function_to_register_output_schema import ProjectFunctionToRegisterOutputSchema


class ProjectFunctionToRegister(UniversalBaseModel):
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    input_schema: typing_extensions.Annotated[
        ProjectFunctionToRegisterInputSchema, FieldMetadata(alias="inputSchema"), pydantic.Field(alias="inputSchema")
    ]
    output_schema: typing_extensions.Annotated[
        ProjectFunctionToRegisterOutputSchema, FieldMetadata(alias="outputSchema"), pydantic.Field(alias="outputSchema")
    ]
    default_inputs: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultInputs"),
        pydantic.Field(alias="defaultInputs"),
    ] = None
    project_id: typing_extensions.Annotated[str, FieldMetadata(alias="projectId"), pydantic.Field(alias="projectId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
