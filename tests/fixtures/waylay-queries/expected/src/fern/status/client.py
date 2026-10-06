

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawStatusClient, RawStatusClient


class StatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStatusClient
        """
        return self._raw_client

    def get_version_and_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Get the version and health status for waylay-query.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.status.get_version_and_health()
        """
        _response = self._raw_client.get_version_and_health(request_options=request_options)
        return _response.data


class AsyncStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStatusClient
        """
        return self._raw_client

    async def get_version_and_health(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Get the version and health status for waylay-query.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.status.get_version_and_health()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_version_and_health(request_options=request_options)
        return _response.data
