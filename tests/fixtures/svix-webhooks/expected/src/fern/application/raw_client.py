

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.application_out import ApplicationOut
from ..types.http_error_out import HttpErrorOut
from ..types.http_validation_error import HttpValidationError
from ..types.list_response_application_out import ListResponseApplicationOut
from ..types.ordering import Ordering
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawApplicationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v1application_list(
        self,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseApplicationOut]:
        """
        List of all the organization's applications.

        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListResponseApplicationOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/app",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseApplicationOut,
                    parse_obj_as(
                        type_=ListResponseApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1application_create(
        self,
        *,
        name: str,
        get_if_exists: typing.Optional[bool] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplicationOut]:
        """
        Create a new application.

        Parameters
        ----------
        name : str

        get_if_exists : typing.Optional[bool]
            Get an existing application, or create a new one if doesn't exist. It's two separate functions in the libs.

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/app",
            method="POST",
            params={
                "get_if_exists": get_if_exists,
            },
            json={
                "metadata": metadata,
                "name": name,
                "throttleRate": throttle_rate,
                "uid": uid,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationOut,
                    parse_obj_as(
                        type_=ApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1application_get(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ApplicationOut]:
        """
        Get an application.

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationOut,
                    parse_obj_as(
                        type_=ApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1application_update(
        self,
        app_id: str,
        *,
        name: str,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplicationOut]:
        """
        Update an application.

        Parameters
        ----------
        app_id : str

        name : str

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}",
            method="PUT",
            json={
                "metadata": metadata,
                "name": name,
                "throttleRate": throttle_rate,
                "uid": uid,
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
                    ApplicationOut,
                    parse_obj_as(
                        type_=ApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def v1application_delete(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete an application.

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    def patch_application(
        self,
        app_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ApplicationOut]:
        """
        Partially update an application.

        Parameters
        ----------
        app_id : str

        metadata : typing.Optional[typing.Dict[str, str]]

        name : typing.Optional[str]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ApplicationOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}",
            method="PATCH",
            json={
                "metadata": metadata,
                "name": name,
                "throttleRate": throttle_rate,
                "uid": uid,
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
                    ApplicationOut,
                    parse_obj_as(
                        type_=ApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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


class AsyncRawApplicationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v1application_list(
        self,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListResponseApplicationOut]:
        """
        List of all the organization's applications.

        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListResponseApplicationOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/app",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseApplicationOut,
                    parse_obj_as(
                        type_=ListResponseApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1application_create(
        self,
        *,
        name: str,
        get_if_exists: typing.Optional[bool] = None,
        idempotency_key: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplicationOut]:
        """
        Create a new application.

        Parameters
        ----------
        name : str

        get_if_exists : typing.Optional[bool]
            Get an existing application, or create a new one if doesn't exist. It's two separate functions in the libs.

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/app",
            method="POST",
            params={
                "get_if_exists": get_if_exists,
            },
            json={
                "metadata": metadata,
                "name": name,
                "throttleRate": throttle_rate,
                "uid": uid,
            },
            headers={
                "content-type": "application/json",
                "idempotency-key": str(idempotency_key) if idempotency_key is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationOut,
                    parse_obj_as(
                        type_=ApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1application_get(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ApplicationOut]:
        """
        Get an application.

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ApplicationOut,
                    parse_obj_as(
                        type_=ApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1application_update(
        self,
        app_id: str,
        *,
        name: str,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplicationOut]:
        """
        Update an application.

        Parameters
        ----------
        app_id : str

        name : str

        metadata : typing.Optional[typing.Dict[str, str]]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]
            Optional unique identifier for the application

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}",
            method="PUT",
            json={
                "metadata": metadata,
                "name": name,
                "throttleRate": throttle_rate,
                "uid": uid,
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
                    ApplicationOut,
                    parse_obj_as(
                        type_=ApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def v1application_delete(
        self, app_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete an application.

        Parameters
        ----------
        app_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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

    async def patch_application(
        self,
        app_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        throttle_rate: typing.Optional[int] = OMIT,
        uid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ApplicationOut]:
        """
        Partially update an application.

        Parameters
        ----------
        app_id : str

        metadata : typing.Optional[typing.Dict[str, str]]

        name : typing.Optional[str]

        throttle_rate : typing.Optional[int]
            Maximum messages per second to send to this application's endpoints.

            Outgoing messages will be throttled to this rate.

        uid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ApplicationOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/app/{encode_path_param(app_id)}",
            method="PATCH",
            json={
                "metadata": metadata,
                "name": name,
                "throttleRate": throttle_rate,
                "uid": uid,
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
                    ApplicationOut,
                    parse_obj_as(
                        type_=ApplicationOut,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpErrorOut,
                        parse_obj_as(
                            type_=HttpErrorOut,
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
