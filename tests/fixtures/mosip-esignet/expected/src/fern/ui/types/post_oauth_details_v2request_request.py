

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from ...types.claim import Claim
from .post_oauth_details_v2request_request_code_challenge_method import (
    PostOauthDetailsV2RequestRequestCodeChallengeMethod,
)


class PostOauthDetailsV2RequestRequest(UniversalBaseModel):
    scope: str = pydantic.Field()
    """
    Specifies what access privileges are being requested for Access Tokens. The scopes associated with Access Tokens determine what resources will be available when they are used to access OAuth 2.0 protected endpoints. OpenID Connect requests MUST contain the OpenID scope value.
    """

    response_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="responseType"),
        pydantic.Field(
            alias="responseType",
            description="Value that determines the authorization processing flow to be used. When using the Authorization Code Flow, this value is code.",
        ),
    ]
    """
    Value that determines the authorization processing flow to be used. When using the Authorization Code Flow, this value is code.
    """

    client_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="clientId"),
        pydantic.Field(alias="clientId", description="OAuth 2.0 Client Identifier valid at the Authorization Server"),
    ]
    """
    OAuth 2.0 Client Identifier valid at the Authorization Server
    """

    redirect_uri: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="redirectUri"),
        pydantic.Field(
            alias="redirectUri",
            description="Redirection URI to which the response will be sent. This URI MUST exactly match one of the Redirection URI values for the Client pre-registered",
        ),
    ]
    """
    Redirection URI to which the response will be sent. This URI MUST exactly match one of the Redirection URI values for the Client pre-registered
    """

    state: typing.Optional[str] = pydantic.Field(default=None)
    """
    client state value echoed.
    """

    nonce: typing.Optional[str] = pydantic.Field(default=None)
    """
    Client's nonce value echoed.
    """

    display: typing.Optional[str] = pydantic.Field(default=None)
    """
    ASCII string value that specifies how the Authorization Server displays the authentication and consent user interface pages to the End-User.
    """

    prompt: typing.Optional[str] = pydantic.Field(default=None)
    """
    Space delimited, case sensitive list of ASCII string values that specifies whether the Authorization Server prompts the End-User for re-authentication and consent.
    """

    acr_values: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="acrValues"),
        pydantic.Field(
            alias="acrValues",
            description="Space separated ACR values, Unknown ACR are ignored. Only registered ACR values will be considered.\nIf none of the provided acr value is among the registered values, all the registered ACR's will be considered.",
        ),
    ] = None
    """
    Space separated ACR values, Unknown ACR are ignored. Only registered ACR values will be considered.
    If none of the provided acr value is among the registered values, all the registered ACR's will be considered.
    """

    claims: typing.Optional[Claim] = None
    max_age: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="maxAge"),
        pydantic.Field(
            alias="maxAge",
            description="Maximum Authentication Age. Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated by the OP. If the elapsed time is greater than this value, the OP MUST attempt to actively re-authenticate the End-User. (The max_age request parameter corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] max_auth_age request parameter.) When max_age is used, the ID Token returned MUST include an auth_time Claim Value.",
        ),
    ] = None
    """
    Maximum Authentication Age. Specifies the allowable elapsed time in seconds since the last time the End-User was actively authenticated by the OP. If the elapsed time is greater than this value, the OP MUST attempt to actively re-authenticate the End-User. (The max_age request parameter corresponds to the OpenID 2.0 PAPE [OpenID.PAPE] max_auth_age request parameter.) When max_age is used, the ID Token returned MUST include an auth_time Claim Value.
    """

    claims_locales: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="claimsLocales"),
        pydantic.Field(
            alias="claimsLocales",
            description="End-User's preferred languages and scripts for Claims being returned, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.",
        ),
    ] = None
    """
    End-User's preferred languages and scripts for Claims being returned, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.
    """

    ui_locales: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uiLocales"),
        pydantic.Field(
            alias="uiLocales",
            description='End-User\'s preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.',
        ),
    ] = None
    """
    End-User's preferred languages and scripts for the user interface, represented as a space-separated list of BCP47 [RFC5646] language tag values, ordered by preference. For instance, the value "fr-CA fr en" represents a preference for French as spoken in Canada, then French (without a region designation), followed by English (without a region designation). An error SHOULD NOT result if some or all of the requested locales are not supported by the OpenID Provider.
    """

    code_challenge: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="codeChallenge"),
        pydantic.Field(
            alias="codeChallenge",
            description="A challenge derived from the code verifier, to be verified against later.",
        ),
    ] = None
    """
    A challenge derived from the code verifier, to be verified against later.
    """

    code_challenge_method: typing_extensions.Annotated[
        typing.Optional[PostOauthDetailsV2RequestRequestCodeChallengeMethod],
        FieldMetadata(alias="codeChallengeMethod"),
        pydantic.Field(alias="codeChallengeMethod", description="A method that was used to derive code challenge."),
    ] = None
    """
    A method that was used to derive code challenge.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
