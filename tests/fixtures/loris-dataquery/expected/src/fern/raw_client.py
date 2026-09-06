

import contextlib
import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.forbidden_error import ForbiddenError
from .errors.internal_server_error import InternalServerError
from .types.all_queries import AllQueries
from .types.bad_request_error_body import BadRequestErrorBody
from .types.get_queries_query_id_count_response import GetQueriesQueryIdCountResponse
from .types.post_queries_response import PostQueriesResponse
from .types.query import Query
from .types.query_criteria_group import QueryCriteriaGroup
from .types.query_field import QueryField
from .types.query_object_type import QueryObjectType
from .types.query_run_list import QueryRunList
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_a_list_of_a_recent_shared_and_study_top_queries_for_the_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AllQueries]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AllQueries]
            Successfully operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "queries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AllQueries,
                    parse_obj_as(
                        type_=AllQueries,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def post_queries(
        self,
        *,
        type: QueryObjectType,
        fields: typing.Sequence[QueryField],
        criteria: typing.Optional[QueryCriteriaGroup] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostQueriesResponse]:
        """
        Create a new query and return the QueryID. If the same query (fields and criteria) already exists, the same QueryID will be returned instead of a new one being created.

        Parameters
        ----------
        type : QueryObjectType

        fields : typing.Sequence[QueryField]

        criteria : typing.Optional[QueryCriteriaGroup]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostQueriesResponse]
            Query successfully created
        """
        _response = self._client_wrapper.httpx_client.request(
            "queries",
            method="POST",
            json={
                "type": type,
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Sequence[QueryField], direction="write"
                ),
                "criteria": convert_and_respect_annotation_metadata(
                    object_=criteria, annotation=QueryCriteriaGroup, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostQueriesResponse,
                    parse_obj_as(
                        type_=PostQueriesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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

    def get_a_list_of_a_recent_query_runs_for_the_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[QueryRunList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryRunList]
            Successfully operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "queries/runs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryRunList,
                    parse_obj_as(
                        type_=QueryRunList,
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

    def get_queries_query_id(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Query]:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Query]
            The Query was successfully retrieved
        """
        _response = self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Query,
                    parse_obj_as(
                        type_=Query,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def patch_queries_query_id(
        self,
        query_id: int,
        *,
        share: typing.Optional[bool] = None,
        star: typing.Optional[bool] = None,
        adminname: typing.Optional[str] = None,
        dashboardname: typing.Optional[str] = None,
        loginpagename: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        share : typing.Optional[bool]
            if true, the query will be shared. If false, it will be unshared

        star : typing.Optional[bool]
            if true, the query will be shared. If false, it will be unshared

        adminname : typing.Optional[str]
            The admin name to pin the query as. If the empty string, will be unpinned.

        dashboardname : typing.Optional[str]
            The admin name to pin the query to the dashboard as. If the empty string, will be unpinned.

        loginpagename : typing.Optional[str]
            The admin name to pin the query to the login page as. If the empty string, will be unpinned.

        name : typing.Optional[str]
            The name to set for the query for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}",
            method="PATCH",
            params={
                "share": share,
                "star": star,
                "adminname": adminname,
                "dashboardname": dashboardname,
                "loginpagename": loginpagename,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_queries_query_id_run(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[QueryRunList]:
        """
        Return a list of summarizing previous runs of this query

        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[QueryRunList]
            Successfully operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}/run",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryRunList,
                    parse_obj_as(
                        type_=QueryRunList,
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

    @contextlib.contextmanager
    def post_queries_query_id_run(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Run the query QueryID and returns the results.

        This endpoint will result in a new query run being generated, which will be returned in the queries of the user on the /queries endpoint.

        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The query was able to be successfully run
        """
        with self._client_wrapper.httpx_client.stream(
            f"queries/{encode_path_param(query_id)}/run",
            method="POST",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def get_queries_query_id_count(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetQueriesQueryIdCountResponse]:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetQueriesQueryIdCountResponse]
            A count of the number of candidate matches that would be returned if the query were to be run by the current user right now.

            This endpoint does *not* result in a new query run being generated or run the query, it only returns the count of how many candidates would match if the query *were* to be run.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetQueriesQueryIdCountResponse,
                    parse_obj_as(
                        type_=GetQueriesQueryIdCountResponse,
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

    def get_queries_query_id_run_query_run_id(
        self, query_id: int, query_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        query_run_id : int
            the identifier of a previous run for this QueryID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}/run/{encode_path_param(query_run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_a_list_of_a_recent_shared_and_study_top_queries_for_the_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AllQueries]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AllQueries]
            Successfully operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "queries",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AllQueries,
                    parse_obj_as(
                        type_=AllQueries,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def post_queries(
        self,
        *,
        type: QueryObjectType,
        fields: typing.Sequence[QueryField],
        criteria: typing.Optional[QueryCriteriaGroup] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostQueriesResponse]:
        """
        Create a new query and return the QueryID. If the same query (fields and criteria) already exists, the same QueryID will be returned instead of a new one being created.

        Parameters
        ----------
        type : QueryObjectType

        fields : typing.Sequence[QueryField]

        criteria : typing.Optional[QueryCriteriaGroup]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostQueriesResponse]
            Query successfully created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "queries",
            method="POST",
            json={
                "type": type,
                "fields": convert_and_respect_annotation_metadata(
                    object_=fields, annotation=typing.Sequence[QueryField], direction="write"
                ),
                "criteria": convert_and_respect_annotation_metadata(
                    object_=criteria, annotation=QueryCriteriaGroup, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostQueriesResponse,
                    parse_obj_as(
                        type_=PostQueriesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadRequestErrorBody,
                        parse_obj_as(
                            type_=BadRequestErrorBody,
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

    async def get_a_list_of_a_recent_query_runs_for_the_current_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[QueryRunList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryRunList]
            Successfully operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "queries/runs",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryRunList,
                    parse_obj_as(
                        type_=QueryRunList,
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

    async def get_queries_query_id(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Query]:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Query]
            The Query was successfully retrieved
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Query,
                    parse_obj_as(
                        type_=Query,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def patch_queries_query_id(
        self,
        query_id: int,
        *,
        share: typing.Optional[bool] = None,
        star: typing.Optional[bool] = None,
        adminname: typing.Optional[str] = None,
        dashboardname: typing.Optional[str] = None,
        loginpagename: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        share : typing.Optional[bool]
            if true, the query will be shared. If false, it will be unshared

        star : typing.Optional[bool]
            if true, the query will be shared. If false, it will be unshared

        adminname : typing.Optional[str]
            The admin name to pin the query as. If the empty string, will be unpinned.

        dashboardname : typing.Optional[str]
            The admin name to pin the query to the dashboard as. If the empty string, will be unpinned.

        loginpagename : typing.Optional[str]
            The admin name to pin the query to the login page as. If the empty string, will be unpinned.

        name : typing.Optional[str]
            The name to set for the query for this user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}",
            method="PATCH",
            params={
                "share": share,
                "star": star,
                "adminname": adminname,
                "dashboardname": dashboardname,
                "loginpagename": loginpagename,
                "name": name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_queries_query_id_run(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[QueryRunList]:
        """
        Return a list of summarizing previous runs of this query

        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[QueryRunList]
            Successfully operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}/run",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    QueryRunList,
                    parse_obj_as(
                        type_=QueryRunList,
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

    @contextlib.asynccontextmanager
    async def post_queries_query_id_run(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Run the query QueryID and returns the results.

        This endpoint will result in a new query run being generated, which will be returned in the queries of the user on the /queries endpoint.

        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The query was able to be successfully run
        """
        async with self._client_wrapper.httpx_client.stream(
            f"queries/{encode_path_param(query_id)}/run",
            method="POST",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                typing.Any,
                                parse_obj_as(
                                    type_=typing.Any,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def get_queries_query_id_count(
        self, query_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetQueriesQueryIdCountResponse]:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetQueriesQueryIdCountResponse]
            A count of the number of candidate matches that would be returned if the query were to be run by the current user right now.

            This endpoint does *not* result in a new query run being generated or run the query, it only returns the count of how many candidates would match if the query *were* to be run.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}/count",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetQueriesQueryIdCountResponse,
                    parse_obj_as(
                        type_=GetQueriesQueryIdCountResponse,
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

    async def get_queries_query_id_run_query_run_id(
        self, query_id: int, query_run_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        query_id : int
            the QueryID returned by posting to /queries

        query_run_id : int
            the identifier of a previous run for this QueryID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"queries/{encode_path_param(query_id)}/run/{encode_path_param(query_run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
