

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
from ..types.v1alpha1trigger_rule_resource_create_response import V1Alpha1TriggerRuleResourceCreateResponse
from ..types.v1alpha1trigger_rule_resource_read_response import V1Alpha1TriggerRuleResourceReadResponse
from ..types.v1alpha1trigger_rule_resource_spec import V1Alpha1TriggerRuleResourceSpec
from ..types.v1alpha1trigger_rule_resource_update_response import V1Alpha1TriggerRuleResourceUpdateResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTriggersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_triggers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[V1Alpha1TriggerRuleResourceReadResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1Alpha1TriggerRuleResourceReadResponse]]
            List of Trigger Rules
        """
        _response = self._client_wrapper.httpx_client.request(
            "triggers/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Alpha1TriggerRuleResourceReadResponse],
                    parse_obj_as(
                        type_=typing.List[V1Alpha1TriggerRuleResourceReadResponse],
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

    def create_trigger(
        self,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1TriggerRuleResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Alpha1TriggerRuleResourceCreateResponse]:
        """
        Parameters
        ----------
        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1TriggerRuleResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1TriggerRuleResourceCreateResponse]
            The created Trigger Rule
        """
        _response = self._client_wrapper.httpx_client.request(
            "triggers/",
            method="POST",
            json={
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=V1Alpha1ResourceMetadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=V1Alpha1TriggerRuleResourceSpec, direction="write"
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
                    V1Alpha1TriggerRuleResourceCreateResponse,
                    parse_obj_as(
                        type_=V1Alpha1TriggerRuleResourceCreateResponse,
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

    def get_trigger(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Alpha1TriggerRuleResourceReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1TriggerRuleResourceReadResponse]
            The Trigger Rule
        """
        _response = self._client_wrapper.httpx_client.request(
            f"triggers/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1TriggerRuleResourceReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1TriggerRuleResourceReadResponse,
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

    def update_trigger(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1TriggerRuleResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[V1Alpha1TriggerRuleResourceUpdateResponse]:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1TriggerRuleResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1TriggerRuleResourceUpdateResponse]
            The updated Trigger Rule
        """
        _response = self._client_wrapper.httpx_client.request(
            f"triggers/{encode_path_param(identifier)}",
            method="PUT",
            json={
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=V1Alpha1ResourceMetadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=V1Alpha1TriggerRuleResourceSpec, direction="write"
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
                    V1Alpha1TriggerRuleResourceUpdateResponse,
                    parse_obj_as(
                        type_=V1Alpha1TriggerRuleResourceUpdateResponse,
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

    def delete_trigger(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[V1Alpha1TriggerRuleResourceReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[V1Alpha1TriggerRuleResourceReadResponse]
            The deleted Trigger Rule
        """
        _response = self._client_wrapper.httpx_client.request(
            f"triggers/{encode_path_param(identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1TriggerRuleResourceReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1TriggerRuleResourceReadResponse,
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


class AsyncRawTriggersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_triggers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[V1Alpha1TriggerRuleResourceReadResponse]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1Alpha1TriggerRuleResourceReadResponse]]
            List of Trigger Rules
        """
        _response = await self._client_wrapper.httpx_client.request(
            "triggers/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1Alpha1TriggerRuleResourceReadResponse],
                    parse_obj_as(
                        type_=typing.List[V1Alpha1TriggerRuleResourceReadResponse],
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

    async def create_trigger(
        self,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1TriggerRuleResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Alpha1TriggerRuleResourceCreateResponse]:
        """
        Parameters
        ----------
        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1TriggerRuleResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1TriggerRuleResourceCreateResponse]
            The created Trigger Rule
        """
        _response = await self._client_wrapper.httpx_client.request(
            "triggers/",
            method="POST",
            json={
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=V1Alpha1ResourceMetadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=V1Alpha1TriggerRuleResourceSpec, direction="write"
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
                    V1Alpha1TriggerRuleResourceCreateResponse,
                    parse_obj_as(
                        type_=V1Alpha1TriggerRuleResourceCreateResponse,
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

    async def get_trigger(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Alpha1TriggerRuleResourceReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1TriggerRuleResourceReadResponse]
            The Trigger Rule
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"triggers/{encode_path_param(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1TriggerRuleResourceReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1TriggerRuleResourceReadResponse,
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

    async def update_trigger(
        self,
        identifier: str,
        *,
        metadata: V1Alpha1ResourceMetadata,
        spec: V1Alpha1TriggerRuleResourceSpec,
        kind: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[V1Alpha1TriggerRuleResourceUpdateResponse]:
        """
        Parameters
        ----------
        identifier : str

        metadata : V1Alpha1ResourceMetadata

        spec : V1Alpha1TriggerRuleResourceSpec

        kind : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1TriggerRuleResourceUpdateResponse]
            The updated Trigger Rule
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"triggers/{encode_path_param(identifier)}",
            method="PUT",
            json={
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=V1Alpha1ResourceMetadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=V1Alpha1TriggerRuleResourceSpec, direction="write"
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
                    V1Alpha1TriggerRuleResourceUpdateResponse,
                    parse_obj_as(
                        type_=V1Alpha1TriggerRuleResourceUpdateResponse,
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

    async def delete_trigger(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[V1Alpha1TriggerRuleResourceReadResponse]:
        """
        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[V1Alpha1TriggerRuleResourceReadResponse]
            The deleted Trigger Rule
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"triggers/{encode_path_param(identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    V1Alpha1TriggerRuleResourceReadResponse,
                    parse_obj_as(
                        type_=V1Alpha1TriggerRuleResourceReadResponse,
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
