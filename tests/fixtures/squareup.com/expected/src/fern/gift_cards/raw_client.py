

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
from ..types.create_gift_card_response import CreateGiftCardResponse
from ..types.gift_card import GiftCard
from ..types.link_customer_to_gift_card_response import LinkCustomerToGiftCardResponse
from ..types.list_gift_cards_response import ListGiftCardsResponse
from ..types.retrieve_gift_card_from_gan_response import RetrieveGiftCardFromGanResponse
from ..types.retrieve_gift_card_from_nonce_response import RetrieveGiftCardFromNonceResponse
from ..types.retrieve_gift_card_response import RetrieveGiftCardResponse
from ..types.unlink_customer_from_gift_card_response import UnlinkCustomerFromGiftCardResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGiftCardsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_gift_cards(
        self,
        *,
        type: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListGiftCardsResponse]:
        """
        Lists all gift cards. You can specify optional filters to retrieve
        a subset of the gift cards.

        Parameters
        ----------
        type : typing.Optional[str]
            If a type is provided, gift cards of this type are returned
            (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)).
            If no type is provided, it returns gift cards of all types.

        state : typing.Optional[str]
            If the state is provided, it returns the gift cards in the specified state
            (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)).
            Otherwise, it returns the gift cards of all states.

        limit : typing.Optional[int]
            If a value is provided, it returns only that number of results per page.
            The maximum number of results allowed per page is 50. The default value is 30.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            If a cursor is not provided, it returns the first page of the results.
            For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination).

        customer_id : typing.Optional[str]
            If a value is provided, returns only the gift cards linked to the specified customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListGiftCardsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/gift-cards",
            method="GET",
            params={
                "type": type,
                "state": state,
                "limit": limit,
                "cursor": cursor,
                "customer_id": customer_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGiftCardsResponse,
                    parse_obj_as(
                        type_=ListGiftCardsResponse,
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

    def create_gift_card(
        self,
        *,
        gift_card: GiftCard,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateGiftCardResponse]:
        """
        Creates a digital gift card or registers a physical (plastic) gift card. You must activate the gift card before
        it can be used for payment. For more information, see
        [Selling gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#selling-square-gift-cards).

        Parameters
        ----------
        gift_card : GiftCard

        idempotency_key : str
            A unique string that identifies the `CreateGiftCard` request.

        location_id : str
            The location ID where the gift card that will be created should be registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateGiftCardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/gift-cards",
            method="POST",
            json={
                "gift_card": convert_and_respect_annotation_metadata(
                    object_=gift_card, annotation=GiftCard, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "location_id": location_id,
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
                    CreateGiftCardResponse,
                    parse_obj_as(
                        type_=CreateGiftCardResponse,
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

    def retrieve_gift_card_from_gan(
        self, *, gan: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveGiftCardFromGanResponse]:
        """
        Retrieves a gift card using the gift card account number (GAN).

        Parameters
        ----------
        gan : str
            The gift card account number (GAN) of the gift card to retrieve.
            The maximum length of a GAN is 255 digits to account for third-party GANs that have been imported.
            Square-issued gift cards have 16-digit GANs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveGiftCardFromGanResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/gift-cards/from-gan",
            method="POST",
            json={
                "gan": gan,
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
                    RetrieveGiftCardFromGanResponse,
                    parse_obj_as(
                        type_=RetrieveGiftCardFromGanResponse,
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

    def retrieve_gift_card_from_nonce(
        self, *, nonce: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveGiftCardFromNonceResponse]:
        """
        Retrieves a gift card using a nonce (a secure token) that represents the gift card.

        Parameters
        ----------
        nonce : str
            The nonce of the gift card to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveGiftCardFromNonceResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/gift-cards/from-nonce",
            method="POST",
            json={
                "nonce": nonce,
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
                    RetrieveGiftCardFromNonceResponse,
                    parse_obj_as(
                        type_=RetrieveGiftCardFromNonceResponse,
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

    def link_customer_to_gift_card(
        self, gift_card_id: str, *, customer_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[LinkCustomerToGiftCardResponse]:
        """
        Links a customer to a gift card

        Parameters
        ----------
        gift_card_id : str
            The ID of the gift card to link.

        customer_id : str
            The ID of the customer to be linked.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LinkCustomerToGiftCardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/gift-cards/{encode_path_param(gift_card_id)}/link-customer",
            method="POST",
            json={
                "customer_id": customer_id,
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
                    LinkCustomerToGiftCardResponse,
                    parse_obj_as(
                        type_=LinkCustomerToGiftCardResponse,
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

    def unlink_customer_from_gift_card(
        self, gift_card_id: str, *, customer_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UnlinkCustomerFromGiftCardResponse]:
        """
        Unlinks a customer from a gift card

        Parameters
        ----------
        gift_card_id : str


        customer_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UnlinkCustomerFromGiftCardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/gift-cards/{encode_path_param(gift_card_id)}/unlink-customer",
            method="POST",
            json={
                "customer_id": customer_id,
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
                    UnlinkCustomerFromGiftCardResponse,
                    parse_obj_as(
                        type_=UnlinkCustomerFromGiftCardResponse,
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

    def retrieve_gift_card(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveGiftCardResponse]:
        """
        Retrieves a gift card using its ID.

        Parameters
        ----------
        id : str
            The ID of the gift card to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveGiftCardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/gift-cards/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveGiftCardResponse,
                    parse_obj_as(
                        type_=RetrieveGiftCardResponse,
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


class AsyncRawGiftCardsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_gift_cards(
        self,
        *,
        type: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListGiftCardsResponse]:
        """
        Lists all gift cards. You can specify optional filters to retrieve
        a subset of the gift cards.

        Parameters
        ----------
        type : typing.Optional[str]
            If a type is provided, gift cards of this type are returned
            (see [GiftCardType](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardType)).
            If no type is provided, it returns gift cards of all types.

        state : typing.Optional[str]
            If the state is provided, it returns the gift cards in the specified state
            (see [GiftCardStatus](https://developer.squareup.com/reference/square_2021-08-18/enums/GiftCardStatus)).
            Otherwise, it returns the gift cards of all states.

        limit : typing.Optional[int]
            If a value is provided, it returns only that number of results per page.
            The maximum number of results allowed per page is 50. The default value is 30.

        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            If a cursor is not provided, it returns the first page of the results.
            For more information, see [Pagination](https://developer.squareup.com/docs/docs/working-with-apis/pagination).

        customer_id : typing.Optional[str]
            If a value is provided, returns only the gift cards linked to the specified customer

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListGiftCardsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/gift-cards",
            method="GET",
            params={
                "type": type,
                "state": state,
                "limit": limit,
                "cursor": cursor,
                "customer_id": customer_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListGiftCardsResponse,
                    parse_obj_as(
                        type_=ListGiftCardsResponse,
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

    async def create_gift_card(
        self,
        *,
        gift_card: GiftCard,
        idempotency_key: str,
        location_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateGiftCardResponse]:
        """
        Creates a digital gift card or registers a physical (plastic) gift card. You must activate the gift card before
        it can be used for payment. For more information, see
        [Selling gift cards](https://developer.squareup.com/docs/gift-cards/using-gift-cards-api#selling-square-gift-cards).

        Parameters
        ----------
        gift_card : GiftCard

        idempotency_key : str
            A unique string that identifies the `CreateGiftCard` request.

        location_id : str
            The location ID where the gift card that will be created should be registered.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateGiftCardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/gift-cards",
            method="POST",
            json={
                "gift_card": convert_and_respect_annotation_metadata(
                    object_=gift_card, annotation=GiftCard, direction="write"
                ),
                "idempotency_key": idempotency_key,
                "location_id": location_id,
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
                    CreateGiftCardResponse,
                    parse_obj_as(
                        type_=CreateGiftCardResponse,
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

    async def retrieve_gift_card_from_gan(
        self, *, gan: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveGiftCardFromGanResponse]:
        """
        Retrieves a gift card using the gift card account number (GAN).

        Parameters
        ----------
        gan : str
            The gift card account number (GAN) of the gift card to retrieve.
            The maximum length of a GAN is 255 digits to account for third-party GANs that have been imported.
            Square-issued gift cards have 16-digit GANs.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveGiftCardFromGanResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/gift-cards/from-gan",
            method="POST",
            json={
                "gan": gan,
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
                    RetrieveGiftCardFromGanResponse,
                    parse_obj_as(
                        type_=RetrieveGiftCardFromGanResponse,
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

    async def retrieve_gift_card_from_nonce(
        self, *, nonce: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveGiftCardFromNonceResponse]:
        """
        Retrieves a gift card using a nonce (a secure token) that represents the gift card.

        Parameters
        ----------
        nonce : str
            The nonce of the gift card to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveGiftCardFromNonceResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/gift-cards/from-nonce",
            method="POST",
            json={
                "nonce": nonce,
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
                    RetrieveGiftCardFromNonceResponse,
                    parse_obj_as(
                        type_=RetrieveGiftCardFromNonceResponse,
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

    async def link_customer_to_gift_card(
        self, gift_card_id: str, *, customer_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[LinkCustomerToGiftCardResponse]:
        """
        Links a customer to a gift card

        Parameters
        ----------
        gift_card_id : str
            The ID of the gift card to link.

        customer_id : str
            The ID of the customer to be linked.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LinkCustomerToGiftCardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/gift-cards/{encode_path_param(gift_card_id)}/link-customer",
            method="POST",
            json={
                "customer_id": customer_id,
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
                    LinkCustomerToGiftCardResponse,
                    parse_obj_as(
                        type_=LinkCustomerToGiftCardResponse,
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

    async def unlink_customer_from_gift_card(
        self, gift_card_id: str, *, customer_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UnlinkCustomerFromGiftCardResponse]:
        """
        Unlinks a customer from a gift card

        Parameters
        ----------
        gift_card_id : str


        customer_id : str


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UnlinkCustomerFromGiftCardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/gift-cards/{encode_path_param(gift_card_id)}/unlink-customer",
            method="POST",
            json={
                "customer_id": customer_id,
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
                    UnlinkCustomerFromGiftCardResponse,
                    parse_obj_as(
                        type_=UnlinkCustomerFromGiftCardResponse,
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

    async def retrieve_gift_card(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveGiftCardResponse]:
        """
        Retrieves a gift card using its ID.

        Parameters
        ----------
        id : str
            The ID of the gift card to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveGiftCardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/gift-cards/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveGiftCardResponse,
                    parse_obj_as(
                        type_=RetrieveGiftCardResponse,
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
