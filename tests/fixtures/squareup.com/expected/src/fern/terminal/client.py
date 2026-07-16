

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.cancel_terminal_checkout_response import CancelTerminalCheckoutResponse
from ..types.cancel_terminal_refund_response import CancelTerminalRefundResponse
from ..types.create_terminal_checkout_response import CreateTerminalCheckoutResponse
from ..types.create_terminal_refund_response import CreateTerminalRefundResponse
from ..types.get_terminal_checkout_response import GetTerminalCheckoutResponse
from ..types.get_terminal_refund_response import GetTerminalRefundResponse
from ..types.search_terminal_checkouts_response import SearchTerminalCheckoutsResponse
from ..types.search_terminal_refunds_response import SearchTerminalRefundsResponse
from ..types.terminal_checkout import TerminalCheckout
from ..types.terminal_checkout_query import TerminalCheckoutQuery
from ..types.terminal_refund import TerminalRefund
from ..types.terminal_refund_query import TerminalRefundQuery
from .raw_client import AsyncRawTerminalClient, RawTerminalClient


OMIT = typing.cast(typing.Any, ...)


class TerminalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTerminalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTerminalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTerminalClient
        """
        return self._raw_client

    def create_terminal_checkout(
        self,
        *,
        checkout: TerminalCheckout,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTerminalCheckoutResponse:
        """
        Creates a Terminal checkout request and sends it to the specified device to take a payment
        for the requested amount.

        Parameters
        ----------
        checkout : TerminalCheckout

        idempotency_key : str
            A unique string that identifies this `CreateCheckout` request. Keys can be any valid string but
            must be unique for every `CreateCheckout` request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTerminalCheckoutResponse
            Success

        Examples
        --------
        from fern import DeviceCheckoutOptions, FernApi, Money, TerminalCheckout

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.terminal.create_terminal_checkout(
            checkout=TerminalCheckout(
                amount_money=Money(),
                device_options=DeviceCheckoutOptions(
                    device_id="device_id",
                ),
            ),
            idempotency_key="idempotency_key",
        )
        """
        _response = self._raw_client.create_terminal_checkout(
            checkout=checkout, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    def search_terminal_checkouts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[TerminalCheckoutQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchTerminalCheckoutsResponse:
        """
        Retrieves a filtered list of Terminal checkout requests created by the account making the request.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        limit : typing.Optional[int]
            Limits the number of results returned for a single request.

        query : typing.Optional[TerminalCheckoutQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchTerminalCheckoutsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.terminal.search_terminal_checkouts()
        """
        _response = self._raw_client.search_terminal_checkouts(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def get_terminal_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTerminalCheckoutResponse:
        """
        Retrieves a Terminal checkout request by `checkout_id`.

        Parameters
        ----------
        checkout_id : str
            The unique ID for the desired `TerminalCheckout`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTerminalCheckoutResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.terminal.get_terminal_checkout(
            checkout_id="checkout_id",
        )
        """
        _response = self._raw_client.get_terminal_checkout(checkout_id, request_options=request_options)
        return _response.data

    def cancel_terminal_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelTerminalCheckoutResponse:
        """
        Cancels a Terminal checkout request if the status of the request permits it.

        Parameters
        ----------
        checkout_id : str
            The unique ID for the desired `TerminalCheckout`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelTerminalCheckoutResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.terminal.cancel_terminal_checkout(
            checkout_id="checkout_id",
        )
        """
        _response = self._raw_client.cancel_terminal_checkout(checkout_id, request_options=request_options)
        return _response.data

    def create_terminal_refund(
        self,
        *,
        idempotency_key: str,
        refund: typing.Optional[TerminalRefund] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTerminalRefundResponse:
        """
        Creates a request to refund an Interac payment completed on a Square Terminal.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateRefund` request. Keys can be any valid string but
            must be unique for every `CreateRefund` request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        refund : typing.Optional[TerminalRefund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTerminalRefundResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.terminal.create_terminal_refund(
            idempotency_key="idempotency_key",
        )
        """
        _response = self._raw_client.create_terminal_refund(
            idempotency_key=idempotency_key, refund=refund, request_options=request_options
        )
        return _response.data

    def search_terminal_refunds(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[TerminalRefundQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchTerminalRefundsResponse:
        """
        Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.

        limit : typing.Optional[int]
            Limits the number of results returned for a single request.

        query : typing.Optional[TerminalRefundQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchTerminalRefundsResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.terminal.search_terminal_refunds()
        """
        _response = self._raw_client.search_terminal_refunds(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    def get_terminal_refund(
        self, terminal_refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTerminalRefundResponse:
        """
        Retrieves an Interac Terminal refund object by ID.

        Parameters
        ----------
        terminal_refund_id : str
            The unique ID for the desired `TerminalRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTerminalRefundResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.terminal.get_terminal_refund(
            terminal_refund_id="terminal_refund_id",
        )
        """
        _response = self._raw_client.get_terminal_refund(terminal_refund_id, request_options=request_options)
        return _response.data

    def cancel_terminal_refund(
        self, terminal_refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelTerminalRefundResponse:
        """
        Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

        Parameters
        ----------
        terminal_refund_id : str
            The unique ID for the desired `TerminalRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelTerminalRefundResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )
        client.terminal.cancel_terminal_refund(
            terminal_refund_id="terminal_refund_id",
        )
        """
        _response = self._raw_client.cancel_terminal_refund(terminal_refund_id, request_options=request_options)
        return _response.data


class AsyncTerminalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTerminalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTerminalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTerminalClient
        """
        return self._raw_client

    async def create_terminal_checkout(
        self,
        *,
        checkout: TerminalCheckout,
        idempotency_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTerminalCheckoutResponse:
        """
        Creates a Terminal checkout request and sends it to the specified device to take a payment
        for the requested amount.

        Parameters
        ----------
        checkout : TerminalCheckout

        idempotency_key : str
            A unique string that identifies this `CreateCheckout` request. Keys can be any valid string but
            must be unique for every `CreateCheckout` request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTerminalCheckoutResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, DeviceCheckoutOptions, Money, TerminalCheckout

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.create_terminal_checkout(
                checkout=TerminalCheckout(
                    amount_money=Money(),
                    device_options=DeviceCheckoutOptions(
                        device_id="device_id",
                    ),
                ),
                idempotency_key="idempotency_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_terminal_checkout(
            checkout=checkout, idempotency_key=idempotency_key, request_options=request_options
        )
        return _response.data

    async def search_terminal_checkouts(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[TerminalCheckoutQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchTerminalCheckoutsResponse:
        """
        Retrieves a filtered list of Terminal checkout requests created by the account making the request.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.
            See [Pagination](https://developer.squareup.com/docs/basics/api101/pagination) for more information.

        limit : typing.Optional[int]
            Limits the number of results returned for a single request.

        query : typing.Optional[TerminalCheckoutQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchTerminalCheckoutsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.search_terminal_checkouts()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_terminal_checkouts(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def get_terminal_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTerminalCheckoutResponse:
        """
        Retrieves a Terminal checkout request by `checkout_id`.

        Parameters
        ----------
        checkout_id : str
            The unique ID for the desired `TerminalCheckout`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTerminalCheckoutResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.get_terminal_checkout(
                checkout_id="checkout_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_terminal_checkout(checkout_id, request_options=request_options)
        return _response.data

    async def cancel_terminal_checkout(
        self, checkout_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelTerminalCheckoutResponse:
        """
        Cancels a Terminal checkout request if the status of the request permits it.

        Parameters
        ----------
        checkout_id : str
            The unique ID for the desired `TerminalCheckout`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelTerminalCheckoutResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.cancel_terminal_checkout(
                checkout_id="checkout_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_terminal_checkout(checkout_id, request_options=request_options)
        return _response.data

    async def create_terminal_refund(
        self,
        *,
        idempotency_key: str,
        refund: typing.Optional[TerminalRefund] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateTerminalRefundResponse:
        """
        Creates a request to refund an Interac payment completed on a Square Terminal.

        Parameters
        ----------
        idempotency_key : str
            A unique string that identifies this `CreateRefund` request. Keys can be any valid string but
            must be unique for every `CreateRefund` request.

            See [Idempotency keys](https://developer.squareup.com/docs/basics/api101/idempotency) for more information.

        refund : typing.Optional[TerminalRefund]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateTerminalRefundResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.create_terminal_refund(
                idempotency_key="idempotency_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_terminal_refund(
            idempotency_key=idempotency_key, refund=refund, request_options=request_options
        )
        return _response.data

    async def search_terminal_refunds(
        self,
        *,
        cursor: typing.Optional[str] = OMIT,
        limit: typing.Optional[int] = OMIT,
        query: typing.Optional[TerminalRefundQuery] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SearchTerminalRefundsResponse:
        """
        Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A pagination cursor returned by a previous call to this endpoint.
            Provide this cursor to retrieve the next set of results for the original query.

        limit : typing.Optional[int]
            Limits the number of results returned for a single request.

        query : typing.Optional[TerminalRefundQuery]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SearchTerminalRefundsResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.search_terminal_refunds()


        asyncio.run(main())
        """
        _response = await self._raw_client.search_terminal_refunds(
            cursor=cursor, limit=limit, query=query, request_options=request_options
        )
        return _response.data

    async def get_terminal_refund(
        self, terminal_refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetTerminalRefundResponse:
        """
        Retrieves an Interac Terminal refund object by ID.

        Parameters
        ----------
        terminal_refund_id : str
            The unique ID for the desired `TerminalRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetTerminalRefundResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.get_terminal_refund(
                terminal_refund_id="terminal_refund_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_terminal_refund(terminal_refund_id, request_options=request_options)
        return _response.data

    async def cancel_terminal_refund(
        self, terminal_refund_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CancelTerminalRefundResponse:
        """
        Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

        Parameters
        ----------
        terminal_refund_id : str
            The unique ID for the desired `TerminalRefund`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CancelTerminalRefundResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            authorization="YOUR_AUTHORIZATION",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.terminal.cancel_terminal_refund(
                terminal_refund_id="terminal_refund_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_terminal_refund(terminal_refund_id, request_options=request_options)
        return _response.data
