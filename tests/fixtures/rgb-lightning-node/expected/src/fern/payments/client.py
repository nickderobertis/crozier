

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_payment_response import GetPaymentResponse
from ..types.keysend_response import KeysendResponse
from ..types.list_payments_response import ListPaymentsResponse
from ..types.send_payment_response import SendPaymentResponse
from .raw_client import AsyncRawPaymentsClient, RawPaymentsClient


OMIT = typing.cast(typing.Any, ...)


class PaymentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPaymentsClient
        """
        return self._raw_client

    def get_a_payment(
        self, *, payment_hash: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPaymentResponse:
        """
        Get a payment by its payment hash

        Parameters
        ----------
        payment_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.payments.get_a_payment(
            payment_hash="5ca5d81b482b4015e7b14df7a27fe0a38c226273604ffd3b008b752571811938",
        )
        """
        _response = self._raw_client.get_a_payment(payment_hash=payment_hash, request_options=request_options)
        return _response.data

    def send_to_a_peer_spontaneously(
        self,
        *,
        dest_pubkey: str,
        amt_msat: int,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KeysendResponse:
        """
        Send bitcoins and RGB assets to a LN peer spontaneously (without a LN invoice)

        Parameters
        ----------
        dest_pubkey : str

        amt_msat : int

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeysendResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.payments.send_to_a_peer_spontaneously(
            dest_pubkey="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d",
            amt_msat=3000000,
        )
        """
        _response = self._raw_client.send_to_a_peer_spontaneously(
            dest_pubkey=dest_pubkey,
            amt_msat=amt_msat,
            asset_id=asset_id,
            asset_amount=asset_amount,
            request_options=request_options,
        )
        return _response.data

    def list_payments(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListPaymentsResponse:
        """
        List the node's LN payments

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPaymentsResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.payments.list_payments()
        """
        _response = self._raw_client.list_payments(request_options=request_options)
        return _response.data

    def send_a_payment(
        self,
        *,
        invoice: str,
        amt_msat: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendPaymentResponse:
        """
        Pay the provided LN invoice

        Parameters
        ----------
        invoice : str

        amt_msat : typing.Optional[int]

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendPaymentResponse
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.payments.send_a_payment(
            invoice="lnbcrt30u1pjv6yzndqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qdpc280eur52luxppv6f3nnj8l6vnd9g2hnv3qv6mjhmhvlzf6327pp5tjjasx6g9dqptea3fhm6yllq5wxzycnnvp8l6wcq3d6j2uvpryuqsp5l8az8x3g8fe05dg7cmgddld3da09nfjvky8xftwsk4cj8p2l7kfq9qyysgqcqpcxqzdylzlwfnkyw3jv344x4rzwgkk53ng0fhxy5rdduk4g5tpvea8xa6rfckkza35va28xjn2tqkhgarcxep5umm4x5k56wfcdvu95eq7qzp20vrl4xz76syapsa3c09j7lg5gerkaj63llj0ark7ph8hfketn6fkqzm8laf66dhsncm23wkwm5l5377we9e8lnlknnkwje5eefkccusqm6rqt8",
        )
        """
        _response = self._raw_client.send_a_payment(
            invoice=invoice,
            amt_msat=amt_msat,
            asset_id=asset_id,
            asset_amount=asset_amount,
            request_options=request_options,
        )
        return _response.data


class AsyncPaymentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPaymentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPaymentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPaymentsClient
        """
        return self._raw_client

    async def get_a_payment(
        self, *, payment_hash: str, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPaymentResponse:
        """
        Get a payment by its payment hash

        Parameters
        ----------
        payment_hash : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPaymentResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payments.get_a_payment(
                payment_hash="5ca5d81b482b4015e7b14df7a27fe0a38c226273604ffd3b008b752571811938",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_payment(payment_hash=payment_hash, request_options=request_options)
        return _response.data

    async def send_to_a_peer_spontaneously(
        self,
        *,
        dest_pubkey: str,
        amt_msat: int,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> KeysendResponse:
        """
        Send bitcoins and RGB assets to a LN peer spontaneously (without a LN invoice)

        Parameters
        ----------
        dest_pubkey : str

        amt_msat : int

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        KeysendResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payments.send_to_a_peer_spontaneously(
                dest_pubkey="03b79a4bc1ec365524b4fab9a39eb133753646babb5a1da5c4bc94c53110b7795d",
                amt_msat=3000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_to_a_peer_spontaneously(
            dest_pubkey=dest_pubkey,
            amt_msat=amt_msat,
            asset_id=asset_id,
            asset_amount=asset_amount,
            request_options=request_options,
        )
        return _response.data

    async def list_payments(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListPaymentsResponse:
        """
        List the node's LN payments

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPaymentsResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payments.list_payments()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_payments(request_options=request_options)
        return _response.data

    async def send_a_payment(
        self,
        *,
        invoice: str,
        amt_msat: typing.Optional[int] = OMIT,
        asset_id: typing.Optional[str] = OMIT,
        asset_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SendPaymentResponse:
        """
        Pay the provided LN invoice

        Parameters
        ----------
        invoice : str

        amt_msat : typing.Optional[int]

        asset_id : typing.Optional[str]

        asset_amount : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SendPaymentResponse
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.payments.send_a_payment(
                invoice="lnbcrt30u1pjv6yzndqud3jxktt5w46x7unfv9kz6mn0v3jsnp4qdpc280eur52luxppv6f3nnj8l6vnd9g2hnv3qv6mjhmhvlzf6327pp5tjjasx6g9dqptea3fhm6yllq5wxzycnnvp8l6wcq3d6j2uvpryuqsp5l8az8x3g8fe05dg7cmgddld3da09nfjvky8xftwsk4cj8p2l7kfq9qyysgqcqpcxqzdylzlwfnkyw3jv344x4rzwgkk53ng0fhxy5rdduk4g5tpvea8xa6rfckkza35va28xjn2tqkhgarcxep5umm4x5k56wfcdvu95eq7qzp20vrl4xz76syapsa3c09j7lg5gerkaj63llj0ark7ph8hfketn6fkqzm8laf66dhsncm23wkwm5l5377we9e8lnlknnkwje5eefkccusqm6rqt8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_a_payment(
            invoice=invoice,
            amt_msat=amt_msat,
            asset_id=asset_id,
            asset_amount=asset_amount,
            request_options=request_options,
        )
        return _response.data
