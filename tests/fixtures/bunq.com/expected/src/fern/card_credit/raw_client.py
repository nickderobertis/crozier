

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
from ..errors.bad_request_error import BadRequestError
from ..types.card_credit_create import CardCreditCreate
from ..types.card_pin_assignment import CardPinAssignment
from ..types.pointer import Pointer
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCardCreditClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_card_credit_for_user(
        self,
        user_id: int,
        *,
        name_on_card: str,
        product_type: str,
        second_line: str,
        type: str,
        alias: typing.Optional[Pointer] = OMIT,
        monetary_account_id_fallback: typing.Optional[int] = OMIT,
        order_status: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        preferred_name_on_card: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CardCreditCreate]:
        """
        Create a new credit card request.

        Parameters
        ----------
        user_id : int


        name_on_card : str
            The user's name as it will be on the card. Check 'card-name' for the available card names for a user.

        product_type : str
            The product type of the card to order.

        second_line : str
            The second line of text on the card, used as name/description for it. It can contain at most 17 characters and it can be empty.

        type : str
            The type of card to order. Can be MASTERCARD.

        alias : typing.Optional[Pointer]
            The pointer to the monetary account that will be connected at first with the card. Its IBAN code is also the one that will be printed on the card itself. The pointer must be of type IBAN.

        monetary_account_id_fallback : typing.Optional[int]
            ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.

        order_status : typing.Optional[str]
            The order status of this card. Can be CARD_REQUEST_PENDING or VIRTUAL_DELIVERY.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        preferred_name_on_card : typing.Optional[str]
            The user's preferred name that can be put on the card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CardCreditCreate]
            With bunq it is possible to order credit cards that can then be connected with each one of the monetary accounts the user has access to (including connected accounts).
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card-credit",
            method="POST",
            json={
                "alias": convert_and_respect_annotation_metadata(object_=alias, annotation=Pointer, direction="write"),
                "monetary_account_id_fallback": monetary_account_id_fallback,
                "name_on_card": name_on_card,
                "order_status": order_status,
                "pin_code_assignment": convert_and_respect_annotation_metadata(
                    object_=pin_code_assignment, annotation=typing.Sequence[CardPinAssignment], direction="write"
                ),
                "preferred_name_on_card": preferred_name_on_card,
                "product_type": product_type,
                "second_line": second_line,
                "type": type,
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
                    CardCreditCreate,
                    parse_obj_as(
                        type_=CardCreditCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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


class AsyncRawCardCreditClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_card_credit_for_user(
        self,
        user_id: int,
        *,
        name_on_card: str,
        product_type: str,
        second_line: str,
        type: str,
        alias: typing.Optional[Pointer] = OMIT,
        monetary_account_id_fallback: typing.Optional[int] = OMIT,
        order_status: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        preferred_name_on_card: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CardCreditCreate]:
        """
        Create a new credit card request.

        Parameters
        ----------
        user_id : int


        name_on_card : str
            The user's name as it will be on the card. Check 'card-name' for the available card names for a user.

        product_type : str
            The product type of the card to order.

        second_line : str
            The second line of text on the card, used as name/description for it. It can contain at most 17 characters and it can be empty.

        type : str
            The type of card to order. Can be MASTERCARD.

        alias : typing.Optional[Pointer]
            The pointer to the monetary account that will be connected at first with the card. Its IBAN code is also the one that will be printed on the card itself. The pointer must be of type IBAN.

        monetary_account_id_fallback : typing.Optional[int]
            ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.

        order_status : typing.Optional[str]
            The order status of this card. Can be CARD_REQUEST_PENDING or VIRTUAL_DELIVERY.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        preferred_name_on_card : typing.Optional[str]
            The user's preferred name that can be put on the card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CardCreditCreate]
            With bunq it is possible to order credit cards that can then be connected with each one of the monetary accounts the user has access to (including connected accounts).
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card-credit",
            method="POST",
            json={
                "alias": convert_and_respect_annotation_metadata(object_=alias, annotation=Pointer, direction="write"),
                "monetary_account_id_fallback": monetary_account_id_fallback,
                "name_on_card": name_on_card,
                "order_status": order_status,
                "pin_code_assignment": convert_and_respect_annotation_metadata(
                    object_=pin_code_assignment, annotation=typing.Sequence[CardPinAssignment], direction="write"
                ),
                "preferred_name_on_card": preferred_name_on_card,
                "product_type": product_type,
                "second_line": second_line,
                "type": type,
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
                    CardCreditCreate,
                    parse_obj_as(
                        type_=CardCreditCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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
