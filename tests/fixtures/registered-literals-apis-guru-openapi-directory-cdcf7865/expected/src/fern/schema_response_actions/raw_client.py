

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.get_schema_responses_schema_response_id_actions_schema_response_action_id_response import (
    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse,
)
from .types.schema_response_action_read_response import SchemaResponseActionReadResponse
from pydantic import ValidationError


class RawSchemaResponseActionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def schema_response_action_read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SchemaResponseActionReadResponse]:
        """
        This retrieves a paginated list of all Schema Response Actions created for a Schema Response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
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
        HttpResponse[SchemaResponseActionReadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}/actions/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaResponseActionReadResponse,
                    parse_obj_as(
                        type_=SchemaResponseActionReadResponse,
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

    def create_a_new_schema_response_action(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        This creates a new Schema Response Action in order to trigger a state transition for a Schema Response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
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
            f"schema_responses/{encode_path_param(schema_response_id)}/actions/",
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

    def a_schema_response_action_from_a_schema_response(
        self,
        schema_response_id: str,
        schema_response_action_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse]:
        """
        Retrieves a Schema Response Action by it's ID.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Schema Response example `61b9cd62eb66180215222669`.

        schema_response_action_id : str
            The unique identifier of the Schema Response Action example `61b9eae1a7d8ac025c4c46d3`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}/actions/{encode_path_param(schema_response_action_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse,
                    parse_obj_as(
                        type_=GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse,
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


class AsyncRawSchemaResponseActionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def schema_response_action_read(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SchemaResponseActionReadResponse]:
        """
        This retrieves a paginated list of all Schema Response Actions created for a Schema Response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
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
        AsyncHttpResponse[SchemaResponseActionReadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}/actions/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SchemaResponseActionReadResponse,
                    parse_obj_as(
                        type_=SchemaResponseActionReadResponse,
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

    async def create_a_new_schema_response_action(
        self, schema_response_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        This creates a new Schema Response Action in order to trigger a state transition for a Schema Response.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
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
            f"schema_responses/{encode_path_param(schema_response_id)}/actions/",
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

    async def a_schema_response_action_from_a_schema_response(
        self,
        schema_response_id: str,
        schema_response_action_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse]:
        """
        Retrieves a Schema Response Action by it's ID.
        #### Returns
        Returns a JSON object with a `data` key containing the representation of the requested Schema Response Actions, if the request is successful.
        #### Errors
        If the request is unsuccessful, an `errors` key containing information about the failure will be returned. Refer to the [list of error codes](#tag/Errors-and-Error-Codes) to understand why this request may have failed.

        Parameters
        ----------
        schema_response_id : str
            The unique identifier of the Schema Response example `61b9cd62eb66180215222669`.

        schema_response_action_id : str
            The unique identifier of the Schema Response Action example `61b9eae1a7d8ac025c4c46d3`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"schema_responses/{encode_path_param(schema_response_id)}/actions/{encode_path_param(schema_response_action_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse,
                    parse_obj_as(
                        type_=GetSchemaResponsesSchemaResponseIdActionsSchemaResponseActionIdResponse,
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
