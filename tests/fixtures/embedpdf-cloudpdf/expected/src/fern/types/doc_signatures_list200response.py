

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_list200response_protection import DocSignaturesList200ResponseProtection
from .doc_signatures_list200response_revisions_item import DocSignaturesList200ResponseRevisionsItem
from .doc_signatures_list200response_signatures_item import DocSignaturesList200ResponseSignaturesItem


class DocSignaturesList200Response(UniversalBaseModel):
    chain_valid: typing_extensions.Annotated[
        bool, FieldMetadata(alias="chainValid"), pydantic.Field(alias="chainValid")
    ]
    revisions: typing.List[DocSignaturesList200ResponseRevisionsItem]
    signatures: typing.List[DocSignaturesList200ResponseSignaturesItem]
    protection: DocSignaturesList200ResponseProtection

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
