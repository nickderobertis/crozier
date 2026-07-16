

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawListingsClient, RawListingsClient
from .types.post_listings_request_categories_item import PostListingsRequestCategoriesItem
from .types.post_listings_request_condition import PostListingsRequestCondition
from .types.post_listings_request_exclusive_channel import PostListingsRequestExclusiveChannel
from .types.post_listings_request_location import PostListingsRequestLocation
from .types.post_listings_request_preorder_info import PostListingsRequestPreorderInfo
from .types.post_listings_request_price import PostListingsRequestPrice
from .types.post_listings_request_seller import PostListingsRequestSeller
from .types.post_listings_request_shipping import PostListingsRequestShipping
from .types.post_listings_request_videos_item import PostListingsRequestVideosItem
from .types.put_listings_slug_request_categories_item import PutListingsSlugRequestCategoriesItem
from .types.put_listings_slug_request_condition import PutListingsSlugRequestCondition
from .types.put_listings_slug_request_exclusive_channel import PutListingsSlugRequestExclusiveChannel
from .types.put_listings_slug_request_location import PutListingsSlugRequestLocation
from .types.put_listings_slug_request_preorder_info import PutListingsSlugRequestPreorderInfo
from .types.put_listings_slug_request_price import PutListingsSlugRequestPrice
from .types.put_listings_slug_request_seller import PutListingsSlugRequestSeller
from .types.put_listings_slug_request_shipping import PutListingsSlugRequestShipping
from .types.put_listings_slug_request_videos_item import PutListingsSlugRequestVideosItem


OMIT = typing.cast(typing.Any, ...)


class ListingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawListingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawListingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawListingsClient
        """
        return self._raw_client

    def default_search_of_listings_includes_only_used_handmade_add_a_filter_to_view_all_listings_or_use_the_listings_all_endpoint(
        self,
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
        Default search of listings includes only used & handmade. Add a filter to view all listings or use the /listings/all endpoint.

        Parameters
        ----------
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
        client.listings.default_search_of_listings_includes_only_used_handmade_add_a_filter_to_view_all_listings_or_use_the_listings_all_endpoint()
        """
        _response = self._raw_client.default_search_of_listings_includes_only_used_handmade_add_a_filter_to_view_all_listings_or_use_the_listings_all_endpoint(
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

    def create_a_listing(
        self,
        *,
        categories: typing.Optional[typing.Sequence[PostListingsRequestCategoriesItem]] = OMIT,
        condition: typing.Optional[PostListingsRequestCondition] = OMIT,
        description: typing.Optional[str] = OMIT,
        exclusive_channel: typing.Optional[PostListingsRequestExclusiveChannel] = OMIT,
        finish: typing.Optional[str] = OMIT,
        has_inventory: typing.Optional[bool] = OMIT,
        inventory: typing.Optional[int] = OMIT,
        location: typing.Optional[PostListingsRequestLocation] = OMIT,
        make: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        multi_item: typing.Optional[bool] = OMIT,
        offers_enabled: typing.Optional[bool] = OMIT,
        origin_country_code: typing.Optional[str] = OMIT,
        photos: typing.Optional[typing.Sequence[str]] = OMIT,
        preorder_info: typing.Optional[PostListingsRequestPreorderInfo] = OMIT,
        price: typing.Optional[PostListingsRequestPrice] = OMIT,
        prop65warning: typing.Optional[str] = OMIT,
        publish: typing.Optional[bool] = OMIT,
        seller: typing.Optional[PostListingsRequestSeller] = OMIT,
        seller_cost: typing.Optional[str] = OMIT,
        shipping: typing.Optional[PostListingsRequestShipping] = OMIT,
        shipping_profile_id: typing.Optional[str] = OMIT,
        shipping_profile_name: typing.Optional[str] = OMIT,
        sku: typing.Optional[str] = OMIT,
        sold_as_is: typing.Optional[bool] = OMIT,
        storage_location: typing.Optional[str] = OMIT,
        tax_exempt: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        upc: typing.Optional[str] = OMIT,
        upc_does_not_apply: typing.Optional[bool] = OMIT,
        videos: typing.Optional[typing.Sequence[PostListingsRequestVideosItem]] = OMIT,
        year: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create a listing

        Parameters
        ----------
        categories : typing.Optional[typing.Sequence[PostListingsRequestCategoriesItem]]

        condition : typing.Optional[PostListingsRequestCondition]
            Condition

        description : typing.Optional[str]
            Product description. Please keep formatting to a minimum.

        exclusive_channel : typing.Optional[PostListingsRequestExclusiveChannel]
            Currently for users of seller sites only, this allows you to have a listing available only to your seller site by setting this to 'seller_site'

        finish : typing.Optional[str]
            Finish, e.g. 'Sunburst'

        has_inventory : typing.Optional[bool]
            Set true if selling more than one

        inventory : typing.Optional[int]
            Number of items available for sale. Reverb will increment and decrement automatically.

        location : typing.Optional[PostListingsRequestLocation]

        make : typing.Optional[str]
            ex: Fender, Gibson

        model : typing.Optional[str]
            ex: Stratocaster, SG

        multi_item : typing.Optional[bool]
            Specifies if the listing is a bundle of multiple individual items

        offers_enabled : typing.Optional[bool]
            Whether the listing accepts negotiated offers (default: true)

        origin_country_code : typing.Optional[str]
            Country of origin/manufacture, ISO code (e.g: US)

        photos : typing.Optional[typing.Sequence[str]]
            An array of image URLs. Ex: ['http://my.site.com/image.jpg']

        preorder_info : typing.Optional[PostListingsRequestPreorderInfo]
            Create or update a preorder listing. Requires opt-in. Please contact sales@reverb.com if you would like to activate this feature.

        price : typing.Optional[PostListingsRequestPrice]

        prop65warning : typing.Optional[str]
            If your listing contains chemicals that are required to be reported under California Prop 65, please provide your warning statement. We will add the required 'Warning' label and link to California's information page, so you only need to provide the body of the warning. For more information, see https://www.p65warnings.ca.gov/new-proposition-65-warnings

        publish : typing.Optional[bool]
            Publish your listing if draft

        seller : typing.Optional[PostListingsRequestSeller]

        seller_cost : typing.Optional[str]
            Cost of goods in your currency as a POSIX-compliant decimal number (internal use only, not shown to buyers)

        shipping : typing.Optional[PostListingsRequestShipping]

        shipping_profile_id : typing.Optional[str]
            id of a shop's shipping profile

        shipping_profile_name : typing.Optional[str]
            DEPRECATED, please use shipping_profile_id. Name of a shipping profile

        sku : typing.Optional[str]
            Unique identifier for product

        sold_as_is : typing.Optional[bool]
            This item is sold As-Is and cannot be returned

        storage_location : typing.Optional[str]
            Internal note used by sellers to back reference their catalog system when entering a listing

        tax_exempt : typing.Optional[bool]
            Listing is exempt from taxes / VAT

        title : typing.Optional[str]
            Title of your listing

        upc : typing.Optional[str]
            Valid UPC code

        upc_does_not_apply : typing.Optional[bool]
            True if a brand new product has no UPC code, ie for a handmade or custom item

        videos : typing.Optional[typing.Sequence[PostListingsRequestVideosItem]]
            List of YouTube video urls. Note: ONLY ONE ALLOWED

        year : typing.Optional[str]
            Supports many formats. Ex: 1979, mid-70s, late 90s

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
        client.listings.create_a_listing()
        """
        _response = self._raw_client.create_a_listing(
            categories=categories,
            condition=condition,
            description=description,
            exclusive_channel=exclusive_channel,
            finish=finish,
            has_inventory=has_inventory,
            inventory=inventory,
            location=location,
            make=make,
            model=model,
            multi_item=multi_item,
            offers_enabled=offers_enabled,
            origin_country_code=origin_country_code,
            photos=photos,
            preorder_info=preorder_info,
            price=price,
            prop65warning=prop65warning,
            publish=publish,
            seller=seller,
            seller_cost=seller_cost,
            shipping=shipping,
            shipping_profile_id=shipping_profile_id,
            shipping_profile_name=shipping_profile_name,
            sku=sku,
            sold_as_is=sold_as_is,
            storage_location=storage_location,
            tax_exempt=tax_exempt,
            title=title,
            upc=upc,
            upc_does_not_apply=upc_does_not_apply,
            videos=videos,
            year=year,
            request_options=request_options,
        )
        return _response.data

    def all_listings_including_used_handmade_and_brand_new(
        self,
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
        All listings including used, handmade, and brand new

        Parameters
        ----------
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
        client.listings.all_listings_including_used_handmade_and_brand_new()
        """
        _response = self._raw_client.all_listings_including_used_handmade_and_brand_new(
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

    def individual_facets(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Individual facets

        Parameters
        ----------
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
        client.listings.individual_facets()
        """
        _response = self._raw_client.individual_facets(request_options=request_options)
        return _response.data

    def returns_the_latest_negotiation_for_the_requesting_user_given_a_listing_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the latest negotiation for the requesting user given a listing id

        Parameters
        ----------
        id : str

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
        client.listings.returns_the_latest_negotiation_for_the_requesting_user_given_a_listing_id(
            id="id",
        )
        """
        _response = self._raw_client.returns_the_latest_negotiation_for_the_requesting_user_given_a_listing_id(
            id, request_options=request_options
        )
        return _response.data

    def make_an_offer_to_the_seller_of_a_listing(
        self,
        id: str,
        *,
        price: str,
        message: typing.Optional[str] = OMIT,
        shipping_price: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Make an offer to the seller of a listing

        Parameters
        ----------
        id : str

        price : str
            Offer price

        message : typing.Optional[str]
            Message to include with counter offer

        shipping_price : typing.Optional[str]
            Shipping price (sellers only)

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
        client.listings.make_an_offer_to_the_seller_of_a_listing(
            id="id",
            price="price",
        )
        """
        _response = self._raw_client.make_an_offer_to_the_seller_of_a_listing(
            id, price=price, message=message, shipping_price=shipping_price, request_options=request_options
        )
        return _response.data

    def view_available_bump_tiers_and_stats_for_a_listing(
        self, listing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View available bump tiers and stats for a listing

        Parameters
        ----------
        listing_id : str

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
        client.listings.view_available_bump_tiers_and_stats_for_a_listing(
            listing_id="listing_id",
        )
        """
        _response = self._raw_client.view_available_bump_tiers_and_stats_for_a_listing(
            listing_id, request_options=request_options
        )
        return _response.data

    def bump_a_listing(
        self, listing_id: str, budget_type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Bump a listing

        Parameters
        ----------
        listing_id : str

        budget_type : str

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
        client.listings.bump_a_listing(
            listing_id="listing_id",
            budget_type="budget_type",
        )
        """
        _response = self._raw_client.bump_a_listing(listing_id, budget_type, request_options=request_options)
        return _response.data

    def start_a_conversation_with_a_seller(
        self, listing_id: str, *, body: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Start a conversation with a seller

        Parameters
        ----------
        listing_id : str

        body : str

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
        client.listings.start_a_conversation_with_a_seller(
            listing_id="listing_id",
            body="body",
        )
        """
        _response = self._raw_client.start_a_conversation_with_a_seller(
            listing_id, body=body, request_options=request_options
        )
        return _response.data

    def view_the_images_associated_with_a_particular_listing(
        self, listing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View the images associated with a particular listing

        Parameters
        ----------
        listing_id : str

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
        client.listings.view_the_images_associated_with_a_particular_listing(
            listing_id="listing_id",
        )
        """
        _response = self._raw_client.view_the_images_associated_with_a_particular_listing(
            listing_id, request_options=request_options
        )
        return _response.data

    def delete_an_image_from_a_listing(
        self, listing_id: str, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an image from a listing

        Parameters
        ----------
        listing_id : str

        image_id : str

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
        client.listings.delete_an_image_from_a_listing(
            listing_id="listing_id",
            image_id="image_id",
        )
        """
        _response = self._raw_client.delete_an_image_from_a_listing(
            listing_id, image_id, request_options=request_options
        )
        return _response.data

    def see_all_sales_that_include_a_listing(
        self, listing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        See all sales that include a listing.

        Parameters
        ----------
        listing_id : str

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
        client.listings.see_all_sales_that_include_a_listing(
            listing_id="listing_id",
        )
        """
        _response = self._raw_client.see_all_sales_that_include_a_listing(listing_id, request_options=request_options)
        return _response.data

    def listing_details(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Listing details

        Parameters
        ----------
        slug : str

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
        client.listings.listing_details(
            slug="slug",
        )
        """
        _response = self._raw_client.listing_details(slug, request_options=request_options)
        return _response.data

    def update_a_listing(
        self,
        slug: str,
        *,
        categories: typing.Optional[typing.Sequence[PutListingsSlugRequestCategoriesItem]] = OMIT,
        condition: typing.Optional[PutListingsSlugRequestCondition] = OMIT,
        description: typing.Optional[str] = OMIT,
        exclusive_channel: typing.Optional[PutListingsSlugRequestExclusiveChannel] = OMIT,
        finish: typing.Optional[str] = OMIT,
        has_inventory: typing.Optional[bool] = OMIT,
        inventory: typing.Optional[int] = OMIT,
        location: typing.Optional[PutListingsSlugRequestLocation] = OMIT,
        make: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        multi_item: typing.Optional[bool] = OMIT,
        offers_enabled: typing.Optional[bool] = OMIT,
        origin_country_code: typing.Optional[str] = OMIT,
        photos: typing.Optional[typing.Sequence[str]] = OMIT,
        preorder_info: typing.Optional[PutListingsSlugRequestPreorderInfo] = OMIT,
        price: typing.Optional[PutListingsSlugRequestPrice] = OMIT,
        prop65warning: typing.Optional[str] = OMIT,
        publish: typing.Optional[bool] = OMIT,
        seller: typing.Optional[PutListingsSlugRequestSeller] = OMIT,
        seller_cost: typing.Optional[str] = OMIT,
        shipping: typing.Optional[PutListingsSlugRequestShipping] = OMIT,
        shipping_profile_id: typing.Optional[str] = OMIT,
        shipping_profile_name: typing.Optional[str] = OMIT,
        sku: typing.Optional[str] = OMIT,
        sold_as_is: typing.Optional[bool] = OMIT,
        storage_location: typing.Optional[str] = OMIT,
        tax_exempt: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        upc: typing.Optional[str] = OMIT,
        upc_does_not_apply: typing.Optional[bool] = OMIT,
        videos: typing.Optional[typing.Sequence[PutListingsSlugRequestVideosItem]] = OMIT,
        year: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a listing

        Parameters
        ----------
        slug : str

        categories : typing.Optional[typing.Sequence[PutListingsSlugRequestCategoriesItem]]

        condition : typing.Optional[PutListingsSlugRequestCondition]
            Condition

        description : typing.Optional[str]
            Product description. Please keep formatting to a minimum.

        exclusive_channel : typing.Optional[PutListingsSlugRequestExclusiveChannel]
            Currently for users of seller sites only, this allows you to have a listing available only to your seller site by setting this to 'seller_site'

        finish : typing.Optional[str]
            Finish, e.g. 'Sunburst'

        has_inventory : typing.Optional[bool]
            Set true if selling more than one

        inventory : typing.Optional[int]
            Number of items available for sale. Reverb will increment and decrement automatically.

        location : typing.Optional[PutListingsSlugRequestLocation]

        make : typing.Optional[str]
            ex: Fender, Gibson

        model : typing.Optional[str]
            ex: Stratocaster, SG

        multi_item : typing.Optional[bool]
            Specifies if the listing is a bundle of multiple individual items

        offers_enabled : typing.Optional[bool]
            Whether the listing accepts negotiated offers (default: true)

        origin_country_code : typing.Optional[str]
            Country of origin/manufacture, ISO code (e.g: US)

        photos : typing.Optional[typing.Sequence[str]]
            An array of image URLs. Ex: ['http://my.site.com/image.jpg']

        preorder_info : typing.Optional[PutListingsSlugRequestPreorderInfo]
            Create or update a preorder listing. Requires opt-in. Please contact sales@reverb.com if you would like to activate this feature.

        price : typing.Optional[PutListingsSlugRequestPrice]

        prop65warning : typing.Optional[str]
            If your listing contains chemicals that are required to be reported under California Prop 65, please provide your warning statement. We will add the required 'Warning' label and link to California's information page, so you only need to provide the body of the warning. For more information, see https://www.p65warnings.ca.gov/new-proposition-65-warnings

        publish : typing.Optional[bool]
            Publish your listing if draft

        seller : typing.Optional[PutListingsSlugRequestSeller]

        seller_cost : typing.Optional[str]
            Cost of goods in your currency as a POSIX-compliant decimal number (internal use only, not shown to buyers)

        shipping : typing.Optional[PutListingsSlugRequestShipping]

        shipping_profile_id : typing.Optional[str]
            id of a shop's shipping profile

        shipping_profile_name : typing.Optional[str]
            DEPRECATED, please use shipping_profile_id. Name of a shipping profile

        sku : typing.Optional[str]
            Unique identifier for product

        sold_as_is : typing.Optional[bool]
            This item is sold As-Is and cannot be returned

        storage_location : typing.Optional[str]
            Internal note used by sellers to back reference their catalog system when entering a listing

        tax_exempt : typing.Optional[bool]
            Listing is exempt from taxes / VAT

        title : typing.Optional[str]
            Title of your listing

        upc : typing.Optional[str]
            Valid UPC code

        upc_does_not_apply : typing.Optional[bool]
            True if a brand new product has no UPC code, ie for a handmade or custom item

        videos : typing.Optional[typing.Sequence[PutListingsSlugRequestVideosItem]]
            List of YouTube video urls. Note: ONLY ONE ALLOWED

        year : typing.Optional[str]
            Supports many formats. Ex: 1979, mid-70s, late 90s

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
        client.listings.update_a_listing(
            slug="slug",
        )
        """
        _response = self._raw_client.update_a_listing(
            slug,
            categories=categories,
            condition=condition,
            description=description,
            exclusive_channel=exclusive_channel,
            finish=finish,
            has_inventory=has_inventory,
            inventory=inventory,
            location=location,
            make=make,
            model=model,
            multi_item=multi_item,
            offers_enabled=offers_enabled,
            origin_country_code=origin_country_code,
            photos=photos,
            preorder_info=preorder_info,
            price=price,
            prop65warning=prop65warning,
            publish=publish,
            seller=seller,
            seller_cost=seller_cost,
            shipping=shipping,
            shipping_profile_id=shipping_profile_id,
            shipping_profile_name=shipping_profile_name,
            sku=sku,
            sold_as_is=sold_as_is,
            storage_location=storage_location,
            tax_exempt=tax_exempt,
            title=title,
            upc=upc,
            upc_does_not_apply=upc_does_not_apply,
            videos=videos,
            year=year,
            request_options=request_options,
        )
        return _response.data

    def delete_a_draft_listing_cannot_be_used_on_non_drafts(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a draft listing. Cannot be used on non-drafts.

        Parameters
        ----------
        slug : str

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
        client.listings.delete_a_draft_listing_cannot_be_used_on_non_drafts(
            slug="slug",
        )
        """
        _response = self._raw_client.delete_a_draft_listing_cannot_be_used_on_non_drafts(
            slug, request_options=request_options
        )
        return _response.data

    def edit_listing(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Edit listing.

        Parameters
        ----------
        slug : str

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
        client.listings.edit_listing(
            slug="slug",
        )
        """
        _response = self._raw_client.edit_listing(slug, request_options=request_options)
        return _response.data

    def flag_a_listing_for_inappropriate_content_or_fraud(
        self,
        slug: str,
        *,
        reason: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Flag a listing for inappropriate content or fraud

        Parameters
        ----------
        slug : str

        reason : str
            Valid reasons: 'Sexuality/nudity', 'Hateful or inappropriate speech', 'Item not as described or potential fraud', 'Trademark infringement', 'Other'

        description : typing.Optional[str]
            User input description specifying what is flag-worthy about this listing

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
        client.listings.flag_a_listing_for_inappropriate_content_or_fraud(
            slug="slug",
            reason="reason",
        )
        """
        _response = self._raw_client.flag_a_listing_for_inappropriate_content_or_fraud(
            slug, reason=reason, description=description, request_options=request_options
        )
        return _response.data

    def view_reviews_of_a_listing(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        View reviews of a listing

        Parameters
        ----------
        slug : str

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
        client.listings.view_reviews_of_a_listing(
            slug="slug",
        )
        """
        _response = self._raw_client.view_reviews_of_a_listing(slug, request_options=request_options)
        return _response.data

    def create_a_review_for_a_listing(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create a review for a listing

        Parameters
        ----------
        slug : str

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
        client.listings.create_a_review_for_a_listing(
            slug="slug",
        )
        """
        _response = self._raw_client.create_a_review_for_a_listing(slug, request_options=request_options)
        return _response.data


class AsyncListingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawListingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawListingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawListingsClient
        """
        return self._raw_client

    async def default_search_of_listings_includes_only_used_handmade_add_a_filter_to_view_all_listings_or_use_the_listings_all_endpoint(
        self,
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
        Default search of listings includes only used & handmade. Add a filter to view all listings or use the /listings/all endpoint.

        Parameters
        ----------
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
            await client.listings.default_search_of_listings_includes_only_used_handmade_add_a_filter_to_view_all_listings_or_use_the_listings_all_endpoint()


        asyncio.run(main())
        """
        _response = await self._raw_client.default_search_of_listings_includes_only_used_handmade_add_a_filter_to_view_all_listings_or_use_the_listings_all_endpoint(
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

    async def create_a_listing(
        self,
        *,
        categories: typing.Optional[typing.Sequence[PostListingsRequestCategoriesItem]] = OMIT,
        condition: typing.Optional[PostListingsRequestCondition] = OMIT,
        description: typing.Optional[str] = OMIT,
        exclusive_channel: typing.Optional[PostListingsRequestExclusiveChannel] = OMIT,
        finish: typing.Optional[str] = OMIT,
        has_inventory: typing.Optional[bool] = OMIT,
        inventory: typing.Optional[int] = OMIT,
        location: typing.Optional[PostListingsRequestLocation] = OMIT,
        make: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        multi_item: typing.Optional[bool] = OMIT,
        offers_enabled: typing.Optional[bool] = OMIT,
        origin_country_code: typing.Optional[str] = OMIT,
        photos: typing.Optional[typing.Sequence[str]] = OMIT,
        preorder_info: typing.Optional[PostListingsRequestPreorderInfo] = OMIT,
        price: typing.Optional[PostListingsRequestPrice] = OMIT,
        prop65warning: typing.Optional[str] = OMIT,
        publish: typing.Optional[bool] = OMIT,
        seller: typing.Optional[PostListingsRequestSeller] = OMIT,
        seller_cost: typing.Optional[str] = OMIT,
        shipping: typing.Optional[PostListingsRequestShipping] = OMIT,
        shipping_profile_id: typing.Optional[str] = OMIT,
        shipping_profile_name: typing.Optional[str] = OMIT,
        sku: typing.Optional[str] = OMIT,
        sold_as_is: typing.Optional[bool] = OMIT,
        storage_location: typing.Optional[str] = OMIT,
        tax_exempt: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        upc: typing.Optional[str] = OMIT,
        upc_does_not_apply: typing.Optional[bool] = OMIT,
        videos: typing.Optional[typing.Sequence[PostListingsRequestVideosItem]] = OMIT,
        year: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Create a listing

        Parameters
        ----------
        categories : typing.Optional[typing.Sequence[PostListingsRequestCategoriesItem]]

        condition : typing.Optional[PostListingsRequestCondition]
            Condition

        description : typing.Optional[str]
            Product description. Please keep formatting to a minimum.

        exclusive_channel : typing.Optional[PostListingsRequestExclusiveChannel]
            Currently for users of seller sites only, this allows you to have a listing available only to your seller site by setting this to 'seller_site'

        finish : typing.Optional[str]
            Finish, e.g. 'Sunburst'

        has_inventory : typing.Optional[bool]
            Set true if selling more than one

        inventory : typing.Optional[int]
            Number of items available for sale. Reverb will increment and decrement automatically.

        location : typing.Optional[PostListingsRequestLocation]

        make : typing.Optional[str]
            ex: Fender, Gibson

        model : typing.Optional[str]
            ex: Stratocaster, SG

        multi_item : typing.Optional[bool]
            Specifies if the listing is a bundle of multiple individual items

        offers_enabled : typing.Optional[bool]
            Whether the listing accepts negotiated offers (default: true)

        origin_country_code : typing.Optional[str]
            Country of origin/manufacture, ISO code (e.g: US)

        photos : typing.Optional[typing.Sequence[str]]
            An array of image URLs. Ex: ['http://my.site.com/image.jpg']

        preorder_info : typing.Optional[PostListingsRequestPreorderInfo]
            Create or update a preorder listing. Requires opt-in. Please contact sales@reverb.com if you would like to activate this feature.

        price : typing.Optional[PostListingsRequestPrice]

        prop65warning : typing.Optional[str]
            If your listing contains chemicals that are required to be reported under California Prop 65, please provide your warning statement. We will add the required 'Warning' label and link to California's information page, so you only need to provide the body of the warning. For more information, see https://www.p65warnings.ca.gov/new-proposition-65-warnings

        publish : typing.Optional[bool]
            Publish your listing if draft

        seller : typing.Optional[PostListingsRequestSeller]

        seller_cost : typing.Optional[str]
            Cost of goods in your currency as a POSIX-compliant decimal number (internal use only, not shown to buyers)

        shipping : typing.Optional[PostListingsRequestShipping]

        shipping_profile_id : typing.Optional[str]
            id of a shop's shipping profile

        shipping_profile_name : typing.Optional[str]
            DEPRECATED, please use shipping_profile_id. Name of a shipping profile

        sku : typing.Optional[str]
            Unique identifier for product

        sold_as_is : typing.Optional[bool]
            This item is sold As-Is and cannot be returned

        storage_location : typing.Optional[str]
            Internal note used by sellers to back reference their catalog system when entering a listing

        tax_exempt : typing.Optional[bool]
            Listing is exempt from taxes / VAT

        title : typing.Optional[str]
            Title of your listing

        upc : typing.Optional[str]
            Valid UPC code

        upc_does_not_apply : typing.Optional[bool]
            True if a brand new product has no UPC code, ie for a handmade or custom item

        videos : typing.Optional[typing.Sequence[PostListingsRequestVideosItem]]
            List of YouTube video urls. Note: ONLY ONE ALLOWED

        year : typing.Optional[str]
            Supports many formats. Ex: 1979, mid-70s, late 90s

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
            await client.listings.create_a_listing()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_listing(
            categories=categories,
            condition=condition,
            description=description,
            exclusive_channel=exclusive_channel,
            finish=finish,
            has_inventory=has_inventory,
            inventory=inventory,
            location=location,
            make=make,
            model=model,
            multi_item=multi_item,
            offers_enabled=offers_enabled,
            origin_country_code=origin_country_code,
            photos=photos,
            preorder_info=preorder_info,
            price=price,
            prop65warning=prop65warning,
            publish=publish,
            seller=seller,
            seller_cost=seller_cost,
            shipping=shipping,
            shipping_profile_id=shipping_profile_id,
            shipping_profile_name=shipping_profile_name,
            sku=sku,
            sold_as_is=sold_as_is,
            storage_location=storage_location,
            tax_exempt=tax_exempt,
            title=title,
            upc=upc,
            upc_does_not_apply=upc_does_not_apply,
            videos=videos,
            year=year,
            request_options=request_options,
        )
        return _response.data

    async def all_listings_including_used_handmade_and_brand_new(
        self,
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
        All listings including used, handmade, and brand new

        Parameters
        ----------
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
            await client.listings.all_listings_including_used_handmade_and_brand_new()


        asyncio.run(main())
        """
        _response = await self._raw_client.all_listings_including_used_handmade_and_brand_new(
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

    async def individual_facets(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Individual facets

        Parameters
        ----------
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
            await client.listings.individual_facets()


        asyncio.run(main())
        """
        _response = await self._raw_client.individual_facets(request_options=request_options)
        return _response.data

    async def returns_the_latest_negotiation_for_the_requesting_user_given_a_listing_id(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns the latest negotiation for the requesting user given a listing id

        Parameters
        ----------
        id : str

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
            await client.listings.returns_the_latest_negotiation_for_the_requesting_user_given_a_listing_id(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_the_latest_negotiation_for_the_requesting_user_given_a_listing_id(
            id, request_options=request_options
        )
        return _response.data

    async def make_an_offer_to_the_seller_of_a_listing(
        self,
        id: str,
        *,
        price: str,
        message: typing.Optional[str] = OMIT,
        shipping_price: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Make an offer to the seller of a listing

        Parameters
        ----------
        id : str

        price : str
            Offer price

        message : typing.Optional[str]
            Message to include with counter offer

        shipping_price : typing.Optional[str]
            Shipping price (sellers only)

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
            await client.listings.make_an_offer_to_the_seller_of_a_listing(
                id="id",
                price="price",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.make_an_offer_to_the_seller_of_a_listing(
            id, price=price, message=message, shipping_price=shipping_price, request_options=request_options
        )
        return _response.data

    async def view_available_bump_tiers_and_stats_for_a_listing(
        self, listing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View available bump tiers and stats for a listing

        Parameters
        ----------
        listing_id : str

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
            await client.listings.view_available_bump_tiers_and_stats_for_a_listing(
                listing_id="listing_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.view_available_bump_tiers_and_stats_for_a_listing(
            listing_id, request_options=request_options
        )
        return _response.data

    async def bump_a_listing(
        self, listing_id: str, budget_type: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Bump a listing

        Parameters
        ----------
        listing_id : str

        budget_type : str

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
            await client.listings.bump_a_listing(
                listing_id="listing_id",
                budget_type="budget_type",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bump_a_listing(listing_id, budget_type, request_options=request_options)
        return _response.data

    async def start_a_conversation_with_a_seller(
        self, listing_id: str, *, body: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Start a conversation with a seller

        Parameters
        ----------
        listing_id : str

        body : str

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
            await client.listings.start_a_conversation_with_a_seller(
                listing_id="listing_id",
                body="body",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_a_conversation_with_a_seller(
            listing_id, body=body, request_options=request_options
        )
        return _response.data

    async def view_the_images_associated_with_a_particular_listing(
        self, listing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View the images associated with a particular listing

        Parameters
        ----------
        listing_id : str

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
            await client.listings.view_the_images_associated_with_a_particular_listing(
                listing_id="listing_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.view_the_images_associated_with_a_particular_listing(
            listing_id, request_options=request_options
        )
        return _response.data

    async def delete_an_image_from_a_listing(
        self, listing_id: str, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an image from a listing

        Parameters
        ----------
        listing_id : str

        image_id : str

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
            await client.listings.delete_an_image_from_a_listing(
                listing_id="listing_id",
                image_id="image_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_an_image_from_a_listing(
            listing_id, image_id, request_options=request_options
        )
        return _response.data

    async def see_all_sales_that_include_a_listing(
        self, listing_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        See all sales that include a listing.

        Parameters
        ----------
        listing_id : str

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
            await client.listings.see_all_sales_that_include_a_listing(
                listing_id="listing_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.see_all_sales_that_include_a_listing(
            listing_id, request_options=request_options
        )
        return _response.data

    async def listing_details(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Listing details

        Parameters
        ----------
        slug : str

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
            await client.listings.listing_details(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listing_details(slug, request_options=request_options)
        return _response.data

    async def update_a_listing(
        self,
        slug: str,
        *,
        categories: typing.Optional[typing.Sequence[PutListingsSlugRequestCategoriesItem]] = OMIT,
        condition: typing.Optional[PutListingsSlugRequestCondition] = OMIT,
        description: typing.Optional[str] = OMIT,
        exclusive_channel: typing.Optional[PutListingsSlugRequestExclusiveChannel] = OMIT,
        finish: typing.Optional[str] = OMIT,
        has_inventory: typing.Optional[bool] = OMIT,
        inventory: typing.Optional[int] = OMIT,
        location: typing.Optional[PutListingsSlugRequestLocation] = OMIT,
        make: typing.Optional[str] = OMIT,
        model: typing.Optional[str] = OMIT,
        multi_item: typing.Optional[bool] = OMIT,
        offers_enabled: typing.Optional[bool] = OMIT,
        origin_country_code: typing.Optional[str] = OMIT,
        photos: typing.Optional[typing.Sequence[str]] = OMIT,
        preorder_info: typing.Optional[PutListingsSlugRequestPreorderInfo] = OMIT,
        price: typing.Optional[PutListingsSlugRequestPrice] = OMIT,
        prop65warning: typing.Optional[str] = OMIT,
        publish: typing.Optional[bool] = OMIT,
        seller: typing.Optional[PutListingsSlugRequestSeller] = OMIT,
        seller_cost: typing.Optional[str] = OMIT,
        shipping: typing.Optional[PutListingsSlugRequestShipping] = OMIT,
        shipping_profile_id: typing.Optional[str] = OMIT,
        shipping_profile_name: typing.Optional[str] = OMIT,
        sku: typing.Optional[str] = OMIT,
        sold_as_is: typing.Optional[bool] = OMIT,
        storage_location: typing.Optional[str] = OMIT,
        tax_exempt: typing.Optional[bool] = OMIT,
        title: typing.Optional[str] = OMIT,
        upc: typing.Optional[str] = OMIT,
        upc_does_not_apply: typing.Optional[bool] = OMIT,
        videos: typing.Optional[typing.Sequence[PutListingsSlugRequestVideosItem]] = OMIT,
        year: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update a listing

        Parameters
        ----------
        slug : str

        categories : typing.Optional[typing.Sequence[PutListingsSlugRequestCategoriesItem]]

        condition : typing.Optional[PutListingsSlugRequestCondition]
            Condition

        description : typing.Optional[str]
            Product description. Please keep formatting to a minimum.

        exclusive_channel : typing.Optional[PutListingsSlugRequestExclusiveChannel]
            Currently for users of seller sites only, this allows you to have a listing available only to your seller site by setting this to 'seller_site'

        finish : typing.Optional[str]
            Finish, e.g. 'Sunburst'

        has_inventory : typing.Optional[bool]
            Set true if selling more than one

        inventory : typing.Optional[int]
            Number of items available for sale. Reverb will increment and decrement automatically.

        location : typing.Optional[PutListingsSlugRequestLocation]

        make : typing.Optional[str]
            ex: Fender, Gibson

        model : typing.Optional[str]
            ex: Stratocaster, SG

        multi_item : typing.Optional[bool]
            Specifies if the listing is a bundle of multiple individual items

        offers_enabled : typing.Optional[bool]
            Whether the listing accepts negotiated offers (default: true)

        origin_country_code : typing.Optional[str]
            Country of origin/manufacture, ISO code (e.g: US)

        photos : typing.Optional[typing.Sequence[str]]
            An array of image URLs. Ex: ['http://my.site.com/image.jpg']

        preorder_info : typing.Optional[PutListingsSlugRequestPreorderInfo]
            Create or update a preorder listing. Requires opt-in. Please contact sales@reverb.com if you would like to activate this feature.

        price : typing.Optional[PutListingsSlugRequestPrice]

        prop65warning : typing.Optional[str]
            If your listing contains chemicals that are required to be reported under California Prop 65, please provide your warning statement. We will add the required 'Warning' label and link to California's information page, so you only need to provide the body of the warning. For more information, see https://www.p65warnings.ca.gov/new-proposition-65-warnings

        publish : typing.Optional[bool]
            Publish your listing if draft

        seller : typing.Optional[PutListingsSlugRequestSeller]

        seller_cost : typing.Optional[str]
            Cost of goods in your currency as a POSIX-compliant decimal number (internal use only, not shown to buyers)

        shipping : typing.Optional[PutListingsSlugRequestShipping]

        shipping_profile_id : typing.Optional[str]
            id of a shop's shipping profile

        shipping_profile_name : typing.Optional[str]
            DEPRECATED, please use shipping_profile_id. Name of a shipping profile

        sku : typing.Optional[str]
            Unique identifier for product

        sold_as_is : typing.Optional[bool]
            This item is sold As-Is and cannot be returned

        storage_location : typing.Optional[str]
            Internal note used by sellers to back reference their catalog system when entering a listing

        tax_exempt : typing.Optional[bool]
            Listing is exempt from taxes / VAT

        title : typing.Optional[str]
            Title of your listing

        upc : typing.Optional[str]
            Valid UPC code

        upc_does_not_apply : typing.Optional[bool]
            True if a brand new product has no UPC code, ie for a handmade or custom item

        videos : typing.Optional[typing.Sequence[PutListingsSlugRequestVideosItem]]
            List of YouTube video urls. Note: ONLY ONE ALLOWED

        year : typing.Optional[str]
            Supports many formats. Ex: 1979, mid-70s, late 90s

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
            await client.listings.update_a_listing(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_listing(
            slug,
            categories=categories,
            condition=condition,
            description=description,
            exclusive_channel=exclusive_channel,
            finish=finish,
            has_inventory=has_inventory,
            inventory=inventory,
            location=location,
            make=make,
            model=model,
            multi_item=multi_item,
            offers_enabled=offers_enabled,
            origin_country_code=origin_country_code,
            photos=photos,
            preorder_info=preorder_info,
            price=price,
            prop65warning=prop65warning,
            publish=publish,
            seller=seller,
            seller_cost=seller_cost,
            shipping=shipping,
            shipping_profile_id=shipping_profile_id,
            shipping_profile_name=shipping_profile_name,
            sku=sku,
            sold_as_is=sold_as_is,
            storage_location=storage_location,
            tax_exempt=tax_exempt,
            title=title,
            upc=upc,
            upc_does_not_apply=upc_does_not_apply,
            videos=videos,
            year=year,
            request_options=request_options,
        )
        return _response.data

    async def delete_a_draft_listing_cannot_be_used_on_non_drafts(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a draft listing. Cannot be used on non-drafts.

        Parameters
        ----------
        slug : str

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
            await client.listings.delete_a_draft_listing_cannot_be_used_on_non_drafts(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_draft_listing_cannot_be_used_on_non_drafts(
            slug, request_options=request_options
        )
        return _response.data

    async def edit_listing(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Edit listing.

        Parameters
        ----------
        slug : str

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
            await client.listings.edit_listing(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_listing(slug, request_options=request_options)
        return _response.data

    async def flag_a_listing_for_inappropriate_content_or_fraud(
        self,
        slug: str,
        *,
        reason: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Flag a listing for inappropriate content or fraud

        Parameters
        ----------
        slug : str

        reason : str
            Valid reasons: 'Sexuality/nudity', 'Hateful or inappropriate speech', 'Item not as described or potential fraud', 'Trademark infringement', 'Other'

        description : typing.Optional[str]
            User input description specifying what is flag-worthy about this listing

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
            await client.listings.flag_a_listing_for_inappropriate_content_or_fraud(
                slug="slug",
                reason="reason",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.flag_a_listing_for_inappropriate_content_or_fraud(
            slug, reason=reason, description=description, request_options=request_options
        )
        return _response.data

    async def view_reviews_of_a_listing(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        View reviews of a listing

        Parameters
        ----------
        slug : str

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
            await client.listings.view_reviews_of_a_listing(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.view_reviews_of_a_listing(slug, request_options=request_options)
        return _response.data

    async def create_a_review_for_a_listing(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create a review for a listing

        Parameters
        ----------
        slug : str

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
            await client.listings.create_a_review_for_a_listing(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_review_for_a_listing(slug, request_options=request_options)
        return _response.data
