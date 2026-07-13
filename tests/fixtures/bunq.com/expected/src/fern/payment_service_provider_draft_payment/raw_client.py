

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
from ..types.amount import Amount
from ..types.payment_service_provider_draft_payment_create import PaymentServiceProviderDraftPaymentCreate
from ..types.payment_service_provider_draft_payment_listing import PaymentServiceProviderDraftPaymentListing
from ..types.payment_service_provider_draft_payment_read import PaymentServiceProviderDraftPaymentRead
from ..types.payment_service_provider_draft_payment_update import PaymentServiceProviderDraftPaymentUpdate


OMIT = typing.cast(typing.Any, ...)


class RawPaymentServiceProviderDraftPaymentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_payment_service_provider_draft_payment_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[PaymentServiceProviderDraftPaymentListing]]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[PaymentServiceProviderDraftPaymentListing]]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-service-provider-draft-payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PaymentServiceProviderDraftPaymentListing],
                    parse_obj_as(
                        type_=typing.List[PaymentServiceProviderDraftPaymentListing],
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

    def create_payment_service_provider_draft_payment_for_user(
        self,
        user_id: int,
        *,
        amount: Amount,
        counterparty_iban: str,
        counterparty_name: str,
        description: str,
        sender_iban: str,
        sender_name: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaymentServiceProviderDraftPaymentCreate]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        amount : Amount
            The Amount to transfer with the Payment. Must be bigger than 0.

        counterparty_iban : str
            The IBAN of the counterparty.

        counterparty_name : str
            The name of the counterparty.

        description : str
            Description of the payment.

        sender_iban : str
            The IBAN of the sender.

        sender_name : typing.Optional[str]
            The name of the sender.

        status : typing.Optional[str]
            The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentServiceProviderDraftPaymentCreate]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-service-provider-draft-payment",
            method="POST",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "counterparty_iban": counterparty_iban,
                "counterparty_name": counterparty_name,
                "description": description,
                "sender_iban": sender_iban,
                "sender_name": sender_name,
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
                    PaymentServiceProviderDraftPaymentCreate,
                    parse_obj_as(
                        type_=PaymentServiceProviderDraftPaymentCreate,
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

    def read_payment_service_provider_draft_payment_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PaymentServiceProviderDraftPaymentRead]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentServiceProviderDraftPaymentRead]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-service-provider-draft-payment/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentServiceProviderDraftPaymentRead,
                    parse_obj_as(
                        type_=PaymentServiceProviderDraftPaymentRead,
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

    def update_payment_service_provider_draft_payment_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        amount: Amount,
        counterparty_iban: str,
        counterparty_name: str,
        description: str,
        sender_iban: str,
        sender_name: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PaymentServiceProviderDraftPaymentUpdate]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        item_id : int


        amount : Amount
            The Amount to transfer with the Payment. Must be bigger than 0.

        counterparty_iban : str
            The IBAN of the counterparty.

        counterparty_name : str
            The name of the counterparty.

        description : str
            Description of the payment.

        sender_iban : str
            The IBAN of the sender.

        sender_name : typing.Optional[str]
            The name of the sender.

        status : typing.Optional[str]
            The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PaymentServiceProviderDraftPaymentUpdate]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-service-provider-draft-payment/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "counterparty_iban": counterparty_iban,
                "counterparty_name": counterparty_name,
                "description": description,
                "sender_iban": sender_iban,
                "sender_name": sender_name,
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
                    PaymentServiceProviderDraftPaymentUpdate,
                    parse_obj_as(
                        type_=PaymentServiceProviderDraftPaymentUpdate,
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


class AsyncRawPaymentServiceProviderDraftPaymentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_payment_service_provider_draft_payment_for_user(
        self, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[PaymentServiceProviderDraftPaymentListing]]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[PaymentServiceProviderDraftPaymentListing]]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-service-provider-draft-payment",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[PaymentServiceProviderDraftPaymentListing],
                    parse_obj_as(
                        type_=typing.List[PaymentServiceProviderDraftPaymentListing],
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

    async def create_payment_service_provider_draft_payment_for_user(
        self,
        user_id: int,
        *,
        amount: Amount,
        counterparty_iban: str,
        counterparty_name: str,
        description: str,
        sender_iban: str,
        sender_name: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaymentServiceProviderDraftPaymentCreate]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        amount : Amount
            The Amount to transfer with the Payment. Must be bigger than 0.

        counterparty_iban : str
            The IBAN of the counterparty.

        counterparty_name : str
            The name of the counterparty.

        description : str
            Description of the payment.

        sender_iban : str
            The IBAN of the sender.

        sender_name : typing.Optional[str]
            The name of the sender.

        status : typing.Optional[str]
            The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentServiceProviderDraftPaymentCreate]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-service-provider-draft-payment",
            method="POST",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "counterparty_iban": counterparty_iban,
                "counterparty_name": counterparty_name,
                "description": description,
                "sender_iban": sender_iban,
                "sender_name": sender_name,
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
                    PaymentServiceProviderDraftPaymentCreate,
                    parse_obj_as(
                        type_=PaymentServiceProviderDraftPaymentCreate,
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

    async def read_payment_service_provider_draft_payment_for_user(
        self, user_id: int, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PaymentServiceProviderDraftPaymentRead]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentServiceProviderDraftPaymentRead]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-service-provider-draft-payment/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PaymentServiceProviderDraftPaymentRead,
                    parse_obj_as(
                        type_=PaymentServiceProviderDraftPaymentRead,
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

    async def update_payment_service_provider_draft_payment_for_user(
        self,
        user_id: int,
        item_id: int,
        *,
        amount: Amount,
        counterparty_iban: str,
        counterparty_name: str,
        description: str,
        sender_iban: str,
        sender_name: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PaymentServiceProviderDraftPaymentUpdate]:
        """
        Manage the PaymentServiceProviderDraftPayment's for a PISP.

        Parameters
        ----------
        user_id : int


        item_id : int


        amount : Amount
            The Amount to transfer with the Payment. Must be bigger than 0.

        counterparty_iban : str
            The IBAN of the counterparty.

        counterparty_name : str
            The name of the counterparty.

        description : str
            Description of the payment.

        sender_iban : str
            The IBAN of the sender.

        sender_name : typing.Optional[str]
            The name of the sender.

        status : typing.Optional[str]
            The new status of the Draft Payment. Can only be set to REJECTED or CANCELLED by update.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PaymentServiceProviderDraftPaymentUpdate]
            Manage the PaymentServiceProviderDraftPayment's for a PISP.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/payment-service-provider-draft-payment/{jsonable_encoder(item_id)}",
            method="PUT",
            json={
                "amount": convert_and_respect_annotation_metadata(object_=amount, annotation=Amount, direction="write"),
                "counterparty_iban": counterparty_iban,
                "counterparty_name": counterparty_name,
                "description": description,
                "sender_iban": sender_iban,
                "sender_name": sender_name,
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
                    PaymentServiceProviderDraftPaymentUpdate,
                    parse_obj_as(
                        type_=PaymentServiceProviderDraftPaymentUpdate,
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
