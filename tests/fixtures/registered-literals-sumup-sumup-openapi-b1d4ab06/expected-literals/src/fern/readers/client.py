

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.affiliate import Affiliate
from ..types.amount import Amount
from ..types.create_reader_checkout_response import CreateReaderCheckoutResponse
from ..types.get_reader_checkout_response import GetReaderCheckoutResponse
from ..types.metadata import Metadata
from ..types.reader import Reader
from ..types.reader_id import ReaderId
from ..types.reader_name import ReaderName
from ..types.reader_pairing_code import ReaderPairingCode
from ..types.reader_payment_response import ReaderPaymentResponse
from ..types.status_response import StatusResponse
from .raw_client import AsyncRawReadersClient, RawReadersClient
from .types.create_reader_checkout_request_aade import CreateReaderCheckoutRequestAade
from .types.create_reader_checkout_request_affiliate import CreateReaderCheckoutRequestAffiliate
from .types.create_reader_checkout_request_card_type import CreateReaderCheckoutRequestCardType
from .types.create_reader_checkout_request_total_amount import CreateReaderCheckoutRequestTotalAmount
from .types.list_readers_response import ListReadersResponse


OMIT = typing.cast(typing.Any, ...)


class ReadersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReadersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReadersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReadersClient
        """
        return self._raw_client

    def create_go_reader_checkout(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        client_transaction_id: str,
        total_amount: Amount,
        affiliate: typing.Optional[Affiliate] = OMIT,
        tip_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReaderPaymentResponse:
        """
        Initiates a payment on the SumUp Go terminal identified by the reader ID.

        Use `client_transaction_id` as an idempotency key: retrying the request with the same value returns the result of the original payment instead of creating a duplicate.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        client_transaction_id : str
            Caller-supplied correlation identifier, used as the idempotency key.

        total_amount : Amount

        affiliate : typing.Optional[Affiliate]

        tip_amount : typing.Optional[int]
            Optional tip amount in minor units, added on top of total_amount.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReaderPaymentResponse
            Returns the result of the payment initiated on the reader.

        Examples
        --------
        from fern import Amount, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.create_go_reader_checkout(
            merchant_code="MK10CL2A",
            reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
            client_transaction_id="19e12390-72cf-4f9f-80b5-b0c8a67fa43f",
            total_amount=Amount(
                currency="MXN",
                value=1000,
            ),
        )
        """
        _response = self._raw_client.create_go_reader_checkout(
            merchant_code,
            reader_id,
            client_transaction_id=client_transaction_id,
            total_amount=total_amount,
            affiliate=affiliate,
            tip_amount=tip_amount,
            request_options=request_options,
        )
        return _response.data

    def list_readers(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListReadersResponse:
        """
        List all readers of the merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListReadersResponse
            Returns a list Reader objects.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.list_readers(
            merchant_code="MK10CL2A",
        )
        """
        _response = self._raw_client.list_readers(merchant_code, request_options=request_options)
        return _response.data

    def create_reader(
        self,
        merchant_code: str,
        *,
        pairing_code: ReaderPairingCode,
        name: ReaderName,
        metadata: typing.Optional[Metadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reader:
        """
        Create a new Reader for the merchant account.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        pairing_code : ReaderPairingCode

        name : ReaderName

        metadata : typing.Optional[Metadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reader
            Returns the Reader object if the creation succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.create_reader(
            merchant_code="MK10CL2A",
            pairing_code="4WLFDSBF",
            name="Frontdesk",
        )
        """
        _response = self._raw_client.create_reader(
            merchant_code, pairing_code=pairing_code, name=name, metadata=metadata, request_options=request_options
        )
        return _response.data

    def get_reader(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reader:
        """
        Retrieve a Reader.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        if_modified_since : typing.Optional[str]
            Return the reader only if it has been modified after the specified timestamp given in the headers.

            Timestamps are accepted in the following formats:

             - HTTP Standard: [IMF format (RFC 5322)](https://www.rfc-editor.org/rfc/rfc5322#section-3.3), sometimes also referred to as [RFC 7231](https://www.rfc-editor.org/rfc/rfc7231#section-7.1.1.1).
             - RFC 3339: Used for timestamps in JSON payloads on this API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reader
            Returns a Reader object for a valid identifier.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.get_reader(
            merchant_code="MK10CL2A",
            reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
        )
        """
        _response = self._raw_client.get_reader(
            merchant_code, reader_id, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    def delete_reader(
        self, merchant_code: str, reader_id: ReaderId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a reader.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.delete_reader(
            merchant_code="MK10CL2A",
            reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
        )
        """
        _response = self._raw_client.delete_reader(merchant_code, reader_id, request_options=request_options)
        return _response.data

    def update_reader(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        name: typing.Optional[ReaderName] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reader:
        """
        Updates a reader's name or metadata and returns the updated reader.

        Providing `metadata` replaces the entire metadata object; include all entries that should be retained. Omitted fields remain unchanged.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        name : typing.Optional[ReaderName]

        metadata : typing.Optional[Metadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reader
            Returns the updated Reader object if the update succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.update_reader(
            merchant_code="MK10CL2A",
            reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
        )
        """
        _response = self._raw_client.update_reader(
            merchant_code, reader_id, name=name, metadata=metadata, request_options=request_options
        )
        return _response.data

    def create_reader_checkout(
        self,
        merchant_code: str,
        reader_id: str,
        *,
        total_amount: CreateReaderCheckoutRequestTotalAmount,
        aade: typing.Optional[CreateReaderCheckoutRequestAade] = OMIT,
        affiliate: typing.Optional[CreateReaderCheckoutRequestAffiliate] = OMIT,
        card_type: typing.Optional[CreateReaderCheckoutRequestCardType] = OMIT,
        description: typing.Optional[str] = OMIT,
        installments: typing.Optional[int] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        tip_rates: typing.Optional[typing.Sequence[float]] = OMIT,
        tip_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateReaderCheckoutResponse:
        """
        Creates a Checkout for a Reader.

        This process is asynchronous and the actual transaction may take some time to be started on the device.


        There are some caveats when using this endpoint:
        * The target device must be online, otherwise checkout won't be accepted
        * After the checkout is accepted, the system has 60 seconds to start the payment on the target device. During this time, any other checkout for the same device will be rejected.


        **Note**: If the target device is a Solo, it must be in version 3.3.24.3 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        total_amount : CreateReaderCheckoutRequestTotalAmount
            Amount structure.

            The amount is represented as an integer value altogether with the currency and the minor unit.

            For example, EUR 1.00 is represented as value 100 with minor unit of 2.

        aade : typing.Optional[CreateReaderCheckoutRequestAade]
            Optional object containing data for transactions from ERP integrators in Greece that comply with the AADE 1155 protocol.
            When such regulatory/business requirements apply, this object must be provided and contains the data needed to validate the transaction with the AADE signature provider.

        affiliate : typing.Optional[CreateReaderCheckoutRequestAffiliate]
            Affiliate metadata for the transaction.
            It is a field that allow for integrators to track the source of the transaction.

        card_type : typing.Optional[CreateReaderCheckoutRequestCardType]
            The card type of the card used for the transaction.
            Is is required only for some countries (e.g: Brazil).

        description : typing.Optional[str]
            Description of the checkout to be shown in the Merchant Sales

        installments : typing.Optional[int]
            Number of installments for the transaction.
            It may vary according to the merchant country.
            For example, in Brazil, the maximum number of installments is 12.

            Omit if the merchant country does support installments.
            Otherwise, the checkout will be rejected.

        return_url : typing.Optional[str]
            Webhook URL to which the payment result will be sent.
            It must be a HTTPS url.

        tip_rates : typing.Optional[typing.Sequence[float]]
            List of tipping rates to be displayed to the cardholder.
            The rates are in percentage and should be between 0.01 and 0.99.
            The list should be sorted in ascending order.

        tip_timeout : typing.Optional[int]
            Time in seconds the cardholder has to select a tip rate.
            If not provided, the default value is 30 seconds.

            It can only be set if `tip_rates` is provided.

            **Note**: If the target device is a Solo, it must be in version 3.3.38.0 or higher.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateReaderCheckoutResponse
            The Checkout got successfully created for the given reader.

        Examples
        --------
        from fern.readers import (
            CreateReaderCheckoutRequestAade,
            CreateReaderCheckoutRequestAffiliate,
            CreateReaderCheckoutRequestTotalAmount,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.create_reader_checkout(
            merchant_code="MC0X0ABC",
            reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
            aade=CreateReaderCheckoutRequestAade(
                provider_id="123",
                signature="QjcxRDdBNTU1MDcyRTNFRTREMkZEM0Y0NTdBMjkxMTU4MzBFNkNCQTs7MjAyNTExMTIyMTQ3MTM7Nzk2OzEwNDs5MDA7OTAwOzU0ODg5MDM5",
                signature_data="B71D7A555072E3EE4D2FD3F457A29115830E6CBA;;20251112214713;796;104;900;900;54889039",
            ),
            affiliate=CreateReaderCheckoutRequestAffiliate(
                app_id="com.example.app",
                foreign_transaction_id="123456",
                key="ef7b684a-d6f4-4e93-9b1b-6acdd6564a8e",
                tags={"key": "value"},
            ),
            card_type="debit",
            description="This is a description...",
            installments=1,
            return_url="https://webhook.site/e21ddbb0-42c4-4358-a981-f5a95cd86fb5",
            tip_rates=[0.05, 0.1, 0.15],
            tip_timeout=60,
            total_amount=CreateReaderCheckoutRequestTotalAmount(
                currency="EUR",
                minor_unit=2,
                value=5033,
            ),
        )
        """
        _response = self._raw_client.create_reader_checkout(
            merchant_code,
            reader_id,
            total_amount=total_amount,
            aade=aade,
            affiliate=affiliate,
            card_type=card_type,
            description=description,
            installments=installments,
            return_url=return_url,
            tip_rates=tip_rates,
            tip_timeout=tip_timeout,
            request_options=request_options,
        )
        return _response.data

    def get_reader_status(
        self, merchant_code: str, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatusResponse:
        """
        Provides the last known status for a Reader.

        This endpoint allows you to retrieve updates from the connected card reader, including the current screen being displayed during the payment process and the device status (battery level, connectivity, and update state).

        Supported States

        * `IDLE` – Reader ready for next transaction
        * `SELECTING_TIP` – Waiting for tip input
        * `WAITING_FOR_CARD` – Awaiting card insert/tap
        * `WAITING_FOR_PIN` – Waiting for PIN entry
        * `WAITING_FOR_SIGNATURE` – Waiting for customer signature
        * `UPDATING_FIRMWARE` – Firmware update in progress

        Device Status

        * `ONLINE` – Device connected and operational
        * `OFFLINE` – Device disconnected (last state persisted)

        **Note**: If the target device is a Solo, it must be in version 3.3.39.0 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Response with the device status.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.get_reader_status(
            merchant_code="MC0X0ABC",
            reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
        )
        """
        _response = self._raw_client.get_reader_status(merchant_code, reader_id, request_options=request_options)
        return _response.data

    def create_reader_terminate(
        self, merchant_code: str, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Terminate a Reader Checkout stops the current transaction on the target device.

        This process is asynchronous and the actual termination may take some time to be performed on the device.


        There are some caveats when using this endpoint:
        * The target device must be online, otherwise terminate won't be accepted
        * The action will succeed only if the device is waiting for cardholder action: e.g: waiting for card, waiting for PIN, etc.
        * There is no confirmation of the termination.

        If a transaction is successfully terminated and `return_url` was provided on Checkout, the transaction status will be sent as `failed` to the provided URL.


        **Note**: If the target device is a Solo, it must be in version 3.3.28.0 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The Terminate action was successfully dispatched for the given reader.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.create_reader_terminate(
            merchant_code="MC0X0ABC",
            reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
        )
        """
        _response = self._raw_client.create_reader_terminate(merchant_code, reader_id, request_options=request_options)
        return _response.data

    def get_reader_checkout(
        self,
        merchant_code: str,
        reader_id: str,
        checkout_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetReaderCheckoutResponse:
        """
        Get a Checkout for a Reader.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        checkout_id : str
            The unique identifier of the Checkout

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetReaderCheckoutResponse
            The Checkout got successfully retrieved for the given reader.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.readers.get_reader_checkout(
            merchant_code="MC0X0ABC",
            reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
            checkout_id="74ecff66-1655-43ed-8ce3-193f49fa602f",
        )
        """
        _response = self._raw_client.get_reader_checkout(
            merchant_code, reader_id, checkout_id, request_options=request_options
        )
        return _response.data


class AsyncReadersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReadersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReadersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReadersClient
        """
        return self._raw_client

    async def create_go_reader_checkout(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        client_transaction_id: str,
        total_amount: Amount,
        affiliate: typing.Optional[Affiliate] = OMIT,
        tip_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReaderPaymentResponse:
        """
        Initiates a payment on the SumUp Go terminal identified by the reader ID.

        Use `client_transaction_id` as an idempotency key: retrying the request with the same value returns the result of the original payment instead of creating a duplicate.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        client_transaction_id : str
            Caller-supplied correlation identifier, used as the idempotency key.

        total_amount : Amount

        affiliate : typing.Optional[Affiliate]

        tip_amount : typing.Optional[int]
            Optional tip amount in minor units, added on top of total_amount.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReaderPaymentResponse
            Returns the result of the payment initiated on the reader.

        Examples
        --------
        import asyncio

        from fern import Amount, AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.create_go_reader_checkout(
                merchant_code="MK10CL2A",
                reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
                client_transaction_id="19e12390-72cf-4f9f-80b5-b0c8a67fa43f",
                total_amount=Amount(
                    currency="MXN",
                    value=1000,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_go_reader_checkout(
            merchant_code,
            reader_id,
            client_transaction_id=client_transaction_id,
            total_amount=total_amount,
            affiliate=affiliate,
            tip_amount=tip_amount,
            request_options=request_options,
        )
        return _response.data

    async def list_readers(
        self, merchant_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListReadersResponse:
        """
        List all readers of the merchant.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListReadersResponse
            Returns a list Reader objects.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.list_readers(
                merchant_code="MK10CL2A",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_readers(merchant_code, request_options=request_options)
        return _response.data

    async def create_reader(
        self,
        merchant_code: str,
        *,
        pairing_code: ReaderPairingCode,
        name: ReaderName,
        metadata: typing.Optional[Metadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reader:
        """
        Create a new Reader for the merchant account.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        pairing_code : ReaderPairingCode

        name : ReaderName

        metadata : typing.Optional[Metadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reader
            Returns the Reader object if the creation succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.create_reader(
                merchant_code="MK10CL2A",
                pairing_code="4WLFDSBF",
                name="Frontdesk",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_reader(
            merchant_code, pairing_code=pairing_code, name=name, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def get_reader(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        if_modified_since: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reader:
        """
        Retrieve a Reader.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        if_modified_since : typing.Optional[str]
            Return the reader only if it has been modified after the specified timestamp given in the headers.

            Timestamps are accepted in the following formats:

             - HTTP Standard: [IMF format (RFC 5322)](https://www.rfc-editor.org/rfc/rfc5322#section-3.3), sometimes also referred to as [RFC 7231](https://www.rfc-editor.org/rfc/rfc7231#section-7.1.1.1).
             - RFC 3339: Used for timestamps in JSON payloads on this API.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reader
            Returns a Reader object for a valid identifier.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.get_reader(
                merchant_code="MK10CL2A",
                reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reader(
            merchant_code, reader_id, if_modified_since=if_modified_since, request_options=request_options
        )
        return _response.data

    async def delete_reader(
        self, merchant_code: str, reader_id: ReaderId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a reader.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.delete_reader(
                merchant_code="MK10CL2A",
                reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_reader(merchant_code, reader_id, request_options=request_options)
        return _response.data

    async def update_reader(
        self,
        merchant_code: str,
        reader_id: ReaderId,
        *,
        name: typing.Optional[ReaderName] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Reader:
        """
        Updates a reader's name or metadata and returns the updated reader.

        Providing `metadata` replaces the entire metadata object; include all entries that should be retained. Omitted fields remain unchanged.

        Parameters
        ----------
        merchant_code : str
            Short unique identifier for the merchant.

        reader_id : ReaderId
            The unique identifier of the reader.

        name : typing.Optional[ReaderName]

        metadata : typing.Optional[Metadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Reader
            Returns the updated Reader object if the update succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.update_reader(
                merchant_code="MK10CL2A",
                reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_reader(
            merchant_code, reader_id, name=name, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def create_reader_checkout(
        self,
        merchant_code: str,
        reader_id: str,
        *,
        total_amount: CreateReaderCheckoutRequestTotalAmount,
        aade: typing.Optional[CreateReaderCheckoutRequestAade] = OMIT,
        affiliate: typing.Optional[CreateReaderCheckoutRequestAffiliate] = OMIT,
        card_type: typing.Optional[CreateReaderCheckoutRequestCardType] = OMIT,
        description: typing.Optional[str] = OMIT,
        installments: typing.Optional[int] = OMIT,
        return_url: typing.Optional[str] = OMIT,
        tip_rates: typing.Optional[typing.Sequence[float]] = OMIT,
        tip_timeout: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateReaderCheckoutResponse:
        """
        Creates a Checkout for a Reader.

        This process is asynchronous and the actual transaction may take some time to be started on the device.


        There are some caveats when using this endpoint:
        * The target device must be online, otherwise checkout won't be accepted
        * After the checkout is accepted, the system has 60 seconds to start the payment on the target device. During this time, any other checkout for the same device will be rejected.


        **Note**: If the target device is a Solo, it must be in version 3.3.24.3 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        total_amount : CreateReaderCheckoutRequestTotalAmount
            Amount structure.

            The amount is represented as an integer value altogether with the currency and the minor unit.

            For example, EUR 1.00 is represented as value 100 with minor unit of 2.

        aade : typing.Optional[CreateReaderCheckoutRequestAade]
            Optional object containing data for transactions from ERP integrators in Greece that comply with the AADE 1155 protocol.
            When such regulatory/business requirements apply, this object must be provided and contains the data needed to validate the transaction with the AADE signature provider.

        affiliate : typing.Optional[CreateReaderCheckoutRequestAffiliate]
            Affiliate metadata for the transaction.
            It is a field that allow for integrators to track the source of the transaction.

        card_type : typing.Optional[CreateReaderCheckoutRequestCardType]
            The card type of the card used for the transaction.
            Is is required only for some countries (e.g: Brazil).

        description : typing.Optional[str]
            Description of the checkout to be shown in the Merchant Sales

        installments : typing.Optional[int]
            Number of installments for the transaction.
            It may vary according to the merchant country.
            For example, in Brazil, the maximum number of installments is 12.

            Omit if the merchant country does support installments.
            Otherwise, the checkout will be rejected.

        return_url : typing.Optional[str]
            Webhook URL to which the payment result will be sent.
            It must be a HTTPS url.

        tip_rates : typing.Optional[typing.Sequence[float]]
            List of tipping rates to be displayed to the cardholder.
            The rates are in percentage and should be between 0.01 and 0.99.
            The list should be sorted in ascending order.

        tip_timeout : typing.Optional[int]
            Time in seconds the cardholder has to select a tip rate.
            If not provided, the default value is 30 seconds.

            It can only be set if `tip_rates` is provided.

            **Note**: If the target device is a Solo, it must be in version 3.3.38.0 or higher.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateReaderCheckoutResponse
            The Checkout got successfully created for the given reader.

        Examples
        --------
        import asyncio

        from fern.readers import (
            CreateReaderCheckoutRequestAade,
            CreateReaderCheckoutRequestAffiliate,
            CreateReaderCheckoutRequestTotalAmount,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.create_reader_checkout(
                merchant_code="MC0X0ABC",
                reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
                aade=CreateReaderCheckoutRequestAade(
                    provider_id="123",
                    signature="QjcxRDdBNTU1MDcyRTNFRTREMkZEM0Y0NTdBMjkxMTU4MzBFNkNCQTs7MjAyNTExMTIyMTQ3MTM7Nzk2OzEwNDs5MDA7OTAwOzU0ODg5MDM5",
                    signature_data="B71D7A555072E3EE4D2FD3F457A29115830E6CBA;;20251112214713;796;104;900;900;54889039",
                ),
                affiliate=CreateReaderCheckoutRequestAffiliate(
                    app_id="com.example.app",
                    foreign_transaction_id="123456",
                    key="ef7b684a-d6f4-4e93-9b1b-6acdd6564a8e",
                    tags={"key": "value"},
                ),
                card_type="debit",
                description="This is a description...",
                installments=1,
                return_url="https://webhook.site/e21ddbb0-42c4-4358-a981-f5a95cd86fb5",
                tip_rates=[0.05, 0.1, 0.15],
                tip_timeout=60,
                total_amount=CreateReaderCheckoutRequestTotalAmount(
                    currency="EUR",
                    minor_unit=2,
                    value=5033,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_reader_checkout(
            merchant_code,
            reader_id,
            total_amount=total_amount,
            aade=aade,
            affiliate=affiliate,
            card_type=card_type,
            description=description,
            installments=installments,
            return_url=return_url,
            tip_rates=tip_rates,
            tip_timeout=tip_timeout,
            request_options=request_options,
        )
        return _response.data

    async def get_reader_status(
        self, merchant_code: str, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StatusResponse:
        """
        Provides the last known status for a Reader.

        This endpoint allows you to retrieve updates from the connected card reader, including the current screen being displayed during the payment process and the device status (battery level, connectivity, and update state).

        Supported States

        * `IDLE` – Reader ready for next transaction
        * `SELECTING_TIP` – Waiting for tip input
        * `WAITING_FOR_CARD` – Awaiting card insert/tap
        * `WAITING_FOR_PIN` – Waiting for PIN entry
        * `WAITING_FOR_SIGNATURE` – Waiting for customer signature
        * `UPDATING_FIRMWARE` – Firmware update in progress

        Device Status

        * `ONLINE` – Device connected and operational
        * `OFFLINE` – Device disconnected (last state persisted)

        **Note**: If the target device is a Solo, it must be in version 3.3.39.0 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StatusResponse
            Response with the device status.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.get_reader_status(
                merchant_code="MC0X0ABC",
                reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reader_status(merchant_code, reader_id, request_options=request_options)
        return _response.data

    async def create_reader_terminate(
        self, merchant_code: str, reader_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Terminate a Reader Checkout stops the current transaction on the target device.

        This process is asynchronous and the actual termination may take some time to be performed on the device.


        There are some caveats when using this endpoint:
        * The target device must be online, otherwise terminate won't be accepted
        * The action will succeed only if the device is waiting for cardholder action: e.g: waiting for card, waiting for PIN, etc.
        * There is no confirmation of the termination.

        If a transaction is successfully terminated and `return_url` was provided on Checkout, the transaction status will be sent as `failed` to the provided URL.


        **Note**: If the target device is a Solo, it must be in version 3.3.28.0 or higher.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            The Terminate action was successfully dispatched for the given reader.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.create_reader_terminate(
                merchant_code="MC0X0ABC",
                reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_reader_terminate(
            merchant_code, reader_id, request_options=request_options
        )
        return _response.data

    async def get_reader_checkout(
        self,
        merchant_code: str,
        reader_id: str,
        checkout_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetReaderCheckoutResponse:
        """
        Get a Checkout for a Reader.

        Parameters
        ----------
        merchant_code : str
            Merchant Code

        reader_id : str
            The unique identifier of the Reader

        checkout_id : str
            The unique identifier of the Checkout

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetReaderCheckoutResponse
            The Checkout got successfully retrieved for the given reader.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.readers.get_reader_checkout(
                merchant_code="MC0X0ABC",
                reader_id="rdr_3MSAFM23CK82VSTT4BN6RWSQ65",
                checkout_id="74ecff66-1655-43ed-8ce3-193f49fa602f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_reader_checkout(
            merchant_code, reader_id, checkout_id, request_options=request_options
        )
        return _response.data
