

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.environment import Environment
from ..types.service import Service
from .raw_client import AsyncRawEnvironmentsClient, RawEnvironmentsClient


class EnvironmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnvironmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnvironmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnvironmentsClient
        """
        return self._raw_client

    def all_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> Environment:
        """
        Get all environments provided by the current Otoroshi instance

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.environments.all_lines()
        """
        _response = self._raw_client.all_lines(request_options=request_options)
        return _response.data

    def services_for_a_line(
        self, line: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Service]:
        """
        Get all services for an environment provided by the current Otoroshi instance

        Parameters
        ----------
        line : str
            The environment where to find services

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Service]
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.environments.services_for_a_line(
            line="line",
        )
        """
        _response = self._raw_client.services_for_a_line(line, request_options=request_options)
        return _response.data


class AsyncEnvironmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnvironmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnvironmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnvironmentsClient
        """
        return self._raw_client

    async def all_lines(self, *, request_options: typing.Optional[RequestOptions] = None) -> Environment:
        """
        Get all environments provided by the current Otoroshi instance

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Environment
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.environments.all_lines()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_lines(request_options=request_options)
        return _response.data

    async def services_for_a_line(
        self, line: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Service]:
        """
        Get all services for an environment provided by the current Otoroshi instance

        Parameters
        ----------
        line : str
            The environment where to find services

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Service]
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.environments.services_for_a_line(
                line="line",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.services_for_a_line(line, request_options=request_options)
        return _response.data
