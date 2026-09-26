

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ActionsActionsItem(UniversalBaseModel):
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    agent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="agentId"), pydantic.Field(alias="agentId")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    description: typing.Optional[str] = None
    secret_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="secretId"), pydantic.Field(alias="secretId")
    ] = None
    enabled: typing.Optional[bool] = None
    function_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="functionId"), pydantic.Field(alias="functionId")
    ] = None
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    name: typing.Optional[str] = None
    action_id: typing_extensions.Annotated[str, FieldMetadata(alias="actionId"), pydantic.Field(alias="actionId")]
    created_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ]
    connection_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="connectionId"), pydantic.Field(alias="connectionId")
    ] = None
    id: typing.Optional[str] = None
    config: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
