

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
from ..types.create_wallet_payment_price_dollars import CreateWalletPaymentPriceDollars
from ..types.envelope_get_wallet_auto_recharge import EnvelopeGetWalletAutoRecharge
from ..types.envelope_list_payment_method_get import EnvelopeListPaymentMethodGet
from ..types.envelope_list_wallet_get_with_available_credits import EnvelopeListWalletGetWithAvailableCredits
from ..types.envelope_list_wallet_group_get import EnvelopeListWalletGroupGet
from ..types.envelope_payment_method_get import EnvelopePaymentMethodGet
from ..types.envelope_payment_method_initiated import EnvelopePaymentMethodInitiated
from ..types.envelope_wallet_get import EnvelopeWalletGet
from ..types.envelope_wallet_get_with_available_credits import EnvelopeWalletGetWithAvailableCredits
from ..types.envelope_wallet_group_get import EnvelopeWalletGroupGet
from ..types.envelope_wallet_payment_initiated import EnvelopeWalletPaymentInitiated
from ..types.group_id_int import GroupIdInt
from ..types.page_payment_transaction import PagePaymentTransaction
from ..types.wallet_id_int import WalletIdInt
from ..types.wallet_status import WalletStatus
from .types.replace_wallet_auto_recharge_monthly_limit_in_usd import ReplaceWalletAutoRechargeMonthlyLimitInUsd
from .types.replace_wallet_auto_recharge_top_up_amount_in_usd import ReplaceWalletAutoRechargeTopUpAmountInUsd
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWalletsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListWalletGetWithAvailableCredits]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListWalletGetWithAvailableCredits]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/wallets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListWalletGetWithAvailableCredits,
                    parse_obj_as(
                        type_=EnvelopeListWalletGetWithAvailableCredits,
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

    def create_wallet(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeWalletGet]:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeWalletGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/wallets",
            method="POST",
            json={
                "name": name,
                "description": description,
                "thumbnail": thumbnail,
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
                    EnvelopeWalletGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGet,
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

    def get_default_wallet(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeWalletGetWithAvailableCredits]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeWalletGetWithAvailableCredits]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/wallets/default",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeWalletGetWithAvailableCredits,
                    parse_obj_as(
                        type_=EnvelopeWalletGetWithAvailableCredits,
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

    def get_wallet(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeWalletGetWithAvailableCredits]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeWalletGetWithAvailableCredits]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeWalletGetWithAvailableCredits,
                    parse_obj_as(
                        type_=EnvelopeWalletGetWithAvailableCredits,
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

    def update_wallet(
        self,
        wallet_id: WalletIdInt,
        *,
        name: str,
        status: WalletStatus,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeWalletGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        name : str

        status : WalletStatus

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeWalletGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}",
            method="PUT",
            json={
                "name": name,
                "description": description,
                "thumbnail": thumbnail,
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
                    EnvelopeWalletGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGet,
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

    def create_payment(
        self,
        wallet_id: WalletIdInt,
        *,
        price_dollars: CreateWalletPaymentPriceDollars,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeWalletPaymentInitiated]:
        """
        Creates payment to wallet `wallet_id`

        Parameters
        ----------
        wallet_id : WalletIdInt

        price_dollars : CreateWalletPaymentPriceDollars

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeWalletPaymentInitiated]
            Payment initialized
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments",
            method="POST",
            json={
                "priceDollars": convert_and_respect_annotation_metadata(
                    object_=price_dollars, annotation=CreateWalletPaymentPriceDollars, direction="write"
                ),
                "comment": comment,
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
                    EnvelopeWalletPaymentInitiated,
                    parse_obj_as(
                        type_=EnvelopeWalletPaymentInitiated,
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

    def list_all_payments(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PagePaymentTransaction]:
        """
        Lists all user payments to his/her wallets (only the ones he/she created)

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PagePaymentTransaction]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/wallets/-/payments",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagePaymentTransaction,
                    parse_obj_as(
                        type_=PagePaymentTransaction,
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

    def get_payment_invoice_link(
        self, wallet_id: WalletIdInt, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments/{encode_path_param(payment_id)}/invoice-link",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def cancel_payment(
        self, wallet_id: WalletIdInt, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments/{encode_path_param(payment_id)}:cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def init_creation_of_payment_method(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopePaymentMethodInitiated]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePaymentMethodInitiated]
            Successfully initialized
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods:init",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePaymentMethodInitiated,
                    parse_obj_as(
                        type_=EnvelopePaymentMethodInitiated,
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

    def cancel_creation_of_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods/{encode_path_param(payment_method_id)}:cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_payments_methods(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListPaymentMethodGet]:
        """
        Lists all payments method associated to `wallet_id`

        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListPaymentMethodGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListPaymentMethodGet,
                    parse_obj_as(
                        type_=EnvelopeListPaymentMethodGet,
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

    def get_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopePaymentMethodGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePaymentMethodGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods/{encode_path_param(payment_method_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePaymentMethodGet,
                    parse_obj_as(
                        type_=EnvelopePaymentMethodGet,
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

    def delete_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods/{encode_path_param(payment_method_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def pay_with_payment_method(
        self,
        wallet_id: WalletIdInt,
        payment_method_id: str,
        *,
        price_dollars: CreateWalletPaymentPriceDollars,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeWalletPaymentInitiated]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        price_dollars : CreateWalletPaymentPriceDollars

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeWalletPaymentInitiated]
            Pay with payment-method
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods/{encode_path_param(payment_method_id)}:pay",
            method="POST",
            json={
                "priceDollars": convert_and_respect_annotation_metadata(
                    object_=price_dollars, annotation=CreateWalletPaymentPriceDollars, direction="write"
                ),
                "comment": comment,
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
                    EnvelopeWalletPaymentInitiated,
                    parse_obj_as(
                        type_=EnvelopeWalletPaymentInitiated,
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

    def get_wallet_autorecharge(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeGetWalletAutoRecharge]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeGetWalletAutoRecharge]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/auto-recharge",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGetWalletAutoRecharge,
                    parse_obj_as(
                        type_=EnvelopeGetWalletAutoRecharge,
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

    def replace_wallet_autorecharge(
        self,
        wallet_id: WalletIdInt,
        *,
        enabled: bool,
        payment_method_id: str,
        top_up_amount_in_usd: ReplaceWalletAutoRechargeTopUpAmountInUsd,
        monthly_limit_in_usd: typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeGetWalletAutoRecharge]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        enabled : bool

        payment_method_id : str

        top_up_amount_in_usd : ReplaceWalletAutoRechargeTopUpAmountInUsd

        monthly_limit_in_usd : typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeGetWalletAutoRecharge]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/auto-recharge",
            method="PUT",
            json={
                "enabled": enabled,
                "paymentMethodId": payment_method_id,
                "topUpAmountInUsd": convert_and_respect_annotation_metadata(
                    object_=top_up_amount_in_usd,
                    annotation=ReplaceWalletAutoRechargeTopUpAmountInUsd,
                    direction="write",
                ),
                "monthlyLimitInUsd": convert_and_respect_annotation_metadata(
                    object_=monthly_limit_in_usd,
                    annotation=typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd],
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
                _data = typing.cast(
                    EnvelopeGetWalletAutoRecharge,
                    parse_obj_as(
                        type_=EnvelopeGetWalletAutoRecharge,
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

    def create_wallet_group(
        self,
        wallet_id: WalletIdInt,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeWalletGroupGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeWalletGroupGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/groups/{encode_path_param(group_id)}",
            method="POST",
            json={
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeWalletGroupGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGroupGet,
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

    def update_wallet_group(
        self,
        wallet_id: WalletIdInt,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeWalletGroupGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeWalletGroupGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/groups/{encode_path_param(group_id)}",
            method="PUT",
            json={
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeWalletGroupGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGroupGet,
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

    def delete_wallet_group(
        self, wallet_id: WalletIdInt, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_wallet_groups(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListWalletGroupGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListWalletGroupGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListWalletGroupGet,
                    parse_obj_as(
                        type_=EnvelopeListWalletGroupGet,
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


class AsyncRawWalletsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_wallets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListWalletGetWithAvailableCredits]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListWalletGetWithAvailableCredits]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/wallets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListWalletGetWithAvailableCredits,
                    parse_obj_as(
                        type_=EnvelopeListWalletGetWithAvailableCredits,
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

    async def create_wallet(
        self,
        *,
        name: str,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeWalletGet]:
        """
        Parameters
        ----------
        name : str

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeWalletGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/wallets",
            method="POST",
            json={
                "name": name,
                "description": description,
                "thumbnail": thumbnail,
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
                    EnvelopeWalletGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGet,
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

    async def get_default_wallet(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeWalletGetWithAvailableCredits]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeWalletGetWithAvailableCredits]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/wallets/default",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeWalletGetWithAvailableCredits,
                    parse_obj_as(
                        type_=EnvelopeWalletGetWithAvailableCredits,
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

    async def get_wallet(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeWalletGetWithAvailableCredits]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeWalletGetWithAvailableCredits]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeWalletGetWithAvailableCredits,
                    parse_obj_as(
                        type_=EnvelopeWalletGetWithAvailableCredits,
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

    async def update_wallet(
        self,
        wallet_id: WalletIdInt,
        *,
        name: str,
        status: WalletStatus,
        description: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeWalletGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        name : str

        status : WalletStatus

        description : typing.Optional[str]

        thumbnail : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeWalletGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}",
            method="PUT",
            json={
                "name": name,
                "description": description,
                "thumbnail": thumbnail,
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
                    EnvelopeWalletGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGet,
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

    async def create_payment(
        self,
        wallet_id: WalletIdInt,
        *,
        price_dollars: CreateWalletPaymentPriceDollars,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeWalletPaymentInitiated]:
        """
        Creates payment to wallet `wallet_id`

        Parameters
        ----------
        wallet_id : WalletIdInt

        price_dollars : CreateWalletPaymentPriceDollars

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeWalletPaymentInitiated]
            Payment initialized
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments",
            method="POST",
            json={
                "priceDollars": convert_and_respect_annotation_metadata(
                    object_=price_dollars, annotation=CreateWalletPaymentPriceDollars, direction="write"
                ),
                "comment": comment,
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
                    EnvelopeWalletPaymentInitiated,
                    parse_obj_as(
                        type_=EnvelopeWalletPaymentInitiated,
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

    async def list_all_payments(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PagePaymentTransaction]:
        """
        Lists all user payments to his/her wallets (only the ones he/she created)

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PagePaymentTransaction]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/wallets/-/payments",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PagePaymentTransaction,
                    parse_obj_as(
                        type_=PagePaymentTransaction,
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

    async def get_payment_invoice_link(
        self, wallet_id: WalletIdInt, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments/{encode_path_param(payment_id)}/invoice-link",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def cancel_payment(
        self, wallet_id: WalletIdInt, payment_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments/{encode_path_param(payment_id)}:cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def init_creation_of_payment_method(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopePaymentMethodInitiated]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePaymentMethodInitiated]
            Successfully initialized
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods:init",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePaymentMethodInitiated,
                    parse_obj_as(
                        type_=EnvelopePaymentMethodInitiated,
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

    async def cancel_creation_of_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods/{encode_path_param(payment_method_id)}:cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_payments_methods(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListPaymentMethodGet]:
        """
        Lists all payments method associated to `wallet_id`

        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListPaymentMethodGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListPaymentMethodGet,
                    parse_obj_as(
                        type_=EnvelopeListPaymentMethodGet,
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

    async def get_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopePaymentMethodGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePaymentMethodGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods/{encode_path_param(payment_method_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePaymentMethodGet,
                    parse_obj_as(
                        type_=EnvelopePaymentMethodGet,
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

    async def delete_payment_method(
        self, wallet_id: WalletIdInt, payment_method_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods/{encode_path_param(payment_method_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def pay_with_payment_method(
        self,
        wallet_id: WalletIdInt,
        payment_method_id: str,
        *,
        price_dollars: CreateWalletPaymentPriceDollars,
        comment: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeWalletPaymentInitiated]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        payment_method_id : str

        price_dollars : CreateWalletPaymentPriceDollars

        comment : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeWalletPaymentInitiated]
            Pay with payment-method
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/payments-methods/{encode_path_param(payment_method_id)}:pay",
            method="POST",
            json={
                "priceDollars": convert_and_respect_annotation_metadata(
                    object_=price_dollars, annotation=CreateWalletPaymentPriceDollars, direction="write"
                ),
                "comment": comment,
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
                    EnvelopeWalletPaymentInitiated,
                    parse_obj_as(
                        type_=EnvelopeWalletPaymentInitiated,
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

    async def get_wallet_autorecharge(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeGetWalletAutoRecharge]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeGetWalletAutoRecharge]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/auto-recharge",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeGetWalletAutoRecharge,
                    parse_obj_as(
                        type_=EnvelopeGetWalletAutoRecharge,
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

    async def replace_wallet_autorecharge(
        self,
        wallet_id: WalletIdInt,
        *,
        enabled: bool,
        payment_method_id: str,
        top_up_amount_in_usd: ReplaceWalletAutoRechargeTopUpAmountInUsd,
        monthly_limit_in_usd: typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeGetWalletAutoRecharge]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        enabled : bool

        payment_method_id : str

        top_up_amount_in_usd : ReplaceWalletAutoRechargeTopUpAmountInUsd

        monthly_limit_in_usd : typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeGetWalletAutoRecharge]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/auto-recharge",
            method="PUT",
            json={
                "enabled": enabled,
                "paymentMethodId": payment_method_id,
                "topUpAmountInUsd": convert_and_respect_annotation_metadata(
                    object_=top_up_amount_in_usd,
                    annotation=ReplaceWalletAutoRechargeTopUpAmountInUsd,
                    direction="write",
                ),
                "monthlyLimitInUsd": convert_and_respect_annotation_metadata(
                    object_=monthly_limit_in_usd,
                    annotation=typing.Optional[ReplaceWalletAutoRechargeMonthlyLimitInUsd],
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
                _data = typing.cast(
                    EnvelopeGetWalletAutoRecharge,
                    parse_obj_as(
                        type_=EnvelopeGetWalletAutoRecharge,
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

    async def create_wallet_group(
        self,
        wallet_id: WalletIdInt,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeWalletGroupGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeWalletGroupGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/groups/{encode_path_param(group_id)}",
            method="POST",
            json={
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeWalletGroupGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGroupGet,
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

    async def update_wallet_group(
        self,
        wallet_id: WalletIdInt,
        group_id: GroupIdInt,
        *,
        read: bool,
        write: bool,
        delete: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeWalletGroupGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        read : bool

        write : bool

        delete : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeWalletGroupGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/groups/{encode_path_param(group_id)}",
            method="PUT",
            json={
                "read": read,
                "write": write,
                "delete": delete,
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
                    EnvelopeWalletGroupGet,
                    parse_obj_as(
                        type_=EnvelopeWalletGroupGet,
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

    async def delete_wallet_group(
        self, wallet_id: WalletIdInt, group_id: GroupIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        group_id : GroupIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/groups/{encode_path_param(group_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_wallet_groups(
        self, wallet_id: WalletIdInt, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListWalletGroupGet]:
        """
        Parameters
        ----------
        wallet_id : WalletIdInt

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListWalletGroupGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/wallets/{encode_path_param(wallet_id)}/groups",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListWalletGroupGet,
                    parse_obj_as(
                        type_=EnvelopeListWalletGroupGet,
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
