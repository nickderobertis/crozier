

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.customer import Customer
from ..types.payment import Payment
from .raw_client import AsyncRawPaymentsClient, RawPaymentsClient
from .types.create_payment_request_payment import CreatePaymentRequestPayment
from .types.listpayments_response import ListpaymentsResponse


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

    def listpayments(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListpaymentsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page number

        limit : typing.Optional[int]
            Number of results per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListpaymentsResponse
            List of payments

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.listpayments()
        """
        _response = self._raw_client.listpayments(page=page, limit=limit, request_options=request_options)
        return _response.data

    def createpayment(
        self,
        *,
        payment: CreatePaymentRequestPayment,
        customer: typing.Optional[Customer] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Payment:
        """
        Parameters
        ----------
        payment : CreatePaymentRequestPayment

        customer : typing.Optional[Customer]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment created successfully

        Examples
        --------
        from fern.payments import CreatePaymentRequestPayment

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.createpayment(
            payment=CreatePaymentRequestPayment(
                purchase_amount=1,
                return_url="return_url",
                installments_count=1,
            ),
        )
        """
        _response = self._raw_client.createpayment(payment=payment, customer=customer, request_options=request_options)
        return _response.data

    def getpayment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Payment:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.getpayment(
            id="id",
        )
        """
        _response = self._raw_client.getpayment(id, request_options=request_options)
        return _response.data

    def modifypayment(
        self,
        id: str,
        *,
        purchase_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Payment:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        purchase_amount : typing.Optional[int]
            Updated purchase amount in cents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment modified

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.modifypayment(
            id="id",
        )
        """
        _response = self._raw_client.modifypayment(id, purchase_amount=purchase_amount, request_options=request_options)
        return _response.data

    def cancelpayment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Payment:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment cancelled

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.cancelpayment(
            id="id",
        )
        """
        _response = self._raw_client.cancelpayment(id, request_options=request_options)
        return _response.data

    def capturepayment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Payment:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment captured

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.capturepayment(
            id="id",
        )
        """
        _response = self._raw_client.capturepayment(id, request_options=request_options)
        return _response.data

    def sendpaymentsms(self, id: str, *, phone: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        phone : str
            Phone number to send the payment link to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.sendpaymentsms(
            id="id",
            phone="phone",
        )
        """
        _response = self._raw_client.sendpaymentsms(id, phone=phone, request_options=request_options)
        return _response.data

    def sendpaymentemail(self, id: str, *, email: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        email : str
            Email address to send the payment link to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.sendpaymentemail(
            id="id",
            email="email",
        )
        """
        _response = self._raw_client.sendpaymentemail(id, email=email, request_options=request_options)
        return _response.data

    def cancel_payment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Cancel an existing payment.

        Parameters
        ----------
        id : str
            Payment ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Cancel payment successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.cancel_payment(
            id="id",
        )
        """
        _response = self._raw_client.cancel_payment(id, request_options=request_options)
        return _response.data

    def update_payment(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Modify an existing payment.

        Parameters
        ----------
        id : str
            Payment ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Update payment successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.payments.update_payment(
            id="id",
            request={"string": {"key": "value"}},
        )
        """
        _response = self._raw_client.update_payment(id, request=request, request_options=request_options)
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

    async def listpayments(
        self,
        *,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListpaymentsResponse:
        """
        Parameters
        ----------
        page : typing.Optional[int]
            Page number

        limit : typing.Optional[int]
            Number of results per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListpaymentsResponse
            List of payments

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.listpayments()


        asyncio.run(main())
        """
        _response = await self._raw_client.listpayments(page=page, limit=limit, request_options=request_options)
        return _response.data

    async def createpayment(
        self,
        *,
        payment: CreatePaymentRequestPayment,
        customer: typing.Optional[Customer] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Payment:
        """
        Parameters
        ----------
        payment : CreatePaymentRequestPayment

        customer : typing.Optional[Customer]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment created successfully

        Examples
        --------
        import asyncio

        from fern.payments import CreatePaymentRequestPayment

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.createpayment(
                payment=CreatePaymentRequestPayment(
                    purchase_amount=1,
                    return_url="return_url",
                    installments_count=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createpayment(
            payment=payment, customer=customer, request_options=request_options
        )
        return _response.data

    async def getpayment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Payment:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.getpayment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpayment(id, request_options=request_options)
        return _response.data

    async def modifypayment(
        self,
        id: str,
        *,
        purchase_amount: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Payment:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        purchase_amount : typing.Optional[int]
            Updated purchase amount in cents

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment modified

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.modifypayment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modifypayment(
            id, purchase_amount=purchase_amount, request_options=request_options
        )
        return _response.data

    async def cancelpayment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Payment:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment cancelled

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.cancelpayment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancelpayment(id, request_options=request_options)
        return _response.data

    async def capturepayment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Payment:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Payment
            Payment captured

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.capturepayment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.capturepayment(id, request_options=request_options)
        return _response.data

    async def sendpaymentsms(
        self, id: str, *, phone: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        phone : str
            Phone number to send the payment link to

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.sendpaymentsms(
                id="id",
                phone="phone",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sendpaymentsms(id, phone=phone, request_options=request_options)
        return _response.data

    async def sendpaymentemail(
        self, id: str, *, email: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        id : str
            Payment identifier

        email : str
            Email address to send the payment link to

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.sendpaymentemail(
                id="id",
                email="email",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sendpaymentemail(id, email=email, request_options=request_options)
        return _response.data

    async def cancel_payment(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Cancel an existing payment.

        Parameters
        ----------
        id : str
            Payment ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Cancel payment successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.cancel_payment(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_payment(id, request_options=request_options)
        return _response.data

    async def update_payment(
        self, id: str, *, request: typing.Dict[str, typing.Any], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Modify an existing payment.

        Parameters
        ----------
        id : str
            Payment ID

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Update payment successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.payments.update_payment(
                id="id",
                request={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_payment(id, request=request, request_options=request_options)
        return _response.data
