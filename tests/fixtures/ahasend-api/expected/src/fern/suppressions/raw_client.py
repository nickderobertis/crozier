

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.create_suppression_response import CreateSuppressionResponse
from ..types.error_response import ErrorResponse
from ..types.paginated_suppressions_response import PaginatedSuppressionsResponse
from ..types.success_response import SuccessResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSuppressionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_suppressions(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedSuppressionsResponse]:
        """
        Returns a list of suppressions for the account

        **Query Parameters:**
        - `domain`: Filter by domain (optional)
        - `email`: Filter by email (optional)
        - `from_time`: Filter suppressions created after this time (RFC3339 format, optional)
        - `to_time`: Filter suppressions created before this time (RFC3339 format, optional)
        - `limit`: Maximum number of items to return (1-100, default: 100)
        - `after`: Pagination cursor for the next page
        - `before`: Pagination cursor for the previous page

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Filter by domain

        email : typing.Optional[str]
            Email address

        from_time : typing.Optional[dt.datetime]
            Filter suppressions created after this time (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter suppressions created before this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page. Provide the value provided in `previous_cursor` from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedSuppressionsResponse]
            List of suppressions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/suppressions",
            method="GET",
            params={
                "domain": domain,
                "email": email,
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "limit": limit,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedSuppressionsResponse,
                    parse_obj_as(
                        type_=PaginatedSuppressionsResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
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

    def create_suppression(
        self,
        account_id: str,
        *,
        email: str,
        expires_at: dt.datetime,
        idempotency_key: typing.Optional[str] = None,
        domain: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateSuppressionResponse]:
        """
        Creates a new suppression for an email address

        **Validation Requirements:**
        - `email` must be a valid email address
        - `expires_at` must be in RFC3339 format
        - `domain` is optional - if not provided, applies to all account domains

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address to suppress

        expires_at : dt.datetime
            When the suppression expires (RFC3339 format)

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        domain : typing.Optional[str]
            Domain for which to suppress the email

        reason : typing.Optional[str]
            Reason for suppression

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateSuppressionResponse]
            Suppression created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/suppressions",
            method="POST",
            json={
                "email": email,
                "domain": domain,
                "reason": reason,
                "expires_at": expires_at,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateSuppressionResponse,
                    parse_obj_as(
                        type_=CreateSuppressionResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def delete_suppression(
        self,
        account_id: str,
        *,
        email: str,
        domain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Deletes suppressions for an email address

        **Query Parameters:**
        - `email`: Required email address to delete from suppression list
        - `domain`: Optional domain filter to delete suppressions for specific domain only

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address

        domain : typing.Optional[str]
            Optional domain filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            Suppression deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/suppressions",
            method="DELETE",
            params={
                "email": email,
                "domain": domain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
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

    def delete_all_suppressions(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SuccessResponse]:
        """
        Deletes all suppressions for the account

        **Query Parameters:**
        - `domain`: Optional domain filter to delete suppressions for specific domain only

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Optional domain filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SuccessResponse]
            All suppressions deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/suppressions/all",
            method="DELETE",
            params={
                "domain": domain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawSuppressionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_suppressions(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        from_time: typing.Optional[dt.datetime] = None,
        to_time: typing.Optional[dt.datetime] = None,
        limit: typing.Optional[int] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedSuppressionsResponse]:
        """
        Returns a list of suppressions for the account

        **Query Parameters:**
        - `domain`: Filter by domain (optional)
        - `email`: Filter by email (optional)
        - `from_time`: Filter suppressions created after this time (RFC3339 format, optional)
        - `to_time`: Filter suppressions created before this time (RFC3339 format, optional)
        - `limit`: Maximum number of items to return (1-100, default: 100)
        - `after`: Pagination cursor for the next page
        - `before`: Pagination cursor for the previous page

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Filter by domain

        email : typing.Optional[str]
            Email address

        from_time : typing.Optional[dt.datetime]
            Filter suppressions created after this time (RFC3339 format)

        to_time : typing.Optional[dt.datetime]
            Filter suppressions created before this time (RFC3339 format)

        limit : typing.Optional[int]
            Maximum number of items to return (1-100)

        after : typing.Optional[str]
            Pagination cursor for the next page. Provide the value provided in `next_cursor` from the response.

        before : typing.Optional[str]
            Pagination cursor for the previous page. Provide the value provided in `previous_cursor` from the response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedSuppressionsResponse]
            List of suppressions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/suppressions",
            method="GET",
            params={
                "domain": domain,
                "email": email,
                "from_time": serialize_datetime(from_time) if from_time is not None else None,
                "to_time": serialize_datetime(to_time) if to_time is not None else None,
                "limit": limit,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedSuppressionsResponse,
                    parse_obj_as(
                        type_=PaginatedSuppressionsResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def create_suppression(
        self,
        account_id: str,
        *,
        email: str,
        expires_at: dt.datetime,
        idempotency_key: typing.Optional[str] = None,
        domain: typing.Optional[str] = OMIT,
        reason: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateSuppressionResponse]:
        """
        Creates a new suppression for an email address

        **Validation Requirements:**
        - `email` must be a valid email address
        - `expires_at` must be in RFC3339 format
        - `domain` is optional - if not provided, applies to all account domains

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address to suppress

        expires_at : dt.datetime
            When the suppression expires (RFC3339 format)

        idempotency_key : typing.Optional[str]
            Optional idempotency key for safe request retries. Must be a unique string for each logical request.
            An identical request with a completed stored outcome returns the original status and body. An in-progress
            execution returns 409, a changed method/path/body returns 422, and a released 5xx execution may run again.
            Keys for non-secret responses expire after 24 hours. API-key create responses include a one-time `secret_key`,
            so successful encrypted replay responses for those operations expire after 5 minutes.

        domain : typing.Optional[str]
            Domain for which to suppress the email

        reason : typing.Optional[str]
            Reason for suppression

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateSuppressionResponse]
            Suppression created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/suppressions",
            method="POST",
            json={
                "email": email,
                "domain": domain,
                "reason": reason,
                "expires_at": expires_at,
            },
            headers={
                "content-type": "application/json",
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateSuppressionResponse,
                    parse_obj_as(
                        type_=CreateSuppressionResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def delete_suppression(
        self,
        account_id: str,
        *,
        email: str,
        domain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Deletes suppressions for an email address

        **Query Parameters:**
        - `email`: Required email address to delete from suppression list
        - `domain`: Optional domain filter to delete suppressions for specific domain only

        Parameters
        ----------
        account_id : str
            Account ID

        email : str
            Email address

        domain : typing.Optional[str]
            Optional domain filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            Suppression deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/suppressions",
            method="DELETE",
            params={
                "email": email,
                "domain": domain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def delete_all_suppressions(
        self,
        account_id: str,
        *,
        domain: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SuccessResponse]:
        """
        Deletes all suppressions for the account

        **Query Parameters:**
        - `domain`: Optional domain filter to delete suppressions for specific domain only

        Parameters
        ----------
        account_id : str
            Account ID

        domain : typing.Optional[str]
            Optional domain filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SuccessResponse]
            All suppressions deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/accounts/{encode_path_param(account_id)}/suppressions/all",
            method="DELETE",
            params={
                "domain": domain,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SuccessResponse,
                    parse_obj_as(
                        type_=SuccessResponse,
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
            if _response.status_code == 404:
                raise NotFoundError(
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
