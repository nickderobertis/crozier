

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from .types.getallpricetablesandrules_response_item import GetallpricetablesandrulesResponseItem
from .types.getrulesforapricetable_response import GetrulesforapricetableResponse
from .types.put_pricing_pipeline_catalog_price_table_id_request_rules_item import (
    PutPricingPipelineCatalogPriceTableIdRequestRulesItem,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPriceTablesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getallpricetablesandrules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GetallpricetablesandrulesResponseItem]]:
        """
        This method will retrieve all price tables and their rules.

        ## Response body example

        ```json
        [
            {
                "tradePolicyId": "2",
                "rules": [
                    {
                        "id": 0,
                        "context": {
                            "categories": {},
                            "brands": {},
                            "stockStatuses": null,
                            "internalCategories": null,
                            "markupRange": null,
                            "dateRange": null
                        },
                        "percentualModifier": 20
                    }
                ]
            },
            {
                "tradePolicyId": "b2c",
                "rules": [
                    {
                        "id": 0,
                        "context": {
                            "categories": {},
                            "brands": {
                                "2000009": "Whiskas"
                            },
                            "stockStatuses": null,
                            "internalCategories": null,
                            "markupRange": null,
                            "dateRange": null
                        },
                        "percentualModifier": 15
                    }
                ]
            }
        ]
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetallpricetablesandrulesResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "pricing/pipeline/catalog",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetallpricetablesandrulesResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetallpricetablesandrulesResponseItem],
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

    def getrulesforapricetable(
        self, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetrulesforapricetableResponse]:
        """
        This method will retrieve the rules from a specific Price Table.

        ## Response body example

        ```json
        {
            "tradePolicyId": "b2c",
            "rules": [{
                "id": 0,
                "context": {
                    "categories": {},
                    "brands": {
                        "2000009": "Whiskas"
                    },
                    "stockStatuses": null,
                    "internalCategories": null,
                    "markupRange": null,
                    "dateRange": null
                },
                "percentualModifier": 15
            }]
        }
        ```

        Parameters
        ----------
        price_table_id : str
            Price Table Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetrulesforapricetableResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/pipeline/catalog/{encode_path_param(price_table_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetrulesforapricetableResponse,
                    parse_obj_as(
                        type_=GetrulesforapricetableResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_rules_for_a_price_table(
        self,
        price_table_id: str,
        *,
        rules: typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        This method will update the rules from a specific Price Table. It will delete all the rules from the requested Price Table and create new rules based on the content of the request.

        ## Request body example

        ```json
        {
            "rules": [
                  {
                       "id": 1,
                       "context": {
                            "categories": {
                                 "Category ID": "1",
                                 "Category Name": "Alimentação"
                            },
                            "brands": {
                                 "Brand ID": "2000002",
                                 "Brand Name": "Whiskas"
                            },
                            "markupRange": {
                                 "from": 0,
                                 "to": 200
                            },
                            "dateRange": {
                                 "from": "2022-01-23T19:00:00.000Z",
                                 "to": "2023-10-26T00:00:00.000Z"
                            }
                       },
                       "percentualModifier": 0
                  }
            ]
        }
        ```

        Parameters
        ----------
        price_table_id : str
            Price Table Name.

        rules : typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem]
            Array of rules for the price table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"pricing/pipeline/catalog/{encode_path_param(price_table_id)}",
            method="PUT",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules,
                    annotation=typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem],
                    direction="write",
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
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def listpricetables(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        This method will list all price tables.

        ## Response body example

        ```json
        [
            "1",
            "2",
            "3",
            "b2c",
            "b2b",
            "gold"
        ]
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "pricing/tables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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


class AsyncRawPriceTablesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getallpricetablesandrules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GetallpricetablesandrulesResponseItem]]:
        """
        This method will retrieve all price tables and their rules.

        ## Response body example

        ```json
        [
            {
                "tradePolicyId": "2",
                "rules": [
                    {
                        "id": 0,
                        "context": {
                            "categories": {},
                            "brands": {},
                            "stockStatuses": null,
                            "internalCategories": null,
                            "markupRange": null,
                            "dateRange": null
                        },
                        "percentualModifier": 20
                    }
                ]
            },
            {
                "tradePolicyId": "b2c",
                "rules": [
                    {
                        "id": 0,
                        "context": {
                            "categories": {},
                            "brands": {
                                "2000009": "Whiskas"
                            },
                            "stockStatuses": null,
                            "internalCategories": null,
                            "markupRange": null,
                            "dateRange": null
                        },
                        "percentualModifier": 15
                    }
                ]
            }
        ]
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetallpricetablesandrulesResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pricing/pipeline/catalog",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetallpricetablesandrulesResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetallpricetablesandrulesResponseItem],
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

    async def getrulesforapricetable(
        self, price_table_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetrulesforapricetableResponse]:
        """
        This method will retrieve the rules from a specific Price Table.

        ## Response body example

        ```json
        {
            "tradePolicyId": "b2c",
            "rules": [{
                "id": 0,
                "context": {
                    "categories": {},
                    "brands": {
                        "2000009": "Whiskas"
                    },
                    "stockStatuses": null,
                    "internalCategories": null,
                    "markupRange": null,
                    "dateRange": null
                },
                "percentualModifier": 15
            }]
        }
        ```

        Parameters
        ----------
        price_table_id : str
            Price Table Name.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetrulesforapricetableResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/pipeline/catalog/{encode_path_param(price_table_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetrulesforapricetableResponse,
                    parse_obj_as(
                        type_=GetrulesforapricetableResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_rules_for_a_price_table(
        self,
        price_table_id: str,
        *,
        rules: typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        This method will update the rules from a specific Price Table. It will delete all the rules from the requested Price Table and create new rules based on the content of the request.

        ## Request body example

        ```json
        {
            "rules": [
                  {
                       "id": 1,
                       "context": {
                            "categories": {
                                 "Category ID": "1",
                                 "Category Name": "Alimentação"
                            },
                            "brands": {
                                 "Brand ID": "2000002",
                                 "Brand Name": "Whiskas"
                            },
                            "markupRange": {
                                 "from": 0,
                                 "to": 200
                            },
                            "dateRange": {
                                 "from": "2022-01-23T19:00:00.000Z",
                                 "to": "2023-10-26T00:00:00.000Z"
                            }
                       },
                       "percentualModifier": 0
                  }
            ]
        }
        ```

        Parameters
        ----------
        price_table_id : str
            Price Table Name.

        rules : typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem]
            Array of rules for the price table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"pricing/pipeline/catalog/{encode_path_param(price_table_id)}",
            method="PUT",
            json={
                "rules": convert_and_respect_annotation_metadata(
                    object_=rules,
                    annotation=typing.Sequence[PutPricingPipelineCatalogPriceTableIdRequestRulesItem],
                    direction="write",
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
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def listpricetables(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        This method will list all price tables.

        ## Response body example

        ```json
        [
            "1",
            "2",
            "3",
            "b2c",
            "b2b",
            "gold"
        ]
        ```

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "pricing/tables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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
