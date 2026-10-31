

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUnitsClient, RawUnitsClient
from .types.units_by_id_response import UnitsByIdResponse
from .types.units_create_request_unit_type import UnitsCreateRequestUnitType
from .types.units_create_response import UnitsCreateResponse
from .types.units_delete_response import UnitsDeleteResponse
from .types.units_list_response import UnitsListResponse
from .types.units_update_request_unit_type import UnitsUpdateRequestUnitType
from .types.units_update_response import UnitsUpdateResponse


OMIT = typing.cast(typing.Any, ...)


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

    def list(
        self, *, property_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> UnitsListResponse:
        """
        Parameters
        ----------
        property_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsListResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.units.list()
        """
        _response = self._raw_client.list(property_id=property_id, request_options=request_options)
        return _response.data

    def create(
        self,
        *,
        name: str,
        market_rate_cents: int,
        unit_type: UnitsCreateRequestUnitType,
        property_id: int,
        bedrooms: typing.Optional[int] = OMIT,
        bathrooms: typing.Optional[float] = OMIT,
        square_feet: typing.Optional[int] = OMIT,
        utility_type_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        amenity_type_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnitsCreateResponse:
        """
        Parameters
        ----------
        name : str

        market_rate_cents : int

        unit_type : UnitsCreateRequestUnitType

        property_id : int

        bedrooms : typing.Optional[int]

        bathrooms : typing.Optional[float]

        square_feet : typing.Optional[int]

        utility_type_ids : typing.Optional[typing.Sequence[int]]

        amenity_type_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsCreateResponse
            Successful response

        Examples
        --------
        from fern.units import UnitsCreateRequestUnitType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.units.create(
            name="name",
            market_rate_cents=1,
            unit_type=UnitsCreateRequestUnitType.RESIDENTIAL,
            property_id=1,
        )
        """
        _response = self._raw_client.create(
            name=name,
            market_rate_cents=market_rate_cents,
            unit_type=unit_type,
            property_id=property_id,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            square_feet=square_feet,
            utility_type_ids=utility_type_ids,
            amenity_type_ids=amenity_type_ids,
            request_options=request_options,
        )
        return _response.data

    def byid(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> UnitsByIdResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsByIdResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.units.byid(
            id=1,
        )
        """
        _response = self._raw_client.byid(id, request_options=request_options)
        return _response.data

    def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> UnitsDeleteResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.units.delete(
            id=1,
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def update(
        self,
        id: int,
        *,
        name: str,
        market_rate_cents: int,
        unit_type: UnitsUpdateRequestUnitType,
        bedrooms: typing.Optional[int] = OMIT,
        bathrooms: typing.Optional[float] = OMIT,
        square_feet: typing.Optional[int] = OMIT,
        utility_type_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        amenity_type_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnitsUpdateResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        market_rate_cents : int

        unit_type : UnitsUpdateRequestUnitType

        bedrooms : typing.Optional[int]

        bathrooms : typing.Optional[float]

        square_feet : typing.Optional[int]

        utility_type_ids : typing.Optional[typing.Sequence[int]]

        amenity_type_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsUpdateResponse
            Successful response

        Examples
        --------
        from fern.units import UnitsUpdateRequestUnitType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.units.update(
            id=1,
            name="name",
            market_rate_cents=1,
            unit_type=UnitsUpdateRequestUnitType.RESIDENTIAL,
        )
        """
        _response = self._raw_client.update(
            id,
            name=name,
            market_rate_cents=market_rate_cents,
            unit_type=unit_type,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            square_feet=square_feet,
            utility_type_ids=utility_type_ids,
            amenity_type_ids=amenity_type_ids,
            request_options=request_options,
        )
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

    async def list(
        self, *, property_id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> UnitsListResponse:
        """
        Parameters
        ----------
        property_id : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsListResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.units.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(property_id=property_id, request_options=request_options)
        return _response.data

    async def create(
        self,
        *,
        name: str,
        market_rate_cents: int,
        unit_type: UnitsCreateRequestUnitType,
        property_id: int,
        bedrooms: typing.Optional[int] = OMIT,
        bathrooms: typing.Optional[float] = OMIT,
        square_feet: typing.Optional[int] = OMIT,
        utility_type_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        amenity_type_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnitsCreateResponse:
        """
        Parameters
        ----------
        name : str

        market_rate_cents : int

        unit_type : UnitsCreateRequestUnitType

        property_id : int

        bedrooms : typing.Optional[int]

        bathrooms : typing.Optional[float]

        square_feet : typing.Optional[int]

        utility_type_ids : typing.Optional[typing.Sequence[int]]

        amenity_type_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsCreateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.units import UnitsCreateRequestUnitType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.units.create(
                name="name",
                market_rate_cents=1,
                unit_type=UnitsCreateRequestUnitType.RESIDENTIAL,
                property_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            name=name,
            market_rate_cents=market_rate_cents,
            unit_type=unit_type,
            property_id=property_id,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            square_feet=square_feet,
            utility_type_ids=utility_type_ids,
            amenity_type_ids=amenity_type_ids,
            request_options=request_options,
        )
        return _response.data

    async def byid(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> UnitsByIdResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsByIdResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.units.byid(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.byid(id, request_options=request_options)
        return _response.data

    async def delete(self, id: int, *, request_options: typing.Optional[RequestOptions] = None) -> UnitsDeleteResponse:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.units.delete(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def update(
        self,
        id: int,
        *,
        name: str,
        market_rate_cents: int,
        unit_type: UnitsUpdateRequestUnitType,
        bedrooms: typing.Optional[int] = OMIT,
        bathrooms: typing.Optional[float] = OMIT,
        square_feet: typing.Optional[int] = OMIT,
        utility_type_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        amenity_type_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UnitsUpdateResponse:
        """
        Parameters
        ----------
        id : int

        name : str

        market_rate_cents : int

        unit_type : UnitsUpdateRequestUnitType

        bedrooms : typing.Optional[int]

        bathrooms : typing.Optional[float]

        square_feet : typing.Optional[int]

        utility_type_ids : typing.Optional[typing.Sequence[int]]

        amenity_type_ids : typing.Optional[typing.Sequence[int]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UnitsUpdateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.units import UnitsUpdateRequestUnitType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.units.update(
                id=1,
                name="name",
                market_rate_cents=1,
                unit_type=UnitsUpdateRequestUnitType.RESIDENTIAL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(
            id,
            name=name,
            market_rate_cents=market_rate_cents,
            unit_type=unit_type,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            square_feet=square_feet,
            utility_type_ids=utility_type_ids,
            amenity_type_ids=amenity_type_ids,
            request_options=request_options,
        )
        return _response.data
