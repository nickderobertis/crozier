

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_server_fastapi_server_public_models_project_models_http_source import (
    ApiServerFastapiServerPublicModelsProjectModelsHttpSource,
)
from ..types.ccs_project import CcsProject
from ..types.cps_task import CpsTask
from ..types.data_flow import DataFlow
from ..types.default_values import DefaultValues
from ..types.file_source import FileSource
from ..types.http_validation_error import HttpValidationError
from ..types.image_urls_info import ImageUrlsInfo
from ..types.package import Package
from ..types.project_data_index_conversion_settings_input import ProjectDataIndexConversionSettingsInput
from ..types.task_context import TaskContext
from ..types.task_result import TaskResult
from .types.get_project_integration_config_genai_response import GetProjectIntegrationConfigGenaiResponse
from .types.update_project_integration_config_genai_request_body import UpdateProjectIntegrationConfigGenaiRequestBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_project_default_values(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DefaultValues]:
        """
        List project's default values.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DefaultValues]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/default_values",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DefaultValues,
                    parse_obj_as(
                        type_=DefaultValues,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_project_default_values(
        self,
        proj_key: str,
        *,
        ccs_project: CcsProject,
        dataflow: typing.Optional[DataFlow] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Update project's default values.

        Parameters
        ----------
        proj_key : str

        ccs_project : CcsProject

        dataflow : typing.Optional[DataFlow]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/default_values",
            method="POST",
            json={
                "ccs_project": convert_and_respect_annotation_metadata(
                    object_=ccs_project, annotation=CcsProject, direction="write"
                ),
                "dataflow": convert_and_respect_annotation_metadata(
                    object_=dataflow, annotation=typing.Optional[DataFlow], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_project_integration_config_genai(
        self,
        proj_key: str,
        *,
        decode_secrets: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetProjectIntegrationConfigGenaiResponse]:
        """
        Get the GenAI config for a given project.

        Parameters
        ----------
        proj_key : str

        decode_secrets : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProjectIntegrationConfigGenaiResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/integrations/genai",
            method="GET",
            params={
                "decode_secrets": decode_secrets,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectIntegrationConfigGenaiResponse,
                    parse_obj_as(
                        type_=GetProjectIntegrationConfigGenaiResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def update_project_integration_config_genai(
        self,
        proj_key: str,
        *,
        request: UpdateProjectIntegrationConfigGenaiRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Update the GenAI config for a given project.

        Parameters
        ----------
        proj_key : str

        request : UpdateProjectIntegrationConfigGenaiRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/integrations/genai",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateProjectIntegrationConfigGenaiRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def delete_project_integration_config_genai(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete the GenAI config for a given project integration.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/integrations/genai",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def provision_project_packages(
        self,
        proj_key: str,
        *,
        packages: typing.Sequence[Package],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskContext]:
        """
        Install packages on a project.

        Parameters
        ----------
        proj_key : str

        packages : typing.Sequence[Package]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskContext]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/packages",
            method="POST",
            json={
                "packages": convert_and_respect_annotation_metadata(
                    object_=packages, annotation=typing.Sequence[Package], direction="write"
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
                    TaskContext,
                    parse_obj_as(
                        type_=TaskContext,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def convert_document(
        self,
        proj_key: str,
        *,
        http_source: typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource] = OMIT,
        file_source: typing.Optional[FileSource] = OMIT,
        settings: typing.Optional[ProjectDataIndexConversionSettingsInput] = OMIT,
        image_urls: typing.Optional[ImageUrlsInfo] = OMIT,
        truncate_pages: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CpsTask]:
        """
        Convert a document directly with Docling.

        Parameters
        ----------
        proj_key : str

        http_source : typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource]

        file_source : typing.Optional[FileSource]

        settings : typing.Optional[ProjectDataIndexConversionSettingsInput]

        image_urls : typing.Optional[ImageUrlsInfo]

        truncate_pages : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CpsTask]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/convert",
            method="POST",
            json={
                "http_source": convert_and_respect_annotation_metadata(
                    object_=http_source,
                    annotation=typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource],
                    direction="write",
                ),
                "file_source": convert_and_respect_annotation_metadata(
                    object_=file_source, annotation=typing.Optional[FileSource], direction="write"
                ),
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings,
                    annotation=typing.Optional[ProjectDataIndexConversionSettingsInput],
                    direction="write",
                ),
                "image_urls": image_urls,
                "truncate_pages": truncate_pages,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_convert_task(
        self,
        proj_key: str,
        task_id: str,
        *,
        wait: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TaskResult]:
        """
        Check status of a Docling conversion task; return presign urls for MD and JSON file if finished conversion successfully.

        Parameters
        ----------
        proj_key : str

        task_id : str

        wait : typing.Optional[int]
            Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TaskResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/convert_tasks/{encode_path_param(task_id)}",
            method="GET",
            params={
                "wait": wait,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskResult,
                    parse_obj_as(
                        type_=TaskResult,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawProjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_project_default_values(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DefaultValues]:
        """
        List project's default values.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DefaultValues]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/default_values",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DefaultValues,
                    parse_obj_as(
                        type_=DefaultValues,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_project_default_values(
        self,
        proj_key: str,
        *,
        ccs_project: CcsProject,
        dataflow: typing.Optional[DataFlow] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Update project's default values.

        Parameters
        ----------
        proj_key : str

        ccs_project : CcsProject

        dataflow : typing.Optional[DataFlow]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/default_values",
            method="POST",
            json={
                "ccs_project": convert_and_respect_annotation_metadata(
                    object_=ccs_project, annotation=CcsProject, direction="write"
                ),
                "dataflow": convert_and_respect_annotation_metadata(
                    object_=dataflow, annotation=typing.Optional[DataFlow], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_project_integration_config_genai(
        self,
        proj_key: str,
        *,
        decode_secrets: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetProjectIntegrationConfigGenaiResponse]:
        """
        Get the GenAI config for a given project.

        Parameters
        ----------
        proj_key : str

        decode_secrets : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProjectIntegrationConfigGenaiResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/integrations/genai",
            method="GET",
            params={
                "decode_secrets": decode_secrets,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectIntegrationConfigGenaiResponse,
                    parse_obj_as(
                        type_=GetProjectIntegrationConfigGenaiResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def update_project_integration_config_genai(
        self,
        proj_key: str,
        *,
        request: UpdateProjectIntegrationConfigGenaiRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Update the GenAI config for a given project.

        Parameters
        ----------
        proj_key : str

        request : UpdateProjectIntegrationConfigGenaiRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/integrations/genai",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateProjectIntegrationConfigGenaiRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def delete_project_integration_config_genai(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete the GenAI config for a given project integration.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/integrations/genai",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def provision_project_packages(
        self,
        proj_key: str,
        *,
        packages: typing.Sequence[Package],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskContext]:
        """
        Install packages on a project.

        Parameters
        ----------
        proj_key : str

        packages : typing.Sequence[Package]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskContext]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/packages",
            method="POST",
            json={
                "packages": convert_and_respect_annotation_metadata(
                    object_=packages, annotation=typing.Sequence[Package], direction="write"
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
                    TaskContext,
                    parse_obj_as(
                        type_=TaskContext,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def convert_document(
        self,
        proj_key: str,
        *,
        http_source: typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource] = OMIT,
        file_source: typing.Optional[FileSource] = OMIT,
        settings: typing.Optional[ProjectDataIndexConversionSettingsInput] = OMIT,
        image_urls: typing.Optional[ImageUrlsInfo] = OMIT,
        truncate_pages: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CpsTask]:
        """
        Convert a document directly with Docling.

        Parameters
        ----------
        proj_key : str

        http_source : typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource]

        file_source : typing.Optional[FileSource]

        settings : typing.Optional[ProjectDataIndexConversionSettingsInput]

        image_urls : typing.Optional[ImageUrlsInfo]

        truncate_pages : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CpsTask]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/convert",
            method="POST",
            json={
                "http_source": convert_and_respect_annotation_metadata(
                    object_=http_source,
                    annotation=typing.Optional[ApiServerFastapiServerPublicModelsProjectModelsHttpSource],
                    direction="write",
                ),
                "file_source": convert_and_respect_annotation_metadata(
                    object_=file_source, annotation=typing.Optional[FileSource], direction="write"
                ),
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings,
                    annotation=typing.Optional[ProjectDataIndexConversionSettingsInput],
                    direction="write",
                ),
                "image_urls": image_urls,
                "truncate_pages": truncate_pages,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_convert_task(
        self,
        proj_key: str,
        task_id: str,
        *,
        wait: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TaskResult]:
        """
        Check status of a Docling conversion task; return presign urls for MD and JSON file if finished conversion successfully.

        Parameters
        ----------
        proj_key : str

        task_id : str

        wait : typing.Optional[int]
            Optionally block this method call for a few seconds to wait for the result instead of polling through multiple calls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TaskResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/convert_tasks/{encode_path_param(task_id)}",
            method="GET",
            params={
                "wait": wait,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TaskResult,
                    parse_obj_as(
                        type_=TaskResult,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
