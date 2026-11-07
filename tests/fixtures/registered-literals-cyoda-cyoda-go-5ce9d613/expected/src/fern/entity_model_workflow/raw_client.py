

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error_response_dto import ErrorResponseDto
from ..types.workflow_configuration_dto import WorkflowConfigurationDto
from ..types.workflow_export_response_dto import WorkflowExportResponseDto
from .types.workflow_import_request_dto_import_mode import WorkflowImportRequestDtoImportMode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEntityModelWorkflowClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def export_entity_model_workflow(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkflowExportResponseDto]:
        """
        Exports all workflow configurations for a specific entity type.

        Since one entity type can have multiple workflows (selected by workflow-level conditions),
        this endpoint returns a collection of all workflows configured for the entity type.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkflowExportResponseDto]
            Workflows exported successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/workflow/export",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowExportResponseDto,
                    parse_obj_as(
                        type_=WorkflowExportResponseDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    def import_entity_model_workflow(
        self,
        entity_name: str,
        model_version: int,
        *,
        workflows: typing.Sequence[WorkflowConfigurationDto],
        import_mode: typing.Optional[WorkflowImportRequestDtoImportMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Imports or updates workflow configurations for a specific entity type.

        Since workflow name must be unique per entity model, this endpoint will either create
        new workflow or update existing workflow with the same name.

        The workflow configuration structure is defined by versioned schemas and may vary
        depending on the version specified in the configuration.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        workflows : typing.Sequence[WorkflowConfigurationDto]
            Array of workflow configurations to import

        import_mode : typing.Optional[WorkflowImportRequestDtoImportMode]
            Import mode for handling existing workflows

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/workflow/import",
            method="POST",
            json={
                "workflows": convert_and_respect_annotation_metadata(
                    object_=workflows, annotation=typing.Sequence[WorkflowConfigurationDto], direction="write"
                ),
                "importMode": import_mode,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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


class AsyncRawEntityModelWorkflowClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def export_entity_model_workflow(
        self, entity_name: str, model_version: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkflowExportResponseDto]:
        """
        Exports all workflow configurations for a specific entity type.

        Since one entity type can have multiple workflows (selected by workflow-level conditions),
        this endpoint returns a collection of all workflows configured for the entity type.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkflowExportResponseDto]
            Workflows exported successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/workflow/export",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkflowExportResponseDto,
                    parse_obj_as(
                        type_=WorkflowExportResponseDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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

    async def import_entity_model_workflow(
        self,
        entity_name: str,
        model_version: int,
        *,
        workflows: typing.Sequence[WorkflowConfigurationDto],
        import_mode: typing.Optional[WorkflowImportRequestDtoImportMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Imports or updates workflow configurations for a specific entity type.

        Since workflow name must be unique per entity model, this endpoint will either create
        new workflow or update existing workflow with the same name.

        The workflow configuration structure is defined by versioned schemas and may vary
        depending on the version specified in the configuration.

        Parameters
        ----------
        entity_name : str
            Name of the entity model

        model_version : int
            Version of the entity model

        workflows : typing.Sequence[WorkflowConfigurationDto]
            Array of workflow configurations to import

        import_mode : typing.Optional[WorkflowImportRequestDtoImportMode]
            Import mode for handling existing workflows

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"model/{encode_path_param(entity_name)}/{encode_path_param(model_version)}/workflow/import",
            method="POST",
            json={
                "workflows": convert_and_respect_annotation_metadata(
                    object_=workflows, annotation=typing.Sequence[WorkflowConfigurationDto], direction="write"
                ),
                "importMode": import_mode,
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
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponseDto,
                        parse_obj_as(
                            type_=ErrorResponseDto,
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
