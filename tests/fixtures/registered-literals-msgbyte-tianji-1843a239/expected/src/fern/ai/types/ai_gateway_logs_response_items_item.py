

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .ai_gateway_logs_response_items_item_status import AiGatewayLogsResponseItemsItemStatus


class AiGatewayLogsResponseItemsItem(UniversalBaseModel):
    id: str
    workspace_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="workspaceId"), pydantic.Field(alias="workspaceId")
    ]
    gateway_id: typing_extensions.Annotated[str, FieldMetadata(alias="gatewayId"), pydantic.Field(alias="gatewayId")]
    input_token: typing_extensions.Annotated[int, FieldMetadata(alias="inputToken"), pydantic.Field(alias="inputToken")]
    output_token: typing_extensions.Annotated[
        int, FieldMetadata(alias="outputToken"), pydantic.Field(alias="outputToken")
    ]
    stream: bool
    model_name: typing_extensions.Annotated[str, FieldMetadata(alias="modelName"), pydantic.Field(alias="modelName")]
    status: AiGatewayLogsResponseItemsItemStatus
    duration: int
    ttft: int
    price: float
    user_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="userId"), pydantic.Field(alias="userId")
    ] = None
    created_at: typing_extensions.Annotated[str, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")]
    updated_at: typing_extensions.Annotated[str, FieldMetadata(alias="updatedAt"), pydantic.Field(alias="updatedAt")]
    request_payload: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="requestPayload"), pydantic.Field(alias="requestPayload")
    ] = None
    response_payload: typing_extensions.Annotated[
        typing.Optional[typing.Any], FieldMetadata(alias="responsePayload"), pydantic.Field(alias="responsePayload")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
