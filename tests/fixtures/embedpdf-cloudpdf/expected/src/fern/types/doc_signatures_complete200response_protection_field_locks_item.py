

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_complete200response_protection_field_locks_item_source import (
    DocSignaturesComplete200ResponseProtectionFieldLocksItemSource,
)
from .doc_signatures_complete200response_protection_field_locks_item_spec import (
    DocSignaturesComplete200ResponseProtectionFieldLocksItemSpec,
)


class DocSignaturesComplete200ResponseProtectionFieldLocksItem(UniversalBaseModel):
    signature_index: typing_extensions.Annotated[
        int, FieldMetadata(alias="signatureIndex"), pydantic.Field(alias="signatureIndex")
    ]
    source: DocSignaturesComplete200ResponseProtectionFieldLocksItemSource
    spec: typing.Optional[DocSignaturesComplete200ResponseProtectionFieldLocksItemSpec] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
