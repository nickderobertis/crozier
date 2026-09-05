

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .solver_function_to_register_input_schema import SolverFunctionToRegisterInputSchema
from .solver_function_to_register_output_schema import SolverFunctionToRegisterOutputSchema


class SolverFunctionToRegister(UniversalBaseModel):
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    input_schema: typing_extensions.Annotated[
        SolverFunctionToRegisterInputSchema, FieldMetadata(alias="inputSchema"), pydantic.Field(alias="inputSchema")
    ]
    output_schema: typing_extensions.Annotated[
        SolverFunctionToRegisterOutputSchema, FieldMetadata(alias="outputSchema"), pydantic.Field(alias="outputSchema")
    ]
    default_inputs: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultInputs"),
        pydantic.Field(alias="defaultInputs"),
    ] = None
    solver_key: typing_extensions.Annotated[str, FieldMetadata(alias="solverKey"), pydantic.Field(alias="solverKey")]
    solver_version: typing_extensions.Annotated[
        str, FieldMetadata(alias="solverVersion"), pydantic.Field(alias="solverVersion")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
