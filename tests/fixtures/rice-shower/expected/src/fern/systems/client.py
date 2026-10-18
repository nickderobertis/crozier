

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawSystemsClient, RawSystemsClient
from .types.create_system_request_heaters_item import CreateSystemRequestHeatersItem
from .types.create_system_request_thermos_item import CreateSystemRequestThermosItem
from .types.create_system_response import CreateSystemResponse
from .types.delete_system_response import DeleteSystemResponse
from .types.get_system_response import GetSystemResponse
from .types.list_systems_response_item import ListSystemsResponseItem
from .types.update_system_request_heaters_item import UpdateSystemRequestHeatersItem
from .types.update_system_request_thermos_item import UpdateSystemRequestThermosItem
from .types.update_system_response import UpdateSystemResponse


OMIT = typing.cast(typing.Any, ...)


class SystemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSystemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSystemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSystemsClient
        """
        return self._raw_client

    def list_systems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListSystemsResponseItem]:
        """
        List all registered systems with their thermometers and heaters

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListSystemsResponseItem]
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.systems.list_systems()
        """
        _response = self._raw_client.list_systems(request_options=request_options)
        return _response.data

    def create_system(
        self,
        *,
        id: str,
        display_name: str,
        thermo_url: str,
        heater_url: str,
        thermos: typing.Sequence[CreateSystemRequestThermosItem],
        heaters: typing.Sequence[CreateSystemRequestHeatersItem],
        location: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSystemResponse:
        """
        Register a new system with thermometers and heaters

        Parameters
        ----------
        id : str
            Unique system slug

        display_name : str
            Human-readable name

        thermo_url : str
            Base URL to thermo/ls-api

        heater_url : str
            Base URL to heater-api

        thermos : typing.Sequence[CreateSystemRequestThermosItem]

        heaters : typing.Sequence[CreateSystemRequestHeatersItem]

        location : typing.Optional[str]
            Physical location

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSystemResponse
            Response for status 200

        Examples
        --------
        from fern.systems import (
            CreateSystemRequestHeatersItem,
            CreateSystemRequestThermosItem,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.systems.create_system(
            id="id",
            display_name="displayName",
            thermo_url="thermoUrl",
            heater_url="heaterUrl",
            thermos=[
                CreateSystemRequestThermosItem(
                    channel=1.1,
                )
            ],
            heaters=[
                CreateSystemRequestHeatersItem(
                    channel=1.1,
                )
            ],
        )
        """
        _response = self._raw_client.create_system(
            id=id,
            display_name=display_name,
            thermo_url=thermo_url,
            heater_url=heater_url,
            thermos=thermos,
            heaters=heaters,
            location=location,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def get_system(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetSystemResponse:
        """
        Get a single system by ID with its thermometers and heaters

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.systems.get_system(
            id="id",
        )
        """
        _response = self._raw_client.get_system(id, request_options=request_options)
        return _response.data

    def update_system(
        self,
        id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        thermo_url: typing.Optional[str] = OMIT,
        heater_url: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        thermos: typing.Optional[typing.Sequence[UpdateSystemRequestThermosItem]] = OMIT,
        heaters: typing.Optional[typing.Sequence[UpdateSystemRequestHeatersItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSystemResponse:
        """
        Update an existing system. Thermos/heaters are replaced if provided.

        Parameters
        ----------
        id : str

        display_name : typing.Optional[str]

        location : typing.Optional[str]

        thermo_url : typing.Optional[str]

        heater_url : typing.Optional[str]

        enabled : typing.Optional[bool]

        thermos : typing.Optional[typing.Sequence[UpdateSystemRequestThermosItem]]

        heaters : typing.Optional[typing.Sequence[UpdateSystemRequestHeatersItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.systems.update_system(
            id="id",
        )
        """
        _response = self._raw_client.update_system(
            id,
            display_name=display_name,
            location=location,
            thermo_url=thermo_url,
            heater_url=heater_url,
            enabled=enabled,
            thermos=thermos,
            heaters=heaters,
            request_options=request_options,
        )
        return _response.data

    def delete_system(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSystemResponse:
        """
        Delete a system and all its associated thermometers and heaters

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSystemResponse
            Response for status 200

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.systems.delete_system(
            id="id",
        )
        """
        _response = self._raw_client.delete_system(id, request_options=request_options)
        return _response.data


class AsyncSystemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSystemsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSystemsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSystemsClient
        """
        return self._raw_client

    async def list_systems(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ListSystemsResponseItem]:
        """
        List all registered systems with their thermometers and heaters

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ListSystemsResponseItem]
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.systems.list_systems()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_systems(request_options=request_options)
        return _response.data

    async def create_system(
        self,
        *,
        id: str,
        display_name: str,
        thermo_url: str,
        heater_url: str,
        thermos: typing.Sequence[CreateSystemRequestThermosItem],
        heaters: typing.Sequence[CreateSystemRequestHeatersItem],
        location: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateSystemResponse:
        """
        Register a new system with thermometers and heaters

        Parameters
        ----------
        id : str
            Unique system slug

        display_name : str
            Human-readable name

        thermo_url : str
            Base URL to thermo/ls-api

        heater_url : str
            Base URL to heater-api

        thermos : typing.Sequence[CreateSystemRequestThermosItem]

        heaters : typing.Sequence[CreateSystemRequestHeatersItem]

        location : typing.Optional[str]
            Physical location

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateSystemResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern.systems import (
            CreateSystemRequestHeatersItem,
            CreateSystemRequestThermosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.systems.create_system(
                id="id",
                display_name="displayName",
                thermo_url="thermoUrl",
                heater_url="heaterUrl",
                thermos=[
                    CreateSystemRequestThermosItem(
                        channel=1.1,
                    )
                ],
                heaters=[
                    CreateSystemRequestHeatersItem(
                        channel=1.1,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_system(
            id=id,
            display_name=display_name,
            thermo_url=thermo_url,
            heater_url=heater_url,
            thermos=thermos,
            heaters=heaters,
            location=location,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def get_system(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSystemResponse:
        """
        Get a single system by ID with its thermometers and heaters

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSystemResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.systems.get_system(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_system(id, request_options=request_options)
        return _response.data

    async def update_system(
        self,
        id: str,
        *,
        display_name: typing.Optional[str] = OMIT,
        location: typing.Optional[str] = OMIT,
        thermo_url: typing.Optional[str] = OMIT,
        heater_url: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        thermos: typing.Optional[typing.Sequence[UpdateSystemRequestThermosItem]] = OMIT,
        heaters: typing.Optional[typing.Sequence[UpdateSystemRequestHeatersItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSystemResponse:
        """
        Update an existing system. Thermos/heaters are replaced if provided.

        Parameters
        ----------
        id : str

        display_name : typing.Optional[str]

        location : typing.Optional[str]

        thermo_url : typing.Optional[str]

        heater_url : typing.Optional[str]

        enabled : typing.Optional[bool]

        thermos : typing.Optional[typing.Sequence[UpdateSystemRequestThermosItem]]

        heaters : typing.Optional[typing.Sequence[UpdateSystemRequestHeatersItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.systems.update_system(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_system(
            id,
            display_name=display_name,
            location=location,
            thermo_url=thermo_url,
            heater_url=heater_url,
            enabled=enabled,
            thermos=thermos,
            heaters=heaters,
            request_options=request_options,
        )
        return _response.data

    async def delete_system(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteSystemResponse:
        """
        Delete a system and all its associated thermometers and heaters

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteSystemResponse
            Response for status 200

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.systems.delete_system(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_system(id, request_options=request_options)
        return _response.data
