

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .function_group_access_rights_get import FunctionGroupAccessRightsGet
from .registered_project_function_get_input_schema import RegisteredProjectFunctionGetInputSchema
from .registered_project_function_get_output_schema import RegisteredProjectFunctionGetOutputSchema


class RegisteredProjectFunctionGet(UniversalBaseModel):
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    input_schema: typing_extensions.Annotated[
        RegisteredProjectFunctionGetInputSchema, FieldMetadata(alias="inputSchema"), pydantic.Field(alias="inputSchema")
    ]
    output_schema: typing_extensions.Annotated[
        RegisteredProjectFunctionGetOutputSchema,
        FieldMetadata(alias="outputSchema"),
        pydantic.Field(alias="outputSchema"),
    ]
    default_inputs: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="defaultInputs"),
        pydantic.Field(alias="defaultInputs"),
    ] = None
    uuid_: typing_extensions.Annotated[str, FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")]
    creation_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="creationDate"), pydantic.Field(alias="creationDate")
    ]
    last_change_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastChangeDate"), pydantic.Field(alias="lastChangeDate")
    ]
    template_id: typing_extensions.Annotated[str, FieldMetadata(alias="templateId"), pydantic.Field(alias="templateId")]
    access_rights: typing_extensions.Annotated[
        typing.Dict[str, FunctionGroupAccessRightsGet],
        FieldMetadata(alias="accessRights"),
        pydantic.Field(alias="accessRights"),
    ]
    thumbnail: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
