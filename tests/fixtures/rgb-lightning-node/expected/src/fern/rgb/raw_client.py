

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.asset_balance_response import AssetBalanceResponse
from ..types.asset_filter import AssetFilter
from ..types.asset_metadata_response import AssetMetadataResponse
from ..types.asset_schema import AssetSchema
from ..types.assignment import Assignment
from ..types.decode_rgb_invoice_response import DecodeRgbInvoiceResponse
from ..types.empty_response import EmptyResponse
from ..types.fail_transfers_response import FailTransfersResponse
from ..types.get_asset_media_response import GetAssetMediaResponse
from ..types.get_consignment_response import GetConsignmentResponse
from ..types.inflate_response import InflateResponse
from ..types.issue_asset_cfa_response import IssueAssetCfaResponse
from ..types.issue_asset_ifa_response import IssueAssetIfaResponse
from ..types.issue_asset_nia_response import IssueAssetNiaResponse
from ..types.issue_asset_uda_response import IssueAssetUdaResponse
from ..types.list_assets_response import ListAssetsResponse
from ..types.list_transfers_response import ListTransfersResponse
from ..types.post_asset_media_response import PostAssetMediaResponse
from ..types.provide_out_of_band_ack_response import ProvideOutOfBandAckResponse
from ..types.provide_out_of_band_consignment_response import ProvideOutOfBandConsignmentResponse
from ..types.recipient import Recipient
from ..types.refresh_filter import RefreshFilter
from ..types.refresh_response import RefreshResponse
from ..types.rgb_invoice_response import RgbInvoiceResponse
from ..types.send_rgb_response import SendRgbResponse
from ..types.sync_options import SyncOptions
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRgbClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_the_balance_of_an_asset(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AssetBalanceResponse]:
        """
        Get the balance for the provided RGB asset

        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AssetBalanceResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "assetbalance",
            method="POST",
            json={
                "asset_id": asset_id,
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
                    AssetBalanceResponse,
                    parse_obj_as(
                        type_=AssetBalanceResponse,
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

    def get_the_metadata_of_an_asset(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AssetMetadataResponse]:
        """
        Get the metadata for the provided RGB asset

        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AssetMetadataResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "assetmetadata",
            method="POST",
            json={
                "asset_id": asset_id,
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
                    AssetMetadataResponse,
                    parse_obj_as(
                        type_=AssetMetadataResponse,
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

    def create_utx_os(
        self,
        *,
        up_to: bool,
        fee_rate: int,
        skip_sync: bool,
        num: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EmptyResponse]:
        """
        Create UTXOs to be used for RGB operations

        Parameters
        ----------
        up_to : bool

        fee_rate : int

        skip_sync : bool

        num : typing.Optional[int]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "createutxos",
            method="POST",
            json={
                "up_to": up_to,
                "num": num,
                "size": size,
                "fee_rate": fee_rate,
                "skip_sync": skip_sync,
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

    def decode_an_rgb_invoice(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DecodeRgbInvoiceResponse]:
        """
        Decode the provided RGB invoice string

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DecodeRgbInvoiceResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "decodergbinvoice",
            method="POST",
            json={
                "invoice": invoice,
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
                    DecodeRgbInvoiceResponse,
                    parse_obj_as(
                        type_=DecodeRgbInvoiceResponse,
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

    def fail_rgb_transfers(
        self,
        *,
        no_asset_only: bool,
        skip_sync: bool,
        batch_transfer_idx: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FailTransfersResponse]:
        """
        Set the status for eligible RGB transfers to `TransferStatus::Failed`.

        Parameters
        ----------
        no_asset_only : bool

        skip_sync : bool

        batch_transfer_idx : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FailTransfersResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "failtransfers",
            method="POST",
            json={
                "batch_transfer_idx": batch_transfer_idx,
                "no_asset_only": no_asset_only,
                "skip_sync": skip_sync,
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
                    FailTransfersResponse,
                    parse_obj_as(
                        type_=FailTransfersResponse,
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

    def get_an_asset_media(
        self, *, digest: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAssetMediaResponse]:
        """
        Get the hex string of the media bytes of the provided media digest

        Parameters
        ----------
        digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetAssetMediaResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "getassetmedia",
            method="POST",
            json={
                "digest": digest,
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
                    GetAssetMediaResponse,
                    parse_obj_as(
                        type_=GetAssetMediaResponse,
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

    def get_a_send_consignment(
        self, *, asset_id: str, txid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetConsignmentResponse]:
        """
        Get the hex string of the consignment bytes for a send transfer, identified by its asset ID and txid. Useful to hand the consignment to the counterparty out-of-band when the node filesystem is not accessible from the API caller.

        Parameters
        ----------
        asset_id : str

        txid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetConsignmentResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "getconsignment",
            method="POST",
            json={
                "asset_id": asset_id,
                "txid": txid,
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
                    GetConsignmentResponse,
                    parse_obj_as(
                        type_=GetConsignmentResponse,
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

    def inflate_rgb_assets(
        self,
        *,
        asset_id: str,
        inflation_amounts: typing.Sequence[int],
        fee_rate: int,
        min_confirmations: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InflateResponse]:
        """
        Inflate RGB assets on-chain

        Parameters
        ----------
        asset_id : str

        inflation_amounts : typing.Sequence[int]

        fee_rate : int

        min_confirmations : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InflateResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "inflate",
            method="POST",
            json={
                "asset_id": asset_id,
                "inflation_amounts": inflation_amounts,
                "fee_rate": fee_rate,
                "min_confirmations": min_confirmations,
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
                    InflateResponse,
                    parse_obj_as(
                        type_=InflateResponse,
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

    def issue_an_rgb_cfa_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        name: str,
        precision: int,
        details: typing.Optional[str] = OMIT,
        file_digest: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IssueAssetCfaResponse]:
        """
        Issue an RGB CFA asset. To provide a media first call the /postassetmedia API.

        Parameters
        ----------
        amounts : typing.Sequence[int]

        name : str

        precision : int

        details : typing.Optional[str]

        file_digest : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueAssetCfaResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "issueassetcfa",
            method="POST",
            json={
                "amounts": amounts,
                "name": name,
                "details": details,
                "precision": precision,
                "file_digest": file_digest,
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
                    IssueAssetCfaResponse,
                    parse_obj_as(
                        type_=IssueAssetCfaResponse,
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

    def issue_an_rgb_ifa_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        inflation_amounts: typing.Sequence[int],
        ticker: str,
        name: str,
        precision: int,
        reject_list_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IssueAssetIfaResponse]:
        """
        Issue an RGB IFA asset

        Parameters
        ----------
        amounts : typing.Sequence[int]

        inflation_amounts : typing.Sequence[int]

        ticker : str

        name : str

        precision : int

        reject_list_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueAssetIfaResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "issueassetifa",
            method="POST",
            json={
                "amounts": amounts,
                "inflation_amounts": inflation_amounts,
                "ticker": ticker,
                "name": name,
                "precision": precision,
                "reject_list_url": reject_list_url,
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
                    IssueAssetIfaResponse,
                    parse_obj_as(
                        type_=IssueAssetIfaResponse,
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

    def issue_an_rgb_nia_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        ticker: str,
        name: str,
        precision: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IssueAssetNiaResponse]:
        """
        Issue an RGB NIA asset

        Parameters
        ----------
        amounts : typing.Sequence[int]

        ticker : str

        name : str

        precision : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueAssetNiaResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "issueassetnia",
            method="POST",
            json={
                "amounts": amounts,
                "ticker": ticker,
                "name": name,
                "precision": precision,
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
                    IssueAssetNiaResponse,
                    parse_obj_as(
                        type_=IssueAssetNiaResponse,
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

    def issue_an_rgb_uda_asset(
        self,
        *,
        ticker: str,
        name: str,
        precision: int,
        attachments_file_digests: typing.Sequence[str],
        details: typing.Optional[str] = OMIT,
        media_file_digest: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[IssueAssetUdaResponse]:
        """
        Issue an RGB UDA asset. To provide a media first call the /postassetmedia API.

        Parameters
        ----------
        ticker : str

        name : str

        precision : int

        attachments_file_digests : typing.Sequence[str]

        details : typing.Optional[str]

        media_file_digest : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[IssueAssetUdaResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "issueassetuda",
            method="POST",
            json={
                "ticker": ticker,
                "name": name,
                "details": details,
                "precision": precision,
                "media_file_digest": media_file_digest,
                "attachments_file_digests": attachments_file_digests,
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
                    IssueAssetUdaResponse,
                    parse_obj_as(
                        type_=IssueAssetUdaResponse,
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

    def list_assets(
        self,
        *,
        filter_asset_schemas: typing.Sequence[AssetSchema],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAssetsResponse]:
        """
        List the node's RGB assets

        Parameters
        ----------
        filter_asset_schemas : typing.Sequence[AssetSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAssetsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "listassets",
            method="POST",
            json={
                "filter_asset_schemas": filter_asset_schemas,
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
                    ListAssetsResponse,
                    parse_obj_as(
                        type_=ListAssetsResponse,
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

    def list_transfers(
        self,
        *,
        asset_filter: AssetFilter,
        txid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListTransfersResponse]:
        """
        List the node's on-chain RGB transfers

        Parameters
        ----------
        asset_filter : AssetFilter

        txid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListTransfersResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "listtransfers",
            method="POST",
            json={
                "asset_filter": convert_and_respect_annotation_metadata(
                    object_=asset_filter, annotation=AssetFilter, direction="write"
                ),
                "txid": txid,
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
                    ListTransfersResponse,
                    parse_obj_as(
                        type_=ListTransfersResponse,
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

    def post_an_asset_media(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostAssetMediaResponse]:
        """
        Save the provided media

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetMediaResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "postassetmedia",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetMediaResponse,
                    parse_obj_as(
                        type_=PostAssetMediaResponse,
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

    def provide_an_out_of_band_ack(
        self, *, recipient_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvideOutOfBandAckResponse]:
        """
        Record the out-of-band ACK received from a recipient of an outgoing transfer

        Parameters
        ----------
        recipient_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvideOutOfBandAckResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "provideoutofbandack",
            method="POST",
            json={
                "recipient_id": recipient_id,
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
                    ProvideOutOfBandAckResponse,
                    parse_obj_as(
                        type_=ProvideOutOfBandAckResponse,
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

    def provide_an_out_of_band_consignment(
        self,
        *,
        file: core.File,
        media: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProvideOutOfBandConsignmentResponse]:
        """
        Provide a consignment received out-of-band, as a binary upload, along with any media files it references (one `media` field per file) The consignment is validated and the matching incoming transfer(s) are processed.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        media : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvideOutOfBandConsignmentResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "provideoutofbandconsignment",
            method="POST",
            data={},
            files={
                "file": file,
                **({"media": media} if media is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvideOutOfBandConsignmentResponse,
                    parse_obj_as(
                        type_=ProvideOutOfBandConsignmentResponse,
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

    def refresh_transfers(
        self,
        *,
        filter: typing.Sequence[RefreshFilter],
        skip_sync: bool,
        asset_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RefreshResponse]:
        """
        Refresh RGB pending transfers

        Parameters
        ----------
        filter : typing.Sequence[RefreshFilter]

        skip_sync : bool

        asset_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RefreshResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "refreshtransfers",
            method="POST",
            json={
                "asset_id": asset_id,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=typing.Sequence[RefreshFilter], direction="write"
                ),
                "skip_sync": skip_sync,
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
                    RefreshResponse,
                    parse_obj_as(
                        type_=RefreshResponse,
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

    def get_an_rgb_invoice(
        self,
        *,
        min_confirmations: int,
        expiration_timestamp: int,
        witness: bool,
        transport_endpoints: typing.Sequence[str],
        asset_id: typing.Optional[str] = OMIT,
        assignment: typing.Optional[Assignment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RgbInvoiceResponse]:
        """
        Get an RGB invoice to receive assets on-chain

        Parameters
        ----------
        min_confirmations : int

        expiration_timestamp : int

        witness : bool

        transport_endpoints : typing.Sequence[str]

        asset_id : typing.Optional[str]

        assignment : typing.Optional[Assignment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RgbInvoiceResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "rgbinvoice",
            method="POST",
            json={
                "min_confirmations": min_confirmations,
                "asset_id": asset_id,
                "assignment": convert_and_respect_annotation_metadata(
                    object_=assignment, annotation=typing.Optional[Assignment], direction="write"
                ),
                "expiration_timestamp": expiration_timestamp,
                "witness": witness,
                "transport_endpoints": transport_endpoints,
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
                    RgbInvoiceResponse,
                    parse_obj_as(
                        type_=RgbInvoiceResponse,
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

    def send_rgb_assets(
        self,
        *,
        donation: bool,
        fee_rate: int,
        min_confirmations: int,
        expiration_timestamp: int,
        recipient_map: typing.Dict[str, typing.Sequence[Recipient]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SendRgbResponse]:
        """
        Send RGB assets on-chain, supporting batch transfers to multiple recipients and/or multiple assets in a single transaction

        Parameters
        ----------
        donation : bool

        fee_rate : int

        min_confirmations : int

        expiration_timestamp : int

        recipient_map : typing.Dict[str, typing.Sequence[Recipient]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SendRgbResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "sendrgb",
            method="POST",
            json={
                "donation": donation,
                "fee_rate": fee_rate,
                "min_confirmations": min_confirmations,
                "expiration_timestamp": expiration_timestamp,
                "recipient_map": convert_and_respect_annotation_metadata(
                    object_=recipient_map, annotation=typing.Dict[str, typing.Sequence[Recipient]], direction="write"
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
                    SendRgbResponse,
                    parse_obj_as(
                        type_=SendRgbResponse,
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

    def sync_the_rgb_wallet(
        self, *, options: SyncOptions, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EmptyResponse]:
        """
        Sync the RGB wallet

        Parameters
        ----------
        options : SyncOptions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EmptyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "sync",
            method="POST",
            json={
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=SyncOptions, direction="write"
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


class AsyncRawRgbClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_the_balance_of_an_asset(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AssetBalanceResponse]:
        """
        Get the balance for the provided RGB asset

        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AssetBalanceResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assetbalance",
            method="POST",
            json={
                "asset_id": asset_id,
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
                    AssetBalanceResponse,
                    parse_obj_as(
                        type_=AssetBalanceResponse,
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

    async def get_the_metadata_of_an_asset(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AssetMetadataResponse]:
        """
        Get the metadata for the provided RGB asset

        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AssetMetadataResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assetmetadata",
            method="POST",
            json={
                "asset_id": asset_id,
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
                    AssetMetadataResponse,
                    parse_obj_as(
                        type_=AssetMetadataResponse,
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

    async def create_utx_os(
        self,
        *,
        up_to: bool,
        fee_rate: int,
        skip_sync: bool,
        num: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Create UTXOs to be used for RGB operations

        Parameters
        ----------
        up_to : bool

        fee_rate : int

        skip_sync : bool

        num : typing.Optional[int]

        size : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "createutxos",
            method="POST",
            json={
                "up_to": up_to,
                "num": num,
                "size": size,
                "fee_rate": fee_rate,
                "skip_sync": skip_sync,
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

    async def decode_an_rgb_invoice(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DecodeRgbInvoiceResponse]:
        """
        Decode the provided RGB invoice string

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DecodeRgbInvoiceResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "decodergbinvoice",
            method="POST",
            json={
                "invoice": invoice,
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
                    DecodeRgbInvoiceResponse,
                    parse_obj_as(
                        type_=DecodeRgbInvoiceResponse,
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

    async def fail_rgb_transfers(
        self,
        *,
        no_asset_only: bool,
        skip_sync: bool,
        batch_transfer_idx: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FailTransfersResponse]:
        """
        Set the status for eligible RGB transfers to `TransferStatus::Failed`.

        Parameters
        ----------
        no_asset_only : bool

        skip_sync : bool

        batch_transfer_idx : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FailTransfersResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "failtransfers",
            method="POST",
            json={
                "batch_transfer_idx": batch_transfer_idx,
                "no_asset_only": no_asset_only,
                "skip_sync": skip_sync,
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
                    FailTransfersResponse,
                    parse_obj_as(
                        type_=FailTransfersResponse,
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

    async def get_an_asset_media(
        self, *, digest: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAssetMediaResponse]:
        """
        Get the hex string of the media bytes of the provided media digest

        Parameters
        ----------
        digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetAssetMediaResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "getassetmedia",
            method="POST",
            json={
                "digest": digest,
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
                    GetAssetMediaResponse,
                    parse_obj_as(
                        type_=GetAssetMediaResponse,
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

    async def get_a_send_consignment(
        self, *, asset_id: str, txid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetConsignmentResponse]:
        """
        Get the hex string of the consignment bytes for a send transfer, identified by its asset ID and txid. Useful to hand the consignment to the counterparty out-of-band when the node filesystem is not accessible from the API caller.

        Parameters
        ----------
        asset_id : str

        txid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetConsignmentResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "getconsignment",
            method="POST",
            json={
                "asset_id": asset_id,
                "txid": txid,
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
                    GetConsignmentResponse,
                    parse_obj_as(
                        type_=GetConsignmentResponse,
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

    async def inflate_rgb_assets(
        self,
        *,
        asset_id: str,
        inflation_amounts: typing.Sequence[int],
        fee_rate: int,
        min_confirmations: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InflateResponse]:
        """
        Inflate RGB assets on-chain

        Parameters
        ----------
        asset_id : str

        inflation_amounts : typing.Sequence[int]

        fee_rate : int

        min_confirmations : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InflateResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inflate",
            method="POST",
            json={
                "asset_id": asset_id,
                "inflation_amounts": inflation_amounts,
                "fee_rate": fee_rate,
                "min_confirmations": min_confirmations,
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
                    InflateResponse,
                    parse_obj_as(
                        type_=InflateResponse,
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

    async def issue_an_rgb_cfa_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        name: str,
        precision: int,
        details: typing.Optional[str] = OMIT,
        file_digest: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IssueAssetCfaResponse]:
        """
        Issue an RGB CFA asset. To provide a media first call the /postassetmedia API.

        Parameters
        ----------
        amounts : typing.Sequence[int]

        name : str

        precision : int

        details : typing.Optional[str]

        file_digest : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueAssetCfaResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "issueassetcfa",
            method="POST",
            json={
                "amounts": amounts,
                "name": name,
                "details": details,
                "precision": precision,
                "file_digest": file_digest,
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
                    IssueAssetCfaResponse,
                    parse_obj_as(
                        type_=IssueAssetCfaResponse,
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

    async def issue_an_rgb_ifa_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        inflation_amounts: typing.Sequence[int],
        ticker: str,
        name: str,
        precision: int,
        reject_list_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IssueAssetIfaResponse]:
        """
        Issue an RGB IFA asset

        Parameters
        ----------
        amounts : typing.Sequence[int]

        inflation_amounts : typing.Sequence[int]

        ticker : str

        name : str

        precision : int

        reject_list_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueAssetIfaResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "issueassetifa",
            method="POST",
            json={
                "amounts": amounts,
                "inflation_amounts": inflation_amounts,
                "ticker": ticker,
                "name": name,
                "precision": precision,
                "reject_list_url": reject_list_url,
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
                    IssueAssetIfaResponse,
                    parse_obj_as(
                        type_=IssueAssetIfaResponse,
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

    async def issue_an_rgb_nia_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        ticker: str,
        name: str,
        precision: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IssueAssetNiaResponse]:
        """
        Issue an RGB NIA asset

        Parameters
        ----------
        amounts : typing.Sequence[int]

        ticker : str

        name : str

        precision : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueAssetNiaResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "issueassetnia",
            method="POST",
            json={
                "amounts": amounts,
                "ticker": ticker,
                "name": name,
                "precision": precision,
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
                    IssueAssetNiaResponse,
                    parse_obj_as(
                        type_=IssueAssetNiaResponse,
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

    async def issue_an_rgb_uda_asset(
        self,
        *,
        ticker: str,
        name: str,
        precision: int,
        attachments_file_digests: typing.Sequence[str],
        details: typing.Optional[str] = OMIT,
        media_file_digest: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[IssueAssetUdaResponse]:
        """
        Issue an RGB UDA asset. To provide a media first call the /postassetmedia API.

        Parameters
        ----------
        ticker : str

        name : str

        precision : int

        attachments_file_digests : typing.Sequence[str]

        details : typing.Optional[str]

        media_file_digest : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[IssueAssetUdaResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "issueassetuda",
            method="POST",
            json={
                "ticker": ticker,
                "name": name,
                "details": details,
                "precision": precision,
                "media_file_digest": media_file_digest,
                "attachments_file_digests": attachments_file_digests,
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
                    IssueAssetUdaResponse,
                    parse_obj_as(
                        type_=IssueAssetUdaResponse,
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

    async def list_assets(
        self,
        *,
        filter_asset_schemas: typing.Sequence[AssetSchema],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAssetsResponse]:
        """
        List the node's RGB assets

        Parameters
        ----------
        filter_asset_schemas : typing.Sequence[AssetSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAssetsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "listassets",
            method="POST",
            json={
                "filter_asset_schemas": filter_asset_schemas,
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
                    ListAssetsResponse,
                    parse_obj_as(
                        type_=ListAssetsResponse,
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

    async def list_transfers(
        self,
        *,
        asset_filter: AssetFilter,
        txid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListTransfersResponse]:
        """
        List the node's on-chain RGB transfers

        Parameters
        ----------
        asset_filter : AssetFilter

        txid : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListTransfersResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "listtransfers",
            method="POST",
            json={
                "asset_filter": convert_and_respect_annotation_metadata(
                    object_=asset_filter, annotation=AssetFilter, direction="write"
                ),
                "txid": txid,
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
                    ListTransfersResponse,
                    parse_obj_as(
                        type_=ListTransfersResponse,
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

    async def post_an_asset_media(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostAssetMediaResponse]:
        """
        Save the provided media

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetMediaResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "postassetmedia",
            method="POST",
            data={},
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetMediaResponse,
                    parse_obj_as(
                        type_=PostAssetMediaResponse,
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

    async def provide_an_out_of_band_ack(
        self, *, recipient_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvideOutOfBandAckResponse]:
        """
        Record the out-of-band ACK received from a recipient of an outgoing transfer

        Parameters
        ----------
        recipient_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvideOutOfBandAckResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "provideoutofbandack",
            method="POST",
            json={
                "recipient_id": recipient_id,
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
                    ProvideOutOfBandAckResponse,
                    parse_obj_as(
                        type_=ProvideOutOfBandAckResponse,
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

    async def provide_an_out_of_band_consignment(
        self,
        *,
        file: core.File,
        media: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProvideOutOfBandConsignmentResponse]:
        """
        Provide a consignment received out-of-band, as a binary upload, along with any media files it references (one `media` field per file) The consignment is validated and the matching incoming transfer(s) are processed.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        media : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvideOutOfBandConsignmentResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "provideoutofbandconsignment",
            method="POST",
            data={},
            files={
                "file": file,
                **({"media": media} if media is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvideOutOfBandConsignmentResponse,
                    parse_obj_as(
                        type_=ProvideOutOfBandConsignmentResponse,
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

    async def refresh_transfers(
        self,
        *,
        filter: typing.Sequence[RefreshFilter],
        skip_sync: bool,
        asset_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RefreshResponse]:
        """
        Refresh RGB pending transfers

        Parameters
        ----------
        filter : typing.Sequence[RefreshFilter]

        skip_sync : bool

        asset_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RefreshResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "refreshtransfers",
            method="POST",
            json={
                "asset_id": asset_id,
                "filter": convert_and_respect_annotation_metadata(
                    object_=filter, annotation=typing.Sequence[RefreshFilter], direction="write"
                ),
                "skip_sync": skip_sync,
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
                    RefreshResponse,
                    parse_obj_as(
                        type_=RefreshResponse,
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

    async def get_an_rgb_invoice(
        self,
        *,
        min_confirmations: int,
        expiration_timestamp: int,
        witness: bool,
        transport_endpoints: typing.Sequence[str],
        asset_id: typing.Optional[str] = OMIT,
        assignment: typing.Optional[Assignment] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RgbInvoiceResponse]:
        """
        Get an RGB invoice to receive assets on-chain

        Parameters
        ----------
        min_confirmations : int

        expiration_timestamp : int

        witness : bool

        transport_endpoints : typing.Sequence[str]

        asset_id : typing.Optional[str]

        assignment : typing.Optional[Assignment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RgbInvoiceResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "rgbinvoice",
            method="POST",
            json={
                "min_confirmations": min_confirmations,
                "asset_id": asset_id,
                "assignment": convert_and_respect_annotation_metadata(
                    object_=assignment, annotation=typing.Optional[Assignment], direction="write"
                ),
                "expiration_timestamp": expiration_timestamp,
                "witness": witness,
                "transport_endpoints": transport_endpoints,
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
                    RgbInvoiceResponse,
                    parse_obj_as(
                        type_=RgbInvoiceResponse,
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

    async def send_rgb_assets(
        self,
        *,
        donation: bool,
        fee_rate: int,
        min_confirmations: int,
        expiration_timestamp: int,
        recipient_map: typing.Dict[str, typing.Sequence[Recipient]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SendRgbResponse]:
        """
        Send RGB assets on-chain, supporting batch transfers to multiple recipients and/or multiple assets in a single transaction

        Parameters
        ----------
        donation : bool

        fee_rate : int

        min_confirmations : int

        expiration_timestamp : int

        recipient_map : typing.Dict[str, typing.Sequence[Recipient]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SendRgbResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sendrgb",
            method="POST",
            json={
                "donation": donation,
                "fee_rate": fee_rate,
                "min_confirmations": min_confirmations,
                "expiration_timestamp": expiration_timestamp,
                "recipient_map": convert_and_respect_annotation_metadata(
                    object_=recipient_map, annotation=typing.Dict[str, typing.Sequence[Recipient]], direction="write"
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
                    SendRgbResponse,
                    parse_obj_as(
                        type_=SendRgbResponse,
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

    async def sync_the_rgb_wallet(
        self, *, options: SyncOptions, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EmptyResponse]:
        """
        Sync the RGB wallet

        Parameters
        ----------
        options : SyncOptions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EmptyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "sync",
            method="POST",
            json={
                "options": convert_and_respect_annotation_metadata(
                    object_=options, annotation=SyncOptions, direction="write"
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
