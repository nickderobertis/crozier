

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
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..types.envelope_computation_get import EnvelopeComputationGet
from ..types.job_encryption_context_metadata import JobEncryptionContextMetadata
from ..types.page_computation_collection_run_rest_get import PageComputationCollectionRunRestGet
from ..types.page_computation_collection_run_task_rest_get import PageComputationCollectionRunTaskRestGet
from ..types.page_computation_run_rest_get import PageComputationRunRestGet
from ..types.page_computation_task_rest_get import PageComputationTaskRestGet
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawComputationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_computation(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeComputationGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeComputationGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeComputationGet,
                    parse_obj_as(
                        type_=EnvelopeComputationGet,
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

    def start_computation(
        self,
        project_id: str,
        *,
        force_restart: typing.Optional[bool] = OMIT,
        subgraph: typing.Optional[typing.Sequence[str]] = OMIT,
        encryption: typing.Optional[JobEncryptionContextMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeComputationGet]:
        """
        Parameters
        ----------
        project_id : str

        force_restart : typing.Optional[bool]

        subgraph : typing.Optional[typing.Sequence[str]]

        encryption : typing.Optional[JobEncryptionContextMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeComputationGet]
            Pipeline is up-to-date, nothing was started
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}:start",
            method="POST",
            json={
                "force_restart": force_restart,
                "subgraph": subgraph,
                "encryption": convert_and_respect_annotation_metadata(
                    object_=encryption, annotation=typing.Optional[JobEncryptionContextMetadata], direction="write"
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
                    EnvelopeComputationGet,
                    parse_obj_as(
                        type_=EnvelopeComputationGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 402:
                raise PaymentRequiredError(
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    def stop_computation(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}:stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_computations_latest_iteration(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter_only_running: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageComputationRunRestGet]:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        filter_only_running : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageComputationRunRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/computations/-/iterations/latest",
            method="GET",
            params={
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "filter_only_running": filter_only_running,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationRunRestGet,
                    parse_obj_as(
                        type_=PageComputationRunRestGet,
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

    def list_computation_iterations(
        self,
        project_id: str,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_children: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageComputationRunRestGet]:
        """
        Parameters
        ----------
        project_id : str

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        include_children : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageComputationRunRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}/iterations",
            method="GET",
            params={
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "include_children": include_children,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationRunRestGet,
                    parse_obj_as(
                        type_=PageComputationRunRestGet,
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

    def list_computations_latest_iteration_tasks(
        self,
        project_id: str,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_children: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageComputationTaskRestGet]:
        """
        Parameters
        ----------
        project_id : str

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        include_children : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageComputationTaskRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}/iterations/latest/tasks",
            method="GET",
            params={
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "include_children": include_children,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationTaskRestGet,
                    parse_obj_as(
                        type_=PageComputationTaskRestGet,
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

    def list_computation_collection_runs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter_only_running: typing.Optional[bool] = None,
        filter_by_root_project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageComputationCollectionRunRestGet]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        filter_only_running : typing.Optional[bool]

        filter_by_root_project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageComputationCollectionRunRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/computation-collection-runs",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "filter_only_running": filter_only_running,
                "filter_by_root_project_id": filter_by_root_project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationCollectionRunRestGet,
                    parse_obj_as(
                        type_=PageComputationCollectionRunRestGet,
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

    def list_computation_collection_run_tasks(
        self,
        collection_run_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PageComputationCollectionRunTaskRestGet]:
        """
        Parameters
        ----------
        collection_run_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PageComputationCollectionRunTaskRestGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/computation-collection-runs/{encode_path_param(collection_run_id)}/tasks",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationCollectionRunTaskRestGet,
                    parse_obj_as(
                        type_=PageComputationCollectionRunTaskRestGet,
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


class AsyncRawComputationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_computation(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeComputationGet]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeComputationGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeComputationGet,
                    parse_obj_as(
                        type_=EnvelopeComputationGet,
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

    async def start_computation(
        self,
        project_id: str,
        *,
        force_restart: typing.Optional[bool] = OMIT,
        subgraph: typing.Optional[typing.Sequence[str]] = OMIT,
        encryption: typing.Optional[JobEncryptionContextMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeComputationGet]:
        """
        Parameters
        ----------
        project_id : str

        force_restart : typing.Optional[bool]

        subgraph : typing.Optional[typing.Sequence[str]]

        encryption : typing.Optional[JobEncryptionContextMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeComputationGet]
            Pipeline is up-to-date, nothing was started
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}:start",
            method="POST",
            json={
                "force_restart": force_restart,
                "subgraph": subgraph,
                "encryption": convert_and_respect_annotation_metadata(
                    object_=encryption, annotation=typing.Optional[JobEncryptionContextMetadata], direction="write"
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
                    EnvelopeComputationGet,
                    parse_obj_as(
                        type_=EnvelopeComputationGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 402:
                raise PaymentRequiredError(
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
            if _response.status_code == 503:
                raise ServiceUnavailableError(
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

    async def stop_computation(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}:stop",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_computations_latest_iteration(
        self,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter_only_running: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageComputationRunRestGet]:
        """
        Parameters
        ----------
        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        filter_only_running : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageComputationRunRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/computations/-/iterations/latest",
            method="GET",
            params={
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "filter_only_running": filter_only_running,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationRunRestGet,
                    parse_obj_as(
                        type_=PageComputationRunRestGet,
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

    async def list_computation_iterations(
        self,
        project_id: str,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_children: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageComputationRunRestGet]:
        """
        Parameters
        ----------
        project_id : str

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        include_children : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageComputationRunRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}/iterations",
            method="GET",
            params={
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "include_children": include_children,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationRunRestGet,
                    parse_obj_as(
                        type_=PageComputationRunRestGet,
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

    async def list_computations_latest_iteration_tasks(
        self,
        project_id: str,
        *,
        order_by: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        include_children: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageComputationTaskRestGet]:
        """
        Parameters
        ----------
        project_id : str

        order_by : typing.Optional[str]

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        include_children : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageComputationTaskRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/computations/{encode_path_param(project_id)}/iterations/latest/tasks",
            method="GET",
            params={
                "order_by": order_by,
                "limit": limit,
                "offset": offset,
                "include_children": include_children,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationTaskRestGet,
                    parse_obj_as(
                        type_=PageComputationTaskRestGet,
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

    async def list_computation_collection_runs(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        filter_only_running: typing.Optional[bool] = None,
        filter_by_root_project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageComputationCollectionRunRestGet]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        filter_only_running : typing.Optional[bool]

        filter_by_root_project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageComputationCollectionRunRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/computation-collection-runs",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "filter_only_running": filter_only_running,
                "filter_by_root_project_id": filter_by_root_project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationCollectionRunRestGet,
                    parse_obj_as(
                        type_=PageComputationCollectionRunRestGet,
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

    async def list_computation_collection_run_tasks(
        self,
        collection_run_id: str,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PageComputationCollectionRunTaskRestGet]:
        """
        Parameters
        ----------
        collection_run_id : str

        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PageComputationCollectionRunTaskRestGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/computation-collection-runs/{encode_path_param(collection_run_id)}/tasks",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PageComputationCollectionRunTaskRestGet,
                    parse_obj_as(
                        type_=PageComputationCollectionRunTaskRestGet,
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
