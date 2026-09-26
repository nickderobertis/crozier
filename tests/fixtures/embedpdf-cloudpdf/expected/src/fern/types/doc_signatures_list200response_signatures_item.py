

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_list200response_signatures_item_coverage import DocSignaturesList200ResponseSignaturesItemCoverage
from .doc_signatures_list200response_signatures_item_field import DocSignaturesList200ResponseSignaturesItemField
from .doc_signatures_list200response_signatures_item_field_mdp import DocSignaturesList200ResponseSignaturesItemFieldMdp
from .doc_signatures_list200response_signatures_item_kind import DocSignaturesList200ResponseSignaturesItemKind
from .doc_signatures_list200response_signatures_item_lock import DocSignaturesList200ResponseSignaturesItemLock
from .doc_signatures_list200response_signatures_item_seed_value import (
    DocSignaturesList200ResponseSignaturesItemSeedValue,
)
from .doc_signatures_list200response_signatures_item_signer import DocSignaturesList200ResponseSignaturesItemSigner
from .doc_signatures_list200response_signatures_item_widget import DocSignaturesList200ResponseSignaturesItemWidget


class DocSignaturesList200ResponseSignaturesItem(UniversalBaseModel):
    index: int
    field: DocSignaturesList200ResponseSignaturesItemField
    field_name: typing_extensions.Annotated[str, FieldMetadata(alias="fieldName"), pydantic.Field(alias="fieldName")]
    widget: typing.Optional[DocSignaturesList200ResponseSignaturesItemWidget] = None
    signed: bool
    kind: DocSignaturesList200ResponseSignaturesItemKind
    filter: typing.Optional[str] = None
    sub_filter: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="subFilter"), pydantic.Field(alias="subFilter")
    ] = None
    byte_range: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Any]], FieldMetadata(alias="byteRange"), pydantic.Field(alias="byteRange")
    ] = None
    contents_size: typing_extensions.Annotated[
        int, FieldMetadata(alias="contentsSize"), pydantic.Field(alias="contentsSize")
    ]
    coverage: typing.Optional[DocSignaturesList200ResponseSignaturesItemCoverage] = None
    revision_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="revisionIndex"), pydantic.Field(alias="revisionIndex")
    ] = None
    signer: DocSignaturesList200ResponseSignaturesItemSigner
    doc_mdp: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="docMdp"), pydantic.Field(alias="docMdp")
    ] = None
    catalog_certification: typing_extensions.Annotated[
        bool, FieldMetadata(alias="catalogCertification"), pydantic.Field(alias="catalogCertification")
    ]
    field_mdp: typing_extensions.Annotated[
        typing.Optional[DocSignaturesList200ResponseSignaturesItemFieldMdp],
        FieldMetadata(alias="fieldMdp"),
        pydantic.Field(alias="fieldMdp"),
    ] = None
    lock: typing.Optional[DocSignaturesList200ResponseSignaturesItemLock] = None
    seed_value: typing_extensions.Annotated[
        typing.Optional[DocSignaturesList200ResponseSignaturesItemSeedValue],
        FieldMetadata(alias="seedValue"),
        pydantic.Field(alias="seedValue"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
