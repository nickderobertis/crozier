

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
from ..types.app_limit_param import AppLimitParam
from ..types.dataset import Dataset
from ..types.dataset_id_param import DatasetIdParam
from ..types.dataset_name import DatasetName
from ..types.ending_before import EndingBefore
from ..types.feedback_dataset_item import FeedbackDatasetItem
from ..types.feedback_response_schema import FeedbackResponseSchema
from ..types.fetch_dataset_events_response import FetchDatasetEventsResponse
from ..types.fetch_limit import FetchLimit
from ..types.fetch_limit_param import FetchLimitParam
from ..types.fetch_pagination_cursor import FetchPaginationCursor
from ..types.ids import Ids
from ..types.insert_dataset_event import InsertDatasetEvent
from ..types.insert_events_response import InsertEventsResponse
from ..types.max_root_span_id import MaxRootSpanId
from ..types.max_xact_id import MaxXactId
from ..types.org_name import OrgName
from ..types.project_id_query import ProjectIdQuery
from ..types.project_name import ProjectName
from ..types.starting_after import StartingAfter
from ..types.summarize_data import SummarizeData
from ..types.summarize_dataset_response import SummarizeDatasetResponse
from ..types.version import Version
from .types.get_dataset_response import GetDatasetResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDatasetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_dataset(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        dataset_name: typing.Optional[DatasetName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDatasetResponse]:
        """
        List out all datasets. The datasets are sorted by creation date, with the most recently-created datasets coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        dataset_name : typing.Optional[DatasetName]
            Name of the dataset to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDatasetResponse]
            Returns a list of dataset objects
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/dataset",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "dataset_name": dataset_name,
                "project_name": project_name,
                "project_id": project_id,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDatasetResponse,
                    parse_obj_as(
                        type_=GetDatasetResponse,
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

    def post_dataset(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dataset]:
        """
        Create a new dataset. If there is an existing dataset in the project with the same name as the one specified in the request, will return the existing dataset unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the dataset belongs under

        name : str
            Name of the dataset. Within a project, dataset names are unique

        description : typing.Optional[str]
            Textual description of the dataset

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the dataset

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            User-controlled metadata about the dataset

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dataset]
            Returns the new dataset object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/dataset",
            method="POST",
            json={
                "project_id": project_id,
                "name": name,
                "description": description,
                "tags": tags,
                "metadata": metadata,
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
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    def get_dataset_id(
        self, dataset_id: DatasetIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dataset]:
        """
        Get a dataset object by its id

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dataset]
            Returns the dataset object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    def delete_dataset_id(
        self, dataset_id: DatasetIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Dataset]:
        """
        Delete a dataset object by its id

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dataset]
            Returns the deleted dataset object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    def patch_dataset_id(
        self,
        dataset_id: DatasetIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Dataset]:
        """
        Partially update a dataset object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        name : typing.Optional[str]
            Name of the dataset. Within a project, dataset names are unique

        description : typing.Optional[str]
            Textual description of the dataset

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the dataset

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            User-controlled metadata about the dataset

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Dataset]
            Returns the dataset object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "tags": tags,
                "metadata": metadata,
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
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    def post_dataset_id_insert(
        self,
        dataset_id: DatasetIdParam,
        *,
        events: typing.Sequence[InsertDatasetEvent],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InsertEventsResponse]:
        """
        Insert a set of events into the dataset

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        events : typing.Sequence[InsertDatasetEvent]
            A list of dataset events to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InsertEventsResponse]
            Returns the inserted row ids
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/insert",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[InsertDatasetEvent], direction="write"
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

    def get_dataset_id_fetch(
        self,
        dataset_id: DatasetIdParam,
        *,
        limit: typing.Optional[FetchLimitParam] = None,
        max_xact_id: typing.Optional[MaxXactId] = None,
        max_root_span_id: typing.Optional[MaxRootSpanId] = None,
        version: typing.Optional[Version] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FetchDatasetEventsResponse]:
        """
        Fetch the events in a dataset. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

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
        HttpResponse[FetchDatasetEventsResponse]
            Returns the fetched rows
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/fetch",
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
                    FetchDatasetEventsResponse,
                    parse_obj_as(
                        type_=FetchDatasetEventsResponse,
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

    def post_dataset_id_fetch(
        self,
        dataset_id: DatasetIdParam,
        *,
        limit: typing.Optional[FetchLimit] = OMIT,
        cursor: typing.Optional[FetchPaginationCursor] = OMIT,
        max_xact_id: typing.Optional[MaxXactId] = OMIT,
        max_root_span_id: typing.Optional[MaxRootSpanId] = OMIT,
        version: typing.Optional[Version] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FetchDatasetEventsResponse]:
        """
        Fetch the events in a dataset. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        limit : typing.Optional[FetchLimit]

        cursor : typing.Optional[FetchPaginationCursor]

        max_xact_id : typing.Optional[MaxXactId]

        max_root_span_id : typing.Optional[MaxRootSpanId]

        version : typing.Optional[Version]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FetchDatasetEventsResponse]
            Returns the fetched rows
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/fetch",
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
                    FetchDatasetEventsResponse,
                    parse_obj_as(
                        type_=FetchDatasetEventsResponse,
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

    def post_dataset_id_feedback(
        self,
        dataset_id: DatasetIdParam,
        *,
        feedback: typing.Sequence[FeedbackDatasetItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FeedbackResponseSchema]:
        """
        Log feedback for a set of dataset events

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        feedback : typing.Sequence[FeedbackDatasetItem]
            A list of dataset feedback items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FeedbackResponseSchema]
            Returns a success status
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/feedback",
            method="POST",
            json={
                "feedback": convert_and_respect_annotation_metadata(
                    object_=feedback, annotation=typing.Sequence[FeedbackDatasetItem], direction="write"
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

    def get_dataset_id_summarize(
        self,
        dataset_id: DatasetIdParam,
        *,
        summarize_data: typing.Optional[SummarizeData] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SummarizeDatasetResponse]:
        """
        Summarize dataset

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        summarize_data : typing.Optional[SummarizeData]
            Whether to summarize the data. If false (or omitted), only the metadata will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SummarizeDatasetResponse]
            Dataset summary
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/summarize",
            method="GET",
            params={
                "summarize_data": summarize_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SummarizeDatasetResponse,
                    parse_obj_as(
                        type_=SummarizeDatasetResponse,
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


class AsyncRawDatasetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_dataset(
        self,
        *,
        limit: typing.Optional[AppLimitParam] = None,
        starting_after: typing.Optional[StartingAfter] = None,
        ending_before: typing.Optional[EndingBefore] = None,
        ids: typing.Optional[Ids] = None,
        dataset_name: typing.Optional[DatasetName] = None,
        project_name: typing.Optional[ProjectName] = None,
        project_id: typing.Optional[ProjectIdQuery] = None,
        org_name: typing.Optional[OrgName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDatasetResponse]:
        """
        List out all datasets. The datasets are sorted by creation date, with the most recently-created datasets coming first

        Parameters
        ----------
        limit : typing.Optional[AppLimitParam]
            Limit the number of objects to return

        starting_after : typing.Optional[StartingAfter]
            Pagination cursor id.

            For example, if the final item in the last page you fetched had an id of `foo`, pass `starting_after=foo` to fetch the next page. Note: you may only pass one of `starting_after` and `ending_before`

        ending_before : typing.Optional[EndingBefore]
            Pagination cursor id.

            For example, if the initial item in the last page you fetched had an id of `foo`, pass `ending_before=foo` to fetch the previous page. Note: you may only pass one of `starting_after` and `ending_before`

        ids : typing.Optional[Ids]
            Filter search results to a particular set of object IDs. To specify a list of IDs, include the query param multiple times

        dataset_name : typing.Optional[DatasetName]
            Name of the dataset to search for

        project_name : typing.Optional[ProjectName]
            Name of the project to search for

        project_id : typing.Optional[ProjectIdQuery]
            Project id

        org_name : typing.Optional[OrgName]
            Filter search results to within a particular organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDatasetResponse]
            Returns a list of dataset objects
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/dataset",
            method="GET",
            params={
                "limit": limit,
                "starting_after": starting_after,
                "ending_before": ending_before,
                "ids": convert_and_respect_annotation_metadata(object_=ids, annotation=Ids, direction="write"),
                "dataset_name": dataset_name,
                "project_name": project_name,
                "project_id": project_id,
                "org_name": org_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDatasetResponse,
                    parse_obj_as(
                        type_=GetDatasetResponse,
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

    async def post_dataset(
        self,
        *,
        project_id: str,
        name: str,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dataset]:
        """
        Create a new dataset. If there is an existing dataset in the project with the same name as the one specified in the request, will return the existing dataset unmodified

        Parameters
        ----------
        project_id : str
            Unique identifier for the project that the dataset belongs under

        name : str
            Name of the dataset. Within a project, dataset names are unique

        description : typing.Optional[str]
            Textual description of the dataset

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the dataset

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            User-controlled metadata about the dataset

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dataset]
            Returns the new dataset object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/dataset",
            method="POST",
            json={
                "project_id": project_id,
                "name": name,
                "description": description,
                "tags": tags,
                "metadata": metadata,
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
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    async def get_dataset_id(
        self, dataset_id: DatasetIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dataset]:
        """
        Get a dataset object by its id

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dataset]
            Returns the dataset object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    async def delete_dataset_id(
        self, dataset_id: DatasetIdParam, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Dataset]:
        """
        Delete a dataset object by its id

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dataset]
            Returns the deleted dataset object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    async def patch_dataset_id(
        self,
        dataset_id: DatasetIdParam,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Dataset]:
        """
        Partially update a dataset object. Specify the fields to update in the payload. Any object-type fields will be deep-merged with existing content. Currently we do not support removing fields or setting them to null.

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        name : typing.Optional[str]
            Name of the dataset. Within a project, dataset names are unique

        description : typing.Optional[str]
            Textual description of the dataset

        tags : typing.Optional[typing.Sequence[str]]
            A list of tags for the dataset

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            User-controlled metadata about the dataset

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Dataset]
            Returns the dataset object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}",
            method="PATCH",
            json={
                "name": name,
                "description": description,
                "tags": tags,
                "metadata": metadata,
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
                    Dataset,
                    parse_obj_as(
                        type_=Dataset,
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

    async def post_dataset_id_insert(
        self,
        dataset_id: DatasetIdParam,
        *,
        events: typing.Sequence[InsertDatasetEvent],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InsertEventsResponse]:
        """
        Insert a set of events into the dataset

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        events : typing.Sequence[InsertDatasetEvent]
            A list of dataset events to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InsertEventsResponse]
            Returns the inserted row ids
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/insert",
            method="POST",
            json={
                "events": convert_and_respect_annotation_metadata(
                    object_=events, annotation=typing.Sequence[InsertDatasetEvent], direction="write"
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

    async def get_dataset_id_fetch(
        self,
        dataset_id: DatasetIdParam,
        *,
        limit: typing.Optional[FetchLimitParam] = None,
        max_xact_id: typing.Optional[MaxXactId] = None,
        max_root_span_id: typing.Optional[MaxRootSpanId] = None,
        version: typing.Optional[Version] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FetchDatasetEventsResponse]:
        """
        Fetch the events in a dataset. Equivalent to the POST form of the same path, but with the parameters in the URL query rather than in the request body. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

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
        AsyncHttpResponse[FetchDatasetEventsResponse]
            Returns the fetched rows
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/fetch",
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
                    FetchDatasetEventsResponse,
                    parse_obj_as(
                        type_=FetchDatasetEventsResponse,
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

    async def post_dataset_id_fetch(
        self,
        dataset_id: DatasetIdParam,
        *,
        limit: typing.Optional[FetchLimit] = OMIT,
        cursor: typing.Optional[FetchPaginationCursor] = OMIT,
        max_xact_id: typing.Optional[MaxXactId] = OMIT,
        max_root_span_id: typing.Optional[MaxRootSpanId] = OMIT,
        version: typing.Optional[Version] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FetchDatasetEventsResponse]:
        """
        Fetch the events in a dataset. Equivalent to the GET form of the same path, but with the parameters in the request body rather than in the URL query. For more complex queries, use the `POST /btql` endpoint.

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        limit : typing.Optional[FetchLimit]

        cursor : typing.Optional[FetchPaginationCursor]

        max_xact_id : typing.Optional[MaxXactId]

        max_root_span_id : typing.Optional[MaxRootSpanId]

        version : typing.Optional[Version]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FetchDatasetEventsResponse]
            Returns the fetched rows
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/fetch",
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
                    FetchDatasetEventsResponse,
                    parse_obj_as(
                        type_=FetchDatasetEventsResponse,
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

    async def post_dataset_id_feedback(
        self,
        dataset_id: DatasetIdParam,
        *,
        feedback: typing.Sequence[FeedbackDatasetItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FeedbackResponseSchema]:
        """
        Log feedback for a set of dataset events

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        feedback : typing.Sequence[FeedbackDatasetItem]
            A list of dataset feedback items

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FeedbackResponseSchema]
            Returns a success status
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/feedback",
            method="POST",
            json={
                "feedback": convert_and_respect_annotation_metadata(
                    object_=feedback, annotation=typing.Sequence[FeedbackDatasetItem], direction="write"
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

    async def get_dataset_id_summarize(
        self,
        dataset_id: DatasetIdParam,
        *,
        summarize_data: typing.Optional[SummarizeData] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SummarizeDatasetResponse]:
        """
        Summarize dataset

        Parameters
        ----------
        dataset_id : DatasetIdParam
            Dataset id

        summarize_data : typing.Optional[SummarizeData]
            Whether to summarize the data. If false (or omitted), only the metadata will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SummarizeDatasetResponse]
            Dataset summary
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/dataset/{encode_path_param(dataset_id)}/summarize",
            method="GET",
            params={
                "summarize_data": summarize_data,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SummarizeDatasetResponse,
                    parse_obj_as(
                        type_=SummarizeDatasetResponse,
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
