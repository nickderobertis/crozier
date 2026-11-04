

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_acceptable_error import NotAcceptableError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unsupported_media_type_error import UnsupportedMediaTypeError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.paginated_response_of_guid import PaginatedResponseOfGuid
from .types.add_guid_alias_request_alias_type import AddGuidAliasRequestAliasType
from .types.get_guid_alias_types_response_item import GetGuidAliasTypesResponseItem
from .types.remove_guid_alias_request_alias_type import RemoveGuidAliasRequestAliasType
from .types.search_by_alias_request_alias_type import SearchByAliasRequestAliasType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAliasClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_guid_aliases(
        self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Dict[str, str]]:
        """
        Looks up the alias for each alias type (group and single) and returns a map of all aliases found.

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/id4ns/{encode_path_param(id4n)}/alias",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, str],
                    parse_obj_as(
                        type_=typing.Dict[str, str],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def add_guid_alias(
        self,
        id4n: str,
        alias_type: AddGuidAliasRequestAliasType,
        *,
        alias: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Adds or replaces aliases for single ID4ns (alias type item and mapp) or groups of ID4ns (alias types gtin, ean and article)

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        alias_type : AddGuidAliasRequestAliasType
            Alias type, see the corresponding API model

        alias : str
            An alias

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/id4ns/{encode_path_param(id4n)}/alias/{encode_path_param(alias_type)}",
            method="POST",
            json={
                "alias": alias,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def remove_guid_alias(
        self,
        id4n: str,
        alias_type: RemoveGuidAliasRequestAliasType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Remove the alias of the given type

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        alias_type : RemoveGuidAliasRequestAliasType
            Alias type, see the corresponding API model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1/id4ns/{encode_path_param(id4n)}/alias/{encode_path_param(alias_type)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def search_by_alias(
        self,
        *,
        alias: str,
        alias_type: SearchByAliasRequestAliasType,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaginatedResponseOfGuid]:
        """
        Parameters
        ----------
        alias : str
            The alias to search for

        alias_type : SearchByAliasRequestAliasType
            Alias type type to search for

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaginatedResponseOfGuid]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/search/guids",
            method="GET",
            params={
                "alias": alias,
                "aliasType": alias_type,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResponseOfGuid,
                    parse_obj_as(
                        type_=PaginatedResponseOfGuid,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def get_guid_alias_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetGuidAliasTypesResponseItem]]:
        """
        Retrieve this list to find out all alias types to use with alias search and change operations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetGuidAliasTypesResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/search/guids/aliases/types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetGuidAliasTypesResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetGuidAliasTypesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )


class AsyncRawAliasClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_guid_aliases(
        self, id4n: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Dict[str, str]]:
        """
        Looks up the alias for each alias type (group and single) and returns a map of all aliases found.

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/id4ns/{encode_path_param(id4n)}/alias",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Dict[str, str],
                    parse_obj_as(
                        type_=typing.Dict[str, str],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def add_guid_alias(
        self,
        id4n: str,
        alias_type: AddGuidAliasRequestAliasType,
        *,
        alias: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Adds or replaces aliases for single ID4ns (alias type item and mapp) or groups of ID4ns (alias types gtin, ean and article)

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        alias_type : AddGuidAliasRequestAliasType
            Alias type, see the corresponding API model

        alias : str
            An alias

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/id4ns/{encode_path_param(id4n)}/alias/{encode_path_param(alias_type)}",
            method="POST",
            json={
                "alias": alias,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def remove_guid_alias(
        self,
        id4n: str,
        alias_type: RemoveGuidAliasRequestAliasType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Remove the alias of the given type

        Parameters
        ----------
        id4n : str
            The GUID or Collection to operate on

        alias_type : RemoveGuidAliasRequestAliasType
            Alias type, see the corresponding API model

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1/id4ns/{encode_path_param(id4n)}/alias/{encode_path_param(alias_type)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def search_by_alias(
        self,
        *,
        alias: str,
        alias_type: SearchByAliasRequestAliasType,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaginatedResponseOfGuid]:
        """
        Parameters
        ----------
        alias : str
            The alias to search for

        alias_type : SearchByAliasRequestAliasType
            Alias type type to search for

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaginatedResponseOfGuid]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/search/guids",
            method="GET",
            params={
                "alias": alias,
                "aliasType": alias_type,
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaginatedResponseOfGuid,
                    parse_obj_as(
                        type_=PaginatedResponseOfGuid,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def get_guid_alias_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetGuidAliasTypesResponseItem]]:
        """
        Retrieve this list to find out all alias types to use with alias search and change operations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetGuidAliasTypesResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/search/guids/aliases/types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetGuidAliasTypesResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetGuidAliasTypesResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
            if _response.status_code == 403:
                raise ForbiddenError(
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
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 406:
                raise NotAcceptableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 415:
                raise UnsupportedMediaTypeError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )
