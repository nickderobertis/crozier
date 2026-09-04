

import json
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param, jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..types.job_history_page import JobHistoryPage
from ..types.job_ref import JobRef
from ..types.stage_input_descriptor import StageInputDescriptor
from ..types.stage_response import StageResponse
from ..types.task_spec import TaskSpec
from ..types.task_summary import TaskSummary
from .types.run_task_request_values_value import RunTaskRequestValuesValue
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContextClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tasks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TaskSummary]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TaskSummary]]
            The available tasks as advisory summaries.
        """
        _response = self._client_wrapper.httpx_client.request(
            "tasks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TaskSummary],
                    parse_obj_as(
                        type_=typing.List[TaskSummary],
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

    def get_task_spec(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TaskSpec]:
        """
        Parameters
        ----------
        task_id : str
            Opaque task identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskSpec]
            The task's neutral task spec.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tasks/{encode_path_param(task_id)}/spec",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskSpec,
                    parse_obj_as(
                        type_=TaskSpec,
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

    def run_task(
        self,
        task_id: str,
        *,
        values: typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobRef]:
        """
        Parameters
        ----------
        task_id : str
            Opaque task identifier.

        values : typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobRef]
            The submitted job handle.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"tasks/{encode_path_param(task_id)}/run",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]],
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
                    JobRef,
                    parse_obj_as(
                        type_=JobRef,
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

    def list_job_history(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JobHistoryPage]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]
            Opaque continuation cursor returned by the prior page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JobHistoryPage]
            One bounded lightweight page; logs and parameters are absent.
        """
        _response = self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobHistoryPage,
                    parse_obj_as(
                        type_=JobHistoryPage,
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

    def stage_input(
        self,
        *,
        file: core.File,
        descriptor: StageInputDescriptor,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StageResponse]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        descriptor : StageInputDescriptor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StageResponse]
            The backend-minted URIs for the staged bytes.
        """
        _response = self._client_wrapper.httpx_client.request(
            "stage",
            method="POST",
            data={},
            files={
                "file": file,
                "descriptor": (None, json.dumps(jsonable_encoder(descriptor)), "text/plain"),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageResponse,
                    parse_obj_as(
                        type_=StageResponse,
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


class AsyncRawContextClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_tasks(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TaskSummary]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TaskSummary]]
            The available tasks as advisory summaries.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "tasks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TaskSummary],
                    parse_obj_as(
                        type_=typing.List[TaskSummary],
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

    async def get_task_spec(
        self, task_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TaskSpec]:
        """
        Parameters
        ----------
        task_id : str
            Opaque task identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskSpec]
            The task's neutral task spec.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tasks/{encode_path_param(task_id)}/spec",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskSpec,
                    parse_obj_as(
                        type_=TaskSpec,
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

    async def run_task(
        self,
        task_id: str,
        *,
        values: typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobRef]:
        """
        Parameters
        ----------
        task_id : str
            Opaque task identifier.

        values : typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobRef]
            The submitted job handle.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"tasks/{encode_path_param(task_id)}/run",
            method="POST",
            json={
                "values": convert_and_respect_annotation_metadata(
                    object_=values,
                    annotation=typing.Dict[str, typing.Optional[RunTaskRequestValuesValue]],
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
                    JobRef,
                    parse_obj_as(
                        type_=JobRef,
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

    async def list_job_history(
        self,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JobHistoryPage]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        cursor : typing.Optional[str]
            Opaque continuation cursor returned by the prior page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JobHistoryPage]
            One bounded lightweight page; logs and parameters are absent.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "jobs",
            method="GET",
            params={
                "limit": limit,
                "cursor": cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JobHistoryPage,
                    parse_obj_as(
                        type_=JobHistoryPage,
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

    async def stage_input(
        self,
        *,
        file: core.File,
        descriptor: StageInputDescriptor,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StageResponse]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        descriptor : StageInputDescriptor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StageResponse]
            The backend-minted URIs for the staged bytes.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "stage",
            method="POST",
            data={},
            files={
                "file": file,
                "descriptor": (None, json.dumps(jsonable_encoder(descriptor)), "text/plain"),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageResponse,
                    parse_obj_as(
                        type_=StageResponse,
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
