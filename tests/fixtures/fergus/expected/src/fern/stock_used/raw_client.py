

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.stock_used_list_response import StockUsedListResponse
from pydantic import ValidationError


class RawStockUsedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_stock_used(
        self,
        *,
        filter_date_from: typing.Optional[dt.date] = None,
        page_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StockUsedListResponse]:
        """

          Returns historical stock used across all jobs, optionally filtered by filterDateFrom.

          Stock used is defined as material line items that:
          - Have been invoiced to the customer (sent or paid).
          - And are assigned as materials sales account.
          - And are not from purchase orders.
          - And are not invoiced from suppliers.


        Parameters
        ----------
        filter_date_from : typing.Optional[dt.date]
            Filter stock used on or after this date (yyyy-mm-dd) default is 90 days ago and max up to 180 days ago

        page_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StockUsedListResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "stockUsed",
            method="GET",
            params={
                "filterDateFrom": str(filter_date_from) if filter_date_from is not None else None,
                "pageCursor": page_cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StockUsedListResponse,
                    parse_obj_as(
                        type_=StockUsedListResponse,
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


class AsyncRawStockUsedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_stock_used(
        self,
        *,
        filter_date_from: typing.Optional[dt.date] = None,
        page_cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StockUsedListResponse]:
        """

          Returns historical stock used across all jobs, optionally filtered by filterDateFrom.

          Stock used is defined as material line items that:
          - Have been invoiced to the customer (sent or paid).
          - And are assigned as materials sales account.
          - And are not from purchase orders.
          - And are not invoiced from suppliers.


        Parameters
        ----------
        filter_date_from : typing.Optional[dt.date]
            Filter stock used on or after this date (yyyy-mm-dd) default is 90 days ago and max up to 180 days ago

        page_cursor : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StockUsedListResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "stockUsed",
            method="GET",
            params={
                "filterDateFrom": str(filter_date_from) if filter_date_from is not None else None,
                "pageCursor": page_cursor,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StockUsedListResponse,
                    parse_obj_as(
                        type_=StockUsedListResponse,
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
