

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.phone_number import PhoneNumber
from ..types.phone_number_page import PhoneNumberPage
from .raw_client import AsyncRawNumbersClient, RawNumbersClient
from .types.buy_phone_number_request_inbound_agent import BuyPhoneNumberRequestInboundAgent
from .types.buy_phone_number_request_telephony_provider import BuyPhoneNumberRequestTelephonyProvider
from .types.link_phone_number_request_inbound_agent import LinkPhoneNumberRequestInboundAgent
from .types.update_number_request_example_context import UpdateNumberRequestExampleContext
from .types.update_number_request_inbound_agent import UpdateNumberRequestInboundAgent
from .types.update_number_request_label import UpdateNumberRequestLabel
from .types.update_number_request_outbound_only import UpdateNumberRequestOutboundOnly


OMIT = typing.cast(typing.Any, ...)


class NumbersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNumbersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNumbersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNumbersClient
        """
        return self._raw_client

    def list_numbers(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumberPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumberPage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.numbers.list_numbers()
        """
        _response = self._raw_client.list_numbers(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    def get_number(self, *, phone_number: str, request_options: typing.Optional[RequestOptions] = None) -> PhoneNumber:
        """
        Parameters
        ----------
        phone_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.numbers.get_number(
            phone_number="phone_number",
        )
        """
        _response = self._raw_client.get_number(phone_number=phone_number, request_options=request_options)
        return _response.data

    def buy_number(
        self,
        *,
        area_code: typing.Optional[str] = OMIT,
        telephony_provider: typing.Optional[BuyPhoneNumberRequestTelephonyProvider] = OMIT,
        telephony_account_connection: typing.Optional[str] = OMIT,
        inbound_agent: typing.Optional[BuyPhoneNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumber:
        """
        Parameters
        ----------
        area_code : typing.Optional[str]

        telephony_provider : typing.Optional[BuyPhoneNumberRequestTelephonyProvider]

        telephony_account_connection : typing.Optional[str]

        inbound_agent : typing.Optional[BuyPhoneNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.numbers.buy_number()
        """
        _response = self._raw_client.buy_number(
            area_code=area_code,
            telephony_provider=telephony_provider,
            telephony_account_connection=telephony_account_connection,
            inbound_agent=inbound_agent,
            request_options=request_options,
        )
        return _response.data

    def update_number(
        self,
        *,
        phone_number: str,
        outbound_only: typing.Optional[UpdateNumberRequestOutboundOnly] = OMIT,
        example_context: typing.Optional[UpdateNumberRequestExampleContext] = OMIT,
        label: typing.Optional[UpdateNumberRequestLabel] = OMIT,
        inbound_agent: typing.Optional[UpdateNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumber:
        """
        Parameters
        ----------
        phone_number : str

        outbound_only : typing.Optional[UpdateNumberRequestOutboundOnly]

        example_context : typing.Optional[UpdateNumberRequestExampleContext]

        label : typing.Optional[UpdateNumberRequestLabel]

        inbound_agent : typing.Optional[UpdateNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.numbers.update_number(
            phone_number="phone_number",
        )
        """
        _response = self._raw_client.update_number(
            phone_number=phone_number,
            outbound_only=outbound_only,
            example_context=example_context,
            label=label,
            inbound_agent=inbound_agent,
            request_options=request_options,
        )
        return _response.data

    def cancel_number(
        self, *, phone_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumber:
        """
        Parameters
        ----------
        phone_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.numbers.cancel_number(
            phone_number="phone_number",
        )
        """
        _response = self._raw_client.cancel_number(phone_number=phone_number, request_options=request_options)
        return _response.data

    def link_number(
        self,
        *,
        phone_number: str,
        telephony_account_connection: str,
        outbound_only: typing.Optional[bool] = OMIT,
        inbound_agent: typing.Optional[LinkPhoneNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumber:
        """
        Parameters
        ----------
        phone_number : str

        telephony_account_connection : str

        outbound_only : typing.Optional[bool]

        inbound_agent : typing.Optional[LinkPhoneNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.numbers.link_number(
            phone_number="phone_number",
            telephony_account_connection="telephony_account_connection",
        )
        """
        _response = self._raw_client.link_number(
            phone_number=phone_number,
            telephony_account_connection=telephony_account_connection,
            outbound_only=outbound_only,
            inbound_agent=inbound_agent,
            request_options=request_options,
        )
        return _response.data


class AsyncNumbersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNumbersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNumbersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNumbersClient
        """
        return self._raw_client

    async def list_numbers(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumberPage:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumberPage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.numbers.list_numbers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_numbers(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    async def get_number(
        self, *, phone_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumber:
        """
        Parameters
        ----------
        phone_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.numbers.get_number(
                phone_number="phone_number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_number(phone_number=phone_number, request_options=request_options)
        return _response.data

    async def buy_number(
        self,
        *,
        area_code: typing.Optional[str] = OMIT,
        telephony_provider: typing.Optional[BuyPhoneNumberRequestTelephonyProvider] = OMIT,
        telephony_account_connection: typing.Optional[str] = OMIT,
        inbound_agent: typing.Optional[BuyPhoneNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumber:
        """
        Parameters
        ----------
        area_code : typing.Optional[str]

        telephony_provider : typing.Optional[BuyPhoneNumberRequestTelephonyProvider]

        telephony_account_connection : typing.Optional[str]

        inbound_agent : typing.Optional[BuyPhoneNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.numbers.buy_number()


        asyncio.run(main())
        """
        _response = await self._raw_client.buy_number(
            area_code=area_code,
            telephony_provider=telephony_provider,
            telephony_account_connection=telephony_account_connection,
            inbound_agent=inbound_agent,
            request_options=request_options,
        )
        return _response.data

    async def update_number(
        self,
        *,
        phone_number: str,
        outbound_only: typing.Optional[UpdateNumberRequestOutboundOnly] = OMIT,
        example_context: typing.Optional[UpdateNumberRequestExampleContext] = OMIT,
        label: typing.Optional[UpdateNumberRequestLabel] = OMIT,
        inbound_agent: typing.Optional[UpdateNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumber:
        """
        Parameters
        ----------
        phone_number : str

        outbound_only : typing.Optional[UpdateNumberRequestOutboundOnly]

        example_context : typing.Optional[UpdateNumberRequestExampleContext]

        label : typing.Optional[UpdateNumberRequestLabel]

        inbound_agent : typing.Optional[UpdateNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.numbers.update_number(
                phone_number="phone_number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_number(
            phone_number=phone_number,
            outbound_only=outbound_only,
            example_context=example_context,
            label=label,
            inbound_agent=inbound_agent,
            request_options=request_options,
        )
        return _response.data

    async def cancel_number(
        self, *, phone_number: str, request_options: typing.Optional[RequestOptions] = None
    ) -> PhoneNumber:
        """
        Parameters
        ----------
        phone_number : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.numbers.cancel_number(
                phone_number="phone_number",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_number(phone_number=phone_number, request_options=request_options)
        return _response.data

    async def link_number(
        self,
        *,
        phone_number: str,
        telephony_account_connection: str,
        outbound_only: typing.Optional[bool] = OMIT,
        inbound_agent: typing.Optional[LinkPhoneNumberRequestInboundAgent] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PhoneNumber:
        """
        Parameters
        ----------
        phone_number : str

        telephony_account_connection : str

        outbound_only : typing.Optional[bool]

        inbound_agent : typing.Optional[LinkPhoneNumberRequestInboundAgent]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PhoneNumber
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.numbers.link_number(
                phone_number="phone_number",
                telephony_account_connection="telephony_account_connection",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link_number(
            phone_number=phone_number,
            telephony_account_connection=telephony_account_connection,
            outbound_only=outbound_only,
            inbound_agent=inbound_agent,
            request_options=request_options,
        )
        return _response.data
