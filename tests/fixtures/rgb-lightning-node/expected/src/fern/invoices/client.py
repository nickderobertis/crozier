

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.decode_ln_invoice_response import DecodeLnInvoiceResponse
from ..types.invoice_status_response import InvoiceStatusResponse
from ..types.ln_invoice_response import LnInvoiceResponse
from .raw_client import AsyncRawInvoicesClient, RawInvoicesClient


OMIT = typing.cast(typing.Any, ...)


class InvoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInvoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInvoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInvoicesClient
        """
        return self._raw_client

    def decode_a_ln_invoice(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DecodeLnInvoiceResponse:
        """
        Decode the provided LN invoice string

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecodeLnInvoiceResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.invoices.decode_a_ln_invoice(
            invoice="lnbcrt30u1pjv6yzndqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qdpc280eur52luxppv6f3nnj8l6vnd9g2hnv3qv6mjhmhvlzf6327pp5tjjasx6g9dqptea3fhm6yllq5wxzycnnvp8l6wcq3d6j2uvpryuqsp5l8az8x3g8fe05dg7cmgddld3da09nfjvky8xftwsk4cj8p2l7kfq9qyysgqcqpcxqzdylzlwfnkyw3jv344x4rzwgkk53ng0fhxy5rdduk4g5tpvea8xa6rfckkza35va28xjn2tqkhgarcxep5umm4x5k56wfcdvu95eq7qzp20vrl4xz76syapsa3c09j7lg5gerkaj63llj0ark7ph8hfketn6fkqzm8laf66dhsncm23wkwm5l5377we9e8lnlknnkwje5eefkccusqm6rqt8",
        )
        """
        _response = self._raw_client.decode_a_ln_invoice(invoice=invoice, request_options=request_options)
        return _response.data

    def get_an_invoice_status(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InvoiceStatusResponse:
        """
        Get the status of the provided LN invoice

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvoiceStatusResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.invoices.get_an_invoice_status(
            invoice="lnbcrt30u1pjv6yzndqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qdpc280eur52luxppv6f3nnj8l6vnd9g2hnv3qv6mjhmhvlzf6327pp5tjjasx6g9dqptea3fhm6yllq5wxzycnnvp8l6wcq3d6j2uvpryuqsp5l8az8x3g8fe05dg7cmgddld3da09nfjvky8xftwsk4cj8p2l7kfq9qyysgqcqpcxqzdylzlwfnkyw3jv344x4rzwgkk53ng0fhxy5rdduk4g5tpvea8xa6rfckkza35va28xjn2tqkhgarcxep5umm4x5k56wfcdvu95eq7qzp20vrl4xz76syapsa3c09j7lg5gerkaj63llj0ark7ph8hfketn6fkqzm8laf66dhsncm23wkwm5l5377we9e8lnlknnkwje5eefkccusqm6rqt8",
        )
        """
        _response = self._raw_client.get_an_invoice_status(invoice=invoice, request_options=request_options)
        return _response.data

    def get_a_ln_invoice(
        self,
        *,
        expiry_sec: int,
        amt_msat: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_hash: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LnInvoiceResponse:
        """
        Get a LN invoice to receive a payment. The description and description_hash fields are mutually exclusive.

        Parameters
        ----------
        expiry_sec : int

        amt_msat : typing.Optional[int]

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        description : typing.Optional[str]

        description_hash : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LnInvoiceResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.invoices.get_a_ln_invoice(
            expiry_sec=420,
        )
        """
        _response = self._raw_client.get_a_ln_invoice(
            expiry_sec=expiry_sec,
            amt_msat=amt_msat,
            asset_id=asset_id,
            asset_amount=asset_amount,
            description=description,
            description_hash=description_hash,
            request_options=request_options,
        )
        return _response.data


class AsyncInvoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInvoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInvoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInvoicesClient
        """
        return self._raw_client

    async def decode_a_ln_invoice(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> DecodeLnInvoiceResponse:
        """
        Decode the provided LN invoice string

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DecodeLnInvoiceResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.decode_a_ln_invoice(
                invoice="lnbcrt30u1pjv6yzndqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qdpc280eur52luxppv6f3nnj8l6vnd9g2hnv3qv6mjhmhvlzf6327pp5tjjasx6g9dqptea3fhm6yllq5wxzycnnvp8l6wcq3d6j2uvpryuqsp5l8az8x3g8fe05dg7cmgddld3da09nfjvky8xftwsk4cj8p2l7kfq9qyysgqcqpcxqzdylzlwfnkyw3jv344x4rzwgkk53ng0fhxy5rdduk4g5tpvea8xa6rfckkza35va28xjn2tqkhgarcxep5umm4x5k56wfcdvu95eq7qzp20vrl4xz76syapsa3c09j7lg5gerkaj63llj0ark7ph8hfketn6fkqzm8laf66dhsncm23wkwm5l5377we9e8lnlknnkwje5eefkccusqm6rqt8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.decode_a_ln_invoice(invoice=invoice, request_options=request_options)
        return _response.data

    async def get_an_invoice_status(
        self, *, invoice: str, request_options: typing.Optional[RequestOptions] = None
    ) -> InvoiceStatusResponse:
        """
        Get the status of the provided LN invoice

        Parameters
        ----------
        invoice : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InvoiceStatusResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.get_an_invoice_status(
                invoice="lnbcrt30u1pjv6yzndqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qdpc280eur52luxppv6f3nnj8l6vnd9g2hnv3qv6mjhmhvlzf6327pp5tjjasx6g9dqptea3fhm6yllq5wxzycnnvp8l6wcq3d6j2uvpryuqsp5l8az8x3g8fe05dg7cmgddld3da09nfjvky8xftwsk4cj8p2l7kfq9qyysgqcqpcxqzdylzlwfnkyw3jv344x4rzwgkk53ng0fhxy5rdduk4g5tpvea8xa6rfckkza35va28xjn2tqkhgarcxep5umm4x5k56wfcdvu95eq7qzp20vrl4xz76syapsa3c09j7lg5gerkaj63llj0ark7ph8hfketn6fkqzm8laf66dhsncm23wkwm5l5377we9e8lnlknnkwje5eefkccusqm6rqt8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_invoice_status(invoice=invoice, request_options=request_options)
        return _response.data

    async def get_a_ln_invoice(
        self,
        *,
        expiry_sec: int,
        amt_msat: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_hash: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LnInvoiceResponse:
        """
        Get a LN invoice to receive a payment. The description and description_hash fields are mutually exclusive.

        Parameters
        ----------
        expiry_sec : int

        amt_msat : typing.Optional[int]

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        description : typing.Optional[str]

        description_hash : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LnInvoiceResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.invoices.get_a_ln_invoice(
                expiry_sec=420,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_ln_invoice(
            expiry_sec=expiry_sec,
            amt_msat=amt_msat,
            asset_id=asset_id,
            asset_amount=asset_amount,
            description=description,
            description_hash=description_hash,
            request_options=request_options,
        )
        return _response.data
