

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class ApprovalRequestsResponseListItem(UniversalBaseModel):
    start_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startTime"), pydantic.Field(alias="startTime")
    ] = None
    end_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="endTime"), pydantic.Field(alias="endTime")
    ] = None
    status: typing.Optional[str] = None
    actor_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="actorId"), pydantic.Field(alias="actorId")
    ] = None
    actor_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="actorType"), pydantic.Field(alias="actorType")
    ] = None
    actor_details: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="actorDetails"),
        pydantic.Field(alias="actorDetails"),
    ] = None
    role: typing.Optional[str] = None
    role_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="roleName"), pydantic.Field(alias="roleName")
    ] = None
    approval_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="approvalType"), pydantic.Field(alias="approvalType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
