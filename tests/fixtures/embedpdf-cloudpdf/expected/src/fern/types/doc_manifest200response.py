

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_manifest200response_pages_item import DocManifest200ResponsePagesItem
from .doc_manifest200response_scopes import DocManifest200ResponseScopes


class DocManifest200Response(UniversalBaseModel):
    doc_version: typing_extensions.Annotated[int, FieldMetadata(alias="docVersion"), pydantic.Field(alias="docVersion")]
    layout_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="layoutVersion"), pydantic.Field(alias="layoutVersion")
    ]
    metadata_version: typing_extensions.Annotated[
        int, FieldMetadata(alias="metadataVersion"), pydantic.Field(alias="metadataVersion")
    ]
    actions_version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="actionsVersion"), pydantic.Field(alias="actionsVersion")
    ] = None
    attachments_version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="attachmentsVersion"), pydantic.Field(alias="attachmentsVersion")
    ] = None
    annotations_version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="annotationsVersion"), pydantic.Field(alias="annotationsVersion")
    ] = None
    audit_head: typing_extensions.Annotated[int, FieldMetadata(alias="auditHead"), pydantic.Field(alias="auditHead")]
    base_sha: typing_extensions.Annotated[str, FieldMetadata(alias="baseSha"), pydantic.Field(alias="baseSha")]
    layer_version: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="layerVersion"), pydantic.Field(alias="layerVersion")
    ] = None
    working: typing.Optional[bool] = None
    base_byte_length: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="baseByteLength"), pydantic.Field(alias="baseByteLength")
    ] = None
    scopes: typing.Optional[DocManifest200ResponseScopes] = None
    pages: typing.List[DocManifest200ResponsePagesItem]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
