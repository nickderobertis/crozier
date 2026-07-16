

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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


class RawMyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_account_details(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Get account details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/account",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/account",
            method="PUT",
            json={
                "currency": currency,
                "first_name": first_name,
                "last_name": last_name,
                "locale_code": locale_code,
                "shipping_region_code": shipping_region_code,
                "third_party_ad_data_consent": third_party_ad_data_consent,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def see_all_addresses_in_your_address_book(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        See all addresses in your address book

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/addresses",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_a_new_address_in_your_address_book(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Create a new address in your address book

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/addresses",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_an_existing_address_in_your_address_book(
        self, address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Update an existing address in your address book

        Parameters
        ----------
        address_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/addresses/{jsonable_encoder(address_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_an_existing_address_in_your_address_book(
        self, address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete an existing address in your address book

        Parameters
        ----------
        address_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/addresses/{jsonable_encoder(address_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_list_of_your_conversations(
        self,
        *,
        search: typing.Optional[str] = None,
        unread_only: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/conversations",
            method="GET",
            params={
                "search": search,
                "unread_only": unread_only,
                "page": page,
                "per_page": per_page,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/conversations",
            method="POST",
            json={
                "body": body,
                "cloudinary_photos": cloudinary_photos,
                "listing_id": listing_id,
                "recipient_id": recipient_id,
                "recipient_uuid": recipient_uuid,
                "shop_id": shop_id,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def send_a_message(
        self, conversation_id: str, *, body: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/conversations/{jsonable_encoder(conversation_id)}/messages",
            method="POST",
            json={
                "body": body,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Display conversation details with messages in natural time order (oldest to newest)

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/conversations/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mark_a_conversation_read_unread(
        self, id: str, *, read: typing.Optional[bool] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/conversations/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "read": read,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_your_actionable_status_counts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get your actionable status counts

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/counts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_my_curated_set_product_product_id(
        self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        product_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/curated_set/product/{jsonable_encoder(product_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_my_curated_set_product_product_id(
        self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        product_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/curated_set/product/{jsonable_encoder(product_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_listings_from_your_feed(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get listings from your feed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/feed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_your_feed_customization_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        get your feed customization options

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/feed/customize",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_your_feed(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        get your feed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/feed/grid",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_of_received_feedback(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        List of received feedback

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/feedback/received",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_of_sent_feedback(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        List of sent feedback

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/feedback/sent",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def see_what_the_user_is_following(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        See what the user is following

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/follows",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def returns_a_users_article_category_follows(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Returns a user's ArticleCategoryFollows

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/follows/articles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def set_a_users_article_category_follows(
        self, *, category_uuids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Set a user's ArticleCategoryFollows

        Parameters
        ----------
        category_uuids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/follows/articles",
            method="POST",
            json={
                "category_uuids": category_uuids,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_status_for_a_brand(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow status for a brand

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/brands/{jsonable_encoder(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_a_brand(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow a brand

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/brands/{jsonable_encoder(slug)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unfollow_a_brand(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Unfollow a brand

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/brands/{jsonable_encoder(slug)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_status_for_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(category)}/{jsonable_encoder(subcategory)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(category)}/{jsonable_encoder(subcategory)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unfollow_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(category)}/{jsonable_encoder(subcategory)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_status_for_a_category(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow status for a category

        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_a_category(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow a category

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(uuid_)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unfollow_a_category(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Unfollow a category

        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_status_for_a_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow status for a collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/collections/{jsonable_encoder(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_a_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow a collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/collections/{jsonable_encoder(slug)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unfollow_a_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Unfollow a collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/collections/{jsonable_encoder(slug)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_status_for_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow status for a handpicked collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/handpicked/{jsonable_encoder(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow a handpicked collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/handpicked/{jsonable_encoder(slug)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unfollow_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Unfollow a handpicked collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/handpicked/{jsonable_encoder(slug)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_status_for_a_search(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow status for a search

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/follows/search",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/follows/search",
            method="POST",
            json={
                "accepts_gift_cards": accepts_gift_cards,
                "accepts_payment_plans": accepts_payment_plans,
                "auction_price_max": auction_price_max,
                "category": category,
                "conditions": conditions,
                "currency": currency,
                "decade": decade,
                "exclude_auctions": exclude_auctions,
                "finish": finish,
                "handmade": handmade,
                "item_city": item_city,
                "item_country": item_country,
                "item_region": item_region,
                "item_state": item_state,
                "listing_type": listing_type,
                "local_pickup": local_pickup,
                "make": make,
                "model": model,
                "must_not": must_not,
                "not_ids": not_ids,
                "preferred_seller": preferred_seller,
                "price_max": price_max,
                "price_min": price_min,
                "product_type": product_type,
                "query": query,
                "ships_to": ships_to,
                "shop": shop,
                "shop_id": shop_id,
                "watchers_count_min": watchers_count_min,
                "year_max": year_max,
                "year_min": year_min,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_status_for_a_shop(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow status for a shop

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/shops/{jsonable_encoder(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def follow_a_shop(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Follow a shop

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/shops/{jsonable_encoder(slug)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def unfollow_a_shop(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Unfollow a shop

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/shops/{jsonable_encoder(slug)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_a_follow(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a follow

        Parameters
        ----------
        follow_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/{jsonable_encoder(follow_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def post_my_follows_follow_id_alert(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        follow_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/{jsonable_encoder(follow_id)}/alert",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_my_follows_follow_id_alert(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        follow_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/follows/{jsonable_encoder(follow_id)}/alert",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/listings",
            method="GET",
            params={
                "query": query,
                "auction_price_max": auction_price_max,
                "category": category,
                "product_type": product_type,
                "conditions": conditions,
                "decade": decade,
                "finish": finish,
                "handmade": handmade,
                "item_city": item_city,
                "item_country": item_country,
                "item_region": item_region,
                "item_state": item_state,
                "make": make,
                "model": model,
                "must_not": must_not,
                "price_max": price_max,
                "price_min": price_min,
                "currency": currency,
                "year_max": year_max,
                "year_min": year_min,
                "accepts_gift_cards": accepts_gift_cards,
                "preferred_seller": preferred_seller,
                "shop": shop,
                "shop_id": shop_id,
                "listing_type": listing_type,
                "ships_to": ships_to,
                "exclude_auctions": exclude_auctions,
                "accepts_payment_plans": accepts_payment_plans,
                "watchers_count_min": watchers_count_min,
                "not_ids": not_ids,
                "local_pickup": local_pickup,
                "state": state,
                "sku": sku,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/listings/drafts",
            method="GET",
            params={
                "query": query,
                "auction_price_max": auction_price_max,
                "category": category,
                "product_type": product_type,
                "conditions": conditions,
                "decade": decade,
                "finish": finish,
                "handmade": handmade,
                "item_city": item_city,
                "item_country": item_country,
                "item_region": item_region,
                "item_state": item_state,
                "make": make,
                "model": model,
                "must_not": must_not,
                "price_max": price_max,
                "price_min": price_min,
                "currency": currency,
                "year_max": year_max,
                "year_min": year_min,
                "accepts_gift_cards": accepts_gift_cards,
                "preferred_seller": preferred_seller,
                "shop": shop,
                "shop_id": shop_id,
                "listing_type": listing_type,
                "ships_to": ships_to,
                "exclude_auctions": exclude_auctions,
                "accepts_payment_plans": accepts_payment_plans,
                "watchers_count_min": watchers_count_min,
                "not_ids": not_ids,
                "local_pickup": local_pickup,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_list_of_active_negotiations_as_a_seller(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/listings/negotiations",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def end_a_listing(
        self,
        slug: str,
        *,
        reason: PutMyListingsSlugStateEndRequestReason,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/listings/{jsonable_encoder(slug)}/state/end",
            method="PUT",
            json={
                "reason": reason,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_list_of_your_lists_wishlist_watch_list_etc(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get a list of your lists (wishlist, watch list, etc)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/lists",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_list_of_active_negotiations_as_a_buyer(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/negotiations/buying",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_offer_details(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get offer details

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/negotiations/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def accept_an_offer(
        self, id: str, *, message: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/negotiations/{jsonable_encoder(id)}/accept",
            method="POST",
            json={
                "message": message,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/negotiations/{jsonable_encoder(id)}/counter",
            method="POST",
            json={
                "country_code": country_code,
                "layaway_terms_slug": layaway_terms_slug,
                "message": message,
                "offer_items": convert_and_respect_annotation_metadata(
                    object_=offer_items,
                    annotation=typing.Sequence[PostMyNegotiationsIdCounterRequestOfferItemsItem],
                    direction="write",
                ),
                "price": convert_and_respect_annotation_metadata(
                    object_=price, annotation=PostMyNegotiationsIdCounterRequestPrice, direction="write"
                ),
                "quantity": quantity,
                "recipient_id": recipient_id,
                "region_code": region_code,
                "shipping_price": convert_and_respect_annotation_metadata(
                    object_=shipping_price,
                    annotation=PostMyNegotiationsIdCounterRequestShippingPrice,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def decline_an_offer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Decline an offer

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/negotiations/{jsonable_encoder(id)}/decline",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_of_orders_that_need_feedback(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        List of orders that need feedback

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/orders/awaiting_feedback",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def returns_all_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Returns all orders, newest first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/orders/buying/all",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_my_orders_buying_by_uuid_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/orders/buying/by_uuid/{jsonable_encoder(uuid_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def returns_unpaid_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Returns unpaid orders, newest first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/orders/buying/unpaid",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def returns_order_details_for_a_buyer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Returns order details for a buyer

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/orders/buying/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def marks_an_order_as_received_by_the_buyer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Marks an order as received by the buyer

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/orders/buying/{jsonable_encoder(id)}/mark_received",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_all_seller_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get all seller orders, newest first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/orders/selling/all",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_unpaid_seller_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get unpaid seller orders, newest first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/orders/selling/unpaid",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def see_previous_orders_from_buyer(
        self, buyer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        See previous orders from buyer

        Parameters
        ----------
        buyer_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/orders/selling/buyer_history/{jsonable_encoder(buyer_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_my_orders_selling_by_uuid_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/orders/selling/by_uuid/{jsonable_encoder(uuid_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def returns_order_details_for_a_seller(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Returns order details for a seller

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/orders/selling/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def marks_an_order_as_picked_up(
        self, id: str, *, date: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/orders/selling/{jsonable_encoder(id)}/mark_picked_up",
            method="POST",
            json={
                "date": date,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def marks_an_order_as_shipped(
        self,
        id: str,
        *,
        provider: str,
        send_notification: bool,
        tracking_number: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/orders/selling/{jsonable_encoder(id)}/ship",
            method="POST",
            json={
                "provider": provider,
                "send_notification": send_notification,
                "tracking_number": tracking_number,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def initiate_a_refund_for_a_sold_order(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Initiate a refund for a sold order

        Parameters
        ----------
        order_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/orders/selling/{jsonable_encoder(order_id)}/refund_requests",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/payments/selling",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "offset": offset,
                "created_start_date": created_start_date,
                "created_end_date": created_end_date,
                "updated_start_date": updated_start_date,
                "updated_end_date": updated_end_date,
                "order_id": order_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_payment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Get payment

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/payments/selling/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_list_of_payouts(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Get a list of payouts

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/payouts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def read_the_line_items_of_a_payout(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Read the line items of a payout

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/payouts/{jsonable_encoder(id)}/line_items",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_list_of_refund_requests_as_a_seller(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get a list of refund requests as a seller

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/refund_requests/selling",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_a_refund_request_for_a_sold_order(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Update a refund request for a sold order

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/refund_requests/selling/{jsonable_encoder(id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_list_of_your_recently_viewed_listings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get a list of your recently viewed listings.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/viewed_listings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_list_of_wishlisted_items(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Get a list of wishlisted items

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "my/wishlist",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def add_a_listing_to_your_wishlist(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Add a listing to your wishlist

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/wishlist/{jsonable_encoder(id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def remove_a_listing_from_your_wishlist(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Remove a listing from your wishlist

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"my/wishlist/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawMyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_account_details(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get account details

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/account",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/account",
            method="PUT",
            json={
                "currency": currency,
                "first_name": first_name,
                "last_name": last_name,
                "locale_code": locale_code,
                "shipping_region_code": shipping_region_code,
                "third_party_ad_data_consent": third_party_ad_data_consent,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def see_all_addresses_in_your_address_book(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        See all addresses in your address book

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/addresses",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_a_new_address_in_your_address_book(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Create a new address in your address book

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/addresses",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_an_existing_address_in_your_address_book(
        self, address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Update an existing address in your address book

        Parameters
        ----------
        address_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/addresses/{jsonable_encoder(address_id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_an_existing_address_in_your_address_book(
        self, address_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete an existing address in your address book

        Parameters
        ----------
        address_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/addresses/{jsonable_encoder(address_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_list_of_your_conversations(
        self,
        *,
        search: typing.Optional[str] = None,
        unread_only: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/conversations",
            method="GET",
            params={
                "search": search,
                "unread_only": unread_only,
                "page": page,
                "per_page": per_page,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/conversations",
            method="POST",
            json={
                "body": body,
                "cloudinary_photos": cloudinary_photos,
                "listing_id": listing_id,
                "recipient_id": recipient_id,
                "recipient_uuid": recipient_uuid,
                "shop_id": shop_id,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def send_a_message(
        self, conversation_id: str, *, body: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/conversations/{jsonable_encoder(conversation_id)}/messages",
            method="POST",
            json={
                "body": body,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def display_conversation_details_with_messages_in_natural_time_order_oldest_to_newest(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Display conversation details with messages in natural time order (oldest to newest)

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/conversations/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mark_a_conversation_read_unread(
        self, id: str, *, read: typing.Optional[bool] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/conversations/{jsonable_encoder(id)}",
            method="PUT",
            json={
                "read": read,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_your_actionable_status_counts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get your actionable status counts

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/counts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_my_curated_set_product_product_id(
        self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        product_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/curated_set/product/{jsonable_encoder(product_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_my_curated_set_product_product_id(
        self, product_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        product_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/curated_set/product/{jsonable_encoder(product_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_listings_from_your_feed(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get listings from your feed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/feed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_your_feed_customization_options(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        get your feed customization options

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/feed/customize",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_your_feed(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        get your feed

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/feed/grid",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_of_received_feedback(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        List of received feedback

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/feedback/received",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_of_sent_feedback(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        List of sent feedback

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/feedback/sent",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def see_what_the_user_is_following(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        See what the user is following

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/follows",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def returns_a_users_article_category_follows(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns a user's ArticleCategoryFollows

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/follows/articles",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def set_a_users_article_category_follows(
        self, *, category_uuids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Set a user's ArticleCategoryFollows

        Parameters
        ----------
        category_uuids : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/follows/articles",
            method="POST",
            json={
                "category_uuids": category_uuids,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_status_for_a_brand(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow status for a brand

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/brands/{jsonable_encoder(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_a_brand(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow a brand

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/brands/{jsonable_encoder(slug)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unfollow_a_brand(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Unfollow a brand

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/brands/{jsonable_encoder(slug)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_status_for_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(category)}/{jsonable_encoder(subcategory)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(category)}/{jsonable_encoder(subcategory)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unfollow_a_subcategory(
        self, category: str, subcategory: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(category)}/{jsonable_encoder(subcategory)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_status_for_a_category(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow status for a category

        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(identifier)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_a_category(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow a category

        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(uuid_)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unfollow_a_category(
        self, identifier: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Unfollow a category

        Parameters
        ----------
        identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/categories/{jsonable_encoder(identifier)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_status_for_a_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow status for a collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/collections/{jsonable_encoder(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_a_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow a collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/collections/{jsonable_encoder(slug)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unfollow_a_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Unfollow a collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/collections/{jsonable_encoder(slug)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_status_for_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow status for a handpicked collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/handpicked/{jsonable_encoder(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow a handpicked collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/handpicked/{jsonable_encoder(slug)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unfollow_a_handpicked_collection(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Unfollow a handpicked collection

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/handpicked/{jsonable_encoder(slug)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_status_for_a_search(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow status for a search

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/follows/search",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/follows/search",
            method="POST",
            json={
                "accepts_gift_cards": accepts_gift_cards,
                "accepts_payment_plans": accepts_payment_plans,
                "auction_price_max": auction_price_max,
                "category": category,
                "conditions": conditions,
                "currency": currency,
                "decade": decade,
                "exclude_auctions": exclude_auctions,
                "finish": finish,
                "handmade": handmade,
                "item_city": item_city,
                "item_country": item_country,
                "item_region": item_region,
                "item_state": item_state,
                "listing_type": listing_type,
                "local_pickup": local_pickup,
                "make": make,
                "model": model,
                "must_not": must_not,
                "not_ids": not_ids,
                "preferred_seller": preferred_seller,
                "price_max": price_max,
                "price_min": price_min,
                "product_type": product_type,
                "query": query,
                "ships_to": ships_to,
                "shop": shop,
                "shop_id": shop_id,
                "watchers_count_min": watchers_count_min,
                "year_max": year_max,
                "year_min": year_min,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_status_for_a_shop(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow status for a shop

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/shops/{jsonable_encoder(slug)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def follow_a_shop(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Follow a shop

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/shops/{jsonable_encoder(slug)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def unfollow_a_shop(
        self, slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Unfollow a shop

        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/shops/{jsonable_encoder(slug)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_a_follow(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a follow

        Parameters
        ----------
        follow_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/{jsonable_encoder(follow_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def post_my_follows_follow_id_alert(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        follow_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/{jsonable_encoder(follow_id)}/alert",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_my_follows_follow_id_alert(
        self, follow_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        follow_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/follows/{jsonable_encoder(follow_id)}/alert",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/listings",
            method="GET",
            params={
                "query": query,
                "auction_price_max": auction_price_max,
                "category": category,
                "product_type": product_type,
                "conditions": conditions,
                "decade": decade,
                "finish": finish,
                "handmade": handmade,
                "item_city": item_city,
                "item_country": item_country,
                "item_region": item_region,
                "item_state": item_state,
                "make": make,
                "model": model,
                "must_not": must_not,
                "price_max": price_max,
                "price_min": price_min,
                "currency": currency,
                "year_max": year_max,
                "year_min": year_min,
                "accepts_gift_cards": accepts_gift_cards,
                "preferred_seller": preferred_seller,
                "shop": shop,
                "shop_id": shop_id,
                "listing_type": listing_type,
                "ships_to": ships_to,
                "exclude_auctions": exclude_auctions,
                "accepts_payment_plans": accepts_payment_plans,
                "watchers_count_min": watchers_count_min,
                "not_ids": not_ids,
                "local_pickup": local_pickup,
                "state": state,
                "sku": sku,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/listings/drafts",
            method="GET",
            params={
                "query": query,
                "auction_price_max": auction_price_max,
                "category": category,
                "product_type": product_type,
                "conditions": conditions,
                "decade": decade,
                "finish": finish,
                "handmade": handmade,
                "item_city": item_city,
                "item_country": item_country,
                "item_region": item_region,
                "item_state": item_state,
                "make": make,
                "model": model,
                "must_not": must_not,
                "price_max": price_max,
                "price_min": price_min,
                "currency": currency,
                "year_max": year_max,
                "year_min": year_min,
                "accepts_gift_cards": accepts_gift_cards,
                "preferred_seller": preferred_seller,
                "shop": shop,
                "shop_id": shop_id,
                "listing_type": listing_type,
                "ships_to": ships_to,
                "exclude_auctions": exclude_auctions,
                "accepts_payment_plans": accepts_payment_plans,
                "watchers_count_min": watchers_count_min,
                "not_ids": not_ids,
                "local_pickup": local_pickup,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_list_of_active_negotiations_as_a_seller(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/listings/negotiations",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def end_a_listing(
        self,
        slug: str,
        *,
        reason: PutMyListingsSlugStateEndRequestReason,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/listings/{jsonable_encoder(slug)}/state/end",
            method="PUT",
            json={
                "reason": reason,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_list_of_your_lists_wishlist_watch_list_etc(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get a list of your lists (wishlist, watch list, etc)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/lists",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_list_of_active_negotiations_as_a_buyer(
        self,
        *,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/negotiations/buying",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_offer_details(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get offer details

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/negotiations/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def accept_an_offer(
        self, id: str, *, message: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/negotiations/{jsonable_encoder(id)}/accept",
            method="POST",
            json={
                "message": message,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/negotiations/{jsonable_encoder(id)}/counter",
            method="POST",
            json={
                "country_code": country_code,
                "layaway_terms_slug": layaway_terms_slug,
                "message": message,
                "offer_items": convert_and_respect_annotation_metadata(
                    object_=offer_items,
                    annotation=typing.Sequence[PostMyNegotiationsIdCounterRequestOfferItemsItem],
                    direction="write",
                ),
                "price": convert_and_respect_annotation_metadata(
                    object_=price, annotation=PostMyNegotiationsIdCounterRequestPrice, direction="write"
                ),
                "quantity": quantity,
                "recipient_id": recipient_id,
                "region_code": region_code,
                "shipping_price": convert_and_respect_annotation_metadata(
                    object_=shipping_price,
                    annotation=PostMyNegotiationsIdCounterRequestShippingPrice,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def decline_an_offer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Decline an offer

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/negotiations/{jsonable_encoder(id)}/decline",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_of_orders_that_need_feedback(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        List of orders that need feedback

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/orders/awaiting_feedback",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def returns_all_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns all orders, newest first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/orders/buying/all",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_my_orders_buying_by_uuid_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/orders/buying/by_uuid/{jsonable_encoder(uuid_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def returns_unpaid_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns unpaid orders, newest first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/orders/buying/unpaid",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def returns_order_details_for_a_buyer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns order details for a buyer

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/orders/buying/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def marks_an_order_as_received_by_the_buyer(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Marks an order as received by the buyer

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/orders/buying/{jsonable_encoder(id)}/mark_received",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_all_seller_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get all seller orders, newest first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/orders/selling/all",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_unpaid_seller_orders_newest_first(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get unpaid seller orders, newest first.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/orders/selling/unpaid",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def see_previous_orders_from_buyer(
        self, buyer_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        See previous orders from buyer

        Parameters
        ----------
        buyer_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/orders/selling/buyer_history/{jsonable_encoder(buyer_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_my_orders_selling_by_uuid_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/orders/selling/by_uuid/{jsonable_encoder(uuid_)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def returns_order_details_for_a_seller(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Returns order details for a seller

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/orders/selling/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def marks_an_order_as_picked_up(
        self, id: str, *, date: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/orders/selling/{jsonable_encoder(id)}/mark_picked_up",
            method="POST",
            json={
                "date": date,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def marks_an_order_as_shipped(
        self,
        id: str,
        *,
        provider: str,
        send_notification: bool,
        tracking_number: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/orders/selling/{jsonable_encoder(id)}/ship",
            method="POST",
            json={
                "provider": provider,
                "send_notification": send_notification,
                "tracking_number": tracking_number,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def initiate_a_refund_for_a_sold_order(
        self, order_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Initiate a refund for a sold order

        Parameters
        ----------
        order_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/orders/selling/{jsonable_encoder(order_id)}/refund_requests",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/payments/selling",
            method="GET",
            params={
                "page": page,
                "per_page": per_page,
                "offset": offset,
                "created_start_date": created_start_date,
                "created_end_date": created_end_date,
                "updated_start_date": updated_start_date,
                "updated_end_date": updated_end_date,
                "order_id": order_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_payment(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get payment

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/payments/selling/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_list_of_payouts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get a list of payouts

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/payouts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def read_the_line_items_of_a_payout(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Read the line items of a payout

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/payouts/{jsonable_encoder(id)}/line_items",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_list_of_refund_requests_as_a_seller(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get a list of refund requests as a seller

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/refund_requests/selling",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_a_refund_request_for_a_sold_order(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Update a refund request for a sold order

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/refund_requests/selling/{jsonable_encoder(id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_list_of_your_recently_viewed_listings(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get a list of your recently viewed listings.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/viewed_listings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_list_of_wishlisted_items(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Get a list of wishlisted items

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "my/wishlist",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def add_a_listing_to_your_wishlist(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Add a listing to your wishlist

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/wishlist/{jsonable_encoder(id)}",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def remove_a_listing_from_your_wishlist(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Remove a listing from your wishlist

        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"my/wishlist/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
