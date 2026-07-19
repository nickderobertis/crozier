

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
from ..errors.not_found_error import NotFoundError
from ..types.pipelines_list_pipelines_request_offset import PipelinesListPipelinesRequestOffset
from .types.pipelines_count_pipelines_response import PipelinesCountPipelinesResponse
from .types.pipelines_create_pipeline_request_integration_type import PipelinesCreatePipelineRequestIntegrationType
from .types.pipelines_create_pipeline_request_producer_config import PipelinesCreatePipelineRequestProducerConfig
from .types.pipelines_create_pipeline_response import PipelinesCreatePipelineResponse
from .types.pipelines_delete_pipeline_response import PipelinesDeletePipelineResponse
from .types.pipelines_get_pipeline_response import PipelinesGetPipelineResponse
from .types.pipelines_list_pipeline_sync_history_response import PipelinesListPipelineSyncHistoryResponse
from .types.pipelines_list_pipelines_response import PipelinesListPipelinesResponse
from .types.pipelines_preview_pipeline_request_integration_type import PipelinesPreviewPipelineRequestIntegrationType
from .types.pipelines_preview_pipeline_request_producer_config import PipelinesPreviewPipelineRequestProducerConfig
from .types.pipelines_preview_pipeline_response import PipelinesPreviewPipelineResponse
from .types.pipelines_sync_pipeline_response import PipelinesSyncPipelineResponse
from .types.pipelines_update_pipeline_response import PipelinesUpdatePipelineResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPipelinesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def listpipelines(
        self,
        *,
        search: typing.Optional[str] = None,
        integration_type: typing.Optional[str] = None,
        offset: typing.Optional[PipelinesListPipelinesRequestOffset] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelinesListPipelinesResponse]:
        """
        List all pipelines for the organization with optional filtering

        Parameters
        ----------
        search : typing.Optional[str]

        integration_type : typing.Optional[str]

        offset : typing.Optional[PipelinesListPipelinesRequestOffset]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesListPipelinesResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/pipelines",
            method="GET",
            params={
                "search": search,
                "integration_type": integration_type,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesListPipelinesResponse,
                    parse_obj_as(
                        type_=PipelinesListPipelinesResponse,
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

    def createpipeline(
        self,
        *,
        name: str,
        project_id: str,
        integration_type: PipelinesCreatePipelineRequestIntegrationType,
        producer_config: PipelinesCreatePipelineRequestProducerConfig,
        subscriber_agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        subscriber_cron_schedule: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelinesCreatePipelineResponse]:
        """
        Create a new pipeline (producer + feed + optionally subscribers)

        Parameters
        ----------
        name : str

        project_id : str

        integration_type : PipelinesCreatePipelineRequestIntegrationType

        producer_config : PipelinesCreatePipelineRequestProducerConfig

        subscriber_agent_ids : typing.Optional[typing.Sequence[str]]

        subscriber_cron_schedule : typing.Optional[str]

        prompt_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesCreatePipelineResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/pipelines",
            method="POST",
            json={
                "name": name,
                "project_id": project_id,
                "integration_type": integration_type,
                "producer_config": convert_and_respect_annotation_metadata(
                    object_=producer_config, annotation=PipelinesCreatePipelineRequestProducerConfig, direction="write"
                ),
                "subscriber_agent_ids": subscriber_agent_ids,
                "subscriber_cron_schedule": subscriber_cron_schedule,
                "prompt_template": prompt_template,
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
                    PipelinesCreatePipelineResponse,
                    parse_obj_as(
                        type_=PipelinesCreatePipelineResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def countpipelines(
        self,
        *,
        search: typing.Optional[str] = None,
        integration_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelinesCountPipelinesResponse]:
        """
        Get the total count of pipelines, optionally filtered by project and search

        Parameters
        ----------
        search : typing.Optional[str]

        integration_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesCountPipelinesResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/pipelines/count",
            method="GET",
            params={
                "search": search,
                "integration_type": integration_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesCountPipelinesResponse,
                    parse_obj_as(
                        type_=PipelinesCountPipelinesResponse,
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

    def getpipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PipelinesGetPipelineResponse]:
        """
        Get a single pipeline with details

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesGetPipelineResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesGetPipelineResponse,
                    parse_obj_as(
                        type_=PipelinesGetPipelineResponse,
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

    def deletepipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PipelinesDeletePipelineResponse]:
        """
        Soft delete a pipeline and cascade to feed + subscriptions

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesDeletePipelineResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}",
            method="DELETE",
            json={},
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesDeletePipelineResponse,
                    parse_obj_as(
                        type_=PipelinesDeletePipelineResponse,
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

    def updatepipeline(
        self,
        pipeline_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelinesUpdatePipelineResponse]:
        """
        Update pipeline name or disable/enable it

        Parameters
        ----------
        pipeline_id : str

        name : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesUpdatePipelineResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}",
            method="PATCH",
            json={
                "name": name,
                "disabled": disabled,
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
                    PipelinesUpdatePipelineResponse,
                    parse_obj_as(
                        type_=PipelinesUpdatePipelineResponse,
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

    def previewpipeline(
        self,
        *,
        integration_type: PipelinesPreviewPipelineRequestIntegrationType,
        integration_id: str,
        producer_config: PipelinesPreviewPipelineRequestProducerConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PipelinesPreviewPipelineResponse]:
        """
        Fetch sample messages from integration to preview what agents will receive

        Parameters
        ----------
        integration_type : PipelinesPreviewPipelineRequestIntegrationType

        integration_id : str

        producer_config : PipelinesPreviewPipelineRequestProducerConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesPreviewPipelineResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/pipelines/preview",
            method="POST",
            json={
                "integration_type": integration_type,
                "integration_id": integration_id,
                "producer_config": convert_and_respect_annotation_metadata(
                    object_=producer_config, annotation=PipelinesPreviewPipelineRequestProducerConfig, direction="write"
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
                    PipelinesPreviewPipelineResponse,
                    parse_obj_as(
                        type_=PipelinesPreviewPipelineResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def syncpipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PipelinesSyncPipelineResponse]:
        """
        Manually trigger a pipeline sync to fetch new messages immediately

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesSyncPipelineResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}/sync",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesSyncPipelineResponse,
                    parse_obj_as(
                        type_=PipelinesSyncPipelineResponse,
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

    def listpipelinesynchistory(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PipelinesListPipelineSyncHistoryResponse]:
        """
        List the sync run history for a pipeline from Temporal with error details

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PipelinesListPipelineSyncHistoryResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}/sync/history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesListPipelineSyncHistoryResponse,
                    parse_obj_as(
                        type_=PipelinesListPipelineSyncHistoryResponse,
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


class AsyncRawPipelinesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def listpipelines(
        self,
        *,
        search: typing.Optional[str] = None,
        integration_type: typing.Optional[str] = None,
        offset: typing.Optional[PipelinesListPipelinesRequestOffset] = None,
        limit: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelinesListPipelinesResponse]:
        """
        List all pipelines for the organization with optional filtering

        Parameters
        ----------
        search : typing.Optional[str]

        integration_type : typing.Optional[str]

        offset : typing.Optional[PipelinesListPipelinesRequestOffset]

        limit : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesListPipelinesResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/pipelines",
            method="GET",
            params={
                "search": search,
                "integration_type": integration_type,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesListPipelinesResponse,
                    parse_obj_as(
                        type_=PipelinesListPipelinesResponse,
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

    async def createpipeline(
        self,
        *,
        name: str,
        project_id: str,
        integration_type: PipelinesCreatePipelineRequestIntegrationType,
        producer_config: PipelinesCreatePipelineRequestProducerConfig,
        subscriber_agent_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        subscriber_cron_schedule: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelinesCreatePipelineResponse]:
        """
        Create a new pipeline (producer + feed + optionally subscribers)

        Parameters
        ----------
        name : str

        project_id : str

        integration_type : PipelinesCreatePipelineRequestIntegrationType

        producer_config : PipelinesCreatePipelineRequestProducerConfig

        subscriber_agent_ids : typing.Optional[typing.Sequence[str]]

        subscriber_cron_schedule : typing.Optional[str]

        prompt_template : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesCreatePipelineResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/pipelines",
            method="POST",
            json={
                "name": name,
                "project_id": project_id,
                "integration_type": integration_type,
                "producer_config": convert_and_respect_annotation_metadata(
                    object_=producer_config, annotation=PipelinesCreatePipelineRequestProducerConfig, direction="write"
                ),
                "subscriber_agent_ids": subscriber_agent_ids,
                "subscriber_cron_schedule": subscriber_cron_schedule,
                "prompt_template": prompt_template,
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
                    PipelinesCreatePipelineResponse,
                    parse_obj_as(
                        type_=PipelinesCreatePipelineResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def countpipelines(
        self,
        *,
        search: typing.Optional[str] = None,
        integration_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelinesCountPipelinesResponse]:
        """
        Get the total count of pipelines, optionally filtered by project and search

        Parameters
        ----------
        search : typing.Optional[str]

        integration_type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesCountPipelinesResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/pipelines/count",
            method="GET",
            params={
                "search": search,
                "integration_type": integration_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesCountPipelinesResponse,
                    parse_obj_as(
                        type_=PipelinesCountPipelinesResponse,
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

    async def getpipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PipelinesGetPipelineResponse]:
        """
        Get a single pipeline with details

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesGetPipelineResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesGetPipelineResponse,
                    parse_obj_as(
                        type_=PipelinesGetPipelineResponse,
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

    async def deletepipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PipelinesDeletePipelineResponse]:
        """
        Soft delete a pipeline and cascade to feed + subscriptions

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesDeletePipelineResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}",
            method="DELETE",
            json={},
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesDeletePipelineResponse,
                    parse_obj_as(
                        type_=PipelinesDeletePipelineResponse,
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

    async def updatepipeline(
        self,
        pipeline_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        disabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelinesUpdatePipelineResponse]:
        """
        Update pipeline name or disable/enable it

        Parameters
        ----------
        pipeline_id : str

        name : typing.Optional[str]

        disabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesUpdatePipelineResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}",
            method="PATCH",
            json={
                "name": name,
                "disabled": disabled,
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
                    PipelinesUpdatePipelineResponse,
                    parse_obj_as(
                        type_=PipelinesUpdatePipelineResponse,
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

    async def previewpipeline(
        self,
        *,
        integration_type: PipelinesPreviewPipelineRequestIntegrationType,
        integration_id: str,
        producer_config: PipelinesPreviewPipelineRequestProducerConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PipelinesPreviewPipelineResponse]:
        """
        Fetch sample messages from integration to preview what agents will receive

        Parameters
        ----------
        integration_type : PipelinesPreviewPipelineRequestIntegrationType

        integration_id : str

        producer_config : PipelinesPreviewPipelineRequestProducerConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesPreviewPipelineResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/pipelines/preview",
            method="POST",
            json={
                "integration_type": integration_type,
                "integration_id": integration_id,
                "producer_config": convert_and_respect_annotation_metadata(
                    object_=producer_config, annotation=PipelinesPreviewPipelineRequestProducerConfig, direction="write"
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
                    PipelinesPreviewPipelineResponse,
                    parse_obj_as(
                        type_=PipelinesPreviewPipelineResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def syncpipeline(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PipelinesSyncPipelineResponse]:
        """
        Manually trigger a pipeline sync to fetch new messages immediately

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesSyncPipelineResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}/sync",
            method="POST",
            json={},
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesSyncPipelineResponse,
                    parse_obj_as(
                        type_=PipelinesSyncPipelineResponse,
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

    async def listpipelinesynchistory(
        self, pipeline_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PipelinesListPipelineSyncHistoryResponse]:
        """
        List the sync run history for a pipeline from Temporal with error details

        Parameters
        ----------
        pipeline_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PipelinesListPipelineSyncHistoryResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/pipelines/{encode_path_param(pipeline_id)}/sync/history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PipelinesListPipelineSyncHistoryResponse,
                    parse_obj_as(
                        type_=PipelinesListPipelineSyncHistoryResponse,
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
