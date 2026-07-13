

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..types.card_pin_assignment import CardPinAssignment
from ..types.card_replace_create import CardReplaceCreate


OMIT = typing.cast(typing.Any, ...)


class RawReplaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_replace_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        name_on_card: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        preferred_name_on_card: typing.Optional[str] = OMIT,
        second_line: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CardReplaceCreate]:
        """
        Request a card replacement.

        Parameters
        ----------
        user_id : int


        card_id : int


        name_on_card : typing.Optional[str]
            The user's name as it will be on the card. Check 'card-name' for the available card names for a user.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        preferred_name_on_card : typing.Optional[str]
            The user's preferred name that can be put on the card.

        second_line : typing.Optional[str]
            The second line on the card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CardReplaceCreate]
            It is possible to order a card replacement with the bunq API.<br/><br/>You can order up to one free card replacement per year. Additional replacement requests will be billed.<br/><br/>The card replacement will have the same expiry date and the same pricing as the old card, but it will have a new card number. You can change the description and optional the PIN through the card replacement endpoint.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/replace",
            method="POST",
            json={
                "name_on_card": name_on_card,
                "pin_code_assignment": convert_and_respect_annotation_metadata(
                    object_=pin_code_assignment, annotation=typing.Sequence[CardPinAssignment], direction="write"
                ),
                "preferred_name_on_card": preferred_name_on_card,
                "second_line": second_line,
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
                    CardReplaceCreate,
                    parse_obj_as(
                        type_=CardReplaceCreate,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawReplaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_replace_for_user_card(
        self,
        user_id: int,
        card_id: int,
        *,
        name_on_card: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        preferred_name_on_card: typing.Optional[str] = OMIT,
        second_line: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CardReplaceCreate]:
        """
        Request a card replacement.

        Parameters
        ----------
        user_id : int


        card_id : int


        name_on_card : typing.Optional[str]
            The user's name as it will be on the card. Check 'card-name' for the available card names for a user.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        preferred_name_on_card : typing.Optional[str]
            The user's preferred name that can be put on the card.

        second_line : typing.Optional[str]
            The second line on the card.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CardReplaceCreate]
            It is possible to order a card replacement with the bunq API.<br/><br/>You can order up to one free card replacement per year. Additional replacement requests will be billed.<br/><br/>The card replacement will have the same expiry date and the same pricing as the old card, but it will have a new card number. You can change the description and optional the PIN through the card replacement endpoint.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/card/{jsonable_encoder(card_id)}/replace",
            method="POST",
            json={
                "name_on_card": name_on_card,
                "pin_code_assignment": convert_and_respect_annotation_metadata(
                    object_=pin_code_assignment, annotation=typing.Sequence[CardPinAssignment], direction="write"
                ),
                "preferred_name_on_card": preferred_name_on_card,
                "second_line": second_line,
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
                    CardReplaceCreate,
                    parse_obj_as(
                        type_=CardReplaceCreate,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
