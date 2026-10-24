

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.decode_swapstring_response import DecodeSwapstringResponse
from ..types.empty_response import EmptyResponse
from ..types.get_swap_response import GetSwapResponse
from ..types.list_swaps_response import ListSwapsResponse
from ..types.maker_init_response import MakerInitResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSwapsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def decode_a_swapstring(
        self, *, swapstring: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DecodeSwapstringResponse]:
        """
        Decode the provided swapstring

        Parameters
        ----------
        swapstring : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DecodeSwapstringResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "decodeswapstring",
            method="POST",
            json={
                "swapstring": swapstring,
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
                    DecodeSwapstringResponse,
                    parse_obj_as(
                        type_=DecodeSwapstringResponse,
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

    def get_a_swap(
        self, *, payment_hash: str, taker: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSwapResponse]:
        """
        Get a swap by its payment hash

        Parameters
        ----------
        payment_hash : str

        taker : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSwapResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "getswap",
            method="POST",
            json={
                "payment_hash": payment_hash,
                "taker": taker,
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
                    GetSwapResponse,
                    parse_obj_as(
                        type_=GetSwapResponse,
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

    def list_swaps(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ListSwapsResponse]:
        """
        List the node's swaps

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListSwapsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "listswaps",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSwapsResponse,
                    parse_obj_as(
                        type_=ListSwapsResponse,
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

    def execute_a_maker_swap(
        self,
        *,
        swapstring: str,
        payment_secret: str,
        taker_pubkey: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmptyResponse]:
        """
        Execute a swap on the maker side

        Parameters
        ----------
        swapstring : str

        payment_secret : str

        taker_pubkey : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "makerexecute",
            method="POST",
            json={
                "swapstring": swapstring,
                "payment_secret": payment_secret,
                "taker_pubkey": taker_pubkey,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    def init_a_maker_swap(
        self,
        *,
        qty_from: int,
        qty_to: int,
        timeout_sec: int,
        from_asset: typing.Optional[str] = OMIT,
        to_asset: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MakerInitResponse]:
        """
        Init a swap on the maker side

        Parameters
        ----------
        qty_from : int

        qty_to : int

        timeout_sec : int

        from_asset : typing.Optional[str]

        to_asset : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MakerInitResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "makerinit",
            method="POST",
            json={
                "qty_from": qty_from,
                "qty_to": qty_to,
                "from_asset": from_asset,
                "to_asset": to_asset,
                "timeout_sec": timeout_sec,
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
                    MakerInitResponse,
                    parse_obj_as(
                        type_=MakerInitResponse,
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

    def accept_a_swap(
        self, *, swapstring: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Accept a swap on the taker side

        Parameters
        ----------
        swapstring : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "taker",
            method="POST",
            json={
                "swapstring": swapstring,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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


class AsyncRawSwapsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def decode_a_swapstring(
        self, *, swapstring: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DecodeSwapstringResponse]:
        """
        Decode the provided swapstring

        Parameters
        ----------
        swapstring : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DecodeSwapstringResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "decodeswapstring",
            method="POST",
            json={
                "swapstring": swapstring,
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
                    DecodeSwapstringResponse,
                    parse_obj_as(
                        type_=DecodeSwapstringResponse,
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

    async def get_a_swap(
        self, *, payment_hash: str, taker: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSwapResponse]:
        """
        Get a swap by its payment hash

        Parameters
        ----------
        payment_hash : str

        taker : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSwapResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "getswap",
            method="POST",
            json={
                "payment_hash": payment_hash,
                "taker": taker,
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
                    GetSwapResponse,
                    parse_obj_as(
                        type_=GetSwapResponse,
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

    async def list_swaps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListSwapsResponse]:
        """
        List the node's swaps

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListSwapsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "listswaps",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListSwapsResponse,
                    parse_obj_as(
                        type_=ListSwapsResponse,
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

    async def execute_a_maker_swap(
        self,
        *,
        swapstring: str,
        payment_secret: str,
        taker_pubkey: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Execute a swap on the maker side

        Parameters
        ----------
        swapstring : str

        payment_secret : str

        taker_pubkey : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "makerexecute",
            method="POST",
            json={
                "swapstring": swapstring,
                "payment_secret": payment_secret,
                "taker_pubkey": taker_pubkey,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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

    async def init_a_maker_swap(
        self,
        *,
        qty_from: int,
        qty_to: int,
        timeout_sec: int,
        from_asset: typing.Optional[str] = OMIT,
        to_asset: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MakerInitResponse]:
        """
        Init a swap on the maker side

        Parameters
        ----------
        qty_from : int

        qty_to : int

        timeout_sec : int

        from_asset : typing.Optional[str]

        to_asset : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MakerInitResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "makerinit",
            method="POST",
            json={
                "qty_from": qty_from,
                "qty_to": qty_to,
                "from_asset": from_asset,
                "to_asset": to_asset,
                "timeout_sec": timeout_sec,
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
                    MakerInitResponse,
                    parse_obj_as(
                        type_=MakerInitResponse,
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

    async def accept_a_swap(
        self, *, swapstring: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Accept a swap on the taker side

        Parameters
        ----------
        swapstring : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "taker",
            method="POST",
            json={
                "swapstring": swapstring,
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
                    EmptyResponse,
                    parse_obj_as(
                        type_=EmptyResponse,
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
