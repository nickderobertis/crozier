

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.expectation import Expectation
from .raw_client import AsyncRawOidcClient, RawOidcClient


OMIT = typing.cast(typing.Any, ...)


class OidcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOidcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOidcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOidcClient
        """
        return self._raw_client

    def mock_oidc_provider(
        self,
        *,
        issuer: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        private_key_pem: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        token_expiry_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Expectation]:
        """
        Generates a set of expectations that emulate an OpenID Connect / OAuth2 provider (discovery document, JWKS, token, authorize, userinfo and related endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        issuer : typing.Optional[str]
            issuer URL advertised in the discovery document and token claims

        client_id : typing.Optional[str]
            OAuth2 client identifier

        client_secret : typing.Optional[str]
            OAuth2 client secret

        private_key_pem : typing.Optional[str]
            PEM-encoded signing private key (never serialized back in responses)

        scopes : typing.Optional[typing.Sequence[str]]
            supported OAuth2 / OIDC scopes

        token_expiry_seconds : typing.Optional[int]
            lifetime of issued access tokens in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            OIDC provider expectations created

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.oidc.mock_oidc_provider(
            issuer="http://localhost:1080",
            client_id="my-app",
            scopes=["openid", "profile", "email"],
            token_expiry_seconds=7200,
        )
        """
        _response = self._raw_client.mock_oidc_provider(
            issuer=issuer,
            client_id=client_id,
            client_secret=client_secret,
            private_key_pem=private_key_pem,
            scopes=scopes,
            token_expiry_seconds=token_expiry_seconds,
            request_options=request_options,
        )
        return _response.data


class AsyncOidcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOidcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOidcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOidcClient
        """
        return self._raw_client

    async def mock_oidc_provider(
        self,
        *,
        issuer: typing.Optional[str] = OMIT,
        client_id: typing.Optional[str] = OMIT,
        client_secret: typing.Optional[str] = OMIT,
        private_key_pem: typing.Optional[str] = OMIT,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        token_expiry_seconds: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Expectation]:
        """
        Generates a set of expectations that emulate an OpenID Connect / OAuth2 provider (discovery document, JWKS, token, authorize, userinfo and related endpoints) and adds them. An empty body uses the default provider configuration.

        Parameters
        ----------
        issuer : typing.Optional[str]
            issuer URL advertised in the discovery document and token claims

        client_id : typing.Optional[str]
            OAuth2 client identifier

        client_secret : typing.Optional[str]
            OAuth2 client secret

        private_key_pem : typing.Optional[str]
            PEM-encoded signing private key (never serialized back in responses)

        scopes : typing.Optional[typing.Sequence[str]]
            supported OAuth2 / OIDC scopes

        token_expiry_seconds : typing.Optional[int]
            lifetime of issued access tokens in seconds

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Expectation]
            OIDC provider expectations created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.oidc.mock_oidc_provider(
                issuer="http://localhost:1080",
                client_id="my-app",
                scopes=["openid", "profile", "email"],
                token_expiry_seconds=7200,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mock_oidc_provider(
            issuer=issuer,
            client_id=client_id,
            client_secret=client_secret,
            private_key_pem=private_key_pem,
            scopes=scopes,
            token_expiry_seconds=token_expiry_seconds,
            request_options=request_options,
        )
        return _response.data
