

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
from ..errors.not_found_error import NotFoundError
from ..types.block import Block
from ..types.chain_index import ChainIndex
from ..types.consensus_checkpoint_response import ConsensusCheckpointResponse
from ..types.consensus_network import ConsensusNetwork
from ..types.consensus_state import ConsensusState
from ..types.consensus_updates_response import ConsensusUpdatesResponse
from .types.get_consensus_block_request_id import GetConsensusBlockRequestId
from .types.get_consensus_checkpoint_request_id import GetConsensusCheckpointRequestId
from pydantic import ValidationError


class RawConsensusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_consensus_network(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConsensusNetwork]:
        """
        Returns consensus parameters for the active network.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConsensusNetwork]
            Consensus network parameters.
        """
        _response = self._client_wrapper.httpx_client.request(
            "consensus/network",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsensusNetwork,
                    parse_obj_as(
                        type_=ConsensusNetwork,
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

    def get_consensus_tip(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ChainIndex]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChainIndex]
            Current best chain index.
        """
        _response = self._client_wrapper.httpx_client.request(
            "consensus/tip",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChainIndex,
                    parse_obj_as(
                        type_=ChainIndex,
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

    def get_consensus_tip_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConsensusState]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConsensusState]
            Consensus state at the current tip.
        """
        _response = self._client_wrapper.httpx_client.request(
            "consensus/tipstate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsensusState,
                    parse_obj_as(
                        type_=ConsensusState,
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

    def get_consensus_checkpoint(
        self, id: GetConsensusCheckpointRequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConsensusCheckpointResponse]:
        """
        Returns the consensus state and block associated with the supplied block ID or height.

        Parameters
        ----------
        id : GetConsensusCheckpointRequestId
            Block ID (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConsensusCheckpointResponse]
            Consensus checkpoint for the supplied block.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"consensus/checkpoint/{encode_path_param(convert_and_respect_annotation_metadata(object_=id, annotation=GetConsensusCheckpointRequestId, direction='write'))}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsensusCheckpointResponse,
                    parse_obj_as(
                        type_=ConsensusCheckpointResponse,
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

    def get_consensus_block(
        self, id: GetConsensusBlockRequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Block]:
        """
        Parameters
        ----------
        id : GetConsensusBlockRequestId
            Block ID (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Block]
            Block data.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"consensus/blocks/{encode_path_param(convert_and_respect_annotation_metadata(object_=id, annotation=GetConsensusBlockRequestId, direction='write'))}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Block,
                    parse_obj_as(
                        type_=Block,
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

    def get_consensus_updates(
        self,
        index: ChainIndex,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConsensusUpdatesResponse]:
        """
        Returns the set of reverted and applied updates needed to move from the supplied chain index to the current tip.

        Parameters
        ----------
        index : ChainIndex
            Starting chain index.

        limit : typing.Optional[int]
            Maximum number of updates to return (default 10, max 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ConsensusUpdatesResponse]
            Consensus updates needed to synchronize the supplied index.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"consensus/updates/{encode_path_param(convert_and_respect_annotation_metadata(object_=index, annotation=ChainIndex, direction='write'))}",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsensusUpdatesResponse,
                    parse_obj_as(
                        type_=ConsensusUpdatesResponse,
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

    def get_consensus_index_by_height(
        self, height: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ChainIndex]:
        """
        Parameters
        ----------
        height : int
            Block height to resolve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChainIndex]
            Chain index at the requested height.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"consensus/index/{encode_path_param(height)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChainIndex,
                    parse_obj_as(
                        type_=ChainIndex,
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


class AsyncRawConsensusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_consensus_network(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConsensusNetwork]:
        """
        Returns consensus parameters for the active network.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConsensusNetwork]
            Consensus network parameters.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "consensus/network",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsensusNetwork,
                    parse_obj_as(
                        type_=ConsensusNetwork,
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

    async def get_consensus_tip(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChainIndex]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChainIndex]
            Current best chain index.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "consensus/tip",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChainIndex,
                    parse_obj_as(
                        type_=ChainIndex,
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

    async def get_consensus_tip_state(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConsensusState]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConsensusState]
            Consensus state at the current tip.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "consensus/tipstate",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsensusState,
                    parse_obj_as(
                        type_=ConsensusState,
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

    async def get_consensus_checkpoint(
        self, id: GetConsensusCheckpointRequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConsensusCheckpointResponse]:
        """
        Returns the consensus state and block associated with the supplied block ID or height.

        Parameters
        ----------
        id : GetConsensusCheckpointRequestId
            Block ID (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConsensusCheckpointResponse]
            Consensus checkpoint for the supplied block.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"consensus/checkpoint/{encode_path_param(convert_and_respect_annotation_metadata(object_=id, annotation=GetConsensusCheckpointRequestId, direction='write'))}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsensusCheckpointResponse,
                    parse_obj_as(
                        type_=ConsensusCheckpointResponse,
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

    async def get_consensus_block(
        self, id: GetConsensusBlockRequestId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Block]:
        """
        Parameters
        ----------
        id : GetConsensusBlockRequestId
            Block ID (hex) or height.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Block]
            Block data.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"consensus/blocks/{encode_path_param(convert_and_respect_annotation_metadata(object_=id, annotation=GetConsensusBlockRequestId, direction='write'))}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Block,
                    parse_obj_as(
                        type_=Block,
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

    async def get_consensus_updates(
        self,
        index: ChainIndex,
        *,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConsensusUpdatesResponse]:
        """
        Returns the set of reverted and applied updates needed to move from the supplied chain index to the current tip.

        Parameters
        ----------
        index : ChainIndex
            Starting chain index.

        limit : typing.Optional[int]
            Maximum number of updates to return (default 10, max 100).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ConsensusUpdatesResponse]
            Consensus updates needed to synchronize the supplied index.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"consensus/updates/{encode_path_param(convert_and_respect_annotation_metadata(object_=index, annotation=ChainIndex, direction='write'))}",
            method="GET",
            params={
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConsensusUpdatesResponse,
                    parse_obj_as(
                        type_=ConsensusUpdatesResponse,
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

    async def get_consensus_index_by_height(
        self, height: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChainIndex]:
        """
        Parameters
        ----------
        height : int
            Block height to resolve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChainIndex]
            Chain index at the requested height.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"consensus/index/{encode_path_param(height)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChainIndex,
                    parse_obj_as(
                        type_=ChainIndex,
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
