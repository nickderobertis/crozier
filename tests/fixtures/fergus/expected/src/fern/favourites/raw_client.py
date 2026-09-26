

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.favourites_response import FavouritesResponse
from ..types.favourites_section import FavouritesSection
from .types.get_favourites_request_representation import GetFavouritesRequestRepresentation
from .types.get_favourites_request_sort_field import GetFavouritesRequestSortField
from .types.get_favourites_request_sort_order import GetFavouritesRequestSortOrder
from pydantic import ValidationError


class RawFavouritesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_favourites(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetFavouritesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_section_name: typing.Optional[str] = None,
        sort_field: typing.Optional[GetFavouritesRequestSortField] = None,
        representation: typing.Optional[GetFavouritesRequestRepresentation] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FavouritesResponse]:
        """
        Get all favourite sections, in flat or tree view

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetFavouritesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_section_name : typing.Optional[str]
            Searchable fields:
            - representation: tree
              - `section.name`
            - representation: flat
              - `section.name`

        sort_field : typing.Optional[GetFavouritesRequestSortField]

        representation : typing.Optional[GetFavouritesRequestRepresentation]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - representation: tree
              - `section.name`
              - `lineItem.itemName`,
            - representation: flat
              - `section.name`
              - `section.description`,
              - `lineItem.itemName`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FavouritesResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "favourites",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "filterSectionName": filter_section_name,
                "sortField": sort_field,
                "representation": representation,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FavouritesResponse,
                    parse_obj_as(
                        type_=FavouritesResponse,
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

    def get_favourites_section_id(
        self, section_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FavouritesSection]:
        """
        Get a specific favourite section

        Parameters
        ----------
        section_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FavouritesSection]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"favourites/{encode_path_param(section_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FavouritesSection,
                    parse_obj_as(
                        type_=FavouritesSection,
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


class AsyncRawFavouritesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_favourites(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetFavouritesRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        filter_section_name: typing.Optional[str] = None,
        sort_field: typing.Optional[GetFavouritesRequestSortField] = None,
        representation: typing.Optional[GetFavouritesRequestRepresentation] = None,
        filter_search_text: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FavouritesResponse]:
        """
        Get all favourite sections, in flat or tree view

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetFavouritesRequestSortOrder]

        page_cursor : typing.Optional[str]

        filter_section_name : typing.Optional[str]
            Searchable fields:
            - representation: tree
              - `section.name`
            - representation: flat
              - `section.name`

        sort_field : typing.Optional[GetFavouritesRequestSortField]

        representation : typing.Optional[GetFavouritesRequestRepresentation]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - representation: tree
              - `section.name`
              - `lineItem.itemName`,
            - representation: flat
              - `section.name`
              - `section.description`,
              - `lineItem.itemName`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FavouritesResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "favourites",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "filterSectionName": filter_section_name,
                "sortField": sort_field,
                "representation": representation,
                "filterSearchText": filter_search_text,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FavouritesResponse,
                    parse_obj_as(
                        type_=FavouritesResponse,
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

    async def get_favourites_section_id(
        self, section_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FavouritesSection]:
        """
        Get a specific favourite section

        Parameters
        ----------
        section_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FavouritesSection]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"favourites/{encode_path_param(section_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FavouritesSection,
                    parse_obj_as(
                        type_=FavouritesSection,
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
