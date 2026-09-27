

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_bridge_read_request_get_current_document_uid_data import (
    PostApiBridgeReadRequestGetCurrentDocumentUidData,
)
from .post_api_bridge_read_request_get_current_edit_mode_data import PostApiBridgeReadRequestGetCurrentEditModeData
from .post_api_bridge_read_request_get_current_model_uid_data import PostApiBridgeReadRequestGetCurrentModelUidData
from .post_api_bridge_read_request_get_deformer_structure_data import PostApiBridgeReadRequestGetDeformerStructureData
from .post_api_bridge_read_request_get_document_data import PostApiBridgeReadRequestGetDocumentData
from .post_api_bridge_read_request_get_documents_data import PostApiBridgeReadRequestGetDocumentsData
from .post_api_bridge_read_request_get_object_data import PostApiBridgeReadRequestGetObjectData
from .post_api_bridge_read_request_get_parameter_groups_data import PostApiBridgeReadRequestGetParameterGroupsData
from .post_api_bridge_read_request_get_parameter_values_data import PostApiBridgeReadRequestGetParameterValuesData
from .post_api_bridge_read_request_get_parameters_data import PostApiBridgeReadRequestGetParametersData
from .post_api_bridge_read_request_get_part_structure_data import PostApiBridgeReadRequestGetPartStructureData
from .post_api_bridge_read_request_get_physics_info_data import PostApiBridgeReadRequestGetPhysicsInfoData


class PostApiBridgeReadRequest_GetDocuments(UniversalBaseModel):
    method: typing.Literal["GetDocuments"] = "GetDocuments"
    data: PostApiBridgeReadRequestGetDocumentsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetCurrentDocumentUid(UniversalBaseModel):
    method: typing.Literal["GetCurrentDocumentUID"] = "GetCurrentDocumentUID"
    data: PostApiBridgeReadRequestGetCurrentDocumentUidData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetCurrentModelUid(UniversalBaseModel):
    method: typing.Literal["GetCurrentModelUID"] = "GetCurrentModelUID"
    data: PostApiBridgeReadRequestGetCurrentModelUidData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetCurrentEditMode(UniversalBaseModel):
    method: typing.Literal["GetCurrentEditMode"] = "GetCurrentEditMode"
    data: PostApiBridgeReadRequestGetCurrentEditModeData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetDocument(UniversalBaseModel):
    method: typing.Literal["GetDocument"] = "GetDocument"
    data: PostApiBridgeReadRequestGetDocumentData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetParameters(UniversalBaseModel):
    method: typing.Literal["GetParameters"] = "GetParameters"
    data: PostApiBridgeReadRequestGetParametersData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetParameterGroups(UniversalBaseModel):
    method: typing.Literal["GetParameterGroups"] = "GetParameterGroups"
    data: PostApiBridgeReadRequestGetParameterGroupsData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetPartStructure(UniversalBaseModel):
    method: typing.Literal["GetPartStructure"] = "GetPartStructure"
    data: PostApiBridgeReadRequestGetPartStructureData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetDeformerStructure(UniversalBaseModel):
    method: typing.Literal["GetDeformerStructure"] = "GetDeformerStructure"
    data: PostApiBridgeReadRequestGetDeformerStructureData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetPhysicsInfo(UniversalBaseModel):
    method: typing.Literal["GetPhysicsInfo"] = "GetPhysicsInfo"
    data: PostApiBridgeReadRequestGetPhysicsInfoData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetParameterValues(UniversalBaseModel):
    method: typing.Literal["GetParameterValues"] = "GetParameterValues"
    data: PostApiBridgeReadRequestGetParameterValuesData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PostApiBridgeReadRequest_GetObject(UniversalBaseModel):
    method: typing.Literal["GetObject"] = "GetObject"
    data: PostApiBridgeReadRequestGetObjectData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PostApiBridgeReadRequest = typing_extensions.Annotated[
    typing.Union[
        PostApiBridgeReadRequest_GetDocuments,
        PostApiBridgeReadRequest_GetCurrentDocumentUid,
        PostApiBridgeReadRequest_GetCurrentModelUid,
        PostApiBridgeReadRequest_GetCurrentEditMode,
        PostApiBridgeReadRequest_GetDocument,
        PostApiBridgeReadRequest_GetParameters,
        PostApiBridgeReadRequest_GetParameterGroups,
        PostApiBridgeReadRequest_GetPartStructure,
        PostApiBridgeReadRequest_GetDeformerStructure,
        PostApiBridgeReadRequest_GetPhysicsInfo,
        PostApiBridgeReadRequest_GetParameterValues,
        PostApiBridgeReadRequest_GetObject,
    ],
    pydantic.Field(discriminator="method"),
]
