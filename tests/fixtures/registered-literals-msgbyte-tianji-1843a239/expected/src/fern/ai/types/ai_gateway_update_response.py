

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class AiGatewayUpdateResponse(UniversalBaseModel):
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    name: str
    model_api_key: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="modelApiKey"), pydantic.Field(alias="modelApiKey")
    ] = None
    custom_model_base_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="customModelBaseUrl"), pydantic.Field(alias="customModelBaseUrl")
    ] = None
    custom_model_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="customModelName"), pydantic.Field(alias="customModelName")
    ] = None
    custom_model_input_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="customModelInputPrice"),
        pydantic.Field(alias="customModelInputPrice"),
    ] = None
    custom_model_output_price: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="customModelOutputPrice"),
        pydantic.Field(alias="customModelOutputPrice"),
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
