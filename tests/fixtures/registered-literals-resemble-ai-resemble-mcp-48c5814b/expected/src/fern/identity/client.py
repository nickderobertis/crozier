

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawIdentityClient, RawIdentityClient
from .types.create_identity_response import CreateIdentityResponse
from .types.list_identities_response import ListIdentitiesResponse
from .types.search_identities_response import SearchIdentitiesResponse


OMIT = typing.cast(typing.Any, ...)


class IdentityClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIdentityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIdentityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIdentityClient
        """
        return self._raw_client

    def list_identities(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListIdentitiesResponse:
        """
        List all speaker identities

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListIdentitiesResponse
            List of identities

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity.list_identities()
        """
        _response = self._raw_client.list_identities(request_options=request_options)
        return _response.data

    def create_identity(
        self,
        *,
        audio_url: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateIdentityResponse:
        """
        Create a new speaker identity

        Parameters
        ----------
        audio_url : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateIdentityResponse
            Identity created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity.create_identity(
            audio_url="audio_url",
        )
        """
        _response = self._raw_client.create_identity(audio_url=audio_url, name=name, request_options=request_options)
        return _response.data

    def search_identities(
        self, *, audio_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchIdentitiesResponse:
        """
        Search for matching speaker identities

        Parameters
        ----------
        audio_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchIdentitiesResponse
            Search results

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.identity.search_identities(
            audio_url="audio_url",
        )
        """
        _response = self._raw_client.search_identities(audio_url=audio_url, request_options=request_options)
        return _response.data


class AsyncIdentityClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIdentityClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIdentityClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIdentityClient
        """
        return self._raw_client

    async def list_identities(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListIdentitiesResponse:
        """
        List all speaker identities

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListIdentitiesResponse
            List of identities

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity.list_identities()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_identities(request_options=request_options)
        return _response.data

    async def create_identity(
        self,
        *,
        audio_url: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateIdentityResponse:
        """
        Create a new speaker identity

        Parameters
        ----------
        audio_url : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateIdentityResponse
            Identity created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity.create_identity(
                audio_url="audio_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_identity(
            audio_url=audio_url, name=name, request_options=request_options
        )
        return _response.data

    async def search_identities(
        self, *, audio_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> SearchIdentitiesResponse:
        """
        Search for matching speaker identities

        Parameters
        ----------
        audio_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchIdentitiesResponse
            Search results

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.identity.search_identities(
                audio_url="audio_url",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_identities(audio_url=audio_url, request_options=request_options)
        return _response.data
