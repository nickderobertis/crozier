

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
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.affiliate import Affiliate
from ..types.amount import Amount
from ..types.create_reader_checkout_response import CreateReaderCheckoutResponse
from ..types.get_reader_checkout_response import GetReaderCheckoutResponse
from ..types.metadata import Metadata
from ..types.reader import Reader
from ..types.reader_id import ReaderId
from ..types.reader_name import ReaderName
from ..types.reader_pairing_code import ReaderPairingCode
from ..types.reader_payment_response import ReaderPaymentResponse
from ..types.status_response import StatusResponse
from .types.create_reader_checkout_request_aade import CreateReaderCheckoutRequestAade
from .types.create_reader_checkout_request_affiliate import CreateReaderCheckoutRequestAffiliate
from .types.create_reader_checkout_request_card_type import CreateReaderCheckoutRequestCardType
from .types.create_reader_checkout_request_total_amount import CreateReaderCheckoutRequestTotalAmount
from .types.list_readers_response import ListReadersResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawReadersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_go_reader_checkout(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        client_transaction_id: str,
        total_amount: Amount,
        affiliate: typing.Optional[Affiliate] = OMIT,
        tip_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ReaderPaymentResponse]:
        """
        Initiates a payment on the SumUp Go terminal identified by the reader ID.

        Use `client_transaction_id` as an idempotency key: retrying the request with the same value returns the result of the original payment instead of creating a duplicate.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        client_transaction_id : str
            Caller-supplied correlation identifier, used as the idempotency key.

        total_amount : Amount

        affiliate : typing.Optional[Affiliate]

        tip_amount : typing.Optional[int]
            Optional tip amount in minor units, added on top of total_amount.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReaderPaymentResponse]
            Returns the result of the payment initiated on the reader.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/go-checkout",
            method="POST",
            json={
                "affiliate": convert_and_respect_annotation_metadata(
                    object_=affiliate, annotation=Affiliate, direction="write"
                ),
                "client_transaction_id": client_transaction_id,
                "tip_amount": tip_amount,
                "total_amount": convert_and_respect_annotation_metadata(
                    object_=total_amount, annotation=Amount, direction="write"
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
                _data = typing.cast(
                    ReaderPaymentResponse,
                    parse_obj_as(
                        type_=ReaderPaymentResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def list_readers(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListReadersResponse]:
        """
        List all readers of the merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListReadersResponse]
            Returns a list Reader objects.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListReadersResponse,
                    parse_obj_as(
                        type_=ListReadersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def create_reader(
        self,
        merchant_code: str,
        *,
        pairing_code: ReaderPairingCode,
        name: ReaderName,
        metadata: typing.Optional[Metadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Reader]:
        """
        Create a new Reader for the merchant account.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        pairing_code : ReaderPairingCode

        name : ReaderName

        metadata : typing.Optional[Metadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Reader]
            Returns the Reader object if the creation succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers",
            method="POST",
            json={
                "pairing_code": pairing_code,
                "name": name,
                "metadata": metadata,
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
                    Reader,
                    parse_obj_as(
                        type_=Reader,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    def get_reader(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Reader]:
        """
        Retrieve a Reader.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        if_modified_since : typing.Optional[str]
            Return the reader only if it has been modified after the specified timestamp given in the headers.

            Timestamps are accepted in the following formats:

             - HTTP Standard: [IMF format (RFC 5322)](https://www.rfc-editor.org/rfc/rfc5322#section-3.3), sometimes also referred to as [RFC 7231](https://www.rfc-editor.org/rfc/rfc7231#section-7.1.1.1).
             - RFC 3339: Used for timestamps in JSON payloads on this API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Reader]
            Returns a Reader object for a valid identifier.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}",
            method="GET",
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Reader,
                    parse_obj_as(
                        type_=Reader,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def delete_reader(
        self, merchant_code: str, reader_id: ReaderId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a reader.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def update_reader(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        name: typing.Optional[ReaderName] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Reader]:
        """
        Updates a reader's name or metadata and returns the updated reader.

        Providing `metadata` replaces the entire metadata object; include all entries that should be retained. Omitted fields remain unchanged.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        name : typing.Optional[ReaderName]

        metadata : typing.Optional[Metadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Reader]
            Returns the updated Reader object if the update succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}",
            method="PATCH",
            json={
                "name": name,
                "metadata": metadata,
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
                    Reader,
                    parse_obj_as(
                        type_=Reader,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def create_reader_checkout(
        self,
        merchant_code: str,
        reader_id: str,
        *,
        total_amount: CreateReaderCheckoutRequestTotalAmount,
        aade: typing.Optional[CreateReaderCheckoutRequestAade] = OMIT,
        affiliate: typing.Optional[CreateReaderCheckoutRequestAffiliate] = OMIT,
        card_type: typing.Optional[CreateReaderCheckoutRequestCardType] = OMIT,
        description: typing.Optional[str] = OMIT,
        installments: typing.Optional[int] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        tip_rates: typing.Optional[typing.Sequence[float]] = OMIT,
        tip_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateReaderCheckoutResponse]:
        """
        Creates a Checkout for a Reader.

        This process is asynchronous and the actual transaction may take some time to be started on the device.


        There are some caveats when using this endpoint:
        * The target device must be online, otherwise checkout won't be accepted
        * After the checkout is accepted, the system has 60 seconds to start the payment on the target device. During this time, any other checkout for the same device will be rejected.


        **Note**: If the target device is a Solo, it must be in version 3.3.24.3 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        total_amount : CreateReaderCheckoutRequestTotalAmount
            Amount structure.

            The amount is represented as an integer value altogether with the currency and the minor unit.

            For example, EUR 1.00 is represented as value 100 with minor unit of 2.

        aade : typing.Optional[CreateReaderCheckoutRequestAade]
            Optional object containing data for transactions from ERP integrators in Greece that comply with the AADE 1155 protocol.
            When such regulatory/business requirements apply, this object must be provided and contains the data needed to validate the transaction with the AADE signature provider.

        affiliate : typing.Optional[CreateReaderCheckoutRequestAffiliate]
            Affiliate metadata for the transaction.
            It is a field that allow for integrators to track the source of the transaction.

        card_type : typing.Optional[CreateReaderCheckoutRequestCardType]
            The card type of the card used for the transaction.
            Is is required only for some countries (e.g: Brazil).

        description : typing.Optional[str]
            Description of the checkout to be shown in the Merchant Sales

        installments : typing.Optional[int]
            Number of installments for the transaction.
            It may vary according to the merchant country.
            For example, in Brazil, the maximum number of installments is 12.

            Omit if the merchant country does support installments.
            Otherwise, the checkout will be rejected.

        return_url : typing.Optional[str]
            Webhook URL to which the payment result will be sent.
            It must be a HTTPS url.

        tip_rates : typing.Optional[typing.Sequence[float]]
            List of tipping rates to be displayed to the cardholder.
            The rates are in percentage and should be between 0.01 and 0.99.
            The list should be sorted in ascending order.

        tip_timeout : typing.Optional[int]
            Time in seconds the cardholder has to select a tip rate.
            If not provided, the default value is 30 seconds.

            It can only be set if `tip_rates` is provided.

            **Note**: If the target device is a Solo, it must be in version 3.3.38.0 or higher.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateReaderCheckoutResponse]
            The Checkout got successfully created for the given reader.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/checkout",
            method="POST",
            json={
                "aade": convert_and_respect_annotation_metadata(
                    object_=aade, annotation=CreateReaderCheckoutRequestAade, direction="write"
                ),
                "affiliate": convert_and_respect_annotation_metadata(
                    object_=affiliate,
                    annotation=typing.Optional[CreateReaderCheckoutRequestAffiliate],
                    direction="write",
                ),
                "card_type": card_type,
                "description": description,
                "installments": installments,
                "return_url": return_url,
                "tip_rates": tip_rates,
                "tip_timeout": tip_timeout,
                "total_amount": convert_and_respect_annotation_metadata(
                    object_=total_amount, annotation=CreateReaderCheckoutRequestTotalAmount, direction="write"
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
                _data = typing.cast(
                    CreateReaderCheckoutResponse,
                    parse_obj_as(
                        type_=CreateReaderCheckoutResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_reader_status(
        self, merchant_code: str, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StatusResponse]:
        """
        Provides the last known status for a Reader.

        This endpoint allows you to retrieve updates from the connected card reader, including the current screen being displayed during the payment process and the device status (battery level, connectivity, and update state).

        Supported States

        * `IDLE` – Reader ready for next transaction
        * `SELECTING_TIP` – Waiting for tip input
        * `WAITING_FOR_CARD` – Awaiting card insert/tap
        * `WAITING_FOR_PIN` – Waiting for PIN entry
        * `WAITING_FOR_SIGNATURE` – Waiting for customer signature
        * `UPDATING_FIRMWARE` – Firmware update in progress

        Device Status

        * `ONLINE` – Device connected and operational
        * `OFFLINE` – Device disconnected (last state persisted)

        **Note**: If the target device is a Solo, it must be in version 3.3.39.0 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StatusResponse]
            Response with the device status.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StatusResponse,
                    parse_obj_as(
                        type_=StatusResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    def create_reader_terminate(
        self, merchant_code: str, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Terminate a Reader Checkout stops the current transaction on the target device.

        This process is asynchronous and the actual termination may take some time to be performed on the device.


        There are some caveats when using this endpoint:
        * The target device must be online, otherwise terminate won't be accepted
        * The action will succeed only if the device is waiting for cardholder action: e.g: waiting for card, waiting for PIN, etc.
        * There is no confirmation of the termination.

        If a transaction is successfully terminated and `return_url` was provided on Checkout, the transaction status will be sent as `failed` to the provided URL.


        **Note**: If the target device is a Solo, it must be in version 3.3.28.0 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            The Terminate action was successfully dispatched for the given reader.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/terminate",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    def get_reader_checkout(
        self,
        merchant_code: str,
        reader_id: str,
        checkout_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetReaderCheckoutResponse]:
        """
        Get a Checkout for a Reader.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        checkout_id : str
            The unique identifier of the Checkout

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetReaderCheckoutResponse]
            The Checkout got successfully retrieved for the given reader.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/checkout/{encode_path_param(checkout_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetReaderCheckoutResponse,
                    parse_obj_as(
                        type_=GetReaderCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawReadersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_go_reader_checkout(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        client_transaction_id: str,
        total_amount: Amount,
        affiliate: typing.Optional[Affiliate] = OMIT,
        tip_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ReaderPaymentResponse]:
        """
        Initiates a payment on the SumUp Go terminal identified by the reader ID.

        Use `client_transaction_id` as an idempotency key: retrying the request with the same value returns the result of the original payment instead of creating a duplicate.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        client_transaction_id : str
            Caller-supplied correlation identifier, used as the idempotency key.

        total_amount : Amount

        affiliate : typing.Optional[Affiliate]

        tip_amount : typing.Optional[int]
            Optional tip amount in minor units, added on top of total_amount.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReaderPaymentResponse]
            Returns the result of the payment initiated on the reader.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/go-checkout",
            method="POST",
            json={
                "affiliate": convert_and_respect_annotation_metadata(
                    object_=affiliate, annotation=Affiliate, direction="write"
                ),
                "client_transaction_id": client_transaction_id,
                "tip_amount": tip_amount,
                "total_amount": convert_and_respect_annotation_metadata(
                    object_=total_amount, annotation=Amount, direction="write"
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
                _data = typing.cast(
                    ReaderPaymentResponse,
                    parse_obj_as(
                        type_=ReaderPaymentResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def list_readers(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListReadersResponse]:
        """
        List all readers of the merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListReadersResponse]
            Returns a list Reader objects.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListReadersResponse,
                    parse_obj_as(
                        type_=ListReadersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def create_reader(
        self,
        merchant_code: str,
        *,
        pairing_code: ReaderPairingCode,
        name: ReaderName,
        metadata: typing.Optional[Metadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Reader]:
        """
        Create a new Reader for the merchant account.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        pairing_code : ReaderPairingCode

        name : ReaderName

        metadata : typing.Optional[Metadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Reader]
            Returns the Reader object if the creation succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers",
            method="POST",
            json={
                "pairing_code": pairing_code,
                "name": name,
                "metadata": metadata,
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
                    Reader,
                    parse_obj_as(
                        type_=Reader,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
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

    async def get_reader(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Reader]:
        """
        Retrieve a Reader.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        if_modified_since : typing.Optional[str]
            Return the reader only if it has been modified after the specified timestamp given in the headers.

            Timestamps are accepted in the following formats:

             - HTTP Standard: [IMF format (RFC 5322)](https://www.rfc-editor.org/rfc/rfc5322#section-3.3), sometimes also referred to as [RFC 7231](https://www.rfc-editor.org/rfc/rfc7231#section-7.1.1.1).
             - RFC 3339: Used for timestamps in JSON payloads on this API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Reader]
            Returns a Reader object for a valid identifier.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}",
            method="GET",
            headers={
                "If-Modified-Since": str(if_modified_since) if if_modified_since is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Reader,
                    parse_obj_as(
                        type_=Reader,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def delete_reader(
        self, merchant_code: str, reader_id: ReaderId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a reader.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def update_reader(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        name: typing.Optional[ReaderName] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Reader]:
        """
        Updates a reader's name or metadata and returns the updated reader.

        Providing `metadata` replaces the entire metadata object; include all entries that should be retained. Omitted fields remain unchanged.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        name : typing.Optional[ReaderName]

        metadata : typing.Optional[Metadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Reader]
            Returns the updated Reader object if the update succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}",
            method="PATCH",
            json={
                "name": name,
                "metadata": metadata,
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
                    Reader,
                    parse_obj_as(
                        type_=Reader,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def create_reader_checkout(
        self,
        merchant_code: str,
        reader_id: str,
        *,
        total_amount: CreateReaderCheckoutRequestTotalAmount,
        aade: typing.Optional[CreateReaderCheckoutRequestAade] = OMIT,
        affiliate: typing.Optional[CreateReaderCheckoutRequestAffiliate] = OMIT,
        card_type: typing.Optional[CreateReaderCheckoutRequestCardType] = OMIT,
        description: typing.Optional[str] = OMIT,
        installments: typing.Optional[int] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        tip_rates: typing.Optional[typing.Sequence[float]] = OMIT,
        tip_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateReaderCheckoutResponse]:
        """
        Creates a Checkout for a Reader.

        This process is asynchronous and the actual transaction may take some time to be started on the device.


        There are some caveats when using this endpoint:
        * The target device must be online, otherwise checkout won't be accepted
        * After the checkout is accepted, the system has 60 seconds to start the payment on the target device. During this time, any other checkout for the same device will be rejected.


        **Note**: If the target device is a Solo, it must be in version 3.3.24.3 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        total_amount : CreateReaderCheckoutRequestTotalAmount
            Amount structure.

            The amount is represented as an integer value altogether with the currency and the minor unit.

            For example, EUR 1.00 is represented as value 100 with minor unit of 2.

        aade : typing.Optional[CreateReaderCheckoutRequestAade]
            Optional object containing data for transactions from ERP integrators in Greece that comply with the AADE 1155 protocol.
            When such regulatory/business requirements apply, this object must be provided and contains the data needed to validate the transaction with the AADE signature provider.

        affiliate : typing.Optional[CreateReaderCheckoutRequestAffiliate]
            Affiliate metadata for the transaction.
            It is a field that allow for integrators to track the source of the transaction.

        card_type : typing.Optional[CreateReaderCheckoutRequestCardType]
            The card type of the card used for the transaction.
            Is is required only for some countries (e.g: Brazil).

        description : typing.Optional[str]
            Description of the checkout to be shown in the Merchant Sales

        installments : typing.Optional[int]
            Number of installments for the transaction.
            It may vary according to the merchant country.
            For example, in Brazil, the maximum number of installments is 12.

            Omit if the merchant country does support installments.
            Otherwise, the checkout will be rejected.

        return_url : typing.Optional[str]
            Webhook URL to which the payment result will be sent.
            It must be a HTTPS url.

        tip_rates : typing.Optional[typing.Sequence[float]]
            List of tipping rates to be displayed to the cardholder.
            The rates are in percentage and should be between 0.01 and 0.99.
            The list should be sorted in ascending order.

        tip_timeout : typing.Optional[int]
            Time in seconds the cardholder has to select a tip rate.
            If not provided, the default value is 30 seconds.

            It can only be set if `tip_rates` is provided.

            **Note**: If the target device is a Solo, it must be in version 3.3.38.0 or higher.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateReaderCheckoutResponse]
            The Checkout got successfully created for the given reader.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/checkout",
            method="POST",
            json={
                "aade": convert_and_respect_annotation_metadata(
                    object_=aade, annotation=CreateReaderCheckoutRequestAade, direction="write"
                ),
                "affiliate": convert_and_respect_annotation_metadata(
                    object_=affiliate,
                    annotation=typing.Optional[CreateReaderCheckoutRequestAffiliate],
                    direction="write",
                ),
                "card_type": card_type,
                "description": description,
                "installments": installments,
                "return_url": return_url,
                "tip_rates": tip_rates,
                "tip_timeout": tip_timeout,
                "total_amount": convert_and_respect_annotation_metadata(
                    object_=total_amount, annotation=CreateReaderCheckoutRequestTotalAmount, direction="write"
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
                _data = typing.cast(
                    CreateReaderCheckoutResponse,
                    parse_obj_as(
                        type_=CreateReaderCheckoutResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_reader_status(
        self, merchant_code: str, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StatusResponse]:
        """
        Provides the last known status for a Reader.

        This endpoint allows you to retrieve updates from the connected card reader, including the current screen being displayed during the payment process and the device status (battery level, connectivity, and update state).

        Supported States

        * `IDLE` – Reader ready for next transaction
        * `SELECTING_TIP` – Waiting for tip input
        * `WAITING_FOR_CARD` – Awaiting card insert/tap
        * `WAITING_FOR_PIN` – Waiting for PIN entry
        * `WAITING_FOR_SIGNATURE` – Waiting for customer signature
        * `UPDATING_FIRMWARE` – Firmware update in progress

        Device Status

        * `ONLINE` – Device connected and operational
        * `OFFLINE` – Device disconnected (last state persisted)

        **Note**: If the target device is a Solo, it must be in version 3.3.39.0 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StatusResponse]
            Response with the device status.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StatusResponse,
                    parse_obj_as(
                        type_=StatusResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def create_reader_terminate(
        self, merchant_code: str, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Terminate a Reader Checkout stops the current transaction on the target device.

        This process is asynchronous and the actual termination may take some time to be performed on the device.


        There are some caveats when using this endpoint:
        * The target device must be online, otherwise terminate won't be accepted
        * The action will succeed only if the device is waiting for cardholder action: e.g: waiting for card, waiting for PIN, etc.
        * There is no confirmation of the termination.

        If a transaction is successfully terminated and `return_url` was provided on Checkout, the transaction status will be sent as `failed` to the provided URL.


        **Note**: If the target device is a Solo, it must be in version 3.3.28.0 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            The Terminate action was successfully dispatched for the given reader.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/terminate",
            method="POST",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
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

    async def get_reader_checkout(
        self,
        merchant_code: str,
        reader_id: str,
        checkout_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetReaderCheckoutResponse]:
        """
        Get a Checkout for a Reader.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        checkout_id : str
            The unique identifier of the Checkout

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetReaderCheckoutResponse]
            The Checkout got successfully retrieved for the given reader.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0.1/merchants/{encode_path_param(merchant_code)}/readers/{encode_path_param(reader_id)}/checkout/{encode_path_param(checkout_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetReaderCheckoutResponse,
                    parse_obj_as(
                        type_=GetReaderCheckoutResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
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
