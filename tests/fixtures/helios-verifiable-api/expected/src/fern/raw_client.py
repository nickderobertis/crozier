

import typing
from json.decoder import JSONDecodeError

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.http_response import AsyncHttpResponse, HttpResponse
from .core.jsonable_encoder import encode_path_param
from .core.parse_error import ParsingError
from .core.pydantic_utilities import parse_obj_as
from .core.request_options import RequestOptions
from .core.serialization import convert_and_respect_annotation_metadata
from .errors.bad_request_error import BadRequestError
from .errors.internal_server_error import InternalServerError
from .types.block import Block
from .types.block_number_or_tag_or_hash import BlockNumberOrTagOrHash
from .types.block_receipts_response import BlockReceiptsResponse
from .types.bytes import Bytes
from .types.chain_id_response import ChainIdResponse
from .types.error_response import ErrorResponse
from .types.filter import Filter
from .types.new_filter_request_kind import NewFilterRequestKind
from .types.new_filter_response import NewFilterResponse
from .types.send_raw_tx_response import SendRawTxResponse
from .types.uint import Uint
from .types.uninstall_filter_response import UninstallFilterResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFernApi:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_chain_id(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[ChainIdResponse]:
        """
        Returns the chain id of the network of the underlying RPC node.
        ### Why is this useful?
        Replaces the `eth_chainId` RPC method.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ChainIdResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "eth/v1/chainId",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChainIdResponse,
                    parse_obj_as(
                        type_=ChainIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_block_information(
        self,
        block_id: BlockNumberOrTagOrHash,
        *,
        transaction_detail_flag: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Block]:
        """
        Returns information about a block.
        ### Why is this useful?
        Replaces the `eth_getBlockByNumber` and `eth_getBlockByHash` RPC methods.

        Parameters
        ----------
        block_id : BlockNumberOrTagOrHash

        transaction_detail_flag : typing.Optional[bool]
            A flag indicating whether to include full transaction details or just the hashes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Block]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"eth/v1/block/{encode_path_param(block_id)}",
            method="GET",
            params={
                "transactionDetailFlag": transaction_detail_flag,
            },
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def get_block_receipts(
        self, block_id: BlockNumberOrTagOrHash, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[BlockReceiptsResponse]:
        """
        Returns all transaction receipts for a given block.
        ### Why is this useful?
        Replaces the `eth_getBlockReceipts` RPC method.
        ### How to verify response?
        - RLP encode each receipt and keccak-256 hash these encoded receipts.
        - Construct a Merkle Patricia Trie (MPT) from these hashes.
        - Verify the root of the constructed MPT against the trusted block's receipt root.

        Parameters
        ----------
        block_id : BlockNumberOrTagOrHash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BlockReceiptsResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"eth/v1/block/{encode_path_param(block_id)}/receipts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockReceiptsResponse,
                    parse_obj_as(
                        type_=BlockReceiptsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def send_raw_transaction(
        self, *, bytes: typing.Optional[Bytes] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SendRawTxResponse]:
        """
        Creates a new message call transaction or a contract creation for signed transactions.
        ### Why is this useful?
        Replaces the `eth_sendRawTransaction` RPC method.

        Parameters
        ----------
        bytes : typing.Optional[Bytes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SendRawTxResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "eth/v1/sendRawTransaction",
            method="POST",
            json={
                "bytes": bytes,
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
                    SendRawTxResponse,
                    parse_obj_as(
                        type_=SendRawTxResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def create_new_filter(
        self,
        *,
        kind: typing.Optional[NewFilterRequestKind] = OMIT,
        filter: typing.Optional[Filter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NewFilterResponse]:
        """
        Creates a filter in the node, to notify when the state changes.

        State changes can be of three types: logs, new blocks and pending transactions.

        To check if the state has changed, query `/filterChanges/{filterId}`.
        ### Why is this useful?
        Replaces the `eth_newFilter`, `eth_newBlockFilter` and `eth_newPendingTransactionFilter` RPC methods.

        Parameters
        ----------
        kind : typing.Optional[NewFilterRequestKind]

        filter : typing.Optional[Filter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NewFilterResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "eth/v1/filter",
            method="POST",
            json={
                "kind": kind,
                "filter": convert_and_respect_annotation_metadata(object_=filter, annotation=Filter, direction="write"),
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
                    NewFilterResponse,
                    parse_obj_as(
                        type_=NewFilterResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    def uninstall_a_filter(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UninstallFilterResponse]:
        """
        Uninstalls a filter with given id.
        ### Why is this useful?
        Replaces the `eth_uninstallFilter` RPC method.

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UninstallFilterResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"eth/v1/filter/{encode_path_param(filter_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UninstallFilterResponse,
                    parse_obj_as(
                        type_=UninstallFilterResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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


class AsyncRawFernApi:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_chain_id(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ChainIdResponse]:
        """
        Returns the chain id of the network of the underlying RPC node.
        ### Why is this useful?
        Replaces the `eth_chainId` RPC method.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ChainIdResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "eth/v1/chainId",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ChainIdResponse,
                    parse_obj_as(
                        type_=ChainIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_block_information(
        self,
        block_id: BlockNumberOrTagOrHash,
        *,
        transaction_detail_flag: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Block]:
        """
        Returns information about a block.
        ### Why is this useful?
        Replaces the `eth_getBlockByNumber` and `eth_getBlockByHash` RPC methods.

        Parameters
        ----------
        block_id : BlockNumberOrTagOrHash

        transaction_detail_flag : typing.Optional[bool]
            A flag indicating whether to include full transaction details or just the hashes.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Block]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"eth/v1/block/{encode_path_param(block_id)}",
            method="GET",
            params={
                "transactionDetailFlag": transaction_detail_flag,
            },
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
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def get_block_receipts(
        self, block_id: BlockNumberOrTagOrHash, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[BlockReceiptsResponse]:
        """
        Returns all transaction receipts for a given block.
        ### Why is this useful?
        Replaces the `eth_getBlockReceipts` RPC method.
        ### How to verify response?
        - RLP encode each receipt and keccak-256 hash these encoded receipts.
        - Construct a Merkle Patricia Trie (MPT) from these hashes.
        - Verify the root of the constructed MPT against the trusted block's receipt root.

        Parameters
        ----------
        block_id : BlockNumberOrTagOrHash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BlockReceiptsResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"eth/v1/block/{encode_path_param(block_id)}/receipts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    BlockReceiptsResponse,
                    parse_obj_as(
                        type_=BlockReceiptsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def send_raw_transaction(
        self, *, bytes: typing.Optional[Bytes] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SendRawTxResponse]:
        """
        Creates a new message call transaction or a contract creation for signed transactions.
        ### Why is this useful?
        Replaces the `eth_sendRawTransaction` RPC method.

        Parameters
        ----------
        bytes : typing.Optional[Bytes]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SendRawTxResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "eth/v1/sendRawTransaction",
            method="POST",
            json={
                "bytes": bytes,
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
                    SendRawTxResponse,
                    parse_obj_as(
                        type_=SendRawTxResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def create_new_filter(
        self,
        *,
        kind: typing.Optional[NewFilterRequestKind] = OMIT,
        filter: typing.Optional[Filter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NewFilterResponse]:
        """
        Creates a filter in the node, to notify when the state changes.

        State changes can be of three types: logs, new blocks and pending transactions.

        To check if the state has changed, query `/filterChanges/{filterId}`.
        ### Why is this useful?
        Replaces the `eth_newFilter`, `eth_newBlockFilter` and `eth_newPendingTransactionFilter` RPC methods.

        Parameters
        ----------
        kind : typing.Optional[NewFilterRequestKind]

        filter : typing.Optional[Filter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NewFilterResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "eth/v1/filter",
            method="POST",
            json={
                "kind": kind,
                "filter": convert_and_respect_annotation_metadata(object_=filter, annotation=Filter, direction="write"),
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
                    NewFilterResponse,
                    parse_obj_as(
                        type_=NewFilterResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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

    async def uninstall_a_filter(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UninstallFilterResponse]:
        """
        Uninstalls a filter with given id.
        ### Why is this useful?
        Replaces the `eth_uninstallFilter` RPC method.

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UninstallFilterResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"eth/v1/filter/{encode_path_param(filter_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UninstallFilterResponse,
                    parse_obj_as(
                        type_=UninstallFilterResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ErrorResponse,
                        parse_obj_as(
                            type_=ErrorResponse,
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
