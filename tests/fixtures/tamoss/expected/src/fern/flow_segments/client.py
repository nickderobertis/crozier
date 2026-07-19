

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.deletion_request import DeletionRequest
from ..types.flow_segment import FlowSegment
from ..types.flow_segment_bulk_failure import FlowSegmentBulkFailure
from ..types.timerange import Timerange
from ..types.url_label_list import UrlLabelList
from ..types.uuid_ import Uuid
from ..types.uuid_list import UuidList
from .raw_client import AsyncRawFlowSegmentsClient, RawFlowSegmentsClient
from .types.post_flows_flow_id_segments_request_body import PostFlowsFlowIdSegmentsRequestBody


OMIT = typing.cast(typing.Any, ...)


class FlowSegmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFlowSegmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFlowSegmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFlowSegmentsClient
        """
        return self._raw_client

    def get_flows_flow_id_segments(
        self,
        flow_id: Uuid,
        *,
        object_id: typing.Optional[str] = None,
        timerange: typing.Optional[Timerange] = None,
        reverse_order: typing.Optional[bool] = None,
        verbose_storage: typing.Optional[bool] = None,
        accept_get_urls: typing.Optional[UrlLabelList] = None,
        accept_storage_ids: typing.Optional[UuidList] = None,
        presigned: typing.Optional[bool] = None,
        include_object_timerange: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FlowSegment]:
        """
        Returns the Flow Segments.

        The Flow Segment provides information about the Media Object.
        The Storage Backend type, which is indicated in the [/service/storage-backends](#/operations/GET_storage-backends) resource, determines the information that is included in the response to allow the Flow Segment's Media Object to be downloaded by the client.
        The examples provided here are for the "http_object_store" Storage Backend type which MUST include a `get_urls` property that contains the HTTP URLs for downloading the Media Object - service implementations should generate this internally.

        The Flow Segment may include timing adjustment information that the client needs to apply when extracting the samples from the Media Object.
        The timestamp of a sample on the Flow Segment's timeline (`segment_ts`) is the timestamp of that sample embedded in or derived from the internal timing of the Media Object (`media_object_ts`) adjusted by `ts_offset`: `segment_ts = media_object_ts + ts_offset`.

        It may also use a subset of the samples in the Media Object, and if the `include_object_timerange=true` parameter is set, the object's timerange will also be returned to aid identifying which samples to skip.

        Clients should use the pagination options to limit the results to a timerange and/or count.
        Service implementations may also limit the results returned.
        This will be signalled via the paging headers in the response.
        The list of Flow Segments can be empty.
        A request for Segments from a non-existent Flow will return an empty list, not a 404.

        Note that for codecs with temporal re-ordering, the timerange represents the _presentation_ timeline, and clients may need to check the `key_frame_count` property and/or read backwards from the start of the requested timerange to retrieve enough reference material to start decoding.

        When making requests to the provided `get_urls`, clients should include credentials if the provided URL is on the same origin as the API itself, akin to the `same-origin` mode in the [WhatWG Fetch Standard](https://fetch.spec.whatwg.org/#concept-request-credentials-mode).

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        object_id : typing.Optional[str]
            Filter on Object identifier.

        timerange : typing.Optional[Timerange]
            Return only the results that partially or wholly overlap the timerange specified.

        reverse_order : typing.Optional[bool]
            Return Segments in reverse time order.

        verbose_storage : typing.Optional[bool]
            Include storage metadata in `get_urls` in the response.
            When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.

        accept_get_urls : typing.Optional[UrlLabelList]
            A comma separated list of labels of Flow Segment `get_urls` to include in the response.
            Omitting `accept_get_urls` will result in no filtering of `get_urls`.
            An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
            Flow Segment `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
            Without `get_urls`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs for example.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        accept_storage_ids : typing.Optional[UuidList]
            A comma separated list of `storage_id`s of Flow Segment `get_urls` to include in the response.
            Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
            Flow Segment `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
            A full list of available `storage_id`s may be found at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        presigned : typing.Optional[bool]
            If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls`.
            If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
            If omitted, both presigned and non-presigned URLs will be returned.
            If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        include_object_timerange : typing.Optional[bool]
            If set to `true`, the underlying object's timerange should appear in the response (if it differs from the Flow Segment's `timerange`).
            Assume `false` if omitted.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FlowSegment]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flow_segments.get_flows_flow_id_segments(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.get_flows_flow_id_segments(
            flow_id,
            object_id=object_id,
            timerange=timerange,
            reverse_order=reverse_order,
            verbose_storage=verbose_storage,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            include_object_timerange=include_object_timerange,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    def post_flows_flow_id_segments(
        self,
        flow_id: Uuid,
        *,
        request: PostFlowsFlowIdSegmentsRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FlowSegmentBulkFailure:
        """
        Register either a single new Flow Segment or an array of Segments, attaching the Object id given to a point in the Flow timeline.

        The Segment may use a newly-written Media Object, or re-use an existing Media Object from another Flow.

        For newly-written Media Objects, the client is responsible for ensuring that the Segment written to the TAMS service instance obeys the following restrictions:
          - All samples in the Object SHOULD be used by the Segment.
          - If the Segment does not use all samples in the Object, `object_timerange` MUST be set to the timerange of media in the object, on the Media Object's timeline
          - The timestamps of each sample in the Media Object MUST equal its position on the Flow timeline, OR `ts_offset` MUST be set such that `media_object_ts + ts_offset = segment_ts`
          - The timerange of the Segment MUST NOT overlap any other Segment in the same Flow. The behaviour is undefined if there is an overlap with existing Segments and a service may return a 400 error response.

        A service instance SHOULD reject registrations of Flow Segments with a 400 error response if it references a newly created Media Object in the local TAMS storage that was not intended to be used for the Flow.
        A service instance SHOULD accept Flow Segments that reference an existing Media Object in the local TAMS storage that was originally created for another Flow.

        A service instance MAY support Media Objects that are held in external storage in another TAMS or other media storage system.
        The Flow Segment may in that case require the `get_urls` property to provide the information needed by clients to access the Media Object.

        The list of instances of an object (and associated `get_urls` entries) can be modified via the [`/objects`](#/operations/GET_objects) endpoints, which provides a mechanism to register new instances of an object.

        Clients MAY modify Flow Segments, but this should only be done in exceptional circumstances to correct metadata such as `key_frame_count`, as such operations will likely break the idempotency of Segments.
        If a client needs to modify a Flow Segment, then the client SHOULD first delete the existing Segment and then write a new one.
        The behaviour is undefined if the Segment exists and the service may return a 400 error response.

        For successful creation of all Segments in the request a 201 response should be provided.
        If an error is detected when processing a list of Segments then processing should continue to try and process the remaining Segments.
        A 200 response should be returned listing the failed Segments.

        Clients are expected to decide how to break content into Media Objects, however those Objects SHOULD be large enough to avoid excessive round trip overheads in the underlying store (_e.g._ of the order of several megabytes) and where codecs with temporal re-ordering are used, Object SHOULD contain complete GOPs or decodable units.

        For Media Objects that have been re-used from other Flows, the `timerange` MAY specify only part of the duration of the object:
          - The `timerange` field indicates the new Segment's position in the Flow
          - The timerange of the Segment MUST NOT overlap any other Segment in the same Flow.
          - The Flow Segment's `timerange` start and end, once offset by `ts_offset`, MUST be contained entirely within the Media Object's `timerange`

        When re-using Media Objects, requests which change object properties (e.g. `key_frame_count` or `object_timerange`) SHOULD be rejected.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : PostFlowsFlowIdSegmentsRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FlowSegmentBulkFailure
            Partial success creating Segments returning list of failed Segments.

        Examples
        --------
        from fern import FernApi, FlowSegmentPost

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flow_segments.post_flows_flow_id_segments(
            flow_id="flowId",
            request=[
                FlowSegmentPost(
                    object_id="object_id",
                    timerange="timerange",
                )
            ],
        )
        """
        _response = self._raw_client.post_flows_flow_id_segments(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    def delete_flows_flow_id_segments(
        self,
        flow_id: Uuid,
        *,
        timerange: typing.Optional[Timerange] = None,
        object_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[DeletionRequest]:
        """
        Deletes the Flow Segments. If the deletion takes too long then this request will return 202 Accepted and the `Location` header will point to a Flow Delete Request to monitor deletion progress

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        timerange : typing.Optional[Timerange]
            Only delete Flow Segments that are completely covered by the given timerange.

        object_id : typing.Optional[str]
            Filter on Object identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DeletionRequest]
            This request has taken longer than the configured timeout, and will continue asynchronously

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flow_segments.delete_flows_flow_id_segments(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.delete_flows_flow_id_segments(
            flow_id, timerange=timerange, object_id=object_id, request_options=request_options
        )
        return _response.data

    def head_flows_flow_id_segments(
        self,
        flow_id: Uuid,
        *,
        object_id: typing.Optional[str] = None,
        timerange: typing.Optional[Timerange] = None,
        reverse_order: typing.Optional[bool] = None,
        verbose_storage: typing.Optional[bool] = None,
        accept_get_urls: typing.Optional[UrlLabelList] = None,
        accept_storage_ids: typing.Optional[UuidList] = None,
        presigned: typing.Optional[bool] = None,
        include_object_timerange: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Flow Segments path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        object_id : typing.Optional[str]
            Filter on Object identifier.

        timerange : typing.Optional[Timerange]
            Return only the results that partially or wholly overlap the timerange specified.

        reverse_order : typing.Optional[bool]
            Return Segments in reverse time order.

        verbose_storage : typing.Optional[bool]
            Include storage metadata in `get_urls` in the response.
            When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.

        accept_get_urls : typing.Optional[UrlLabelList]
            A comma separated list of labels of Flow Segment `get_urls` to include in the response.
            Omitting `accept_get_urls` will result in no filtering of `get_urls`.
            An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
            Flow Segment `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
            Without `get_urls`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs for example.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        accept_storage_ids : typing.Optional[UuidList]
            A comma separated list of `storage_id`s of Flow Segment `get_urls` to include in the response.
            Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
            Flow Segment `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
            A full list of available `storage_id`s may be found at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        presigned : typing.Optional[bool]
            If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls` in the response.
            If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
            If omitted, both presigned and non-presigned URLs will be returned.
            If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        include_object_timerange : typing.Optional[bool]
            If set to `true`, the underlying object's timerange should appear in the response (if it differs from the segment timerange).
            Assume `false` if omitted.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.flow_segments.head_flows_flow_id_segments(
            flow_id="flowId",
        )
        """
        _response = self._raw_client.head_flows_flow_id_segments(
            flow_id,
            object_id=object_id,
            timerange=timerange,
            reverse_order=reverse_order,
            verbose_storage=verbose_storage,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            include_object_timerange=include_object_timerange,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.headers


class AsyncFlowSegmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFlowSegmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFlowSegmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFlowSegmentsClient
        """
        return self._raw_client

    async def get_flows_flow_id_segments(
        self,
        flow_id: Uuid,
        *,
        object_id: typing.Optional[str] = None,
        timerange: typing.Optional[Timerange] = None,
        reverse_order: typing.Optional[bool] = None,
        verbose_storage: typing.Optional[bool] = None,
        accept_get_urls: typing.Optional[UrlLabelList] = None,
        accept_storage_ids: typing.Optional[UuidList] = None,
        presigned: typing.Optional[bool] = None,
        include_object_timerange: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[FlowSegment]:
        """
        Returns the Flow Segments.

        The Flow Segment provides information about the Media Object.
        The Storage Backend type, which is indicated in the [/service/storage-backends](#/operations/GET_storage-backends) resource, determines the information that is included in the response to allow the Flow Segment's Media Object to be downloaded by the client.
        The examples provided here are for the "http_object_store" Storage Backend type which MUST include a `get_urls` property that contains the HTTP URLs for downloading the Media Object - service implementations should generate this internally.

        The Flow Segment may include timing adjustment information that the client needs to apply when extracting the samples from the Media Object.
        The timestamp of a sample on the Flow Segment's timeline (`segment_ts`) is the timestamp of that sample embedded in or derived from the internal timing of the Media Object (`media_object_ts`) adjusted by `ts_offset`: `segment_ts = media_object_ts + ts_offset`.

        It may also use a subset of the samples in the Media Object, and if the `include_object_timerange=true` parameter is set, the object's timerange will also be returned to aid identifying which samples to skip.

        Clients should use the pagination options to limit the results to a timerange and/or count.
        Service implementations may also limit the results returned.
        This will be signalled via the paging headers in the response.
        The list of Flow Segments can be empty.
        A request for Segments from a non-existent Flow will return an empty list, not a 404.

        Note that for codecs with temporal re-ordering, the timerange represents the _presentation_ timeline, and clients may need to check the `key_frame_count` property and/or read backwards from the start of the requested timerange to retrieve enough reference material to start decoding.

        When making requests to the provided `get_urls`, clients should include credentials if the provided URL is on the same origin as the API itself, akin to the `same-origin` mode in the [WhatWG Fetch Standard](https://fetch.spec.whatwg.org/#concept-request-credentials-mode).

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        object_id : typing.Optional[str]
            Filter on Object identifier.

        timerange : typing.Optional[Timerange]
            Return only the results that partially or wholly overlap the timerange specified.

        reverse_order : typing.Optional[bool]
            Return Segments in reverse time order.

        verbose_storage : typing.Optional[bool]
            Include storage metadata in `get_urls` in the response.
            When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.

        accept_get_urls : typing.Optional[UrlLabelList]
            A comma separated list of labels of Flow Segment `get_urls` to include in the response.
            Omitting `accept_get_urls` will result in no filtering of `get_urls`.
            An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
            Flow Segment `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
            Without `get_urls`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs for example.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        accept_storage_ids : typing.Optional[UuidList]
            A comma separated list of `storage_id`s of Flow Segment `get_urls` to include in the response.
            Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
            Flow Segment `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
            A full list of available `storage_id`s may be found at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        presigned : typing.Optional[bool]
            If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls`.
            If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
            If omitted, both presigned and non-presigned URLs will be returned.
            If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        include_object_timerange : typing.Optional[bool]
            If set to `true`, the underlying object's timerange should appear in the response (if it differs from the Flow Segment's `timerange`).
            Assume `false` if omitted.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FlowSegment]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flow_segments.get_flows_flow_id_segments(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_flows_flow_id_segments(
            flow_id,
            object_id=object_id,
            timerange=timerange,
            reverse_order=reverse_order,
            verbose_storage=verbose_storage,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            include_object_timerange=include_object_timerange,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.data

    async def post_flows_flow_id_segments(
        self,
        flow_id: Uuid,
        *,
        request: PostFlowsFlowIdSegmentsRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FlowSegmentBulkFailure:
        """
        Register either a single new Flow Segment or an array of Segments, attaching the Object id given to a point in the Flow timeline.

        The Segment may use a newly-written Media Object, or re-use an existing Media Object from another Flow.

        For newly-written Media Objects, the client is responsible for ensuring that the Segment written to the TAMS service instance obeys the following restrictions:
          - All samples in the Object SHOULD be used by the Segment.
          - If the Segment does not use all samples in the Object, `object_timerange` MUST be set to the timerange of media in the object, on the Media Object's timeline
          - The timestamps of each sample in the Media Object MUST equal its position on the Flow timeline, OR `ts_offset` MUST be set such that `media_object_ts + ts_offset = segment_ts`
          - The timerange of the Segment MUST NOT overlap any other Segment in the same Flow. The behaviour is undefined if there is an overlap with existing Segments and a service may return a 400 error response.

        A service instance SHOULD reject registrations of Flow Segments with a 400 error response if it references a newly created Media Object in the local TAMS storage that was not intended to be used for the Flow.
        A service instance SHOULD accept Flow Segments that reference an existing Media Object in the local TAMS storage that was originally created for another Flow.

        A service instance MAY support Media Objects that are held in external storage in another TAMS or other media storage system.
        The Flow Segment may in that case require the `get_urls` property to provide the information needed by clients to access the Media Object.

        The list of instances of an object (and associated `get_urls` entries) can be modified via the [`/objects`](#/operations/GET_objects) endpoints, which provides a mechanism to register new instances of an object.

        Clients MAY modify Flow Segments, but this should only be done in exceptional circumstances to correct metadata such as `key_frame_count`, as such operations will likely break the idempotency of Segments.
        If a client needs to modify a Flow Segment, then the client SHOULD first delete the existing Segment and then write a new one.
        The behaviour is undefined if the Segment exists and the service may return a 400 error response.

        For successful creation of all Segments in the request a 201 response should be provided.
        If an error is detected when processing a list of Segments then processing should continue to try and process the remaining Segments.
        A 200 response should be returned listing the failed Segments.

        Clients are expected to decide how to break content into Media Objects, however those Objects SHOULD be large enough to avoid excessive round trip overheads in the underlying store (_e.g._ of the order of several megabytes) and where codecs with temporal re-ordering are used, Object SHOULD contain complete GOPs or decodable units.

        For Media Objects that have been re-used from other Flows, the `timerange` MAY specify only part of the duration of the object:
          - The `timerange` field indicates the new Segment's position in the Flow
          - The timerange of the Segment MUST NOT overlap any other Segment in the same Flow.
          - The Flow Segment's `timerange` start and end, once offset by `ts_offset`, MUST be contained entirely within the Media Object's `timerange`

        When re-using Media Objects, requests which change object properties (e.g. `key_frame_count` or `object_timerange`) SHOULD be rejected.

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        request : PostFlowsFlowIdSegmentsRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FlowSegmentBulkFailure
            Partial success creating Segments returning list of failed Segments.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FlowSegmentPost

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flow_segments.post_flows_flow_id_segments(
                flow_id="flowId",
                request=[
                    FlowSegmentPost(
                        object_id="object_id",
                        timerange="timerange",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_flows_flow_id_segments(
            flow_id, request=request, request_options=request_options
        )
        return _response.data

    async def delete_flows_flow_id_segments(
        self,
        flow_id: Uuid,
        *,
        timerange: typing.Optional[Timerange] = None,
        object_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Optional[DeletionRequest]:
        """
        Deletes the Flow Segments. If the deletion takes too long then this request will return 202 Accepted and the `Location` header will point to a Flow Delete Request to monitor deletion progress

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        timerange : typing.Optional[Timerange]
            Only delete Flow Segments that are completely covered by the given timerange.

        object_id : typing.Optional[str]
            Filter on Object identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[DeletionRequest]
            This request has taken longer than the configured timeout, and will continue asynchronously

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flow_segments.delete_flows_flow_id_segments(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_flows_flow_id_segments(
            flow_id, timerange=timerange, object_id=object_id, request_options=request_options
        )
        return _response.data

    async def head_flows_flow_id_segments(
        self,
        flow_id: Uuid,
        *,
        object_id: typing.Optional[str] = None,
        timerange: typing.Optional[Timerange] = None,
        reverse_order: typing.Optional[bool] = None,
        verbose_storage: typing.Optional[bool] = None,
        accept_get_urls: typing.Optional[UrlLabelList] = None,
        accept_storage_ids: typing.Optional[UuidList] = None,
        presigned: typing.Optional[bool] = None,
        include_object_timerange: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return Flow Segments path headers

        Parameters
        ----------
        flow_id : Uuid
            The Flow identifier.

        object_id : typing.Optional[str]
            Filter on Object identifier.

        timerange : typing.Optional[Timerange]
            Return only the results that partially or wholly overlap the timerange specified.

        reverse_order : typing.Optional[bool]
            Return Segments in reverse time order.

        verbose_storage : typing.Optional[bool]
            Include storage metadata in `get_urls` in the response.
            When `verbose_storage` is `false` only `url`, `presigned`, and `label` will be included in `get_urls`.

        accept_get_urls : typing.Optional[UrlLabelList]
            A comma separated list of labels of Flow Segment `get_urls` to include in the response.
            Omitting `accept_get_urls` will result in no filtering of `get_urls`.
            An empty `accept_get_urls` results in an empty or no `get_urls` in the response.
            Flow Segment `get_urls` with no label will only be returned if `accept_get_urls` is omitted.
            Without `get_urls`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs for example.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        accept_storage_ids : typing.Optional[UuidList]
            A comma separated list of `storage_id`s of Flow Segment `get_urls` to include in the response.
            Omitting `accept_storage_ids`, or providing an empty `accept_storage_ids` will result in no filtering of `get_urls`.
            Flow Segment `get_urls` with no storage ID will only be returned if `accept_storage_ids` is omitted or empty.
            A full list of available `storage_id`s may be found at the [/service/storage-backends](#/operations/GET_storage-backends) endpoint.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        presigned : typing.Optional[bool]
            If set to `true`, only presigned URLs (i.e. those whos `presigned` property is `true`) will be returned in `get_urls` in the response.
            If set to `false`, only non-presigned URLs (i.e. those whos `presigned` property is `false`) will be returned in `get_urls`.
            If omitted, both presigned and non-presigned URLs will be returned.
            If `presigned` is set to `false`, the response from the service could be substantially faster if it is not required to generate a large number of pre-signed URLs.
            Where multiple filter query parameters are provided, the returned `get_urls` will match all filters.

        include_object_timerange : typing.Optional[bool]
            If set to `true`, the underlying object's timerange should appear in the response (if it differs from the segment timerange).
            Assume `false` if omitted.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.flow_segments.head_flows_flow_id_segments(
                flow_id="flowId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_flows_flow_id_segments(
            flow_id,
            object_id=object_id,
            timerange=timerange,
            reverse_order=reverse_order,
            verbose_storage=verbose_storage,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            include_object_timerange=include_object_timerange,
            page=page,
            limit=limit,
            request_options=request_options,
        )
        return _response.headers
