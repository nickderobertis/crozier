

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
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output12 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output13 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output14 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14,
)
from ..types.agentstack_server_api_schema_common_entity_model_class_getitem_locals_model_output15 import (
    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15,
)
from ..types.context_history_item_create_request import ContextHistoryItemCreateRequest
from ..types.context_permissions_grant import ContextPermissionsGrant
from ..types.context_token_response import ContextTokenResponse
from ..types.global_permission_grant import GlobalPermissionGrant
from ..types.http_validation_error import HttpValidationError
from ..types.paginated_result_context import PaginatedResultContext
from ..types.paginated_result_context_history_item import PaginatedResultContextHistoryItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContextsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_context(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        include_empty: typing.Optional[bool] = None,
        provider_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedResultContext]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        include_empty : typing.Optional[bool]

        provider_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResultContext]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/contexts",
            method="GET",
            params={
                "limit": limit,
                "page_token": page_token,
                "order": order,
                "order_by": order_by,
                "include_empty": include_empty,
                "provider_id": provider_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultContext,
                    parse_obj_as(
                        type_=PaginatedResultContext,
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

    def create_context(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        provider_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12]:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        provider_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/contexts",
            method="POST",
            json={
                "metadata": metadata,
                "provider_id": provider_id,
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12,
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

    def get_context(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13]:
        """
        Parameters
        ----------
        context_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13,
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

    def update_context(
        self,
        context_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14]:
        """
        Parameters
        ----------
        context_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}",
            method="PUT",
            json={
                "metadata": metadata,
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14,
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

    def delete_context(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        context_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}",
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

    def patch_context_metadata(
        self,
        context_id: str,
        *,
        metadata: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15]:
        """
        Parameters
        ----------
        context_id : str

        metadata : typing.Dict[str, typing.Optional[str]]
            Metadata update, will add or overwrite existing keys, None will delete the key from metadata.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/metadata",
            method="PATCH",
            json={
                "metadata": metadata,
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15,
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

    def generate_context_token(
        self,
        context_id: str,
        *,
        grant_global_permissions: typing.Optional[GlobalPermissionGrant] = OMIT,
        grant_context_permissions: typing.Optional[ContextPermissionsGrant] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContextTokenResponse]:
        """
        Parameters
        ----------
        context_id : str

        grant_global_permissions : typing.Optional[GlobalPermissionGrant]
            Global permissions granted by the token. Must be subset of the users permissions

        grant_context_permissions : typing.Optional[ContextPermissionsGrant]
            Context permissions granted by the token. Must be subset of the users permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContextTokenResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/token",
            method="POST",
            json={
                "grant_global_permissions": convert_and_respect_annotation_metadata(
                    object_=grant_global_permissions, annotation=GlobalPermissionGrant, direction="write"
                ),
                "grant_context_permissions": convert_and_respect_annotation_metadata(
                    object_=grant_context_permissions, annotation=ContextPermissionsGrant, direction="write"
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
                    ContextTokenResponse,
                    parse_obj_as(
                        type_=ContextTokenResponse,
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

    def list_context_history(
        self,
        context_id: str,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedResultContextHistoryItem]:
        """
        Parameters
        ----------
        context_id : str

        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResultContextHistoryItem]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/history",
            method="GET",
            params={
                "limit": limit,
                "page_token": page_token,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultContextHistoryItem,
                    parse_obj_as(
                        type_=PaginatedResultContextHistoryItem,
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

    def add_context_history_item(
        self,
        context_id: str,
        *,
        request: ContextHistoryItemCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        context_id : str

        request : ContextHistoryItemCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/history",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ContextHistoryItemCreateRequest, direction="write"
            ),
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

    def delete_context_history_from_id(
        self, context_id: str, *, from_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        context_id : str

        from_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/history",
            method="DELETE",
            params={
                "from_id": from_id,
            },
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


class AsyncRawContextsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_context(
        self,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        include_empty: typing.Optional[bool] = None,
        provider_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedResultContext]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        include_empty : typing.Optional[bool]

        provider_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResultContext]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/contexts",
            method="GET",
            params={
                "limit": limit,
                "page_token": page_token,
                "order": order,
                "order_by": order_by,
                "include_empty": include_empty,
                "provider_id": provider_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultContext,
                    parse_obj_as(
                        type_=PaginatedResultContext,
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

    async def create_context(
        self,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        provider_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12]:
        """
        Parameters
        ----------
        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        provider_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/contexts",
            method="POST",
            json={
                "metadata": metadata,
                "provider_id": provider_id,
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput12,
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

    async def get_context(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13]:
        """
        Parameters
        ----------
        context_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput13,
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

    async def update_context(
        self,
        context_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14]:
        """
        Parameters
        ----------
        context_id : str

        metadata : typing.Optional[typing.Dict[str, typing.Optional[str]]]

            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional
            information about the object in a structured format, and querying for objects via API or the dashboard.

            Keys are strings with a maximum length of 64 characters. Values are strings with a maximum length of
            512 characters.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}",
            method="PUT",
            json={
                "metadata": metadata,
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput14,
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

    async def delete_context(
        self, context_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        context_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}",
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

    async def patch_context_metadata(
        self,
        context_id: str,
        *,
        metadata: typing.Dict[str, typing.Optional[str]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15]:
        """
        Parameters
        ----------
        context_id : str

        metadata : typing.Dict[str, typing.Optional[str]]
            Metadata update, will add or overwrite existing keys, None will delete the key from metadata.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/metadata",
            method="PATCH",
            json={
                "metadata": metadata,
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
                    AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15,
                    parse_obj_as(
                        type_=AgentstackServerApiSchemaCommonEntityModelClassGetitemLocalsModelOutput15,
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

    async def generate_context_token(
        self,
        context_id: str,
        *,
        grant_global_permissions: typing.Optional[GlobalPermissionGrant] = OMIT,
        grant_context_permissions: typing.Optional[ContextPermissionsGrant] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContextTokenResponse]:
        """
        Parameters
        ----------
        context_id : str

        grant_global_permissions : typing.Optional[GlobalPermissionGrant]
            Global permissions granted by the token. Must be subset of the users permissions

        grant_context_permissions : typing.Optional[ContextPermissionsGrant]
            Context permissions granted by the token. Must be subset of the users permissions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContextTokenResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/token",
            method="POST",
            json={
                "grant_global_permissions": convert_and_respect_annotation_metadata(
                    object_=grant_global_permissions, annotation=GlobalPermissionGrant, direction="write"
                ),
                "grant_context_permissions": convert_and_respect_annotation_metadata(
                    object_=grant_context_permissions, annotation=ContextPermissionsGrant, direction="write"
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
                    ContextTokenResponse,
                    parse_obj_as(
                        type_=ContextTokenResponse,
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

    async def list_context_history(
        self,
        context_id: str,
        *,
        limit: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        order: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedResultContextHistoryItem]:
        """
        Parameters
        ----------
        context_id : str

        limit : typing.Optional[int]

        page_token : typing.Optional[str]

        order : typing.Optional[str]

        order_by : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResultContextHistoryItem]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/history",
            method="GET",
            params={
                "limit": limit,
                "page_token": page_token,
                "order": order,
                "order_by": order_by,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResultContextHistoryItem,
                    parse_obj_as(
                        type_=PaginatedResultContextHistoryItem,
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

    async def add_context_history_item(
        self,
        context_id: str,
        *,
        request: ContextHistoryItemCreateRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        context_id : str

        request : ContextHistoryItemCreateRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/history",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=ContextHistoryItemCreateRequest, direction="write"
            ),
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

    async def delete_context_history_from_id(
        self, context_id: str, *, from_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        context_id : str

        from_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/contexts/{encode_path_param(context_id)}/history",
            method="DELETE",
            params={
                "from_id": from_id,
            },
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
