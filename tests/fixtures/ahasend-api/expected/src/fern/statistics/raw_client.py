

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.bounce_statistics_response import BounceStatisticsResponse
from ..types.deliverability_statistics_response import DeliverabilityStatisticsResponse
from ..types.delivery_time_statistics_response import DeliveryTimeStatisticsResponse
from ..types.error_response import ErrorResponse
from .types.get_bounce_statistics_request_group_by import GetBounceStatisticsRequestGroupBy
from .types.get_deliverability_statistics_request_group_by import GetDeliverabilityStatisticsRequestGroupBy
from .types.get_delivery_time_statistics_request_group_by import GetDeliveryTimeStatisticsRequestGroupBy
from pydantic import ValidationError


class RawStatisticsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_deliverability_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetDeliverabilityStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeliverabilityStatisticsResponse]:
        """
        Returns transactional deliverability statistics grouped by status

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domain
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetDeliverabilityStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeliverabilityStatisticsResponse]
            Deliverability statistics
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/statistics/transactional/deliverability",
            method="GET",
            params={
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "sender_domain": sender_domain,
                "recipient_domains": recipient_domains,
                "tags": tags,
                "group_by": group_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeliverabilityStatisticsResponse,
                    parse_obj_as(
                        type_=DeliverabilityStatisticsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_bounce_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetBounceStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BounceStatisticsResponse]:
        """
        Returns transactional bounce statistics grouped by classification

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domain
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetBounceStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BounceStatisticsResponse]
            Bounce statistics
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/statistics/transactional/bounce",
            method="GET",
            params={
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "sender_domain": sender_domain,
                "recipient_domains": recipient_domains,
                "tags": tags,
                "group_by": group_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BounceStatisticsResponse,
                    parse_obj_as(
                        type_=BounceStatisticsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_delivery_time_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetDeliveryTimeStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeliveryTimeStatisticsResponse]:
        """
        Returns transactional delivery time statistics grouped by recipient domain

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domains
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetDeliveryTimeStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeliveryTimeStatisticsResponse]
            Delivery time statistics
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/statistics/transactional/delivery-time",
            method="GET",
            params={
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "sender_domain": sender_domain,
                "recipient_domains": recipient_domains,
                "tags": tags,
                "group_by": group_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeliveryTimeStatisticsResponse,
                    parse_obj_as(
                        type_=DeliveryTimeStatisticsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawStatisticsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_deliverability_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetDeliverabilityStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeliverabilityStatisticsResponse]:
        """
        Returns transactional deliverability statistics grouped by status

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domain
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetDeliverabilityStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeliverabilityStatisticsResponse]
            Deliverability statistics
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/statistics/transactional/deliverability",
            method="GET",
            params={
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "sender_domain": sender_domain,
                "recipient_domains": recipient_domains,
                "tags": tags,
                "group_by": group_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeliverabilityStatisticsResponse,
                    parse_obj_as(
                        type_=DeliverabilityStatisticsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_bounce_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetBounceStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BounceStatisticsResponse]:
        """
        Returns transactional bounce statistics grouped by classification

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domain
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetBounceStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BounceStatisticsResponse]
            Bounce statistics
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/statistics/transactional/bounce",
            method="GET",
            params={
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "sender_domain": sender_domain,
                "recipient_domains": recipient_domains,
                "tags": tags,
                "group_by": group_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BounceStatisticsResponse,
                    parse_obj_as(
                        type_=BounceStatisticsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_delivery_time_statistics(
        self,
        account_id: str,
        *,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        sender_domain: typing.Optional[str] = None,
        recipient_domains: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        group_by: typing.Optional[GetDeliveryTimeStatisticsRequestGroupBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeliveryTimeStatisticsResponse]:
        """
        Returns transactional delivery time statistics grouped by recipient domain

        The global statistics role can query all sender domains. A
        domain-scoped key is limited to authorized domains and must authorize
        every comma-separated value supplied in `sender_domain`.

        **Query Parameters:**
        - `from_time`: Filter statistics after this date (RFC3339 format)
        - `to_time`: Filter statistics before this date (RFC3339 format)
        - `sender_domain`: Filter by sender domain
        - `recipient_domains`: Filter by recipient domains
        - `tags`: Filter by tags (comma-separated)
        - `group_by`: Group by time period (hour, day, week, month)

        Parameters
        ----------
        account_id : str
            Account ID

        from_time : typing.Optional[dt.datetime]
            Filter statistics after this datetime (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter statistics before this datetime (RFC3339 format)

        sender_domain : typing.Optional[str]
            Comma-separated sender domains; the key must authorize every requested domain

        recipient_domains : typing.Optional[str]
            Filter by a comma separated list of recipient domains

        tags : typing.Optional[str]
            Filter by tags (comma-separated)

        group_by : typing.Optional[GetDeliveryTimeStatisticsRequestGroupBy]
            Group by time period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeliveryTimeStatisticsResponse]
            Delivery time statistics
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/statistics/transactional/delivery-time",
            method="GET",
            params={
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "sender_domain": sender_domain,
                "recipient_domains": recipient_domains,
                "tags": tags,
                "group_by": group_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeliveryTimeStatisticsResponse,
                    parse_obj_as(
                        type_=DeliveryTimeStatisticsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
