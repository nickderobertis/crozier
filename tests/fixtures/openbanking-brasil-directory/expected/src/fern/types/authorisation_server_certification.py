

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_certification_uri import ApiCertificationUri
from .authorisation_server_certification_id import AuthorisationServerCertificationId
from .authorisation_server_certification_status import AuthorisationServerCertificationStatus
from .authorisation_server_id import AuthorisationServerId
from .certification_expiration_date import CertificationExpirationDate
from .certification_start_date import CertificationStartDate
from .profile_type import ProfileType
from .profile_variant import ProfileVariant


class AuthorisationServerCertification(UniversalBaseModel):
    authorisation_server_id: typing_extensions.Annotated[
        typing.Optional[AuthorisationServerId],
        FieldMetadata(alias="AuthorisationServerId"),
        pydantic.Field(alias="AuthorisationServerId"),
    ] = None
    certification_expiration_date: typing_extensions.Annotated[
        typing.Optional[CertificationExpirationDate],
        FieldMetadata(alias="CertificationExpirationDate"),
        pydantic.Field(alias="CertificationExpirationDate"),
    ] = None
    certification_id: typing_extensions.Annotated[
        typing.Optional[AuthorisationServerCertificationId],
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

    status: typing_extensions.Annotated[
        typing.Optional[AuthorisationServerCertificationStatus],
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
