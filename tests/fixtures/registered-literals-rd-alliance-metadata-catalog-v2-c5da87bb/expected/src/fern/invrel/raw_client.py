

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
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.patch_inv_relation import PatchInvRelation
from ..types.response_item_inv_relation import ResponseItemInvRelation
from ..types.response_page_inv_relation import ResponsePageInvRelation
from ..types.response_success_inv_relation import ResponseSuccessInvRelation
from .types.get_api2invrel_table_int_request_table import GetApi2InvrelTableIntRequestTable
from .types.patch_api2invrel_table_int_request_table import PatchApi2InvrelTableIntRequestTable
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInvrelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_virtual_records_of_inverse_entity_relations(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponsePageInvRelation]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponsePageInvRelation]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/invrel",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageInvRelation,
                    parse_obj_as(
                        type_=ResponsePageInvRelation,
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

    def retrieve_a_virtual_record_of_inverse_entity_relations(
        self,
        table: GetApi2InvrelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseItemInvRelation]:
        """
        Parameters
        ----------
        table : GetApi2InvrelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseItemInvRelation]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/invrel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemInvRelation,
                    parse_obj_as(
                        type_=ResponseItemInvRelation,
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

    def add_or_remove_an_individual_entity_relation(
        self,
        table: PatchApi2InvrelTableIntRequestTable,
        int_: int,
        *,
        request: PatchInvRelation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessInvRelation]:
        """
        Parameters
        ----------
        table : PatchApi2InvrelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request : PatchInvRelation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessInvRelation]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/invrel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PatchInvRelation, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessInvRelation,
                    parse_obj_as(
                        type_=ResponseSuccessInvRelation,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawInvrelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_virtual_records_of_inverse_entity_relations(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponsePageInvRelation]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponsePageInvRelation]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/invrel",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageInvRelation,
                    parse_obj_as(
                        type_=ResponsePageInvRelation,
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

    async def retrieve_a_virtual_record_of_inverse_entity_relations(
        self,
        table: GetApi2InvrelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseItemInvRelation]:
        """
        Parameters
        ----------
        table : GetApi2InvrelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseItemInvRelation]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/invrel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemInvRelation,
                    parse_obj_as(
                        type_=ResponseItemInvRelation,
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

    async def add_or_remove_an_individual_entity_relation(
        self,
        table: PatchApi2InvrelTableIntRequestTable,
        int_: int,
        *,
        request: PatchInvRelation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessInvRelation]:
        """
        Parameters
        ----------
        table : PatchApi2InvrelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request : PatchInvRelation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessInvRelation]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/invrel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PatchInvRelation, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessInvRelation,
                    parse_obj_as(
                        type_=ResponseSuccessInvRelation,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
