

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from .types.create_products_request_product import CreateProductsRequestProduct
from .types.create_products_request_publish_status import CreateProductsRequestPublishStatus
from .types.create_products_request_sku import CreateProductsRequestSku
from .types.create_products_response import CreateProductsResponse
from .types.create_sku_products_request_publish_status import CreateSkuProductsRequestPublishStatus
from .types.create_sku_products_request_skus_item import CreateSkuProductsRequestSkusItem
from .types.create_sku_products_response import CreateSkuProductsResponse
from .types.get_products_response import GetProductsResponse
from .types.list_products_response import ListProductsResponse
from .types.update_products_request_product import UpdateProductsRequestProduct
from .types.update_products_request_publish_status import UpdateProductsRequestPublishStatus
from .types.update_products_request_sku import UpdateProductsRequestSku
from .types.update_products_response import UpdateProductsResponse
from .types.update_sku_products_request_publish_status import UpdateSkuProductsRequestPublishStatus
from .types.update_sku_products_request_sku import UpdateSkuProductsRequestSku
from .types.update_sku_products_response import UpdateSkuProductsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProductsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListProductsResponse]:
        """
        Retrieve all products for a site.

        Use `limit` and `offset` to page through all products with subsequent requests. All SKUs for each product
        will also be fetched and returned. The `limit`, `offset` and `total` values represent Products only and do not include any SKUs.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListProductsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products",
            base_url=self._client_wrapper.get_environment().base,
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
                    ListProductsResponse,
                    parse_obj_as(
                        type_=ListProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def create(
        self,
        site_id: str,
        *,
        product: CreateProductsRequestProduct,
        sku: CreateProductsRequestSku,
        publish_status: typing.Optional[CreateProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateProductsResponse]:
        """
        Create a new ecommerce product and defaultSKU. A product, at minimum, must have a single SKU.

        To create a product with multiple SKUs:
          - First, create a list of `sku-properties`, also known as [product options](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants). For example, a T-shirt product may have a "color" `sku-property`, with a list of enum values: red, yellow, and blue, another `sku-property` may be "size", with a list of enum values: small, medium, and large.
          - Once, a product is created with a list of `sku-properties`, Webflow will create a **default SKU**, which is always a combination of the first `enum` values of each `sku-property`. (e.g. Small - Red - T-Shirt)
          - After creation, you can create additional SKUs for the product, using the [Create SKUs endpoint.](/data/reference/ecommerce/products/create-sku)

        Upon creation, the default product type will be `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product : CreateProductsRequestProduct

        sku : CreateProductsRequestSku

        publish_status : typing.Optional[CreateProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateProductsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "publishStatus": publish_status,
                "product": convert_and_respect_annotation_metadata(
                    object_=product, annotation=CreateProductsRequestProduct, direction="write"
                ),
                "sku": convert_and_respect_annotation_metadata(
                    object_=sku, annotation=CreateProductsRequestSku, direction="write"
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
                    CreateProductsResponse,
                    parse_obj_as(
                        type_=CreateProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get(
        self, site_id: str, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetProductsResponse]:
        """
        Retrieve a single product by its ID. All of its SKUs will also be
        retrieved.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProductsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products/{encode_path_param(product_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProductsResponse,
                    parse_obj_as(
                        type_=GetProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def update(
        self,
        site_id: str,
        product_id: str,
        *,
        publish_status: typing.Optional[UpdateProductsRequestPublishStatus] = OMIT,
        product: typing.Optional[UpdateProductsRequestProduct] = OMIT,
        sku: typing.Optional[UpdateProductsRequestSku] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateProductsResponse]:
        """
        Update an existing Product.

        Updating an existing Product will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        publish_status : typing.Optional[UpdateProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        product : typing.Optional[UpdateProductsRequestProduct]
            The Product object

        sku : typing.Optional[UpdateProductsRequestSku]
            The SKU object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateProductsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products/{encode_path_param(product_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "publishStatus": publish_status,
                "product": convert_and_respect_annotation_metadata(
                    object_=product, annotation=UpdateProductsRequestProduct, direction="write"
                ),
                "sku": convert_and_respect_annotation_metadata(
                    object_=sku, annotation=UpdateProductsRequestSku, direction="write"
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
                    UpdateProductsResponse,
                    parse_obj_as(
                        type_=UpdateProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def create_sku(
        self,
        site_id: str,
        product_id: str,
        *,
        skus: typing.Sequence[CreateSkuProductsRequestSkusItem],
        publish_status: typing.Optional[CreateSkuProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateSkuProductsResponse]:
        """
        Create additional SKUs to manage every [option and variant of your Product.](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants)

        Creating SKUs through the API will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        skus : typing.Sequence[CreateSkuProductsRequestSkusItem]
            An array of the SKU data your are adding

        publish_status : typing.Optional[CreateSkuProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateSkuProductsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products/{encode_path_param(product_id)}/skus",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "publishStatus": publish_status,
                "skus": convert_and_respect_annotation_metadata(
                    object_=skus, annotation=typing.Sequence[CreateSkuProductsRequestSkusItem], direction="write"
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
                    CreateSkuProductsResponse,
                    parse_obj_as(
                        type_=CreateSkuProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def update_sku(
        self,
        site_id: str,
        product_id: str,
        sku_id: str,
        *,
        sku: UpdateSkuProductsRequestSku,
        publish_status: typing.Optional[UpdateSkuProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateSkuProductsResponse]:
        """
        Update a specified SKU.

        Updating an existing SKU will set the Product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        sku_id : str
            Unique identifier for a SKU

        sku : UpdateSkuProductsRequestSku
            The SKU object

        publish_status : typing.Optional[UpdateSkuProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateSkuProductsResponse]
            Request was successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products/{encode_path_param(product_id)}/skus/{encode_path_param(sku_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "publishStatus": publish_status,
                "sku": convert_and_respect_annotation_metadata(
                    object_=sku, annotation=UpdateSkuProductsRequestSku, direction="write"
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
                    UpdateSkuProductsResponse,
                    parse_obj_as(
                        type_=UpdateSkuProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawProductsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        site_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListProductsResponse]:
        """
        Retrieve all products for a site.

        Use `limit` and `offset` to page through all products with subsequent requests. All SKUs for each product
        will also be fetched and returned. The `limit`, `offset` and `total` values represent Products only and do not include any SKUs.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        offset : typing.Optional[int]
            Offset used for pagination if the results have more than limit records

        limit : typing.Optional[int]
            Maximum number of records to be returned (max limit: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListProductsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products",
            base_url=self._client_wrapper.get_environment().base,
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
                    ListProductsResponse,
                    parse_obj_as(
                        type_=ListProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def create(
        self,
        site_id: str,
        *,
        product: CreateProductsRequestProduct,
        sku: CreateProductsRequestSku,
        publish_status: typing.Optional[CreateProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateProductsResponse]:
        """
        Create a new ecommerce product and defaultSKU. A product, at minimum, must have a single SKU.

        To create a product with multiple SKUs:
          - First, create a list of `sku-properties`, also known as [product options](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants). For example, a T-shirt product may have a "color" `sku-property`, with a list of enum values: red, yellow, and blue, another `sku-property` may be "size", with a list of enum values: small, medium, and large.
          - Once, a product is created with a list of `sku-properties`, Webflow will create a **default SKU**, which is always a combination of the first `enum` values of each `sku-property`. (e.g. Small - Red - T-Shirt)
          - After creation, you can create additional SKUs for the product, using the [Create SKUs endpoint.](/data/reference/ecommerce/products/create-sku)

        Upon creation, the default product type will be `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product : CreateProductsRequestProduct

        sku : CreateProductsRequestSku

        publish_status : typing.Optional[CreateProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateProductsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "publishStatus": publish_status,
                "product": convert_and_respect_annotation_metadata(
                    object_=product, annotation=CreateProductsRequestProduct, direction="write"
                ),
                "sku": convert_and_respect_annotation_metadata(
                    object_=sku, annotation=CreateProductsRequestSku, direction="write"
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
                    CreateProductsResponse,
                    parse_obj_as(
                        type_=CreateProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get(
        self, site_id: str, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetProductsResponse]:
        """
        Retrieve a single product by its ID. All of its SKUs will also be
        retrieved.

        Required scope | `ecommerce:read`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProductsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products/{encode_path_param(product_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProductsResponse,
                    parse_obj_as(
                        type_=GetProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def update(
        self,
        site_id: str,
        product_id: str,
        *,
        publish_status: typing.Optional[UpdateProductsRequestPublishStatus] = OMIT,
        product: typing.Optional[UpdateProductsRequestProduct] = OMIT,
        sku: typing.Optional[UpdateProductsRequestSku] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateProductsResponse]:
        """
        Update an existing Product.

        Updating an existing Product will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        publish_status : typing.Optional[UpdateProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        product : typing.Optional[UpdateProductsRequestProduct]
            The Product object

        sku : typing.Optional[UpdateProductsRequestSku]
            The SKU object

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateProductsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products/{encode_path_param(product_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "publishStatus": publish_status,
                "product": convert_and_respect_annotation_metadata(
                    object_=product, annotation=UpdateProductsRequestProduct, direction="write"
                ),
                "sku": convert_and_respect_annotation_metadata(
                    object_=sku, annotation=UpdateProductsRequestSku, direction="write"
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
                    UpdateProductsResponse,
                    parse_obj_as(
                        type_=UpdateProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def create_sku(
        self,
        site_id: str,
        product_id: str,
        *,
        skus: typing.Sequence[CreateSkuProductsRequestSkusItem],
        publish_status: typing.Optional[CreateSkuProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateSkuProductsResponse]:
        """
        Create additional SKUs to manage every [option and variant of your Product.](https://help.webflow.com/hc/en-us/articles/33961334531347-Create-product-options-and-variants)

        Creating SKUs through the API will set the product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        skus : typing.Sequence[CreateSkuProductsRequestSkusItem]
            An array of the SKU data your are adding

        publish_status : typing.Optional[CreateSkuProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateSkuProductsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products/{encode_path_param(product_id)}/skus",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "publishStatus": publish_status,
                "skus": convert_and_respect_annotation_metadata(
                    object_=skus, annotation=typing.Sequence[CreateSkuProductsRequestSkusItem], direction="write"
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
                    CreateSkuProductsResponse,
                    parse_obj_as(
                        type_=CreateSkuProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def update_sku(
        self,
        site_id: str,
        product_id: str,
        sku_id: str,
        *,
        sku: UpdateSkuProductsRequestSku,
        publish_status: typing.Optional[UpdateSkuProductsRequestPublishStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateSkuProductsResponse]:
        """
        Update a specified SKU.

        Updating an existing SKU will set the Product type to `Advanced`, which ensures all Product and SKU fields will be shown to users in the Designer.

        Required scope | `ecommerce:write`

        Parameters
        ----------
        site_id : str
            Unique identifier for a Site

        product_id : str
            Unique identifier for a Product

        sku_id : str
            Unique identifier for a SKU

        sku : UpdateSkuProductsRequestSku
            The SKU object

        publish_status : typing.Optional[UpdateSkuProductsRequestPublishStatus]
            Indicate whether your Product should be set as "staging" or "live"

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateSkuProductsResponse]
            Request was successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"sites/{encode_path_param(site_id)}/products/{encode_path_param(product_id)}/skus/{encode_path_param(sku_id)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "publishStatus": publish_status,
                "sku": convert_and_respect_annotation_metadata(
                    object_=sku, annotation=UpdateSkuProductsRequestSku, direction="write"
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
                    UpdateSkuProductsResponse,
                    parse_obj_as(
                        type_=UpdateSkuProductsResponse,
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
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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
