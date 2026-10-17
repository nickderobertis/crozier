

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
from ..errors.bad_gateway_error import BadGatewayError
from ..errors.conflict_error import ConflictError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.bad_gateway_error_body import BadGatewayErrorBody
from ..types.list_experiments_request_started_after import ListExperimentsRequestStartedAfter
from ..types.list_experiments_request_started_before import ListExperimentsRequestStartedBefore
from .types.delete_experiment_response import DeleteExperimentResponse
from .types.get_active_experiment_response import GetActiveExperimentResponse
from .types.get_experiment_response import GetExperimentResponse
from .types.list_experiments_request_status import ListExperimentsRequestStatus
from .types.list_experiments_response import ListExperimentsResponse
from .types.start_experiment_response import StartExperimentResponse
from .types.stop_experiment_response import StopExperimentResponse
from .types.update_experiment_response import UpdateExperimentResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawExperimentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_experiments(
        self,
        *,
        system_id: typing.Optional[str] = None,
        channel: typing.Optional[float] = None,
        status: typing.Optional[ListExperimentsRequestStatus] = None,
        name_contains: typing.Optional[str] = None,
        started_after: typing.Optional[ListExperimentsRequestStartedAfter] = None,
        started_before: typing.Optional[ListExperimentsRequestStartedBefore] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListExperimentsResponse]:
        """
        List experiments with optional filters by system, channel, status, name, and start-time range. Sorted by startedAt desc.

        Parameters
        ----------
        system_id : typing.Optional[str]

        channel : typing.Optional[float]

        status : typing.Optional[ListExperimentsRequestStatus]

        name_contains : typing.Optional[str]

        started_after : typing.Optional[ListExperimentsRequestStartedAfter]

        started_before : typing.Optional[ListExperimentsRequestStartedBefore]

        limit : typing.Optional[float]

        offset : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListExperimentsResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            "experiments/",
            method="GET",
            params={
                "systemId": system_id,
                "channel": channel,
                "status": status,
                "nameContains": name_contains,
                "startedAfter": convert_and_respect_annotation_metadata(
                    object_=started_after, annotation=ListExperimentsRequestStartedAfter, direction="write"
                ),
                "startedBefore": convert_and_respect_annotation_metadata(
                    object_=started_before, annotation=ListExperimentsRequestStartedBefore, direction="write"
                ),
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListExperimentsResponse,
                    parse_obj_as(
                        type_=ListExperimentsResponse,
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

    def start_experiment(
        self,
        *,
        name: str,
        system_id: str,
        channel: float,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StartExperimentResponse]:
        """
        Create an experiment and start the PID loop. Captures setpoint and Kp/Ki/Kd as the experiment's start snapshot. Refuses if PID is already active or another experiment is running on the same channel.

        Parameters
        ----------
        name : str
            Experiment name

        system_id : str

        channel : float

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StartExperimentResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            "experiments/",
            method="POST",
            json={
                "name": name,
                "systemId": system_id,
                "channel": channel,
                "notes": notes,
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
                    StartExperimentResponse,
                    parse_obj_as(
                        type_=StartExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 409:
                raise ConflictError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadGatewayErrorBody,
                        parse_obj_as(
                            type_=BadGatewayErrorBody,
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

    def get_active_experiment(
        self, *, system_id: str, channel: float, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetActiveExperimentResponse]:
        """
        Return the currently running experiment for a given (systemId, channel), or null if none.

        Parameters
        ----------
        system_id : str

        channel : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetActiveExperimentResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            "experiments/active",
            method="GET",
            params={
                "systemId": system_id,
                "channel": channel,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetActiveExperimentResponse,
                    parse_obj_as(
                        type_=GetActiveExperimentResponse,
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

    def get_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetExperimentResponse]:
        """
        Get a single experiment by id.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetExperimentResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"experiments/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetExperimentResponse,
                    parse_obj_as(
                        type_=GetExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteExperimentResponse]:
        """
        Delete a non-running experiment. Refuses to delete a running one.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteExperimentResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"experiments/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteExperimentResponse,
                    parse_obj_as(
                        type_=DeleteExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 409:
                raise ConflictError(
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

    def update_experiment(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateExperimentResponse]:
        """
        Update an experiment's name or notes (no other fields).

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateExperimentResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"experiments/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "notes": notes,
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
                    UpdateExperimentResponse,
                    parse_obj_as(
                        type_=UpdateExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def stop_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StopExperimentResponse]:
        """
        Stop a running experiment. Calls the heater PID stop endpoint and finalizes the experiment row.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StopExperimentResponse]
            Response for status 200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"experiments/{encode_path_param(id)}/stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StopExperimentResponse,
                    parse_obj_as(
                        type_=StopExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawExperimentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_experiments(
        self,
        *,
        system_id: typing.Optional[str] = None,
        channel: typing.Optional[float] = None,
        status: typing.Optional[ListExperimentsRequestStatus] = None,
        name_contains: typing.Optional[str] = None,
        started_after: typing.Optional[ListExperimentsRequestStartedAfter] = None,
        started_before: typing.Optional[ListExperimentsRequestStartedBefore] = None,
        limit: typing.Optional[float] = None,
        offset: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListExperimentsResponse]:
        """
        List experiments with optional filters by system, channel, status, name, and start-time range. Sorted by startedAt desc.

        Parameters
        ----------
        system_id : typing.Optional[str]

        channel : typing.Optional[float]

        status : typing.Optional[ListExperimentsRequestStatus]

        name_contains : typing.Optional[str]

        started_after : typing.Optional[ListExperimentsRequestStartedAfter]

        started_before : typing.Optional[ListExperimentsRequestStartedBefore]

        limit : typing.Optional[float]

        offset : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListExperimentsResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experiments/",
            method="GET",
            params={
                "systemId": system_id,
                "channel": channel,
                "status": status,
                "nameContains": name_contains,
                "startedAfter": convert_and_respect_annotation_metadata(
                    object_=started_after, annotation=ListExperimentsRequestStartedAfter, direction="write"
                ),
                "startedBefore": convert_and_respect_annotation_metadata(
                    object_=started_before, annotation=ListExperimentsRequestStartedBefore, direction="write"
                ),
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListExperimentsResponse,
                    parse_obj_as(
                        type_=ListExperimentsResponse,
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

    async def start_experiment(
        self,
        *,
        name: str,
        system_id: str,
        channel: float,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StartExperimentResponse]:
        """
        Create an experiment and start the PID loop. Captures setpoint and Kp/Ki/Kd as the experiment's start snapshot. Refuses if PID is already active or another experiment is running on the same channel.

        Parameters
        ----------
        name : str
            Experiment name

        system_id : str

        channel : float

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StartExperimentResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experiments/",
            method="POST",
            json={
                "name": name,
                "systemId": system_id,
                "channel": channel,
                "notes": notes,
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
                    StartExperimentResponse,
                    parse_obj_as(
                        type_=StartExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 409:
                raise ConflictError(
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 502:
                raise BadGatewayError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        BadGatewayErrorBody,
                        parse_obj_as(
                            type_=BadGatewayErrorBody,
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

    async def get_active_experiment(
        self, *, system_id: str, channel: float, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetActiveExperimentResponse]:
        """
        Return the currently running experiment for a given (systemId, channel), or null if none.

        Parameters
        ----------
        system_id : str

        channel : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetActiveExperimentResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "experiments/active",
            method="GET",
            params={
                "systemId": system_id,
                "channel": channel,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetActiveExperimentResponse,
                    parse_obj_as(
                        type_=GetActiveExperimentResponse,
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

    async def get_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetExperimentResponse]:
        """
        Get a single experiment by id.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetExperimentResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"experiments/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetExperimentResponse,
                    parse_obj_as(
                        type_=GetExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteExperimentResponse]:
        """
        Delete a non-running experiment. Refuses to delete a running one.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteExperimentResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"experiments/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteExperimentResponse,
                    parse_obj_as(
                        type_=DeleteExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 409:
                raise ConflictError(
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

    async def update_experiment(
        self,
        id: str,
        *,
        name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateExperimentResponse]:
        """
        Update an experiment's name or notes (no other fields).

        Parameters
        ----------
        id : str

        name : typing.Optional[str]

        notes : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateExperimentResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"experiments/{encode_path_param(id)}",
            method="PATCH",
            json={
                "name": name,
                "notes": notes,
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
                    UpdateExperimentResponse,
                    parse_obj_as(
                        type_=UpdateExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def stop_experiment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StopExperimentResponse]:
        """
        Stop a running experiment. Calls the heater PID stop endpoint and finalizes the experiment row.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StopExperimentResponse]
            Response for status 200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"experiments/{encode_path_param(id)}/stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StopExperimentResponse,
                    parse_obj_as(
                        type_=StopExperimentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
