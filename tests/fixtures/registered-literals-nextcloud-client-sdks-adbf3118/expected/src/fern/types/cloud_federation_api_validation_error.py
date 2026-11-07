

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .cloud_federation_api_error import CloudFederationApiError
from .cloud_federation_api_validation_error_all_of import CloudFederationApiValidationErrorAllOf


class CloudFederationApiValidationError(CloudFederationApiError, CloudFederationApiValidationErrorAllOf):
    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
