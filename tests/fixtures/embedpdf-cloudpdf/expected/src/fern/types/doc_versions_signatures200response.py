

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_versions_signatures200response_protection import DocVersionsSignatures200ResponseProtection
from .doc_versions_signatures200response_revisions_item import DocVersionsSignatures200ResponseRevisionsItem
from .doc_versions_signatures200response_signatures_item import DocVersionsSignatures200ResponseSignaturesItem


class DocVersionsSignatures200Response(UniversalBaseModel):
    chain_valid: typing_extensions.Annotated[
        bool, FieldMetadata(alias="chainValid"), pydantic.Field(alias="chainValid")
    ]
    revisions: typing.List[DocVersionsSignatures200ResponseRevisionsItem]
    signatures: typing.List[DocVersionsSignatures200ResponseSignaturesItem]
    protection: DocVersionsSignatures200ResponseProtection

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
