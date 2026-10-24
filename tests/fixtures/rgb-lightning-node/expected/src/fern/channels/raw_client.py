

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.empty_response import EmptyResponse
from ..types.get_channel_id_response import GetChannelIdResponse
from ..types.list_channels_response import ListChannelsResponse
from ..types.open_channel_response import OpenChannelResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawChannelsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def close_a_channel(
        self, *, channel_id: str, peer_pubkey: str, force: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Close a LN channel cooperatively or forcibly

        Parameters
        ----------
        channel_id : str

        peer_pubkey : str

        force : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "closechannel",
            method="POST",
            json={
                "channel_id": channel_id,
                "peer_pubkey": peer_pubkey,
                "force": force,
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

    def get_a_channels_id(
        self, *, temporary_channel_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetChannelIdResponse]:
        """
        Get a channel's ID from its former temporary channel ID

        Parameters
        ----------
        temporary_channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetChannelIdResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "getchannelid",
            method="POST",
            json={
                "temporary_channel_id": temporary_channel_id,
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
                    GetChannelIdResponse,
                    parse_obj_as(
                        type_=GetChannelIdResponse,
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

    def list_channels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListChannelsResponse]:
        """
        List the node's LN channels

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListChannelsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "listchannels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChannelsResponse,
                    parse_obj_as(
                        type_=ListChannelsResponse,
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

    def open_a_channel(
        self,
        *,
        peer_pubkey_and_opt_addr: str,
        capacity_sat: int,
        push_msat: int,
        public: bool,
        with_anchors: bool,
        asset_amount: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        push_asset_amount: typing.Optional[int] = OMIT,
        fee_base_msat: typing.Optional[int] = OMIT,
        fee_proportional_millionths: typing.Optional[int] = OMIT,
        temporary_channel_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OpenChannelResponse]:
        """
        Open a new LN channel (RGB-enabled when both asset_id and asset_amount are specified). You can optionally provide a 32 bytes temporary channel ID as a hex-encoded string.

        Parameters
        ----------
        peer_pubkey_and_opt_addr : str

        capacity_sat : int

        push_msat : int

        public : bool

        with_anchors : bool

        asset_amount : typing.Optional[int]

        asset_id : typing.Optional[str]

        push_asset_amount : typing.Optional[int]

        fee_base_msat : typing.Optional[int]

        fee_proportional_millionths : typing.Optional[int]

        temporary_channel_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OpenChannelResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "openchannel",
            method="POST",
            json={
                "peer_pubkey_and_opt_addr": peer_pubkey_and_opt_addr,
                "capacity_sat": capacity_sat,
                "push_msat": push_msat,
                "asset_amount": asset_amount,
                "asset_id": asset_id,
                "push_asset_amount": push_asset_amount,
                "public": public,
                "with_anchors": with_anchors,
                "fee_base_msat": fee_base_msat,
                "fee_proportional_millionths": fee_proportional_millionths,
                "temporary_channel_id": temporary_channel_id,
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
                    OpenChannelResponse,
                    parse_obj_as(
                        type_=OpenChannelResponse,
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


class AsyncRawChannelsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def close_a_channel(
        self, *, channel_id: str, peer_pubkey: str, force: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Close a LN channel cooperatively or forcibly

        Parameters
        ----------
        channel_id : str

        peer_pubkey : str

        force : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "closechannel",
            method="POST",
            json={
                "channel_id": channel_id,
                "peer_pubkey": peer_pubkey,
                "force": force,
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

    async def get_a_channels_id(
        self, *, temporary_channel_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetChannelIdResponse]:
        """
        Get a channel's ID from its former temporary channel ID

        Parameters
        ----------
        temporary_channel_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetChannelIdResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "getchannelid",
            method="POST",
            json={
                "temporary_channel_id": temporary_channel_id,
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
                    GetChannelIdResponse,
                    parse_obj_as(
                        type_=GetChannelIdResponse,
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

    async def list_channels(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListChannelsResponse]:
        """
        List the node's LN channels

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListChannelsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "listchannels",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListChannelsResponse,
                    parse_obj_as(
                        type_=ListChannelsResponse,
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

    async def open_a_channel(
        self,
        *,
        peer_pubkey_and_opt_addr: str,
        capacity_sat: int,
        push_msat: int,
        public: bool,
        with_anchors: bool,
        asset_amount: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        push_asset_amount: typing.Optional[int] = OMIT,
        fee_base_msat: typing.Optional[int] = OMIT,
        fee_proportional_millionths: typing.Optional[int] = OMIT,
        temporary_channel_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OpenChannelResponse]:
        """
        Open a new LN channel (RGB-enabled when both asset_id and asset_amount are specified). You can optionally provide a 32 bytes temporary channel ID as a hex-encoded string.

        Parameters
        ----------
        peer_pubkey_and_opt_addr : str

        capacity_sat : int

        push_msat : int

        public : bool

        with_anchors : bool

        asset_amount : typing.Optional[int]

        asset_id : typing.Optional[str]

        push_asset_amount : typing.Optional[int]

        fee_base_msat : typing.Optional[int]

        fee_proportional_millionths : typing.Optional[int]

        temporary_channel_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OpenChannelResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "openchannel",
            method="POST",
            json={
                "peer_pubkey_and_opt_addr": peer_pubkey_and_opt_addr,
                "capacity_sat": capacity_sat,
                "push_msat": push_msat,
                "asset_amount": asset_amount,
                "asset_id": asset_id,
                "push_asset_amount": push_asset_amount,
                "public": public,
                "with_anchors": with_anchors,
                "fee_base_msat": fee_base_msat,
                "fee_proportional_millionths": fee_proportional_millionths,
                "temporary_channel_id": temporary_channel_id,
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
                    OpenChannelResponse,
                    parse_obj_as(
                        type_=OpenChannelResponse,
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
