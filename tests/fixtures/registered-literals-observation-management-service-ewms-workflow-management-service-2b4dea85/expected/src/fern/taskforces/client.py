

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.taskforce_object import TaskforceObject
from .raw_client import AsyncRawTaskforcesClient, RawTaskforcesClient
from .types.post_v1query_taskforces_response import PostV1QueryTaskforcesResponse


OMIT = typing.cast(typing.Any, ...)


class TaskforcesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTaskforcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTaskforcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTaskforcesClient
        """
        return self._raw_client

    def post_v1query_taskforces(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1QueryTaskforcesResponse:
        """
        Queries and returns a list of taskforce objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        query : typing.Dict[str, typing.Any]
            The search criteria (MongoDB-filter syntax)

        projection : typing.Optional[typing.Sequence[str]]
            The fields to include in the response

        after : typing.Optional[str]
            The database '_id' to resume pagination from, taken from a previous response's 'next_after' field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1QueryTaskforcesResponse
            Matching taskforces and pagination metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.taskforces.post_v1query_taskforces(
            query={"key": "value"},
        )
        """
        _response = self._raw_client.post_v1query_taskforces(
            query=query, projection=projection, after=after, request_options=request_options
        )
        return _response.data

    def get_v1taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskforceObject:
        """
        Retrieves the taskforce object that matches the specified taskforce UUID. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskforceObject
            The matching taskforce object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.taskforces.get_v1taskforces_taskforce_uuid(
            taskforce_uuid="taskforce_uuid",
        )
        """
        _response = self._raw_client.get_v1taskforces_taskforce_uuid(taskforce_uuid, request_options=request_options)
        return _response.data


class AsyncTaskforcesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTaskforcesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTaskforcesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTaskforcesClient
        """
        return self._raw_client

    async def post_v1query_taskforces(
        self,
        *,
        query: typing.Dict[str, typing.Any],
        projection: typing.Optional[typing.Sequence[str]] = OMIT,
        after: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostV1QueryTaskforcesResponse:
        """
        Queries and returns a list of taskforce objects based on the provided criteria. See `FindObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#findobject>`_, `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        query : typing.Dict[str, typing.Any]
            The search criteria (MongoDB-filter syntax)

        projection : typing.Optional[typing.Sequence[str]]
            The fields to include in the response

        after : typing.Optional[str]
            The database '_id' to resume pagination from, taken from a previous response's 'next_after' field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostV1QueryTaskforcesResponse
            Matching taskforces and pagination metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.taskforces.post_v1query_taskforces(
                query={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_v1query_taskforces(
            query=query, projection=projection, after=after, request_options=request_options
        )
        return _response.data

    async def get_v1taskforces_taskforce_uuid(
        self, taskforce_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TaskforceObject:
        """
        Retrieves the taskforce object that matches the specified taskforce UUID. See `TaskforceObject <https://observation-management-service.github.io/ewms-docs/apis/_generated/wms-objects.html#taskforceobject>`_.

        Parameters
        ----------
        taskforce_uuid : str
            UUID of the taskforce.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TaskforceObject
            The matching taskforce object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.taskforces.get_v1taskforces_taskforce_uuid(
                taskforce_uuid="taskforce_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_v1taskforces_taskforce_uuid(
            taskforce_uuid, request_options=request_options
        )
        return _response.data
