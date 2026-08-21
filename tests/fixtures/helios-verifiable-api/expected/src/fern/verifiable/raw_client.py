

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
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..types.account_response import AccountResponse
from ..types.address import Address
from ..types.block_number_or_tag_or_hash import BlockNumberOrTagOrHash
from ..types.bytes_max32 import BytesMax32
from ..types.error_response import ErrorResponse
from ..types.extended_access_list_response import ExtendedAccessListResponse
from ..types.filter_changes_response import FilterChangesResponse
from ..types.filter_logs_response import FilterLogsResponse
from ..types.filter_topic import FilterTopic
from ..types.generic_transaction import GenericTransaction
from ..types.get_eth_v1proof_logs_request_address import GetEthV1ProofLogsRequestAddress
from ..types.hash32 import Hash32
from ..types.logs_response import LogsResponse
from ..types.transaction_receipt_response import TransactionReceiptResponse
from ..types.uint import Uint
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawVerifiableClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_account_information(
        self,
        address: Address,
        *,
        include_code: typing.Optional[bool] = None,
        storage_slots: typing.Optional[typing.Union[BytesMax32, typing.Sequence[BytesMax32]]] = None,
        block: typing.Optional[BlockNumberOrTagOrHash] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AccountResponse]:
        """
        Returns information about an address along with its EIP-1186 account proof.
        ### Why is this useful?
        Replaces the `eth_getProof`, `eth_getTransactionCount`, `eth_getBalance`, `eth_getCode`, and `eth_getStorageAt` RPC methods.
        ### How to verify response?
        - RLP encode the `TrieAccount` struct and keccak-256 hash it.
        - Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
        - For each item in `storageProof`, verify the given leaf’s Merkle Proof against the `storageHash`

        Parameters
        ----------
        address : Address
            The address of the account.

        include_code : typing.Optional[bool]
            A flag indicating whether to include the account's code.

        storage_slots : typing.Optional[typing.Union[BytesMax32, typing.Sequence[BytesMax32]]]
            A list of storage positions (in hex) to include in the proof.

        block : typing.Optional[BlockNumberOrTagOrHash]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AccountResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"eth/v1/proof/account/{encode_path_param(address)}",
            method="GET",
            params={
                "includeCode": include_code,
                "storageSlots": storage_slots,
                "block": block,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountResponse,
                    parse_obj_as(
                        type_=AccountResponse,
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

    def get_transaction_receipt(
        self, tx_hash: Hash32, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TransactionReceiptResponse]:
        """
        Returns the receipt of a transaction along with a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getTransactionReceipt` RPC method.
        ### How to verify response?
        - RLP encode the given receipt and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        tx_hash : Hash32
            The hash of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TransactionReceiptResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"eth/v1/proof/transaction/{encode_path_param(tx_hash)}/receipt",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransactionReceiptResponse,
                    parse_obj_as(
                        type_=TransactionReceiptResponse,
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

    def get_logs(
        self,
        *,
        from_block: typing.Optional[Uint] = None,
        to_block: typing.Optional[Uint] = None,
        block_hash: typing.Optional[Hash32] = None,
        address: typing.Optional[GetEthV1ProofLogsRequestAddress] = None,
        topic0: typing.Optional[FilterTopic] = None,
        topic1: typing.Optional[FilterTopic] = None,
        topic2: typing.Optional[FilterTopic] = None,
        topic3: typing.Optional[FilterTopic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[LogsResponse]:
        """
        Returns an array of all logs matching the given filter object.
        Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getLogs` RPC method.
        ### How to verify response?
        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        from_block : typing.Optional[Uint]
            Starting block number or tag.

        to_block : typing.Optional[Uint]
            Ending block number or tag.

        block_hash : typing.Optional[Hash32]
            Block hash. If present, fromBlock and toBlock are not allowed.

        address : typing.Optional[GetEthV1ProofLogsRequestAddress]
            Contract address or a list of addresses from which logs should originate.

        topic0 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic1 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic2 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic3 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[LogsResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "eth/v1/proof/logs",
            method="GET",
            params={
                "fromBlock": from_block,
                "toBlock": to_block,
                "blockHash": block_hash,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=GetEthV1ProofLogsRequestAddress, direction="write"
                ),
                "topic0": convert_and_respect_annotation_metadata(
                    object_=topic0, annotation=typing.Optional[FilterTopic], direction="write"
                ),
                "topic1": convert_and_respect_annotation_metadata(
                    object_=topic1, annotation=typing.Optional[FilterTopic], direction="write"
                ),
                "topic2": convert_and_respect_annotation_metadata(
                    object_=topic2, annotation=typing.Optional[FilterTopic], direction="write"
                ),
                "topic3": convert_and_respect_annotation_metadata(
                    object_=topic3, annotation=typing.Optional[FilterTopic], direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogsResponse,
                    parse_obj_as(
                        type_=LogsResponse,
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

    def get_filter_logs(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FilterLogsResponse]:
        """
        Returns an array of all logs matching the filter with given id.
        Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getFilterLogs` RPC method.
        ### How to verify response?
        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilterLogsResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"eth/v1/proof/filterLogs/{encode_path_param(filter_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilterLogsResponse,
                    parse_obj_as(
                        type_=FilterLogsResponse,
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

    def get_filter_changes(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FilterChangesResponse]:
        """
        Returns the changes since the last poll for a given filter id. If filter is of logs type, then corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getFilterChanges` RPC method.
        ### How to verify response?
        > Note: Only applicable for filters of logs type.

        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilterChangesResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"eth/v1/proof/filterChanges/{encode_path_param(filter_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilterChangesResponse,
                    parse_obj_as(
                        type_=FilterChangesResponse,
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

    def create_extended_access_list(
        self,
        *,
        tx: typing.Optional[GenericTransaction] = OMIT,
        validate_tx: typing.Optional[bool] = OMIT,
        block: typing.Optional[BlockNumberOrTagOrHash] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExtendedAccessListResponse]:
        """
        Returns a list of all addresses and storage keys (along with their EIP-1186 proofs) that are accessed by a given transaction.

        It's an extended list because it includes the `from`, `to` and `block.beneficiary` addresses as well.
        ### Why is this useful?
        Replaces the `eth_createAccessList` RPC method.
        ### How to verify response?
        For each account:
        - RLP encode the `TrieAccount` struct and keccak-256 hash it.
        - Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
        - For each item in `storageProof`: verify the given leaf’s Merkle Proof against the `storageHash`.

        Parameters
        ----------
        tx : typing.Optional[GenericTransaction]

        validate_tx : typing.Optional[bool]
            A flag indicating whether to validate the transaction (such as enforcing gas limit).

        block : typing.Optional[BlockNumberOrTagOrHash]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExtendedAccessListResponse]
            Success response
        """
        _response = self._client_wrapper.httpx_client.request(
            "eth/v1/proof/createExtendedAccessList",
            method="POST",
            json={
                "tx": convert_and_respect_annotation_metadata(
                    object_=tx, annotation=GenericTransaction, direction="write"
                ),
                "validateTx": validate_tx,
                "block": convert_and_respect_annotation_metadata(
                    object_=block, annotation=BlockNumberOrTagOrHash, direction="write"
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
                    ExtendedAccessListResponse,
                    parse_obj_as(
                        type_=ExtendedAccessListResponse,
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


class AsyncRawVerifiableClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_account_information(
        self,
        address: Address,
        *,
        include_code: typing.Optional[bool] = None,
        storage_slots: typing.Optional[typing.Union[BytesMax32, typing.Sequence[BytesMax32]]] = None,
        block: typing.Optional[BlockNumberOrTagOrHash] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AccountResponse]:
        """
        Returns information about an address along with its EIP-1186 account proof.
        ### Why is this useful?
        Replaces the `eth_getProof`, `eth_getTransactionCount`, `eth_getBalance`, `eth_getCode`, and `eth_getStorageAt` RPC methods.
        ### How to verify response?
        - RLP encode the `TrieAccount` struct and keccak-256 hash it.
        - Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
        - For each item in `storageProof`, verify the given leaf’s Merkle Proof against the `storageHash`

        Parameters
        ----------
        address : Address
            The address of the account.

        include_code : typing.Optional[bool]
            A flag indicating whether to include the account's code.

        storage_slots : typing.Optional[typing.Union[BytesMax32, typing.Sequence[BytesMax32]]]
            A list of storage positions (in hex) to include in the proof.

        block : typing.Optional[BlockNumberOrTagOrHash]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AccountResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"eth/v1/proof/account/{encode_path_param(address)}",
            method="GET",
            params={
                "includeCode": include_code,
                "storageSlots": storage_slots,
                "block": block,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AccountResponse,
                    parse_obj_as(
                        type_=AccountResponse,
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

    async def get_transaction_receipt(
        self, tx_hash: Hash32, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TransactionReceiptResponse]:
        """
        Returns the receipt of a transaction along with a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getTransactionReceipt` RPC method.
        ### How to verify response?
        - RLP encode the given receipt and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        tx_hash : Hash32
            The hash of the transaction.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TransactionReceiptResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"eth/v1/proof/transaction/{encode_path_param(tx_hash)}/receipt",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TransactionReceiptResponse,
                    parse_obj_as(
                        type_=TransactionReceiptResponse,
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

    async def get_logs(
        self,
        *,
        from_block: typing.Optional[Uint] = None,
        to_block: typing.Optional[Uint] = None,
        block_hash: typing.Optional[Hash32] = None,
        address: typing.Optional[GetEthV1ProofLogsRequestAddress] = None,
        topic0: typing.Optional[FilterTopic] = None,
        topic1: typing.Optional[FilterTopic] = None,
        topic2: typing.Optional[FilterTopic] = None,
        topic3: typing.Optional[FilterTopic] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[LogsResponse]:
        """
        Returns an array of all logs matching the given filter object.
        Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getLogs` RPC method.
        ### How to verify response?
        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        from_block : typing.Optional[Uint]
            Starting block number or tag.

        to_block : typing.Optional[Uint]
            Ending block number or tag.

        block_hash : typing.Optional[Hash32]
            Block hash. If present, fromBlock and toBlock are not allowed.

        address : typing.Optional[GetEthV1ProofLogsRequestAddress]
            Contract address or a list of addresses from which logs should originate.

        topic0 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic1 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic2 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        topic3 : typing.Optional[FilterTopic]
            32 Bytes DATA topic(s).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[LogsResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "eth/v1/proof/logs",
            method="GET",
            params={
                "fromBlock": from_block,
                "toBlock": to_block,
                "blockHash": block_hash,
                "address": convert_and_respect_annotation_metadata(
                    object_=address, annotation=GetEthV1ProofLogsRequestAddress, direction="write"
                ),
                "topic0": convert_and_respect_annotation_metadata(
                    object_=topic0, annotation=typing.Optional[FilterTopic], direction="write"
                ),
                "topic1": convert_and_respect_annotation_metadata(
                    object_=topic1, annotation=typing.Optional[FilterTopic], direction="write"
                ),
                "topic2": convert_and_respect_annotation_metadata(
                    object_=topic2, annotation=typing.Optional[FilterTopic], direction="write"
                ),
                "topic3": convert_and_respect_annotation_metadata(
                    object_=topic3, annotation=typing.Optional[FilterTopic], direction="write"
                ),
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    LogsResponse,
                    parse_obj_as(
                        type_=LogsResponse,
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

    async def get_filter_logs(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FilterLogsResponse]:
        """
        Returns an array of all logs matching the filter with given id.
        Corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getFilterLogs` RPC method.
        ### How to verify response?
        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf.

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilterLogsResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"eth/v1/proof/filterLogs/{encode_path_param(filter_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilterLogsResponse,
                    parse_obj_as(
                        type_=FilterLogsResponse,
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

    async def get_filter_changes(
        self, filter_id: Uint, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FilterChangesResponse]:
        """
        Returns the changes since the last poll for a given filter id. If filter is of logs type, then corresponding to each log, it also returns the transaction receipt and a Merkle Proof of its inclusion.
        ### Why is this useful?
        Replaces the `eth_getFilterChanges` RPC method.
        ### How to verify response?
        > Note: Only applicable for filters of logs type.

        For each log:
        - Find the corresponding transaction receipt for the log from the `receiptProofs` field. Let’s call this `receipt`.
        - Ensure that this log entry is included in the `receipt.logs` array.
        - RLP encode the `receipt` and keccak-256 hash it.
        - Verify the given `receiptProof` against the trusted block's receipt root with the given receipt's hash as the leaf

        Parameters
        ----------
        filter_id : Uint
            Filter identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilterChangesResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"eth/v1/proof/filterChanges/{encode_path_param(filter_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilterChangesResponse,
                    parse_obj_as(
                        type_=FilterChangesResponse,
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

    async def create_extended_access_list(
        self,
        *,
        tx: typing.Optional[GenericTransaction] = OMIT,
        validate_tx: typing.Optional[bool] = OMIT,
        block: typing.Optional[BlockNumberOrTagOrHash] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExtendedAccessListResponse]:
        """
        Returns a list of all addresses and storage keys (along with their EIP-1186 proofs) that are accessed by a given transaction.

        It's an extended list because it includes the `from`, `to` and `block.beneficiary` addresses as well.
        ### Why is this useful?
        Replaces the `eth_createAccessList` RPC method.
        ### How to verify response?
        For each account:
        - RLP encode the `TrieAccount` struct and keccak-256 hash it.
        - Verify the given `accountProof` against the trusted block's state root using the address as the key (path) and the hashed account as the value (leaf).
        - For each item in `storageProof`: verify the given leaf’s Merkle Proof against the `storageHash`.

        Parameters
        ----------
        tx : typing.Optional[GenericTransaction]

        validate_tx : typing.Optional[bool]
            A flag indicating whether to validate the transaction (such as enforcing gas limit).

        block : typing.Optional[BlockNumberOrTagOrHash]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExtendedAccessListResponse]
            Success response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "eth/v1/proof/createExtendedAccessList",
            method="POST",
            json={
                "tx": convert_and_respect_annotation_metadata(
                    object_=tx, annotation=GenericTransaction, direction="write"
                ),
                "validateTx": validate_tx,
                "block": convert_and_respect_annotation_metadata(
                    object_=block, annotation=BlockNumberOrTagOrHash, direction="write"
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
                    ExtendedAccessListResponse,
                    parse_obj_as(
                        type_=ExtendedAccessListResponse,
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
