

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawMyClient, RawMyClient
from .types.post_my_follows_search_request_currency import PostMyFollowsSearchRequestCurrency
from .types.post_my_follows_search_request_listing_type import PostMyFollowsSearchRequestListingType
from .types.post_my_negotiations_id_counter_request_offer_items_item import (
    PostMyNegotiationsIdCounterRequestOfferItemsItem,
)
from .types.post_my_negotiations_id_counter_request_price import PostMyNegotiationsIdCounterRequestPrice
from .types.post_my_negotiations_id_counter_request_shipping_price import (
    PostMyNegotiationsIdCounterRequestShippingPrice,
)
from .types.put_my_listings_slug_state_end_request_reason import PutMyListingsSlugStateEndRequestReason


OMIT = typing.cast(typing.Any, ...)


class MyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMyClient
        """
        return self._raw_client

    def get_account_details(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get account details

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
        client.my.get_account_details()
        """
        _response = self._raw_client.get_account_details(request_options=request_options)
        return _response.data

    def update_account_details(
        self,
        *,
        currency: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        locale_code: typing.Optional[str] = OMIT,
        shipping_region_code: typing.Optional[str] = OMIT,
        third_party_ad_data_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update account details

        Parameters
        ----------
        currency : typing.Optional[str]
            The currency preference for the account

        first_name : typing.Optional[str]
            The first name of the account holder

        last_name : typing.Optional[str]
            The last name of the account holder

        locale_code : typing.Optional[str]
            The locale code for the account

        shipping_region_code : typing.Optional[str]
            The shipping region preference for the account

        third_party_ad_data_consent : typing.Optional[bool]
            The privacy setting preference for the account

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
        client.my.update_account_details()
        """
        _response = self._raw_client.update_account_details(
            currency=currency,
            first_name=first_name,
            last_name=last_name,
            locale_code=locale_code,
            shipping_region_code=shipping_region_code,
            third_party_ad_data_consent=third_party_ad_data_consent,
            request_options=request_options,
        )
        return _response.data

    def see_all_addresses_in_your_address_book(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        See all addresses in your address book

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
        client.my.see_all_addresses_in_your_address_book()
        """
        _response = self._raw_client.see_all_addresses_in_your_address_book(request_options=request_options)
        return _response.data

    def create_a_new_address_in_your_address_book(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create a new address in your address book

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
        client.my.create_a_new_address_in_your_address_book()
        """
        _response = self._raw_client.create_a_new_address_in_your_address_book(request_options=request_options)
        return _response.data

    def update_an_existing_address_in_your_address_book(
        self, address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Update an existing address in your address book

        Parameters
        ----------
        address_id : str

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
        client.my.update_an_existing_address_in_your_address_book(
            address_id="address_id",
        )
        """
        _response = self._raw_client.update_an_existing_address_in_your_address_book(
            address_id, request_options=request_options
        )
        return _response.data

    def delete_an_existing_address_in_your_address_book(
        self, address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an existing address in your address book

        Parameters
        ----------
        address_id : str

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
        client.my.delete_an_existing_address_in_your_address_book(
            address_id="address_id",
        )
        """
        _response = self._raw_client.delete_an_existing_address_in_your_address_book(
            address_id, request_options=request_options
        )
        return _response.data

    def get_a_list_of_your_conversations(
        self,
        *,
        search: typing.Optional[str] = None,
        unread_only: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a list of your conversations

        Parameters
        ----------
        search : typing.Optional[str]
            Query string to search conversations by

        unread_only : typing.Optional[bool]
            Show unread conversations only

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
        client.my.get_a_list_of_your_conversations()
        """
        _response = self._raw_client.get_a_list_of_your_conversations(
            search=search,
            unread_only=unread_only,
            page=page,
            per_page=per_page,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def start_a_conversation(
        self,
        *,
        body: str,
        cloudinary_photos: typing.Optional[typing.Sequence[str]] = OMIT,
        listing_id: typing.Optional[int] = OMIT,
        recipient_id: typing.Optional[int] = OMIT,
        recipient_uuid: typing.Optional[str] = OMIT,
        shop_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Start a conversation

        Parameters
        ----------
        body : str
            The body of the message

        cloudinary_photos : typing.Optional[typing.Sequence[str]]
            An array of cloudinary data hashes (Reverb internal use only).

        listing_id : typing.Optional[int]
            The id of the listing being discussed

        recipient_id : typing.Optional[int]
            The id of the user you are trying to contact

        recipient_uuid : typing.Optional[str]
            The uuid of the user you are trying to contact

        shop_id : typing.Optional[str]
            The id of the shop you are trying to contact

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
        client.my.start_a_conversation(
            body="body",
        )
        """
        _response = self._raw_client.start_a_conversation(
            body=body,
            cloudinary_photos=cloudinary_photos,
            listing_id=listing_id,
            recipient_id=recipient_id,
            recipient_uuid=recipient_uuid,
            shop_id=shop_id,
            request_options=request_options,
        )
        return _response.data

    def send_a_message(
        self, conversation_id: str, *, body: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Send a message

        Parameters
        ----------
        conversation_id : str

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
        client.my.send_a_message(
            conversation_id="conversation_id",
            body="body",
        )
        """
        _response = self._raw_client.send_a_message(conversation_id, body=body, request_options=request_options)
        return _response.data

    def display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Display conversation details with messages in natural time order (oldest to newest)

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
        client.my.display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest(
            id="id",
        )
        """
        _response = self._raw_client.display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest(
            id, request_options=request_options
        )
        return _response.data

    def mark_a_conversation_read_unread(
        self, id: str, *, read: typing.Optional[bool] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mark a conversation read/unread

        Parameters
        ----------
        id : str

        read : typing.Optional[bool]
            Should the conversation be marked as read

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
        client.my.mark_a_conversation_read_unread(
            id="id",
        )
        """
        _response = self._raw_client.mark_a_conversation_read_unread(id, read=read, request_options=request_options)
        return _response.data

    def get_your_actionable_status_counts(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get your actionable status counts

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
        client.my.get_your_actionable_status_counts()
        """
        _response = self._raw_client.get_your_actionable_status_counts(request_options=request_options)
        return _response.data

    def post_my_curated_set_product_product_id(
        self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        product_id : str

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
        client.my.post_my_curated_set_product_product_id(
            product_id="product_id",
        )
        """
        _response = self._raw_client.post_my_curated_set_product_product_id(product_id, request_options=request_options)
        return _response.data

    def delete_my_curated_set_product_product_id(
        self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        product_id : str

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
        client.my.delete_my_curated_set_product_product_id(
            product_id="product_id",
        )
        """
        _response = self._raw_client.delete_my_curated_set_product_product_id(
            product_id, request_options=request_options
        )
        return _response.data

    def get_listings_from_your_feed(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get listings from your feed

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
        client.my.get_listings_from_your_feed()
        """
        _response = self._raw_client.get_listings_from_your_feed(request_options=request_options)
        return _response.data

    def get_your_feed_customization_options(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        get your feed customization options

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
        client.my.get_your_feed_customization_options()
        """
        _response = self._raw_client.get_your_feed_customization_options(request_options=request_options)
        return _response.data

    def get_your_feed(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        get your feed

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
        client.my.get_your_feed()
        """
        _response = self._raw_client.get_your_feed(request_options=request_options)
        return _response.data

    def list_of_received_feedback(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of received feedback

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
        client.my.list_of_received_feedback()
        """
        _response = self._raw_client.list_of_received_feedback(request_options=request_options)
        return _response.data

    def list_of_sent_feedback(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of sent feedback

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
        client.my.list_of_sent_feedback()
        """
        _response = self._raw_client.list_of_sent_feedback(request_options=request_options)
        return _response.data

    def see_what_the_user_is_following(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        See what the user is following

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
        client.my.see_what_the_user_is_following()
        """
        _response = self._raw_client.see_what_the_user_is_following(request_options=request_options)
        return _response.data

    def returns_a_users_article_category_follows(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a user's ArticleCategoryFollows

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
        client.my.returns_a_users_article_category_follows()
        """
        _response = self._raw_client.returns_a_users_article_category_follows(request_options=request_options)
        return _response.data

    def set_a_users_article_category_follows(
        self, *, category_uuids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Set a user's ArticleCategoryFollows

        Parameters
        ----------
        category_uuids : str

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
        client.my.set_a_users_article_category_follows(
            category_uuids="category_uuids",
        )
        """
        _response = self._raw_client.set_a_users_article_category_follows(
            category_uuids=category_uuids, request_options=request_options
        )
        return _response.data

    def follow_status_for_a_brand(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow status for a brand

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
        client.my.follow_status_for_a_brand(
            slug="slug",
        )
        """
        _response = self._raw_client.follow_status_for_a_brand(slug, request_options=request_options)
        return _response.data

    def follow_a_brand(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow a brand

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
        client.my.follow_a_brand(
            slug="slug",
        )
        """
        _response = self._raw_client.follow_a_brand(slug, request_options=request_options)
        return _response.data

    def unfollow_a_brand(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Unfollow a brand

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
        client.my.unfollow_a_brand(
            slug="slug",
        )
        """
        _response = self._raw_client.unfollow_a_brand(slug, request_options=request_options)
        return _response.data

    def follow_status_for_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a subcategory

        Parameters
        ----------
        category : str

        subcategory : str

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
        client.my.follow_status_for_a_subcategory(
            category="category",
            subcategory="subcategory",
        )
        """
        _response = self._raw_client.follow_status_for_a_subcategory(
            category, subcategory, request_options=request_options
        )
        return _response.data

    def follow_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow a subcategory

        Parameters
        ----------
        category : str

        subcategory : str

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
        client.my.follow_a_subcategory(
            category="category",
            subcategory="subcategory",
        )
        """
        _response = self._raw_client.follow_a_subcategory(category, subcategory, request_options=request_options)
        return _response.data

    def unfollow_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unfollow a subcategory

        Parameters
        ----------
        category : str

        subcategory : str

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
        client.my.unfollow_a_subcategory(
            category="category",
            subcategory="subcategory",
        )
        """
        _response = self._raw_client.unfollow_a_subcategory(category, subcategory, request_options=request_options)
        return _response.data

    def follow_status_for_a_category(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a category

        Parameters
        ----------
        identifier : str

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
        client.my.follow_status_for_a_category(
            identifier="identifier",
        )
        """
        _response = self._raw_client.follow_status_for_a_category(identifier, request_options=request_options)
        return _response.data

    def follow_a_category(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow a category

        Parameters
        ----------
        uuid_ : str

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
        client.my.follow_a_category(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.follow_a_category(uuid_, request_options=request_options)
        return _response.data

    def unfollow_a_category(self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Unfollow a category

        Parameters
        ----------
        identifier : str

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
        client.my.unfollow_a_category(
            identifier="identifier",
        )
        """
        _response = self._raw_client.unfollow_a_category(identifier, request_options=request_options)
        return _response.data

    def follow_status_for_a_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a collection

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
        client.my.follow_status_for_a_collection(
            slug="slug",
        )
        """
        _response = self._raw_client.follow_status_for_a_collection(slug, request_options=request_options)
        return _response.data

    def follow_a_collection(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow a collection

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
        client.my.follow_a_collection(
            slug="slug",
        )
        """
        _response = self._raw_client.follow_a_collection(slug, request_options=request_options)
        return _response.data

    def unfollow_a_collection(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Unfollow a collection

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
        client.my.unfollow_a_collection(
            slug="slug",
        )
        """
        _response = self._raw_client.unfollow_a_collection(slug, request_options=request_options)
        return _response.data

    def follow_status_for_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a handpicked collection

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
        client.my.follow_status_for_a_handpicked_collection(
            slug="slug",
        )
        """
        _response = self._raw_client.follow_status_for_a_handpicked_collection(slug, request_options=request_options)
        return _response.data

    def follow_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow a handpicked collection

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
        client.my.follow_a_handpicked_collection(
            slug="slug",
        )
        """
        _response = self._raw_client.follow_a_handpicked_collection(slug, request_options=request_options)
        return _response.data

    def unfollow_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unfollow a handpicked collection

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
        client.my.unfollow_a_handpicked_collection(
            slug="slug",
        )
        """
        _response = self._raw_client.unfollow_a_handpicked_collection(slug, request_options=request_options)
        return _response.data

    def follow_status_for_a_search(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow status for a search

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
        client.my.follow_status_for_a_search()
        """
        _response = self._raw_client.follow_status_for_a_search(request_options=request_options)
        return _response.data

    def follow_a_search(
        self,
        *,
        accepts_gift_cards: typing.Optional[bool] = OMIT,
        accepts_payment_plans: typing.Optional[bool] = OMIT,
        auction_price_max: typing.Optional[float] = OMIT,
        category: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Sequence[str]] = OMIT,
        currency: typing.Optional[PostMyFollowsSearchRequestCurrency] = OMIT,
        decade: typing.Optional[str] = OMIT,
        exclude_auctions: typing.Optional[bool] = OMIT,
        finish: typing.Optional[str] = OMIT,
        handmade: typing.Optional[bool] = OMIT,
        item_city: typing.Optional[str] = OMIT,
        item_country: typing.Optional[str] = OMIT,
        item_region: typing.Optional[str] = OMIT,
        item_state: typing.Optional[str] = OMIT,
        listing_type: typing.Optional[PostMyFollowsSearchRequestListingType] = OMIT,
        local_pickup: typing.Optional[bool] = OMIT,
        make: typing.Optional[typing.Sequence[str]] = OMIT,
        model: typing.Optional[str] = OMIT,
        must_not: typing.Optional[str] = OMIT,
        not_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        preferred_seller: typing.Optional[bool] = OMIT,
        price_max: typing.Optional[float] = OMIT,
        price_min: typing.Optional[float] = OMIT,
        product_type: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        ships_to: typing.Optional[str] = OMIT,
        shop: typing.Optional[str] = OMIT,
        shop_id: typing.Optional[str] = OMIT,
        watchers_count_min: typing.Optional[int] = OMIT,
        year_max: typing.Optional[int] = OMIT,
        year_min: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Follow a search

        Parameters
        ----------
        accepts_gift_cards : typing.Optional[bool]
            If true, include only items that accept gift cards

        accepts_payment_plans : typing.Optional[bool]
            If true, only show items that can be purchased with a payment plan

        auction_price_max : typing.Optional[float]
            Maximum current auction price

        category : typing.Optional[str]
            Category slug from /api/categories

        conditions : typing.Optional[typing.Sequence[str]]
            Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint

        currency : typing.Optional[PostMyFollowsSearchRequestCurrency]
            The currency to be used for the price filters

        decade : typing.Optional[str]
            Decade: e.g. 1970s, early 70s

        exclude_auctions : typing.Optional[bool]
            If true, exclude auctions

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

        listing_type : typing.Optional[PostMyFollowsSearchRequestListingType]
            Type of listing: auctions,offers

        local_pickup : typing.Optional[bool]
            Only items that offer local pickup

        make : typing.Optional[typing.Sequence[str]]
            Make(s)/brand of item (e.g. Fender). Can take a single value or an array.

        model : typing.Optional[str]
            Model of item (e.g. Stratocaster)

        must_not : typing.Optional[str]
            Search term negation. If you want to exclude a term, add it here

        not_ids : typing.Optional[typing.Sequence[int]]
            Listing ID negation. If you want to exclude a listing, add it here.

        preferred_seller : typing.Optional[bool]
            If true, include only items by Reverb Preferred Sellers

        price_max : typing.Optional[float]
            Maximum price of search results (USD)

        price_min : typing.Optional[float]
            Minimum price of search results (USD)

        product_type : typing.Optional[str]
            Product type slug from /api/categories

        query : typing.Optional[str]
            Search query.

        ships_to : typing.Optional[str]
            Limit search to items that ship to this country code

        shop : typing.Optional[str]
            Slug of shop to search

        shop_id : typing.Optional[str]
            ID of shop to search

        watchers_count_min : typing.Optional[int]
            Minimum number of watchers (used to find popular items)

        year_max : typing.Optional[int]
            Maximum year of manufacture

        year_min : typing.Optional[int]
            Minumum year of manufacture

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
        client.my.follow_a_search()
        """
        _response = self._raw_client.follow_a_search(
            accepts_gift_cards=accepts_gift_cards,
            accepts_payment_plans=accepts_payment_plans,
            auction_price_max=auction_price_max,
            category=category,
            conditions=conditions,
            currency=currency,
            decade=decade,
            exclude_auctions=exclude_auctions,
            finish=finish,
            handmade=handmade,
            item_city=item_city,
            item_country=item_country,
            item_region=item_region,
            item_state=item_state,
            listing_type=listing_type,
            local_pickup=local_pickup,
            make=make,
            model=model,
            must_not=must_not,
            not_ids=not_ids,
            preferred_seller=preferred_seller,
            price_max=price_max,
            price_min=price_min,
            product_type=product_type,
            query=query,
            ships_to=ships_to,
            shop=shop,
            shop_id=shop_id,
            watchers_count_min=watchers_count_min,
            year_max=year_max,
            year_min=year_min,
            request_options=request_options,
        )
        return _response.data

    def follow_status_for_a_shop(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow status for a shop

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
        client.my.follow_status_for_a_shop(
            slug="slug",
        )
        """
        _response = self._raw_client.follow_status_for_a_shop(slug, request_options=request_options)
        return _response.data

    def follow_a_shop(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow a shop

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
        client.my.follow_a_shop(
            slug="slug",
        )
        """
        _response = self._raw_client.follow_a_shop(slug, request_options=request_options)
        return _response.data

    def unfollow_a_shop(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Unfollow a shop

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
        client.my.unfollow_a_shop(
            slug="slug",
        )
        """
        _response = self._raw_client.unfollow_a_shop(slug, request_options=request_options)
        return _response.data

    def delete_a_follow(self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a follow

        Parameters
        ----------
        follow_id : str

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
        client.my.delete_a_follow(
            follow_id="follow_id",
        )
        """
        _response = self._raw_client.delete_a_follow(follow_id, request_options=request_options)
        return _response.data

    def post_my_follows_follow_id_alert(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        follow_id : str

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
        client.my.post_my_follows_follow_id_alert(
            follow_id="follow_id",
        )
        """
        _response = self._raw_client.post_my_follows_follow_id_alert(follow_id, request_options=request_options)
        return _response.data

    def delete_my_follows_follow_id_alert(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        follow_id : str

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
        client.my.delete_my_follows_follow_id_alert(
            follow_id="follow_id",
        )
        """
        _response = self._raw_client.delete_my_follows_follow_id_alert(follow_id, request_options=request_options)
        return _response.data

    def retrieve_a_list_of_live_listings_for_the_seller_to_search_all_listings_specify_state_all(
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
        state: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieve a list of live listings for the seller. To search all listings specify state=all

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

        state : typing.Optional[str]
            Available: ["all", "draft", "ended", "live", "ordered", "sold_out", "suspended", "seller_unavailable"]. Defaults to 'live'

        sku : typing.Optional[str]
            Find a listing by sku

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
        client.my.retrieve_a_list_of_live_listings_for_the_seller_to_search_all_listings_specify_state_all()
        """
        _response = (
            self._raw_client.retrieve_a_list_of_live_listings_for_the_seller_to_search_all_listings_specify_state_all(
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
                state=state,
                sku=sku,
                request_options=request_options,
            )
        )
        return _response.data

    def retrieve_a_list_your_draft_listings(
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieve a list your draft listings

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
        client.my.retrieve_a_list_your_draft_listings()
        """
        _response = self._raw_client.retrieve_a_list_your_draft_listings(
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
            request_options=request_options,
        )
        return _response.data

    def get_a_list_of_active_negotiations_as_a_seller(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a list of active negotiations as a seller

        Parameters
        ----------
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
        client.my.get_a_list_of_active_negotiations_as_a_seller()
        """
        _response = self._raw_client.get_a_list_of_active_negotiations_as_a_seller(
            page=page, per_page=per_page, offset=offset, request_options=request_options
        )
        return _response.data

    def end_a_listing(
        self,
        slug: str,
        *,
        reason: PutMyListingsSlugStateEndRequestReason,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        End a listing

        Parameters
        ----------
        slug : str

        reason : PutMyListingsSlugStateEndRequestReason
            The reason this listing is being ended. Valid reasons: ["not_sold", "reverb_sale"].

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.my import PutMyListingsSlugStateEndRequestReason

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.my.end_a_listing(
            slug="slug",
            reason=PutMyListingsSlugStateEndRequestReason.NOT_SOLD,
        )
        """
        _response = self._raw_client.end_a_listing(slug, reason=reason, request_options=request_options)
        return _response.data

    def get_a_list_of_your_lists_wishlist_watch_list_etc(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get a list of your lists (wishlist, watch list, etc)

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
        client.my.get_a_list_of_your_lists_wishlist_watch_list_etc()
        """
        _response = self._raw_client.get_a_list_of_your_lists_wishlist_watch_list_etc(request_options=request_options)
        return _response.data

    def get_a_list_of_active_negotiations_as_a_buyer(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a list of active negotiations as a buyer

        Parameters
        ----------
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
        client.my.get_a_list_of_active_negotiations_as_a_buyer()
        """
        _response = self._raw_client.get_a_list_of_active_negotiations_as_a_buyer(
            page=page, per_page=per_page, offset=offset, request_options=request_options
        )
        return _response.data

    def get_offer_details(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get offer details

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
        client.my.get_offer_details(
            id="id",
        )
        """
        _response = self._raw_client.get_offer_details(id, request_options=request_options)
        return _response.data

    def accept_an_offer(
        self, id: str, *, message: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Accept an offer

        Parameters
        ----------
        id : str

        message : typing.Optional[str]
            Message to include with accepted offer

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
        client.my.accept_an_offer(
            id="id",
        )
        """
        _response = self._raw_client.accept_an_offer(id, message=message, request_options=request_options)
        return _response.data

    def counter_an_offer(
        self,
        id: str,
        *,
        country_code: typing.Optional[str] = OMIT,
        layaway_terms_slug: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        offer_items: typing.Optional[typing.Sequence[PostMyNegotiationsIdCounterRequestOfferItemsItem]] = OMIT,
        price: typing.Optional[PostMyNegotiationsIdCounterRequestPrice] = OMIT,
        quantity: typing.Optional[str] = OMIT,
        recipient_id: typing.Optional[str] = OMIT,
        region_code: typing.Optional[str] = OMIT,
        shipping_price: typing.Optional[PostMyNegotiationsIdCounterRequestShippingPrice] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Counter an offer

        Parameters
        ----------
        id : str

        country_code : typing.Optional[str]

        layaway_terms_slug : typing.Optional[str]

        message : typing.Optional[str]
            Message to include with counter offer

        offer_items : typing.Optional[typing.Sequence[PostMyNegotiationsIdCounterRequestOfferItemsItem]]

        price : typing.Optional[PostMyNegotiationsIdCounterRequestPrice]

        quantity : typing.Optional[str]

        recipient_id : typing.Optional[str]
            ID of the recipient of the offer. Required if you are the seller pushing an offer to a buyer.

        region_code : typing.Optional[str]

        shipping_price : typing.Optional[PostMyNegotiationsIdCounterRequestShippingPrice]
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
        client.my.counter_an_offer(
            id="id",
        )
        """
        _response = self._raw_client.counter_an_offer(
            id,
            country_code=country_code,
            layaway_terms_slug=layaway_terms_slug,
            message=message,
            offer_items=offer_items,
            price=price,
            quantity=quantity,
            recipient_id=recipient_id,
            region_code=region_code,
            shipping_price=shipping_price,
            request_options=request_options,
        )
        return _response.data

    def decline_an_offer(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Decline an offer

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
        client.my.decline_an_offer(
            id="id",
        )
        """
        _response = self._raw_client.decline_an_offer(id, request_options=request_options)
        return _response.data

    def list_of_orders_that_need_feedback(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of orders that need feedback

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
        client.my.list_of_orders_that_need_feedback()
        """
        _response = self._raw_client.list_of_orders_that_need_feedback(request_options=request_options)
        return _response.data

    def returns_all_orders_newest_first(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns all orders, newest first.

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
        client.my.returns_all_orders_newest_first()
        """
        _response = self._raw_client.returns_all_orders_newest_first(request_options=request_options)
        return _response.data

    def get_my_orders_buying_by_uuid_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        uuid_ : str

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
        client.my.get_my_orders_buying_by_uuid_uuid(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_my_orders_buying_by_uuid_uuid(uuid_, request_options=request_options)
        return _response.data

    def returns_unpaid_orders_newest_first(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns unpaid orders, newest first.

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
        client.my.returns_unpaid_orders_newest_first()
        """
        _response = self._raw_client.returns_unpaid_orders_newest_first(request_options=request_options)
        return _response.data

    def returns_order_details_for_a_buyer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns order details for a buyer

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
        client.my.returns_order_details_for_a_buyer(
            id="id",
        )
        """
        _response = self._raw_client.returns_order_details_for_a_buyer(id, request_options=request_options)
        return _response.data

    def marks_an_order_as_received_by_the_buyer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Marks an order as received by the buyer

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
        client.my.marks_an_order_as_received_by_the_buyer(
            id="id",
        )
        """
        _response = self._raw_client.marks_an_order_as_received_by_the_buyer(id, request_options=request_options)
        return _response.data

    def get_all_seller_orders_newest_first(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get all seller orders, newest first.

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
        client.my.get_all_seller_orders_newest_first()
        """
        _response = self._raw_client.get_all_seller_orders_newest_first(request_options=request_options)
        return _response.data

    def get_unpaid_seller_orders_newest_first(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get unpaid seller orders, newest first.

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
        client.my.get_unpaid_seller_orders_newest_first()
        """
        _response = self._raw_client.get_unpaid_seller_orders_newest_first(request_options=request_options)
        return _response.data

    def see_previous_orders_from_buyer(
        self, buyer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        See previous orders from buyer

        Parameters
        ----------
        buyer_id : str

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
        client.my.see_previous_orders_from_buyer(
            buyer_id="buyer_id",
        )
        """
        _response = self._raw_client.see_previous_orders_from_buyer(buyer_id, request_options=request_options)
        return _response.data

    def get_my_orders_selling_by_uuid_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        uuid_ : str

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
        client.my.get_my_orders_selling_by_uuid_uuid(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_my_orders_selling_by_uuid_uuid(uuid_, request_options=request_options)
        return _response.data

    def returns_order_details_for_a_seller(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns order details for a seller

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
        client.my.returns_order_details_for_a_seller(
            id="id",
        )
        """
        _response = self._raw_client.returns_order_details_for_a_seller(id, request_options=request_options)
        return _response.data

    def marks_an_order_as_picked_up(
        self, id: str, *, date: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Marks an order as picked up

        Parameters
        ----------
        id : str

        date : typing.Optional[str]
            Date the item was picked up.

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
        client.my.marks_an_order_as_picked_up(
            id="id",
        )
        """
        _response = self._raw_client.marks_an_order_as_picked_up(id, date=date, request_options=request_options)
        return _response.data

    def marks_an_order_as_shipped(
        self,
        id: str,
        *,
        provider: str,
        send_notification: bool,
        tracking_number: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Marks an order as shipped

        Parameters
        ----------
        id : str

        provider : str
            Shipping provider: One of UPS, USPS, FedEx, DHL Deutschland, DHLExpress, DHLGlobalMail, DHL, Canada Post, CanPar, Royal Mail, PostNL, Australia Post, EMS, La Poste - Colissimo, China Post, GLS, Parcelforce, Purolator, Interlogistica, Correos España, Ukraine Post, DPD Germany, DPD UK, DPD France, Hermes, TNT, Other

        send_notification : bool
            Should we send an email notification to the buyer

        tracking_number : str
            Tracking number provided by the shipping provider

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
        client.my.marks_an_order_as_shipped(
            id="id",
            provider="provider",
            send_notification=True,
            tracking_number="tracking_number",
        )
        """
        _response = self._raw_client.marks_an_order_as_shipped(
            id,
            provider=provider,
            send_notification=send_notification,
            tracking_number=tracking_number,
            request_options=request_options,
        )
        return _response.data

    def initiate_a_refund_for_a_sold_order(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Initiate a refund for a sold order

        Parameters
        ----------
        order_id : str

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
        client.my.initiate_a_refund_for_a_sold_order(
            order_id="order_id",
        )
        """
        _response = self._raw_client.initiate_a_refund_for_a_sold_order(order_id, request_options=request_options)
        return _response.data

    def get_payments(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        created_start_date: typing.Optional[str] = None,
        created_end_date: typing.Optional[str] = None,
        updated_start_date: typing.Optional[str] = None,
        updated_end_date: typing.Optional[str] = None,
        order_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get payments

        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

        offset : typing.Optional[int]

        created_start_date : typing.Optional[str]
            Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00

        created_end_date : typing.Optional[str]
            Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00

        updated_start_date : typing.Optional[str]
            Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00

        updated_end_date : typing.Optional[str]
            Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00

        order_id : typing.Optional[str]
            Look up payments by order id

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
        client.my.get_payments()
        """
        _response = self._raw_client.get_payments(
            page=page,
            per_page=per_page,
            offset=offset,
            created_start_date=created_start_date,
            created_end_date=created_end_date,
            updated_start_date=updated_start_date,
            updated_end_date=updated_end_date,
            order_id=order_id,
            request_options=request_options,
        )
        return _response.data

    def get_payment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get payment

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
        client.my.get_payment(
            id="id",
        )
        """
        _response = self._raw_client.get_payment(id, request_options=request_options)
        return _response.data

    def get_a_list_of_payouts(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get a list of payouts

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
        client.my.get_a_list_of_payouts()
        """
        _response = self._raw_client.get_a_list_of_payouts(request_options=request_options)
        return _response.data

    def read_the_line_items_of_a_payout(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Read the line items of a payout

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
        client.my.read_the_line_items_of_a_payout(
            id="id",
        )
        """
        _response = self._raw_client.read_the_line_items_of_a_payout(id, request_options=request_options)
        return _response.data

    def get_a_list_of_refund_requests_as_a_seller(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get a list of refund requests as a seller

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
        client.my.get_a_list_of_refund_requests_as_a_seller()
        """
        _response = self._raw_client.get_a_list_of_refund_requests_as_a_seller(request_options=request_options)
        return _response.data

    def update_a_refund_request_for_a_sold_order(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Update a refund request for a sold order

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
        client.my.update_a_refund_request_for_a_sold_order(
            id="id",
        )
        """
        _response = self._raw_client.update_a_refund_request_for_a_sold_order(id, request_options=request_options)
        return _response.data

    def get_a_list_of_your_recently_viewed_listings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get a list of your recently viewed listings.

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
        client.my.get_a_list_of_your_recently_viewed_listings()
        """
        _response = self._raw_client.get_a_list_of_your_recently_viewed_listings(request_options=request_options)
        return _response.data

    def get_a_list_of_wishlisted_items(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get a list of wishlisted items

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
        client.my.get_a_list_of_wishlisted_items()
        """
        _response = self._raw_client.get_a_list_of_wishlisted_items(request_options=request_options)
        return _response.data

    def add_a_listing_to_your_wishlist(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add a listing to your wishlist

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
        client.my.add_a_listing_to_your_wishlist(
            id="id",
        )
        """
        _response = self._raw_client.add_a_listing_to_your_wishlist(id, request_options=request_options)
        return _response.data

    def remove_a_listing_from_your_wishlist(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a listing from your wishlist

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
        client.my.remove_a_listing_from_your_wishlist(
            id="id",
        )
        """
        _response = self._raw_client.remove_a_listing_from_your_wishlist(id, request_options=request_options)
        return _response.data


class AsyncMyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMyClient
        """
        return self._raw_client

    async def get_account_details(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get account details

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
            await client.my.get_account_details()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_account_details(request_options=request_options)
        return _response.data

    async def update_account_details(
        self,
        *,
        currency: typing.Optional[str] = OMIT,
        first_name: typing.Optional[str] = OMIT,
        last_name: typing.Optional[str] = OMIT,
        locale_code: typing.Optional[str] = OMIT,
        shipping_region_code: typing.Optional[str] = OMIT,
        third_party_ad_data_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Update account details

        Parameters
        ----------
        currency : typing.Optional[str]
            The currency preference for the account

        first_name : typing.Optional[str]
            The first name of the account holder

        last_name : typing.Optional[str]
            The last name of the account holder

        locale_code : typing.Optional[str]
            The locale code for the account

        shipping_region_code : typing.Optional[str]
            The shipping region preference for the account

        third_party_ad_data_consent : typing.Optional[bool]
            The privacy setting preference for the account

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
            await client.my.update_account_details()


        asyncio.run(main())
        """
        _response = await self._raw_client.update_account_details(
            currency=currency,
            first_name=first_name,
            last_name=last_name,
            locale_code=locale_code,
            shipping_region_code=shipping_region_code,
            third_party_ad_data_consent=third_party_ad_data_consent,
            request_options=request_options,
        )
        return _response.data

    async def see_all_addresses_in_your_address_book(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        See all addresses in your address book

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
            await client.my.see_all_addresses_in_your_address_book()


        asyncio.run(main())
        """
        _response = await self._raw_client.see_all_addresses_in_your_address_book(request_options=request_options)
        return _response.data

    async def create_a_new_address_in_your_address_book(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Create a new address in your address book

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
            await client.my.create_a_new_address_in_your_address_book()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_address_in_your_address_book(request_options=request_options)
        return _response.data

    async def update_an_existing_address_in_your_address_book(
        self, address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Update an existing address in your address book

        Parameters
        ----------
        address_id : str

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
            await client.my.update_an_existing_address_in_your_address_book(
                address_id="address_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_an_existing_address_in_your_address_book(
            address_id, request_options=request_options
        )
        return _response.data

    async def delete_an_existing_address_in_your_address_book(
        self, address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an existing address in your address book

        Parameters
        ----------
        address_id : str

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
            await client.my.delete_an_existing_address_in_your_address_book(
                address_id="address_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_an_existing_address_in_your_address_book(
            address_id, request_options=request_options
        )
        return _response.data

    async def get_a_list_of_your_conversations(
        self,
        *,
        search: typing.Optional[str] = None,
        unread_only: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a list of your conversations

        Parameters
        ----------
        search : typing.Optional[str]
            Query string to search conversations by

        unread_only : typing.Optional[bool]
            Show unread conversations only

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
            await client.my.get_a_list_of_your_conversations()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_your_conversations(
            search=search,
            unread_only=unread_only,
            page=page,
            per_page=per_page,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def start_a_conversation(
        self,
        *,
        body: str,
        cloudinary_photos: typing.Optional[typing.Sequence[str]] = OMIT,
        listing_id: typing.Optional[int] = OMIT,
        recipient_id: typing.Optional[int] = OMIT,
        recipient_uuid: typing.Optional[str] = OMIT,
        shop_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Start a conversation

        Parameters
        ----------
        body : str
            The body of the message

        cloudinary_photos : typing.Optional[typing.Sequence[str]]
            An array of cloudinary data hashes (Reverb internal use only).

        listing_id : typing.Optional[int]
            The id of the listing being discussed

        recipient_id : typing.Optional[int]
            The id of the user you are trying to contact

        recipient_uuid : typing.Optional[str]
            The uuid of the user you are trying to contact

        shop_id : typing.Optional[str]
            The id of the shop you are trying to contact

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
            await client.my.start_a_conversation(
                body="body",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_a_conversation(
            body=body,
            cloudinary_photos=cloudinary_photos,
            listing_id=listing_id,
            recipient_id=recipient_id,
            recipient_uuid=recipient_uuid,
            shop_id=shop_id,
            request_options=request_options,
        )
        return _response.data

    async def send_a_message(
        self, conversation_id: str, *, body: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Send a message

        Parameters
        ----------
        conversation_id : str

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
            await client.my.send_a_message(
                conversation_id="conversation_id",
                body="body",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_a_message(conversation_id, body=body, request_options=request_options)
        return _response.data

    async def display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Display conversation details with messages in natural time order (oldest to newest)

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
            await client.my.display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest(
                id="id",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest(
                id, request_options=request_options
            )
        )
        return _response.data

    async def mark_a_conversation_read_unread(
        self, id: str, *, read: typing.Optional[bool] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Mark a conversation read/unread

        Parameters
        ----------
        id : str

        read : typing.Optional[bool]
            Should the conversation be marked as read

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
            await client.my.mark_a_conversation_read_unread(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mark_a_conversation_read_unread(
            id, read=read, request_options=request_options
        )
        return _response.data

    async def get_your_actionable_status_counts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get your actionable status counts

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
            await client.my.get_your_actionable_status_counts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_your_actionable_status_counts(request_options=request_options)
        return _response.data

    async def post_my_curated_set_product_product_id(
        self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        product_id : str

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
            await client.my.post_my_curated_set_product_product_id(
                product_id="product_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_my_curated_set_product_product_id(
            product_id, request_options=request_options
        )
        return _response.data

    async def delete_my_curated_set_product_product_id(
        self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        product_id : str

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
            await client.my.delete_my_curated_set_product_product_id(
                product_id="product_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_my_curated_set_product_product_id(
            product_id, request_options=request_options
        )
        return _response.data

    async def get_listings_from_your_feed(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get listings from your feed

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
            await client.my.get_listings_from_your_feed()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_listings_from_your_feed(request_options=request_options)
        return _response.data

    async def get_your_feed_customization_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        get your feed customization options

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
            await client.my.get_your_feed_customization_options()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_your_feed_customization_options(request_options=request_options)
        return _response.data

    async def get_your_feed(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        get your feed

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
            await client.my.get_your_feed()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_your_feed(request_options=request_options)
        return _response.data

    async def list_of_received_feedback(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of received feedback

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
            await client.my.list_of_received_feedback()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_received_feedback(request_options=request_options)
        return _response.data

    async def list_of_sent_feedback(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        List of sent feedback

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
            await client.my.list_of_sent_feedback()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_sent_feedback(request_options=request_options)
        return _response.data

    async def see_what_the_user_is_following(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        See what the user is following

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
            await client.my.see_what_the_user_is_following()


        asyncio.run(main())
        """
        _response = await self._raw_client.see_what_the_user_is_following(request_options=request_options)
        return _response.data

    async def returns_a_users_article_category_follows(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns a user's ArticleCategoryFollows

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
            await client.my.returns_a_users_article_category_follows()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_users_article_category_follows(request_options=request_options)
        return _response.data

    async def set_a_users_article_category_follows(
        self, *, category_uuids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Set a user's ArticleCategoryFollows

        Parameters
        ----------
        category_uuids : str

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
            await client.my.set_a_users_article_category_follows(
                category_uuids="category_uuids",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_a_users_article_category_follows(
            category_uuids=category_uuids, request_options=request_options
        )
        return _response.data

    async def follow_status_for_a_brand(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a brand

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
            await client.my.follow_status_for_a_brand(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_status_for_a_brand(slug, request_options=request_options)
        return _response.data

    async def follow_a_brand(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow a brand

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
            await client.my.follow_a_brand(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_a_brand(slug, request_options=request_options)
        return _response.data

    async def unfollow_a_brand(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Unfollow a brand

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
            await client.my.unfollow_a_brand(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unfollow_a_brand(slug, request_options=request_options)
        return _response.data

    async def follow_status_for_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a subcategory

        Parameters
        ----------
        category : str

        subcategory : str

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
            await client.my.follow_status_for_a_subcategory(
                category="category",
                subcategory="subcategory",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_status_for_a_subcategory(
            category, subcategory, request_options=request_options
        )
        return _response.data

    async def follow_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow a subcategory

        Parameters
        ----------
        category : str

        subcategory : str

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
            await client.my.follow_a_subcategory(
                category="category",
                subcategory="subcategory",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_a_subcategory(category, subcategory, request_options=request_options)
        return _response.data

    async def unfollow_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unfollow a subcategory

        Parameters
        ----------
        category : str

        subcategory : str

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
            await client.my.unfollow_a_subcategory(
                category="category",
                subcategory="subcategory",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unfollow_a_subcategory(
            category, subcategory, request_options=request_options
        )
        return _response.data

    async def follow_status_for_a_category(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a category

        Parameters
        ----------
        identifier : str

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
            await client.my.follow_status_for_a_category(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_status_for_a_category(identifier, request_options=request_options)
        return _response.data

    async def follow_a_category(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow a category

        Parameters
        ----------
        uuid_ : str

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
            await client.my.follow_a_category(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_a_category(uuid_, request_options=request_options)
        return _response.data

    async def unfollow_a_category(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unfollow a category

        Parameters
        ----------
        identifier : str

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
            await client.my.unfollow_a_category(
                identifier="identifier",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unfollow_a_category(identifier, request_options=request_options)
        return _response.data

    async def follow_status_for_a_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a collection

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
            await client.my.follow_status_for_a_collection(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_status_for_a_collection(slug, request_options=request_options)
        return _response.data

    async def follow_a_collection(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow a collection

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
            await client.my.follow_a_collection(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_a_collection(slug, request_options=request_options)
        return _response.data

    async def unfollow_a_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unfollow a collection

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
            await client.my.unfollow_a_collection(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unfollow_a_collection(slug, request_options=request_options)
        return _response.data

    async def follow_status_for_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a handpicked collection

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
            await client.my.follow_status_for_a_handpicked_collection(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_status_for_a_handpicked_collection(
            slug, request_options=request_options
        )
        return _response.data

    async def follow_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow a handpicked collection

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
            await client.my.follow_a_handpicked_collection(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_a_handpicked_collection(slug, request_options=request_options)
        return _response.data

    async def unfollow_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Unfollow a handpicked collection

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
            await client.my.unfollow_a_handpicked_collection(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unfollow_a_handpicked_collection(slug, request_options=request_options)
        return _response.data

    async def follow_status_for_a_search(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow status for a search

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
            await client.my.follow_status_for_a_search()


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_status_for_a_search(request_options=request_options)
        return _response.data

    async def follow_a_search(
        self,
        *,
        accepts_gift_cards: typing.Optional[bool] = OMIT,
        accepts_payment_plans: typing.Optional[bool] = OMIT,
        auction_price_max: typing.Optional[float] = OMIT,
        category: typing.Optional[str] = OMIT,
        conditions: typing.Optional[typing.Sequence[str]] = OMIT,
        currency: typing.Optional[PostMyFollowsSearchRequestCurrency] = OMIT,
        decade: typing.Optional[str] = OMIT,
        exclude_auctions: typing.Optional[bool] = OMIT,
        finish: typing.Optional[str] = OMIT,
        handmade: typing.Optional[bool] = OMIT,
        item_city: typing.Optional[str] = OMIT,
        item_country: typing.Optional[str] = OMIT,
        item_region: typing.Optional[str] = OMIT,
        item_state: typing.Optional[str] = OMIT,
        listing_type: typing.Optional[PostMyFollowsSearchRequestListingType] = OMIT,
        local_pickup: typing.Optional[bool] = OMIT,
        make: typing.Optional[typing.Sequence[str]] = OMIT,
        model: typing.Optional[str] = OMIT,
        must_not: typing.Optional[str] = OMIT,
        not_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        preferred_seller: typing.Optional[bool] = OMIT,
        price_max: typing.Optional[float] = OMIT,
        price_min: typing.Optional[float] = OMIT,
        product_type: typing.Optional[str] = OMIT,
        query: typing.Optional[str] = OMIT,
        ships_to: typing.Optional[str] = OMIT,
        shop: typing.Optional[str] = OMIT,
        shop_id: typing.Optional[str] = OMIT,
        watchers_count_min: typing.Optional[int] = OMIT,
        year_max: typing.Optional[int] = OMIT,
        year_min: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Follow a search

        Parameters
        ----------
        accepts_gift_cards : typing.Optional[bool]
            If true, include only items that accept gift cards

        accepts_payment_plans : typing.Optional[bool]
            If true, only show items that can be purchased with a payment plan

        auction_price_max : typing.Optional[float]
            Maximum current auction price

        category : typing.Optional[str]
            Category slug from /api/categories

        conditions : typing.Optional[typing.Sequence[str]]
            Condition: all,new,b-stock,used,non-functioning,all-but-new,poor,fair,good,very-good,excellent,mint

        currency : typing.Optional[PostMyFollowsSearchRequestCurrency]
            The currency to be used for the price filters

        decade : typing.Optional[str]
            Decade: e.g. 1970s, early 70s

        exclude_auctions : typing.Optional[bool]
            If true, exclude auctions

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

        listing_type : typing.Optional[PostMyFollowsSearchRequestListingType]
            Type of listing: auctions,offers

        local_pickup : typing.Optional[bool]
            Only items that offer local pickup

        make : typing.Optional[typing.Sequence[str]]
            Make(s)/brand of item (e.g. Fender). Can take a single value or an array.

        model : typing.Optional[str]
            Model of item (e.g. Stratocaster)

        must_not : typing.Optional[str]
            Search term negation. If you want to exclude a term, add it here

        not_ids : typing.Optional[typing.Sequence[int]]
            Listing ID negation. If you want to exclude a listing, add it here.

        preferred_seller : typing.Optional[bool]
            If true, include only items by Reverb Preferred Sellers

        price_max : typing.Optional[float]
            Maximum price of search results (USD)

        price_min : typing.Optional[float]
            Minimum price of search results (USD)

        product_type : typing.Optional[str]
            Product type slug from /api/categories

        query : typing.Optional[str]
            Search query.

        ships_to : typing.Optional[str]
            Limit search to items that ship to this country code

        shop : typing.Optional[str]
            Slug of shop to search

        shop_id : typing.Optional[str]
            ID of shop to search

        watchers_count_min : typing.Optional[int]
            Minimum number of watchers (used to find popular items)

        year_max : typing.Optional[int]
            Maximum year of manufacture

        year_min : typing.Optional[int]
            Minumum year of manufacture

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
            await client.my.follow_a_search()


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_a_search(
            accepts_gift_cards=accepts_gift_cards,
            accepts_payment_plans=accepts_payment_plans,
            auction_price_max=auction_price_max,
            category=category,
            conditions=conditions,
            currency=currency,
            decade=decade,
            exclude_auctions=exclude_auctions,
            finish=finish,
            handmade=handmade,
            item_city=item_city,
            item_country=item_country,
            item_region=item_region,
            item_state=item_state,
            listing_type=listing_type,
            local_pickup=local_pickup,
            make=make,
            model=model,
            must_not=must_not,
            not_ids=not_ids,
            preferred_seller=preferred_seller,
            price_max=price_max,
            price_min=price_min,
            product_type=product_type,
            query=query,
            ships_to=ships_to,
            shop=shop,
            shop_id=shop_id,
            watchers_count_min=watchers_count_min,
            year_max=year_max,
            year_min=year_min,
            request_options=request_options,
        )
        return _response.data

    async def follow_status_for_a_shop(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Follow status for a shop

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
            await client.my.follow_status_for_a_shop(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_status_for_a_shop(slug, request_options=request_options)
        return _response.data

    async def follow_a_shop(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Follow a shop

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
            await client.my.follow_a_shop(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.follow_a_shop(slug, request_options=request_options)
        return _response.data

    async def unfollow_a_shop(self, slug: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Unfollow a shop

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
            await client.my.unfollow_a_shop(
                slug="slug",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unfollow_a_shop(slug, request_options=request_options)
        return _response.data

    async def delete_a_follow(self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a follow

        Parameters
        ----------
        follow_id : str

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
            await client.my.delete_a_follow(
                follow_id="follow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_follow(follow_id, request_options=request_options)
        return _response.data

    async def post_my_follows_follow_id_alert(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        follow_id : str

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
            await client.my.post_my_follows_follow_id_alert(
                follow_id="follow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_my_follows_follow_id_alert(follow_id, request_options=request_options)
        return _response.data

    async def delete_my_follows_follow_id_alert(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        follow_id : str

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
            await client.my.delete_my_follows_follow_id_alert(
                follow_id="follow_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_my_follows_follow_id_alert(follow_id, request_options=request_options)
        return _response.data

    async def retrieve_a_list_of_live_listings_for_the_seller_to_search_all_listings_specify_state_all(
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
        state: typing.Optional[str] = None,
        sku: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieve a list of live listings for the seller. To search all listings specify state=all

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

        state : typing.Optional[str]
            Available: ["all", "draft", "ended", "live", "ordered", "sold_out", "suspended", "seller_unavailable"]. Defaults to 'live'

        sku : typing.Optional[str]
            Find a listing by sku

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
            await client.my.retrieve_a_list_of_live_listings_for_the_seller_to_search_all_listings_specify_state_all()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_list_of_live_listings_for_the_seller_to_search_all_listings_specify_state_all(
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
            state=state,
            sku=sku,
            request_options=request_options,
        )
        return _response.data

    async def retrieve_a_list_your_draft_listings(
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
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Retrieve a list your draft listings

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
            await client.my.retrieve_a_list_your_draft_listings()


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieve_a_list_your_draft_listings(
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
            request_options=request_options,
        )
        return _response.data

    async def get_a_list_of_active_negotiations_as_a_seller(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a list of active negotiations as a seller

        Parameters
        ----------
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
            await client.my.get_a_list_of_active_negotiations_as_a_seller()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_active_negotiations_as_a_seller(
            page=page, per_page=per_page, offset=offset, request_options=request_options
        )
        return _response.data

    async def end_a_listing(
        self,
        slug: str,
        *,
        reason: PutMyListingsSlugStateEndRequestReason,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        End a listing

        Parameters
        ----------
        slug : str

        reason : PutMyListingsSlugStateEndRequestReason
            The reason this listing is being ended. Valid reasons: ["not_sold", "reverb_sale"].

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.my import PutMyListingsSlugStateEndRequestReason

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.my.end_a_listing(
                slug="slug",
                reason=PutMyListingsSlugStateEndRequestReason.NOT_SOLD,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.end_a_listing(slug, reason=reason, request_options=request_options)
        return _response.data

    async def get_a_list_of_your_lists_wishlist_watch_list_etc(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get a list of your lists (wishlist, watch list, etc)

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
            await client.my.get_a_list_of_your_lists_wishlist_watch_list_etc()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_your_lists_wishlist_watch_list_etc(
            request_options=request_options
        )
        return _response.data

    async def get_a_list_of_active_negotiations_as_a_buyer(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get a list of active negotiations as a buyer

        Parameters
        ----------
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
            await client.my.get_a_list_of_active_negotiations_as_a_buyer()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_active_negotiations_as_a_buyer(
            page=page, per_page=per_page, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_offer_details(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get offer details

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
            await client.my.get_offer_details(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_offer_details(id, request_options=request_options)
        return _response.data

    async def accept_an_offer(
        self, id: str, *, message: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Accept an offer

        Parameters
        ----------
        id : str

        message : typing.Optional[str]
            Message to include with accepted offer

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
            await client.my.accept_an_offer(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.accept_an_offer(id, message=message, request_options=request_options)
        return _response.data

    async def counter_an_offer(
        self,
        id: str,
        *,
        country_code: typing.Optional[str] = OMIT,
        layaway_terms_slug: typing.Optional[str] = OMIT,
        message: typing.Optional[str] = OMIT,
        offer_items: typing.Optional[typing.Sequence[PostMyNegotiationsIdCounterRequestOfferItemsItem]] = OMIT,
        price: typing.Optional[PostMyNegotiationsIdCounterRequestPrice] = OMIT,
        quantity: typing.Optional[str] = OMIT,
        recipient_id: typing.Optional[str] = OMIT,
        region_code: typing.Optional[str] = OMIT,
        shipping_price: typing.Optional[PostMyNegotiationsIdCounterRequestShippingPrice] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Counter an offer

        Parameters
        ----------
        id : str

        country_code : typing.Optional[str]

        layaway_terms_slug : typing.Optional[str]

        message : typing.Optional[str]
            Message to include with counter offer

        offer_items : typing.Optional[typing.Sequence[PostMyNegotiationsIdCounterRequestOfferItemsItem]]

        price : typing.Optional[PostMyNegotiationsIdCounterRequestPrice]

        quantity : typing.Optional[str]

        recipient_id : typing.Optional[str]
            ID of the recipient of the offer. Required if you are the seller pushing an offer to a buyer.

        region_code : typing.Optional[str]

        shipping_price : typing.Optional[PostMyNegotiationsIdCounterRequestShippingPrice]
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
            await client.my.counter_an_offer(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.counter_an_offer(
            id,
            country_code=country_code,
            layaway_terms_slug=layaway_terms_slug,
            message=message,
            offer_items=offer_items,
            price=price,
            quantity=quantity,
            recipient_id=recipient_id,
            region_code=region_code,
            shipping_price=shipping_price,
            request_options=request_options,
        )
        return _response.data

    async def decline_an_offer(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Decline an offer

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
            await client.my.decline_an_offer(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.decline_an_offer(id, request_options=request_options)
        return _response.data

    async def list_of_orders_that_need_feedback(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        List of orders that need feedback

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
            await client.my.list_of_orders_that_need_feedback()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_of_orders_that_need_feedback(request_options=request_options)
        return _response.data

    async def returns_all_orders_newest_first(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Returns all orders, newest first.

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
            await client.my.returns_all_orders_newest_first()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_orders_newest_first(request_options=request_options)
        return _response.data

    async def get_my_orders_buying_by_uuid_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        uuid_ : str

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
            await client.my.get_my_orders_buying_by_uuid_uuid(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_orders_buying_by_uuid_uuid(uuid_, request_options=request_options)
        return _response.data

    async def returns_unpaid_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns unpaid orders, newest first.

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
            await client.my.returns_unpaid_orders_newest_first()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_unpaid_orders_newest_first(request_options=request_options)
        return _response.data

    async def returns_order_details_for_a_buyer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns order details for a buyer

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
            await client.my.returns_order_details_for_a_buyer(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_order_details_for_a_buyer(id, request_options=request_options)
        return _response.data

    async def marks_an_order_as_received_by_the_buyer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Marks an order as received by the buyer

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
            await client.my.marks_an_order_as_received_by_the_buyer(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.marks_an_order_as_received_by_the_buyer(id, request_options=request_options)
        return _response.data

    async def get_all_seller_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get all seller orders, newest first.

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
            await client.my.get_all_seller_orders_newest_first()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_seller_orders_newest_first(request_options=request_options)
        return _response.data

    async def get_unpaid_seller_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get unpaid seller orders, newest first.

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
            await client.my.get_unpaid_seller_orders_newest_first()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_unpaid_seller_orders_newest_first(request_options=request_options)
        return _response.data

    async def see_previous_orders_from_buyer(
        self, buyer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        See previous orders from buyer

        Parameters
        ----------
        buyer_id : str

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
            await client.my.see_previous_orders_from_buyer(
                buyer_id="buyer_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.see_previous_orders_from_buyer(buyer_id, request_options=request_options)
        return _response.data

    async def get_my_orders_selling_by_uuid_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        uuid_ : str

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
            await client.my.get_my_orders_selling_by_uuid_uuid(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_my_orders_selling_by_uuid_uuid(uuid_, request_options=request_options)
        return _response.data

    async def returns_order_details_for_a_seller(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Returns order details for a seller

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
            await client.my.returns_order_details_for_a_seller(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_order_details_for_a_seller(id, request_options=request_options)
        return _response.data

    async def marks_an_order_as_picked_up(
        self, id: str, *, date: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Marks an order as picked up

        Parameters
        ----------
        id : str

        date : typing.Optional[str]
            Date the item was picked up.

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
            await client.my.marks_an_order_as_picked_up(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.marks_an_order_as_picked_up(id, date=date, request_options=request_options)
        return _response.data

    async def marks_an_order_as_shipped(
        self,
        id: str,
        *,
        provider: str,
        send_notification: bool,
        tracking_number: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Marks an order as shipped

        Parameters
        ----------
        id : str

        provider : str
            Shipping provider: One of UPS, USPS, FedEx, DHL Deutschland, DHLExpress, DHLGlobalMail, DHL, Canada Post, CanPar, Royal Mail, PostNL, Australia Post, EMS, La Poste - Colissimo, China Post, GLS, Parcelforce, Purolator, Interlogistica, Correos España, Ukraine Post, DPD Germany, DPD UK, DPD France, Hermes, TNT, Other

        send_notification : bool
            Should we send an email notification to the buyer

        tracking_number : str
            Tracking number provided by the shipping provider

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
            await client.my.marks_an_order_as_shipped(
                id="id",
                provider="provider",
                send_notification=True,
                tracking_number="tracking_number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.marks_an_order_as_shipped(
            id,
            provider=provider,
            send_notification=send_notification,
            tracking_number=tracking_number,
            request_options=request_options,
        )
        return _response.data

    async def initiate_a_refund_for_a_sold_order(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Initiate a refund for a sold order

        Parameters
        ----------
        order_id : str

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
            await client.my.initiate_a_refund_for_a_sold_order(
                order_id="order_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.initiate_a_refund_for_a_sold_order(order_id, request_options=request_options)
        return _response.data

    async def get_payments(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        created_start_date: typing.Optional[str] = None,
        created_end_date: typing.Optional[str] = None,
        updated_start_date: typing.Optional[str] = None,
        updated_end_date: typing.Optional[str] = None,
        order_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Get payments

        Parameters
        ----------
        page : typing.Optional[int]

        per_page : typing.Optional[int]

        offset : typing.Optional[int]

        created_start_date : typing.Optional[str]
            Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00

        created_end_date : typing.Optional[str]
            Filter by date created in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00

        updated_start_date : typing.Optional[str]
            Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00

        updated_end_date : typing.Optional[str]
            Filter by date modified in ISO8601 format - e.g: 2015-04-09T10:52:23-00:00

        order_id : typing.Optional[str]
            Look up payments by order id

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
            await client.my.get_payments()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payments(
            page=page,
            per_page=per_page,
            offset=offset,
            created_start_date=created_start_date,
            created_end_date=created_end_date,
            updated_start_date=updated_start_date,
            updated_end_date=updated_end_date,
            order_id=order_id,
            request_options=request_options,
        )
        return _response.data

    async def get_payment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get payment

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
            await client.my.get_payment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_payment(id, request_options=request_options)
        return _response.data

    async def get_a_list_of_payouts(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get a list of payouts

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
            await client.my.get_a_list_of_payouts()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_payouts(request_options=request_options)
        return _response.data

    async def read_the_line_items_of_a_payout(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Read the line items of a payout

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
            await client.my.read_the_line_items_of_a_payout(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_the_line_items_of_a_payout(id, request_options=request_options)
        return _response.data

    async def get_a_list_of_refund_requests_as_a_seller(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get a list of refund requests as a seller

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
            await client.my.get_a_list_of_refund_requests_as_a_seller()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_refund_requests_as_a_seller(request_options=request_options)
        return _response.data

    async def update_a_refund_request_for_a_sold_order(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Update a refund request for a sold order

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
            await client.my.update_a_refund_request_for_a_sold_order(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_a_refund_request_for_a_sold_order(id, request_options=request_options)
        return _response.data

    async def get_a_list_of_your_recently_viewed_listings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Get a list of your recently viewed listings.

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
            await client.my.get_a_list_of_your_recently_viewed_listings()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_your_recently_viewed_listings(request_options=request_options)
        return _response.data

    async def get_a_list_of_wishlisted_items(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Get a list of wishlisted items

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
            await client.my.get_a_list_of_wishlisted_items()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_list_of_wishlisted_items(request_options=request_options)
        return _response.data

    async def add_a_listing_to_your_wishlist(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Add a listing to your wishlist

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
            await client.my.add_a_listing_to_your_wishlist(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_a_listing_to_your_wishlist(id, request_options=request_options)
        return _response.data

    async def remove_a_listing_from_your_wishlist(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove a listing from your wishlist

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
            await client.my.remove_a_listing_from_your_wishlist(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_a_listing_from_your_wishlist(id, request_options=request_options)
        return _response.data
