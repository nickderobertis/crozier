

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .certificates_or_keys import CertificatesOrKeys
from .software_authority_claims import SoftwareAuthorityClaims
from .software_statement import SoftwareStatement


class OrganisationSnapshotSoftwareStatementsValue(UniversalBaseModel):
    software_authority_claims: typing_extensions.Annotated[
        typing.Optional[SoftwareAuthorityClaims],
        FieldMetadata(alias="SoftwareAuthorityClaims"),
        pydantic.Field(alias="SoftwareAuthorityClaims"),
    ] = None
    software_certificates: typing_extensions.Annotated[
        typing.Optional[CertificatesOrKeys],
        FieldMetadata(alias="SoftwareCertificates"),
        pydantic.Field(alias="SoftwareCertificates"),
    ] = None
    software_details: typing_extensions.Annotated[
        typing.Optional[SoftwareStatement],
        FieldMetadata(alias="SoftwareDetails"),
        pydantic.Field(alias="SoftwareDetails"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
