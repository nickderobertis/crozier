

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.computation_get import ComputationGet
from ..types.job_encryption_context_metadata import JobEncryptionContextMetadata
from ..types.task_log_file_get import TaskLogFileGet
from ..types.tasks_outputs import TasksOutputs
from ..types.user_id_int import UserIdInt
from ..types.wallet_info_input import WalletInfoInput
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawComputationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_or_update_or_start_computation(
        self,
        *,
        user_id: UserIdInt,
        project_id: str,
        product_name: str,
        product_api_base_url: str,
        start_pipeline: typing.Optional[bool] = OMIT,
        subgraph: typing.Optional[typing.Sequence[str]] = OMIT,
        force_restart: typing.Optional[bool] = OMIT,
        simcore_user_agent: typing.Optional[str] = OMIT,
        use_on_demand_clusters: typing.Optional[bool] = OMIT,
        wallet_info: typing.Optional[WalletInfoInput] = OMIT,
        collection_run_id: typing.Optional[str] = OMIT,
        encryption: typing.Optional[JobEncryptionContextMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ComputationGet]:
        """
        Create and optionally start a new computation

        Parameters
        ----------
        user_id : UserIdInt

        project_id : str

        product_name : str

        product_api_base_url : str
            Base url of the product

        start_pipeline : typing.Optional[bool]
            if True the computation pipeline will start right away

        subgraph : typing.Optional[typing.Sequence[str]]
            An optional set of nodes that must be executed, if empty the whole pipeline is executed

        force_restart : typing.Optional[bool]
            if True will force re-running all dependent nodes

        simcore_user_agent : typing.Optional[str]

        use_on_demand_clusters : typing.Optional[bool]
            if True, a cluster will be created as necessary (wallet_id cannot be None)

        wallet_info : typing.Optional[WalletInfoInput]
            contains information about the wallet used to bill the running service

        collection_run_id : typing.Optional[str]
            In case start_pipeline is True, this is the collection run id to which the comp run belongs.

        encryption : typing.Optional[JobEncryptionContextMetadata]
            Optional job encryption context to decrypt input files and encrypt output files

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComputationGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/computations",
            method="POST",
            json={
                "user_id": user_id,
                "project_id": project_id,
                "start_pipeline": start_pipeline,
                "product_name": product_name,
                "product_api_base_url": product_api_base_url,
                "subgraph": subgraph,
                "force_restart": force_restart,
                "simcore_user_agent": simcore_user_agent,
                "use_on_demand_clusters": use_on_demand_clusters,
                "wallet_info": convert_and_respect_annotation_metadata(
                    object_=wallet_info, annotation=typing.Optional[WalletInfoInput], direction="write"
                ),
                "collection_run_id": collection_run_id,
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
                    ComputationGet,
                    parse_obj_as(
                        type_=ComputationGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_computation(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComputationGet]:
        """
        Returns a computation pipeline state

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComputationGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}",
            method="GET",
            params={
                "user_id": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComputationGet,
                    parse_obj_as(
                        type_=ComputationGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def delete_computation(
        self,
        project_id: str,
        *,
        user_id: UserIdInt,
        force: typing.Optional[bool] = OMIT,
        wait_for: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Deletes a computation pipeline

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        force : typing.Optional[bool]
            if True then the pipeline will be removed even if it is running

        wait_for : typing.Optional[str]
            timeout when waiting for pipeline to stop

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}",
            method="DELETE",
            json={
                "user_id": user_id,
                "force": force,
                "wait_for": wait_for,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ComputationGet]:
        """
        Stops a computation pipeline

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ComputationGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}:stop",
            method="POST",
            json={
                "user_id": user_id,
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
                    ComputationGet,
                    parse_obj_as(
                        type_=ComputationGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[TaskLogFileGet]]:
        """
        Returns download links to log-files of each task in a computation.
        Each log is only available when the corresponding task is done

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[TaskLogFileGet]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}/tasks/-/logfile",
            method="GET",
            params={
                "user_id": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TaskLogFileGet],
                    parse_obj_as(
                        type_=typing.List[TaskLogFileGet],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_task_log_file(
        self,
        project_id: str,
        node_uuid: str,
        *,
        user_id: UserIdInt,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskLogFileGet]:
        """
        Returns a link to download logs file of a give task.
        The log is only available when the task is done

        Parameters
        ----------
        project_id : str

        node_uuid : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskLogFileGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}/tasks/{encode_path_param(node_uuid)}/logfile",
            method="GET",
            params={
                "user_id": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskLogFileGet,
                    parse_obj_as(
                        type_=TaskLogFileGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post(
        self,
        project_id: str,
        *,
        nodes_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TasksOutputs]:
        """
        Parameters
        ----------
        project_id : str

        nodes_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TasksOutputs]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}/tasks/-/outputs:batchGet",
            method="POST",
            json={
                "nodes_ids": nodes_ids,
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
                    TasksOutputs,
                    parse_obj_as(
                        type_=TasksOutputs,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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


class AsyncRawComputationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_or_update_or_start_computation(
        self,
        *,
        user_id: UserIdInt,
        project_id: str,
        product_name: str,
        product_api_base_url: str,
        start_pipeline: typing.Optional[bool] = OMIT,
        subgraph: typing.Optional[typing.Sequence[str]] = OMIT,
        force_restart: typing.Optional[bool] = OMIT,
        simcore_user_agent: typing.Optional[str] = OMIT,
        use_on_demand_clusters: typing.Optional[bool] = OMIT,
        wallet_info: typing.Optional[WalletInfoInput] = OMIT,
        collection_run_id: typing.Optional[str] = OMIT,
        encryption: typing.Optional[JobEncryptionContextMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ComputationGet]:
        """
        Create and optionally start a new computation

        Parameters
        ----------
        user_id : UserIdInt

        project_id : str

        product_name : str

        product_api_base_url : str
            Base url of the product

        start_pipeline : typing.Optional[bool]
            if True the computation pipeline will start right away

        subgraph : typing.Optional[typing.Sequence[str]]
            An optional set of nodes that must be executed, if empty the whole pipeline is executed

        force_restart : typing.Optional[bool]
            if True will force re-running all dependent nodes

        simcore_user_agent : typing.Optional[str]

        use_on_demand_clusters : typing.Optional[bool]
            if True, a cluster will be created as necessary (wallet_id cannot be None)

        wallet_info : typing.Optional[WalletInfoInput]
            contains information about the wallet used to bill the running service

        collection_run_id : typing.Optional[str]
            In case start_pipeline is True, this is the collection run id to which the comp run belongs.

        encryption : typing.Optional[JobEncryptionContextMetadata]
            Optional job encryption context to decrypt input files and encrypt output files

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComputationGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/computations",
            method="POST",
            json={
                "user_id": user_id,
                "project_id": project_id,
                "start_pipeline": start_pipeline,
                "product_name": product_name,
                "product_api_base_url": product_api_base_url,
                "subgraph": subgraph,
                "force_restart": force_restart,
                "simcore_user_agent": simcore_user_agent,
                "use_on_demand_clusters": use_on_demand_clusters,
                "wallet_info": convert_and_respect_annotation_metadata(
                    object_=wallet_info, annotation=typing.Optional[WalletInfoInput], direction="write"
                ),
                "collection_run_id": collection_run_id,
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
                    ComputationGet,
                    parse_obj_as(
                        type_=ComputationGet,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_computation(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComputationGet]:
        """
        Returns a computation pipeline state

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComputationGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}",
            method="GET",
            params={
                "user_id": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ComputationGet,
                    parse_obj_as(
                        type_=ComputationGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def delete_computation(
        self,
        project_id: str,
        *,
        user_id: UserIdInt,
        force: typing.Optional[bool] = OMIT,
        wait_for: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a computation pipeline

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        force : typing.Optional[bool]
            if True then the pipeline will be removed even if it is running

        wait_for : typing.Optional[str]
            timeout when waiting for pipeline to stop

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}",
            method="DELETE",
            json={
                "user_id": user_id,
                "force": force,
                "wait_for": wait_for,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ComputationGet]:
        """
        Stops a computation pipeline

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ComputationGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}:stop",
            method="POST",
            json={
                "user_id": user_id,
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
                    ComputationGet,
                    parse_obj_as(
                        type_=ComputationGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_all_tasks_log_files_v2computations_project_id_tasks_logfile_get(
        self, project_id: str, *, user_id: UserIdInt, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[TaskLogFileGet]]:
        """
        Returns download links to log-files of each task in a computation.
        Each log is only available when the corresponding task is done

        Parameters
        ----------
        project_id : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[TaskLogFileGet]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}/tasks/-/logfile",
            method="GET",
            params={
                "user_id": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[TaskLogFileGet],
                    parse_obj_as(
                        type_=typing.List[TaskLogFileGet],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_task_log_file(
        self,
        project_id: str,
        node_uuid: str,
        *,
        user_id: UserIdInt,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskLogFileGet]:
        """
        Returns a link to download logs file of a give task.
        The log is only available when the task is done

        Parameters
        ----------
        project_id : str

        node_uuid : str

        user_id : UserIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskLogFileGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}/tasks/{encode_path_param(node_uuid)}/logfile",
            method="GET",
            params={
                "user_id": user_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskLogFileGet,
                    parse_obj_as(
                        type_=TaskLogFileGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_batch_tasks_outputs_v2computations_project_id_tasks_outputs_batch_get_post(
        self,
        project_id: str,
        *,
        nodes_ids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TasksOutputs]:
        """
        Parameters
        ----------
        project_id : str

        nodes_ids : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TasksOutputs]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/computations/{encode_path_param(project_id)}/tasks/-/outputs:batchGet",
            method="POST",
            json={
                "nodes_ids": nodes_ids,
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
                    TasksOutputs,
                    parse_obj_as(
                        type_=TasksOutputs,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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
