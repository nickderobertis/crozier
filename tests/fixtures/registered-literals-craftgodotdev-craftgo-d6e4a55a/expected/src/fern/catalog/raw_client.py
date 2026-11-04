

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.cents import Cents
from ..types.create_product_resp_body import CreateProductRespBody
from ..types.currency_code import CurrencyCode
from ..types.delete_product_resp_body import DeleteProductRespBody
from ..types.get_product_resp_body import GetProductRespBody
from ..types.list_categories_resp_body import ListCategoriesRespBody
from ..types.list_products_resp_body import ListProductsRespBody
from ..types.non_empty_id import NonEmptyId
from ..types.sku import Sku
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCatalogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_categories(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCategoriesRespBody]:
        """
        List categories.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCategoriesRespBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "catalog/categories",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCategoriesRespBody,
                    parse_obj_as(
                        type_=ListCategoriesRespBody,
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

    def list_products(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListProductsRespBody]:
        """
        List products with cursor pagination.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        category : typing.Optional[str]

        tag : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListProductsRespBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "catalog/products",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "category": category,
                "tag": tag,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListProductsRespBody,
                    parse_obj_as(
                        type_=ListProductsRespBody,
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

    def create_product(
        self,
        *,
        category_id: NonEmptyId,
        name: str,
        price_cents: Cents,
        sku: Sku,
        currency: typing.Optional[CurrencyCode] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateProductRespBody]:
        """
        Create a product (admin only).

        Parameters
        ----------
        category_id : NonEmptyId

        name : str

        price_cents : Cents

        sku : Sku

        currency : typing.Optional[CurrencyCode]

        description : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateProductRespBody]
            Created
        """
        _response = self._client_wrapper.httpx_client.request(
            "catalog/products",
            method="POST",
            json={
                "categoryId": category_id,
                "currency": currency,
                "description": description,
                "name": name,
                "priceCents": price_cents,
                "sku": sku,
                "tags": tags,
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
                    CreateProductRespBody,
                    parse_obj_as(
                        type_=CreateProductRespBody,
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

    def get_product(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetProductRespBody]:
        """
        Fetch one product by id.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProductRespBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/products/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProductRespBody,
                    parse_obj_as(
                        type_=GetProductRespBody,
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

    def delete_product(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteProductRespBody]:
        """
        Delete a product (admin only).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteProductRespBody]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"catalog/products/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteProductRespBody,
                    parse_obj_as(
                        type_=DeleteProductRespBody,
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


class AsyncRawCatalogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_categories(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCategoriesRespBody]:
        """
        List categories.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCategoriesRespBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "catalog/categories",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCategoriesRespBody,
                    parse_obj_as(
                        type_=ListCategoriesRespBody,
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

    async def list_products(
        self,
        *,
        limit: int,
        cursor: typing.Optional[str] = None,
        category: typing.Optional[str] = None,
        tag: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListProductsRespBody]:
        """
        List products with cursor pagination.

        Parameters
        ----------
        limit : int

        cursor : typing.Optional[str]

        category : typing.Optional[str]

        tag : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListProductsRespBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "catalog/products",
            method="GET",
            params={
                "cursor": cursor,
                "limit": limit,
                "category": category,
                "tag": tag,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListProductsRespBody,
                    parse_obj_as(
                        type_=ListProductsRespBody,
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

    async def create_product(
        self,
        *,
        category_id: NonEmptyId,
        name: str,
        price_cents: Cents,
        sku: Sku,
        currency: typing.Optional[CurrencyCode] = OMIT,
        description: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateProductRespBody]:
        """
        Create a product (admin only).

        Parameters
        ----------
        category_id : NonEmptyId

        name : str

        price_cents : Cents

        sku : Sku

        currency : typing.Optional[CurrencyCode]

        description : typing.Optional[str]

        tags : typing.Optional[typing.Sequence[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateProductRespBody]
            Created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "catalog/products",
            method="POST",
            json={
                "categoryId": category_id,
                "currency": currency,
                "description": description,
                "name": name,
                "priceCents": price_cents,
                "sku": sku,
                "tags": tags,
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
                    CreateProductRespBody,
                    parse_obj_as(
                        type_=CreateProductRespBody,
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

    async def get_product(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetProductRespBody]:
        """
        Fetch one product by id.

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProductRespBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/products/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProductRespBody,
                    parse_obj_as(
                        type_=GetProductRespBody,
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

    async def delete_product(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteProductRespBody]:
        """
        Delete a product (admin only).

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteProductRespBody]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"catalog/products/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteProductRespBody,
                    parse_obj_as(
                        type_=DeleteProductRespBody,
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
