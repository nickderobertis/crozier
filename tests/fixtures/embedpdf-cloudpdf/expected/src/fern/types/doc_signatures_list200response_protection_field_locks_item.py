

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_list200response_protection_field_locks_item_source import (
    DocSignaturesList200ResponseProtectionFieldLocksItemSource,
)
from .doc_signatures_list200response_protection_field_locks_item_spec import (
    DocSignaturesList200ResponseProtectionFieldLocksItemSpec,
)


class DocSignaturesList200ResponseProtectionFieldLocksItem(UniversalBaseModel):
    signature_index: typing_extensions.Annotated[
        int, FieldMetadata(alias="signatureIndex"), pydantic.Field(alias="signatureIndex")
    ]
    source: DocSignaturesList200ResponseProtectionFieldLocksItemSource
    spec: typing.Optional[DocSignaturesList200ResponseProtectionFieldLocksItemSpec] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
