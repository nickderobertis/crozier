

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .atlas_classification import AtlasClassification
from .atlas_entity_status import AtlasEntityStatus
from .atlas_term_assignment_header import AtlasTermAssignmentHeader


class AtlasEntity(UniversalBaseModel):
    type_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="typeName"), pydantic.Field(alias="typeName")
    ] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None
    guid: typing.Optional[str] = None
    home_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="homeId"), pydantic.Field(alias="homeId")
    ] = None
    is_proxy: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isProxy"), pydantic.Field(alias="isProxy")
    ] = None
    is_incomplete: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="isIncomplete"), pydantic.Field(alias="isIncomplete")
    ] = None
    provenance_type: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="provenanceType"), pydantic.Field(alias="provenanceType")
    ] = None
    status: typing.Optional[AtlasEntityStatus] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    updated_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="updatedBy"), pydantic.Field(alias="updatedBy")
    ] = None
    create_time: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="createTime"), pydantic.Field(alias="createTime")
    ] = None
    update_time: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="updateTime"), pydantic.Field(alias="updateTime")
    ] = None
    version: typing.Optional[int] = None
    relationship_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="relationshipAttributes"),
        pydantic.Field(alias="relationshipAttributes"),
    ] = None
    classifications: typing.Optional[typing.List[AtlasClassification]] = None
    meanings: typing.Optional[typing.List[AtlasTermAssignmentHeader]] = None
    custom_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="customAttributes"),
        pydantic.Field(alias="customAttributes"),
    ] = None
    business_attributes: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="businessAttributes"),
        pydantic.Field(alias="businessAttributes"),
    ] = None
    labels: typing.Optional[typing.List[str]] = None
    pending_tasks: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="pendingTasks"), pydantic.Field(alias="pendingTasks")
    ] = None
    proxy: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
