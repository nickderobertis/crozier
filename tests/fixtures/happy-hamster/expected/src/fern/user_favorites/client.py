

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.location import Location
from ..types.location_id import LocationId
from .raw_client import AsyncRawUserFavoritesClient, RawUserFavoritesClient


class UserFavoritesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUserFavoritesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUserFavoritesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUserFavoritesClient
        """
        return self._raw_client

    def list_favorites(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Location]:
        """
        List all favorite locations for the currently logged in user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Location]
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_favorites.list_favorites()
        """
        _response = self._raw_client.list_favorites(request_options=request_options)
        return _response.data

    def add_favorite_by_location_id(
        self, id: LocationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Location:
        """
        Add a favorite by location id for the currently logged in user.

        Parameters
        ----------
        id : LocationId
            id of the location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_favorites.add_favorite_by_location_id(
            id=73621836,
        )
        """
        _response = self._raw_client.add_favorite_by_location_id(id, request_options=request_options)
        return _response.data

    def delete_favorite_by_location_id(
        self, id: LocationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Location:
        """
        Remove a favorite by location id for the currently logged in user.

        Parameters
        ----------
        id : LocationId
            id of the location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.user_favorites.delete_favorite_by_location_id(
            id=73621836,
        )
        """
        _response = self._raw_client.delete_favorite_by_location_id(id, request_options=request_options)
        return _response.data


class AsyncUserFavoritesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUserFavoritesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUserFavoritesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUserFavoritesClient
        """
        return self._raw_client

    async def list_favorites(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Location]:
        """
        List all favorite locations for the currently logged in user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Location]
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_favorites.list_favorites()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_favorites(request_options=request_options)
        return _response.data

    async def add_favorite_by_location_id(
        self, id: LocationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Location:
        """
        Add a favorite by location id for the currently logged in user.

        Parameters
        ----------
        id : LocationId
            id of the location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_favorites.add_favorite_by_location_id(
                id=73621836,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_favorite_by_location_id(id, request_options=request_options)
        return _response.data

    async def delete_favorite_by_location_id(
        self, id: LocationId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Location:
        """
        Remove a favorite by location id for the currently logged in user.

        Parameters
        ----------
        id : LocationId
            id of the location

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Location
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.user_favorites.delete_favorite_by_location_id(
                id=73621836,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_favorite_by_location_id(id, request_options=request_options)
        return _response.data
