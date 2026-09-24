

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.robot_state_response import RobotStateResponse
from .raw_client import AsyncRawRobotStateClient, RawRobotStateClient


class RobotStateClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRobotStateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRobotStateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRobotStateClient
        """
        return self._raw_client

    def get_robot_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> RobotStateResponse:
        """
        Get the current state of the robot

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RobotStateResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.robot_state.get_robot_state()
        """
        _response = self._raw_client.get_robot_state(request_options=request_options)
        return _response.data


class AsyncRobotStateClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRobotStateClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRobotStateClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRobotStateClient
        """
        return self._raw_client

    async def get_robot_state(self, *, request_options: typing.Optional[RequestOptions] = None) -> RobotStateResponse:
        """
        Get the current state of the robot

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RobotStateResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.robot_state.get_robot_state()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_robot_state(request_options=request_options)
        return _response.data
