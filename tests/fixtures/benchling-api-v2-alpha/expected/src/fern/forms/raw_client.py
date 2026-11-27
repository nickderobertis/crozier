

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.form_definition import FormDefinition
from ..types.form_definitions_paginated_list import FormDefinitionsPaginatedList
from .types.get_form_definitions_request_sort import GetFormDefinitionsRequestSort
from pydantic import ValidationError


class RawFormsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_form_definitions(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        sort: typing.Optional[GetFormDefinitionsRequestSort] = None,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FormDefinitionsPaginatedList]:
        """
        Lists available form definitions. Only the latest version along is returned for each definition.

        Parameters
        ----------
        next_token : typing.Optional[str]
            Token for pagination

        page_size : typing.Optional[int]

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        sort : typing.Optional[GetFormDefinitionsRequestSort]
            Sets the sort-order of the response. Valid sorts are modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order.

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FormDefinitionsPaginatedList]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "form-definitions",
            method="GET",
            params={
                "nextToken": next_token,
                "pageSize": page_size,
                "modifiedAt": modified_at,
                "sort": sort,
                "returning": returning,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FormDefinitionsPaginatedList,
                    parse_obj_as(
                        type_=FormDefinitionsPaginatedList,
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

    def get_form_definition(
        self,
        form_definition_id: str,
        *,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FormDefinition]:
        """
        Get a specific form definition. Only the latest version is returned

        Parameters
        ----------
        form_definition_id : str
            API ID of the specific form definition desired

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FormDefinition]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"form-definitions/{encode_path_param(form_definition_id)}",
            method="GET",
            params={
                "returning": returning,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FormDefinition,
                    parse_obj_as(
                        type_=FormDefinition,
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


class AsyncRawFormsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_form_definitions(
        self,
        *,
        next_token: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        modified_at: typing.Optional[str] = None,
        sort: typing.Optional[GetFormDefinitionsRequestSort] = None,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FormDefinitionsPaginatedList]:
        """
        Lists available form definitions. Only the latest version along is returned for each definition.

        Parameters
        ----------
        next_token : typing.Optional[str]
            Token for pagination

        page_size : typing.Optional[int]

        modified_at : typing.Optional[str]
            Datetime, in RFC 3339 format. Supports the > and < operators. Time zone defaults to UTC. Restricts results to those modified in the specified range. e.g. > 2017-04-30. Date ranges can be specified with the following nomenclature > YYYY-MM-DD AND <YYYY-MM-DD.

        sort : typing.Optional[GetFormDefinitionsRequestSort]
            Sets the sort-order of the response. Valid sorts are modifiedAt (modified time, most recent first). Optionally add :asc or :desc to specify ascending or descending order.

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FormDefinitionsPaginatedList]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "form-definitions",
            method="GET",
            params={
                "nextToken": next_token,
                "pageSize": page_size,
                "modifiedAt": modified_at,
                "sort": sort,
                "returning": returning,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FormDefinitionsPaginatedList,
                    parse_obj_as(
                        type_=FormDefinitionsPaginatedList,
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

    async def get_form_definition(
        self,
        form_definition_id: str,
        *,
        returning: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FormDefinition]:
        """
        Get a specific form definition. Only the latest version is returned

        Parameters
        ----------
        form_definition_id : str
            API ID of the specific form definition desired

        returning : typing.Optional[str]
            Comma-separated list of fields to return. Modifies the output shape. To return all keys at a given level, enumerate them or use the wildcard, '*'. For more information, [click here](https://docs.benchling.com/docs/getting-started-1#returning-query-parameter).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FormDefinition]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"form-definitions/{encode_path_param(form_definition_id)}",
            method="GET",
            params={
                "returning": returning,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FormDefinition,
                    parse_obj_as(
                        type_=FormDefinition,
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
