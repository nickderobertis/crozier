

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
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_acceptable_error import NotAcceptableError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.ob_error_response1 import ObErrorResponse1
from ..types.ob_read_transaction6 import ObReadTransaction6
from pydantic import ValidationError


class RawTransactionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_accounts_account_id_statements_statement_id_transactions(
        self, account_id: str, statement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ObReadTransaction6]:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        statement_id : str
            StatementId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObReadTransaction6]
            Transactions Read
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounts/{encode_path_param(account_id)}/statements/{encode_path_param(statement_id)}/transactions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObReadTransaction6,
                    parse_obj_as(
                        type_=ObReadTransaction6,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
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

    def get_accounts_account_id_transactions(
        self,
        account_id: str,
        *,
        from_booking_date_time: typing.Optional[dt.datetime] = None,
        to_booking_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ObReadTransaction6]:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        from_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObReadTransaction6]
            Transactions Read
        """
        _response = self._client_wrapper.httpx_client.request(
            f"accounts/{encode_path_param(account_id)}/transactions",
            method="GET",
            params={
                "fromBookingDateTime": serialize_datetime(from_booking_date_time)
                if from_booking_date_time is not None
                else None,
                "toBookingDateTime": serialize_datetime(to_booking_date_time)
                if to_booking_date_time is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObReadTransaction6,
                    parse_obj_as(
                        type_=ObReadTransaction6,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
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

    def get_transactions(
        self,
        *,
        from_booking_date_time: typing.Optional[dt.datetime] = None,
        to_booking_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ObReadTransaction6]:
        """
        Parameters
        ----------
        from_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ObReadTransaction6]
            Transactions Read
        """
        _response = self._client_wrapper.httpx_client.request(
            "transactions",
            method="GET",
            params={
                "fromBookingDateTime": serialize_datetime(from_booking_date_time)
                if from_booking_date_time is not None
                else None,
                "toBookingDateTime": serialize_datetime(to_booking_date_time)
                if to_booking_date_time is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObReadTransaction6,
                    parse_obj_as(
                        type_=ObReadTransaction6,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
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


class AsyncRawTransactionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_accounts_account_id_statements_statement_id_transactions(
        self, account_id: str, statement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ObReadTransaction6]:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        statement_id : str
            StatementId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObReadTransaction6]
            Transactions Read
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounts/{encode_path_param(account_id)}/statements/{encode_path_param(statement_id)}/transactions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObReadTransaction6,
                    parse_obj_as(
                        type_=ObReadTransaction6,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
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

    async def get_accounts_account_id_transactions(
        self,
        account_id: str,
        *,
        from_booking_date_time: typing.Optional[dt.datetime] = None,
        to_booking_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ObReadTransaction6]:
        """
        Parameters
        ----------
        account_id : str
            AccountId

        from_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObReadTransaction6]
            Transactions Read
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"accounts/{encode_path_param(account_id)}/transactions",
            method="GET",
            params={
                "fromBookingDateTime": serialize_datetime(from_booking_date_time)
                if from_booking_date_time is not None
                else None,
                "toBookingDateTime": serialize_datetime(to_booking_date_time)
                if to_booking_date_time is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObReadTransaction6,
                    parse_obj_as(
                        type_=ObReadTransaction6,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
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

    async def get_transactions(
        self,
        *,
        from_booking_date_time: typing.Optional[dt.datetime] = None,
        to_booking_date_time: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ObReadTransaction6]:
        """
        Parameters
        ----------
        from_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions FROM
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        to_booking_date_time : typing.Optional[dt.datetime]
            The UTC ISO 8601 Date Time to filter transactions TO
            NB Time component is optional - set to 00:00:00 for just Date.
            If the Date Time contains a timezone, the ASPSP must ignore the timezone component.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ObReadTransaction6]
            Transactions Read
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transactions",
            method="GET",
            params={
                "fromBookingDateTime": serialize_datetime(from_booking_date_time)
                if from_booking_date_time is not None
                else None,
                "toBookingDateTime": serialize_datetime(to_booking_date_time)
                if to_booking_date_time is not None
                else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ObReadTransaction6,
                    parse_obj_as(
                        type_=ObReadTransaction6,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ObErrorResponse1,
                        parse_obj_as(
                            type_=ObErrorResponse1,
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
