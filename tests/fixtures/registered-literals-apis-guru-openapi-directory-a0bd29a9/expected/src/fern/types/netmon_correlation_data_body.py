

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class NetmonCorrelationDataBody(UniversalBaseModel):
    billable_owner_created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="billableOwnerCreatedAt"),
        pydantic.Field(alias="billableOwnerCreatedAt"),
    ] = None
    billable_owner_database_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="billableOwnerDatabaseId"),
        pydantic.Field(alias="billableOwnerDatabaseId"),
    ] = None
    billable_owner_global_relay_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="billableOwnerGlobalRelayId"),
        pydantic.Field(alias="billableOwnerGlobalRelayId"),
    ] = None
    billable_owner_plan: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="billableOwnerPlan"), pydantic.Field(alias="billableOwnerPlan")
    ] = None
    owner_created_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownerCreatedAt"), pydantic.Field(alias="ownerCreatedAt")
    ] = None
    owner_database_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownerDatabaseId"), pydantic.Field(alias="ownerDatabaseId")
    ] = None
    owner_global_relay_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownerGlobalRelayId"), pydantic.Field(alias="ownerGlobalRelayId")
    ] = None
    owner_plan: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownerPlan"), pydantic.Field(alias="ownerPlan")
    ] = None
    repository_created_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="repositoryCreatedAt"), pydantic.Field(alias="repositoryCreatedAt")
    ] = None
    repository_database_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="repositoryDatabaseId"), pydantic.Field(alias="repositoryDatabaseId")
    ] = None
    repository_global_relay_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="repositoryGlobalRelayId"),
        pydantic.Field(alias="repositoryGlobalRelayId"),
    ] = None
    repository_private: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="repositoryPrivate"), pydantic.Field(alias="repositoryPrivate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
