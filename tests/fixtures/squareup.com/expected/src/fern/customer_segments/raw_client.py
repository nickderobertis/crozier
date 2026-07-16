

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.list_customer_segments_response import ListCustomerSegmentsResponse
from ..types.retrieve_customer_segment_response import RetrieveCustomerSegmentResponse


class RawCustomerSegmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_customer_segments(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCustomerSegmentsResponse]:
        """
        Retrieves the list of customer segments of a business.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by previous calls to `ListCustomerSegments`.
            This cursor is used to retrieve the next set of query results.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than 1 or greater than 50. The default value is 50.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCustomerSegmentsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/customers/segments",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCustomerSegmentsResponse,
                    parse_obj_as(
                        type_=ListCustomerSegmentsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_customer_segment(
        self, segment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveCustomerSegmentResponse]:
        """
        Retrieves a specific customer segment as identified by the `segment_id` value.

        Parameters
        ----------
        segment_id : str
            The Square-issued ID of the customer segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveCustomerSegmentResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/customers/segments/{jsonable_encoder(segment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveCustomerSegmentResponse,
                    parse_obj_as(
                        type_=RetrieveCustomerSegmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCustomerSegmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_customer_segments(
        self,
        *,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCustomerSegmentsResponse]:
        """
        Retrieves the list of customer segments of a business.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by previous calls to `ListCustomerSegments`.
            This cursor is used to retrieve the next set of query results.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        limit : typing.Optional[int]
            The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.
            The limit is ignored if it is less than 1 or greater than 50. The default value is 50.

            For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCustomerSegmentsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/customers/segments",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCustomerSegmentsResponse,
                    parse_obj_as(
                        type_=ListCustomerSegmentsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_customer_segment(
        self, segment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveCustomerSegmentResponse]:
        """
        Retrieves a specific customer segment as identified by the `segment_id` value.

        Parameters
        ----------
        segment_id : str
            The Square-issued ID of the customer segment.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveCustomerSegmentResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/customers/segments/{jsonable_encoder(segment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveCustomerSegmentResponse,
                    parse_obj_as(
                        type_=RetrieveCustomerSegmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
