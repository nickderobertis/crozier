

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_versions_signatures200response_signatures_item_coverage import (
    DocVersionsSignatures200ResponseSignaturesItemCoverage,
)
from .doc_versions_signatures200response_signatures_item_field import (
    DocVersionsSignatures200ResponseSignaturesItemField,
)
from .doc_versions_signatures200response_signatures_item_field_mdp import (
    DocVersionsSignatures200ResponseSignaturesItemFieldMdp,
)
from .doc_versions_signatures200response_signatures_item_kind import DocVersionsSignatures200ResponseSignaturesItemKind
from .doc_versions_signatures200response_signatures_item_lock import DocVersionsSignatures200ResponseSignaturesItemLock
from .doc_versions_signatures200response_signatures_item_seed_value import (
    DocVersionsSignatures200ResponseSignaturesItemSeedValue,
)
from .doc_versions_signatures200response_signatures_item_signer import (
    DocVersionsSignatures200ResponseSignaturesItemSigner,
)
from .doc_versions_signatures200response_signatures_item_widget import (
    DocVersionsSignatures200ResponseSignaturesItemWidget,
)


class DocVersionsSignatures200ResponseSignaturesItem(UniversalBaseModel):
    index: int
    field: DocVersionsSignatures200ResponseSignaturesItemField
    field_name: typing_extensions.Annotated[str, FieldMetadata(alias="fieldName"), pydantic.Field(alias="fieldName")]
    widget: typing.Optional[DocVersionsSignatures200ResponseSignaturesItemWidget] = None
    signed: bool
    kind: DocVersionsSignatures200ResponseSignaturesItemKind
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
    coverage: typing.Optional[DocVersionsSignatures200ResponseSignaturesItemCoverage] = None
    revision_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="revisionIndex"), pydantic.Field(alias="revisionIndex")
    ] = None
    signer: DocVersionsSignatures200ResponseSignaturesItemSigner
    doc_mdp: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="docMdp"), pydantic.Field(alias="docMdp")
    ] = None
    catalog_certification: typing_extensions.Annotated[
        bool, FieldMetadata(alias="catalogCertification"), pydantic.Field(alias="catalogCertification")
    ]
    field_mdp: typing_extensions.Annotated[
        typing.Optional[DocVersionsSignatures200ResponseSignaturesItemFieldMdp],
        FieldMetadata(alias="fieldMdp"),
        pydantic.Field(alias="fieldMdp"),
    ] = None
    lock: typing.Optional[DocVersionsSignatures200ResponseSignaturesItemLock] = None
    seed_value: typing_extensions.Annotated[
        typing.Optional[DocVersionsSignatures200ResponseSignaturesItemSeedValue],
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
