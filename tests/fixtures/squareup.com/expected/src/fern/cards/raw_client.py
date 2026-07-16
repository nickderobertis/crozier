

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
from ..types.card import Card
from ..types.create_card_response import CreateCardResponse
from ..types.disable_card_response import DisableCardResponse
from ..types.list_cards_response import ListCardsResponse
from ..types.retrieve_card_response import RetrieveCardResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCardsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_cards(
        self,
        *,
        cursor: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        include_disabled: typing.Optional[bool] = None,
        reference_id: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListCardsResponse]:
        """
        Retrieves a list of cards owned by the account making the request.
        A max of 25 cards will be returned.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        customer_id : typing.Optional[str]
            Limit results to cards associated with the customer supplied.
            By default, all cards owned by the merchant are returned.

        include_disabled : typing.Optional[bool]
            Includes disabled cards.
            By default, all enabled cards owned by the merchant are returned.

        reference_id : typing.Optional[str]
            Limit results to cards associated with the reference_id supplied.

        sort_order : typing.Optional[str]
            Sorts the returned list by when the card was created with the specified order.
            This field defaults to ASC.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListCardsResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/cards",
            method="GET",
            params={
                "cursor": cursor,
                "customer_id": customer_id,
                "include_disabled": include_disabled,
                "reference_id": reference_id,
                "sort_order": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCardsResponse,
                    parse_obj_as(
                        type_=ListCardsResponse,
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

    def create_card(
        self,
        *,
        card: Card,
        idempotency_key: str,
        source_id: str,
        verification_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateCardResponse]:
        """
        Adds a card on file to an existing merchant.

        Parameters
        ----------
        card : Card

        idempotency_key : str
            A unique string that identifies this CreateCard request. Keys can be
            any valid string and must be unique for every request.

            Max: 45 characters

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        source_id : str
            The ID of the source which represents the card information to be stored. This can be a card nonce or a payment id.

        verification_token : typing.Optional[str]
            An identifying token generated by [Payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
            Verification tokens encapsulate customer device information and 3-D Secure
            challenge results to indicate that Square has verified the buyer identity.

            See the [SCA Overview](https://developer.squareup.com/docs/sca-overview).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateCardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/cards",
            method="POST",
            json={
                "card": convert_and_respect_annotation_metadata(object_=card, annotation=Card, direction="write"),
                "idempotency_key": idempotency_key,
                "source_id": source_id,
                "verification_token": verification_token,
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
                    CreateCardResponse,
                    parse_obj_as(
                        type_=CreateCardResponse,
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

    def retrieve_card(
        self, card_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveCardResponse]:
        """
        Retrieves details for a specific Card.

        Parameters
        ----------
        card_id : str
            Unique ID for the desired Card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveCardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/cards/{encode_path_param(card_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveCardResponse,
                    parse_obj_as(
                        type_=RetrieveCardResponse,
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

    def disable_card(
        self, card_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DisableCardResponse]:
        """
        Disables the card, preventing any further updates or charges.
        Disabling an already disabled card is allowed but has no effect.

        Parameters
        ----------
        card_id : str
            Unique ID for the desired Card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DisableCardResponse]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/cards/{encode_path_param(card_id)}/disable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DisableCardResponse,
                    parse_obj_as(
                        type_=DisableCardResponse,
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


class AsyncRawCardsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_cards(
        self,
        *,
        cursor: typing.Optional[str] = None,
        customer_id: typing.Optional[str] = None,
        include_disabled: typing.Optional[bool] = None,
        reference_id: typing.Optional[str] = None,
        sort_order: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListCardsResponse]:
        """
        Retrieves a list of cards owned by the account making the request.
        A max of 25 cards will be returned.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this to retrieve the next set of results for your original query.

            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        customer_id : typing.Optional[str]
            Limit results to cards associated with the customer supplied.
            By default, all cards owned by the merchant are returned.

        include_disabled : typing.Optional[bool]
            Includes disabled cards.
            By default, all enabled cards owned by the merchant are returned.

        reference_id : typing.Optional[str]
            Limit results to cards associated with the reference_id supplied.

        sort_order : typing.Optional[str]
            Sorts the returned list by when the card was created with the specified order.
            This field defaults to ASC.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListCardsResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/cards",
            method="GET",
            params={
                "cursor": cursor,
                "customer_id": customer_id,
                "include_disabled": include_disabled,
                "reference_id": reference_id,
                "sort_order": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListCardsResponse,
                    parse_obj_as(
                        type_=ListCardsResponse,
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

    async def create_card(
        self,
        *,
        card: Card,
        idempotency_key: str,
        source_id: str,
        verification_token: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateCardResponse]:
        """
        Adds a card on file to an existing merchant.

        Parameters
        ----------
        card : Card

        idempotency_key : str
            A unique string that identifies this CreateCard request. Keys can be
            any valid string and must be unique for every request.

            Max: 45 characters

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        source_id : str
            The ID of the source which represents the card information to be stored. This can be a card nonce or a payment id.

        verification_token : typing.Optional[str]
            An identifying token generated by [Payments.verifyBuyer()](https://developer.squareup.com/reference/sdks/web/payments/objects/Payments#Payments.verifyBuyer).
            Verification tokens encapsulate customer device information and 3-D Secure
            challenge results to indicate that Square has verified the buyer identity.

            See the [SCA Overview](https://developer.squareup.com/docs/sca-overview).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateCardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/cards",
            method="POST",
            json={
                "card": convert_and_respect_annotation_metadata(object_=card, annotation=Card, direction="write"),
                "idempotency_key": idempotency_key,
                "source_id": source_id,
                "verification_token": verification_token,
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
                    CreateCardResponse,
                    parse_obj_as(
                        type_=CreateCardResponse,
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

    async def retrieve_card(
        self, card_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveCardResponse]:
        """
        Retrieves details for a specific Card.

        Parameters
        ----------
        card_id : str
            Unique ID for the desired Card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveCardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/cards/{encode_path_param(card_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveCardResponse,
                    parse_obj_as(
                        type_=RetrieveCardResponse,
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

    async def disable_card(
        self, card_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DisableCardResponse]:
        """
        Disables the card, preventing any further updates or charges.
        Disabling an already disabled card is allowed but has no effect.

        Parameters
        ----------
        card_id : str
            Unique ID for the desired Card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DisableCardResponse]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/cards/{encode_path_param(card_id)}/disable",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DisableCardResponse,
                    parse_obj_as(
                        type_=DisableCardResponse,
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
