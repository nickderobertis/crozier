

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .hooks_hooks_item_trigger import HooksHooksItemTrigger


class HooksHooksItem(UniversalBaseModel):
    updated_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedTime"), pydantic.Field(alias="updatedTime")
    ] = None
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    description: typing.Optional[str] = None
    trigger: typing.Optional[HooksHooksItemTrigger] = None
    enabled: typing.Optional[bool] = None
    function_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="functionId"), pydantic.Field(alias="functionId")
    ] = None
    false_action_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="falseActionId"), pydantic.Field(alias="falseActionId")
    ] = None
    created_by: typing_extensions.Annotated[str, FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")]
    true_action_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="trueActionId"), pydantic.Field(alias="trueActionId")
    ] = None
    hook_id: typing_extensions.Annotated[str, FieldMetadata(alias="hookId"), pydantic.Field(alias="hookId")]
    name: typing.Optional[str] = None
    created_time: typing_extensions.Annotated[
        str, FieldMetadata(alias="createdTime"), pydantic.Field(alias="createdTime")
    ]
    id: typing.Optional[str] = None
    config: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
