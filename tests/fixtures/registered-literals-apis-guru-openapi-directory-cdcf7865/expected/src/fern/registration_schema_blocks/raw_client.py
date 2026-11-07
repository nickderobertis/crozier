

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_schema_responses_schema_response_id_schema_blocks_schema_response_block_id_response import (
    GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse,
)
from .types.schema_response_blocks_read_response import SchemaResponseBlocksReadResponse
from pydantic import ValidationError


class RawRegistrationSchemaBlocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def schema_response_blocks_read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SchemaResponseBlocksReadResponse]:
        """
        This returns a list of all the Registration Schema Blocks are contained in Registration Schema.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
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
        HttpResponse[SchemaResponseBlocksReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}/schema_blocks/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaResponseBlocksReadResponse,
                    parse_obj_as(
                        type_=SchemaResponseBlocksReadResponse,
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

    def retrieve_a_registration_schema_block(
        self,
        schema_response_id: str,
        schema_response_block_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse]:
        """
        This returns a Registration Schema Block by it's ID.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        schema_response_block_id : str
            The unique identifier of the Schema Response Block example `61b79f9eadbb5701424a2d5e`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}/schema_blocks/{encode_path_param(schema_response_block_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse,
                    parse_obj_as(
                        type_=GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse,
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


class AsyncRawRegistrationSchemaBlocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def schema_response_blocks_read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SchemaResponseBlocksReadResponse]:
        """
        This returns a list of all the Registration Schema Blocks are contained in Registration Schema.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
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
        AsyncHttpResponse[SchemaResponseBlocksReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}/schema_blocks/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaResponseBlocksReadResponse,
                    parse_obj_as(
                        type_=SchemaResponseBlocksReadResponse,
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

    async def retrieve_a_registration_schema_block(
        self,
        schema_response_id: str,
        schema_response_block_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse]:
        """
        This returns a Registration Schema Block by it's ID.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Registration Schemas, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Registration Schema example `6176c9d45e01f100091d4f94`.

        schema_response_block_id : str
            The unique identifier of the Schema Response Block example `61b79f9eadbb5701424a2d5e`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}/schema_blocks/{encode_path_param(schema_response_block_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse,
                    parse_obj_as(
                        type_=GetSchemaResponsesSchemaResponseIdSchemaBlocksSchemaResponseBlockIdResponse,
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
