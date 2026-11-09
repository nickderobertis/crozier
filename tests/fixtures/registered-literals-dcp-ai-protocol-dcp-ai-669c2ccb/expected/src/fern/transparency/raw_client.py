

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
from ..types.inclusion_proof import InclusionProof
from ..types.signed_tree_head import SignedTreeHead
from .types.add_gossip_peer_response import AddGossipPeerResponse
from .types.add_to_log_response import AddToLogResponse
from .types.get_gossip_alerts_response import GetGossipAlertsResponse
from .types.get_gossip_peers_response import GetGossipPeersResponse
from .types.get_log_root_response import GetLogRootResponse
from .types.gossip_exchange_response import GossipExchangeResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTransparencyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_to_log(
        self, *, bundle_hash: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AddToLogResponse]:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        bundle_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddToLogResponse]
            Log entry added
        """
        _response = self._client_wrapper.httpx_client.request(
            "transparency-log/add",
            method="POST",
            json={
                "bundle_hash": bundle_hash,
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
                    AddToLogResponse,
                    parse_obj_as(
                        type_=AddToLogResponse,
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

    def get_log_root(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetLogRootResponse]:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetLogRootResponse]
            Current Merkle root of the transparency log
        """
        _response = self._client_wrapper.httpx_client.request(
            "transparency-log/root",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLogRootResponse,
                    parse_obj_as(
                        type_=GetLogRootResponse,
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

    def get_log_proof(
        self, index: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[InclusionProof]:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        index : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InclusionProof]
            Merkle inclusion proof
        """
        _response = self._client_wrapper.httpx_client.request(
            f"transparency-log/proof/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InclusionProof,
                    parse_obj_as(
                        type_=InclusionProof,
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

    def get_signed_tree_head(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SignedTreeHead]:
        """
        Returns a Signed Tree Head — the current Merkle root signed by the log operator.
        Used for gossip protocol cross-log verification.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SignedTreeHead]
            Signed tree head
        """
        _response = self._client_wrapper.httpx_client.request(
            "transparency-log/root/signed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SignedTreeHead,
                    parse_obj_as(
                        type_=SignedTreeHead,
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

    def get_gossip_peers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetGossipPeersResponse]:
        """
        List all known gossip peers and recent split-view alerts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetGossipPeersResponse]
            Gossip peers and alerts
        """
        _response = self._client_wrapper.httpx_client.request(
            "transparency-log/gossip/peers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGossipPeersResponse,
                    parse_obj_as(
                        type_=GetGossipPeersResponse,
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

    def add_gossip_peer(
        self, *, peer_id: str, endpoint: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AddGossipPeerResponse]:
        """
        Parameters
        ----------
        peer_id : str

        endpoint : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddGossipPeerResponse]
            Peer added
        """
        _response = self._client_wrapper.httpx_client.request(
            "transparency-log/gossip/peers",
            method="POST",
            json={
                "peer_id": peer_id,
                "endpoint": endpoint,
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
                    AddGossipPeerResponse,
                    parse_obj_as(
                        type_=AddGossipPeerResponse,
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

    def gossip_exchange(
        self, *, sth: typing.Optional[SignedTreeHead] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GossipExchangeResponse]:
        """
        Exchange signed tree heads between log instances for cross-verification.
        Detects split-view attacks when roots differ for the same tree size.

        Parameters
        ----------
        sth : typing.Optional[SignedTreeHead]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GossipExchangeResponse]
            Local STH and any detected alert
        """
        _response = self._client_wrapper.httpx_client.request(
            "transparency-log/gossip/exchange",
            method="POST",
            json={
                "sth": convert_and_respect_annotation_metadata(
                    object_=sth, annotation=SignedTreeHead, direction="write"
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
                    GossipExchangeResponse,
                    parse_obj_as(
                        type_=GossipExchangeResponse,
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

    def get_gossip_alerts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetGossipAlertsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetGossipAlertsResponse]
            List of detected split-view alerts
        """
        _response = self._client_wrapper.httpx_client.request(
            "transparency-log/gossip/alerts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGossipAlertsResponse,
                    parse_obj_as(
                        type_=GetGossipAlertsResponse,
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


class AsyncRawTransparencyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_to_log(
        self, *, bundle_hash: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AddToLogResponse]:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        bundle_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddToLogResponse]
            Log entry added
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transparency-log/add",
            method="POST",
            json={
                "bundle_hash": bundle_hash,
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
                    AddToLogResponse,
                    parse_obj_as(
                        type_=AddToLogResponse,
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

    async def get_log_root(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetLogRootResponse]:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetLogRootResponse]
            Current Merkle root of the transparency log
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transparency-log/root",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetLogRootResponse,
                    parse_obj_as(
                        type_=GetLogRootResponse,
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

    async def get_log_proof(
        self, index: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[InclusionProof]:
        """
        Available on the transparency-log service (port 3002).

        Parameters
        ----------
        index : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InclusionProof]
            Merkle inclusion proof
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"transparency-log/proof/{encode_path_param(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    InclusionProof,
                    parse_obj_as(
                        type_=InclusionProof,
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

    async def get_signed_tree_head(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SignedTreeHead]:
        """
        Returns a Signed Tree Head — the current Merkle root signed by the log operator.
        Used for gossip protocol cross-log verification.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SignedTreeHead]
            Signed tree head
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transparency-log/root/signed",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SignedTreeHead,
                    parse_obj_as(
                        type_=SignedTreeHead,
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

    async def get_gossip_peers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetGossipPeersResponse]:
        """
        List all known gossip peers and recent split-view alerts.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetGossipPeersResponse]
            Gossip peers and alerts
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transparency-log/gossip/peers",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGossipPeersResponse,
                    parse_obj_as(
                        type_=GetGossipPeersResponse,
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

    async def add_gossip_peer(
        self, *, peer_id: str, endpoint: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AddGossipPeerResponse]:
        """
        Parameters
        ----------
        peer_id : str

        endpoint : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddGossipPeerResponse]
            Peer added
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transparency-log/gossip/peers",
            method="POST",
            json={
                "peer_id": peer_id,
                "endpoint": endpoint,
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
                    AddGossipPeerResponse,
                    parse_obj_as(
                        type_=AddGossipPeerResponse,
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

    async def gossip_exchange(
        self, *, sth: typing.Optional[SignedTreeHead] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GossipExchangeResponse]:
        """
        Exchange signed tree heads between log instances for cross-verification.
        Detects split-view attacks when roots differ for the same tree size.

        Parameters
        ----------
        sth : typing.Optional[SignedTreeHead]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GossipExchangeResponse]
            Local STH and any detected alert
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transparency-log/gossip/exchange",
            method="POST",
            json={
                "sth": convert_and_respect_annotation_metadata(
                    object_=sth, annotation=SignedTreeHead, direction="write"
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
                    GossipExchangeResponse,
                    parse_obj_as(
                        type_=GossipExchangeResponse,
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

    async def get_gossip_alerts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetGossipAlertsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetGossipAlertsResponse]
            List of detected split-view alerts
        """
        _response = await self._client_wrapper.httpx_client.request(
            "transparency-log/gossip/alerts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetGossipAlertsResponse,
                    parse_obj_as(
                        type_=GetGossipAlertsResponse,
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
