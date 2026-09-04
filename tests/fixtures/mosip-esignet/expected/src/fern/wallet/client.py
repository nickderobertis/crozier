

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWalletClient, RawWalletClient
from .types.post_authorization_link_transaction_request_request import PostAuthorizationLinkTransactionRequestRequest
from .types.post_authorization_link_transaction_response import PostAuthorizationLinkTransactionResponse
from .types.post_authorization_link_transaction_v2request_request import (
    PostAuthorizationLinkTransactionV2RequestRequest,
)
from .types.post_authorization_link_transaction_v2response import PostAuthorizationLinkTransactionV2Response
from .types.post_linked_authenticate_request_request import PostLinkedAuthenticateRequestRequest
from .types.post_linked_authenticate_response import PostLinkedAuthenticateResponse
from .types.post_linked_authenticate_v2request_request import PostLinkedAuthenticateV2RequestRequest
from .types.post_linked_authenticate_v2response import PostLinkedAuthenticateV2Response
from .types.post_linked_consent_request_request import PostLinkedConsentRequestRequest
from .types.post_linked_consent_response import PostLinkedConsentResponse
from .types.post_linked_consent_v2request_request import PostLinkedConsentV2RequestRequest
from .types.post_linked_consent_v2response import PostLinkedConsentV2Response


OMIT = typing.cast(typing.Any, ...)


class WalletClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWalletClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWalletClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWalletClient
        """
        return self._raw_client

    def post_authorization_link_transaction(
        self,
        *,
        request_time: str,
        request: PostAuthorizationLinkTransactionRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationLinkTransactionResponse:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        request_time : str

        request : PostAuthorizationLinkTransactionRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationLinkTransactionResponse
            OK

        Examples
        --------
        from fern.wallet import PostAuthorizationLinkTransactionRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wallet.post_authorization_link_transaction(
            request_time="2023-09-22T08:01:10.000Z",
            request=PostAuthorizationLinkTransactionRequestRequest(
                link_code="xl4cnYtLQkGRxUj",
            ),
        )
        """
        _response = self._raw_client.post_authorization_link_transaction(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_authorization_link_transaction_v2(
        self,
        *,
        request_time: str,
        request: PostAuthorizationLinkTransactionV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationLinkTransactionV2Response:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        request_time : str

        request : PostAuthorizationLinkTransactionV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationLinkTransactionV2Response
            OK

        Examples
        --------
        from fern.wallet import PostAuthorizationLinkTransactionV2RequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wallet.post_authorization_link_transaction_v2(
            request_time="2023-09-22T08:01:10.000Z",
            request=PostAuthorizationLinkTransactionV2RequestRequest(
                link_code="xl4cnYtLQkGRxUj",
            ),
        )
        """
        _response = self._raw_client.post_authorization_link_transaction_v2(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_linked_authenticate(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedAuthenticateRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinkedAuthenticateResponse:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates linkedTransactionId.
        2. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: Only linkTransactionId is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedAuthenticateRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinkedAuthenticateResponse
            OK

        Examples
        --------
        import datetime

        from fern.wallet import PostLinkedAuthenticateRequestRequest

        from fern import (
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wallet.post_linked_authenticate(
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:10+00:00",
            ),
            request=PostLinkedAuthenticateRequestRequest(
                linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
                individual_id="34543276756",
                challenge_list=[
                    AuthChallenge(
                        auth_factor_type=AuthChallengeAuthFactorType.OTP,
                        challenge="111111",
                        format=AuthChallengeFormat.ALPHA_NUMERIC,
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.post_linked_authenticate(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_linked_authenticate_v2(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedAuthenticateV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinkedAuthenticateV2Response:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates linkedTransactionId.
        2. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. Relays error from integrated authentication server to UI on failure.
        6. It validates stored userconsent against the requested claims and scopes

        On Authentication Success: linkTransactionId and consentAction is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedAuthenticateV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinkedAuthenticateV2Response
            OK

        Examples
        --------
        import datetime

        from fern.wallet import PostLinkedAuthenticateV2RequestRequest

        from fern import (
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wallet.post_linked_authenticate_v2(
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:10+00:00",
            ),
            request=PostLinkedAuthenticateV2RequestRequest(
                linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
                individual_id="34543276756",
                challenge_list=[
                    AuthChallenge(
                        auth_factor_type=AuthChallengeAuthFactorType.OTP,
                        challenge="111111",
                        format=AuthChallengeFormat.ALPHA_NUMERIC,
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.post_linked_authenticate_v2(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_linked_consent(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedConsentRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinkedConsentResponse:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

        1. Validates linkedTransactionId.
        2. Validate accepted claims and permitted scopes in the request.
        3. If valid, stores the accepted claims and permitted scopes in the cache.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedConsentRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinkedConsentResponse
            OK

        Examples
        --------
        import datetime

        from fern.wallet import PostLinkedConsentRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wallet.post_linked_consent(
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:10+00:00",
            ),
            request=PostLinkedConsentRequestRequest(
                linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
                permitted_authorize_scopes=["permittedAuthorizeScopes"],
                accepted_claims=["name", "email", "phone_number", "address"],
            ),
        )
        """
        _response = self._raw_client.post_linked_consent(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    def post_linked_consent_v2(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedConsentV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinkedConsentV2Response:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

        1. Validates linkedTransactionId.
        2. Validate accepted claims and permitted scopes in the request and the signature.
        3. If valid, stores the accepted claims, permitted scopes and signature in the consent registry.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedConsentV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinkedConsentV2Response
            OK

        Examples
        --------
        import datetime

        from fern.wallet import PostLinkedConsentV2RequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wallet.post_linked_consent_v2(
            request_time=datetime.datetime.fromisoformat(
                "2023-09-22 08:01:13+00:00",
            ),
            request=PostLinkedConsentV2RequestRequest(
                linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
                permitted_authorize_scopes=["permittedAuthorizeScopes"],
                accepted_claims=["name", "email", "phone_number", "address"],
                signature="<detached signature>",
            ),
        )
        """
        _response = self._raw_client.post_linked_consent_v2(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data


class AsyncWalletClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWalletClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWalletClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWalletClient
        """
        return self._raw_client

    async def post_authorization_link_transaction(
        self,
        *,
        request_time: str,
        request: PostAuthorizationLinkTransactionRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationLinkTransactionResponse:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        request_time : str

        request : PostAuthorizationLinkTransactionRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationLinkTransactionResponse
            OK

        Examples
        --------
        import asyncio

        from fern.wallet import PostAuthorizationLinkTransactionRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wallet.post_authorization_link_transaction(
                request_time="2023-09-22T08:01:10.000Z",
                request=PostAuthorizationLinkTransactionRequestRequest(
                    link_code="xl4cnYtLQkGRxUj",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_authorization_link_transaction(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_authorization_link_transaction_v2(
        self,
        *,
        request_time: str,
        request: PostAuthorizationLinkTransactionV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAuthorizationLinkTransactionV2Response:
        """
        The link transaction endpoint is invoked from Wallet-app.

        1. Validates the link-code and its expiry and generates the linkTransactionId. This linkTransactionId is linked to transactionId returned from /oauth-details endpoint.

        2. Returns the auth-factors, clientName, logoUrl, User claims, authorize scopes along with linkTransactionId.

        **Note:**
        Wallet-app will hereafter address the transaction with this linkTransactionId for the /authenticate and /consent endpoints.

        Parameters
        ----------
        request_time : str

        request : PostAuthorizationLinkTransactionV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAuthorizationLinkTransactionV2Response
            OK

        Examples
        --------
        import asyncio

        from fern.wallet import PostAuthorizationLinkTransactionV2RequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wallet.post_authorization_link_transaction_v2(
                request_time="2023-09-22T08:01:10.000Z",
                request=PostAuthorizationLinkTransactionV2RequestRequest(
                    link_code="xl4cnYtLQkGRxUj",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_authorization_link_transaction_v2(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_linked_authenticate(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedAuthenticateRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinkedAuthenticateResponse:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates linkedTransactionId.
        2. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. Relays error from integrated authentication server to UI on failure.

        On Authentication Success: Only linkTransactionId is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedAuthenticateRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinkedAuthenticateResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.wallet import PostLinkedAuthenticateRequestRequest

        from fern import (
            AsyncFernApi,
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wallet.post_linked_authenticate(
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:10+00:00",
                ),
                request=PostLinkedAuthenticateRequestRequest(
                    linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
                    individual_id="34543276756",
                    challenge_list=[
                        AuthChallenge(
                            auth_factor_type=AuthChallengeAuthFactorType.OTP,
                            challenge="111111",
                            format=AuthChallengeFormat.ALPHA_NUMERIC,
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_linked_authenticate(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_linked_authenticate_v2(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedAuthenticateV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinkedAuthenticateV2Response:
        """
        Once end user provides the user identifier (UIN/VID) and all the required auth challenge to the Wallet-app, this endpoint will be invoked from wallet-app.

        Supported auth-challenge depends on the integrated authentication server.

        1. Validates linkedTransactionId.
        2. Validates null / empty individualId.
        4. Invokes kyc-auth call to integrated authentication server (IDA).
        5. Relays error from integrated authentication server to UI on failure.
        6. It validates stored userconsent against the requested claims and scopes

        On Authentication Success: linkTransactionId and consentAction is returned in the below response without any errors.

        On Authentication Failure: Error list will be set with the errors returned from the integrated authentication server.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedAuthenticateV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinkedAuthenticateV2Response
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.wallet import PostLinkedAuthenticateV2RequestRequest

        from fern import (
            AsyncFernApi,
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wallet.post_linked_authenticate_v2(
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:10+00:00",
                ),
                request=PostLinkedAuthenticateV2RequestRequest(
                    linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
                    individual_id="34543276756",
                    challenge_list=[
                        AuthChallenge(
                            auth_factor_type=AuthChallengeAuthFactorType.OTP,
                            challenge="111111",
                            format=AuthChallengeFormat.ALPHA_NUMERIC,
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_linked_authenticate_v2(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_linked_consent(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedConsentRequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinkedConsentResponse:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

        1. Validates linkedTransactionId.
        2. Validate accepted claims and permitted scopes in the request.
        3. If valid, stores the accepted claims and permitted scopes in the cache.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedConsentRequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinkedConsentResponse
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.wallet import PostLinkedConsentRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wallet.post_linked_consent(
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:10+00:00",
                ),
                request=PostLinkedConsentRequestRequest(
                    linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
                    permitted_authorize_scopes=["permittedAuthorizeScopes"],
                    accepted_claims=["name", "email", "phone_number", "address"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_linked_consent(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data

    async def post_linked_consent_v2(
        self,
        *,
        request_time: dt.datetime,
        request: PostLinkedConsentV2RequestRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostLinkedConsentV2Response:
        """
        Once the authentication is successful and user consent is obtained, this endpoint will be invoked by the wallet app to send the accepted consent and permitted scopes.

        1. Validates linkedTransactionId.
        2. Validate accepted claims and permitted scopes in the request and the signature.
        3. If valid, stores the accepted claims, permitted scopes and signature in the consent registry.

        Parameters
        ----------
        request_time : dt.datetime

        request : PostLinkedConsentV2RequestRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostLinkedConsentV2Response
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern.wallet import PostLinkedConsentV2RequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wallet.post_linked_consent_v2(
                request_time=datetime.datetime.fromisoformat(
                    "2023-09-22 08:01:13+00:00",
                ),
                request=PostLinkedConsentV2RequestRequest(
                    linked_transaction_id="qwert_yt46_hX0xlBJNExl9cnYtL8kGvcbf555",
                    permitted_authorize_scopes=["permittedAuthorizeScopes"],
                    accepted_claims=["name", "email", "phone_number", "address"],
                    signature="<detached signature>",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_linked_consent_v2(
            request_time=request_time, request=request, request_options=request_options
        )
        return _response.data
