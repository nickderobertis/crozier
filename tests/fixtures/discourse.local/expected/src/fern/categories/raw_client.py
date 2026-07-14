

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.create_category_request_permissions import CreateCategoryRequestPermissions
from .types.create_category_response import CreateCategoryResponse
from .types.get_category_response import GetCategoryResponse
from .types.list_categories_response import ListCategoriesResponse
from .types.list_category_topics_response import ListCategoryTopicsResponse
from .types.update_category_request_permissions import UpdateCategoryRequestPermissions
from .types.update_category_response import UpdateCategoryResponse


OMIT = typing.cast(typing.Any, ...)


class RawCategoriesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_category(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetCategoryResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetCategoryResponse]
            response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"c/{jsonable_encoder(id)}/show.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCategoryResponse,
                    parse_obj_as(
                        type_=GetCategoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_category_topics(
        self, slug: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListCategoryTopicsResponse]:
        """
        Parameters
        ----------
        slug : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCategoryTopicsResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"c/{jsonable_encoder(slug)}/{jsonable_encoder(id)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCategoryTopicsResponse,
                    parse_obj_as(
                        type_=ListCategoryTopicsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_categories(
        self,
        *,
        include_subcategories: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCategoriesResponse]:
        """
        Parameters
        ----------
        include_subcategories : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCategoriesResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "categories.json",
            method="GET",
            params={
                "include_subcategories": include_subcategories,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCategoriesResponse,
                    parse_obj_as(
                        type_=ListCategoriesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_category(
        self,
        *,
        name: str,
        allow_badges: typing.Optional[bool] = OMIT,
        color: typing.Optional[str] = OMIT,
        form_template_ids: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        parent_category_id: typing.Optional[int] = OMIT,
        permissions: typing.Optional[CreateCategoryRequestPermissions] = OMIT,
        search_priority: typing.Optional[int] = OMIT,
        slug: typing.Optional[str] = OMIT,
        text_color: typing.Optional[str] = OMIT,
        topic_featured_links_allowed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCategoryResponse]:
        """
        Parameters
        ----------
        name : str

        allow_badges : typing.Optional[bool]

        color : typing.Optional[str]

        form_template_ids : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        parent_category_id : typing.Optional[int]

        permissions : typing.Optional[CreateCategoryRequestPermissions]

        search_priority : typing.Optional[int]

        slug : typing.Optional[str]

        text_color : typing.Optional[str]

        topic_featured_links_allowed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateCategoryResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "categories.json",
            method="POST",
            json={
                "allow_badges": allow_badges,
                "color": color,
                "form_template_ids": form_template_ids,
                "name": name,
                "parent_category_id": parent_category_id,
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions, annotation=CreateCategoryRequestPermissions, direction="write"
                ),
                "search_priority": search_priority,
                "slug": slug,
                "text_color": text_color,
                "topic_featured_links_allowed": topic_featured_links_allowed,
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
                    CreateCategoryResponse,
                    parse_obj_as(
                        type_=CreateCategoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_category(
        self,
        id: int,
        *,
        name: str,
        allow_badges: typing.Optional[bool] = OMIT,
        color: typing.Optional[str] = OMIT,
        form_template_ids: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        parent_category_id: typing.Optional[int] = OMIT,
        permissions: typing.Optional[UpdateCategoryRequestPermissions] = OMIT,
        search_priority: typing.Optional[int] = OMIT,
        slug: typing.Optional[str] = OMIT,
        text_color: typing.Optional[str] = OMIT,
        topic_featured_links_allowed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateCategoryResponse]:
        """
        Parameters
        ----------
        id : int

        name : str

        allow_badges : typing.Optional[bool]

        color : typing.Optional[str]

        form_template_ids : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        parent_category_id : typing.Optional[int]

        permissions : typing.Optional[UpdateCategoryRequestPermissions]

        search_priority : typing.Optional[int]

        slug : typing.Optional[str]

        text_color : typing.Optional[str]

        topic_featured_links_allowed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateCategoryResponse]
            success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"categories/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "allow_badges": allow_badges,
                "color": color,
                "form_template_ids": form_template_ids,
                "name": name,
                "parent_category_id": parent_category_id,
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions, annotation=UpdateCategoryRequestPermissions, direction="write"
                ),
                "search_priority": search_priority,
                "slug": slug,
                "text_color": text_color,
                "topic_featured_links_allowed": topic_featured_links_allowed,
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
                    UpdateCategoryResponse,
                    parse_obj_as(
                        type_=UpdateCategoryResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCategoriesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_category(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetCategoryResponse]:
        """
        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetCategoryResponse]
            response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"c/{jsonable_encoder(id)}/show.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetCategoryResponse,
                    parse_obj_as(
                        type_=GetCategoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_category_topics(
        self, slug: str, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListCategoryTopicsResponse]:
        """
        Parameters
        ----------
        slug : str

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCategoryTopicsResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"c/{jsonable_encoder(slug)}/{jsonable_encoder(id)}.json",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCategoryTopicsResponse,
                    parse_obj_as(
                        type_=ListCategoryTopicsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_categories(
        self,
        *,
        include_subcategories: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCategoriesResponse]:
        """
        Parameters
        ----------
        include_subcategories : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCategoriesResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "categories.json",
            method="GET",
            params={
                "include_subcategories": include_subcategories,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCategoriesResponse,
                    parse_obj_as(
                        type_=ListCategoriesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_category(
        self,
        *,
        name: str,
        allow_badges: typing.Optional[bool] = OMIT,
        color: typing.Optional[str] = OMIT,
        form_template_ids: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        parent_category_id: typing.Optional[int] = OMIT,
        permissions: typing.Optional[CreateCategoryRequestPermissions] = OMIT,
        search_priority: typing.Optional[int] = OMIT,
        slug: typing.Optional[str] = OMIT,
        text_color: typing.Optional[str] = OMIT,
        topic_featured_links_allowed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCategoryResponse]:
        """
        Parameters
        ----------
        name : str

        allow_badges : typing.Optional[bool]

        color : typing.Optional[str]

        form_template_ids : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        parent_category_id : typing.Optional[int]

        permissions : typing.Optional[CreateCategoryRequestPermissions]

        search_priority : typing.Optional[int]

        slug : typing.Optional[str]

        text_color : typing.Optional[str]

        topic_featured_links_allowed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateCategoryResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "categories.json",
            method="POST",
            json={
                "allow_badges": allow_badges,
                "color": color,
                "form_template_ids": form_template_ids,
                "name": name,
                "parent_category_id": parent_category_id,
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions, annotation=CreateCategoryRequestPermissions, direction="write"
                ),
                "search_priority": search_priority,
                "slug": slug,
                "text_color": text_color,
                "topic_featured_links_allowed": topic_featured_links_allowed,
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
                    CreateCategoryResponse,
                    parse_obj_as(
                        type_=CreateCategoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_category(
        self,
        id: int,
        *,
        name: str,
        allow_badges: typing.Optional[bool] = OMIT,
        color: typing.Optional[str] = OMIT,
        form_template_ids: typing.Optional[typing.Sequence[typing.Optional[typing.Any]]] = OMIT,
        parent_category_id: typing.Optional[int] = OMIT,
        permissions: typing.Optional[UpdateCategoryRequestPermissions] = OMIT,
        search_priority: typing.Optional[int] = OMIT,
        slug: typing.Optional[str] = OMIT,
        text_color: typing.Optional[str] = OMIT,
        topic_featured_links_allowed: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateCategoryResponse]:
        """
        Parameters
        ----------
        id : int

        name : str

        allow_badges : typing.Optional[bool]

        color : typing.Optional[str]

        form_template_ids : typing.Optional[typing.Sequence[typing.Optional[typing.Any]]]

        parent_category_id : typing.Optional[int]

        permissions : typing.Optional[UpdateCategoryRequestPermissions]

        search_priority : typing.Optional[int]

        slug : typing.Optional[str]

        text_color : typing.Optional[str]

        topic_featured_links_allowed : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateCategoryResponse]
            success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"categories/{jsonable_encoder(id)}.json",
            method="PUT",
            json={
                "allow_badges": allow_badges,
                "color": color,
                "form_template_ids": form_template_ids,
                "name": name,
                "parent_category_id": parent_category_id,
                "permissions": convert_and_respect_annotation_metadata(
                    object_=permissions, annotation=UpdateCategoryRequestPermissions, direction="write"
                ),
                "search_priority": search_priority,
                "slug": slug,
                "text_color": text_color,
                "topic_featured_links_allowed": topic_featured_links_allowed,
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
                    UpdateCategoryResponse,
                    parse_obj_as(
                        type_=UpdateCategoryResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
