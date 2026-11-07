

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
from ..types.chain_index import ChainIndex
from ..types.currency import Currency
from ..types.event import Event
from ..types.file_contract import FileContract
from ..types.file_contract_revision import FileContractRevision
from ..types.siacoin_input import SiacoinInput
from ..types.siacoin_output_with_id import SiacoinOutputWithId
from ..types.siafund_input import SiafundInput
from ..types.siafund_output_with_id import SiafundOutputWithId
from ..types.storage_proof import StorageProof
from ..types.transaction import Transaction
from ..types.transaction_id import TransactionId
from ..types.transaction_signature import TransactionSignature
from ..types.txpool_broadcast_response import TxpoolBroadcastResponse
from ..types.txpool_transactions_response import TxpoolTransactionsResponse
from ..types.txpool_update_v2transactions_response import TxpoolUpdateV2TransactionsResponse
from ..types.v2transaction import V2Transaction
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawTxpoolClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_txpool_transactions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TxpoolTransactionsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TxpoolTransactionsResponse]
            Current contents of the transaction pools.
        """
        _response = self._client_wrapper.httpx_client.request(
            "txpool/transactions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TxpoolTransactionsResponse,
                    parse_obj_as(
                        type_=TxpoolTransactionsResponse,
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

    def post_txpool_v2transactions_basis(
        self,
        *,
        basis: ChainIndex,
        target: ChainIndex,
        transactions: typing.Sequence[V2Transaction],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TxpoolUpdateV2TransactionsResponse]:
        """
        Adjusts a v2 transaction set from one basis chain index to another. Use this to keep proofs and references valid when the chain advances.

        Parameters
        ----------
        basis : ChainIndex

        target : ChainIndex

        transactions : typing.Sequence[V2Transaction]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TxpoolUpdateV2TransactionsResponse]
            Updated transaction set anchored at the target basis.
        """
        _response = self._client_wrapper.httpx_client.request(
            "txpool/transactions/v2/basis",
            method="POST",
            json={
                "basis": convert_and_respect_annotation_metadata(
                    object_=basis, annotation=ChainIndex, direction="write"
                ),
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=ChainIndex, direction="write"
                ),
                "transactions": convert_and_respect_annotation_metadata(
                    object_=transactions, annotation=typing.Sequence[V2Transaction], direction="write"
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
                    TxpoolUpdateV2TransactionsResponse,
                    parse_obj_as(
                        type_=TxpoolUpdateV2TransactionsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def get_txpool_fee(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Currency]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Currency]
            Fee rate recommended for prompt confirmation.
        """
        _response = self._client_wrapper.httpx_client.request(
            "txpool/fee",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Currency,
                    parse_obj_as(
                        type_=Currency,
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

    def post_txpool_parents(
        self,
        *,
        id: TransactionId,
        siacoin_inputs: typing.Optional[typing.Sequence[SiacoinInput]] = OMIT,
        siacoin_outputs: typing.Optional[typing.Sequence[SiacoinOutputWithId]] = OMIT,
        file_contracts: typing.Optional[typing.Sequence[FileContract]] = OMIT,
        file_contract_revisions: typing.Optional[typing.Sequence[FileContractRevision]] = OMIT,
        storage_proofs: typing.Optional[typing.Sequence[StorageProof]] = OMIT,
        siafund_inputs: typing.Optional[typing.Sequence[SiafundInput]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[SiafundOutputWithId]] = OMIT,
        miner_fees: typing.Optional[typing.Sequence[Currency]] = OMIT,
        arbitrary_data: typing.Optional[typing.Sequence[str]] = OMIT,
        signatures: typing.Optional[typing.Sequence[TransactionSignature]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[Transaction]]:
        """
        Returns unconfirmed parent transactions required to validate the supplied transaction.

        Parameters
        ----------
        id : TransactionId

        siacoin_inputs : typing.Optional[typing.Sequence[SiacoinInput]]

        siacoin_outputs : typing.Optional[typing.Sequence[SiacoinOutputWithId]]

        file_contracts : typing.Optional[typing.Sequence[FileContract]]

        file_contract_revisions : typing.Optional[typing.Sequence[FileContractRevision]]

        storage_proofs : typing.Optional[typing.Sequence[StorageProof]]

        siafund_inputs : typing.Optional[typing.Sequence[SiafundInput]]

        siafund_outputs : typing.Optional[typing.Sequence[SiafundOutputWithId]]

        miner_fees : typing.Optional[typing.Sequence[Currency]]

        arbitrary_data : typing.Optional[typing.Sequence[str]]
            Arbitrary data entries encoded as base64 strings.

        signatures : typing.Optional[typing.Sequence[TransactionSignature]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Transaction]]
            Parent transactions that must be included ahead of the supplied transaction.
        """
        _response = self._client_wrapper.httpx_client.request(
            "txpool/parents",
            method="POST",
            json={
                "id": id,
                "siacoinInputs": convert_and_respect_annotation_metadata(
                    object_=siacoin_inputs, annotation=typing.Sequence[SiacoinInput], direction="write"
                ),
                "siacoinOutputs": convert_and_respect_annotation_metadata(
                    object_=siacoin_outputs, annotation=typing.Sequence[SiacoinOutputWithId], direction="write"
                ),
                "fileContracts": convert_and_respect_annotation_metadata(
                    object_=file_contracts, annotation=typing.Sequence[FileContract], direction="write"
                ),
                "fileContractRevisions": convert_and_respect_annotation_metadata(
                    object_=file_contract_revisions, annotation=typing.Sequence[FileContractRevision], direction="write"
                ),
                "storageProofs": convert_and_respect_annotation_metadata(
                    object_=storage_proofs, annotation=typing.Sequence[StorageProof], direction="write"
                ),
                "siafundInputs": convert_and_respect_annotation_metadata(
                    object_=siafund_inputs, annotation=typing.Sequence[SiafundInput], direction="write"
                ),
                "siafundOutputs": convert_and_respect_annotation_metadata(
                    object_=siafund_outputs, annotation=typing.Sequence[SiafundOutputWithId], direction="write"
                ),
                "minerFees": miner_fees,
                "arbitraryData": arbitrary_data,
                "signatures": convert_and_respect_annotation_metadata(
                    object_=signatures, annotation=typing.Sequence[TransactionSignature], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Transaction],
                    parse_obj_as(
                        type_=typing.List[Transaction],
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

    def post_txpool_broadcast(
        self,
        *,
        basis: typing.Optional[ChainIndex] = OMIT,
        transactions: typing.Optional[typing.Sequence[Transaction]] = OMIT,
        v2transactions: typing.Optional[typing.Sequence[V2Transaction]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TxpoolBroadcastResponse]:
        """
        Broadcasts v1 or v2 transaction sets. Walletd may augment the submitted transactions with missing parents or overwritten proofs before sending them to peers.

        Parameters
        ----------
        basis : typing.Optional[ChainIndex]

        transactions : typing.Optional[typing.Sequence[Transaction]]
            v1 transactions to broadcast.

        v2transactions : typing.Optional[typing.Sequence[V2Transaction]]
            v2 transactions to broadcast.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TxpoolBroadcastResponse]
            Transactions accepted by the pool and broadcast to peers.
        """
        _response = self._client_wrapper.httpx_client.request(
            "txpool/broadcast",
            method="POST",
            json={
                "basis": convert_and_respect_annotation_metadata(
                    object_=basis, annotation=ChainIndex, direction="write"
                ),
                "transactions": convert_and_respect_annotation_metadata(
                    object_=transactions, annotation=typing.Sequence[Transaction], direction="write"
                ),
                "v2transactions": convert_and_respect_annotation_metadata(
                    object_=v2transactions, annotation=typing.Sequence[V2Transaction], direction="write"
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
                    TxpoolBroadcastResponse,
                    parse_obj_as(
                        type_=TxpoolBroadcastResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def get_txpool_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Event]]:
        """
        Returns unconfirmed wallet events backed by transactions in the pool.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Event]]
            Pending wallet events derived from the transaction pool.
        """
        _response = self._client_wrapper.httpx_client.request(
            "txpool/events",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
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


class AsyncRawTxpoolClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_txpool_transactions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TxpoolTransactionsResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TxpoolTransactionsResponse]
            Current contents of the transaction pools.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "txpool/transactions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TxpoolTransactionsResponse,
                    parse_obj_as(
                        type_=TxpoolTransactionsResponse,
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

    async def post_txpool_v2transactions_basis(
        self,
        *,
        basis: ChainIndex,
        target: ChainIndex,
        transactions: typing.Sequence[V2Transaction],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TxpoolUpdateV2TransactionsResponse]:
        """
        Adjusts a v2 transaction set from one basis chain index to another. Use this to keep proofs and references valid when the chain advances.

        Parameters
        ----------
        basis : ChainIndex

        target : ChainIndex

        transactions : typing.Sequence[V2Transaction]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TxpoolUpdateV2TransactionsResponse]
            Updated transaction set anchored at the target basis.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "txpool/transactions/v2/basis",
            method="POST",
            json={
                "basis": convert_and_respect_annotation_metadata(
                    object_=basis, annotation=ChainIndex, direction="write"
                ),
                "target": convert_and_respect_annotation_metadata(
                    object_=target, annotation=ChainIndex, direction="write"
                ),
                "transactions": convert_and_respect_annotation_metadata(
                    object_=transactions, annotation=typing.Sequence[V2Transaction], direction="write"
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
                    TxpoolUpdateV2TransactionsResponse,
                    parse_obj_as(
                        type_=TxpoolUpdateV2TransactionsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def get_txpool_fee(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Currency]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Currency]
            Fee rate recommended for prompt confirmation.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "txpool/fee",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Currency,
                    parse_obj_as(
                        type_=Currency,
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

    async def post_txpool_parents(
        self,
        *,
        id: TransactionId,
        siacoin_inputs: typing.Optional[typing.Sequence[SiacoinInput]] = OMIT,
        siacoin_outputs: typing.Optional[typing.Sequence[SiacoinOutputWithId]] = OMIT,
        file_contracts: typing.Optional[typing.Sequence[FileContract]] = OMIT,
        file_contract_revisions: typing.Optional[typing.Sequence[FileContractRevision]] = OMIT,
        storage_proofs: typing.Optional[typing.Sequence[StorageProof]] = OMIT,
        siafund_inputs: typing.Optional[typing.Sequence[SiafundInput]] = OMIT,
        siafund_outputs: typing.Optional[typing.Sequence[SiafundOutputWithId]] = OMIT,
        miner_fees: typing.Optional[typing.Sequence[Currency]] = OMIT,
        arbitrary_data: typing.Optional[typing.Sequence[str]] = OMIT,
        signatures: typing.Optional[typing.Sequence[TransactionSignature]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[Transaction]]:
        """
        Returns unconfirmed parent transactions required to validate the supplied transaction.

        Parameters
        ----------
        id : TransactionId

        siacoin_inputs : typing.Optional[typing.Sequence[SiacoinInput]]

        siacoin_outputs : typing.Optional[typing.Sequence[SiacoinOutputWithId]]

        file_contracts : typing.Optional[typing.Sequence[FileContract]]

        file_contract_revisions : typing.Optional[typing.Sequence[FileContractRevision]]

        storage_proofs : typing.Optional[typing.Sequence[StorageProof]]

        siafund_inputs : typing.Optional[typing.Sequence[SiafundInput]]

        siafund_outputs : typing.Optional[typing.Sequence[SiafundOutputWithId]]

        miner_fees : typing.Optional[typing.Sequence[Currency]]

        arbitrary_data : typing.Optional[typing.Sequence[str]]
            Arbitrary data entries encoded as base64 strings.

        signatures : typing.Optional[typing.Sequence[TransactionSignature]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Transaction]]
            Parent transactions that must be included ahead of the supplied transaction.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "txpool/parents",
            method="POST",
            json={
                "id": id,
                "siacoinInputs": convert_and_respect_annotation_metadata(
                    object_=siacoin_inputs, annotation=typing.Sequence[SiacoinInput], direction="write"
                ),
                "siacoinOutputs": convert_and_respect_annotation_metadata(
                    object_=siacoin_outputs, annotation=typing.Sequence[SiacoinOutputWithId], direction="write"
                ),
                "fileContracts": convert_and_respect_annotation_metadata(
                    object_=file_contracts, annotation=typing.Sequence[FileContract], direction="write"
                ),
                "fileContractRevisions": convert_and_respect_annotation_metadata(
                    object_=file_contract_revisions, annotation=typing.Sequence[FileContractRevision], direction="write"
                ),
                "storageProofs": convert_and_respect_annotation_metadata(
                    object_=storage_proofs, annotation=typing.Sequence[StorageProof], direction="write"
                ),
                "siafundInputs": convert_and_respect_annotation_metadata(
                    object_=siafund_inputs, annotation=typing.Sequence[SiafundInput], direction="write"
                ),
                "siafundOutputs": convert_and_respect_annotation_metadata(
                    object_=siafund_outputs, annotation=typing.Sequence[SiafundOutputWithId], direction="write"
                ),
                "minerFees": miner_fees,
                "arbitraryData": arbitrary_data,
                "signatures": convert_and_respect_annotation_metadata(
                    object_=signatures, annotation=typing.Sequence[TransactionSignature], direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Transaction],
                    parse_obj_as(
                        type_=typing.List[Transaction],
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

    async def post_txpool_broadcast(
        self,
        *,
        basis: typing.Optional[ChainIndex] = OMIT,
        transactions: typing.Optional[typing.Sequence[Transaction]] = OMIT,
        v2transactions: typing.Optional[typing.Sequence[V2Transaction]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TxpoolBroadcastResponse]:
        """
        Broadcasts v1 or v2 transaction sets. Walletd may augment the submitted transactions with missing parents or overwritten proofs before sending them to peers.

        Parameters
        ----------
        basis : typing.Optional[ChainIndex]

        transactions : typing.Optional[typing.Sequence[Transaction]]
            v1 transactions to broadcast.

        v2transactions : typing.Optional[typing.Sequence[V2Transaction]]
            v2 transactions to broadcast.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TxpoolBroadcastResponse]
            Transactions accepted by the pool and broadcast to peers.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "txpool/broadcast",
            method="POST",
            json={
                "basis": convert_and_respect_annotation_metadata(
                    object_=basis, annotation=ChainIndex, direction="write"
                ),
                "transactions": convert_and_respect_annotation_metadata(
                    object_=transactions, annotation=typing.Sequence[Transaction], direction="write"
                ),
                "v2transactions": convert_and_respect_annotation_metadata(
                    object_=v2transactions, annotation=typing.Sequence[V2Transaction], direction="write"
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
                    TxpoolBroadcastResponse,
                    parse_obj_as(
                        type_=TxpoolBroadcastResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def get_txpool_events(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Event]]:
        """
        Returns unconfirmed wallet events backed by transactions in the pool.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Event]]
            Pending wallet events derived from the transaction pool.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "txpool/events",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Event],
                    parse_obj_as(
                        type_=typing.List[Event],
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
