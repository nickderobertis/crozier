

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.collected_data import CollectedData
from .raw_client import AsyncRawHeartBeatClient, RawHeartBeatClient


OMIT = typing.cast(typing.Any, ...)


class HeartBeatClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHeartBeatClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHeartBeatClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHeartBeatClient
        """
        return self._raw_client

    def post_api_v1heart_beat(
        self,
        *,
        agent_version: typing.Optional[str] = OMIT,
        collected_data_list: typing.Optional[typing.Sequence[CollectedData]] = OMIT,
        environment_id: typing.Optional[str] = OMIT,
        resource_id: typing.Optional[str] = OMIT,
        time_stamp: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        agent_version : typing.Optional[str]

        collected_data_list : typing.Optional[typing.Sequence[CollectedData]]

        environment_id : typing.Optional[str]

        resource_id : typing.Optional[str]

        time_stamp : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.heart_beat.post_api_v1heart_beat()
        """
        _response = self._raw_client.post_api_v1heart_beat(
            agent_version=agent_version,
            collected_data_list=collected_data_list,
            environment_id=environment_id,
            resource_id=resource_id,
            time_stamp=time_stamp,
            request_options=request_options,
        )
        return _response.data


class AsyncHeartBeatClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHeartBeatClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHeartBeatClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHeartBeatClient
        """
        return self._raw_client

    async def post_api_v1heart_beat(
        self,
        *,
        agent_version: typing.Optional[str] = OMIT,
        collected_data_list: typing.Optional[typing.Sequence[CollectedData]] = OMIT,
        environment_id: typing.Optional[str] = OMIT,
        resource_id: typing.Optional[str] = OMIT,
        time_stamp: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        agent_version : typing.Optional[str]

        collected_data_list : typing.Optional[typing.Sequence[CollectedData]]

        environment_id : typing.Optional[str]

        resource_id : typing.Optional[str]

        time_stamp : typing.Optional[dt.datetime]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.heart_beat.post_api_v1heart_beat()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1heart_beat(
            agent_version=agent_version,
            collected_data_list=collected_data_list,
            environment_id=environment_id,
            resource_id=resource_id,
            time_stamp=time_stamp,
            request_options=request_options,
        )
        return _response.data
