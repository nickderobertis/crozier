

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..types.block_id import BlockId
from ..types.consensus_transaction import ConsensusTransaction
from ..types.consensus_v2block_data import ConsensusV2BlockData
from ..types.gateway_peer import GatewayPeer
from ..types.siacoin_output import SiacoinOutput
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSyncerClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_syncer_connect(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Attempts to connect to the supplied peer address.

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "syncer/connect",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_syncer_peers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[GatewayPeer]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GatewayPeer]]
            Connected peers and their metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            "syncer/peers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GatewayPeer],
                    parse_obj_as(
                        type_=typing.List[GatewayPeer],
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

    def post_syncer_broadcast_block(
        self,
        *,
        id: BlockId,
        parent_id: BlockId,
        nonce: int,
        timestamp: dt.datetime,
        miner_payouts: typing.Sequence[SiacoinOutput],
        transactions: typing.Sequence[ConsensusTransaction],
        v2: typing.Optional[ConsensusV2BlockData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Adds the supplied block to the local chain (if valid) and broadcasts it to peers. When broadcasting a v2 block, walletd sends the block outline.

        Parameters
        ----------
        id : BlockId

        parent_id : BlockId

        nonce : int

        timestamp : dt.datetime

        miner_payouts : typing.Sequence[SiacoinOutput]

        transactions : typing.Sequence[ConsensusTransaction]

        v2 : typing.Optional[ConsensusV2BlockData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "syncer/broadcast/block",
            method="POST",
            json={
                "id": id,
                "parentID": parent_id,
                "nonce": nonce,
                "timestamp": timestamp,
                "minerPayouts": convert_and_respect_annotation_metadata(
                    object_=miner_payouts, annotation=typing.Sequence[SiacoinOutput], direction="write"
                ),
                "transactions": convert_and_respect_annotation_metadata(
                    object_=transactions, annotation=typing.Sequence[ConsensusTransaction], direction="write"
                ),
                "v2": convert_and_respect_annotation_metadata(
                    object_=v2, annotation=ConsensusV2BlockData, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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


class AsyncRawSyncerClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_syncer_connect(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Attempts to connect to the supplied peer address.

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "syncer/connect",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_syncer_peers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[GatewayPeer]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GatewayPeer]]
            Connected peers and their metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "syncer/peers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GatewayPeer],
                    parse_obj_as(
                        type_=typing.List[GatewayPeer],
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

    async def post_syncer_broadcast_block(
        self,
        *,
        id: BlockId,
        parent_id: BlockId,
        nonce: int,
        timestamp: dt.datetime,
        miner_payouts: typing.Sequence[SiacoinOutput],
        transactions: typing.Sequence[ConsensusTransaction],
        v2: typing.Optional[ConsensusV2BlockData] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Adds the supplied block to the local chain (if valid) and broadcasts it to peers. When broadcasting a v2 block, walletd sends the block outline.

        Parameters
        ----------
        id : BlockId

        parent_id : BlockId

        nonce : int

        timestamp : dt.datetime

        miner_payouts : typing.Sequence[SiacoinOutput]

        transactions : typing.Sequence[ConsensusTransaction]

        v2 : typing.Optional[ConsensusV2BlockData]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "syncer/broadcast/block",
            method="POST",
            json={
                "id": id,
                "parentID": parent_id,
                "nonce": nonce,
                "timestamp": timestamp,
                "minerPayouts": convert_and_respect_annotation_metadata(
                    object_=miner_payouts, annotation=typing.Sequence[SiacoinOutput], direction="write"
                ),
                "transactions": convert_and_respect_annotation_metadata(
                    object_=transactions, annotation=typing.Sequence[ConsensusTransaction], direction="write"
                ),
                "v2": convert_and_respect_annotation_metadata(
                    object_=v2, annotation=ConsensusV2BlockData, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
