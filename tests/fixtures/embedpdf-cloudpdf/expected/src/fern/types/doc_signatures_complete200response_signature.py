

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .doc_signatures_complete200response_signature_coverage import DocSignaturesComplete200ResponseSignatureCoverage
from .doc_signatures_complete200response_signature_field import DocSignaturesComplete200ResponseSignatureField
from .doc_signatures_complete200response_signature_field_mdp import DocSignaturesComplete200ResponseSignatureFieldMdp
from .doc_signatures_complete200response_signature_kind import DocSignaturesComplete200ResponseSignatureKind
from .doc_signatures_complete200response_signature_lock import DocSignaturesComplete200ResponseSignatureLock
from .doc_signatures_complete200response_signature_seed_value import DocSignaturesComplete200ResponseSignatureSeedValue
from .doc_signatures_complete200response_signature_signer import DocSignaturesComplete200ResponseSignatureSigner
from .doc_signatures_complete200response_signature_widget import DocSignaturesComplete200ResponseSignatureWidget


class DocSignaturesComplete200ResponseSignature(UniversalBaseModel):
    index: int
    field: DocSignaturesComplete200ResponseSignatureField
    field_name: typing_extensions.Annotated[str, FieldMetadata(alias="fieldName"), pydantic.Field(alias="fieldName")]
    widget: typing.Optional[DocSignaturesComplete200ResponseSignatureWidget] = None
    signed: bool
    kind: DocSignaturesComplete200ResponseSignatureKind
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
    coverage: typing.Optional[DocSignaturesComplete200ResponseSignatureCoverage] = None
    revision_index: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="revisionIndex"), pydantic.Field(alias="revisionIndex")
    ] = None
    signer: DocSignaturesComplete200ResponseSignatureSigner
    doc_mdp: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="docMdp"), pydantic.Field(alias="docMdp")
    ] = None
    catalog_certification: typing_extensions.Annotated[
        bool, FieldMetadata(alias="catalogCertification"), pydantic.Field(alias="catalogCertification")
    ]
    field_mdp: typing_extensions.Annotated[
        typing.Optional[DocSignaturesComplete200ResponseSignatureFieldMdp],
        FieldMetadata(alias="fieldMdp"),
        pydantic.Field(alias="fieldMdp"),
    ] = None
    lock: typing.Optional[DocSignaturesComplete200ResponseSignatureLock] = None
    seed_value: typing_extensions.Annotated[
        typing.Optional[DocSignaturesComplete200ResponseSignatureSeedValue],
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
