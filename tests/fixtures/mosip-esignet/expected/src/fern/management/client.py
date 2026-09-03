

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawManagementClient, RawManagementClient
from .types.patch_client_client_id_request_request import PatchClientClientIdRequestRequest
from .types.patch_client_client_id_response import PatchClientClientIdResponse
from .types.post_client_mgmt_client_request_request import PostClientMgmtClientRequestRequest
from .types.post_client_mgmt_client_response import PostClientMgmtClientResponse
from .types.post_client_request_request import PostClientRequestRequest
from .types.post_client_response import PostClientResponse
from .types.post_oauth_client_request_request import PostOauthClientRequestRequest
from .types.post_oauth_client_response import PostOauthClientResponse
from .types.put_client_client_id_request_request import PutClientClientIdRequestRequest
from .types.put_client_client_id_response import PutClientClientIdResponse
from .types.put_oauth_client_client_id_request_request import PutOauthClientClientIdRequestRequest
from .types.put_oauth_client_client_id_response import PutOauthClientClientIdResponse
from .types.put_oidc_client_client_id_request_request import PutOidcClientClientIdRequestRequest
from .types.put_oidc_client_client_id_response import PutOidcClientClientIdResponse


OMIT = typing.cast(typing.Any, ...)


class ManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagementClient
        """
        return self._raw_client

    def post_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostClientResponse:
        """
        API to add new open ID connect (OIDC) clients, it can be invoked by other modules which manages the relying parties / partners.

        Each relying party can associate to one or multiple OIDC client ids.

        On create, OIDC client status will be by default set to "**active**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostClientResponse
            OK

        Examples
        --------
        import datetime

        from fern.management import (
            PostClientRequestRequest,
            PostClientRequestRequestAuthContextRefsItem,
            PostClientRequestRequestClientAuthMethodsItem,
            PostClientRequestRequestGrantTypesItem,
            PostClientRequestRequestUserClaimsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.management.post_client(
            request_time=datetime.datetime.fromisoformat(
                "2011-10-05 14:48:00+00:00",
            ),
            request=PostClientRequestRequest(
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                client_name="Fastlane e-Sim Service",
                relying_party_id="Fastlane",
                logo_uri="https://fastlane.com/fastline-esim.png",
                redirect_uris=["https://fastlane.com/homepage"],
                auth_context_refs=[
                    PostClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                    PostClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                    PostClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                ],
                public_key={
                    "kty": "RSA",
                    "e": "AQAB",
                    "use": "sig",
                    "alg": "RS256",
                    "n": "g7KPXZdZ18H2JoW9FhYz8WrSbLeKA5mO8ROW5YQVyzYDfjbRA9sy0FwpF7pa7mBmU1_G0RvD0xbEhSaFtCL5hyNVVZCfgVqNl41C7-F2yUWhfVQPhT5YnT3eH3gV9ZczhP1trNjIzGuH-8D7EDJcoxuwdGaaY-wTmEtHykHRyab08qr62hfwLuSjHAGN6VgV-Na81XIdXmR7Dwnd1U4MxWJxzRvnVlHFCBaZIG6jNJ21vbzM-DBMq1d8tvtrGQx4w3niK_sctUZ5NP1BLkQhYSEGLr-e_mbmHFCnGtuKfnfIm-PVD-6ihfEwX3j_YQT3LhphBZj7AdXg6iyyQn9EJQ",
                },
                user_claims=[
                    PostClientRequestRequestUserClaimsItem.NAME,
                    PostClientRequestRequestUserClaimsItem.EMAIL,
                    PostClientRequestRequestUserClaimsItem.PHONE_NUMBER,
                    PostClientRequestRequestUserClaimsItem.ADDRESS,
                ],
                grant_types=[PostClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE],
                client_auth_methods=[
                    PostClientRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                ],
            ),
        )
        """
        _response = self._raw_client.post_client(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_oauth_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostOauthClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOauthClientResponse:
        """
        API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

        Each relying party can associate with one or more client ids.

        On create, client status will be by default set to "**ACTIVE**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostOauthClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauthClientResponse
            OK

        Examples
        --------
        import datetime

        from fern.management import (
            PostOauthClientRequestRequest,
            PostOauthClientRequestRequestAuthContextRefsItem,
            PostOauthClientRequestRequestClientAuthMethodsItem,
            PostOauthClientRequestRequestGrantTypesItem,
            PostOauthClientRequestRequestUserClaimsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.management.post_oauth_client(
            request_time=datetime.datetime.fromisoformat(
                "2011-10-05 14:48:00+00:00",
            ),
            request=PostOauthClientRequestRequest(
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                client_name="Fastlane e-Sim Service",
                client_name_lang_map={
                    "fra": "Service e-Sim de Fastlane",
                    "ara": "خدمة فاست لين e-SIM",
                },
                relying_party_id="Fastlane",
                logo_uri="https://fastlane.com/fastlane-esim.png",
                redirect_uris=[
                    "https://fastlane.com/homepage",
                    "io.mosip.residentapp://oauth",
                ],
                auth_context_refs=[
                    PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                    PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                    PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                ],
                public_key={
                    "kty": "RSA",
                    "e": "AQAB",
                    "use": "sig",
                    "alg": "RS256",
                    "n": "g7KPXZdZ18H2JoW9FhYz8WrSbLeKA5mO8ROW5YQVyzYDfjbRA9sy0FwpF7pa7mBmU1_G0RvD0xbEhSaFtCL5hyNVVZCfgVqNl41C7-F2yUWhfVQPhT5YnT3eH3gV9ZczhP1trNjIzGuH-8D7EDJcoxuwdGaaY-wTmEtHykHRyab08qr62hfwLuSjHAGN6VgV-Na81XIdXmR7Dwnd1U4MxWJxzRvnVlHFCBaZIG6jNJ21vbzM-DBMq1d8tvtrGQx4w3niK_sctUZ5NP1BLkQhYSEGLr-e_mbmHFCnGtuKfnfIm-PVD-6ihfEwX3j_YQT3LhphBZj7AdXg6iyyQn9EJQ",
                },
                user_claims=[
                    PostOauthClientRequestRequestUserClaimsItem.NAME,
                    PostOauthClientRequestRequestUserClaimsItem.EMAIL,
                    PostOauthClientRequestRequestUserClaimsItem.PHONE_NUMBER,
                    PostOauthClientRequestRequestUserClaimsItem.ADDRESS,
                ],
                grant_types=[
                    PostOauthClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                ],
                client_auth_methods=[
                    PostOauthClientRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                ],
            ),
        )
        """
        _response = self._raw_client.post_oauth_client(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_client_mgmt_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostClientMgmtClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostClientMgmtClientResponse:
        """
        API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

        Each relying party can associate with one or more client ids.

        On create, client status will be by default set to "**ACTIVE**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostClientMgmtClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostClientMgmtClientResponse
            OK

        Examples
        --------
        import datetime

        from fern.management import (
            PostClientMgmtClientRequestRequest,
            PostClientMgmtClientRequestRequestAdditionalConfig,
            PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType,
            PostClientMgmtClientRequestRequestAuthContextRefsItem,
            PostClientMgmtClientRequestRequestClientAuthMethodsItem,
            PostClientMgmtClientRequestRequestGrantTypesItem,
            PostClientMgmtClientRequestRequestUserClaimsItem,
        )

        from fern import FernApi, Purpose, PurposeType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.management.post_client_mgmt_client(
            request_time=datetime.datetime.fromisoformat(
                "2011-10-05 14:48:00+00:00",
            ),
            request=PostClientMgmtClientRequestRequest(
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                client_name="Fastlane e-Sim Service",
                client_name_lang_map={
                    "fra": "Service e-Sim de Fastlane",
                    "ara": "خدمة فاست لين e-SIM",
                },
                relying_party_id="Fastlane",
                logo_uri="https://fastlane.com/fastlane-esim.png",
                redirect_uris=[
                    "https://fastlane.com/homepage",
                    "io.mosip.residentapp://oauth",
                ],
                auth_context_refs=[
                    PostClientMgmtClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                    PostClientMgmtClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                    PostClientMgmtClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                ],
                public_key={
                    "kty": "RSA",
                    "e": "AQAB",
                    "use": "sig",
                    "alg": "RS256",
                    "n": "g7KPXZdZ18H2JoW9FhYz8WrSbLeKA5mO8ROW5YQVyzYDfjbRA9sy0FwpF7pa7mBmU1_G0RvD0xbEhSaFtCL5hyNVVZCfgVqNl41C7-F2yUWhfVQPhT5YnT3eH3gV9ZczhP1trNjIzGuH-8D7EDJcoxuwdGaaY-wTmEtHykHRyab08qr62hfwLuSjHAGN6VgV-Na81XIdXmR7Dwnd1U4MxWJxzRvnVlHFCBaZIG6jNJ21vbzM-DBMq1d8tvtrGQx4w3niK_sctUZ5NP1BLkQhYSEGLr-e_mbmHFCnGtuKfnfIm-PVD-6ihfEwX3j_YQT3LhphBZj7AdXg6iyyQn9EJQ",
                },
                user_claims=[
                    PostClientMgmtClientRequestRequestUserClaimsItem.NAME,
                    PostClientMgmtClientRequestRequestUserClaimsItem.EMAIL,
                    PostClientMgmtClientRequestRequestUserClaimsItem.PHONE_NUMBER,
                    PostClientMgmtClientRequestRequestUserClaimsItem.ADDRESS,
                ],
                grant_types=[
                    PostClientMgmtClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                ],
                client_auth_methods=[
                    PostClientMgmtClientRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                ],
                additional_config=PostClientMgmtClientRequestRequestAdditionalConfig(
                    userinfo_response_type=PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType.JWS,
                    purpose=Purpose(
                        type=PurposeType.VERIFY,
                        title={"@none": "Title"},
                        sub_title={"@none": "subTitle"},
                    ),
                    signup_banner_required=True,
                    forgot_pwd_link_required=True,
                    consent_expire_in_mins=30.0,
                    require_pushed_authorization_requests=True,
                    dpop_bound_access_tokens=True,
                ),
            ),
        )
        """
        _response = self._raw_client.post_client_mgmt_client(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def put_oidc_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutOidcClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutOidcClientClientIdResponse:
        """
        API to update existing Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutOidcClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutOidcClientClientIdResponse
            OK

        Examples
        --------
        from fern.management import (
            PutOidcClientClientIdRequestRequest,
            PutOidcClientClientIdRequestRequestAuthContextRefsItem,
            PutOidcClientClientIdRequestRequestClientAuthMethodsItem,
            PutOidcClientClientIdRequestRequestGrantTypesItem,
            PutOidcClientClientIdRequestRequestStatus,
            PutOidcClientClientIdRequestRequestUserClaimsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.management.put_oidc_client_client_id(
            client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
            request_time="2011-10-05T14:48:00.000Z",
            request=PutOidcClientClientIdRequestRequest(
                client_name="Fastlane e-Sim Service",
                status=PutOidcClientClientIdRequestRequestStatus.ACTIVE,
                logo_uri="https://fastline.com/logo.png",
                redirect_uris=[
                    "https://fastlane.com/homepage",
                    "https://fastlane-dev.com/*",
                    "fastlaneapp://oauth/*",
                ],
                user_claims=[
                    PutOidcClientClientIdRequestRequestUserClaimsItem.NAME,
                    PutOidcClientClientIdRequestRequestUserClaimsItem.EMAIL,
                    PutOidcClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER,
                    PutOidcClientClientIdRequestRequestUserClaimsItem.ADDRESS,
                ],
                auth_context_refs=[
                    PutOidcClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                    PutOidcClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                    PutOidcClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                ],
                grant_types=[
                    PutOidcClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                ],
                client_auth_methods=[
                    PutOidcClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                ],
            ),
        )
        """
        _response = self._raw_client.put_oidc_client_client_id(
            client_id, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def put_oauth_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutOauthClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutOauthClientClientIdResponse:
        """
        API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutOauthClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutOauthClientClientIdResponse
            OK

        Examples
        --------
        from fern.management import (
            PutOauthClientClientIdRequestRequest,
            PutOauthClientClientIdRequestRequestAuthContextRefsItem,
            PutOauthClientClientIdRequestRequestClientAuthMethodsItem,
            PutOauthClientClientIdRequestRequestGrantTypesItem,
            PutOauthClientClientIdRequestRequestStatus,
            PutOauthClientClientIdRequestRequestUserClaimsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.management.put_oauth_client_client_id(
            client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
            request_time="2011-10-05T14:48:00.000Z",
            request=PutOauthClientClientIdRequestRequest(
                client_name="Fastlane e-Sim Service",
                client_name_lang_map={
                    "fra": "Service e-Sim de Fastlane",
                    "ara": "خدمة فاست لين e-SIM",
                },
                status=PutOauthClientClientIdRequestRequestStatus.ACTIVE,
                logo_uri="https://fastlane.com/logo.png",
                redirect_uris=[
                    "https://fastlane.com/homepage",
                    "http://fastlane-dev.com/*",
                    "fastlaneapp://oauth/*",
                ],
                user_claims=[
                    PutOauthClientClientIdRequestRequestUserClaimsItem.NAME,
                    PutOauthClientClientIdRequestRequestUserClaimsItem.EMAIL,
                    PutOauthClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER,
                    PutOauthClientClientIdRequestRequestUserClaimsItem.ADDRESS,
                ],
                auth_context_refs=[
                    PutOauthClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                    PutOauthClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                    PutOauthClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                ],
                grant_types=[
                    PutOauthClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                ],
                client_auth_methods=[
                    PutOauthClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                ],
            ),
        )
        """
        _response = self._raw_client.put_oauth_client_client_id(
            client_id, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def put_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutClientClientIdResponse:
        """
        API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutClientClientIdResponse
            OK

        Examples
        --------
        from fern.management import (
            PutClientClientIdRequestRequest,
            PutClientClientIdRequestRequestAdditionalConfig,
            PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType,
            PutClientClientIdRequestRequestAuthContextRefsItem,
            PutClientClientIdRequestRequestClientAuthMethodsItem,
            PutClientClientIdRequestRequestGrantTypesItem,
            PutClientClientIdRequestRequestStatus,
            PutClientClientIdRequestRequestUserClaimsItem,
        )

        from fern import FernApi, Purpose, PurposeType

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.management.put_client_client_id(
            client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
            request_time="2011-10-05T14:48:00.000Z",
            request=PutClientClientIdRequestRequest(
                client_name="Fastlane e-Sim Service",
                client_name_lang_map={
                    "fra": "Service e-Sim de Fastlane",
                    "ara": "خدمة فاست لين e-SIM",
                },
                status=PutClientClientIdRequestRequestStatus.ACTIVE,
                logo_uri="https://fastlane.com/logo.png",
                redirect_uris=[
                    "https://fastlane.com/homepage",
                    "http://fastlane-dev.com/*",
                    "fastlaneapp://oauth/*",
                ],
                user_claims=[
                    PutClientClientIdRequestRequestUserClaimsItem.NAME,
                    PutClientClientIdRequestRequestUserClaimsItem.EMAIL,
                    PutClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER,
                    PutClientClientIdRequestRequestUserClaimsItem.ADDRESS,
                ],
                auth_context_refs=[
                    PutClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                    PutClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                    PutClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                ],
                grant_types=[
                    PutClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                ],
                client_auth_methods=[
                    PutClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                ],
                additional_config=PutClientClientIdRequestRequestAdditionalConfig(
                    userinfo_response_type=PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType.JWS,
                    purpose=Purpose(
                        type=PurposeType.VERIFY,
                        title={"@none": "Title"},
                        sub_title={"@none": "subTitle"},
                    ),
                    signup_banner_required=True,
                    forgot_pwd_link_required=True,
                    consent_expire_in_mins=30.0,
                    require_pushed_authorization_requests=False,
                    dpop_bound_access_tokens=True,
                ),
            ),
        )
        """
        _response = self._raw_client.put_client_client_id(
            client_id, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def patch_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PatchClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchClientClientIdResponse:
        """
        API to partially update existing OAuth/Open ID Connect (OIDC) client. Only provided fields will be updated.

        **Special handling for encPublicKey:**
        - When set/updated: validates format and computes enc_public_key_hash
        - When explicitly set to null: clears both enc_public_key and enc_public_key_hash
        - When not present in request: leaves both fields unchanged

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PatchClientClientIdRequestRequest
            All fields are optional. Only provided fields will be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchClientClientIdResponse
            OK

        Examples
        --------
        from fern.management import (
            PatchClientClientIdRequestRequest,
            PatchClientClientIdRequestRequestStatus,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.management.patch_client_client_id(
            client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
            request_time="2024-01-15T10:30:00.000Z",
            request=PatchClientClientIdRequestRequest(
                status=PatchClientClientIdRequestRequestStatus.INACTIVE,
            ),
        )
        """
        _response = self._raw_client.patch_client_client_id(
            client_id, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data


class AsyncManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagementClient
        """
        return self._raw_client

    async def post_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostClientResponse:
        """
        API to add new open ID connect (OIDC) clients, it can be invoked by other modules which manages the relying parties / partners.

        Each relying party can associate to one or multiple OIDC client ids.

        On create, OIDC client status will be by default set to "**active**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostClientResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.management import (
            PostClientRequestRequest,
            PostClientRequestRequestAuthContextRefsItem,
            PostClientRequestRequestClientAuthMethodsItem,
            PostClientRequestRequestGrantTypesItem,
            PostClientRequestRequestUserClaimsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.management.post_client(
                request_time=datetime.datetime.fromisoformat(
                    "2011-10-05 14:48:00+00:00",
                ),
                request=PostClientRequestRequest(
                    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                    client_name="Fastlane e-Sim Service",
                    relying_party_id="Fastlane",
                    logo_uri="https://fastlane.com/fastline-esim.png",
                    redirect_uris=["https://fastlane.com/homepage"],
                    auth_context_refs=[
                        PostClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                        PostClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                        PostClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                    ],
                    public_key={
                        "kty": "RSA",
                        "e": "AQAB",
                        "use": "sig",
                        "alg": "RS256",
                        "n": "g7KPXZdZ18H2JoW9FhYz8WrSbLeKA5mO8ROW5YQVyzYDfjbRA9sy0FwpF7pa7mBmU1_G0RvD0xbEhSaFtCL5hyNVVZCfgVqNl41C7-F2yUWhfVQPhT5YnT3eH3gV9ZczhP1trNjIzGuH-8D7EDJcoxuwdGaaY-wTmEtHykHRyab08qr62hfwLuSjHAGN6VgV-Na81XIdXmR7Dwnd1U4MxWJxzRvnVlHFCBaZIG6jNJ21vbzM-DBMq1d8tvtrGQx4w3niK_sctUZ5NP1BLkQhYSEGLr-e_mbmHFCnGtuKfnfIm-PVD-6ihfEwX3j_YQT3LhphBZj7AdXg6iyyQn9EJQ",
                    },
                    user_claims=[
                        PostClientRequestRequestUserClaimsItem.NAME,
                        PostClientRequestRequestUserClaimsItem.EMAIL,
                        PostClientRequestRequestUserClaimsItem.PHONE_NUMBER,
                        PostClientRequestRequestUserClaimsItem.ADDRESS,
                    ],
                    grant_types=[
                        PostClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                    ],
                    client_auth_methods=[
                        PostClientRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_client(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_oauth_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostOauthClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostOauthClientResponse:
        """
        API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

        Each relying party can associate with one or more client ids.

        On create, client status will be by default set to "**ACTIVE**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostOauthClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostOauthClientResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.management import (
            PostOauthClientRequestRequest,
            PostOauthClientRequestRequestAuthContextRefsItem,
            PostOauthClientRequestRequestClientAuthMethodsItem,
            PostOauthClientRequestRequestGrantTypesItem,
            PostOauthClientRequestRequestUserClaimsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.management.post_oauth_client(
                request_time=datetime.datetime.fromisoformat(
                    "2011-10-05 14:48:00+00:00",
                ),
                request=PostOauthClientRequestRequest(
                    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                    client_name="Fastlane e-Sim Service",
                    client_name_lang_map={
                        "fra": "Service e-Sim de Fastlane",
                        "ara": "خدمة فاست لين e-SIM",
                    },
                    relying_party_id="Fastlane",
                    logo_uri="https://fastlane.com/fastlane-esim.png",
                    redirect_uris=[
                        "https://fastlane.com/homepage",
                        "io.mosip.residentapp://oauth",
                    ],
                    auth_context_refs=[
                        PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                        PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                        PostOauthClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                    ],
                    public_key={
                        "kty": "RSA",
                        "e": "AQAB",
                        "use": "sig",
                        "alg": "RS256",
                        "n": "g7KPXZdZ18H2JoW9FhYz8WrSbLeKA5mO8ROW5YQVyzYDfjbRA9sy0FwpF7pa7mBmU1_G0RvD0xbEhSaFtCL5hyNVVZCfgVqNl41C7-F2yUWhfVQPhT5YnT3eH3gV9ZczhP1trNjIzGuH-8D7EDJcoxuwdGaaY-wTmEtHykHRyab08qr62hfwLuSjHAGN6VgV-Na81XIdXmR7Dwnd1U4MxWJxzRvnVlHFCBaZIG6jNJ21vbzM-DBMq1d8tvtrGQx4w3niK_sctUZ5NP1BLkQhYSEGLr-e_mbmHFCnGtuKfnfIm-PVD-6ihfEwX3j_YQT3LhphBZj7AdXg6iyyQn9EJQ",
                    },
                    user_claims=[
                        PostOauthClientRequestRequestUserClaimsItem.NAME,
                        PostOauthClientRequestRequestUserClaimsItem.EMAIL,
                        PostOauthClientRequestRequestUserClaimsItem.PHONE_NUMBER,
                        PostOauthClientRequestRequestUserClaimsItem.ADDRESS,
                    ],
                    grant_types=[
                        PostOauthClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                    ],
                    client_auth_methods=[
                        PostOauthClientRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_oauth_client(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_client_mgmt_client(
        self,
        *,
        request_time: dt.datetime,
        request: PostClientMgmtClientRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostClientMgmtClientResponse:
        """
        API to add new OAuth or open ID connect (OIDC) clients. This API should be used to create client in esignet by the partner management modules in the integrated ID system.

        Each relying party can associate with one or more client ids.

        On create, client status will be by default set to "**ACTIVE**".

        Parameters
        ----------
        request_time : dt.datetime
            Current date and time when the request is sent

        request : PostClientMgmtClientRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostClientMgmtClientResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.management import (
            PostClientMgmtClientRequestRequest,
            PostClientMgmtClientRequestRequestAdditionalConfig,
            PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType,
            PostClientMgmtClientRequestRequestAuthContextRefsItem,
            PostClientMgmtClientRequestRequestClientAuthMethodsItem,
            PostClientMgmtClientRequestRequestGrantTypesItem,
            PostClientMgmtClientRequestRequestUserClaimsItem,
        )

        from fern import AsyncFernApi, Purpose, PurposeType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.management.post_client_mgmt_client(
                request_time=datetime.datetime.fromisoformat(
                    "2011-10-05 14:48:00+00:00",
                ),
                request=PostClientMgmtClientRequestRequest(
                    client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                    client_name="Fastlane e-Sim Service",
                    client_name_lang_map={
                        "fra": "Service e-Sim de Fastlane",
                        "ara": "خدمة فاست لين e-SIM",
                    },
                    relying_party_id="Fastlane",
                    logo_uri="https://fastlane.com/fastlane-esim.png",
                    redirect_uris=[
                        "https://fastlane.com/homepage",
                        "io.mosip.residentapp://oauth",
                    ],
                    auth_context_refs=[
                        PostClientMgmtClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                        PostClientMgmtClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                        PostClientMgmtClientRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                    ],
                    public_key={
                        "kty": "RSA",
                        "e": "AQAB",
                        "use": "sig",
                        "alg": "RS256",
                        "n": "g7KPXZdZ18H2JoW9FhYz8WrSbLeKA5mO8ROW5YQVyzYDfjbRA9sy0FwpF7pa7mBmU1_G0RvD0xbEhSaFtCL5hyNVVZCfgVqNl41C7-F2yUWhfVQPhT5YnT3eH3gV9ZczhP1trNjIzGuH-8D7EDJcoxuwdGaaY-wTmEtHykHRyab08qr62hfwLuSjHAGN6VgV-Na81XIdXmR7Dwnd1U4MxWJxzRvnVlHFCBaZIG6jNJ21vbzM-DBMq1d8tvtrGQx4w3niK_sctUZ5NP1BLkQhYSEGLr-e_mbmHFCnGtuKfnfIm-PVD-6ihfEwX3j_YQT3LhphBZj7AdXg6iyyQn9EJQ",
                    },
                    user_claims=[
                        PostClientMgmtClientRequestRequestUserClaimsItem.NAME,
                        PostClientMgmtClientRequestRequestUserClaimsItem.EMAIL,
                        PostClientMgmtClientRequestRequestUserClaimsItem.PHONE_NUMBER,
                        PostClientMgmtClientRequestRequestUserClaimsItem.ADDRESS,
                    ],
                    grant_types=[
                        PostClientMgmtClientRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                    ],
                    client_auth_methods=[
                        PostClientMgmtClientRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                    ],
                    additional_config=PostClientMgmtClientRequestRequestAdditionalConfig(
                        userinfo_response_type=PostClientMgmtClientRequestRequestAdditionalConfigUserinfoResponseType.JWS,
                        purpose=Purpose(
                            type=PurposeType.VERIFY,
                            title={"@none": "Title"},
                            sub_title={"@none": "subTitle"},
                        ),
                        signup_banner_required=True,
                        forgot_pwd_link_required=True,
                        consent_expire_in_mins=30.0,
                        require_pushed_authorization_requests=True,
                        dpop_bound_access_tokens=True,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_client_mgmt_client(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def put_oidc_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutOidcClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutOidcClientClientIdResponse:
        """
        API to update existing Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutOidcClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutOidcClientClientIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern.management import (
            PutOidcClientClientIdRequestRequest,
            PutOidcClientClientIdRequestRequestAuthContextRefsItem,
            PutOidcClientClientIdRequestRequestClientAuthMethodsItem,
            PutOidcClientClientIdRequestRequestGrantTypesItem,
            PutOidcClientClientIdRequestRequestStatus,
            PutOidcClientClientIdRequestRequestUserClaimsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.management.put_oidc_client_client_id(
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                request_time="2011-10-05T14:48:00.000Z",
                request=PutOidcClientClientIdRequestRequest(
                    client_name="Fastlane e-Sim Service",
                    status=PutOidcClientClientIdRequestRequestStatus.ACTIVE,
                    logo_uri="https://fastline.com/logo.png",
                    redirect_uris=[
                        "https://fastlane.com/homepage",
                        "https://fastlane-dev.com/*",
                        "fastlaneapp://oauth/*",
                    ],
                    user_claims=[
                        PutOidcClientClientIdRequestRequestUserClaimsItem.NAME,
                        PutOidcClientClientIdRequestRequestUserClaimsItem.EMAIL,
                        PutOidcClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER,
                        PutOidcClientClientIdRequestRequestUserClaimsItem.ADDRESS,
                    ],
                    auth_context_refs=[
                        PutOidcClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                        PutOidcClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                        PutOidcClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                    ],
                    grant_types=[
                        PutOidcClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                    ],
                    client_auth_methods=[
                        PutOidcClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_oidc_client_client_id(
            client_id, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def put_oauth_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutOauthClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutOauthClientClientIdResponse:
        """
        API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutOauthClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutOauthClientClientIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern.management import (
            PutOauthClientClientIdRequestRequest,
            PutOauthClientClientIdRequestRequestAuthContextRefsItem,
            PutOauthClientClientIdRequestRequestClientAuthMethodsItem,
            PutOauthClientClientIdRequestRequestGrantTypesItem,
            PutOauthClientClientIdRequestRequestStatus,
            PutOauthClientClientIdRequestRequestUserClaimsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.management.put_oauth_client_client_id(
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                request_time="2011-10-05T14:48:00.000Z",
                request=PutOauthClientClientIdRequestRequest(
                    client_name="Fastlane e-Sim Service",
                    client_name_lang_map={
                        "fra": "Service e-Sim de Fastlane",
                        "ara": "خدمة فاست لين e-SIM",
                    },
                    status=PutOauthClientClientIdRequestRequestStatus.ACTIVE,
                    logo_uri="https://fastlane.com/logo.png",
                    redirect_uris=[
                        "https://fastlane.com/homepage",
                        "http://fastlane-dev.com/*",
                        "fastlaneapp://oauth/*",
                    ],
                    user_claims=[
                        PutOauthClientClientIdRequestRequestUserClaimsItem.NAME,
                        PutOauthClientClientIdRequestRequestUserClaimsItem.EMAIL,
                        PutOauthClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER,
                        PutOauthClientClientIdRequestRequestUserClaimsItem.ADDRESS,
                    ],
                    auth_context_refs=[
                        PutOauthClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                        PutOauthClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                        PutOauthClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                    ],
                    grant_types=[
                        PutOauthClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                    ],
                    client_auth_methods=[
                        PutOauthClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_oauth_client_client_id(
            client_id, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def put_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PutClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PutClientClientIdResponse:
        """
        API to update existing OAuth/Open ID Connect (OIDC) client, it can be invoked by other modules which manages the relying parties / partners when there any updates on the fields accepted in this API.

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PutClientClientIdRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PutClientClientIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern.management import (
            PutClientClientIdRequestRequest,
            PutClientClientIdRequestRequestAdditionalConfig,
            PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType,
            PutClientClientIdRequestRequestAuthContextRefsItem,
            PutClientClientIdRequestRequestClientAuthMethodsItem,
            PutClientClientIdRequestRequestGrantTypesItem,
            PutClientClientIdRequestRequestStatus,
            PutClientClientIdRequestRequestUserClaimsItem,
        )

        from fern import AsyncFernApi, Purpose, PurposeType

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.management.put_client_client_id(
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                request_time="2011-10-05T14:48:00.000Z",
                request=PutClientClientIdRequestRequest(
                    client_name="Fastlane e-Sim Service",
                    client_name_lang_map={
                        "fra": "Service e-Sim de Fastlane",
                        "ara": "خدمة فاست لين e-SIM",
                    },
                    status=PutClientClientIdRequestRequestStatus.ACTIVE,
                    logo_uri="https://fastlane.com/logo.png",
                    redirect_uris=[
                        "https://fastlane.com/homepage",
                        "http://fastlane-dev.com/*",
                        "fastlaneapp://oauth/*",
                    ],
                    user_claims=[
                        PutClientClientIdRequestRequestUserClaimsItem.NAME,
                        PutClientClientIdRequestRequestUserClaimsItem.EMAIL,
                        PutClientClientIdRequestRequestUserClaimsItem.PHONE_NUMBER,
                        PutClientClientIdRequestRequestUserClaimsItem.ADDRESS,
                    ],
                    auth_context_refs=[
                        PutClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_BIOMETRICS,
                        PutClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_GENERATED_CODE,
                        PutClientClientIdRequestRequestAuthContextRefsItem.MOSIP_IDP_ACR_LINKED_WALLET,
                    ],
                    grant_types=[
                        PutClientClientIdRequestRequestGrantTypesItem.AUTHORIZATION_CODE
                    ],
                    client_auth_methods=[
                        PutClientClientIdRequestRequestClientAuthMethodsItem.PRIVATE_KEY_JWT
                    ],
                    additional_config=PutClientClientIdRequestRequestAdditionalConfig(
                        userinfo_response_type=PutClientClientIdRequestRequestAdditionalConfigUserinfoResponseType.JWS,
                        purpose=Purpose(
                            type=PurposeType.VERIFY,
                            title={"@none": "Title"},
                            sub_title={"@none": "subTitle"},
                        ),
                        signup_banner_required=True,
                        forgot_pwd_link_required=True,
                        consent_expire_in_mins=30.0,
                        require_pushed_authorization_requests=False,
                        dpop_bound_access_tokens=True,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_client_client_id(
            client_id, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def patch_client_client_id(
        self,
        client_id: str,
        *,
        request_time: str,
        request: PatchClientClientIdRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PatchClientClientIdResponse:
        """
        API to partially update existing OAuth/Open ID Connect (OIDC) client. Only provided fields will be updated.

        **Special handling for encPublicKey:**
        - When set/updated: validates format and computes enc_public_key_hash
        - When explicitly set to null: clears both enc_public_key and enc_public_key_hash
        - When not present in request: leaves both fields unchanged

        **Authentication and authorization** is based on a valid JWT issued by a trusted IAM system including "**update_oidc_client**" scope.

        Parameters
        ----------
        client_id : str
            Client Identifier

        request_time : str
            Current date and time when the request is sent

        request : PatchClientClientIdRequestRequest
            All fields are optional. Only provided fields will be updated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PatchClientClientIdResponse
            OK

        Examples
        --------
        import asyncio

        from fern.management import (
            PatchClientClientIdRequestRequest,
            PatchClientClientIdRequestRequestStatus,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.management.patch_client_client_id(
                client_id="WMX5pO6dYdCFR3iaVWGclVPNxTNSADDv",
                request_time="2024-01-15T10:30:00.000Z",
                request=PatchClientClientIdRequestRequest(
                    status=PatchClientClientIdRequestRequestStatus.INACTIVE,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_client_client_id(
            client_id, request_time=request_time, request=request, request_options=request_options
        )
        return _response.data
