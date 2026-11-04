

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_preparation_time_response import PaginatedPreparationTimeResponse
from .raw_client import AsyncRawPreparationtimeClient, RawPreparationtimeClient
from .types.preparation_time import PreparationTime


OMIT = typing.cast(typing.Any, ...)


class PreparationtimeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPreparationtimeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPreparationtimeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPreparationtimeClient
        """
        return self._raw_client

    def get_all_preparationtime(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedPreparationTimeResponse:
        """
        Retrieves all preparation times the server knows in a paginated format

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
        PaginatedPreparationTimeResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.preparationtime.get_all_preparationtime()
        """
        _response = self._raw_client.get_all_preparationtime(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create_preparationtime(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        duration: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreparationTime:
        """
        Creates a preparation time

        Parameters
        ----------
        id : typing.Optional[str]
            ID of a Peparation Time

        duration : typing.Optional[int]
            name of a Peparation Time

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreparationTime
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.preparationtime.create_preparationtime(
            duration=75,
        )
        """
        _response = self._raw_client.create_preparationtime(id=id, duration=duration, request_options=request_options)
        return _response.data

    def get_preparationtime(
        self, preparation_time_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreparationTime:
        """
        Get a single preparationID

        Parameters
        ----------
        preparation_time_id : str
            UUID of a PreparationTime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreparationTime
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.preparationtime.get_preparationtime(
            preparation_time_id="PreparationTimeID",
        )
        """
        _response = self._raw_client.get_preparationtime(preparation_time_id, request_options=request_options)
        return _response.data

    def put_preparationtime(
        self,
        preparation_time_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        duration: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreparationTime:
        """
        Update preparation time entry

        Parameters
        ----------
        preparation_time_id : str
            UUID of a PreparationTime

        id : typing.Optional[str]
            ID of a Peparation Time

        duration : typing.Optional[int]
            name of a Peparation Time

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreparationTime
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.preparationtime.put_preparationtime(
            preparation_time_id="PreparationTimeID",
            duration=75,
        )
        """
        _response = self._raw_client.put_preparationtime(
            preparation_time_id, id=id, duration=duration, request_options=request_options
        )
        return _response.data

    def delete_preparationtime(
        self, preparation_time_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a preparation time object

        Parameters
        ----------
        preparation_time_id : str
            UUID of a PreparationTime

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
        client.preparationtime.delete_preparationtime(
            preparation_time_id="PreparationTimeID",
        )
        """
        _response = self._raw_client.delete_preparationtime(preparation_time_id, request_options=request_options)
        return _response.data


class AsyncPreparationtimeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPreparationtimeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPreparationtimeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPreparationtimeClient
        """
        return self._raw_client

    async def get_all_preparationtime(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedPreparationTimeResponse:
        """
        Retrieves all preparation times the server knows in a paginated format

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
        PaginatedPreparationTimeResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.preparationtime.get_all_preparationtime()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_preparationtime(
            page=page, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_preparationtime(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        duration: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreparationTime:
        """
        Creates a preparation time

        Parameters
        ----------
        id : typing.Optional[str]
            ID of a Peparation Time

        duration : typing.Optional[int]
            name of a Peparation Time

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreparationTime
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.preparationtime.create_preparationtime(
                duration=75,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_preparationtime(
            id=id, duration=duration, request_options=request_options
        )
        return _response.data

    async def get_preparationtime(
        self, preparation_time_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreparationTime:
        """
        Get a single preparationID

        Parameters
        ----------
        preparation_time_id : str
            UUID of a PreparationTime

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreparationTime
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.preparationtime.get_preparationtime(
                preparation_time_id="PreparationTimeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_preparationtime(preparation_time_id, request_options=request_options)
        return _response.data

    async def put_preparationtime(
        self,
        preparation_time_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        duration: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreparationTime:
        """
        Update preparation time entry

        Parameters
        ----------
        preparation_time_id : str
            UUID of a PreparationTime

        id : typing.Optional[str]
            ID of a Peparation Time

        duration : typing.Optional[int]
            name of a Peparation Time

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreparationTime
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.preparationtime.put_preparationtime(
                preparation_time_id="PreparationTimeID",
                duration=75,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_preparationtime(
            preparation_time_id, id=id, duration=duration, request_options=request_options
        )
        return _response.data

    async def delete_preparationtime(
        self, preparation_time_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a preparation time object

        Parameters
        ----------
        preparation_time_id : str
            UUID of a PreparationTime

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
            await client.preparationtime.delete_preparationtime(
                preparation_time_id="PreparationTimeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_preparationtime(preparation_time_id, request_options=request_options)
        return _response.data
