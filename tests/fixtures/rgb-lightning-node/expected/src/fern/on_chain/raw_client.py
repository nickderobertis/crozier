

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.address_response import AddressResponse
from ..types.btc_balance_response import BtcBalanceResponse
from ..types.estimate_fee_response import EstimateFeeResponse
from ..types.list_transactions_response import ListTransactionsResponse
from ..types.list_unspents_response import ListUnspentsResponse
from ..types.send_btc_response import SendBtcResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawOnChainClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_a_bitcoin_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AddressResponse]:
        """
        Get a new Bitcoin address from the internal BDK wallet

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddressResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "address",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddressResponse,
                    parse_obj_as(
                        type_=AddressResponse,
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

    def get_the_btc_balance(
        self, *, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BtcBalanceResponse]:
        """
        Get the node's bitcoin balance for the vanilla and colored wallets

        Parameters
        ----------
        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BtcBalanceResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "btcbalance",
            method="POST",
            json={
                "skip_sync": skip_sync,
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
                    BtcBalanceResponse,
                    parse_obj_as(
                        type_=BtcBalanceResponse,
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

    def get_fee_estimation(
        self, *, blocks: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EstimateFeeResponse]:
        """
        Get on-chain fee estimation

        Parameters
        ----------
        blocks : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EstimateFeeResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "estimatefee",
            method="POST",
            json={
                "blocks": blocks,
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
                    EstimateFeeResponse,
                    parse_obj_as(
                        type_=EstimateFeeResponse,
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

    def list_transactions(
        self, *, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListTransactionsResponse]:
        """
        List the node's on-chain transactions

        Parameters
        ----------
        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTransactionsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "listtransactions",
            method="POST",
            json={
                "skip_sync": skip_sync,
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
                    ListTransactionsResponse,
                    parse_obj_as(
                        type_=ListTransactionsResponse,
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

    def list_unspents(
        self, *, settled_only: bool, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListUnspentsResponse]:
        """
        List the unspent outputs of the internal BDK wallet

        Parameters
        ----------
        settled_only : bool

        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListUnspentsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "listunspents",
            method="POST",
            json={
                "settled_only": settled_only,
                "skip_sync": skip_sync,
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
                    ListUnspentsResponse,
                    parse_obj_as(
                        type_=ListUnspentsResponse,
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

    def send_btc(
        self,
        *,
        amount: int,
        address: str,
        fee_rate: int,
        skip_sync: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SendBtcResponse]:
        """
        Send bitcoins on-chain

        Parameters
        ----------
        amount : int

        address : str

        fee_rate : int

        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SendBtcResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "sendbtc",
            method="POST",
            json={
                "amount": amount,
                "address": address,
                "fee_rate": fee_rate,
                "skip_sync": skip_sync,
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
                    SendBtcResponse,
                    parse_obj_as(
                        type_=SendBtcResponse,
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


class AsyncRawOnChainClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_a_bitcoin_address(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AddressResponse]:
        """
        Get a new Bitcoin address from the internal BDK wallet

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddressResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "address",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AddressResponse,
                    parse_obj_as(
                        type_=AddressResponse,
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

    async def get_the_btc_balance(
        self, *, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BtcBalanceResponse]:
        """
        Get the node's bitcoin balance for the vanilla and colored wallets

        Parameters
        ----------
        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BtcBalanceResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "btcbalance",
            method="POST",
            json={
                "skip_sync": skip_sync,
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
                    BtcBalanceResponse,
                    parse_obj_as(
                        type_=BtcBalanceResponse,
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

    async def get_fee_estimation(
        self, *, blocks: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EstimateFeeResponse]:
        """
        Get on-chain fee estimation

        Parameters
        ----------
        blocks : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EstimateFeeResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "estimatefee",
            method="POST",
            json={
                "blocks": blocks,
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
                    EstimateFeeResponse,
                    parse_obj_as(
                        type_=EstimateFeeResponse,
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

    async def list_transactions(
        self, *, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListTransactionsResponse]:
        """
        List the node's on-chain transactions

        Parameters
        ----------
        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTransactionsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "listtransactions",
            method="POST",
            json={
                "skip_sync": skip_sync,
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
                    ListTransactionsResponse,
                    parse_obj_as(
                        type_=ListTransactionsResponse,
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

    async def list_unspents(
        self, *, settled_only: bool, skip_sync: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListUnspentsResponse]:
        """
        List the unspent outputs of the internal BDK wallet

        Parameters
        ----------
        settled_only : bool

        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListUnspentsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "listunspents",
            method="POST",
            json={
                "settled_only": settled_only,
                "skip_sync": skip_sync,
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
                    ListUnspentsResponse,
                    parse_obj_as(
                        type_=ListUnspentsResponse,
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

    async def send_btc(
        self,
        *,
        amount: int,
        address: str,
        fee_rate: int,
        skip_sync: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SendBtcResponse]:
        """
        Send bitcoins on-chain

        Parameters
        ----------
        amount : int

        address : str

        fee_rate : int

        skip_sync : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SendBtcResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sendbtc",
            method="POST",
            json={
                "amount": amount,
                "address": address,
                "fee_rate": fee_rate,
                "skip_sync": skip_sync,
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
                    SendBtcResponse,
                    parse_obj_as(
                        type_=SendBtcResponse,
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
