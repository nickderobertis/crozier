

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAmenitiesClient, RawAmenitiesClient
from .types.amenities_list_response import AmenitiesListResponse
from .types.amenities_update_response import AmenitiesUpdateResponse


OMIT = typing.cast(typing.Any, ...)


class AmenitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAmenitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAmenitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAmenitiesClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> AmenitiesListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AmenitiesListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.amenities.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def update(
        self, id: int, *, label: str, sort_order: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AmenitiesUpdateResponse:
        """
        Parameters
        ----------
        id : int

        label : str

        sort_order : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AmenitiesUpdateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.amenities.update(
            id=1,
            label="label",
            sort_order=1,
        )
        """
        _response = self._raw_client.update(id, label=label, sort_order=sort_order, request_options=request_options)
        return _response.data


class AsyncAmenitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAmenitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAmenitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAmenitiesClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> AmenitiesListResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AmenitiesListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.amenities.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def update(
        self, id: int, *, label: str, sort_order: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AmenitiesUpdateResponse:
        """
        Parameters
        ----------
        id : int

        label : str

        sort_order : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AmenitiesUpdateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.amenities.update(
                id=1,
                label="label",
                sort_order=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id, label=label, sort_order=sort_order, request_options=request_options
        )
        return _response.data
