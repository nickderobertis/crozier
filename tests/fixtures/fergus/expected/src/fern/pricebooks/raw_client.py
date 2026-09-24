

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.get_price_book_by_id_response import GetPriceBookByIdResponse
from ..types.get_pricebook_item_by_id_response import GetPricebookItemByIdResponse
from ..types.get_pricebook_items_response import GetPricebookItemsResponse
from ..types.get_pricebooks_response import GetPricebooksResponse
from ..types.search_pricebooks_response import SearchPricebooksResponse
from .types.get_pricebooks_id_pricebook_items_request_sort_order import GetPricebooksIdPricebookItemsRequestSortOrder
from .types.get_pricebooks_request_sort_field import GetPricebooksRequestSortField
from .types.get_pricebooks_request_sort_order import GetPricebooksRequestSortOrder
from .types.post_pricebooks_search_request_sort_order import PostPricebooksSearchRequestSortOrder
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPricebooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_pricebooks_search(
        self,
        *,
        search: str,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[PostPricebooksSearchRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        pricing_tier_id: typing.Optional[float] = OMIT,
        all_suppliers: typing.Optional[bool] = OMIT,
        supplier_ids: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SearchPricebooksResponse]:
        """
        Search for pricebook items across multiple pricebooks

        This endpoint allows you to search for products/items across one or more supplier pricebooks using a text-based search query. The search is performed across item names, product codes, and search values.

        **Search Behavior:**
        - Searches match when the search term appears anywhere within searchable fields (substring matching)
        - Results are ranked by relevance (exact matches and word-start matches ranked higher)
        - Pagination uses cursor-based navigation with encoded ranking information

        **allSuppliers**

        When `allSuppliers` is provided and set to `true`, it will override the list of `supplierIds` array.

        For example the below payload will search across all suppliers for the term "hammer" and apply the pricing tier with id 123:

        ```
        {
          "search": "hammer",
          "pricingTierId": 123,
          "allSuppliers": true,
          "supplierIds": [
            101,
            102,
            103
          ]
        }
        ```

        To narrow search by specific suppliers, set `allSuppliers` to `false` and provide a list of supplier IDs:

        ```
        {
          "search": "hammer",
          "pricingTierId": 123,
          "allSuppliers": false,
          "supplierIds": [
            101,
            102,
            103
          ]
        }
        ```

        Parameters
        ----------
        search : str
            Search term for pricebook items (minimum 3 characters). Searches across:
            - `name` - Product or item name
            - `productCode` - Product identification code
            - `supplierSku` - Supplier SKU/part number

        page_size : typing.Optional[float]

        sort_order : typing.Optional[PostPricebooksSearchRequestSortOrder]

        page_cursor : typing.Optional[str]

        pricing_tier_id : typing.Optional[float]
            Filter results to show prices for a specific pricing tier ID. If not provided, the default pricing tier will be used

        all_suppliers : typing.Optional[bool]
            When true (default), searches across all supplier pricebooks. When false, only searches pricebooks specified in supplierIds

        supplier_ids : typing.Optional[typing.Sequence[float]]
            Array of supplier/pricebook IDs to limit the search scope. Only used when allSuppliers is false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SearchPricebooksResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "pricebooks/search",
            method="POST",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
            },
            json={
                "search": search,
                "pricingTierId": pricing_tier_id,
                "allSuppliers": all_suppliers,
                "supplierIds": supplier_ids,
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
                    SearchPricebooksResponse,
                    parse_obj_as(
                        type_=SearchPricebooksResponse,
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

    def get_pricebooks(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricebooksRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPricebooksRequestSortField] = None,
        filter_supplier_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPricebooksResponse]:
        """
        Schema for Pricebooks

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricebooksRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPricebooksRequestSortField]

        filter_supplier_name : typing.Optional[str]
            Filter pricebooks by supplier name containing this string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPricebooksResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "pricebooks",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSupplierName": filter_supplier_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricebooksResponse,
                    parse_obj_as(
                        type_=GetPricebooksResponse,
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

    def get_pricebooks_id(
        self, id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetPriceBookByIdResponse]:
        """
        Schema for a Pricebook by ID

        Parameters
        ----------
        id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPriceBookByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricebooks/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPriceBookByIdResponse,
                    parse_obj_as(
                        type_=GetPriceBookByIdResponse,
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

    def get_pricebooks_id_pricebook_items(
        self,
        id: float,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricebooksIdPricebookItemsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPricebookItemsResponse]:
        """
        Schema for Pricebook Items

        Parameters
        ----------
        id : float

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricebooksIdPricebookItemsRequestSortOrder]

        page_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPricebookItemsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricebooks/{encode_path_param(id)}/pricebookItems",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricebookItemsResponse,
                    parse_obj_as(
                        type_=GetPricebookItemsResponse,
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

    def get_pricebooks_id_pricebook_items_pricebook_item_id(
        self,
        id: float,
        pricebook_item_id: float,
        *,
        filter_pricing_tier_id: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetPricebookItemByIdResponse]:
        """
        Schema for a Pricebook Item by ID

        Parameters
        ----------
        id : float

        pricebook_item_id : float

        filter_pricing_tier_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetPricebookItemByIdResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricebooks/{encode_path_param(id)}/pricebookItems/{encode_path_param(pricebook_item_id)}",
            method="GET",
            params={
                "filterPricingTierId": filter_pricing_tier_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricebookItemByIdResponse,
                    parse_obj_as(
                        type_=GetPricebookItemByIdResponse,
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


class AsyncRawPricebooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_pricebooks_search(
        self,
        *,
        search: str,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[PostPricebooksSearchRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        pricing_tier_id: typing.Optional[float] = OMIT,
        all_suppliers: typing.Optional[bool] = OMIT,
        supplier_ids: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SearchPricebooksResponse]:
        """
        Search for pricebook items across multiple pricebooks

        This endpoint allows you to search for products/items across one or more supplier pricebooks using a text-based search query. The search is performed across item names, product codes, and search values.

        **Search Behavior:**
        - Searches match when the search term appears anywhere within searchable fields (substring matching)
        - Results are ranked by relevance (exact matches and word-start matches ranked higher)
        - Pagination uses cursor-based navigation with encoded ranking information

        **allSuppliers**

        When `allSuppliers` is provided and set to `true`, it will override the list of `supplierIds` array.

        For example the below payload will search across all suppliers for the term "hammer" and apply the pricing tier with id 123:

        ```
        {
          "search": "hammer",
          "pricingTierId": 123,
          "allSuppliers": true,
          "supplierIds": [
            101,
            102,
            103
          ]
        }
        ```

        To narrow search by specific suppliers, set `allSuppliers` to `false` and provide a list of supplier IDs:

        ```
        {
          "search": "hammer",
          "pricingTierId": 123,
          "allSuppliers": false,
          "supplierIds": [
            101,
            102,
            103
          ]
        }
        ```

        Parameters
        ----------
        search : str
            Search term for pricebook items (minimum 3 characters). Searches across:
            - `name` - Product or item name
            - `productCode` - Product identification code
            - `supplierSku` - Supplier SKU/part number

        page_size : typing.Optional[float]

        sort_order : typing.Optional[PostPricebooksSearchRequestSortOrder]

        page_cursor : typing.Optional[str]

        pricing_tier_id : typing.Optional[float]
            Filter results to show prices for a specific pricing tier ID. If not provided, the default pricing tier will be used

        all_suppliers : typing.Optional[bool]
            When true (default), searches across all supplier pricebooks. When false, only searches pricebooks specified in supplierIds

        supplier_ids : typing.Optional[typing.Sequence[float]]
            Array of supplier/pricebook IDs to limit the search scope. Only used when allSuppliers is false

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SearchPricebooksResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pricebooks/search",
            method="POST",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
            },
            json={
                "search": search,
                "pricingTierId": pricing_tier_id,
                "allSuppliers": all_suppliers,
                "supplierIds": supplier_ids,
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
                    SearchPricebooksResponse,
                    parse_obj_as(
                        type_=SearchPricebooksResponse,
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

    async def get_pricebooks(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricebooksRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPricebooksRequestSortField] = None,
        filter_supplier_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPricebooksResponse]:
        """
        Schema for Pricebooks

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricebooksRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPricebooksRequestSortField]

        filter_supplier_name : typing.Optional[str]
            Filter pricebooks by supplier name containing this string

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPricebooksResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pricebooks",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSupplierName": filter_supplier_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricebooksResponse,
                    parse_obj_as(
                        type_=GetPricebooksResponse,
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

    async def get_pricebooks_id(
        self, id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetPriceBookByIdResponse]:
        """
        Schema for a Pricebook by ID

        Parameters
        ----------
        id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPriceBookByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricebooks/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPriceBookByIdResponse,
                    parse_obj_as(
                        type_=GetPriceBookByIdResponse,
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

    async def get_pricebooks_id_pricebook_items(
        self,
        id: float,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPricebooksIdPricebookItemsRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPricebookItemsResponse]:
        """
        Schema for Pricebook Items

        Parameters
        ----------
        id : float

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPricebooksIdPricebookItemsRequestSortOrder]

        page_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPricebookItemsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricebooks/{encode_path_param(id)}/pricebookItems",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricebookItemsResponse,
                    parse_obj_as(
                        type_=GetPricebookItemsResponse,
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

    async def get_pricebooks_id_pricebook_items_pricebook_item_id(
        self,
        id: float,
        pricebook_item_id: float,
        *,
        filter_pricing_tier_id: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetPricebookItemByIdResponse]:
        """
        Schema for a Pricebook Item by ID

        Parameters
        ----------
        id : float

        pricebook_item_id : float

        filter_pricing_tier_id : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetPricebookItemByIdResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricebooks/{encode_path_param(id)}/pricebookItems/{encode_path_param(pricebook_item_id)}",
            method="GET",
            params={
                "filterPricingTierId": filter_pricing_tier_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetPricebookItemByIdResponse,
                    parse_obj_as(
                        type_=GetPricebookItemByIdResponse,
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
