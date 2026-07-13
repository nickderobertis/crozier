

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
from ..types.ideal_merchant_transaction_create import IdealMerchantTransactionCreate
from ..types.ideal_merchant_transaction_listing import IdealMerchantTransactionListing
from ..types.ideal_merchant_transaction_read import IdealMerchantTransactionRead
from ..types.label_monetary_account import LabelMonetaryAccount


OMIT = typing.cast(typing.Any, ...)


class RawIdealMerchantTransactionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_ideal_merchant_transaction_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[IdealMerchantTransactionListing]]:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[IdealMerchantTransactionListing]]
            View for requesting iDEAL transactions and polling their status.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[IdealMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[IdealMerchantTransactionListing],
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

    def create_ideal_merchant_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_guaranteed: typing.Optional[Amount] = OMIT,
        amount_requested: typing.Optional[Amount] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        expiration: typing.Optional[str] = OMIT,
        issuer: typing.Optional[str] = OMIT,
        issuer_authentication_url: typing.Optional[str] = OMIT,
        issuer_name: typing.Optional[str] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        purchase_identifier: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_timestamp: typing.Optional[str] = OMIT,
        transaction_identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IdealMerchantTransactionCreate]:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        alias : typing.Optional[LabelMonetaryAccount]
            The alias of the monetary account to add money to.

        amount_guaranteed : typing.Optional[Amount]
            In case of a successful transaction, the amount of money that will be transferred.

        amount_requested : typing.Optional[Amount]
            The requested amount of money to add.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The alias of the monetary account the money comes from.

        expiration : typing.Optional[str]
            When the transaction will expire.

        issuer : typing.Optional[str]
            The BIC of the issuer.

        issuer_authentication_url : typing.Optional[str]
            The URL to visit to

        issuer_name : typing.Optional[str]
            The Name of the issuer.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account this ideal merchant transaction links to.

        purchase_identifier : typing.Optional[str]
            The 'purchase ID' of the iDEAL transaction.

        status : typing.Optional[str]
            The status of the transaction.

        status_timestamp : typing.Optional[str]
            When the status was last updated.

        transaction_identifier : typing.Optional[str]
            The 'transaction ID' of the iDEAL transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IdealMerchantTransactionCreate]
            View for requesting iDEAL transactions and polling their status.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id_)}/ideal-merchant-transaction",
            method="POST",
            json={
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "amount_guaranteed": convert_and_respect_annotation_metadata(
                    object_=amount_guaranteed, annotation=Amount, direction="write"
                ),
                "amount_requested": convert_and_respect_annotation_metadata(
                    object_=amount_requested, annotation=Amount, direction="write"
                ),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "expiration": expiration,
                "issuer": issuer,
                "issuer_authentication_url": issuer_authentication_url,
                "issuer_name": issuer_name,
                "monetary_account_id": monetary_account_id,
                "purchase_identifier": purchase_identifier,
                "status": status,
                "status_timestamp": status_timestamp,
                "transaction_identifier": transaction_identifier,
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
                    IdealMerchantTransactionCreate,
                    parse_obj_as(
                        type_=IdealMerchantTransactionCreate,
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

    def read_ideal_merchant_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IdealMerchantTransactionRead]:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IdealMerchantTransactionRead]
            View for requesting iDEAL transactions and polling their status.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IdealMerchantTransactionRead,
                    parse_obj_as(
                        type_=IdealMerchantTransactionRead,
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


class AsyncRawIdealMerchantTransactionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_ideal_merchant_transaction_for_user_monetary_account(
        self, user_id: int, monetary_account_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[IdealMerchantTransactionListing]]:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[IdealMerchantTransactionListing]]
            View for requesting iDEAL transactions and polling their status.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[IdealMerchantTransactionListing],
                    parse_obj_as(
                        type_=typing.List[IdealMerchantTransactionListing],
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

    async def create_ideal_merchant_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id_: int,
        *,
        alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        amount_guaranteed: typing.Optional[Amount] = OMIT,
        amount_requested: typing.Optional[Amount] = OMIT,
        counterparty_alias: typing.Optional[LabelMonetaryAccount] = OMIT,
        expiration: typing.Optional[str] = OMIT,
        issuer: typing.Optional[str] = OMIT,
        issuer_authentication_url: typing.Optional[str] = OMIT,
        issuer_name: typing.Optional[str] = OMIT,
        monetary_account_id: typing.Optional[int] = OMIT,
        purchase_identifier: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        status_timestamp: typing.Optional[str] = OMIT,
        transaction_identifier: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IdealMerchantTransactionCreate]:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id_ : int


        alias : typing.Optional[LabelMonetaryAccount]
            The alias of the monetary account to add money to.

        amount_guaranteed : typing.Optional[Amount]
            In case of a successful transaction, the amount of money that will be transferred.

        amount_requested : typing.Optional[Amount]
            The requested amount of money to add.

        counterparty_alias : typing.Optional[LabelMonetaryAccount]
            The alias of the monetary account the money comes from.

        expiration : typing.Optional[str]
            When the transaction will expire.

        issuer : typing.Optional[str]
            The BIC of the issuer.

        issuer_authentication_url : typing.Optional[str]
            The URL to visit to

        issuer_name : typing.Optional[str]
            The Name of the issuer.

        monetary_account_id : typing.Optional[int]
            The id of the monetary account this ideal merchant transaction links to.

        purchase_identifier : typing.Optional[str]
            The 'purchase ID' of the iDEAL transaction.

        status : typing.Optional[str]
            The status of the transaction.

        status_timestamp : typing.Optional[str]
            When the status was last updated.

        transaction_identifier : typing.Optional[str]
            The 'transaction ID' of the iDEAL transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IdealMerchantTransactionCreate]
            View for requesting iDEAL transactions and polling their status.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id_)}/ideal-merchant-transaction",
            method="POST",
            json={
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "amount_guaranteed": convert_and_respect_annotation_metadata(
                    object_=amount_guaranteed, annotation=Amount, direction="write"
                ),
                "amount_requested": convert_and_respect_annotation_metadata(
                    object_=amount_requested, annotation=Amount, direction="write"
                ),
                "counterparty_alias": convert_and_respect_annotation_metadata(
                    object_=counterparty_alias, annotation=LabelMonetaryAccount, direction="write"
                ),
                "expiration": expiration,
                "issuer": issuer,
                "issuer_authentication_url": issuer_authentication_url,
                "issuer_name": issuer_name,
                "monetary_account_id": monetary_account_id,
                "purchase_identifier": purchase_identifier,
                "status": status,
                "status_timestamp": status_timestamp,
                "transaction_identifier": transaction_identifier,
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
                    IdealMerchantTransactionCreate,
                    parse_obj_as(
                        type_=IdealMerchantTransactionCreate,
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

    async def read_ideal_merchant_transaction_for_user_monetary_account(
        self,
        user_id: int,
        monetary_account_id: int,
        item_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IdealMerchantTransactionRead]:
        """
        View for requesting iDEAL transactions and polling their status.

        Parameters
        ----------
        user_id : int


        monetary_account_id : int


        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IdealMerchantTransactionRead]
            View for requesting iDEAL transactions and polling their status.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user/{jsonable_encoder(user_id)}/monetary-account/{jsonable_encoder(monetary_account_id)}/ideal-merchant-transaction/{jsonable_encoder(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    IdealMerchantTransactionRead,
                    parse_obj_as(
                        type_=IdealMerchantTransactionRead,
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
