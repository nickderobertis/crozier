

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawRgbClient, RawRgbClient


OMIT = typing.cast(typing.Any, ...)


class RgbClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRgbClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRgbClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRgbClient
        """
        return self._raw_client

    def get_the_balance_of_an_asset(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AssetBalanceResponse:
        """
        Get the balance for the provided RGB asset

        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetBalanceResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.get_the_balance_of_an_asset(
            asset_id="rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8",
        )
        """
        _response = self._raw_client.get_the_balance_of_an_asset(asset_id=asset_id, request_options=request_options)
        return _response.data

    def get_the_metadata_of_an_asset(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AssetMetadataResponse:
        """
        Get the metadata for the provided RGB asset

        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetMetadataResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.get_the_metadata_of_an_asset(
            asset_id="rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8",
        )
        """
        _response = self._raw_client.get_the_metadata_of_an_asset(asset_id=asset_id, request_options=request_options)
        return _response.data

    def create_utx_os(
        self,
        *,
        up_to: bool,
        fee_rate: int,
        skip_sync: bool,
        num: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
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
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.create_utx_os(
            up_to=False,
            fee_rate=5,
            skip_sync=False,
        )
        """
        _response = self._raw_client.create_utx_os(
            up_to=up_to, fee_rate=fee_rate, skip_sync=skip_sync, num=num, size=size, request_options=request_options
        )
        return _response.data

    def decode_an_rgb_invoice(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DecodeRgbInvoiceResponse:
        """
        Decode the provided RGB invoice string

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecodeRgbInvoiceResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.decode_an_rgb_invoice(
            invoice="rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/RWhwUfTMpuP2Zfx1~j4nswCANGeJrYOqDcKelaMV4zU/~/bcrt:utxob:cbgHUJ4e-7QyKY4U-Jsj5AZw-oI0gxZh-7fxQY2_-tFFUAZN-4CgpX?expiry=1749906951&endpoints=rpcs://proxy.iriswallet.com/0.2/json-rpc",
        )
        """
        _response = self._raw_client.decode_an_rgb_invoice(invoice=invoice, request_options=request_options)
        return _response.data

    def fail_rgb_transfers(
        self,
        *,
        no_asset_only: bool,
        skip_sync: bool,
        batch_transfer_idx: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FailTransfersResponse:
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
        FailTransfersResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.fail_rgb_transfers(
            no_asset_only=False,
            skip_sync=False,
        )
        """
        _response = self._raw_client.fail_rgb_transfers(
            no_asset_only=no_asset_only,
            skip_sync=skip_sync,
            batch_transfer_idx=batch_transfer_idx,
            request_options=request_options,
        )
        return _response.data

    def get_an_asset_media(
        self, *, digest: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAssetMediaResponse:
        """
        Get the hex string of the media bytes of the provided media digest

        Parameters
        ----------
        digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAssetMediaResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.get_an_asset_media(
            digest="5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03",
        )
        """
        _response = self._raw_client.get_an_asset_media(digest=digest, request_options=request_options)
        return _response.data

    def get_a_send_consignment(
        self, *, asset_id: str, txid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConsignmentResponse:
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
        GetConsignmentResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.get_a_send_consignment(
            asset_id="rgb:2dkSTbr-jFhznbPmo-TQafzswCN-av4gTsJjX-ttx6CNou5-M98k8Zt",
            txid="33cf3e42fb1c6faa0d47e6a498a9d4e5c56e8a06ea0d295c6d90e2b6c85f7a1e",
        )
        """
        _response = self._raw_client.get_a_send_consignment(
            asset_id=asset_id, txid=txid, request_options=request_options
        )
        return _response.data

    def inflate_rgb_assets(
        self,
        *,
        asset_id: str,
        inflation_amounts: typing.Sequence[int],
        fee_rate: int,
        min_confirmations: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InflateResponse:
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
        InflateResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.inflate_rgb_assets(
            asset_id="rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8",
            inflation_amounts=[100, 50],
            fee_rate=5,
            min_confirmations=1,
        )
        """
        _response = self._raw_client.inflate_rgb_assets(
            asset_id=asset_id,
            inflation_amounts=inflation_amounts,
            fee_rate=fee_rate,
            min_confirmations=min_confirmations,
            request_options=request_options,
        )
        return _response.data

    def issue_an_rgb_cfa_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        name: str,
        precision: int,
        details: typing.Optional[str] = OMIT,
        file_digest: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueAssetCfaResponse:
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
        IssueAssetCfaResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.issue_an_rgb_cfa_asset(
            amounts=[1000, 600],
            name="Tether",
            precision=0,
        )
        """
        _response = self._raw_client.issue_an_rgb_cfa_asset(
            amounts=amounts,
            name=name,
            precision=precision,
            details=details,
            file_digest=file_digest,
            request_options=request_options,
        )
        return _response.data

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
    ) -> IssueAssetIfaResponse:
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
        IssueAssetIfaResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.issue_an_rgb_ifa_asset(
            amounts=[1000, 600],
            inflation_amounts=[100, 50],
            ticker="USDT",
            name="Tether",
            precision=0,
        )
        """
        _response = self._raw_client.issue_an_rgb_ifa_asset(
            amounts=amounts,
            inflation_amounts=inflation_amounts,
            ticker=ticker,
            name=name,
            precision=precision,
            reject_list_url=reject_list_url,
            request_options=request_options,
        )
        return _response.data

    def issue_an_rgb_nia_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        ticker: str,
        name: str,
        precision: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueAssetNiaResponse:
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
        IssueAssetNiaResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.issue_an_rgb_nia_asset(
            amounts=[1000, 600],
            ticker="USDT",
            name="Tether",
            precision=0,
        )
        """
        _response = self._raw_client.issue_an_rgb_nia_asset(
            amounts=amounts, ticker=ticker, name=name, precision=precision, request_options=request_options
        )
        return _response.data

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
    ) -> IssueAssetUdaResponse:
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
        IssueAssetUdaResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.issue_an_rgb_uda_asset(
            ticker="UNI",
            name="Unique",
            precision=0,
            attachments_file_digests=[
                "5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03",
                "d7516e3a27cdf35aa9dcb323b5f556344ef7f57570be30b88de2bfd4ba339b1a",
            ],
        )
        """
        _response = self._raw_client.issue_an_rgb_uda_asset(
            ticker=ticker,
            name=name,
            precision=precision,
            attachments_file_digests=attachments_file_digests,
            details=details,
            media_file_digest=media_file_digest,
            request_options=request_options,
        )
        return _response.data

    def list_assets(
        self,
        *,
        filter_asset_schemas: typing.Sequence[AssetSchema],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAssetsResponse:
        """
        List the node's RGB assets

        Parameters
        ----------
        filter_asset_schemas : typing.Sequence[AssetSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAssetsResponse
            Successful operation

        Examples
        --------
        from fern import AssetSchema, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.list_assets(
            filter_asset_schemas=[
                AssetSchema.NIA,
                AssetSchema.UDA,
                AssetSchema.CFA,
                AssetSchema.IFA,
            ],
        )
        """
        _response = self._raw_client.list_assets(
            filter_asset_schemas=filter_asset_schemas, request_options=request_options
        )
        return _response.data

    def list_transfers(
        self,
        *,
        asset_filter: AssetFilter,
        txid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTransfersResponse:
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
        ListTransfersResponse
            Successful operation

        Examples
        --------
        from fern import AssetFilter_AnyOrNone, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.list_transfers(
            asset_filter=AssetFilter_AnyOrNone(),
        )
        """
        _response = self._raw_client.list_transfers(
            asset_filter=asset_filter, txid=txid, request_options=request_options
        )
        return _response.data

    def post_an_asset_media(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetMediaResponse:
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
        PostAssetMediaResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.post_an_asset_media()
        """
        _response = self._raw_client.post_an_asset_media(file=file, request_options=request_options)
        return _response.data

    def provide_an_out_of_band_ack(
        self, *, recipient_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvideOutOfBandAckResponse:
        """
        Record the out-of-band ACK received from a recipient of an outgoing transfer

        Parameters
        ----------
        recipient_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvideOutOfBandAckResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.provide_an_out_of_band_ack(
            recipient_id="utxob:2Bwv2Vx-t7VD8XjTh-9EMbpBFKh-J5HDFY4pj-eywu4tKKk-hjTvzJa",
        )
        """
        _response = self._raw_client.provide_an_out_of_band_ack(
            recipient_id=recipient_id, request_options=request_options
        )
        return _response.data

    def provide_an_out_of_band_consignment(
        self,
        *,
        file: core.File,
        media: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvideOutOfBandConsignmentResponse:
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
        ProvideOutOfBandConsignmentResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.provide_an_out_of_band_consignment()
        """
        _response = self._raw_client.provide_an_out_of_band_consignment(
            file=file, media=media, request_options=request_options
        )
        return _response.data

    def refresh_transfers(
        self,
        *,
        filter: typing.Sequence[RefreshFilter],
        skip_sync: bool,
        asset_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefreshResponse:
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
        RefreshResponse
            Successful operation

        Examples
        --------
        from fern import FernApi, RefreshFilter, RefreshTransferStatus

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.refresh_transfers(
            filter=[
                RefreshFilter(
                    status=RefreshTransferStatus.WAITING_COUNTERPARTY,
                    incoming=True,
                )
            ],
            skip_sync=False,
        )
        """
        _response = self._raw_client.refresh_transfers(
            filter=filter, skip_sync=skip_sync, asset_id=asset_id, request_options=request_options
        )
        return _response.data

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
    ) -> RgbInvoiceResponse:
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
        RgbInvoiceResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.get_an_rgb_invoice(
            min_confirmations=1,
            expiration_timestamp=1695811760,
            witness=False,
            transport_endpoints=["rpc://127.0.0.1:3000/json-rpc"],
        )
        """
        _response = self._raw_client.get_an_rgb_invoice(
            min_confirmations=min_confirmations,
            expiration_timestamp=expiration_timestamp,
            witness=witness,
            transport_endpoints=transport_endpoints,
            asset_id=asset_id,
            assignment=assignment,
            request_options=request_options,
        )
        return _response.data

    def send_rgb_assets(
        self,
        *,
        donation: bool,
        fee_rate: int,
        min_confirmations: int,
        expiration_timestamp: int,
        recipient_map: typing.Dict[str, typing.Sequence[Recipient]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendRgbResponse:
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
        SendRgbResponse
            Successful operation

        Examples
        --------
        from fern import Assignment_Fungible, FernApi, Recipient

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.send_rgb_assets(
            donation=False,
            fee_rate=5,
            min_confirmations=1,
            expiration_timestamp=1695811760,
            recipient_map={
                "rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8": [
                    Recipient(
                        recipient_id="utxob:2FjRqgQ-eEWCVHY5-zmpFtYzT-gGm3MdR-sTnxNcS-7RtUbY9-4NYuuh",
                        assignment=Assignment_Fungible(
                            value=42,
                        ),
                        transport_endpoints=["rpc://127.0.0.1:3000/json-rpc"],
                    ),
                    Recipient(
                        recipient_id="utxob:3GkRrhR-fFXDLIZ6-0anqGuzU-hHn4NeS-tUoyOdT-8SuVcZ0-5OZvvi",
                        assignment=Assignment_Fungible(
                            value=42,
                        ),
                        transport_endpoints=["rpc://127.0.0.1:3000/json-rpc"],
                    ),
                ],
                "rgb:d8qDVS5X-ICVG2uM-CPr3yO4-lfBhgjt-7FN1EPE-ApY1LcM": [
                    Recipient(
                        recipient_id="utxob:4HlSsiS-gGYEMKA7-1borHvaV-iIo5OfT-uVpzPeU-9TvWdA1-6PAwwj",
                        assignment=Assignment_Fungible(
                            value=42,
                        ),
                        transport_endpoints=["rpc://127.0.0.1:3000/json-rpc"],
                    )
                ],
            },
        )
        """
        _response = self._raw_client.send_rgb_assets(
            donation=donation,
            fee_rate=fee_rate,
            min_confirmations=min_confirmations,
            expiration_timestamp=expiration_timestamp,
            recipient_map=recipient_map,
            request_options=request_options,
        )
        return _response.data

    def sync_the_rgb_wallet(
        self, *, options: SyncOptions, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Sync the RGB wallet

        Parameters
        ----------
        options : SyncOptions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        from fern import FernApi, SyncKeychainZero, SyncOptions, SyncStrategy

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.rgb.sync_the_rgb_wallet(
            options=SyncOptions(
                keychain=SyncKeychainZero.COLORED,
                strategy=SyncStrategy.FAST_SYNC,
            ),
        )
        """
        _response = self._raw_client.sync_the_rgb_wallet(options=options, request_options=request_options)
        return _response.data


class AsyncRgbClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRgbClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRgbClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRgbClient
        """
        return self._raw_client

    async def get_the_balance_of_an_asset(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AssetBalanceResponse:
        """
        Get the balance for the provided RGB asset

        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetBalanceResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.get_the_balance_of_an_asset(
                asset_id="rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_balance_of_an_asset(
            asset_id=asset_id, request_options=request_options
        )
        return _response.data

    async def get_the_metadata_of_an_asset(
        self, *, asset_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AssetMetadataResponse:
        """
        Get the metadata for the provided RGB asset

        Parameters
        ----------
        asset_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssetMetadataResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.get_the_metadata_of_an_asset(
                asset_id="rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_the_metadata_of_an_asset(
            asset_id=asset_id, request_options=request_options
        )
        return _response.data

    async def create_utx_os(
        self,
        *,
        up_to: bool,
        fee_rate: int,
        skip_sync: bool,
        num: typing.Optional[int] = OMIT,
        size: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EmptyResponse:
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
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.create_utx_os(
                up_to=False,
                fee_rate=5,
                skip_sync=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_utx_os(
            up_to=up_to, fee_rate=fee_rate, skip_sync=skip_sync, num=num, size=size, request_options=request_options
        )
        return _response.data

    async def decode_an_rgb_invoice(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DecodeRgbInvoiceResponse:
        """
        Decode the provided RGB invoice string

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecodeRgbInvoiceResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.decode_an_rgb_invoice(
                invoice="rgb:icfqnK9y-wObZKTu-XJcDL98-sKbE5Mh-OuDJhiI-brRJrzE/RWhwUfTMpuP2Zfx1~j4nswCANGeJrYOqDcKelaMV4zU/~/bcrt:utxob:cbgHUJ4e-7QyKY4U-Jsj5AZw-oI0gxZh-7fxQY2_-tFFUAZN-4CgpX?expiry=1749906951&endpoints=rpcs://proxy.iriswallet.com/0.2/json-rpc",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.decode_an_rgb_invoice(invoice=invoice, request_options=request_options)
        return _response.data

    async def fail_rgb_transfers(
        self,
        *,
        no_asset_only: bool,
        skip_sync: bool,
        batch_transfer_idx: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FailTransfersResponse:
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
        FailTransfersResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.fail_rgb_transfers(
                no_asset_only=False,
                skip_sync=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fail_rgb_transfers(
            no_asset_only=no_asset_only,
            skip_sync=skip_sync,
            batch_transfer_idx=batch_transfer_idx,
            request_options=request_options,
        )
        return _response.data

    async def get_an_asset_media(
        self, *, digest: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAssetMediaResponse:
        """
        Get the hex string of the media bytes of the provided media digest

        Parameters
        ----------
        digest : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAssetMediaResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.get_an_asset_media(
                digest="5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_asset_media(digest=digest, request_options=request_options)
        return _response.data

    async def get_a_send_consignment(
        self, *, asset_id: str, txid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetConsignmentResponse:
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
        GetConsignmentResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.get_a_send_consignment(
                asset_id="rgb:2dkSTbr-jFhznbPmo-TQafzswCN-av4gTsJjX-ttx6CNou5-M98k8Zt",
                txid="33cf3e42fb1c6faa0d47e6a498a9d4e5c56e8a06ea0d295c6d90e2b6c85f7a1e",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_send_consignment(
            asset_id=asset_id, txid=txid, request_options=request_options
        )
        return _response.data

    async def inflate_rgb_assets(
        self,
        *,
        asset_id: str,
        inflation_amounts: typing.Sequence[int],
        fee_rate: int,
        min_confirmations: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InflateResponse:
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
        InflateResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.inflate_rgb_assets(
                asset_id="rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8",
                inflation_amounts=[100, 50],
                fee_rate=5,
                min_confirmations=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.inflate_rgb_assets(
            asset_id=asset_id,
            inflation_amounts=inflation_amounts,
            fee_rate=fee_rate,
            min_confirmations=min_confirmations,
            request_options=request_options,
        )
        return _response.data

    async def issue_an_rgb_cfa_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        name: str,
        precision: int,
        details: typing.Optional[str] = OMIT,
        file_digest: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueAssetCfaResponse:
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
        IssueAssetCfaResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.issue_an_rgb_cfa_asset(
                amounts=[1000, 600],
                name="Tether",
                precision=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_an_rgb_cfa_asset(
            amounts=amounts,
            name=name,
            precision=precision,
            details=details,
            file_digest=file_digest,
            request_options=request_options,
        )
        return _response.data

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
    ) -> IssueAssetIfaResponse:
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
        IssueAssetIfaResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.issue_an_rgb_ifa_asset(
                amounts=[1000, 600],
                inflation_amounts=[100, 50],
                ticker="USDT",
                name="Tether",
                precision=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_an_rgb_ifa_asset(
            amounts=amounts,
            inflation_amounts=inflation_amounts,
            ticker=ticker,
            name=name,
            precision=precision,
            reject_list_url=reject_list_url,
            request_options=request_options,
        )
        return _response.data

    async def issue_an_rgb_nia_asset(
        self,
        *,
        amounts: typing.Sequence[int],
        ticker: str,
        name: str,
        precision: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> IssueAssetNiaResponse:
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
        IssueAssetNiaResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.issue_an_rgb_nia_asset(
                amounts=[1000, 600],
                ticker="USDT",
                name="Tether",
                precision=0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_an_rgb_nia_asset(
            amounts=amounts, ticker=ticker, name=name, precision=precision, request_options=request_options
        )
        return _response.data

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
    ) -> IssueAssetUdaResponse:
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
        IssueAssetUdaResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.issue_an_rgb_uda_asset(
                ticker="UNI",
                name="Unique",
                precision=0,
                attachments_file_digests=[
                    "5891b5b522d5df086d0ff0b110fbd9d21bb4fc7163af34d08286a2e846f6be03",
                    "d7516e3a27cdf35aa9dcb323b5f556344ef7f57570be30b88de2bfd4ba339b1a",
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.issue_an_rgb_uda_asset(
            ticker=ticker,
            name=name,
            precision=precision,
            attachments_file_digests=attachments_file_digests,
            details=details,
            media_file_digest=media_file_digest,
            request_options=request_options,
        )
        return _response.data

    async def list_assets(
        self,
        *,
        filter_asset_schemas: typing.Sequence[AssetSchema],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAssetsResponse:
        """
        List the node's RGB assets

        Parameters
        ----------
        filter_asset_schemas : typing.Sequence[AssetSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAssetsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AssetSchema, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.list_assets(
                filter_asset_schemas=[
                    AssetSchema.NIA,
                    AssetSchema.UDA,
                    AssetSchema.CFA,
                    AssetSchema.IFA,
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_assets(
            filter_asset_schemas=filter_asset_schemas, request_options=request_options
        )
        return _response.data

    async def list_transfers(
        self,
        *,
        asset_filter: AssetFilter,
        txid: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTransfersResponse:
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
        ListTransfersResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AssetFilter_AnyOrNone, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.list_transfers(
                asset_filter=AssetFilter_AnyOrNone(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_transfers(
            asset_filter=asset_filter, txid=txid, request_options=request_options
        )
        return _response.data

    async def post_an_asset_media(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetMediaResponse:
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
        PostAssetMediaResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.post_an_asset_media()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_an_asset_media(file=file, request_options=request_options)
        return _response.data

    async def provide_an_out_of_band_ack(
        self, *, recipient_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProvideOutOfBandAckResponse:
        """
        Record the out-of-band ACK received from a recipient of an outgoing transfer

        Parameters
        ----------
        recipient_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProvideOutOfBandAckResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.provide_an_out_of_band_ack(
                recipient_id="utxob:2Bwv2Vx-t7VD8XjTh-9EMbpBFKh-J5HDFY4pj-eywu4tKKk-hjTvzJa",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.provide_an_out_of_band_ack(
            recipient_id=recipient_id, request_options=request_options
        )
        return _response.data

    async def provide_an_out_of_band_consignment(
        self,
        *,
        file: core.File,
        media: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProvideOutOfBandConsignmentResponse:
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
        ProvideOutOfBandConsignmentResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.provide_an_out_of_band_consignment()


        asyncio.run(main())
        """
        _response = await self._raw_client.provide_an_out_of_band_consignment(
            file=file, media=media, request_options=request_options
        )
        return _response.data

    async def refresh_transfers(
        self,
        *,
        filter: typing.Sequence[RefreshFilter],
        skip_sync: bool,
        asset_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefreshResponse:
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
        RefreshResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RefreshFilter, RefreshTransferStatus

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.refresh_transfers(
                filter=[
                    RefreshFilter(
                        status=RefreshTransferStatus.WAITING_COUNTERPARTY,
                        incoming=True,
                    )
                ],
                skip_sync=False,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.refresh_transfers(
            filter=filter, skip_sync=skip_sync, asset_id=asset_id, request_options=request_options
        )
        return _response.data

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
    ) -> RgbInvoiceResponse:
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
        RgbInvoiceResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.get_an_rgb_invoice(
                min_confirmations=1,
                expiration_timestamp=1695811760,
                witness=False,
                transport_endpoints=["rpc://127.0.0.1:3000/json-rpc"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_rgb_invoice(
            min_confirmations=min_confirmations,
            expiration_timestamp=expiration_timestamp,
            witness=witness,
            transport_endpoints=transport_endpoints,
            asset_id=asset_id,
            assignment=assignment,
            request_options=request_options,
        )
        return _response.data

    async def send_rgb_assets(
        self,
        *,
        donation: bool,
        fee_rate: int,
        min_confirmations: int,
        expiration_timestamp: int,
        recipient_map: typing.Dict[str, typing.Sequence[Recipient]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendRgbResponse:
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
        SendRgbResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import Assignment_Fungible, AsyncFernApi, Recipient

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.send_rgb_assets(
                donation=False,
                fee_rate=5,
                min_confirmations=1,
                expiration_timestamp=1695811760,
                recipient_map={
                    "rgb:CJkb4YZw-jRiz2sk-~PARPio-wtVYI1c-XAEYCqO-wTfvRZ8": [
                        Recipient(
                            recipient_id="utxob:2FjRqgQ-eEWCVHY5-zmpFtYzT-gGm3MdR-sTnxNcS-7RtUbY9-4NYuuh",
                            assignment=Assignment_Fungible(
                                value=42,
                            ),
                            transport_endpoints=["rpc://127.0.0.1:3000/json-rpc"],
                        ),
                        Recipient(
                            recipient_id="utxob:3GkRrhR-fFXDLIZ6-0anqGuzU-hHn4NeS-tUoyOdT-8SuVcZ0-5OZvvi",
                            assignment=Assignment_Fungible(
                                value=42,
                            ),
                            transport_endpoints=["rpc://127.0.0.1:3000/json-rpc"],
                        ),
                    ],
                    "rgb:d8qDVS5X-ICVG2uM-CPr3yO4-lfBhgjt-7FN1EPE-ApY1LcM": [
                        Recipient(
                            recipient_id="utxob:4HlSsiS-gGYEMKA7-1borHvaV-iIo5OfT-uVpzPeU-9TvWdA1-6PAwwj",
                            assignment=Assignment_Fungible(
                                value=42,
                            ),
                            transport_endpoints=["rpc://127.0.0.1:3000/json-rpc"],
                        )
                    ],
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_rgb_assets(
            donation=donation,
            fee_rate=fee_rate,
            min_confirmations=min_confirmations,
            expiration_timestamp=expiration_timestamp,
            recipient_map=recipient_map,
            request_options=request_options,
        )
        return _response.data

    async def sync_the_rgb_wallet(
        self, *, options: SyncOptions, request_options: typing.Optional[RequestOptions] = None
    ) -> EmptyResponse:
        """
        Sync the RGB wallet

        Parameters
        ----------
        options : SyncOptions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EmptyResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SyncKeychainZero, SyncOptions, SyncStrategy

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.rgb.sync_the_rgb_wallet(
                options=SyncOptions(
                    keychain=SyncKeychainZero.COLORED,
                    strategy=SyncStrategy.FAST_SYNC,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sync_the_rgb_wallet(options=options, request_options=request_options)
        return _response.data
