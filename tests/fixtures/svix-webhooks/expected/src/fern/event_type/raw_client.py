

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
from ..types.event_type_out import EventTypeOut
from ..types.http_error_out import HttpErrorOut
from ..types.http_validation_error import HttpValidationError
from ..types.list_response_event_type_out import ListResponseEventTypeOut
from ..types.ordering import Ordering
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEventTypeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v1event_type_list(
        self,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        include_archived: typing.Optional[bool] = None,
        with_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListResponseEventTypeOut]:
        """
        Return the list of event types.

        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        include_archived : typing.Optional[bool]
            When `true` archived (deleted but not expunged) items are included in the response

        with_content : typing.Optional[bool]
            When `true` the full item (including the schema) is included in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListResponseEventTypeOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/event-type",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "order": order,
                "include_archived": include_archived,
                "with_content": with_content,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseEventTypeOut,
                    parse_obj_as(
                        type_=ListResponseEventTypeOut,
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

    def v1event_type_create(
        self,
        *,
        description: str,
        name: str,
        idempotency_key: typing.Optional[str] = None,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EventTypeOut]:
        """
        Create new or unarchive existing event type.

        Unarchiving an event type will allow endpoints to filter on it and messages to be sent with it.
        Endpoints filtering on the event type before archival will continue to filter on it.
        This operation does not preserve the description and schemas.

        Parameters
        ----------
        description : str

        name : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]
            The schema for the event type for a specific version as a JSON schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EventTypeOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/event-type",
            method="POST",
            json={
                "archived": archived,
                "deprecated": deprecated,
                "description": description,
                "featureFlag": feature_flag,
                "name": name,
                "schemas": schemas,
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
                    EventTypeOut,
                    parse_obj_as(
                        type_=EventTypeOut,
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

    def v1event_type_get(
        self, event_type_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EventTypeOut]:
        """
        Get an event type.

        Parameters
        ----------
        event_type_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EventTypeOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/event-type/{encode_path_param(event_type_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventTypeOut,
                    parse_obj_as(
                        type_=EventTypeOut,
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

    def v1event_type_update(
        self,
        event_type_name: str,
        *,
        description: str,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EventTypeOut]:
        """
        Update an event type.

        Parameters
        ----------
        event_type_name : str

        description : str

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]
            The schema for the event type for a specific version as a JSON schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EventTypeOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/event-type/{encode_path_param(event_type_name)}",
            method="PUT",
            json={
                "archived": archived,
                "deprecated": deprecated,
                "description": description,
                "featureFlag": feature_flag,
                "schemas": schemas,
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
                    EventTypeOut,
                    parse_obj_as(
                        type_=EventTypeOut,
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

    def v1event_type_delete(
        self,
        event_type_name: str,
        *,
        expunge: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Archive an event type.

        Endpoints already configured to filter on an event type will continue to do so after archival.
        However, new messages can not be sent with it and endpoints can not filter on it.
        An event type can be unarchived with the
        [create operation](#operation/create_event_type_api_v1_event_type__post).

        Parameters
        ----------
        event_type_name : str

        expunge : typing.Optional[bool]
            By default event types are archived when "deleted". Passing this to `true` deletes them entirely.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/event-type/{encode_path_param(event_type_name)}",
            method="DELETE",
            params={
                "expunge": expunge,
            },
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

    def patch_event_type(
        self,
        event_type_name: str,
        *,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EventTypeOut]:
        """
        Partially update an event type.

        Parameters
        ----------
        event_type_name : str

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        description : typing.Optional[str]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EventTypeOut]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/event-type/{encode_path_param(event_type_name)}",
            method="PATCH",
            json={
                "archived": archived,
                "deprecated": deprecated,
                "description": description,
                "featureFlag": feature_flag,
                "schemas": schemas,
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
                    EventTypeOut,
                    parse_obj_as(
                        type_=EventTypeOut,
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


class AsyncRawEventTypeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v1event_type_list(
        self,
        *,
        limit: typing.Optional[int] = None,
        iterator: typing.Optional[str] = None,
        order: typing.Optional[Ordering] = None,
        include_archived: typing.Optional[bool] = None,
        with_content: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListResponseEventTypeOut]:
        """
        Return the list of event types.

        Parameters
        ----------
        limit : typing.Optional[int]
            Limit the number of returned items

        iterator : typing.Optional[str]
            The iterator returned from a prior invocation

        order : typing.Optional[Ordering]
            The sorting order of the returned items

        include_archived : typing.Optional[bool]
            When `true` archived (deleted but not expunged) items are included in the response

        with_content : typing.Optional[bool]
            When `true` the full item (including the schema) is included in the response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListResponseEventTypeOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/event-type",
            method="GET",
            params={
                "limit": limit,
                "iterator": iterator,
                "order": order,
                "include_archived": include_archived,
                "with_content": with_content,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListResponseEventTypeOut,
                    parse_obj_as(
                        type_=ListResponseEventTypeOut,
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

    async def v1event_type_create(
        self,
        *,
        description: str,
        name: str,
        idempotency_key: typing.Optional[str] = None,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EventTypeOut]:
        """
        Create new or unarchive existing event type.

        Unarchiving an event type will allow endpoints to filter on it and messages to be sent with it.
        Endpoints filtering on the event type before archival will continue to filter on it.
        This operation does not preserve the description and schemas.

        Parameters
        ----------
        description : str

        name : str

        idempotency_key : typing.Optional[str]
            The request's idempotency key

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]
            The schema for the event type for a specific version as a JSON schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EventTypeOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/event-type",
            method="POST",
            json={
                "archived": archived,
                "deprecated": deprecated,
                "description": description,
                "featureFlag": feature_flag,
                "name": name,
                "schemas": schemas,
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
                    EventTypeOut,
                    parse_obj_as(
                        type_=EventTypeOut,
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

    async def v1event_type_get(
        self, event_type_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EventTypeOut]:
        """
        Get an event type.

        Parameters
        ----------
        event_type_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EventTypeOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/event-type/{encode_path_param(event_type_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EventTypeOut,
                    parse_obj_as(
                        type_=EventTypeOut,
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

    async def v1event_type_update(
        self,
        event_type_name: str,
        *,
        description: str,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EventTypeOut]:
        """
        Update an event type.

        Parameters
        ----------
        event_type_name : str

        description : str

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]
            The schema for the event type for a specific version as a JSON schema.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EventTypeOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/event-type/{encode_path_param(event_type_name)}",
            method="PUT",
            json={
                "archived": archived,
                "deprecated": deprecated,
                "description": description,
                "featureFlag": feature_flag,
                "schemas": schemas,
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
                    EventTypeOut,
                    parse_obj_as(
                        type_=EventTypeOut,
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

    async def v1event_type_delete(
        self,
        event_type_name: str,
        *,
        expunge: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Archive an event type.

        Endpoints already configured to filter on an event type will continue to do so after archival.
        However, new messages can not be sent with it and endpoints can not filter on it.
        An event type can be unarchived with the
        [create operation](#operation/create_event_type_api_v1_event_type__post).

        Parameters
        ----------
        event_type_name : str

        expunge : typing.Optional[bool]
            By default event types are archived when "deleted". Passing this to `true` deletes them entirely.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/event-type/{encode_path_param(event_type_name)}",
            method="DELETE",
            params={
                "expunge": expunge,
            },
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

    async def patch_event_type(
        self,
        event_type_name: str,
        *,
        archived: typing.Optional[bool] = OMIT,
        deprecated: typing.Optional[bool] = OMIT,
        description: typing.Optional[str] = OMIT,
        feature_flag: typing.Optional[str] = OMIT,
        schemas: typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EventTypeOut]:
        """
        Partially update an event type.

        Parameters
        ----------
        event_type_name : str

        archived : typing.Optional[bool]

        deprecated : typing.Optional[bool]

        description : typing.Optional[str]

        feature_flag : typing.Optional[str]

        schemas : typing.Optional[typing.Dict[str, typing.Optional[typing.Dict[str, typing.Any]]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EventTypeOut]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/event-type/{encode_path_param(event_type_name)}",
            method="PATCH",
            json={
                "archived": archived,
                "deprecated": deprecated,
                "description": description,
                "featureFlag": feature_flag,
                "schemas": schemas,
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
                    EventTypeOut,
                    parse_obj_as(
                        type_=EventTypeOut,
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
