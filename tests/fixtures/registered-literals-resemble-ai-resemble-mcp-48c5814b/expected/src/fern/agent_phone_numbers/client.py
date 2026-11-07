

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAgentPhoneNumbersClient, RawAgentPhoneNumbersClient
from .types.create_phone_number_request_provider import CreatePhoneNumberRequestProvider
from .types.create_phone_number_response import CreatePhoneNumberResponse
from .types.delete_phone_number_response import DeletePhoneNumberResponse
from .types.force_delete_phone_number_response import ForceDeletePhoneNumberResponse
from .types.get_phone_number_response import GetPhoneNumberResponse
from .types.list_phone_numbers_response import ListPhoneNumbersResponse


OMIT = typing.cast(typing.Any, ...)


class AgentPhoneNumbersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentPhoneNumbersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentPhoneNumbersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentPhoneNumbersClient
        """
        return self._raw_client

    def list_phone_numbers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListPhoneNumbersResponse:
        """
        List all agent phone numbers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPhoneNumbersResponse
            List of phone numbers

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_phone_numbers.list_phone_numbers()
        """
        _response = self._raw_client.list_phone_numbers(request_options=request_options)
        return _response.data

    def create_phone_number(
        self,
        *,
        phone_number: str,
        label: str,
        supports_inbound: typing.Optional[bool] = OMIT,
        supports_outbound: typing.Optional[bool] = OMIT,
        provider: typing.Optional[CreatePhoneNumberRequestProvider] = OMIT,
        twilio_account_sid: typing.Optional[str] = OMIT,
        twilio_auth_token: typing.Optional[str] = OMIT,
        outbound_trunk: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        inbound_trunk: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePhoneNumberResponse:
        """
        Create a new agent phone number

        Parameters
        ----------
        phone_number : str
            E.164 formatted phone number

        label : str

        supports_inbound : typing.Optional[bool]

        supports_outbound : typing.Optional[bool]

        provider : typing.Optional[CreatePhoneNumberRequestProvider]

        twilio_account_sid : typing.Optional[str]

        twilio_auth_token : typing.Optional[str]

        outbound_trunk : typing.Optional[typing.Dict[str, typing.Any]]

        inbound_trunk : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePhoneNumberResponse
            Phone number created

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_phone_numbers.create_phone_number(
            phone_number="phone_number",
            label="label",
        )
        """
        _response = self._raw_client.create_phone_number(
            phone_number=phone_number,
            label=label,
            supports_inbound=supports_inbound,
            supports_outbound=supports_outbound,
            provider=provider,
            twilio_account_sid=twilio_account_sid,
            twilio_auth_token=twilio_auth_token,
            outbound_trunk=outbound_trunk,
            inbound_trunk=inbound_trunk,
            request_options=request_options,
        )
        return _response.data

    def get_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPhoneNumberResponse:
        """
        Get agent phone number details

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPhoneNumberResponse
            Phone number details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_phone_numbers.get_phone_number(
            id=1,
        )
        """
        _response = self._raw_client.get_phone_number(id, request_options=request_options)
        return _response.data

    def delete_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePhoneNumberResponse:
        """
        Delete an agent phone number

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePhoneNumberResponse
            Phone number deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_phone_numbers.delete_phone_number(
            id=1,
        )
        """
        _response = self._raw_client.delete_phone_number(id, request_options=request_options)
        return _response.data

    def force_delete_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ForceDeletePhoneNumberResponse:
        """
        Force delete an agent phone number even if linked to agent

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForceDeletePhoneNumberResponse
            Phone number force deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_phone_numbers.force_delete_phone_number(
            id=1,
        )
        """
        _response = self._raw_client.force_delete_phone_number(id, request_options=request_options)
        return _response.data


class AsyncAgentPhoneNumbersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentPhoneNumbersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentPhoneNumbersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentPhoneNumbersClient
        """
        return self._raw_client

    async def list_phone_numbers(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListPhoneNumbersResponse:
        """
        List all agent phone numbers

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListPhoneNumbersResponse
            List of phone numbers

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_phone_numbers.list_phone_numbers()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_phone_numbers(request_options=request_options)
        return _response.data

    async def create_phone_number(
        self,
        *,
        phone_number: str,
        label: str,
        supports_inbound: typing.Optional[bool] = OMIT,
        supports_outbound: typing.Optional[bool] = OMIT,
        provider: typing.Optional[CreatePhoneNumberRequestProvider] = OMIT,
        twilio_account_sid: typing.Optional[str] = OMIT,
        twilio_auth_token: typing.Optional[str] = OMIT,
        outbound_trunk: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        inbound_trunk: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreatePhoneNumberResponse:
        """
        Create a new agent phone number

        Parameters
        ----------
        phone_number : str
            E.164 formatted phone number

        label : str

        supports_inbound : typing.Optional[bool]

        supports_outbound : typing.Optional[bool]

        provider : typing.Optional[CreatePhoneNumberRequestProvider]

        twilio_account_sid : typing.Optional[str]

        twilio_auth_token : typing.Optional[str]

        outbound_trunk : typing.Optional[typing.Dict[str, typing.Any]]

        inbound_trunk : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreatePhoneNumberResponse
            Phone number created

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_phone_numbers.create_phone_number(
                phone_number="phone_number",
                label="label",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_phone_number(
            phone_number=phone_number,
            label=label,
            supports_inbound=supports_inbound,
            supports_outbound=supports_outbound,
            provider=provider,
            twilio_account_sid=twilio_account_sid,
            twilio_auth_token=twilio_auth_token,
            outbound_trunk=outbound_trunk,
            inbound_trunk=inbound_trunk,
            request_options=request_options,
        )
        return _response.data

    async def get_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPhoneNumberResponse:
        """
        Get agent phone number details

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPhoneNumberResponse
            Phone number details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_phone_numbers.get_phone_number(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_phone_number(id, request_options=request_options)
        return _response.data

    async def delete_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeletePhoneNumberResponse:
        """
        Delete an agent phone number

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeletePhoneNumberResponse
            Phone number deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_phone_numbers.delete_phone_number(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_phone_number(id, request_options=request_options)
        return _response.data

    async def force_delete_phone_number(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ForceDeletePhoneNumberResponse:
        """
        Force delete an agent phone number even if linked to agent

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ForceDeletePhoneNumberResponse
            Phone number force deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_phone_numbers.force_delete_phone_number(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.force_delete_phone_number(id, request_options=request_options)
        return _response.data
