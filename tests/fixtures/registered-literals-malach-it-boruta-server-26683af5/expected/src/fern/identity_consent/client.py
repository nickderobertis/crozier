

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentityConsentClient, RawIdentityConsentClient


OMIT = typing.cast(typing.Any, ...)


class IdentityConsentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityConsentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityConsentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityConsentClient
        """
        return self._raw_client

    def display_the_consent_page(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_consent.display_the_consent_page()
        """
        _response = self._raw_client.display_the_consent_page(request_options=request_options)
        return _response.data

    def record_user_consent(
        self,
        *,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        scopes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity_consent.record_user_consent()
        """
        _response = self._raw_client.record_user_consent(scopes=scopes, request_options=request_options)
        return _response.data


class AsyncIdentityConsentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityConsentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityConsentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityConsentClient
        """
        return self._raw_client

    async def display_the_consent_page(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            HTML page

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_consent.display_the_consent_page()


        asyncio.run(main())
        """
        _response = await self._raw_client.display_the_consent_page(request_options=request_options)
        return _response.data

    async def record_user_consent(
        self,
        *,
        scopes: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        scopes : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity_consent.record_user_consent()


        asyncio.run(main())
        """
        _response = await self._raw_client.record_user_consent(scopes=scopes, request_options=request_options)
        return _response.data
