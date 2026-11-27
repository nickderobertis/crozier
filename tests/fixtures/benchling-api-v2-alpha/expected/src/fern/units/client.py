

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.unit_type import UnitType
from .raw_client import AsyncRawUnitsClient, RawUnitsClient
from .types.list_unit_types_response import ListUnitTypesResponse


class UnitsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUnitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUnitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUnitsClient
        """
        return self._raw_client

    def list_unit_types(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListUnitTypesResponse:
        """
        List all unit types in the tenant Unit Dictionary, including their constituent units.

        Parameters
        ----------
        next_token : typing.Optional[str]
            Token for pagination

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUnitTypesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.units.list_unit_types()
        """
        _response = self._raw_client.list_unit_types(
            next_token=next_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    def get_unit_type(self, unit_type_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> UnitType:
        """
        Get a specific unit type, including constituent units.

        Parameters
        ----------
        unit_type_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitType
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.units.get_unit_type(
            unit_type_id="qnty_7W2R1EFJ",
        )
        """
        _response = self._raw_client.get_unit_type(unit_type_id, request_options=request_options)
        return _response.data


class AsyncUnitsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUnitsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUnitsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUnitsClient
        """
        return self._raw_client

    async def list_unit_types(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListUnitTypesResponse:
        """
        List all unit types in the tenant Unit Dictionary, including their constituent units.

        Parameters
        ----------
        next_token : typing.Optional[str]
            Token for pagination

        page_size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListUnitTypesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.units.list_unit_types()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_unit_types(
            next_token=next_token, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def get_unit_type(
        self, unit_type_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UnitType:
        """
        Get a specific unit type, including constituent units.

        Parameters
        ----------
        unit_type_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitType
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.units.get_unit_type(
                unit_type_id="qnty_7W2R1EFJ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_unit_type(unit_type_id, request_options=request_options)
        return _response.data
