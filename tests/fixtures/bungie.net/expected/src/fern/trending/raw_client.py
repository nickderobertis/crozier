

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.trending_get_trending_categories_response import TrendingGetTrendingCategoriesResponse
from .types.trending_get_trending_category_response import TrendingGetTrendingCategoryResponse
from .types.trending_get_trending_entry_detail_response import TrendingGetTrendingEntryDetailResponse


class RawTrendingClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def gettrendingcategories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TrendingGetTrendingCategoriesResponse]:
        """
        Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrendingGetTrendingCategoriesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            "Trending/Categories/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrendingGetTrendingCategoriesResponse,
                    parse_obj_as(
                        type_=TrendingGetTrendingCategoriesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def gettrendingcategory(
        self, category_id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TrendingGetTrendingCategoryResponse]:
        """
        Returns paginated lists of trending items for a category.

        Parameters
        ----------
        category_id : str
            The ID of the category for whom you want additional results.

        page_number : int
            The page # of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrendingGetTrendingCategoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Trending/Categories/{jsonable_encoder(category_id)}/{jsonable_encoder(page_number)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrendingGetTrendingCategoryResponse,
                    parse_obj_as(
                        type_=TrendingGetTrendingCategoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def gettrendingentrydetail(
        self, trending_entry_type: int, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TrendingGetTrendingEntryDetailResponse]:
        """
        Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

        Parameters
        ----------
        trending_entry_type : int
            The type of entity to be returned.

        identifier : str
            The identifier for the entity to be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TrendingGetTrendingEntryDetailResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"Trending/Details/{jsonable_encoder(trending_entry_type)}/{jsonable_encoder(identifier)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrendingGetTrendingEntryDetailResponse,
                    parse_obj_as(
                        type_=TrendingGetTrendingEntryDetailResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawTrendingClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def gettrendingcategories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TrendingGetTrendingCategoriesResponse]:
        """
        Returns trending items for Bungie.net, collapsed into the first page of items per category. For pagination within a category, call GetTrendingCategory.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrendingGetTrendingCategoriesResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "Trending/Categories/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrendingGetTrendingCategoriesResponse,
                    parse_obj_as(
                        type_=TrendingGetTrendingCategoriesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def gettrendingcategory(
        self, category_id: str, page_number: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TrendingGetTrendingCategoryResponse]:
        """
        Returns paginated lists of trending items for a category.

        Parameters
        ----------
        category_id : str
            The ID of the category for whom you want additional results.

        page_number : int
            The page # of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrendingGetTrendingCategoryResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Trending/Categories/{jsonable_encoder(category_id)}/{jsonable_encoder(page_number)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrendingGetTrendingCategoryResponse,
                    parse_obj_as(
                        type_=TrendingGetTrendingCategoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def gettrendingentrydetail(
        self, trending_entry_type: int, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TrendingGetTrendingEntryDetailResponse]:
        """
        Returns the detailed results for a specific trending entry. Note that trending entries are uniquely identified by a combination of *both* the TrendingEntryType *and* the identifier: the identifier alone is not guaranteed to be globally unique.

        Parameters
        ----------
        trending_entry_type : int
            The type of entity to be returned.

        identifier : str
            The identifier for the entity to be returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TrendingGetTrendingEntryDetailResponse]
            Look at the Response property for more information about the nature of this response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"Trending/Details/{jsonable_encoder(trending_entry_type)}/{jsonable_encoder(identifier)}/",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TrendingGetTrendingEntryDetailResponse,
                    parse_obj_as(
                        type_=TrendingGetTrendingEntryDetailResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
