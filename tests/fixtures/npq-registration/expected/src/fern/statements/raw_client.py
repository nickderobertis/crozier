

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.id_attribute import IdAttribute
from ..types.list_statements_filter import ListStatementsFilter
from ..types.not_found_response import NotFoundResponse
from ..types.pagination_filter import PaginationFilter
from ..types.statement_response import StatementResponse
from ..types.statements_response import StatementsResponse
from ..types.unauthorised_response import UnauthorisedResponse
from pydantic import ValidationError


class RawStatementsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def retrieve_financial_statements(
        self,
        *,
        filter: typing.Optional[ListStatementsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StatementsResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListStatementsFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StatementsResponse]
            A list of statements as part of which the DfE will make output payments for participants
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v3/statements",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListStatementsFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StatementsResponse,
                    parse_obj_as(
                        type_=StatementsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
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

    def retrieve_a_specific_financial_statement(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StatementResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StatementResponse]
            A specific financial statement
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v3/statements/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StatementResponse,
                    parse_obj_as(
                        type_=StatementResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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


class AsyncRawStatementsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def retrieve_financial_statements(
        self,
        *,
        filter: typing.Optional[ListStatementsFilter] = None,
        page: typing.Optional[PaginationFilter] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StatementsResponse]:
        """
        Parameters
        ----------
        filter : typing.Optional[ListStatementsFilter]

        page : typing.Optional[PaginationFilter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StatementsResponse]
            A list of statements as part of which the DfE will make output payments for participants
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v3/statements",
            method="GET",
            params={
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=ListStatementsFilter, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(
                    object_=page, annotation=PaginationFilter, direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StatementsResponse,
                    parse_obj_as(
                        type_=StatementsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
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

    async def retrieve_a_specific_financial_statement(
        self, id: IdAttribute, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StatementResponse]:
        """
        Parameters
        ----------
        id : IdAttribute

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StatementResponse]
            A specific financial statement
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v3/statements/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StatementResponse,
                    parse_obj_as(
                        type_=StatementResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        UnauthorisedResponse,
                        parse_obj_as(
                            type_=UnauthorisedResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundResponse,
                        parse_obj_as(
                            type_=NotFoundResponse,
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
