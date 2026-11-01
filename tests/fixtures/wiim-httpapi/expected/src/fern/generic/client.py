

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawGenericClient, RawGenericClient


class GenericClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGenericClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGenericClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGenericClient
        """
        return self._raw_client

    def command(self, command: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Generic command to the device. All calls will follow the format /httpapi.asp?command={command}.


        The actual command is passed as a path parameter. With this, you can test out any command that is not explicitly defined in this API.

        The response could be a simple 'OK' or an object with data. The actual response will depend on the command sent. If you get an 'unknown command' response, the command is not supported by the device.


        Examples:
        -  'getStatusEx' will do an /httpapi.asp?command=getStatusEx
        -  'setPlayerCmd:pause' will do an /httpapi.asp?command=setPlayerCmd:pause
        -  'setPlayerCmd:resume' will do an /httpapi.asp?command=setPlayerCmd:resume

        Parameters
        ----------
        command : str
            The actual command to send to the device. Note that the command is case-sensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.generic.command(
            command="command",
        )
        """
        _response = self._raw_client.command(command, request_options=request_options)
        return _response.data


class AsyncGenericClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGenericClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGenericClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGenericClient
        """
        return self._raw_client

    async def command(self, command: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Generic command to the device. All calls will follow the format /httpapi.asp?command={command}.


        The actual command is passed as a path parameter. With this, you can test out any command that is not explicitly defined in this API.

        The response could be a simple 'OK' or an object with data. The actual response will depend on the command sent. If you get an 'unknown command' response, the command is not supported by the device.


        Examples:
        -  'getStatusEx' will do an /httpapi.asp?command=getStatusEx
        -  'setPlayerCmd:pause' will do an /httpapi.asp?command=setPlayerCmd:pause
        -  'setPlayerCmd:resume' will do an /httpapi.asp?command=setPlayerCmd:resume

        Parameters
        ----------
        command : str
            The actual command to send to the device. Note that the command is case-sensitive.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.generic.command(
                command="command",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.command(command, request_options=request_options)
        return _response.data
