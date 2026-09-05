

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.get_block import GetBlock
from ..types.get_ethereum_balance import GetEthereumBalance
from ..types.get_exchange_rate import GetExchangeRate
from ..types.get_gas_price import GetGasPrice
from ..types.get_last_block_number import GetLastBlockNumber
from ..types.get_token import GetToken
from ..types.get_token_balance import GetTokenBalance
from ..types.get_transactions import GetTransactions
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawInfoRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_block(
        self, *, authorization: str, block: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetBlock]:
        """
        Returns information of an ethereum block with or without transactions

        Parameters
        ----------
        authorization : str
            API Key

        block : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetBlock]

        """
        _response = self._client_wrapper.httpx_client.request(
            "getBlock",
            method="POST",
            json={
                "block": block,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBlock,
                    parse_obj_as(
                        type_=GetBlock,
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

    def get_ethereum_balance(
        self, *, authorization: str, ethereumaddress: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetEthereumBalance]:
        """
        Returns the ethereum balance of a given address.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetEthereumBalance]

        """
        _response = self._client_wrapper.httpx_client.request(
            "getEthereumBalance",
            method="POST",
            json={
                "ethereumaddress": ethereumaddress,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEthereumBalance,
                    parse_obj_as(
                        type_=GetEthereumBalance,
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

    def get_exchange_rate(
        self, *, authorization: str, currency: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetExchangeRate]:
        """
        Returns the current Ethereum price in Euro or US Dollar.

        Parameters
        ----------
        authorization : str
            API Key

        currency : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetExchangeRate]

        """
        _response = self._client_wrapper.httpx_client.request(
            "getExchangeRate",
            method="POST",
            json={
                "currency": currency,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetExchangeRate,
                    parse_obj_as(
                        type_=GetExchangeRate,
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

    def get_gas_price(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetGasPrice]:
        """
        Returns the current gas price in GWEI.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetGasPrice]

        """
        _response = self._client_wrapper.httpx_client.request(
            "getGasPrice",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGasPrice,
                    parse_obj_as(
                        type_=GetGasPrice,
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

    def get_last_block_number(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetLastBlockNumber]:
        """
        Returns the block number of the last mined ethereum block.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLastBlockNumber]

        """
        _response = self._client_wrapper.httpx_client.request(
            "getLastBlockNumber",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLastBlockNumber,
                    parse_obj_as(
                        type_=GetLastBlockNumber,
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

    def get_token(
        self, *, authorization: str, contractaddress: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetToken]:
        """
        Returns information about a specific ERC20 token like name, symbol, decimal places and total supply.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetToken]

        """
        _response = self._client_wrapper.httpx_client.request(
            "getToken",
            method="POST",
            json={
                "contractaddress": contractaddress,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetToken,
                    parse_obj_as(
                        type_=GetToken,
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

    def get_token_balance(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetTokenBalance]:
        """
        Returns the token balance of a given address.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTokenBalance]

        """
        _response = self._client_wrapper.httpx_client.request(
            "getTokenBalance",
            method="POST",
            json={
                "contractaddress": contractaddress,
                "ethereumaddress": ethereumaddress,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTokenBalance,
                    parse_obj_as(
                        type_=GetTokenBalance,
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

    def get_transactions(
        self, *, authorization: str, txid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetTransactions]:
        """
        Returns information like confirmations, token contract address, amount, gas price and more of a given transaction.

        Parameters
        ----------
        authorization : str
            API Key

        txid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetTransactions]

        """
        _response = self._client_wrapper.httpx_client.request(
            "getTransactions",
            method="POST",
            json={
                "txid": txid,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTransactions,
                    parse_obj_as(
                        type_=GetTransactions,
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


class AsyncRawInfoRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_block(
        self, *, authorization: str, block: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetBlock]:
        """
        Returns information of an ethereum block with or without transactions

        Parameters
        ----------
        authorization : str
            API Key

        block : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetBlock]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "getBlock",
            method="POST",
            json={
                "block": block,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetBlock,
                    parse_obj_as(
                        type_=GetBlock,
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

    async def get_ethereum_balance(
        self, *, authorization: str, ethereumaddress: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetEthereumBalance]:
        """
        Returns the ethereum balance of a given address.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetEthereumBalance]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "getEthereumBalance",
            method="POST",
            json={
                "ethereumaddress": ethereumaddress,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetEthereumBalance,
                    parse_obj_as(
                        type_=GetEthereumBalance,
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

    async def get_exchange_rate(
        self, *, authorization: str, currency: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetExchangeRate]:
        """
        Returns the current Ethereum price in Euro or US Dollar.

        Parameters
        ----------
        authorization : str
            API Key

        currency : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetExchangeRate]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "getExchangeRate",
            method="POST",
            json={
                "currency": currency,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetExchangeRate,
                    parse_obj_as(
                        type_=GetExchangeRate,
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

    async def get_gas_price(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetGasPrice]:
        """
        Returns the current gas price in GWEI.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetGasPrice]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "getGasPrice",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGasPrice,
                    parse_obj_as(
                        type_=GetGasPrice,
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

    async def get_last_block_number(
        self, *, authorization: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetLastBlockNumber]:
        """
        Returns the block number of the last mined ethereum block.

        Parameters
        ----------
        authorization : str
            API Key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLastBlockNumber]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "getLastBlockNumber",
            method="POST",
            headers={
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLastBlockNumber,
                    parse_obj_as(
                        type_=GetLastBlockNumber,
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

    async def get_token(
        self, *, authorization: str, contractaddress: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetToken]:
        """
        Returns information about a specific ERC20 token like name, symbol, decimal places and total supply.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetToken]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "getToken",
            method="POST",
            json={
                "contractaddress": contractaddress,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetToken,
                    parse_obj_as(
                        type_=GetToken,
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

    async def get_token_balance(
        self,
        *,
        authorization: str,
        contractaddress: str,
        ethereumaddress: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetTokenBalance]:
        """
        Returns the token balance of a given address.

        Parameters
        ----------
        authorization : str
            API Key

        contractaddress : str

        ethereumaddress : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTokenBalance]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "getTokenBalance",
            method="POST",
            json={
                "contractaddress": contractaddress,
                "ethereumaddress": ethereumaddress,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTokenBalance,
                    parse_obj_as(
                        type_=GetTokenBalance,
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

    async def get_transactions(
        self, *, authorization: str, txid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetTransactions]:
        """
        Returns information like confirmations, token contract address, amount, gas price and more of a given transaction.

        Parameters
        ----------
        authorization : str
            API Key

        txid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetTransactions]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "getTransactions",
            method="POST",
            json={
                "txid": txid,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetTransactions,
                    parse_obj_as(
                        type_=GetTransactions,
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
