

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
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.create_score_response import CreateScoreResponse
from ..types.create_score_value import CreateScoreValue
from ..types.get_scores_response import GetScoresResponse
from ..types.score import Score
from ..types.score_data_type import ScoreDataType
from ..types.score_source import ScoreSource
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawScoreClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        source: typing.Optional[ScoreSource] = None,
        operator: typing.Optional[str] = None,
        value: typing.Optional[float] = None,
        score_ids: typing.Optional[str] = None,
        config_id: typing.Optional[str] = None,
        queue_id: typing.Optional[str] = None,
        data_type: typing.Optional[ScoreDataType] = None,
        trace_tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetScoresResponse]:
        """
        Get a list of scores

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1.

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        user_id : typing.Optional[str]
            Retrieve only scores with this userId associated to the trace.

        name : typing.Optional[str]
            Retrieve only scores with this name.

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include scores created on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include scores created before a certain datetime (ISO 8601)

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for scores where the environment is one of the provided values.

        source : typing.Optional[ScoreSource]
            Retrieve only scores from a specific source.

        operator : typing.Optional[str]
            Retrieve only scores with <operator> value.

        value : typing.Optional[float]
            Retrieve only scores with <operator> value.

        score_ids : typing.Optional[str]
            Comma-separated list of score IDs to limit the results to.

        config_id : typing.Optional[str]
            Retrieve only scores with a specific configId.

        queue_id : typing.Optional[str]
            Retrieve only scores with a specific annotation queueId.

        data_type : typing.Optional[ScoreDataType]
            Retrieve only scores with a specific dataType.

        trace_tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Only scores linked to traces that include all of these tags will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetScoresResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "api/public/scores",
            method="GET",
            params={
                "page": page,
                "limit": limit,
                "userId": user_id,
                "name": name,
                "fromTimestamp": serialize_datetime(from_timestamp) if from_timestamp is not None else None,
                "toTimestamp": serialize_datetime(to_timestamp) if to_timestamp is not None else None,
                "environment": environment,
                "source": source,
                "operator": operator,
                "value": value,
                "scoreIds": score_ids,
                "configId": config_id,
                "queueId": queue_id,
                "dataType": data_type,
                "traceTags": trace_tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetScoresResponse,
                    parse_obj_as(
                        type_=GetScoresResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create(
        self,
        *,
        trace_id: str,
        name: str,
        value: CreateScoreValue,
        id: typing.Optional[str] = OMIT,
        observation_id: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        environment: typing.Optional[str] = OMIT,
        data_type: typing.Optional[ScoreDataType] = OMIT,
        config_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateScoreResponse]:
        """
        Create a score

        Parameters
        ----------
        trace_id : str

        name : str

        value : CreateScoreValue
            The value of the score. Must be passed as string for categorical scores, and numeric for boolean and numeric scores. Boolean score values must equal either 1 or 0 (true or false)

        id : typing.Optional[str]

        observation_id : typing.Optional[str]

        comment : typing.Optional[str]

        environment : typing.Optional[str]
            The environment of the score. Can be any lowercase alphanumeric string with hyphens and underscores that does not start with 'langfuse'.

        data_type : typing.Optional[ScoreDataType]
            The data type of the score. When passing a configId this field is inferred. Otherwise, this field must be passed or will default to numeric.

        config_id : typing.Optional[str]
            Reference a score config on a score. The unique langfuse identifier of a score config. When passing this field, the dataType and stringValue fields are automatically populated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateScoreResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "api/public/scores",
            method="POST",
            json={
                "id": id,
                "traceId": trace_id,
                "name": name,
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=CreateScoreValue, direction="write"
                ),
                "observationId": observation_id,
                "comment": comment,
                "environment": environment,
                "dataType": data_type,
                "configId": config_id,
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
                    CreateScoreResponse,
                    parse_obj_as(
                        type_=CreateScoreResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_by_id(
        self, score_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Score]:
        """
        Get a score

        Parameters
        ----------
        score_id : str
            The unique langfuse identifier of a score

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Score]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/scores/{encode_path_param(score_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Score,
                    parse_obj_as(
                        type_=Score,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete(self, score_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Delete a score

        Parameters
        ----------
        score_id : str
            The unique langfuse identifier of a score

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/public/scores/{encode_path_param(score_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawScoreClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        user_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        from_timestamp: typing.Optional[dt.datetime] = None,
        to_timestamp: typing.Optional[dt.datetime] = None,
        environment: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        source: typing.Optional[ScoreSource] = None,
        operator: typing.Optional[str] = None,
        value: typing.Optional[float] = None,
        score_ids: typing.Optional[str] = None,
        config_id: typing.Optional[str] = None,
        queue_id: typing.Optional[str] = None,
        data_type: typing.Optional[ScoreDataType] = None,
        trace_tags: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetScoresResponse]:
        """
        Get a list of scores

        Parameters
        ----------
        page : typing.Optional[int]
            Page number, starts at 1.

        limit : typing.Optional[int]
            Limit of items per page. If you encounter api issues due to too large page sizes, try to reduce the limit.

        user_id : typing.Optional[str]
            Retrieve only scores with this userId associated to the trace.

        name : typing.Optional[str]
            Retrieve only scores with this name.

        from_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include scores created on or after a certain datetime (ISO 8601)

        to_timestamp : typing.Optional[dt.datetime]
            Optional filter to only include scores created before a certain datetime (ISO 8601)

        environment : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Optional filter for scores where the environment is one of the provided values.

        source : typing.Optional[ScoreSource]
            Retrieve only scores from a specific source.

        operator : typing.Optional[str]
            Retrieve only scores with <operator> value.

        value : typing.Optional[float]
            Retrieve only scores with <operator> value.

        score_ids : typing.Optional[str]
            Comma-separated list of score IDs to limit the results to.

        config_id : typing.Optional[str]
            Retrieve only scores with a specific configId.

        queue_id : typing.Optional[str]
            Retrieve only scores with a specific annotation queueId.

        data_type : typing.Optional[ScoreDataType]
            Retrieve only scores with a specific dataType.

        trace_tags : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Only scores linked to traces that include all of these tags will be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetScoresResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/public/scores",
            method="GET",
            params={
                "page": page,
                "limit": limit,
                "userId": user_id,
                "name": name,
                "fromTimestamp": serialize_datetime(from_timestamp) if from_timestamp is not None else None,
                "toTimestamp": serialize_datetime(to_timestamp) if to_timestamp is not None else None,
                "environment": environment,
                "source": source,
                "operator": operator,
                "value": value,
                "scoreIds": score_ids,
                "configId": config_id,
                "queueId": queue_id,
                "dataType": data_type,
                "traceTags": trace_tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetScoresResponse,
                    parse_obj_as(
                        type_=GetScoresResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create(
        self,
        *,
        trace_id: str,
        name: str,
        value: CreateScoreValue,
        id: typing.Optional[str] = OMIT,
        observation_id: typing.Optional[str] = OMIT,
        comment: typing.Optional[str] = OMIT,
        environment: typing.Optional[str] = OMIT,
        data_type: typing.Optional[ScoreDataType] = OMIT,
        config_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateScoreResponse]:
        """
        Create a score

        Parameters
        ----------
        trace_id : str

        name : str

        value : CreateScoreValue
            The value of the score. Must be passed as string for categorical scores, and numeric for boolean and numeric scores. Boolean score values must equal either 1 or 0 (true or false)

        id : typing.Optional[str]

        observation_id : typing.Optional[str]

        comment : typing.Optional[str]

        environment : typing.Optional[str]
            The environment of the score. Can be any lowercase alphanumeric string with hyphens and underscores that does not start with 'langfuse'.

        data_type : typing.Optional[ScoreDataType]
            The data type of the score. When passing a configId this field is inferred. Otherwise, this field must be passed or will default to numeric.

        config_id : typing.Optional[str]
            Reference a score config on a score. The unique langfuse identifier of a score config. When passing this field, the dataType and stringValue fields are automatically populated.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateScoreResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/public/scores",
            method="POST",
            json={
                "id": id,
                "traceId": trace_id,
                "name": name,
                "value": convert_and_respect_annotation_metadata(
                    object_=value, annotation=CreateScoreValue, direction="write"
                ),
                "observationId": observation_id,
                "comment": comment,
                "environment": environment,
                "dataType": data_type,
                "configId": config_id,
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
                    CreateScoreResponse,
                    parse_obj_as(
                        type_=CreateScoreResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_by_id(
        self, score_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Score]:
        """
        Get a score

        Parameters
        ----------
        score_id : str
            The unique langfuse identifier of a score

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Score]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/scores/{encode_path_param(score_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Score,
                    parse_obj_as(
                        type_=Score,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete(
        self, score_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a score

        Parameters
        ----------
        score_id : str
            The unique langfuse identifier of a score

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/public/scores/{encode_path_param(score_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
