

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.index_response_object import IndexResponseObject
from .raw_client import AsyncRawApiKeyClient, RawApiKeyClient


OMIT = typing.cast(typing.Any, ...)


class ApiKeyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApiKeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApiKeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApiKeyClient
        """
        return self._raw_client

    def get_api_key_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IndexResponseObject]:
        """
        Get info about all indices associated with the specified API key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IndexResponseObject]
            Indices found, returns a list of index info

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.api_key.get_api_key_info()
        """
        _response = self._raw_client.get_api_key_info(request_options=request_options)
        return _response.data

    def create_api_key(
        self,
        *,
        indices_max: int,
        indices_size_max: int,
        documents_max: int,
        operations_max: int,
        rate_limit: typing.Optional[int] = OMIT,
        demo: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Creates an API key and returns the Base64 encoded API key.
        Expects the Base64 encoded master API key in the header.
        Use the **master API key displayed** in the server console at startup.

        WARNING: make sure to set the MASTER_KEY_SECRET environment variable to a secret, otherwise your generated API keys will be compromised.
        For development purposes you may also use the SeekStorm server console command 'create' to create an demo API key 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='.

        Parameters
        ----------
        indices_max : int
            number of indices per API key

        indices_size_max : int
            combined index size per API key in MB

        documents_max : int
            combined number of documents in all indices per API key

        operations_max : int
            operations per month per API key: index/update/delete/query doc

        rate_limit : typing.Optional[int]
            queries per sec per API key

        demo : typing.Optional[bool]
            create fixed demo api key instead of random api key for demo purposes (default=false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            API key created, returns Base64 encoded API key

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.api_key.create_api_key(
            indices_max=1,
            indices_size_max=1,
            documents_max=1,
            operations_max=1,
        )
        """
        _response = self._raw_client.create_api_key(
            indices_max=indices_max,
            indices_size_max=indices_size_max,
            documents_max=documents_max,
            operations_max=operations_max,
            rate_limit=rate_limit,
            demo=demo,
            request_options=request_options,
        )
        return _response.data

    def delete_api_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Deletes an API key and returns the number of remaining API keys.
        Expects the Base64 encoded master API key in the header.
        WARNING: This will delete all indices and documents associated with the API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            API key deleted, returns number of remaining API keys

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.api_key.delete_api_key()
        """
        _response = self._raw_client.delete_api_key(request_options=request_options)
        return _response.data


class AsyncApiKeyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApiKeyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApiKeyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApiKeyClient
        """
        return self._raw_client

    async def get_api_key_info(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[IndexResponseObject]:
        """
        Get info about all indices associated with the specified API key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[IndexResponseObject]
            Indices found, returns a list of index info

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.api_key.get_api_key_info()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_key_info(request_options=request_options)
        return _response.data

    async def create_api_key(
        self,
        *,
        indices_max: int,
        indices_size_max: int,
        documents_max: int,
        operations_max: int,
        rate_limit: typing.Optional[int] = OMIT,
        demo: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Creates an API key and returns the Base64 encoded API key.
        Expects the Base64 encoded master API key in the header.
        Use the **master API key displayed** in the server console at startup.

        WARNING: make sure to set the MASTER_KEY_SECRET environment variable to a secret, otherwise your generated API keys will be compromised.
        For development purposes you may also use the SeekStorm server console command 'create' to create an demo API key 'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA='.

        Parameters
        ----------
        indices_max : int
            number of indices per API key

        indices_size_max : int
            combined index size per API key in MB

        documents_max : int
            combined number of documents in all indices per API key

        operations_max : int
            operations per month per API key: index/update/delete/query doc

        rate_limit : typing.Optional[int]
            queries per sec per API key

        demo : typing.Optional[bool]
            create fixed demo api key instead of random api key for demo purposes (default=false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            API key created, returns Base64 encoded API key

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.api_key.create_api_key(
                indices_max=1,
                indices_size_max=1,
                documents_max=1,
                operations_max=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_api_key(
            indices_max=indices_max,
            indices_size_max=indices_size_max,
            documents_max=documents_max,
            operations_max=operations_max,
            rate_limit=rate_limit,
            demo=demo,
            request_options=request_options,
        )
        return _response.data

    async def delete_api_key(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Deletes an API key and returns the number of remaining API keys.
        Expects the Base64 encoded master API key in the header.
        WARNING: This will delete all indices and documents associated with the API key.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            API key deleted, returns number of remaining API keys

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.api_key.delete_api_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_key(request_options=request_options)
        return _response.data
