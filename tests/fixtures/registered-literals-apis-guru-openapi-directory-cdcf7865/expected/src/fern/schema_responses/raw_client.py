

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
from .types.schema_response_patch_request_attributes import SchemaResponsePatchRequestAttributes
from .types.schema_response_patch_request_links import SchemaResponsePatchRequestLinks
from .types.schema_response_patch_request_relationships import SchemaResponsePatchRequestRelationships
from .types.schema_response_patch_response import SchemaResponsePatchResponse
from .types.schema_response_ppost_request_attributes import SchemaResponsePpostRequestAttributes
from .types.schema_response_ppost_request_links import SchemaResponsePpostRequestLinks
from .types.schema_response_ppost_request_relationships import SchemaResponsePpostRequestRelationships
from .types.schema_response_ppost_response import SchemaResponsePpostResponse
from .types.schema_responses_list_response import SchemaResponsesListResponse
from .types.schema_responses_read_response import SchemaResponsesReadResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSchemaResponsesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SchemaResponsesListResponse]:
        """
        This retrieves a paginated list of all active Schema Responses that are public.
        #### Returns
        Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of 10 Schema Responses. Each resource in the array is a separate Registration Schemas object. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchemaResponsesListResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "schema_responses/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaResponsesListResponse,
                    parse_obj_as(
                        type_=SchemaResponsesListResponse,
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

    def schema_response_ppost(
        self,
        *,
        attributes: SchemaResponsePpostRequestAttributes,
        type: str,
        links: typing.Optional[SchemaResponsePpostRequestLinks] = OMIT,
        relationships: typing.Optional[SchemaResponsePpostRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchemaResponsePpostResponse]:
        """
        This endpoint creates a new Schema Response with an `in_progress` state. A new response can only be created if the current schema response is in an `approved` state.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        attributes : SchemaResponsePpostRequestAttributes
            The properties of the Schema Response.

        type : str
            The type identifier of the Schema Response (`schema-response`).

        links : typing.Optional[SchemaResponsePpostRequestLinks]
            URLs to alternative representations of the Schema Response entity.

        relationships : typing.Optional[SchemaResponsePpostRequestRelationships]
            Links to other entities or entity collections that have a relationship to the file entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchemaResponsePpostResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "schema_responses/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=SchemaResponsePpostRequestAttributes, direction="write"
                ),
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=SchemaResponsePpostRequestLinks, direction="write"
                ),
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships, annotation=SchemaResponsePpostRequestRelationships, direction="write"
                ),
                "type": type,
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
                    SchemaResponsePpostResponse,
                    parse_obj_as(
                        type_=SchemaResponsePpostResponse,
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

    def read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SchemaResponsesReadResponse]:
        """
        This retrieves a single Schema response using it's id.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchemaResponsesReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaResponsesReadResponse,
                    parse_obj_as(
                        type_=SchemaResponsesReadResponse,
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

    def schema_response_delete(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        This endpoint deletes a new Schema Response. Schema Responses can only be deleted in the `in_progress` state. Once a Schema Response is transitioned to an `approved` it is immutable and another Schema Response must be created to update the Schema Response for that registration.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}",
            method="DELETE",
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

    def schema_response_patch(
        self,
        schema_response_id: str,
        *,
        attributes: SchemaResponsePatchRequestAttributes,
        type: str,
        links: typing.Optional[SchemaResponsePatchRequestLinks] = OMIT,
        relationships: typing.Optional[SchemaResponsePatchRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SchemaResponsePatchResponse]:
        """
        Patching to this endpoint allows one to directly edit the revision responses on the Schema Response of a Registration if that Schema Response is in an `in_progress` state.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        attributes : SchemaResponsePatchRequestAttributes
            The properties of the Schema Response.

        type : str
            The type identifier of the Schema Response (`schema-response`).

        links : typing.Optional[SchemaResponsePatchRequestLinks]
            URLs to alternative representations of the Schema Response entity.

        relationships : typing.Optional[SchemaResponsePatchRequestRelationships]
            Links to other entities or entity collections that have a relationship to the file entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SchemaResponsePatchResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}",
            method="PATCH",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=SchemaResponsePatchRequestAttributes, direction="write"
                ),
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=SchemaResponsePatchRequestLinks, direction="write"
                ),
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships, annotation=SchemaResponsePatchRequestRelationships, direction="write"
                ),
                "type": type,
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
                    SchemaResponsePatchResponse,
                    parse_obj_as(
                        type_=SchemaResponsePatchResponse,
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


class AsyncRawSchemaResponsesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SchemaResponsesListResponse]:
        """
        This retrieves a paginated list of all active Schema Responses that are public.
        #### Returns
        Returns a JSON object containing `data` and `links` keys. The `data` key contains an array of 10 Schema Responses. Each resource in the array is a separate Registration Schemas object. The `links` key contains a dictionary of links that can be used for [pagination](#tag/Pagination).
        #### Errors
        This request should never return an error.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchemaResponsesListResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "schema_responses/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaResponsesListResponse,
                    parse_obj_as(
                        type_=SchemaResponsesListResponse,
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

    async def schema_response_ppost(
        self,
        *,
        attributes: SchemaResponsePpostRequestAttributes,
        type: str,
        links: typing.Optional[SchemaResponsePpostRequestLinks] = OMIT,
        relationships: typing.Optional[SchemaResponsePpostRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchemaResponsePpostResponse]:
        """
        This endpoint creates a new Schema Response with an `in_progress` state. A new response can only be created if the current schema response is in an `approved` state.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        attributes : SchemaResponsePpostRequestAttributes
            The properties of the Schema Response.

        type : str
            The type identifier of the Schema Response (`schema-response`).

        links : typing.Optional[SchemaResponsePpostRequestLinks]
            URLs to alternative representations of the Schema Response entity.

        relationships : typing.Optional[SchemaResponsePpostRequestRelationships]
            Links to other entities or entity collections that have a relationship to the file entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchemaResponsePpostResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "schema_responses/",
            method="POST",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=SchemaResponsePpostRequestAttributes, direction="write"
                ),
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=SchemaResponsePpostRequestLinks, direction="write"
                ),
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships, annotation=SchemaResponsePpostRequestRelationships, direction="write"
                ),
                "type": type,
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
                    SchemaResponsePpostResponse,
                    parse_obj_as(
                        type_=SchemaResponsePpostResponse,
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

    async def read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SchemaResponsesReadResponse]:
        """
        This retrieves a single Schema response using it's id.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchemaResponsesReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaResponsesReadResponse,
                    parse_obj_as(
                        type_=SchemaResponsesReadResponse,
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

    async def schema_response_delete(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        This endpoint deletes a new Schema Response. Schema Responses can only be deleted in the `in_progress` state. Once a Schema Response is transitioned to an `approved` it is immutable and another Schema Response must be created to update the Schema Response for that registration.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}",
            method="DELETE",
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

    async def schema_response_patch(
        self,
        schema_response_id: str,
        *,
        attributes: SchemaResponsePatchRequestAttributes,
        type: str,
        links: typing.Optional[SchemaResponsePatchRequestLinks] = OMIT,
        relationships: typing.Optional[SchemaResponsePatchRequestRelationships] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SchemaResponsePatchResponse]:
        """
        Patching to this endpoint allows one to directly edit the revision responses on the Schema Response of a Registration if that Schema Response is in an `in_progress` state.
        #### Returns
        Returns a JSON object with a `data` key containing an updated representation of the requested Schema Response, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        attributes : SchemaResponsePatchRequestAttributes
            The properties of the Schema Response.

        type : str
            The type identifier of the Schema Response (`schema-response`).

        links : typing.Optional[SchemaResponsePatchRequestLinks]
            URLs to alternative representations of the Schema Response entity.

        relationships : typing.Optional[SchemaResponsePatchRequestRelationships]
            Links to other entities or entity collections that have a relationship to the file entity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SchemaResponsePatchResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}",
            method="PATCH",
            json={
                "attributes": convert_and_respect_annotation_metadata(
                    object_=attributes, annotation=SchemaResponsePatchRequestAttributes, direction="write"
                ),
                "links": convert_and_respect_annotation_metadata(
                    object_=links, annotation=SchemaResponsePatchRequestLinks, direction="write"
                ),
                "relationships": convert_and_respect_annotation_metadata(
                    object_=relationships, annotation=SchemaResponsePatchRequestRelationships, direction="write"
                ),
                "type": type,
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
                    SchemaResponsePatchResponse,
                    parse_obj_as(
                        type_=SchemaResponsePatchResponse,
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
