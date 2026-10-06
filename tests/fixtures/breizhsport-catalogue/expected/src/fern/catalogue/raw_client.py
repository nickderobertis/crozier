

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.get_api_catalogue_response import GetApiCatalogueResponse
from .types.post_api_catalogue_response import PostApiCatalogueResponse
from .types.put_api_catalogue_quantity_response import PutApiCatalogueQuantityResponse
from .types.update_item_items_item import UpdateItemItemsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCatalogueClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_articles(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetApiCatalogueResponse]:
        """
        Retrieves a list of articles with optional pagination.

        Parameters
        ----------
        offset : typing.Optional[int]
            Offset for pagination

        limit : typing.Optional[int]
            Maximum number of articles to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetApiCatalogueResponse]
            List of articles
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/catalogue",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiCatalogueResponse,
                    parse_obj_as(
                        type_=GetApiCatalogueResponse,
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

    def create_an_article(
        self,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        price: typing.Optional[typing.Any] = OMIT,
        quantity: typing.Optional[typing.Any] = OMIT,
        brand: typing.Optional[str] = OMIT,
        rating: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostApiCatalogueResponse]:
        """
        Creates a new article in the catalogue.

        Parameters
        ----------
        title : typing.Optional[str]

        description : typing.Optional[str]

        image : typing.Optional[str]

        price : typing.Optional[typing.Any]

        quantity : typing.Optional[typing.Any]

        brand : typing.Optional[str]

        rating : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostApiCatalogueResponse]
            Article created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/catalogue",
            method="POST",
            json={
                "title": title,
                "description": description,
                "image": image,
                "price": price,
                "quantity": quantity,
                "brand": brand,
                "rating": rating,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiCatalogueResponse,
                    parse_obj_as(
                        type_=PostApiCatalogueResponse,
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

    def update_article_quantities(
        self,
        *,
        order_id: typing.Optional[str] = OMIT,
        items: typing.Optional[typing.Sequence[UpdateItemItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PutApiCatalogueQuantityResponse]:
        """
        Updates the quantities of multiple articles.

        Parameters
        ----------
        order_id : typing.Optional[str]

        items : typing.Optional[typing.Sequence[UpdateItemItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PutApiCatalogueQuantityResponse]
            Articles updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/catalogue/quantity",
            method="PUT",
            json={
                "orderId": order_id,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[UpdateItemItemsItem], direction="write"
                ),
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
                    PutApiCatalogueQuantityResponse,
                    parse_obj_as(
                        type_=PutApiCatalogueQuantityResponse,
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


class AsyncRawCatalogueClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_articles(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetApiCatalogueResponse]:
        """
        Retrieves a list of articles with optional pagination.

        Parameters
        ----------
        offset : typing.Optional[int]
            Offset for pagination

        limit : typing.Optional[int]
            Maximum number of articles to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetApiCatalogueResponse]
            List of articles
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/catalogue",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetApiCatalogueResponse,
                    parse_obj_as(
                        type_=GetApiCatalogueResponse,
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

    async def create_an_article(
        self,
        *,
        title: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        image: typing.Optional[str] = OMIT,
        price: typing.Optional[typing.Any] = OMIT,
        quantity: typing.Optional[typing.Any] = OMIT,
        brand: typing.Optional[str] = OMIT,
        rating: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostApiCatalogueResponse]:
        """
        Creates a new article in the catalogue.

        Parameters
        ----------
        title : typing.Optional[str]

        description : typing.Optional[str]

        image : typing.Optional[str]

        price : typing.Optional[typing.Any]

        quantity : typing.Optional[typing.Any]

        brand : typing.Optional[str]

        rating : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostApiCatalogueResponse]
            Article created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/catalogue",
            method="POST",
            json={
                "title": title,
                "description": description,
                "image": image,
                "price": price,
                "quantity": quantity,
                "brand": brand,
                "rating": rating,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostApiCatalogueResponse,
                    parse_obj_as(
                        type_=PostApiCatalogueResponse,
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

    async def update_article_quantities(
        self,
        *,
        order_id: typing.Optional[str] = OMIT,
        items: typing.Optional[typing.Sequence[UpdateItemItemsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PutApiCatalogueQuantityResponse]:
        """
        Updates the quantities of multiple articles.

        Parameters
        ----------
        order_id : typing.Optional[str]

        items : typing.Optional[typing.Sequence[UpdateItemItemsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PutApiCatalogueQuantityResponse]
            Articles updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/catalogue/quantity",
            method="PUT",
            json={
                "orderId": order_id,
                "items": convert_and_respect_annotation_metadata(
                    object_=items, annotation=typing.Sequence[UpdateItemItemsItem], direction="write"
                ),
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
                    PutApiCatalogueQuantityResponse,
                    parse_obj_as(
                        type_=PutApiCatalogueQuantityResponse,
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
