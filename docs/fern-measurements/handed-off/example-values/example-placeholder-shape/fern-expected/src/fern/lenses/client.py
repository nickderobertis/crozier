

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawLensesClient, RawLensesClient
from .types.append_lens_logs_response import AppendLensLogsResponse
from .types.update_lens_settings_response import UpdateLensSettingsResponse


OMIT = typing.cast(typing.Any, ...)


class LensesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLensesClient
        """
        return self._raw_client

    def update_lens_settings(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateLensSettingsResponse:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLensSettingsResponse
            Updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.lenses.update_lens_settings(
            request={"0": "focus", "1": "tilt"},
        )
        """
        _response = self._raw_client.update_lens_settings(request=request, request_options=request_options)
        return _response.data

    def append_lens_logs(
        self,
        lens_id: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppendLensLogsResponse:
        """
        Parameters
        ----------
        lens_id : int

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppendLensLogsResponse
            Appended

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.lenses.append_lens_logs(
            lens_id=1000000,
            request={
                "0": {"note": "wiped", "keeper": "Tamsin"},
                "1": {"note": "realigned", "keeper": "Jory"},
            },
        )
        """
        _response = self._raw_client.append_lens_logs(lens_id, request=request, request_options=request_options)
        return _response.data


class AsyncLensesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLensesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLensesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLensesClient
        """
        return self._raw_client

    async def update_lens_settings(
        self, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateLensSettingsResponse:
        """
        Parameters
        ----------
        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateLensSettingsResponse
            Updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.lenses.update_lens_settings(
                request={"0": "focus", "1": "tilt"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_lens_settings(request=request, request_options=request_options)
        return _response.data

    async def append_lens_logs(
        self,
        lens_id: int,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AppendLensLogsResponse:
        """
        Parameters
        ----------
        lens_id : int

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AppendLensLogsResponse
            Appended

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.lenses.append_lens_logs(
                lens_id=1000000,
                request={
                    "0": {"note": "wiped", "keeper": "Tamsin"},
                    "1": {"note": "realigned", "keeper": "Jory"},
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.append_lens_logs(lens_id, request=request, request_options=request_options)
        return _response.data
