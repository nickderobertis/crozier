

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_certification_uri import ApiCertificationUri
from .api_discovery_endpoint import ApiDiscoveryEndpoint
from .api_family_type import ApiFamilyType
from .api_resource_certification_status import ApiResourceCertificationStatus
from .api_resource_id import ApiResourceId
from .certification_expiration_date import CertificationExpirationDate
from .certification_start_date import CertificationStartDate


class ApiResource(UniversalBaseModel):
    api_certification_uri: typing_extensions.Annotated[
        typing.Optional[ApiCertificationUri],
        FieldMetadata(alias="ApiCertificationUri"),
        pydantic.Field(alias="ApiCertificationUri"),
    ] = None
    api_discovery_endpoints: typing_extensions.Annotated[
        typing.Optional[typing.List[ApiDiscoveryEndpoint]],
        FieldMetadata(alias="ApiDiscoveryEndpoints"),
        pydantic.Field(alias="ApiDiscoveryEndpoints"),
    ] = None
    api_family_type: typing_extensions.Annotated[
        typing.Optional[ApiFamilyType], FieldMetadata(alias="ApiFamilyType"), pydantic.Field(alias="ApiFamilyType")
    ] = None
    api_resource_id: typing_extensions.Annotated[
        typing.Optional[ApiResourceId], FieldMetadata(alias="ApiResourceId"), pydantic.Field(alias="ApiResourceId")
    ] = None
    api_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ApiVersion"),
        pydantic.Field(alias="ApiVersion", description="The version number of the API"),
    ] = None
    """
    The version number of the API
    """

    certification_expiration_date: typing_extensions.Annotated[
        typing.Optional[CertificationExpirationDate],
        FieldMetadata(alias="CertificationExpirationDate"),
        pydantic.Field(alias="CertificationExpirationDate"),
    ] = None
    certification_start_date: typing_extensions.Annotated[
        typing.Optional[CertificationStartDate],
        FieldMetadata(alias="CertificationStartDate"),
        pydantic.Field(alias="CertificationStartDate"),
    ] = None
    certification_status: typing_extensions.Annotated[
        typing.Optional[ApiResourceCertificationStatus],
        FieldMetadata(alias="CertificationStatus"),
        pydantic.Field(alias="CertificationStatus", description="Is this certification current or expired"),
    ] = None
    """
    Is this certification current or expired
    """

    family_complete: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="FamilyComplete"),
        pydantic.Field(
            alias="FamilyComplete",
            description="Denotes whether or not the api resource has had all related api endpoints published",
        ),
    ] = None
    """
    Denotes whether or not the api resource has had all related api endpoints published
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
