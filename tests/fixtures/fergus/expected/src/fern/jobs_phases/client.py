

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stock_on_hand_list_response import StockOnHandListResponse
from ..types.stock_on_hand_response import StockOnHandResponse
from .raw_client import AsyncRawJobsPhasesClient, RawJobsPhasesClient
from .types.get_phases_job_phase_id_stock_on_hand_request_sort_field import (
    GetPhasesJobPhaseIdStockOnHandRequestSortField,
)
from .types.get_phases_job_phase_id_stock_on_hand_request_sort_order import (
    GetPhasesJobPhaseIdStockOnHandRequestSortOrder,
)
from .types.get_phases_stock_on_hand_request_sort_field import GetPhasesStockOnHandRequestSortField
from .types.get_phases_stock_on_hand_request_sort_order import GetPhasesStockOnHandRequestSortOrder
from .types.post_phases_job_phase_id_stock_on_hand_request_body import PostPhasesJobPhaseIdStockOnHandRequestBody


OMIT = typing.cast(typing.Any, ...)


class JobsPhasesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobsPhasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobsPhasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobsPhasesClient
        """
        return self._raw_client

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
    ) -> StockOnHandListResponse:
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
        StockOnHandListResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_phases.get_phases_job_phase_id_stock_on_hand(
            job_phase_id=1.1,
        )
        """
        _response = self._raw_client.get_phases_job_phase_id_stock_on_hand(
            job_phase_id,
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            last_modified=last_modified,
            date_entered=date_entered,
            request_options=request_options,
        )
        return _response.data

    def post_phases_job_phase_id_stock_on_hand(
        self,
        job_phase_id: float,
        *,
        request: PostPhasesJobPhaseIdStockOnHandRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StockOnHandResponse:
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
        StockOnHandResponse
            Successful Response

        Examples
        --------
        from fern.jobs_phases import (
            PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_phases.post_phases_job_phase_id_stock_on_hand(
            job_phase_id=1.1,
            request=PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId(
                item_quantity=1.1,
                price_book_line_item_id=1.1,
            ),
        )
        """
        _response = self._raw_client.post_phases_job_phase_id_stock_on_hand(
            job_phase_id, request=request, request_options=request_options
        )
        return _response.data

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
    ) -> StockOnHandListResponse:
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
        StockOnHandListResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_phases.get_phases_stock_on_hand()
        """
        _response = self._raw_client.get_phases_stock_on_hand(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            last_modified=last_modified,
            date_entered=date_entered,
            request_options=request_options,
        )
        return _response.data

    def delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
        self, job_phase_id: float, stock_on_hand_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_phases.delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
            job_phase_id=1.1,
            stock_on_hand_id=1.1,
        )
        """
        _response = self._raw_client.delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
            job_phase_id, stock_on_hand_id, request_options=request_options
        )
        return _response.data

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
    ) -> StockOnHandResponse:
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
        StockOnHandResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.jobs_phases.patch_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
            job_phase_id=1.1,
            stock_on_hand_id=1.1,
        )
        """
        _response = self._raw_client.patch_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
            job_phase_id,
            stock_on_hand_id,
            item_description=item_description,
            item_price=item_price,
            item_cost=item_cost,
            item_quantity=item_quantity,
            sales_account_id=sales_account_id,
            is_labour=is_labour,
            request_options=request_options,
        )
        return _response.data


class AsyncJobsPhasesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobsPhasesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobsPhasesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobsPhasesClient
        """
        return self._raw_client

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
    ) -> StockOnHandListResponse:
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
        StockOnHandListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_phases.get_phases_job_phase_id_stock_on_hand(
                job_phase_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_phases_job_phase_id_stock_on_hand(
            job_phase_id,
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            last_modified=last_modified,
            date_entered=date_entered,
            request_options=request_options,
        )
        return _response.data

    async def post_phases_job_phase_id_stock_on_hand(
        self,
        job_phase_id: float,
        *,
        request: PostPhasesJobPhaseIdStockOnHandRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> StockOnHandResponse:
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
        StockOnHandResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.jobs_phases import (
            PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_phases.post_phases_job_phase_id_stock_on_hand(
                job_phase_id=1.1,
                request=PostPhasesJobPhaseIdStockOnHandRequestBodyPriceBookLineItemId(
                    item_quantity=1.1,
                    price_book_line_item_id=1.1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_phases_job_phase_id_stock_on_hand(
            job_phase_id, request=request, request_options=request_options
        )
        return _response.data

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
    ) -> StockOnHandListResponse:
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
        StockOnHandListResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_phases.get_phases_stock_on_hand()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_phases_stock_on_hand(
            page_size=page_size,
            sort_order=sort_order,
            page_cursor=page_cursor,
            sort_field=sort_field,
            filter_search_text=filter_search_text,
            last_modified=last_modified,
            date_entered=date_entered,
            request_options=request_options,
        )
        return _response.data

    async def delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
        self, job_phase_id: float, stock_on_hand_id: float, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_phases.delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
                job_phase_id=1.1,
                stock_on_hand_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
            job_phase_id, stock_on_hand_id, request_options=request_options
        )
        return _response.data

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
    ) -> StockOnHandResponse:
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
        StockOnHandResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.jobs_phases.patch_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
                job_phase_id=1.1,
                stock_on_hand_id=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_phases_job_phase_id_stock_on_hand_stock_on_hand_id(
            job_phase_id,
            stock_on_hand_id,
            item_description=item_description,
            item_price=item_price,
            item_cost=item_cost,
            item_quantity=item_quantity,
            sales_account_id=sales_account_id,
            is_labour=is_labour,
            request_options=request_options,
        )
        return _response.data
