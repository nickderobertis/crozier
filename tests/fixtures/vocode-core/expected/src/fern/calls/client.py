

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.call import Call
from ..types.call_page import CallPage
from .raw_client import AsyncRawCallsClient, RawCallsClient
from .types.create_call_request_agent import CreateCallRequestAgent
from .types.create_call_request_on_no_human_answer import CreateCallRequestOnNoHumanAnswer


OMIT = typing.cast(typing.Any, ...)


class CallsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCallsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCallsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCallsClient
        """
        return self._raw_client

    def list_calls(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CallPage:
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
        CallPage
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calls.list_calls()
        """
        _response = self._raw_client.list_calls(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    def get_call(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Call:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calls.get_call(
            id="id",
        )
        """
        _response = self._raw_client.get_call(id=id, request_options=request_options)
        return _response.data

    def end_call(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Call:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calls.end_call(
            id="id",
        )
        """
        _response = self._raw_client.end_call(id=id, request_options=request_options)
        return _response.data

    def create_call(
        self,
        *,
        from_number: str,
        to_number: str,
        agent: CreateCallRequestAgent,
        on_no_human_answer: typing.Optional[CreateCallRequestOnNoHumanAnswer] = OMIT,
        run_do_not_call_detection: typing.Optional[bool] = OMIT,
        hipaa_compliant: typing.Optional[bool] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        telephony_params: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Call:
        """
        Parameters
        ----------
        from_number : str

        to_number : str

        agent : CreateCallRequestAgent

        on_no_human_answer : typing.Optional[CreateCallRequestOnNoHumanAnswer]

        run_do_not_call_detection : typing.Optional[bool]

        hipaa_compliant : typing.Optional[bool]

        context : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        telephony_params : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calls.create_call(
            from_number="from_number",
            to_number="to_number",
            agent="agent",
        )
        """
        _response = self._raw_client.create_call(
            from_number=from_number,
            to_number=to_number,
            agent=agent,
            on_no_human_answer=on_no_human_answer,
            run_do_not_call_detection=run_do_not_call_detection,
            hipaa_compliant=hipaa_compliant,
            context=context,
            telephony_params=telephony_params,
            request_options=request_options,
        )
        return _response.data

    def get_recording(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.calls.get_recording(
            id="id",
        )
        """
        with self._raw_client.get_recording(id=id, request_options=request_options) as r:
            yield from r.data


class AsyncCallsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCallsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCallsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCallsClient
        """
        return self._raw_client

    async def list_calls(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CallPage:
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
        CallPage
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.list_calls()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_calls(
            page=page, size=size, sort_column=sort_column, sort_desc=sort_desc, request_options=request_options
        )
        return _response.data

    async def get_call(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Call:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.get_call(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_call(id=id, request_options=request_options)
        return _response.data

    async def end_call(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> Call:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.end_call(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.end_call(id=id, request_options=request_options)
        return _response.data

    async def create_call(
        self,
        *,
        from_number: str,
        to_number: str,
        agent: CreateCallRequestAgent,
        on_no_human_answer: typing.Optional[CreateCallRequestOnNoHumanAnswer] = OMIT,
        run_do_not_call_detection: typing.Optional[bool] = OMIT,
        hipaa_compliant: typing.Optional[bool] = OMIT,
        context: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        telephony_params: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Call:
        """
        Parameters
        ----------
        from_number : str

        to_number : str

        agent : CreateCallRequestAgent

        on_no_human_answer : typing.Optional[CreateCallRequestOnNoHumanAnswer]

        run_do_not_call_detection : typing.Optional[bool]

        hipaa_compliant : typing.Optional[bool]

        context : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        telephony_params : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.create_call(
                from_number="from_number",
                to_number="to_number",
                agent="agent",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_call(
            from_number=from_number,
            to_number=to_number,
            agent=agent,
            on_no_human_answer=on_no_human_answer,
            run_do_not_call_detection=run_do_not_call_detection,
            hipaa_compliant=hipaa_compliant,
            context=context,
            telephony_params=telephony_params,
            request_options=request_options,
        )
        return _response.data

    async def get_recording(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.get_recording(
                id="id",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_recording(id=id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
