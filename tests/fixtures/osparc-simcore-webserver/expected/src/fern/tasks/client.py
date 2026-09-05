

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_dict_uuid_activity import EnvelopeDictUuidActivity
from .raw_client import AsyncRawTasksClient, RawTasksClient


class TasksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTasksClient
        """
        return self._raw_client

    def get_activity_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictUuidActivity:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictUuidActivity
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.tasks.get_activity_status()
        """
        _response = self._raw_client.get_activity_status(request_options=request_options)
        return _response.data


class AsyncTasksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTasksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTasksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTasksClient
        """
        return self._raw_client

    async def get_activity_status(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictUuidActivity:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictUuidActivity
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.tasks.get_activity_status()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_activity_status(request_options=request_options)
        return _response.data
