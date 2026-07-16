

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawHandpickedClient, RawHandpickedClient


class HandpickedClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHandpickedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHandpickedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHandpickedClient
        """
        return self._raw_client

    def get_results_from_a_handpicked_collection(
        self,
        slug: str,
        *,
        query: typing.Optional[str] = None,
        auction_price_max: typing.Optional[float] = None,
        category: typing.Optional[str] = None,
        product_type: typing.Optional[str] = None,
        conditions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        decade: typing.Optional[str] = None,
        finish: typing.Optional[str] = None,
        handmade: typing.Optional[bool] = None,
        item_city: typing.Optional[str] = None,
        item_country: typing.Optional[str] = None,
        item_region: typing.Optional[str] = None,
        item_state: typing.Optional[str] = None,
        make: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        model: typing.Optional[str] = None,
        must_not: typing.Optional[str] = None,
        price_max: typing.Optional[float] = None,
        price_min: typing.Optional[float] = None,
        currency: typing.Optional[str] = None,
        year_max: typing.Optional[int] = None,
        year_min: typing.Optional[int] = None,
        accepts_gift_cards: typing.Optional[bool] = None,
        preferred_seller: typing.Optional[bool] = None,
        shop: typing.Optional[str] = None,
        shop_id: typing.Optional[str] = None,
        listing_type: typing.Optional[str] = None,
        ships_to: typing.Optional[str] = None,
        exclude_auctions: typing.Optional[bool] = None,
        accepts_payment_plans: typing.Optional[bool] = None,
        watchers_count_min: typing.Optional[int] = None,
        not_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        local_pickup: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get results from a handpicked collection

        Parameters
        ----------
        slug : str

        query : typing.Optional[str]
            Search query.

        auction_price_max : typing.Optional[float]
            Maximum current auction price

        category : typing.Optional[str]
            Category slug from /api/categories

        product_type : typing.Optional[str]
            Product type slug from /api/categories

        conditions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint

        decade : typing.Optional[str]
            Decade: e.g. 1970s, early 70s

        finish : typing.Optional[str]
            Visual finish of the item, common for guitars

        handmade : typing.Optional[bool]
            Handmade items only

        item_city : typing.Optional[str]
            City where item is located

        item_country : typing.Optional[str]
            DEPRECATED - Country code where item is located

        item_region : typing.Optional[str]
            Country code where item is located

        item_state : typing.Optional[str]
            State or region code where item is located

        make : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Make(s)/brand of item (e.g. Fender). Can take a single value or an array.

        model : typing.Optional[str]
            Model of item (e.g. Stratocaster)

        must_not : typing.Optional[str]
            Search term negation. If you want to exclude a term, add it here

        price_max : typing.Optional[float]
            Maximum price of search results (USD)

        price_min : typing.Optional[float]
            Minimum price of search results (USD)

        currency : typing.Optional[str]
            The currency to be used for the price filters

        year_max : typing.Optional[int]
            Maximum year of manufacture

        year_min : typing.Optional[int]
            Minumum year of manufacture

        accepts_gift_cards : typing.Optional[bool]
            If true, include only items that accept gift cards

        preferred_seller : typing.Optional[bool]
            If true, include only items by Reverb Preferred Sellers

        shop : typing.Optional[str]
            Slug of shop to search

        shop_id : typing.Optional[str]
            ID of shop to search

        listing_type : typing.Optional[str]
            Type of listing: auctions,offers

        ships_to : typing.Optional[str]
            Limit search to items that ship to this country code

        exclude_auctions : typing.Optional[bool]
            If true, exclude auctions

        accepts_payment_plans : typing.Optional[bool]
            If true, only show items that can be purchased with a payment plan

        watchers_count_min : typing.Optional[int]
            Minimum number of watchers (used to find popular items)

        not_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Listing ID negation. If you want to exclude a listing, add it here.

        local_pickup : typing.Optional[bool]
            Only items that offer local pickup

        page : typing.Optional[int]

        per_page : typing.Optional[int]

        offset : typing.Optional[int]

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
        client.handpicked.get_results_from_a_handpicked_collection(
            slug="slug",
        )
        """
        _response = self._raw_client.get_results_from_a_handpicked_collection(
            slug,
            query=query,
            auction_price_max=auction_price_max,
            category=category,
            product_type=product_type,
            conditions=conditions,
            decade=decade,
            finish=finish,
            handmade=handmade,
            item_city=item_city,
            item_country=item_country,
            item_region=item_region,
            item_state=item_state,
            make=make,
            model=model,
            must_not=must_not,
            price_max=price_max,
            price_min=price_min,
            currency=currency,
            year_max=year_max,
            year_min=year_min,
            accepts_gift_cards=accepts_gift_cards,
            preferred_seller=preferred_seller,
            shop=shop,
            shop_id=shop_id,
            listing_type=listing_type,
            ships_to=ships_to,
            exclude_auctions=exclude_auctions,
            accepts_payment_plans=accepts_payment_plans,
            watchers_count_min=watchers_count_min,
            not_ids=not_ids,
            local_pickup=local_pickup,
            page=page,
            per_page=per_page,
            offset=offset,
            request_options=request_options,
        )
        return _response.data


class AsyncHandpickedClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHandpickedClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHandpickedClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHandpickedClient
        """
        return self._raw_client

    async def get_results_from_a_handpicked_collection(
        self,
        slug: str,
        *,
        query: typing.Optional[str] = None,
        auction_price_max: typing.Optional[float] = None,
        category: typing.Optional[str] = None,
        product_type: typing.Optional[str] = None,
        conditions: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        decade: typing.Optional[str] = None,
        finish: typing.Optional[str] = None,
        handmade: typing.Optional[bool] = None,
        item_city: typing.Optional[str] = None,
        item_country: typing.Optional[str] = None,
        item_region: typing.Optional[str] = None,
        item_state: typing.Optional[str] = None,
        make: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        model: typing.Optional[str] = None,
        must_not: typing.Optional[str] = None,
        price_max: typing.Optional[float] = None,
        price_min: typing.Optional[float] = None,
        currency: typing.Optional[str] = None,
        year_max: typing.Optional[int] = None,
        year_min: typing.Optional[int] = None,
        accepts_gift_cards: typing.Optional[bool] = None,
        preferred_seller: typing.Optional[bool] = None,
        shop: typing.Optional[str] = None,
        shop_id: typing.Optional[str] = None,
        listing_type: typing.Optional[str] = None,
        ships_to: typing.Optional[str] = None,
        exclude_auctions: typing.Optional[bool] = None,
        accepts_payment_plans: typing.Optional[bool] = None,
        watchers_count_min: typing.Optional[int] = None,
        not_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        local_pickup: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get results from a handpicked collection

        Parameters
        ----------
        slug : str

        query : typing.Optional[str]
            Search query.

        auction_price_max : typing.Optional[float]
            Maximum current auction price

        category : typing.Optional[str]
            Category slug from /api/categories

        product_type : typing.Optional[str]
            Product type slug from /api/categories

        conditions : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint

        decade : typing.Optional[str]
            Decade: e.g. 1970s, early 70s

        finish : typing.Optional[str]
            Visual finish of the item, common for guitars

        handmade : typing.Optional[bool]
            Handmade items only

        item_city : typing.Optional[str]
            City where item is located

        item_country : typing.Optional[str]
            DEPRECATED - Country code where item is located

        item_region : typing.Optional[str]
            Country code where item is located

        item_state : typing.Optional[str]
            State or region code where item is located

        make : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Make(s)/brand of item (e.g. Fender). Can take a single value or an array.

        model : typing.Optional[str]
            Model of item (e.g. Stratocaster)

        must_not : typing.Optional[str]
            Search term negation. If you want to exclude a term, add it here

        price_max : typing.Optional[float]
            Maximum price of search results (USD)

        price_min : typing.Optional[float]
            Minimum price of search results (USD)

        currency : typing.Optional[str]
            The currency to be used for the price filters

        year_max : typing.Optional[int]
            Maximum year of manufacture

        year_min : typing.Optional[int]
            Minumum year of manufacture

        accepts_gift_cards : typing.Optional[bool]
            If true, include only items that accept gift cards

        preferred_seller : typing.Optional[bool]
            If true, include only items by Reverb Preferred Sellers

        shop : typing.Optional[str]
            Slug of shop to search

        shop_id : typing.Optional[str]
            ID of shop to search

        listing_type : typing.Optional[str]
            Type of listing: auctions,offers

        ships_to : typing.Optional[str]
            Limit search to items that ship to this country code

        exclude_auctions : typing.Optional[bool]
            If true, exclude auctions

        accepts_payment_plans : typing.Optional[bool]
            If true, only show items that can be purchased with a payment plan

        watchers_count_min : typing.Optional[int]
            Minimum number of watchers (used to find popular items)

        not_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Listing ID negation. If you want to exclude a listing, add it here.

        local_pickup : typing.Optional[bool]
            Only items that offer local pickup

        page : typing.Optional[int]

        per_page : typing.Optional[int]

        offset : typing.Optional[int]

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
            await client.handpicked.get_results_from_a_handpicked_collection(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_results_from_a_handpicked_collection(
            slug,
            query=query,
            auction_price_max=auction_price_max,
            category=category,
            product_type=product_type,
            conditions=conditions,
            decade=decade,
            finish=finish,
            handmade=handmade,
            item_city=item_city,
            item_country=item_country,
            item_region=item_region,
            item_state=item_state,
            make=make,
            model=model,
            must_not=must_not,
            price_max=price_max,
            price_min=price_min,
            currency=currency,
            year_max=year_max,
            year_min=year_min,
            accepts_gift_cards=accepts_gift_cards,
            preferred_seller=preferred_seller,
            shop=shop,
            shop_id=shop_id,
            listing_type=listing_type,
            ships_to=ships_to,
            exclude_auctions=exclude_auctions,
            accepts_payment_plans=accepts_payment_plans,
            watchers_count_min=watchers_count_min,
            not_ids=not_ids,
            local_pickup=local_pickup,
            page=page,
            per_page=per_page,
            offset=offset,
            request_options=request_options,
        )
        return _response.data
