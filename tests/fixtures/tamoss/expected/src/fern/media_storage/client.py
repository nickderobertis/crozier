

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.flow_storage import FlowStorage
from ..types.uuid_ import Uuid
from .raw_client import AsyncRawMediaStorageClient, RawMediaStorageClient


OMIT = typing.cast(typing.Any, ...)


class MediaStorageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMediaStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMediaStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMediaStorageClient
        """
        return self._raw_client

    def post_flows_flow_id_storage(
        self,
        flow_id: Uuid,
        *,
        limit: typing.Optional[int] = OMIT,
        object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        storage_id: typing.Optional[Uuid] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FlowStorage:
        """
        Allocate initial storage locations for writing Media Objects.

        The Storage Backend type, which is indicated in the [/service](#/operations/GET_service) resource, determines the information provided in the response.
        The examples and description below are for the "http_object_store" Storage Backend type.
        This Storage Backend type provides HTTP URLs for uploading and downloading Media Objects in buckets.

        The response will include a PUT URL that a client uses to upload the Media Object.
        The client is expected to register the Flow Segment using the [/flows/{flowId}/segments](#/operations/POST_flows-flowId-segments) endpoint once the upload is complete.

        Clients MAY request Objects in batches to reduce the number of HTTP requests made to the Service.
        Clients are not expected to use all of the Objects they requested.
        Objects will likely go unused in cases such as shutdown of ingesting clients, the end of ingested live streams, and unexpected network congestion.
        Clients SHOULD, however, adapt the number of Objects they request such that they may reasonably expect to use them before the timeout advertised in [`min_object_timeout` at the `/service`](#/operations/GET_service) endpoint, which is subject to a specified minimum (see service endpoint schema).

        Service implementations need to handle situations where Objects are not used, and where content was uploaded but no Flow Segment was registered successfully.
        In these circumstances, Services should garbage collect Objects after the timeout advertised in [`min_object_timeout` at the `/service`](#/operations/GET_service) endpoint.

        When making requests to the provided `put_url`, clients should include credentials if the provided URL is on the same origin as the API itself, akin to the `same-origin` mode in the [WhatWG Fetch Standard](https://fetch.spec.whatwg.org/#concept-request-credentials-mode).

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        limit : typing.Optional[int]
            Limit the number of Media Objects in each response page. Service implementations may specify their own default and maximum for the limit

        object_ids : typing.Optional[typing.Sequence[str]]
            Array of object_ids to use. The supplied object_ids must be new and not already in use in this TAMS service instance. A 400 response will be returned if any supplied object_id already exists.

        storage_id : typing.Optional[Uuid]
            The Storage Backend to allocate storage in. A Storage Backend identifier as advertised at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint. If not set the default, as advertised at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint, will be used if available. An invalid Storage Backend identifier will result in a 400 error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FlowStorage
            Storage locations for writing Media Objects.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.media_storage.post_flows_flow_id_storage(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.post_flows_flow_id_storage(
            flow_id, limit=limit, object_ids=object_ids, storage_id=storage_id, request_options=request_options
        )
        return _response.data


class AsyncMediaStorageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMediaStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMediaStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMediaStorageClient
        """
        return self._raw_client

    async def post_flows_flow_id_storage(
        self,
        flow_id: Uuid,
        *,
        limit: typing.Optional[int] = OMIT,
        object_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        storage_id: typing.Optional[Uuid] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FlowStorage:
        """
        Allocate initial storage locations for writing Media Objects.

        The Storage Backend type, which is indicated in the [/service](#/operations/GET_service) resource, determines the information provided in the response.
        The examples and description below are for the "http_object_store" Storage Backend type.
        This Storage Backend type provides HTTP URLs for uploading and downloading Media Objects in buckets.

        The response will include a PUT URL that a client uses to upload the Media Object.
        The client is expected to register the Flow Segment using the [/flows/{flowId}/segments](#/operations/POST_flows-flowId-segments) endpoint once the upload is complete.

        Clients MAY request Objects in batches to reduce the number of HTTP requests made to the Service.
        Clients are not expected to use all of the Objects they requested.
        Objects will likely go unused in cases such as shutdown of ingesting clients, the end of ingested live streams, and unexpected network congestion.
        Clients SHOULD, however, adapt the number of Objects they request such that they may reasonably expect to use them before the timeout advertised in [`min_object_timeout` at the `/service`](#/operations/GET_service) endpoint, which is subject to a specified minimum (see service endpoint schema).

        Service implementations need to handle situations where Objects are not used, and where content was uploaded but no Flow Segment was registered successfully.
        In these circumstances, Services should garbage collect Objects after the timeout advertised in [`min_object_timeout` at the `/service`](#/operations/GET_service) endpoint.

        When making requests to the provided `put_url`, clients should include credentials if the provided URL is on the same origin as the API itself, akin to the `same-origin` mode in the [WhatWG Fetch Standard](https://fetch.spec.whatwg.org/#concept-request-credentials-mode).

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        limit : typing.Optional[int]
            Limit the number of Media Objects in each response page. Service implementations may specify their own default and maximum for the limit

        object_ids : typing.Optional[typing.Sequence[str]]
            Array of object_ids to use. The supplied object_ids must be new and not already in use in this TAMS service instance. A 400 response will be returned if any supplied object_id already exists.

        storage_id : typing.Optional[Uuid]
            The Storage Backend to allocate storage in. A Storage Backend identifier as advertised at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint. If not set the default, as advertised at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint, will be used if available. An invalid Storage Backend identifier will result in a 400 error.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FlowStorage
            Storage locations for writing Media Objects.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.media_storage.post_flows_flow_id_storage(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_flows_flow_id_storage(
            flow_id, limit=limit, object_ids=object_ids, storage_id=storage_id, request_options=request_options
        )
        return _response.data
