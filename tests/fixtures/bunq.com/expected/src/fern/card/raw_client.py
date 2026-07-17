

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
from ..types.amount import Amount
from ..types.card_country_permission import CardCountryPermission
from ..types.card_listing import CardListing
from ..types.card_pin_assignment import CardPinAssignment
from ..types.card_primary_account_number import CardPrimaryAccountNumber
from ..types.card_read import CardRead
from ..types.card_update import CardUpdate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_card_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[CardListing]]:
        """
        Return all the cards available to the user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[CardListing]]
            Endpoint for retrieving details for the cards the user has access to.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CardListing],
                    parse_obj_as(
                        type_=typing.List[CardListing],
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

    def read_card_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CardRead]:
        """
        Return the details of a specific card.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CardRead]
            Endpoint for retrieving details for the cards the user has access to.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CardRead,
                    parse_obj_as(
                        type_=CardRead,
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

    def update_card_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        activation_code: typing.Optional[str] = OMIT,
        card_limit: typing.Optional[Amount] = OMIT,
        card_limit_atm: typing.Optional[Amount] = OMIT,
        country_permission: typing.Optional[typing.Sequence[CardCountryPermission]] = OMIT,
        monetary_account_id_fallback: typing.Optional[int] = OMIT,
        order_status: typing.Optional[str] = OMIT,
        pin_code: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        primary_account_numbers: typing.Optional[typing.Sequence[CardPrimaryAccountNumber]] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CardUpdate]:
        """
        Update the card details. Allow to change pin code, status, limits, country permissions and the monetary account connected to the card. When the card has been received, it can be also activated through this endpoint.

        Parameters
        ----------
        user_id : int


        item_id : int


        activation_code : typing.Optional[str]
            DEPRECATED: Activate a card by setting status to ACTIVE when the order_status is ACCEPTED_FOR_PRODUCTION.

        card_limit : typing.Optional[Amount]
            The spending limit for the card.

        card_limit_atm : typing.Optional[Amount]
            The ATM spending limit for the card.

        country_permission : typing.Optional[typing.Sequence[CardCountryPermission]]
            The countries for which to grant (temporary) permissions to use the card.

        monetary_account_id_fallback : typing.Optional[int]
            ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.

        order_status : typing.Optional[str]
            The order status to set for the card. Set to CARD_REQUEST_PENDING to get a virtual card produced.

        pin_code : typing.Optional[str]
            The plaintext pin code. Requests require encryption to be enabled.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        primary_account_numbers : typing.Optional[typing.Sequence[CardPrimaryAccountNumber]]
            Array of PANs and their attributes.

        status : typing.Optional[str]
            The status to set for the card. Can be ACTIVE, DEACTIVATED, LOST, STOLEN or CANCELLED, and can only be set to LOST/STOLEN/CANCELLED when order status is ACCEPTED_FOR_PRODUCTION/DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Can only be set to DEACTIVATED after initial activation, i.e. order_status is DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Mind that all the possible choices (apart from ACTIVE and DEACTIVATED) are permanent and cannot be changed after.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CardUpdate]
            Endpoint for retrieving details for the cards the user has access to.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "activation_code": activation_code,
                "card_limit": convert_and_respect_annotation_metadata(
                    object_=card_limit, annotation=Amount, direction="write"
                ),
                "card_limit_atm": convert_and_respect_annotation_metadata(
                    object_=card_limit_atm, annotation=Amount, direction="write"
                ),
                "country_permission": convert_and_respect_annotation_metadata(
                    object_=country_permission, annotation=typing.Sequence[CardCountryPermission], direction="write"
                ),
                "monetary_account_id_fallback": monetary_account_id_fallback,
                "order_status": order_status,
                "pin_code": pin_code,
                "pin_code_assignment": convert_and_respect_annotation_metadata(
                    object_=pin_code_assignment, annotation=typing.Sequence[CardPinAssignment], direction="write"
                ),
                "primary_account_numbers": convert_and_respect_annotation_metadata(
                    object_=primary_account_numbers,
                    annotation=typing.Sequence[CardPrimaryAccountNumber],
                    direction="write",
                ),
                "status": status,
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
                    CardUpdate,
                    parse_obj_as(
                        type_=CardUpdate,
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


class AsyncRawCardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_card_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[CardListing]]:
        """
        Return all the cards available to the user.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[CardListing]]
            Endpoint for retrieving details for the cards the user has access to.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[CardListing],
                    parse_obj_as(
                        type_=typing.List[CardListing],
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

    async def read_card_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CardRead]:
        """
        Return the details of a specific card.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CardRead]
            Endpoint for retrieving details for the cards the user has access to.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CardRead,
                    parse_obj_as(
                        type_=CardRead,
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

    async def update_card_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        activation_code: typing.Optional[str] = OMIT,
        card_limit: typing.Optional[Amount] = OMIT,
        card_limit_atm: typing.Optional[Amount] = OMIT,
        country_permission: typing.Optional[typing.Sequence[CardCountryPermission]] = OMIT,
        monetary_account_id_fallback: typing.Optional[int] = OMIT,
        order_status: typing.Optional[str] = OMIT,
        pin_code: typing.Optional[str] = OMIT,
        pin_code_assignment: typing.Optional[typing.Sequence[CardPinAssignment]] = OMIT,
        primary_account_numbers: typing.Optional[typing.Sequence[CardPrimaryAccountNumber]] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CardUpdate]:
        """
        Update the card details. Allow to change pin code, status, limits, country permissions and the monetary account connected to the card. When the card has been received, it can be also activated through this endpoint.

        Parameters
        ----------
        user_id : int


        item_id : int


        activation_code : typing.Optional[str]
            DEPRECATED: Activate a card by setting status to ACTIVE when the order_status is ACCEPTED_FOR_PRODUCTION.

        card_limit : typing.Optional[Amount]
            The spending limit for the card.

        card_limit_atm : typing.Optional[Amount]
            The ATM spending limit for the card.

        country_permission : typing.Optional[typing.Sequence[CardCountryPermission]]
            The countries for which to grant (temporary) permissions to use the card.

        monetary_account_id_fallback : typing.Optional[int]
            ID of the MA to be used as fallback for this card if insufficient balance. Fallback account is removed if not supplied.

        order_status : typing.Optional[str]
            The order status to set for the card. Set to CARD_REQUEST_PENDING to get a virtual card produced.

        pin_code : typing.Optional[str]
            The plaintext pin code. Requests require encryption to be enabled.

        pin_code_assignment : typing.Optional[typing.Sequence[CardPinAssignment]]
            Array of Types, PINs, account IDs assigned to the card.

        primary_account_numbers : typing.Optional[typing.Sequence[CardPrimaryAccountNumber]]
            Array of PANs and their attributes.

        status : typing.Optional[str]
            The status to set for the card. Can be ACTIVE, DEACTIVATED, LOST, STOLEN or CANCELLED, and can only be set to LOST/STOLEN/CANCELLED when order status is ACCEPTED_FOR_PRODUCTION/DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Can only be set to DEACTIVATED after initial activation, i.e. order_status is DELIVERED_TO_CUSTOMER/CARD_UPDATE_REQUESTED/CARD_UPDATE_SENT/CARD_UPDATE_ACCEPTED. Mind that all the possible choices (apart from ACTIVE and DEACTIVATED) are permanent and cannot be changed after.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CardUpdate]
            Endpoint for retrieving details for the cards the user has access to.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{encode_path_param(user_id)}/card/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "activation_code": activation_code,
                "card_limit": convert_and_respect_annotation_metadata(
                    object_=card_limit, annotation=Amount, direction="write"
                ),
                "card_limit_atm": convert_and_respect_annotation_metadata(
                    object_=card_limit_atm, annotation=Amount, direction="write"
                ),
                "country_permission": convert_and_respect_annotation_metadata(
                    object_=country_permission, annotation=typing.Sequence[CardCountryPermission], direction="write"
                ),
                "monetary_account_id_fallback": monetary_account_id_fallback,
                "order_status": order_status,
                "pin_code": pin_code,
                "pin_code_assignment": convert_and_respect_annotation_metadata(
                    object_=pin_code_assignment, annotation=typing.Sequence[CardPinAssignment], direction="write"
                ),
                "primary_account_numbers": convert_and_respect_annotation_metadata(
                    object_=primary_account_numbers,
                    annotation=typing.Sequence[CardPrimaryAccountNumber],
                    direction="write",
                ),
                "status": status,
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
                    CardUpdate,
                    parse_obj_as(
                        type_=CardUpdate,
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
