

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_certification_uri import ApiCertificationUri
from .authorisation_server_certification_request_status import AuthorisationServerCertificationRequestStatus
from .profile_type import ProfileType
from .profile_variant import ProfileVariant


class AuthorisationServerCertificationRequest(UniversalBaseModel):
    certification_start_date: typing_extensions.Annotated[
        typing.Optional[str],
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
        typing.Optional[AuthorisationServerCertificationRequestStatus],
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
