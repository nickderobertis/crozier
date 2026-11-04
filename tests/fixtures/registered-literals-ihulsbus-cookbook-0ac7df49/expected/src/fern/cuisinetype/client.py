

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_cuisine_type_response import PaginatedCuisineTypeResponse
from .raw_client import AsyncRawCuisinetypeClient, RawCuisinetypeClient
from .types.cuisine_type import CuisineType


OMIT = typing.cast(typing.Any, ...)


class CuisinetypeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCuisinetypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCuisinetypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCuisinetypeClient
        """
        return self._raw_client

    def get_all_cuisinetype(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCuisineTypeResponse:
        """
        Get all cuisinetypes known to the API in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCuisineTypeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cuisinetype.get_all_cuisinetype()
        """
        _response = self._raw_client.get_all_cuisinetype(page=page, limit=limit, request_options=request_options)
        return _response.data

    def get_cuisinetype(
        self, cuisine_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CuisineType:
        """
        Get a single cuisinetype definition

        Parameters
        ----------
        cuisine_type_id : str
            UUID of a cuisine type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CuisineType
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cuisinetype.get_cuisinetype(
            cuisine_type_id="CuisineTypeID",
        )
        """
        _response = self._raw_client.get_cuisinetype(cuisine_type_id, request_options=request_options)
        return _response.data

    def update_cuisinetype(
        self,
        cuisine_type_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CuisineType:
        """
        Update a cuisinetype definition

        Parameters
        ----------
        cuisine_type_id : str
            UUID of a cuisine type

        id : typing.Optional[str]
            ID of a cuisine type

        name : typing.Optional[str]
            name of a cuisine type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CuisineType
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.cuisinetype.update_cuisinetype(
            cuisine_type_id="CuisineTypeID",
            name="Italian",
        )
        """
        _response = self._raw_client.update_cuisinetype(
            cuisine_type_id, id=id, name=name, request_options=request_options
        )
        return _response.data

    def delete_cuisinetype(
        self, cuisine_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a cuisinetype

        Parameters
        ----------
        cuisine_type_id : str
            UUID of a cuisine type

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
        client.cuisinetype.delete_cuisinetype(
            cuisine_type_id="CuisineTypeID",
        )
        """
        _response = self._raw_client.delete_cuisinetype(cuisine_type_id, request_options=request_options)
        return _response.data


class AsyncCuisinetypeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCuisinetypeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCuisinetypeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCuisinetypeClient
        """
        return self._raw_client

    async def get_all_cuisinetype(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedCuisineTypeResponse:
        """
        Get all cuisinetypes known to the API in a paginated format

        Parameters
        ----------
        page : typing.Optional[int]
            Page number (1-indexed)

        limit : typing.Optional[int]
            Number of items per page (max 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedCuisineTypeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cuisinetype.get_all_cuisinetype()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_cuisinetype(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def get_cuisinetype(
        self, cuisine_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CuisineType:
        """
        Get a single cuisinetype definition

        Parameters
        ----------
        cuisine_type_id : str
            UUID of a cuisine type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CuisineType
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cuisinetype.get_cuisinetype(
                cuisine_type_id="CuisineTypeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_cuisinetype(cuisine_type_id, request_options=request_options)
        return _response.data

    async def update_cuisinetype(
        self,
        cuisine_type_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CuisineType:
        """
        Update a cuisinetype definition

        Parameters
        ----------
        cuisine_type_id : str
            UUID of a cuisine type

        id : typing.Optional[str]
            ID of a cuisine type

        name : typing.Optional[str]
            name of a cuisine type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CuisineType
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.cuisinetype.update_cuisinetype(
                cuisine_type_id="CuisineTypeID",
                name="Italian",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_cuisinetype(
            cuisine_type_id, id=id, name=name, request_options=request_options
        )
        return _response.data

    async def delete_cuisinetype(
        self, cuisine_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a cuisinetype

        Parameters
        ----------
        cuisine_type_id : str
            UUID of a cuisine type

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
            await client.cuisinetype.delete_cuisinetype(
                cuisine_type_id="CuisineTypeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_cuisinetype(cuisine_type_id, request_options=request_options)
        return _response.data
