

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.cross_object_insert_response import CrossObjectInsertResponse
from .types.cross_object_insert_request_dataset_value import CrossObjectInsertRequestDatasetValue
from .types.cross_object_insert_request_experiment_value import CrossObjectInsertRequestExperimentValue
from .types.cross_object_insert_request_project_logs_value import CrossObjectInsertRequestProjectLogsValue
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCrossObjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_cross_object_insert(
        self,
        *,
        experiment: typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]] = OMIT,
        dataset: typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]] = OMIT,
        project_logs: typing.Optional[
            typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CrossObjectInsertResponse]:
        """
        Insert events and feedback across object types

        Parameters
        ----------
        experiment : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]]
            A mapping from experiment id to a set of log events and feedback items to insert

        dataset : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]]
            A mapping from dataset id to a set of log events and feedback items to insert

        project_logs : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]]
            A mapping from project id to a set of log events and feedback items to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CrossObjectInsertResponse]
            Returns the inserted row ids for the events on each individual object
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/insert",
            method="POST",
            json={
                "experiment": convert_and_respect_annotation_metadata(
                    object_=experiment,
                    annotation=typing.Optional[
                        typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]
                    ],
                    direction="write",
                ),
                "dataset": convert_and_respect_annotation_metadata(
                    object_=dataset,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]],
                    direction="write",
                ),
                "project_logs": convert_and_respect_annotation_metadata(
                    object_=project_logs,
                    annotation=typing.Optional[
                        typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]
                    ],
                    direction="write",
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
                    CrossObjectInsertResponse,
                    parse_obj_as(
                        type_=CrossObjectInsertResponse,
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


class AsyncRawCrossObjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_cross_object_insert(
        self,
        *,
        experiment: typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]] = OMIT,
        dataset: typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]] = OMIT,
        project_logs: typing.Optional[
            typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CrossObjectInsertResponse]:
        """
        Insert events and feedback across object types

        Parameters
        ----------
        experiment : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]]
            A mapping from experiment id to a set of log events and feedback items to insert

        dataset : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]]
            A mapping from dataset id to a set of log events and feedback items to insert

        project_logs : typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]]
            A mapping from project id to a set of log events and feedback items to insert

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CrossObjectInsertResponse]
            Returns the inserted row ids for the events on each individual object
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/insert",
            method="POST",
            json={
                "experiment": convert_and_respect_annotation_metadata(
                    object_=experiment,
                    annotation=typing.Optional[
                        typing.Dict[str, typing.Optional[CrossObjectInsertRequestExperimentValue]]
                    ],
                    direction="write",
                ),
                "dataset": convert_and_respect_annotation_metadata(
                    object_=dataset,
                    annotation=typing.Optional[typing.Dict[str, typing.Optional[CrossObjectInsertRequestDatasetValue]]],
                    direction="write",
                ),
                "project_logs": convert_and_respect_annotation_metadata(
                    object_=project_logs,
                    annotation=typing.Optional[
                        typing.Dict[str, typing.Optional[CrossObjectInsertRequestProjectLogsValue]]
                    ],
                    direction="write",
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
                    CrossObjectInsertResponse,
                    parse_obj_as(
                        type_=CrossObjectInsertResponse,
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
