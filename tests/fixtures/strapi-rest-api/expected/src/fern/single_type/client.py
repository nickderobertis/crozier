

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.entry_single_response import EntrySingleResponse
from .raw_client import AsyncRawSingleTypeClient, RawSingleTypeClient


OMIT = typing.cast(typing.Any, ...)


class SingleTypeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSingleTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSingleTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSingleTypeClient
        """
        return self._raw_client

    def update_single_type(
        self,
        api_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntrySingleResponse:
        """
        For a single type (`apiId` = singular API ID), update the one global entry, creating it if absent. Collection-type entries are updated at `/{apiId}/{documentId}` instead. Note: updating over REST publishes the entry; there is no REST route to unpublish.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntrySingleResponse
            Updated single-type entry.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.single_type.update_single_type(
            api_id="apiId",
            data={"key": "value"},
        )
        """
        _response = self._raw_client.update_single_type(api_id, data=data, request_options=request_options)
        return _response.data

    def delete_single_type(self, api_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        For a single type (`apiId` = singular API ID), delete the one global entry. Collection-type entries are deleted at `/{apiId}/{documentId}` instead.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

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
        client.single_type.delete_single_type(
            api_id="apiId",
        )
        """
        _response = self._raw_client.delete_single_type(api_id, request_options=request_options)
        return _response.data


class AsyncSingleTypeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSingleTypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSingleTypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSingleTypeClient
        """
        return self._raw_client

    async def update_single_type(
        self,
        api_id: str,
        *,
        data: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntrySingleResponse:
        """
        For a single type (`apiId` = singular API ID), update the one global entry, creating it if absent. Collection-type entries are updated at `/{apiId}/{documentId}` instead. Note: updating over REST publishes the entry; there is no REST route to unpublish.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

        data : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntrySingleResponse
            Updated single-type entry.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.single_type.update_single_type(
                api_id="apiId",
                data={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_single_type(api_id, data=data, request_options=request_options)
        return _response.data

    async def delete_single_type(self, api_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        For a single type (`apiId` = singular API ID), delete the one global entry. Collection-type entries are deleted at `/{apiId}/{documentId}` instead.

        Parameters
        ----------
        api_id : str
            The content type's API ID: the plural API ID for a collection type (e.g. `articles`, `page-metadatas`) or the singular API ID for a single type (e.g. `homepage`, `global`).

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
            await client.single_type.delete_single_type(
                api_id="apiId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_single_type(api_id, request_options=request_options)
        return _response.data
