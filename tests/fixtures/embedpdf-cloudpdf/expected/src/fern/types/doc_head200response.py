

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_head200response_access import DocHead200ResponseAccess
from .doc_head200response_encryption import DocHead200ResponseEncryption
from .doc_head200response_permissions import DocHead200ResponsePermissions
from .doc_head200response_state import DocHead200ResponseState


class DocHead200Response(UniversalBaseModel):
    id: str
    base_sha: typing_extensions.Annotated[str, FieldMetadata(alias="baseSha"), pydantic.Field(alias="baseSha")]
    storage_size_bytes: typing_extensions.Annotated[
        int, FieldMetadata(alias="storageSizeBytes"), pydantic.Field(alias="storageSizeBytes")
    ]
    doc_version: typing_extensions.Annotated[int, FieldMetadata(alias="docVersion"), pydantic.Field(alias="docVersion")]
    state: DocHead200ResponseState
    encryption: DocHead200ResponseEncryption
    permissions: DocHead200ResponsePermissions
    access: DocHead200ResponseAccess

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
