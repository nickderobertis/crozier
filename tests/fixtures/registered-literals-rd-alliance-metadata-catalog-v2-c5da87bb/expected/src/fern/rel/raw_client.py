

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
from ..types.mscid import Mscid
from ..types.patch_relation import PatchRelation
from ..types.response_item_relation import ResponseItemRelation
from ..types.response_page_relation import ResponsePageRelation
from ..types.response_success_relation import ResponseSuccessRelation
from .types.delete_api2rel_table_int_request_table import DeleteApi2RelTableIntRequestTable
from .types.get_api2rel_table_int_request_table import GetApi2RelTableIntRequestTable
from .types.patch_api2rel_table_int_request_table import PatchApi2RelTableIntRequestTable
from .types.put_api2rel_table_int_request_table import PutApi2RelTableIntRequestTable
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRelClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_entity_relation_records(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ResponsePageRelation]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponsePageRelation]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "api2/rel",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageRelation,
                    parse_obj_as(
                        type_=ResponsePageRelation,
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

    def retrieve_an_existing_entity_relation_record(
        self,
        table: GetApi2RelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseItemRelation]:
        """
        Parameters
        ----------
        table : GetApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseItemRelation]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/rel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemRelation,
                    parse_obj_as(
                        type_=ResponseItemRelation,
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

    def modify_an_existing_entity_relation_record(
        self,
        table: PutApi2RelTableIntRequestTable,
        int_: int,
        *,
        id: typing.Optional[Mscid] = OMIT,
        parent_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        supported_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        input_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        output_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        endorsed_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        maintainers: typing.Optional[typing.Sequence[str]] = OMIT,
        funders: typing.Optional[typing.Sequence[str]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        originators: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessRelation]:
        """
        Parameters
        ----------
        table : PutApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        id : typing.Optional[Mscid]

        parent_schemes : typing.Optional[typing.Sequence[str]]
            Schemes of which the current scheme is a profile. In practice, this means either that the current scheme explicitly “borrows” elements from the parent scheme, or that all instances of the current scheme would be valid instances of the parent scheme.

        supported_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which the tool’s input metadata should conform, or output metadata does conform.

        input_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which a metadata record input to the current mapping must conform.

        output_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which metadata records output from the current mapping conform.

        endorsed_schemes : typing.Optional[typing.Sequence[str]]
            Schemes endorsed by the current endorsement.

        maintainers : typing.Optional[typing.Sequence[str]]
            Organizations that maintain the current scheme, tool or mapping.

        funders : typing.Optional[typing.Sequence[str]]
            Organizations that fund the current scheme, tool or mapping.

        users : typing.Optional[typing.Sequence[str]]
            Organizations that are known to use the current scheme.

        originators : typing.Optional[typing.Sequence[str]]
            Organizations that have made the current endorsement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessRelation]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/rel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="PUT",
            json={
                "@id": id,
                "parent schemes": parent_schemes,
                "supported schemes": supported_schemes,
                "input schemes": input_schemes,
                "output schemes": output_schemes,
                "endorsed schemes": endorsed_schemes,
                "maintainers": maintainers,
                "funders": funders,
                "users": users,
                "originators": originators,
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
                    ResponseSuccessRelation,
                    parse_obj_as(
                        type_=ResponseSuccessRelation,
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

    def remove_an_existing_entity_relation_record(
        self,
        table: DeleteApi2RelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        table : DeleteApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/rel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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

    def add_or_remove_an_individual_entity_relation(
        self,
        table: PatchApi2RelTableIntRequestTable,
        int_: int,
        *,
        request: PatchRelation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ResponseSuccessRelation]:
        """
        Parameters
        ----------
        table : PatchApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request : PatchRelation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ResponseSuccessRelation]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api2/rel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=PatchRelation, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessRelation,
                    parse_obj_as(
                        type_=ResponseSuccessRelation,
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


class AsyncRawRelClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_entity_relation_records(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ResponsePageRelation]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Include only records that match the specified criterion, which should be written in Lucene query parser syntax. Supported: quoted phrases, fields (using dots for nested fields, e.g. ‘versions.number’, and ‘=’ instead of ‘:’ for an exact match), wildcards, inclusive date ranges, NOT, OR, AND, grouping, field grouping, backslash escapes. Use the ‘thesaurus’ pseudofield to limit to schemes related (directly or indirectly) to a given concept, e.g. ‘thesaurus=concept514’.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponsePageRelation]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api2/rel",
            method="GET",
            params={
                "q": q,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponsePageRelation,
                    parse_obj_as(
                        type_=ResponsePageRelation,
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

    async def retrieve_an_existing_entity_relation_record(
        self,
        table: GetApi2RelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseItemRelation]:
        """
        Parameters
        ----------
        table : GetApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseItemRelation]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/rel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseItemRelation,
                    parse_obj_as(
                        type_=ResponseItemRelation,
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

    async def modify_an_existing_entity_relation_record(
        self,
        table: PutApi2RelTableIntRequestTable,
        int_: int,
        *,
        id: typing.Optional[Mscid] = OMIT,
        parent_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        supported_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        input_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        output_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        endorsed_schemes: typing.Optional[typing.Sequence[str]] = OMIT,
        maintainers: typing.Optional[typing.Sequence[str]] = OMIT,
        funders: typing.Optional[typing.Sequence[str]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        originators: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessRelation]:
        """
        Parameters
        ----------
        table : PutApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        id : typing.Optional[Mscid]

        parent_schemes : typing.Optional[typing.Sequence[str]]
            Schemes of which the current scheme is a profile. In practice, this means either that the current scheme explicitly “borrows” elements from the parent scheme, or that all instances of the current scheme would be valid instances of the parent scheme.

        supported_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which the tool’s input metadata should conform, or output metadata does conform.

        input_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which a metadata record input to the current mapping must conform.

        output_schemes : typing.Optional[typing.Sequence[str]]
            Schemes to which metadata records output from the current mapping conform.

        endorsed_schemes : typing.Optional[typing.Sequence[str]]
            Schemes endorsed by the current endorsement.

        maintainers : typing.Optional[typing.Sequence[str]]
            Organizations that maintain the current scheme, tool or mapping.

        funders : typing.Optional[typing.Sequence[str]]
            Organizations that fund the current scheme, tool or mapping.

        users : typing.Optional[typing.Sequence[str]]
            Organizations that are known to use the current scheme.

        originators : typing.Optional[typing.Sequence[str]]
            Organizations that have made the current endorsement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessRelation]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/rel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="PUT",
            json={
                "@id": id,
                "parent schemes": parent_schemes,
                "supported schemes": supported_schemes,
                "input schemes": input_schemes,
                "output schemes": output_schemes,
                "endorsed schemes": endorsed_schemes,
                "maintainers": maintainers,
                "funders": funders,
                "users": users,
                "originators": originators,
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
                    ResponseSuccessRelation,
                    parse_obj_as(
                        type_=ResponseSuccessRelation,
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

    async def remove_an_existing_entity_relation_record(
        self,
        table: DeleteApi2RelTableIntRequestTable,
        int_: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        table : DeleteApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/rel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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

    async def add_or_remove_an_individual_entity_relation(
        self,
        table: PatchApi2RelTableIntRequestTable,
        int_: int,
        *,
        request: PatchRelation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ResponseSuccessRelation]:
        """
        Parameters
        ----------
        table : PatchApi2RelTableIntRequestTable
            Table name portion of the MSC ID.

        int_ : int
            Numeric portion of the MSC ID.

        request : PatchRelation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ResponseSuccessRelation]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api2/rel/{encode_path_param(table)}{encode_path_param(int_)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(object_=request, annotation=PatchRelation, direction="write"),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ResponseSuccessRelation,
                    parse_obj_as(
                        type_=ResponseSuccessRelation,
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
