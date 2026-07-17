

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.cancel_terminal_checkout_response import CancelTerminalCheckoutResponse
from ..types.cancel_terminal_refund_response import CancelTerminalRefundResponse
from ..types.create_terminal_checkout_response import CreateTerminalCheckoutResponse
from ..types.create_terminal_refund_response import CreateTerminalRefundResponse
from ..types.get_terminal_checkout_response import GetTerminalCheckoutResponse
from ..types.get_terminal_refund_response import GetTerminalRefundResponse
from ..types.search_terminal_checkouts_response import SearchTerminalCheckoutsResponse
from ..types.search_terminal_refunds_response import SearchTerminalRefundsResponse
from ..types.terminal_checkout import TerminalCheckout
from ..types.terminal_checkout_query import TerminalCheckoutQuery
from ..types.terminal_refund import TerminalRefund
from ..types.terminal_refund_query import TerminalRefundQuery
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTerminalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_terminal_checkout(
        self,
        *,
        checkout: TerminalCheckout,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTerminalCheckoutResponse]:
        """
        Creates a Terminal checkout request and sends it to the specified device to take a payment
        for the requested amount.

        Parameters
        ----------
        checkout : TerminalCheckout

        idempotency_key : str
            A unique string that identifies this `CreateCheckout` request. Keys can be any valid string but
            must be unique for every `CreateCheckout` request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTerminalCheckoutResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/terminals/checkouts",
            method="POST",
            json={
                "checkout": convert_and_respect_annotation_metadata(
                    object_=checkout, annotation=TerminalCheckout, direction="write"
                ),
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTerminalCheckoutResponse,
                    parse_obj_as(
                        type_=CreateTerminalCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_terminal_checkouts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[TerminalCheckoutQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchTerminalCheckoutsResponse]:
        """
        Retrieves a filtered list of Terminal checkout requests created by the account making the request.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        limit : typing.Optional[int]
            Limits the number of results returned for a single request.

        query : typing.Optional[TerminalCheckoutQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchTerminalCheckoutsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/terminals/checkouts/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=TerminalCheckoutQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchTerminalCheckoutsResponse,
                    parse_obj_as(
                        type_=SearchTerminalCheckoutsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_terminal_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTerminalCheckoutResponse]:
        """
        Retrieves a Terminal checkout request by `checkout_id`.

        Parameters
        ----------
        checkout_id : str
            The unique ID for the desired `TerminalCheckout`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTerminalCheckoutResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/terminals/checkouts/{encode_path_param(checkout_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTerminalCheckoutResponse,
                    parse_obj_as(
                        type_=GetTerminalCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_terminal_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelTerminalCheckoutResponse]:
        """
        Cancels a Terminal checkout request if the status of the request permits it.

        Parameters
        ----------
        checkout_id : str
            The unique ID for the desired `TerminalCheckout`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CancelTerminalCheckoutResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/terminals/checkouts/{encode_path_param(checkout_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelTerminalCheckoutResponse,
                    parse_obj_as(
                        type_=CancelTerminalCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_terminal_refund(
        self,
        *,
        idempotency_key: str,
        refund: typing.Optional[TerminalRefund] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateTerminalRefundResponse]:
        """
        Creates a request to refund an Interac payment completed on a Square Terminal.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateRefund` request. Keys can be any valid string but
            must be unique for every `CreateRefund` request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        refund : typing.Optional[TerminalRefund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateTerminalRefundResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/terminals/refunds",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "refund": convert_and_respect_annotation_metadata(
                    object_=refund, annotation=TerminalRefund, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTerminalRefundResponse,
                    parse_obj_as(
                        type_=CreateTerminalRefundResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_terminal_refunds(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[TerminalRefundQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchTerminalRefundsResponse]:
        """
        Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.

        limit : typing.Optional[int]
            Limits the number of results returned for a single request.

        query : typing.Optional[TerminalRefundQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchTerminalRefundsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/terminals/refunds/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=TerminalRefundQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchTerminalRefundsResponse,
                    parse_obj_as(
                        type_=SearchTerminalRefundsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_terminal_refund(
        self, terminal_refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTerminalRefundResponse]:
        """
        Retrieves an Interac Terminal refund object by ID.

        Parameters
        ----------
        terminal_refund_id : str
            The unique ID for the desired `TerminalRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTerminalRefundResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/terminals/refunds/{encode_path_param(terminal_refund_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTerminalRefundResponse,
                    parse_obj_as(
                        type_=GetTerminalRefundResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_terminal_refund(
        self, terminal_refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CancelTerminalRefundResponse]:
        """
        Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

        Parameters
        ----------
        terminal_refund_id : str
            The unique ID for the desired `TerminalRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CancelTerminalRefundResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/terminals/refunds/{encode_path_param(terminal_refund_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelTerminalRefundResponse,
                    parse_obj_as(
                        type_=CancelTerminalRefundResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTerminalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_terminal_checkout(
        self,
        *,
        checkout: TerminalCheckout,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTerminalCheckoutResponse]:
        """
        Creates a Terminal checkout request and sends it to the specified device to take a payment
        for the requested amount.

        Parameters
        ----------
        checkout : TerminalCheckout

        idempotency_key : str
            A unique string that identifies this `CreateCheckout` request. Keys can be any valid string but
            must be unique for every `CreateCheckout` request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTerminalCheckoutResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/terminals/checkouts",
            method="POST",
            json={
                "checkout": convert_and_respect_annotation_metadata(
                    object_=checkout, annotation=TerminalCheckout, direction="write"
                ),
                "idempotency_key": idempotency_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTerminalCheckoutResponse,
                    parse_obj_as(
                        type_=CreateTerminalCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_terminal_checkouts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[TerminalCheckoutQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchTerminalCheckoutsResponse]:
        """
        Retrieves a filtered list of Terminal checkout requests created by the account making the request.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        limit : typing.Optional[int]
            Limits the number of results returned for a single request.

        query : typing.Optional[TerminalCheckoutQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchTerminalCheckoutsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/terminals/checkouts/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=TerminalCheckoutQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchTerminalCheckoutsResponse,
                    parse_obj_as(
                        type_=SearchTerminalCheckoutsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_terminal_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTerminalCheckoutResponse]:
        """
        Retrieves a Terminal checkout request by `checkout_id`.

        Parameters
        ----------
        checkout_id : str
            The unique ID for the desired `TerminalCheckout`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTerminalCheckoutResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/terminals/checkouts/{encode_path_param(checkout_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTerminalCheckoutResponse,
                    parse_obj_as(
                        type_=GetTerminalCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_terminal_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelTerminalCheckoutResponse]:
        """
        Cancels a Terminal checkout request if the status of the request permits it.

        Parameters
        ----------
        checkout_id : str
            The unique ID for the desired `TerminalCheckout`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CancelTerminalCheckoutResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/terminals/checkouts/{encode_path_param(checkout_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelTerminalCheckoutResponse,
                    parse_obj_as(
                        type_=CancelTerminalCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_terminal_refund(
        self,
        *,
        idempotency_key: str,
        refund: typing.Optional[TerminalRefund] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateTerminalRefundResponse]:
        """
        Creates a request to refund an Interac payment completed on a Square Terminal.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateRefund` request. Keys can be any valid string but
            must be unique for every `CreateRefund` request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        refund : typing.Optional[TerminalRefund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateTerminalRefundResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/terminals/refunds",
            method="POST",
            json={
                "idempotency_key": idempotency_key,
                "refund": convert_and_respect_annotation_metadata(
                    object_=refund, annotation=TerminalRefund, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateTerminalRefundResponse,
                    parse_obj_as(
                        type_=CreateTerminalRefundResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_terminal_refunds(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[TerminalRefundQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchTerminalRefundsResponse]:
        """
        Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.

        limit : typing.Optional[int]
            Limits the number of results returned for a single request.

        query : typing.Optional[TerminalRefundQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchTerminalRefundsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/terminals/refunds/search",
            method="POST",
            json={
                "cursor": cursor,
                "limit": limit,
                "query": convert_and_respect_annotation_metadata(
                    object_=query, annotation=TerminalRefundQuery, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SearchTerminalRefundsResponse,
                    parse_obj_as(
                        type_=SearchTerminalRefundsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_terminal_refund(
        self, terminal_refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTerminalRefundResponse]:
        """
        Retrieves an Interac Terminal refund object by ID.

        Parameters
        ----------
        terminal_refund_id : str
            The unique ID for the desired `TerminalRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTerminalRefundResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/terminals/refunds/{encode_path_param(terminal_refund_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTerminalRefundResponse,
                    parse_obj_as(
                        type_=GetTerminalRefundResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_terminal_refund(
        self, terminal_refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CancelTerminalRefundResponse]:
        """
        Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

        Parameters
        ----------
        terminal_refund_id : str
            The unique ID for the desired `TerminalRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CancelTerminalRefundResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/terminals/refunds/{encode_path_param(terminal_refund_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CancelTerminalRefundResponse,
                    parse_obj_as(
                        type_=CancelTerminalRefundResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
