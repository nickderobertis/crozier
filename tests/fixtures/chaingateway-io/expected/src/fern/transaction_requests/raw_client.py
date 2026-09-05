

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.clear_address import ClearAddress
from ..types.send_ethereum import SendEthereum
from ..types.send_token import SendToken
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTransactionRequestsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def clear_address(
        self,
        *,
        authorization: str,
        ethereumaddress: str,
        newaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ClearAddress]:
        """
        Sends all available ethereum funds of an address to a specified receiver address.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        newaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ClearAddress]

        """
        _response = self._client_wrapper.httpx_client.request(
            "clearAddress",
            method="POST",
            json={
                "ethereumaddress": ethereumaddress,
                "newaddress": newaddress,
                "password": password,
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
                    ClearAddress,
                    parse_obj_as(
                        type_=ClearAddress,
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

    def send_ethereum(
        self,
        *,
        authorization: str,
        amount: float,
        from_: str,
        password: str,
        to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SendEthereum]:
        """
        Sends ethereum from an address controlled by the account to a specified receiver address.

        Parameters
        ----------
        authorization : str
            API Key

        amount : float

        from_ : str

        password : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SendEthereum]

        """
        _response = self._client_wrapper.httpx_client.request(
            "sendEthereum",
            method="POST",
            json={
                "amount": amount,
                "from": from_,
                "password": password,
                "to": to,
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
                    SendEthereum,
                    parse_obj_as(
                        type_=SendEthereum,
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

    def send_token(
        self,
        *,
        authorization: str,
        amount: int,
        contractaddress: str,
        from_: str,
        identifier: str,
        password: str,
        to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SendToken]:
        """
        Sends ERC20 tokens from an address controlled by the account to a specified receiver address. The token contract address is needed to specify the token. The use of the identifier parameter is recommend and awaits an unique string. Whenever a transaction is beeing sent, the identifier is checked and the transaction gets dropped if there is one with that identifier already.

        Parameters
        ----------
        authorization : str
            API Key

        amount : int

        contractaddress : str

        from_ : str

        identifier : str

        password : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SendToken]

        """
        _response = self._client_wrapper.httpx_client.request(
            "sendToken",
            method="POST",
            json={
                "amount": amount,
                "contractaddress": contractaddress,
                "from": from_,
                "identifier": identifier,
                "password": password,
                "to": to,
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
                    SendToken,
                    parse_obj_as(
                        type_=SendToken,
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


class AsyncRawTransactionRequestsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def clear_address(
        self,
        *,
        authorization: str,
        ethereumaddress: str,
        newaddress: str,
        password: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ClearAddress]:
        """
        Sends all available ethereum funds of an address to a specified receiver address.

        Parameters
        ----------
        authorization : str
            API Key

        ethereumaddress : str

        newaddress : str

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ClearAddress]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "clearAddress",
            method="POST",
            json={
                "ethereumaddress": ethereumaddress,
                "newaddress": newaddress,
                "password": password,
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
                    ClearAddress,
                    parse_obj_as(
                        type_=ClearAddress,
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

    async def send_ethereum(
        self,
        *,
        authorization: str,
        amount: float,
        from_: str,
        password: str,
        to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SendEthereum]:
        """
        Sends ethereum from an address controlled by the account to a specified receiver address.

        Parameters
        ----------
        authorization : str
            API Key

        amount : float

        from_ : str

        password : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SendEthereum]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "sendEthereum",
            method="POST",
            json={
                "amount": amount,
                "from": from_,
                "password": password,
                "to": to,
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
                    SendEthereum,
                    parse_obj_as(
                        type_=SendEthereum,
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

    async def send_token(
        self,
        *,
        authorization: str,
        amount: int,
        contractaddress: str,
        from_: str,
        identifier: str,
        password: str,
        to: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SendToken]:
        """
        Sends ERC20 tokens from an address controlled by the account to a specified receiver address. The token contract address is needed to specify the token. The use of the identifier parameter is recommend and awaits an unique string. Whenever a transaction is beeing sent, the identifier is checked and the transaction gets dropped if there is one with that identifier already.

        Parameters
        ----------
        authorization : str
            API Key

        amount : int

        contractaddress : str

        from_ : str

        identifier : str

        password : str

        to : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SendToken]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "sendToken",
            method="POST",
            json={
                "amount": amount,
                "contractaddress": contractaddress,
                "from": from_,
                "identifier": identifier,
                "password": password,
                "to": to,
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
                    SendToken,
                    parse_obj_as(
                        type_=SendToken,
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
