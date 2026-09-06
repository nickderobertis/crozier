

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_certification_uri import ApiCertificationUri
from .certification_expiration_date import CertificationExpirationDate
from .certification_start_date import CertificationStartDate
from .profile_type import ProfileType
from .profile_variant import ProfileVariant
from .software_statement_certification_id import SoftwareStatementCertificationId
from .software_statement_certification_status import SoftwareStatementCertificationStatus
from .software_statement_id import SoftwareStatementId


class SoftwareStatementCertification(UniversalBaseModel):
    certification_expiration_date: typing_extensions.Annotated[
        typing.Optional[CertificationExpirationDate],
        FieldMetadata(alias="CertificationExpirationDate"),
        pydantic.Field(alias="CertificationExpirationDate"),
    ] = None
    certification_id: typing_extensions.Annotated[
        typing.Optional[SoftwareStatementCertificationId],
        FieldMetadata(alias="CertificationId"),
        pydantic.Field(alias="CertificationId"),
    ] = None
    certification_start_date: typing_extensions.Annotated[
        typing.Optional[CertificationStartDate],
        FieldMetadata(alias="CertificationStartDate"),
        pydantic.Field(alias="CertificationStartDate"),
    ] = None
    certification_uri: typing_extensions.Annotated[
        typing.Optional[ApiCertificationUri],
        FieldMetadata(alias="CertificationURI"),
        pydantic.Field(alias="CertificationURI"),
    ] = None
    profile_type: typing_extensions.Annotated[
        typing.Optional[ProfileType], FieldMetadata(alias="ProfileType"), pydantic.Field(alias="ProfileType")
    ] = None
    profile_variant: typing_extensions.Annotated[
        typing.Optional[ProfileVariant], FieldMetadata(alias="ProfileVariant"), pydantic.Field(alias="ProfileVariant")
    ] = None
    profile_version: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="ProfileVersion"),
        pydantic.Field(alias="ProfileVersion", description="The version number of the certification"),
    ] = None
    """
    The version number of the certification
    """

    software_statement_id: typing_extensions.Annotated[
        typing.Optional[SoftwareStatementId],
        FieldMetadata(alias="SoftwareStatementId"),
        pydantic.Field(alias="SoftwareStatementId"),
    ] = None
    status: typing_extensions.Annotated[
        typing.Optional[SoftwareStatementCertificationStatus],
        FieldMetadata(alias="Status"),
        pydantic.Field(alias="Status", description="Is this certification current or expired"),
    ] = None
    """
    Is this certification current or expired
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
