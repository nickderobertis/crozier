

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLampsClient, RawLampsClient
from .types.get_lamp_response import GetLampResponse
from .types.update_lamp_settings_response import UpdateLampSettingsResponse


OMIT = typing.cast(typing.Any, ...)


class LampsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLampsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLampsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLampsClient
        """
        return self._raw_client

    def get_lamp(
        self, lamp_id: str, *, wattage: int, shade: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLampResponse:
        """
        Parameters
        ----------
        lamp_id : str

        wattage : int

        shade : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLampResponse
            The lamp

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.lamps.get_lamp(
            lamp_id="lmp_8f2kq",
            wattage=60,
            shade="amber-glass",
        )
        """
        _response = self._raw_client.get_lamp(lamp_id, wattage=wattage, shade=shade, request_options=request_options)
        return _response.data

    def get_lamp_manual(
        self, lamp_id: str, *, edition: str, shade: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        lamp_id : str

        edition : str

        shade : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.lamps.get_lamp_manual(
            lamp_id="lmp_8f2kq",
            edition="second",
            shade="amber-glass",
        )
        """
        _response = self._raw_client.get_lamp_manual(
            lamp_id, edition=edition, shade=shade, request_options=request_options
        )
        return _response.data

    def update_lamp_settings(
        self, lamp_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateLampSettingsResponse:
        """
        Parameters
        ----------
        lamp_id : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLampSettingsResponse
            Updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.lamps.update_lamp_settings(
            lamp_id="lampId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_lamp_settings(lamp_id, request=request, request_options=request_options)
        return _response.data


class AsyncLampsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLampsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLampsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLampsClient
        """
        return self._raw_client

    async def get_lamp(
        self, lamp_id: str, *, wattage: int, shade: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetLampResponse:
        """
        Parameters
        ----------
        lamp_id : str

        wattage : int

        shade : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLampResponse
            The lamp

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.lamps.get_lamp(
                lamp_id="lmp_8f2kq",
                wattage=60,
                shade="amber-glass",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lamp(
            lamp_id, wattage=wattage, shade=shade, request_options=request_options
        )
        return _response.data

    async def get_lamp_manual(
        self, lamp_id: str, *, edition: str, shade: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        lamp_id : str

        edition : str

        shade : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.lamps.get_lamp_manual(
                lamp_id="lmp_8f2kq",
                edition="second",
                shade="amber-glass",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_lamp_manual(
            lamp_id, edition=edition, shade=shade, request_options=request_options
        )
        return _response.data

    async def update_lamp_settings(
        self, lamp_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateLampSettingsResponse:
        """
        Parameters
        ----------
        lamp_id : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLampSettingsResponse
            Updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.lamps.update_lamp_settings(
                lamp_id="lampId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_lamp_settings(
            lamp_id, request=request, request_options=request_options
        )
        return _response.data
