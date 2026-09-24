

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.datetime_utils import serialize_datetime
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.stock_on_hand_list_response import StockOnHandListResponse
from ..types.stock_on_hand_response import StockOnHandResponse
from .types.get_phases_job_phase_id_stock_on_hand_request_sort_field import (
    GetPhasesJobPhaseIdStockOnHandRequestSortField,
)
from .types.get_phases_job_phase_id_stock_on_hand_request_sort_order import (
    GetPhasesJobPhaseIdStockOnHandRequestSortOrder,
)
from .types.get_phases_stock_on_hand_request_sort_field import GetPhasesStockOnHandRequestSortField
from .types.get_phases_stock_on_hand_request_sort_order import GetPhasesStockOnHandRequestSortOrder
from .types.post_phases_job_phase_id_stock_on_hand_request_body import PostPhasesJobPhaseIdStockOnHandRequestBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawJobsPhasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_phases_job_phase_id_stock_on_hand(
        self,
        job_phase_id: float,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        last_modified: typing.Optional[dt.datetime] = None,
        date_entered: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StockOnHandListResponse]:
        """
        Job Phase stock on hand

        Parameters
        ----------
        job_phase_id : float

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `itemDescription`

        last_modified : typing.Optional[dt.datetime]

        date_entered : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StockOnHandListResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phases/{encode_path_param(job_phase_id)}/stockOnHand",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
                "lastModified": serialize_datetime(last_modified) if last_modified is not None else None,
                "dateEntered": serialize_datetime(date_entered) if date_entered is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StockOnHandListResponse,
                    parse_obj_as(
                        type_=StockOnHandListResponse,
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

    def post_phases_job_phase_id_stock_on_hand(
        self,
        job_phase_id: float,
        *,
        request: PostPhasesJobPhaseIdStockOnHandRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StockOnHandResponse]:
        """
        Add stock on hand to job phase. Two scenarios are supported:

        **With `priceBookLineItemId`:** Only `itemQuantity` is required. `itemDescription`, `itemPrice`, and `itemCost` will be populated from the price book item. No other fields may be passed.

        **Without `priceBookLineItemId`:** `itemDescription`, `itemPrice`, `itemCost`, and `itemQuantity` are all required.

        Parameters
        ----------
        job_phase_id : float

        request : PostPhasesJobPhaseIdStockOnHandRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StockOnHandResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phases/{encode_path_param(job_phase_id)}/stockOnHand",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPhasesJobPhaseIdStockOnHandRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StockOnHandResponse,
                    parse_obj_as(
                        type_=StockOnHandResponse,
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

    def get_phases_stock_on_hand(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPhasesStockOnHandRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPhasesStockOnHandRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        last_modified: typing.Optional[dt.datetime] = None,
        date_entered: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StockOnHandListResponse]:
        """
        Stock on hand across all Job Phases

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPhasesStockOnHandRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPhasesStockOnHandRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `itemDescription`

        last_modified : typing.Optional[dt.datetime]

        date_entered : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StockOnHandListResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "phases/stockOnHand",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
                "lastModified": serialize_datetime(last_modified) if last_modified is not None else None,
                "dateEntered": serialize_datetime(date_entered) if date_entered is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StockOnHandListResponse,
                    parse_obj_as(
                        type_=StockOnHandListResponse,
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

    def delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
        self, job_phase_id: float, stock_on_hand_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete stock on hand on job phase

        Parameters
        ----------
        job_phase_id : float

        stock_on_hand_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phases/{encode_path_param(job_phase_id)}/stockOnHand/{encode_path_param(stock_on_hand_id)}",
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

    def patch_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
        self,
        job_phase_id: float,
        stock_on_hand_id: float,
        *,
        item_description: typing.Optional[str] = OMIT,
        item_price: typing.Optional[float] = OMIT,
        item_cost: typing.Optional[float] = OMIT,
        item_quantity: typing.Optional[float] = OMIT,
        sales_account_id: typing.Optional[float] = OMIT,
        is_labour: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[StockOnHandResponse]:
        """
        Update stock on hand on job phase

        Parameters
        ----------
        job_phase_id : float

        stock_on_hand_id : float

        item_description : typing.Optional[str]

        item_price : typing.Optional[float]

        item_cost : typing.Optional[float]

        item_quantity : typing.Optional[float]

        sales_account_id : typing.Optional[float]

        is_labour : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StockOnHandResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"phases/{encode_path_param(job_phase_id)}/stockOnHand/{encode_path_param(stock_on_hand_id)}",
            method="PATCH",
            json={
                "itemDescription": item_description,
                "itemPrice": item_price,
                "itemCost": item_cost,
                "itemQuantity": item_quantity,
                "salesAccountId": sales_account_id,
                "isLabour": is_labour,
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
                    StockOnHandResponse,
                    parse_obj_as(
                        type_=StockOnHandResponse,
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


class AsyncRawJobsPhasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_phases_job_phase_id_stock_on_hand(
        self,
        job_phase_id: float,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        last_modified: typing.Optional[dt.datetime] = None,
        date_entered: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StockOnHandListResponse]:
        """
        Job Phase stock on hand

        Parameters
        ----------
        job_phase_id : float

        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPhasesJobPhaseIdStockOnHandRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `itemDescription`

        last_modified : typing.Optional[dt.datetime]

        date_entered : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StockOnHandListResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phases/{encode_path_param(job_phase_id)}/stockOnHand",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
                "lastModified": serialize_datetime(last_modified) if last_modified is not None else None,
                "dateEntered": serialize_datetime(date_entered) if date_entered is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StockOnHandListResponse,
                    parse_obj_as(
                        type_=StockOnHandListResponse,
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

    async def post_phases_job_phase_id_stock_on_hand(
        self,
        job_phase_id: float,
        *,
        request: PostPhasesJobPhaseIdStockOnHandRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StockOnHandResponse]:
        """
        Add stock on hand to job phase. Two scenarios are supported:

        **With `priceBookLineItemId`:** Only `itemQuantity` is required. `itemDescription`, `itemPrice`, and `itemCost` will be populated from the price book item. No other fields may be passed.

        **Without `priceBookLineItemId`:** `itemDescription`, `itemPrice`, `itemCost`, and `itemQuantity` are all required.

        Parameters
        ----------
        job_phase_id : float

        request : PostPhasesJobPhaseIdStockOnHandRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StockOnHandResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phases/{encode_path_param(job_phase_id)}/stockOnHand",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPhasesJobPhaseIdStockOnHandRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StockOnHandResponse,
                    parse_obj_as(
                        type_=StockOnHandResponse,
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

    async def get_phases_stock_on_hand(
        self,
        *,
        page_size: typing.Optional[float] = None,
        sort_order: typing.Optional[GetPhasesStockOnHandRequestSortOrder] = None,
        page_cursor: typing.Optional[str] = None,
        sort_field: typing.Optional[GetPhasesStockOnHandRequestSortField] = None,
        filter_search_text: typing.Optional[str] = None,
        last_modified: typing.Optional[dt.datetime] = None,
        date_entered: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StockOnHandListResponse]:
        """
        Stock on hand across all Job Phases

        Parameters
        ----------
        page_size : typing.Optional[float]

        sort_order : typing.Optional[GetPhasesStockOnHandRequestSortOrder]

        page_cursor : typing.Optional[str]

        sort_field : typing.Optional[GetPhasesStockOnHandRequestSortField]

        filter_search_text : typing.Optional[str]
            Searchable fields:
            - `itemDescription`

        last_modified : typing.Optional[dt.datetime]

        date_entered : typing.Optional[dt.datetime]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StockOnHandListResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "phases/stockOnHand",
            method="GET",
            params={
                "pageSize": page_size,
                "sortOrder": sort_order,
                "pageCursor": page_cursor,
                "sortField": sort_field,
                "filterSearchText": filter_search_text,
                "lastModified": serialize_datetime(last_modified) if last_modified is not None else None,
                "dateEntered": serialize_datetime(date_entered) if date_entered is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StockOnHandListResponse,
                    parse_obj_as(
                        type_=StockOnHandListResponse,
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

    async def delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
        self, job_phase_id: float, stock_on_hand_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete stock on hand on job phase

        Parameters
        ----------
        job_phase_id : float

        stock_on_hand_id : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phases/{encode_path_param(job_phase_id)}/stockOnHand/{encode_path_param(stock_on_hand_id)}",
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

    async def patch_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
        self,
        job_phase_id: float,
        stock_on_hand_id: float,
        *,
        item_description: typing.Optional[str] = OMIT,
        item_price: typing.Optional[float] = OMIT,
        item_cost: typing.Optional[float] = OMIT,
        item_quantity: typing.Optional[float] = OMIT,
        sales_account_id: typing.Optional[float] = OMIT,
        is_labour: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[StockOnHandResponse]:
        """
        Update stock on hand on job phase

        Parameters
        ----------
        job_phase_id : float

        stock_on_hand_id : float

        item_description : typing.Optional[str]

        item_price : typing.Optional[float]

        item_cost : typing.Optional[float]

        item_quantity : typing.Optional[float]

        sales_account_id : typing.Optional[float]

        is_labour : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StockOnHandResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"phases/{encode_path_param(job_phase_id)}/stockOnHand/{encode_path_param(stock_on_hand_id)}",
            method="PATCH",
            json={
                "itemDescription": item_description,
                "itemPrice": item_price,
                "itemCost": item_cost,
                "itemQuantity": item_quantity,
                "salesAccountId": sales_account_id,
                "isLabour": is_labour,
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
                    StockOnHandResponse,
                    parse_obj_as(
                        type_=StockOnHandResponse,
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
