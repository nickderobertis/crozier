

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.purpose import Purpose
from .put_client_client_id_request_request_additional_config_userinfo_response_type import (
    PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType,
)


class PutClientClientIdRequestRequestAdditionalConfig(UniversalBaseModel):
    """
    This parameter allow us to configure the required values based on their specific authentication and integration needs, ensuring efficient implementation of eSignet for ID verification/authentication.
    """

    userinfo_response_type: typing.Optional[PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType] = (
        pydantic.Field(default=None)
    )
    """
    The response type for the user info endpoint should be configurable to allow the Relying Party to choose between only signed tokens or signed tokens with encryption.
    """

    purpose: typing.Optional[Purpose] = None
    signup_banner_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Relying Parties should be able to specify whether they require eSignet sign-up. If no signup service is required UI should not have “Sign up with Unified login“ option.
    """

    forgot_pwd_link_required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Relying Parties should be able to specify whether they require eSignet forgot password feature. If it is not required UI should not have “Forgot password“ option
    """

    consent_expire_in_mins: typing.Optional[float] = pydantic.Field(default=None)
    """
    The number of minuets after which a user's given consent will expire.
    """

    require_pushed_authorization_requests: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Boolean parameter indicating whether the only means of initiating an authorization request the client is allowed to use is PAR. If omitted, the default value is false.
    """

    dpop_bound_access_tokens: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean value specifying whether the client always uses DPoP for token requests. If omitted, the default value is false. If the value is true, the eSignet rejects token request from the client that do not contain the DPoP header.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
