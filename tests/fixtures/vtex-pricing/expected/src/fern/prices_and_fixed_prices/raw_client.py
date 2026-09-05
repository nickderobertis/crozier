

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
from ..types.fixed_price import FixedPrice
from ..types.getcomputedprice import Getcomputedprice
from ..types.getprice import Getprice
from .types.create_update_price_or_fixed_price_request_fixed_prices_item import (
    CreateUpdatePriceOrFixedPriceRequestFixedPricesItem,
)
from .types.createorupdatefixedpricesonpricetableortradepolicy_request_body_item import (
    CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPricesAndFixedPricesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_price(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Getprice]:
        """
        Retrieves price data given a specific SKU ID. Within the `fixedPrices` object, there might be a list of prices for specific Trade Policies and Minimium Quantities of the SKU. Fixed Prices may also be scheduled.

         ## Response body example

        ```json
        {
            "itemId": "1",
            "listPrice": 50,
            "costPrice": 90,
            "markup": 30,
            "basePrice": 117,
            "fixedPrices": [
                {
                    "tradePolicyId": "1",
                    "value": 50.5,
                    "listPrice": 50.5,
                    "minQuantity": 2,
                    "dateRange": {
                        "from": "2021-12-31T01:00:00Z",
                        "to": "2022-12-31T01:00:00Z"
                    }
                },
                {
                    "tradePolicyId": "2",
                    "value": 30,
                    "listPrice": 50,
                    "minQuantity": 2
                }
            ]
        }
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Getprice]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Getprice,
                    parse_obj_as(
                        type_=Getprice,
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

    def create_update_price_or_fixed_price(
        self,
        item_id: int,
        *,
        base_price: float,
        list_price: float,
        markup: int,
        cost_price: typing.Optional[float] = OMIT,
        fixed_prices: typing.Optional[typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Creates or updates an SKU Base Price or Fixed Prices. The **base price** is the basic selling price of a product, it comprises the cost price and the markup wanted in the sale of the product. The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated.

         <p> You may optionally set a list price. Additionally, you may set either a cost price or a markup value. By defining either one of them, the other will be calculated to conform to the formula <code>costPrice * (1 + markup) = basePrice</code>.</p> <h2>Request body example</h2>

        ```json
        {
            "markup": 30,
            "basePrice": 100,
            "listPrice": 35,
            "fixedPrices": [
                {
                    "tradePolicyId": "1",
                    "value": 31,
                    "listPrice": 32,
                    "minQuantity": 1,
                    "dateRange": {
                        "from": "2022-05-21T22:00:00Z",
                        "to": "2023-05-28T22:00:00Z"
                    }
                },
                {
                    "tradePolicyId": "1",
                    "value": 31.5,
                    "listPrice": 33,
                    "minQuantity": 2
                }
            ]
        }
        ```

        Parameters
        ----------
        item_id : int
            SKU unique identifier number.

        base_price : float
            SKU selling base price. If you decide to fill only the `basePrice` item, the `markup` and `costPrice` will be automatically generated to adapt to the number inserted in `basePrice`.

        list_price : float
            SKU's suggested selling price.

        markup : int
            The profit percentage that is to be obtained from the sale of that SKU. If you decide to fill the `markup` item, you must also fill the `costPrice`. The `basePrice` will be automatically generated based on both values.

        cost_price : typing.Optional[float]
            SKU selling cost price. If you decide to fill the `costPrice` item, you must also fill the `markup` and `basePrice` will be automatically generated based on both values.

        fixed_prices : typing.Optional[typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "basePrice": base_price,
                "costPrice": cost_price,
                "fixedPrices": convert_and_respect_annotation_metadata(
                    object_=fixed_prices,
                    annotation=typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem],
                    direction="write",
                ),
                "listPrice": list_price,
                "markup": markup,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_price(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes the Base Price and all available Fixed Prices for an SKU in all trade policies.

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_computed_pricebypricetable(
        self,
        item_id: int,
        price_table_id: str,
        *,
        category_ids: int,
        brand_id: int,
        quantity: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Getcomputedprice]:
        """
        Gets the Computed Price, which is the price after all the steps in the Pricing pipeline, for an SKU in a specific price table or trade policy.

        ## Response body example

        ```json
        {
            "tradePolicyId": "1",
            "listPrice": 30,
            "costPrice": 76.92,
            "sellingPrice": 18.9,
            "priceValidUntil": "2018-12-20T18:12:14Z"
        }
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            SKU Price Table Name.

        category_ids : int
            Category ID.

        brand_id : int
            Brand ID.

        quantity : int
            SKU quantity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Getcomputedprice]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/computed/{encode_path_param(price_table_id)}",
            method="GET",
            params={
                "categoryIds": category_ids,
                "brandId": brand_id,
                "quantity": quantity,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Getcomputedprice,
                    parse_obj_as(
                        type_=Getcomputedprice,
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

    def get_fixed_prices(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[FixedPrice]]:
        """
        The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated. This method retrieves an array of Fixed Prices for an SKU in a Trade Policy with Minimum Quantities.

         The default value for a Minimum Quantity is `1`. This means a Fixed Price will be valid for a SKU in a Trade Policy for orders containing the specified number of Minimum Quantity or above, unless a higher Minimum Quantity is specified.

         Fixed prices may, optionally, be scheduled. If so, these objects will contain the `dateRange` object with `from` and `to` properties, indicating the start and end time of the scheduled fixed price in the RFC3339 timestamp format (`YYYY-MM-DDT23:59:60Z`).

         Note that the 'Z', at the end, represents the UTC time (GMT+00:00). If it was in GMT-03:00, for example, it would be (`YYYY-MM-DDT23:59:60-03:00`).

         ## Response body example

        ```json
        [
            {
                "tradePolicyId": "6",
                "value": 20.9,
                "listPrice": 22.9,
                "minQuantity": 1,
                "dateRange": {
                    "from": "2021-12-30T22:00:00-03:00",
                    "to": "2021-12-30T22:00:00-03:00"
                }
            },
            {
                "tradePolicyId": "1",
                "value": 18.9,
                "listPrice": null,
                "minQuantity": 1,
                "dateRange": {
                    "from": "2021-12-30T22:00:00-03:00",
                    "to": "2021-12-30T22:00:00-03:00"
                }
            }
        ]
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FixedPrice]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/fixed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FixedPrice],
                    parse_obj_as(
                        type_=typing.List[FixedPrice],
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

    def get_fixed_pricesonapricetable(
        self, item_id: int, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[FixedPrice]]:
        """
        Retrieves all Fixed Prices on a price table or trade policy.

        ## Response body example

        ```json
        [
            {
                "tradePolicyId": "6",
                "value": 20.9,
                "listPrice": 22.9,
                "minQuantity": 1,
                "dateRange": {
                    "from": "2021-12-30T22:00:00-03:00",
                    "to": "2021-12-30T22:00:00-04:00"
                }
            },
            {
                "tradePolicyId": "1",
                "value": 18.9,
                "listPrice": null,
                "minQuantity": 1
            }
        ]
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            Price Table Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FixedPrice]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/fixed/{encode_path_param(price_table_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FixedPrice],
                    parse_obj_as(
                        type_=typing.List[FixedPrice],
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

    def createorupdatefixedpricesonpricetableortradepolicy(
        self,
        item_id: int,
        price_table_id: str,
        *,
        request: typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Creates or updates the fixed prices of an SKU for a specific price table or trade policy. You can add one or multiple fixed prices per SKU.

         ## Request body example

        ```json
        [
          {
            "value": 50.5,
            "listPrice": 50.5,
            "minQuantity": 2,
            "dateRange": {
              "from": "2021-12-30T22:00:00-03:00",
              "to": "2021-12-30T22:00:00-04:00"
            }
          }
        ]
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            SKU **price table** name or **trade policy** ID.

        request : typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/fixed/{encode_path_param(price_table_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deletefixedpricesonapricetableortradepolicy(
        self, item_id: int, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes all Fixed Prices of an SKU in a specific Price Table or Trade Policy.

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            Price Table or Trade Policy Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/fixed/{encode_path_param(price_table_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPricesAndFixedPricesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_price(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Getprice]:
        """
        Retrieves price data given a specific SKU ID. Within the `fixedPrices` object, there might be a list of prices for specific Trade Policies and Minimium Quantities of the SKU. Fixed Prices may also be scheduled.

         ## Response body example

        ```json
        {
            "itemId": "1",
            "listPrice": 50,
            "costPrice": 90,
            "markup": 30,
            "basePrice": 117,
            "fixedPrices": [
                {
                    "tradePolicyId": "1",
                    "value": 50.5,
                    "listPrice": 50.5,
                    "minQuantity": 2,
                    "dateRange": {
                        "from": "2021-12-31T01:00:00Z",
                        "to": "2022-12-31T01:00:00Z"
                    }
                },
                {
                    "tradePolicyId": "2",
                    "value": 30,
                    "listPrice": 50,
                    "minQuantity": 2
                }
            ]
        }
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Getprice]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Getprice,
                    parse_obj_as(
                        type_=Getprice,
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

    async def create_update_price_or_fixed_price(
        self,
        item_id: int,
        *,
        base_price: float,
        list_price: float,
        markup: int,
        cost_price: typing.Optional[float] = OMIT,
        fixed_prices: typing.Optional[typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Creates or updates an SKU Base Price or Fixed Prices. The **base price** is the basic selling price of a product, it comprises the cost price and the markup wanted in the sale of the product. The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated.

         <p> You may optionally set a list price. Additionally, you may set either a cost price or a markup value. By defining either one of them, the other will be calculated to conform to the formula <code>costPrice * (1 + markup) = basePrice</code>.</p> <h2>Request body example</h2>

        ```json
        {
            "markup": 30,
            "basePrice": 100,
            "listPrice": 35,
            "fixedPrices": [
                {
                    "tradePolicyId": "1",
                    "value": 31,
                    "listPrice": 32,
                    "minQuantity": 1,
                    "dateRange": {
                        "from": "2022-05-21T22:00:00Z",
                        "to": "2023-05-28T22:00:00Z"
                    }
                },
                {
                    "tradePolicyId": "1",
                    "value": 31.5,
                    "listPrice": 33,
                    "minQuantity": 2
                }
            ]
        }
        ```

        Parameters
        ----------
        item_id : int
            SKU unique identifier number.

        base_price : float
            SKU selling base price. If you decide to fill only the `basePrice` item, the `markup` and `costPrice` will be automatically generated to adapt to the number inserted in `basePrice`.

        list_price : float
            SKU's suggested selling price.

        markup : int
            The profit percentage that is to be obtained from the sale of that SKU. If you decide to fill the `markup` item, you must also fill the `costPrice`. The `basePrice` will be automatically generated based on both values.

        cost_price : typing.Optional[float]
            SKU selling cost price. If you decide to fill the `costPrice` item, you must also fill the `markup` and `basePrice` will be automatically generated based on both values.

        fixed_prices : typing.Optional[typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "basePrice": base_price,
                "costPrice": cost_price,
                "fixedPrices": convert_and_respect_annotation_metadata(
                    object_=fixed_prices,
                    annotation=typing.Sequence[CreateUpdatePriceOrFixedPriceRequestFixedPricesItem],
                    direction="write",
                ),
                "listPrice": list_price,
                "markup": markup,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_price(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes the Base Price and all available Fixed Prices for an SKU in all trade policies.

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_computed_pricebypricetable(
        self,
        item_id: int,
        price_table_id: str,
        *,
        category_ids: int,
        brand_id: int,
        quantity: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Getcomputedprice]:
        """
        Gets the Computed Price, which is the price after all the steps in the Pricing pipeline, for an SKU in a specific price table or trade policy.

        ## Response body example

        ```json
        {
            "tradePolicyId": "1",
            "listPrice": 30,
            "costPrice": 76.92,
            "sellingPrice": 18.9,
            "priceValidUntil": "2018-12-20T18:12:14Z"
        }
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            SKU Price Table Name.

        category_ids : int
            Category ID.

        brand_id : int
            Brand ID.

        quantity : int
            SKU quantity.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Getcomputedprice]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/computed/{encode_path_param(price_table_id)}",
            method="GET",
            params={
                "categoryIds": category_ids,
                "brandId": brand_id,
                "quantity": quantity,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Getcomputedprice,
                    parse_obj_as(
                        type_=Getcomputedprice,
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

    async def get_fixed_prices(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[FixedPrice]]:
        """
        The **fixed price** is an optional price of the SKU for a specific trade policy with a specific minimum quantity to be activated. This method retrieves an array of Fixed Prices for an SKU in a Trade Policy with Minimum Quantities.

         The default value for a Minimum Quantity is `1`. This means a Fixed Price will be valid for a SKU in a Trade Policy for orders containing the specified number of Minimum Quantity or above, unless a higher Minimum Quantity is specified.

         Fixed prices may, optionally, be scheduled. If so, these objects will contain the `dateRange` object with `from` and `to` properties, indicating the start and end time of the scheduled fixed price in the RFC3339 timestamp format (`YYYY-MM-DDT23:59:60Z`).

         Note that the 'Z', at the end, represents the UTC time (GMT+00:00). If it was in GMT-03:00, for example, it would be (`YYYY-MM-DDT23:59:60-03:00`).

         ## Response body example

        ```json
        [
            {
                "tradePolicyId": "6",
                "value": 20.9,
                "listPrice": 22.9,
                "minQuantity": 1,
                "dateRange": {
                    "from": "2021-12-30T22:00:00-03:00",
                    "to": "2021-12-30T22:00:00-03:00"
                }
            },
            {
                "tradePolicyId": "1",
                "value": 18.9,
                "listPrice": null,
                "minQuantity": 1,
                "dateRange": {
                    "from": "2021-12-30T22:00:00-03:00",
                    "to": "2021-12-30T22:00:00-03:00"
                }
            }
        ]
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FixedPrice]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/fixed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FixedPrice],
                    parse_obj_as(
                        type_=typing.List[FixedPrice],
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

    async def get_fixed_pricesonapricetable(
        self, item_id: int, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[FixedPrice]]:
        """
        Retrieves all Fixed Prices on a price table or trade policy.

        ## Response body example

        ```json
        [
            {
                "tradePolicyId": "6",
                "value": 20.9,
                "listPrice": 22.9,
                "minQuantity": 1,
                "dateRange": {
                    "from": "2021-12-30T22:00:00-03:00",
                    "to": "2021-12-30T22:00:00-04:00"
                }
            },
            {
                "tradePolicyId": "1",
                "value": 18.9,
                "listPrice": null,
                "minQuantity": 1
            }
        ]
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            Price Table Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FixedPrice]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/fixed/{encode_path_param(price_table_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FixedPrice],
                    parse_obj_as(
                        type_=typing.List[FixedPrice],
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

    async def createorupdatefixedpricesonpricetableortradepolicy(
        self,
        item_id: int,
        price_table_id: str,
        *,
        request: typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Creates or updates the fixed prices of an SKU for a specific price table or trade policy. You can add one or multiple fixed prices per SKU.

         ## Request body example

        ```json
        [
          {
            "value": 50.5,
            "listPrice": 50.5,
            "minQuantity": 2,
            "dateRange": {
              "from": "2021-12-30T22:00:00-03:00",
              "to": "2021-12-30T22:00:00-04:00"
            }
          }
        ]
        ```

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            SKU **price table** name or **trade policy** ID.

        request : typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/fixed/{encode_path_param(price_table_id)}",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=typing.Sequence[CreateorupdatefixedpricesonpricetableortradepolicyRequestBodyItem],
                direction="write",
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deletefixedpricesonapricetableortradepolicy(
        self, item_id: int, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes all Fixed Prices of an SKU in a specific Price Table or Trade Policy.

        Parameters
        ----------
        item_id : int
            SKU ID.

        price_table_id : str
            Price Table or Trade Policy Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/prices/{encode_path_param(item_id)}/fixed/{encode_path_param(price_table_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
