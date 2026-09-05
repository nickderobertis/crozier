

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
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.feedback_project_logs_item import FeedbackProjectLogsItem
from ..types.feedback_response_schema import FeedbackResponseSchema
from ..types.fetch_limit import FetchLimit
from ..types.fetch_limit_param import FetchLimitParam
from ..types.fetch_pagination_cursor import FetchPaginationCursor
from ..types.fetch_project_logs_events_response import FetchProjectLogsEventsResponse
from ..types.insert_events_response import InsertEventsResponse
from ..types.insert_project_logs_event import InsertProjectLogsEvent
from ..types.max_root_span_id import MaxRootSpanId
from ..types.max_xact_id import MaxXactId
from ..types.project_id_param import ProjectIdParam
from ..types.version import Version
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLogsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_project_logs_id_insert(
        self,
        project_id: ProjectIdParam,
        *,
        events: typing.Sequence[InsertProjectLogsEvent],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InsertEventsResponse]:
        """
        Insert a set of events into the project logs

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        events : typing.Sequence[InsertProjectLogsEvent]
            A list of project logs events to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InsertEventsResponse]
            Returns the inserted row ids
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/project_logs/{encode_path_param(project_id)}/insert",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[InsertProjectLogsEvent], direction="write"
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
                    InsertEventsResponse,
                    parse_obj_as(
                        type_=InsertEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def get_project_logs_id_fetch(
        self,
        project_id: ProjectIdParam,
        *,
        limit: typing.Optional[FetchLimitParam] = None,
        max_xact_id: typing.Optional[MaxXactId] = None,
        max_root_span_id: typing.Optional[MaxRootSpanId] = None,
        version: typing.Optional[Version] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FetchProjectLogsEventsResponse]:
        """
        Fetch the events in a project logs. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        limit : typing.Optional[FetchLimitParam]
            limit the number of traces fetched

            Fetch queries may be paginated if the total result size is expected to be large (e.g. project_logs which accumulate over a long time). Note that fetch queries only support pagination in descending time order (from latest to earliest `_xact_id`. Furthermore, later pages may return rows which showed up in earlier pages, except with an earlier `_xact_id`. This happens because pagination occurs over the whole version history of the event log. You will most likely want to exclude any such duplicate, outdated rows (by `id`) from your combined result set.

            The `limit` parameter controls the number of full traces to return. So you may end up with more individual rows than the specified limit if you are fetching events containing traces.

        max_xact_id : typing.Optional[MaxXactId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        max_root_span_id : typing.Optional[MaxRootSpanId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        version : typing.Optional[Version]
            Retrieve a snapshot of events from a past time

            The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FetchProjectLogsEventsResponse]
            Returns the fetched rows
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/project_logs/{encode_path_param(project_id)}/fetch",
            method="GET",
            params={
                "limit": limit,
                "max_xact_id": max_xact_id,
                "max_root_span_id": max_root_span_id,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FetchProjectLogsEventsResponse,
                    parse_obj_as(
                        type_=FetchProjectLogsEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_project_logs_id_fetch(
        self,
        project_id: ProjectIdParam,
        *,
        limit: typing.Optional[FetchLimit] = OMIT,
        cursor: typing.Optional[FetchPaginationCursor] = OMIT,
        max_xact_id: typing.Optional[MaxXactId] = OMIT,
        max_root_span_id: typing.Optional[MaxRootSpanId] = OMIT,
        version: typing.Optional[Version] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FetchProjectLogsEventsResponse]:
        """
        Fetch the events in a project logs. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        limit : typing.Optional[FetchLimit]

        cursor : typing.Optional[FetchPaginationCursor]

        max_xact_id : typing.Optional[MaxXactId]

        max_root_span_id : typing.Optional[MaxRootSpanId]

        version : typing.Optional[Version]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FetchProjectLogsEventsResponse]
            Returns the fetched rows
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/project_logs/{encode_path_param(project_id)}/fetch",
            method="POST",
            json={
                "limit": limit,
                "cursor": cursor,
                "max_xact_id": max_xact_id,
                "max_root_span_id": max_root_span_id,
                "version": version,
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
                    FetchProjectLogsEventsResponse,
                    parse_obj_as(
                        type_=FetchProjectLogsEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    def post_project_logs_id_feedback(
        self,
        project_id: ProjectIdParam,
        *,
        feedback: typing.Sequence[FeedbackProjectLogsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedbackResponseSchema]:
        """
        Log feedback for a set of project logs events

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        feedback : typing.Sequence[FeedbackProjectLogsItem]
            A list of project logs feedback items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedbackResponseSchema]
            Returns a success status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/project_logs/{encode_path_param(project_id)}/feedback",
            method="POST",
            json={
                "feedback": convert_and_respect_annotation_metadata(
                    object_=feedback, annotation=typing.Sequence[FeedbackProjectLogsItem], direction="write"
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
                    FeedbackResponseSchema,
                    parse_obj_as(
                        type_=FeedbackResponseSchema,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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


class AsyncRawLogsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_project_logs_id_insert(
        self,
        project_id: ProjectIdParam,
        *,
        events: typing.Sequence[InsertProjectLogsEvent],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InsertEventsResponse]:
        """
        Insert a set of events into the project logs

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        events : typing.Sequence[InsertProjectLogsEvent]
            A list of project logs events to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InsertEventsResponse]
            Returns the inserted row ids
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/project_logs/{encode_path_param(project_id)}/insert",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[InsertProjectLogsEvent], direction="write"
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
                    InsertEventsResponse,
                    parse_obj_as(
                        type_=InsertEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def get_project_logs_id_fetch(
        self,
        project_id: ProjectIdParam,
        *,
        limit: typing.Optional[FetchLimitParam] = None,
        max_xact_id: typing.Optional[MaxXactId] = None,
        max_root_span_id: typing.Optional[MaxRootSpanId] = None,
        version: typing.Optional[Version] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FetchProjectLogsEventsResponse]:
        """
        Fetch the events in a project logs. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        limit : typing.Optional[FetchLimitParam]
            limit the number of traces fetched

            Fetch queries may be paginated if the total result size is expected to be large (e.g. project_logs which accumulate over a long time). Note that fetch queries only support pagination in descending time order (from latest to earliest `_xact_id`. Furthermore, later pages may return rows which showed up in earlier pages, except with an earlier `_xact_id`. This happens because pagination occurs over the whole version history of the event log. You will most likely want to exclude any such duplicate, outdated rows (by `id`) from your combined result set.

            The `limit` parameter controls the number of full traces to return. So you may end up with more individual rows than the specified limit if you are fetching events containing traces.

        max_xact_id : typing.Optional[MaxXactId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        max_root_span_id : typing.Optional[MaxRootSpanId]
            DEPRECATION NOTICE: The manually-constructed pagination cursor is deprecated in favor of the explicit 'cursor' returned by object fetch requests. Please prefer the 'cursor' argument going forwards.

            Together, `max_xact_id` and `max_root_span_id` form a pagination cursor

            Since a paginated fetch query returns results in order from latest to earliest, the cursor for the next page can be found as the row with the minimum (earliest) value of the tuple `(_xact_id, root_span_id)`. See the documentation of `limit` for an overview of paginating fetch queries.

        version : typing.Optional[Version]
            Retrieve a snapshot of events from a past time

            The version id is essentially a filter on the latest event transaction id. You can use the `max_xact_id` returned by a past fetch as the version to reproduce that exact fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FetchProjectLogsEventsResponse]
            Returns the fetched rows
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/project_logs/{encode_path_param(project_id)}/fetch",
            method="GET",
            params={
                "limit": limit,
                "max_xact_id": max_xact_id,
                "max_root_span_id": max_root_span_id,
                "version": version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FetchProjectLogsEventsResponse,
                    parse_obj_as(
                        type_=FetchProjectLogsEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_project_logs_id_fetch(
        self,
        project_id: ProjectIdParam,
        *,
        limit: typing.Optional[FetchLimit] = OMIT,
        cursor: typing.Optional[FetchPaginationCursor] = OMIT,
        max_xact_id: typing.Optional[MaxXactId] = OMIT,
        max_root_span_id: typing.Optional[MaxRootSpanId] = OMIT,
        version: typing.Optional[Version] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FetchProjectLogsEventsResponse]:
        """
        Fetch the events in a project logs. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        limit : typing.Optional[FetchLimit]

        cursor : typing.Optional[FetchPaginationCursor]

        max_xact_id : typing.Optional[MaxXactId]

        max_root_span_id : typing.Optional[MaxRootSpanId]

        version : typing.Optional[Version]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FetchProjectLogsEventsResponse]
            Returns the fetched rows
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/project_logs/{encode_path_param(project_id)}/fetch",
            method="POST",
            json={
                "limit": limit,
                "cursor": cursor,
                "max_xact_id": max_xact_id,
                "max_root_span_id": max_root_span_id,
                "version": version,
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
                    FetchProjectLogsEventsResponse,
                    parse_obj_as(
                        type_=FetchProjectLogsEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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

    async def post_project_logs_id_feedback(
        self,
        project_id: ProjectIdParam,
        *,
        feedback: typing.Sequence[FeedbackProjectLogsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedbackResponseSchema]:
        """
        Log feedback for a set of project logs events

        Parameters
        ----------
        project_id : ProjectIdParam
            Project id

        feedback : typing.Sequence[FeedbackProjectLogsItem]
            A list of project logs feedback items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedbackResponseSchema]
            Returns a success status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/project_logs/{encode_path_param(project_id)}/feedback",
            method="POST",
            json={
                "feedback": convert_and_respect_annotation_metadata(
                    object_=feedback, annotation=typing.Sequence[FeedbackProjectLogsItem], direction="write"
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
                    FeedbackResponseSchema,
                    parse_obj_as(
                        type_=FeedbackResponseSchema,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        str,
                        parse_obj_as(
                            type_=str,
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
