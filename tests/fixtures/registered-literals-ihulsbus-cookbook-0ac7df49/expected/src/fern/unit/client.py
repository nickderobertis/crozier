

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.paginated_unit_response import PaginatedUnitResponse
from .raw_client import AsyncRawUnitClient, RawUnitClient
from .types.unit import Unit


OMIT = typing.cast(typing.Any, ...)


class UnitClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUnitClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUnitClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUnitClient
        """
        return self._raw_client

    def get_al_units(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedUnitResponse:
        """
        Retrieve all units known to the API in a paginated format

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
        PaginatedUnitResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.unit.get_al_units()
        """
        _response = self._raw_client.get_al_units(page=page, limit=limit, request_options=request_options)
        return _response.data

    def create_unit(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        short_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Unit:
        """
        Create a new unit

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the unit

        full_name : typing.Optional[str]
            Full name of the unit

        short_name : typing.Optional[str]
            Abbreviation of the unit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unit
            Created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.unit.create_unit()
        """
        _response = self._raw_client.create_unit(
            id=id, full_name=full_name, short_name=short_name, request_options=request_options
        )
        return _response.data

    def get_single_unit(self, unit_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Unit:
        """
        Get a single unit

        Parameters
        ----------
        unit_id : str
            UUID of the unit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unit
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.unit.get_single_unit(
            unit_id="UnitID",
        )
        """
        _response = self._raw_client.get_single_unit(unit_id, request_options=request_options)
        return _response.data

    def update_unit(
        self,
        unit_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        short_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Unit:
        """
        Update a unit

        Parameters
        ----------
        unit_id : str
            UUID of the unit

        id : typing.Optional[str]
            ID of the unit

        full_name : typing.Optional[str]
            Full name of the unit

        short_name : typing.Optional[str]
            Abbreviation of the unit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unit
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.unit.update_unit(
            unit_id="UnitID",
        )
        """
        _response = self._raw_client.update_unit(
            unit_id, id=id, full_name=full_name, short_name=short_name, request_options=request_options
        )
        return _response.data

    def delete_unit(self, unit_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an unit

        Parameters
        ----------
        unit_id : str
            UUID of the unit

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
        client.unit.delete_unit(
            unit_id="UnitID",
        )
        """
        _response = self._raw_client.delete_unit(unit_id, request_options=request_options)
        return _response.data


class AsyncUnitClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUnitClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUnitClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUnitClient
        """
        return self._raw_client

    async def get_al_units(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedUnitResponse:
        """
        Retrieve all units known to the API in a paginated format

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
        PaginatedUnitResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.unit.get_al_units()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_al_units(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def create_unit(
        self,
        *,
        id: typing.Optional[str] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        short_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Unit:
        """
        Create a new unit

        Parameters
        ----------
        id : typing.Optional[str]
            ID of the unit

        full_name : typing.Optional[str]
            Full name of the unit

        short_name : typing.Optional[str]
            Abbreviation of the unit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unit
            Created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.unit.create_unit()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_unit(
            id=id, full_name=full_name, short_name=short_name, request_options=request_options
        )
        return _response.data

    async def get_single_unit(self, unit_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Unit:
        """
        Get a single unit

        Parameters
        ----------
        unit_id : str
            UUID of the unit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unit
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.unit.get_single_unit(
                unit_id="UnitID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_single_unit(unit_id, request_options=request_options)
        return _response.data

    async def update_unit(
        self,
        unit_id: str,
        *,
        id: typing.Optional[str] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        short_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Unit:
        """
        Update a unit

        Parameters
        ----------
        unit_id : str
            UUID of the unit

        id : typing.Optional[str]
            ID of the unit

        full_name : typing.Optional[str]
            Full name of the unit

        short_name : typing.Optional[str]
            Abbreviation of the unit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Unit
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.unit.update_unit(
                unit_id="UnitID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_unit(
            unit_id, id=id, full_name=full_name, short_name=short_name, request_options=request_options
        )
        return _response.data

    async def delete_unit(self, unit_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete an unit

        Parameters
        ----------
        unit_id : str
            UUID of the unit

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
            await client.unit.delete_unit(
                unit_id="UnitID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_unit(unit_id, request_options=request_options)
        return _response.data
