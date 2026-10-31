

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WorkflowsFilterFieldsCreatedBy(UniversalBaseModel):
    deleted: typing.Optional[bool] = None
    deleted_on: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="deletedOn"), pydantic.Field(alias="deletedOn")
    ] = None
    deleted_by: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="deletedBy"), pydantic.Field(alias="deletedBy")
    ] = None
    created_on: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="createdOn"), pydantic.Field(alias="createdOn")
    ] = None
    modified_on: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="modifiedOn"), pydantic.Field(alias="modifiedOn")
    ] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    modified_by: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="modifiedBy"), pydantic.Field(alias="modifiedBy")
    ] = None
    id: typing.Optional[bool] = None
    workflow_version: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="workflowVersion"), pydantic.Field(alias="workflowVersion")
    ] = None
    external_identifier: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="externalIdentifier"), pydantic.Field(alias="externalIdentifier")
    ] = None
    name: typing.Optional[bool] = None
    provider: typing.Optional[bool] = None
    input_schema: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="inputSchema"), pydantic.Field(alias="inputSchema")
    ] = None
    description: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
