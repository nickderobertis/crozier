

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_error_model import ApiErrorModel
from ..types.http_validation_error import HttpValidationError
from ..types.v1alpha1resource_metadata import V1Alpha1ResourceMetadata
from ..types.v1alpha1workflow_resource_create_response import V1Alpha1WorkflowResourceCreateResponse
from ..types.v1alpha1workflow_resource_read_response import V1Alpha1WorkflowResourceReadResponse
from ..types.v1alpha1workflow_resource_spec import V1Alpha1WorkflowResourceSpec
from ..types.v1alpha1workflow_resource_update_response import V1Alpha1WorkflowResourceUpdateResponse
from ..types.v1alpha1workflow_run_read_response import V1Alpha1WorkflowRunReadResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_workflows(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[V1Alpha1WorkflowResourceReadResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Alpha1WorkflowResourceReadResponse]]
            List of Workflows
        """
        _response = self._client_wrapper.httpx_client.request(
            "workflows/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Alpha1WorkflowResourceReadResponse],
                    parse_obj_as(
                        type_=typing.List[V1Alpha1WorkflowResourceReadResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def create_workflow(
        self,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1WorkflowResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Alpha1WorkflowResourceCreateResponse]:
        """
        Parameters
        ----------
        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1WorkflowResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1WorkflowResourceCreateResponse]
            The created Workflow
        """
        _response = self._client_wrapper.httpx_client.request(
            "workflows/",
            method="POST",
            json={
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=V1Alpha1ResourceMetadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=V1Alpha1WorkflowResourceSpec, direction="write"
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
                    V1Alpha1WorkflowResourceCreateResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowResourceCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def get_workflow(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Alpha1WorkflowResourceReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1WorkflowResourceReadResponse]
            The Workflow Definition
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowResourceReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowResourceReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def update_workflow(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1WorkflowResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Alpha1WorkflowResourceUpdateResponse]:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1WorkflowResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1WorkflowResourceUpdateResponse]
            The updated Workflow
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}",
            method="PUT",
            json={
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=V1Alpha1ResourceMetadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=V1Alpha1WorkflowResourceSpec, direction="write"
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
                    V1Alpha1WorkflowResourceUpdateResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowResourceUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def delete_workflow(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Alpha1WorkflowResourceReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1WorkflowResourceReadResponse]
            The Workflow that was deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowResourceReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowResourceReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def list_workflow_runs(
        self,
        identifier: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[V1Alpha1WorkflowRunReadResponse]]:
        """
        Parameters
        ----------
        identifier : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Alpha1WorkflowRunReadResponse]]
            List of Workflow Runs
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}/run",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Alpha1WorkflowRunReadResponse],
                    parse_obj_as(
                        type_=typing.List[V1Alpha1WorkflowRunReadResponse],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def run_workflow(
        self,
        identifier: str,
        *,
        request: typing.Dict[str, typing.Any],
        namespace: typing.Optional[str] = None,
        wait: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Alpha1WorkflowRunReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request : typing.Dict[str, typing.Any]

        namespace : typing.Optional[str]

        wait : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1WorkflowRunReadResponse]
            The WorkflowRun that was created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}/run",
            method="POST",
            params={
                "namespace": namespace,
                "wait": wait,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowRunReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowRunReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def get_workflow_run(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Alpha1WorkflowRunReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1WorkflowRunReadResponse]
            The Workflow Run
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/run/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowRunReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowRunReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def delete_workflow_run(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Alpha1WorkflowRunReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1WorkflowRunReadResponse]
            The deleted Workflow Run
        """
        _response = self._client_wrapper.httpx_client.request(
            f"workflows/run/{encode_path_param(identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowRunReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowRunReadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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


class AsyncRawWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_workflows(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[V1Alpha1WorkflowResourceReadResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Alpha1WorkflowResourceReadResponse]]
            List of Workflows
        """
        _response = await self._client_wrapper.httpx_client.request(
            "workflows/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Alpha1WorkflowResourceReadResponse],
                    parse_obj_as(
                        type_=typing.List[V1Alpha1WorkflowResourceReadResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def create_workflow(
        self,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1WorkflowResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Alpha1WorkflowResourceCreateResponse]:
        """
        Parameters
        ----------
        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1WorkflowResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1WorkflowResourceCreateResponse]
            The created Workflow
        """
        _response = await self._client_wrapper.httpx_client.request(
            "workflows/",
            method="POST",
            json={
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=V1Alpha1ResourceMetadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=V1Alpha1WorkflowResourceSpec, direction="write"
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
                    V1Alpha1WorkflowResourceCreateResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowResourceCreateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def get_workflow(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Alpha1WorkflowResourceReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1WorkflowResourceReadResponse]
            The Workflow Definition
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowResourceReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowResourceReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def update_workflow(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1WorkflowResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Alpha1WorkflowResourceUpdateResponse]:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1WorkflowResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1WorkflowResourceUpdateResponse]
            The updated Workflow
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}",
            method="PUT",
            json={
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=V1Alpha1ResourceMetadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=V1Alpha1WorkflowResourceSpec, direction="write"
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
                    V1Alpha1WorkflowResourceUpdateResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowResourceUpdateResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def delete_workflow(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Alpha1WorkflowResourceReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1WorkflowResourceReadResponse]
            The Workflow that was deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowResourceReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowResourceReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def list_workflow_runs(
        self,
        identifier: str,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[V1Alpha1WorkflowRunReadResponse]]:
        """
        Parameters
        ----------
        identifier : str

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Alpha1WorkflowRunReadResponse]]
            List of Workflow Runs
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}/run",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Alpha1WorkflowRunReadResponse],
                    parse_obj_as(
                        type_=typing.List[V1Alpha1WorkflowRunReadResponse],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def run_workflow(
        self,
        identifier: str,
        *,
        request: typing.Dict[str, typing.Any],
        namespace: typing.Optional[str] = None,
        wait: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Alpha1WorkflowRunReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request : typing.Dict[str, typing.Any]

        namespace : typing.Optional[str]

        wait : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1WorkflowRunReadResponse]
            The WorkflowRun that was created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/{encode_path_param(identifier)}/run",
            method="POST",
            params={
                "namespace": namespace,
                "wait": wait,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowRunReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowRunReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def get_workflow_run(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Alpha1WorkflowRunReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1WorkflowRunReadResponse]
            The Workflow Run
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/run/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowRunReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowRunReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def delete_workflow_run(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Alpha1WorkflowRunReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1WorkflowRunReadResponse]
            The deleted Workflow Run
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"workflows/run/{encode_path_param(identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1WorkflowRunReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1WorkflowRunReadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorModel,
                        parse_obj_as(
                            type_=ApiErrorModel,
                            object_=_response.json(),
                        ),
                    ),
                )
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
