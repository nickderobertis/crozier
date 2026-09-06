

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .api_certification_uri import ApiCertificationUri
from .api_endpoint import ApiEndpoint
from .api_family_type import ApiFamilyType
from .api_resource_request_certification_status import ApiResourceRequestCertificationStatus


class ApiResourceRequest(UniversalBaseModel):
    api_certification_uri: typing_extensions.Annotated[
        typing.Optional[ApiCertificationUri],
        FieldMetadata(alias="ApiCertificationUri"),
        pydantic.Field(alias="ApiCertificationUri"),
    ] = None
    api_endpoint: typing_extensions.Annotated[
        typing.Optional[ApiEndpoint], FieldMetadata(alias="ApiEndpoint"), pydantic.Field(alias="ApiEndpoint")
    ] = None
    api_family_type: typing_extensions.Annotated[
        ApiFamilyType, FieldMetadata(alias="ApiFamilyType"), pydantic.Field(alias="ApiFamilyType")
    ]
    api_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ApiVersion"),
        pydantic.Field(alias="ApiVersion", description="The version number of the API"),
    ]
    """
    The version number of the API
    """

    certification_start_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="CertificationStartDate"),
        pydantic.Field(alias="CertificationStartDate"),
    ] = None
    certification_status: typing_extensions.Annotated[
        typing.Optional[ApiResourceRequestCertificationStatus],
        FieldMetadata(alias="CertificationStatus"),
        pydantic.Field(alias="CertificationStatus", description="Is this certification current or expired"),
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
