

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.service_descriptor_list import ServiceDescriptorList
from ..types.string_list import StringList
from .raw_client import AsyncRawLinesClient, RawLinesClient


class LinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLinesClient
        """
        return self._raw_client

    def otoroshi_controllers_adminapi_services_controller_services_for_a_line(
        self, line: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceDescriptorList:
        """
        Parameters
        ----------
        line : str
            The line param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceDescriptorList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.lines.otoroshi_controllers_adminapi_services_controller_services_for_a_line(
            line="line",
        )
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_services_for_a_line(
            line, request_options=request_options
        )
        return _response.data

    def otoroshi_controllers_adminapi_services_controller_all_lines(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StringList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StringList
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.lines.otoroshi_controllers_adminapi_services_controller_all_lines()
        """
        _response = self._raw_client.otoroshi_controllers_adminapi_services_controller_all_lines(
            request_options=request_options
        )
        return _response.data


class AsyncLinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLinesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLinesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLinesClient
        """
        return self._raw_client

    async def otoroshi_controllers_adminapi_services_controller_services_for_a_line(
        self, line: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ServiceDescriptorList:
        """
        Parameters
        ----------
        line : str
            The line param of the target entity

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ServiceDescriptorList
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
            await client.lines.otoroshi_controllers_adminapi_services_controller_services_for_a_line(
                line="line",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_services_for_a_line(
            line, request_options=request_options
        )
        return _response.data

    async def otoroshi_controllers_adminapi_services_controller_all_lines(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StringList:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StringList
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
            await client.lines.otoroshi_controllers_adminapi_services_controller_all_lines()


        asyncio.run(main())
        """
        _response = await self._raw_client.otoroshi_controllers_adminapi_services_controller_all_lines(
            request_options=request_options
        )
        return _response.data
