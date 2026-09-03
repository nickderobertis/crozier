

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawWalletBackendClient, RawWalletBackendClient
from .types.post_binding_otp_request_request import PostBindingOtpRequestRequest
from .types.post_binding_otp_response import PostBindingOtpResponse
from .types.post_binding_otp_v2request_request import PostBindingOtpV2RequestRequest
from .types.post_binding_otp_v2response import PostBindingOtpV2Response
from .types.post_wallet_binding_request_request import PostWalletBindingRequestRequest
from .types.post_wallet_binding_response import PostWalletBindingResponse


OMIT = typing.cast(typing.Any, ...)


class WalletBackendClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWalletBackendClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWalletBackendClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWalletBackendClient
        """
        return self._raw_client

    def post_binding_otp(
        self,
        *,
        request_time: str,
        request: PostBindingOtpRequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostBindingOtpResponse:
        """
        Send wallet binding OTP endpoint is invoked by Mimoto server.

        Parameters
        ----------
        request_time : str

        request : PostBindingOtpRequestRequest

        partner_api_key : typing.Optional[str]
            API key of the binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostBindingOtpResponse
            OK

        Examples
        --------
        from fern.wallet_backend import PostBindingOtpRequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wallet_backend.post_binding_otp(
            request_time="2023-09-22T08:01:13.000Z",
            request=PostBindingOtpRequestRequest(
                individual_id="24554655645",
                otp_channels=["sms", "email"],
            ),
        )
        """
        _response = self._raw_client.post_binding_otp(
            request_time=request_time,
            request=request,
            partner_api_key=partner_api_key,
            partner_id=partner_id,
            request_options=request_options,
        )
        return _response.data

    def post_binding_otp_v2(
        self,
        *,
        request_time: str,
        request: PostBindingOtpV2RequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostBindingOtpV2Response:
        """
        Send wallet binding OTP endpoint is invoked by Mimoto server.

        Parameters
        ----------
        request_time : str

        request : PostBindingOtpV2RequestRequest

        partner_api_key : typing.Optional[str]
            API key of the binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostBindingOtpV2Response
            OK

        Examples
        --------
        from fern.wallet_backend import PostBindingOtpV2RequestRequest

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wallet_backend.post_binding_otp_v2(
            request_time="2023-09-22T08:01:13.000Z",
            request=PostBindingOtpV2RequestRequest(
                individual_id="24554655645",
                otp_channels=["sms", "email"],
                captcha_token="ALSKDJFURIEOQPZMKFURHFVBH",
            ),
        )
        """
        _response = self._raw_client.post_binding_otp_v2(
            request_time=request_time,
            request=request,
            partner_api_key=partner_api_key,
            partner_id=partner_id,
            request_options=request_options,
        )
        return _response.data

    def post_wallet_binding(
        self,
        *,
        request_time: str,
        request: PostWalletBindingRequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWalletBindingResponse:
        """
        Wallet binding endpoint is invoked by Mimoto server.

        1. This request is invoked from wallet-app with authChallenge.
        2. Integrated keybinder implementation validates the authChallenge.
        3. Public key registry is updated with the key binding details for the provided individualId.
        4. Binded walletUserId (WUID) is returned with keybinder signed certificate.

        **Note**: Binding entry uniqueness is combination of these 3 values -> (PSUT, public-key, auth-factor-type)

        Parameters
        ----------
        request_time : str

        request : PostWalletBindingRequestRequest

        partner_api_key : typing.Optional[str]
            API key of the Binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWalletBindingResponse
            OK

        Examples
        --------
        from fern.wallet_backend import PostWalletBindingRequestRequest

        from fern import (
            AuthChallenge,
            AuthChallengeAuthFactorType,
            AuthChallengeFormat,
            FernApi,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wallet_backend.post_wallet_binding(
            request_time="2023-09-22T08:01:15.000Z",
            request=PostWalletBindingRequestRequest(
                individual_id="24554655645",
                auth_factor_type="WLA",
                format="jwt",
                challenge_list=[
                    AuthChallenge(
                        auth_factor_type=AuthChallengeAuthFactorType.OTP,
                        challenge="111111",
                        format=AuthChallengeFormat.ALPHA_NUMERIC,
                    )
                ],
                public_key={
                    "kty": "RSA",
                    "e": "AQAB",
                    "use": "sig",
                    "alg": "RS256",
                    "n": "sfIT-5o9ZSr8lJuBsRTzodJYvEgNeIayJRd9WLip6tU9NZ_5VvVS_jq5STza9WELs127xH7e6rgGJ31B6VLBbrRRgLm2sz2_0s1p9ilRSrae0P3cJHK7aIgY0c-E1SwbzrKmV4FQKzARfHG-M-DmAD8V38LclxZycAu7gXWFVS7RPW_NpmjtVGDpnx0pKYgfJb8QgzGEbSKUGB39GRWNA2ij-6tEPQQwYSO5akyFup-bVaJrKKaIWn37iiB9T7umXnmzp-3HuP1SQp6cPQLkeWp64lozxTq4To12gbietIKyfJto7r9sra1wRyq0XNKhQvswLmuQcORJKhEMJWVCpQ",
                },
            ),
        )
        """
        _response = self._raw_client.post_wallet_binding(
            request_time=request_time,
            request=request,
            partner_api_key=partner_api_key,
            partner_id=partner_id,
            request_options=request_options,
        )
        return _response.data


class AsyncWalletBackendClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWalletBackendClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWalletBackendClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWalletBackendClient
        """
        return self._raw_client

    async def post_binding_otp(
        self,
        *,
        request_time: str,
        request: PostBindingOtpRequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostBindingOtpResponse:
        """
        Send wallet binding OTP endpoint is invoked by Mimoto server.

        Parameters
        ----------
        request_time : str

        request : PostBindingOtpRequestRequest

        partner_api_key : typing.Optional[str]
            API key of the binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostBindingOtpResponse
            OK

        Examples
        --------
        import asyncio

        from fern.wallet_backend import PostBindingOtpRequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wallet_backend.post_binding_otp(
                request_time="2023-09-22T08:01:13.000Z",
                request=PostBindingOtpRequestRequest(
                    individual_id="24554655645",
                    otp_channels=["sms", "email"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_binding_otp(
            request_time=request_time,
            request=request,
            partner_api_key=partner_api_key,
            partner_id=partner_id,
            request_options=request_options,
        )
        return _response.data

    async def post_binding_otp_v2(
        self,
        *,
        request_time: str,
        request: PostBindingOtpV2RequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostBindingOtpV2Response:
        """
        Send wallet binding OTP endpoint is invoked by Mimoto server.

        Parameters
        ----------
        request_time : str

        request : PostBindingOtpV2RequestRequest

        partner_api_key : typing.Optional[str]
            API key of the binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner Identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostBindingOtpV2Response
            OK

        Examples
        --------
        import asyncio

        from fern.wallet_backend import PostBindingOtpV2RequestRequest

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wallet_backend.post_binding_otp_v2(
                request_time="2023-09-22T08:01:13.000Z",
                request=PostBindingOtpV2RequestRequest(
                    individual_id="24554655645",
                    otp_channels=["sms", "email"],
                    captcha_token="ALSKDJFURIEOQPZMKFURHFVBH",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_binding_otp_v2(
            request_time=request_time,
            request=request,
            partner_api_key=partner_api_key,
            partner_id=partner_id,
            request_options=request_options,
        )
        return _response.data

    async def post_wallet_binding(
        self,
        *,
        request_time: str,
        request: PostWalletBindingRequestRequest,
        partner_api_key: typing.Optional[str] = None,
        partner_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWalletBindingResponse:
        """
        Wallet binding endpoint is invoked by Mimoto server.

        1. This request is invoked from wallet-app with authChallenge.
        2. Integrated keybinder implementation validates the authChallenge.
        3. Public key registry is updated with the key binding details for the provided individualId.
        4. Binded walletUserId (WUID) is returned with keybinder signed certificate.

        **Note**: Binding entry uniqueness is combination of these 3 values -> (PSUT, public-key, auth-factor-type)

        Parameters
        ----------
        request_time : str

        request : PostWalletBindingRequestRequest

        partner_api_key : typing.Optional[str]
            API key of the Binding partner, this will be passed to binder implementation to interact with authentication system.

        partner_id : typing.Optional[str]
            Binding partner identifier, this will be passed to binder implementation to interact with authentication system.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWalletBindingResponse
            OK

        Examples
        --------
        import asyncio

        from fern.wallet_backend import PostWalletBindingRequestRequest

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
            await client.wallet_backend.post_wallet_binding(
                request_time="2023-09-22T08:01:15.000Z",
                request=PostWalletBindingRequestRequest(
                    individual_id="24554655645",
                    auth_factor_type="WLA",
                    format="jwt",
                    challenge_list=[
                        AuthChallenge(
                            auth_factor_type=AuthChallengeAuthFactorType.OTP,
                            challenge="111111",
                            format=AuthChallengeFormat.ALPHA_NUMERIC,
                        )
                    ],
                    public_key={
                        "kty": "RSA",
                        "e": "AQAB",
                        "use": "sig",
                        "alg": "RS256",
                        "n": "sfIT-5o9ZSr8lJuBsRTzodJYvEgNeIayJRd9WLip6tU9NZ_5VvVS_jq5STza9WELs127xH7e6rgGJ31B6VLBbrRRgLm2sz2_0s1p9ilRSrae0P3cJHK7aIgY0c-E1SwbzrKmV4FQKzARfHG-M-DmAD8V38LclxZycAu7gXWFVS7RPW_NpmjtVGDpnx0pKYgfJb8QgzGEbSKUGB39GRWNA2ij-6tEPQQwYSO5akyFup-bVaJrKKaIWn37iiB9T7umXnmzp-3HuP1SQp6cPQLkeWp64lozxTq4To12gbietIKyfJto7r9sra1wRyq0XNKhQvswLmuQcORJKhEMJWVCpQ",
                    },
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_wallet_binding(
            request_time=request_time,
            request=request,
            partner_api_key=partner_api_key,
            partner_id=partner_id,
            request_options=request_options,
        )
        return _response.data
