

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feedback import Feedback
from ..types.seldon_message import SeldonMessage
from ..types.seldon_message_list import SeldonMessageList
from .raw_client import AsyncRawInternalClient, RawInternalClient


OMIT = typing.cast(typing.Any, ...)


class InternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawInternalClient
        """
        return self._raw_client

    def aggregate(
        self, *, body: SeldonMessageList, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        body : SeldonMessageList

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi, SeldonMessageList

        client = FernApi()
        client.internal.aggregate(
            body=SeldonMessageList(),
        )
        """
        _response = self._raw_client.aggregate(body=body, request_options=request_options)
        return _response.data

    def aggregate2(
        self,
        *,
        json: typing.Optional[SeldonMessageList] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessageList]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal.aggregate2()
        """
        _response = self._raw_client.aggregate2(json=json, request_options=request_options)
        return _response.data

    def transform_input4(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi, SeldonMessage

        client = FernApi()
        client.internal.transform_input4(
            json=SeldonMessage(),
        )
        """
        _response = self._raw_client.transform_input4(json=json, request_options=request_options)
        return _response.data

    def transform_input3(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal.transform_input3()
        """
        _response = self._raw_client.transform_input3(json=json, request_options=request_options)
        return _response.data

    def route2(self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None) -> SeldonMessage:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi, SeldonMessage

        client = FernApi()
        client.internal.route2(
            json=SeldonMessage(),
        )
        """
        _response = self._raw_client.route2(json=json, request_options=request_options)
        return _response.data

    def route(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal.route()
        """
        _response = self._raw_client.route(json=json, request_options=request_options)
        return _response.data

    def send_feedback2(
        self, *, json: Feedback, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : Feedback

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import Feedback, FernApi

        client = FernApi()
        client.internal.send_feedback2(
            json=Feedback(),
        )
        """
        _response = self._raw_client.send_feedback2(json=json, request_options=request_options)
        return _response.data

    def send_feedback(
        self, *, json: typing.Optional[Feedback] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[Feedback]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal.send_feedback()
        """
        _response = self._raw_client.send_feedback(json=json, request_options=request_options)
        return _response.data

    def transform_input2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi, SeldonMessage

        client = FernApi()
        client.internal.transform_input2(
            json=SeldonMessage(),
        )
        """
        _response = self._raw_client.transform_input2(json=json, request_options=request_options)
        return _response.data

    def transform_input(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal.transform_input()
        """
        _response = self._raw_client.transform_input(json=json, request_options=request_options)
        return _response.data

    def transform_output2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi, SeldonMessage

        client = FernApi()
        client.internal.transform_output2(
            json=SeldonMessage(),
        )
        """
        _response = self._raw_client.transform_output2(json=json, request_options=request_options)
        return _response.data

    def transform_output(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.internal.transform_output()
        """
        _response = self._raw_client.transform_output(json=json, request_options=request_options)
        return _response.data


class AsyncInternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawInternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawInternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawInternalClient
        """
        return self._raw_client

    async def aggregate(
        self, *, body: SeldonMessageList, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        body : SeldonMessageList

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SeldonMessageList

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.aggregate(
                body=SeldonMessageList(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregate(body=body, request_options=request_options)
        return _response.data

    async def aggregate2(
        self,
        *,
        json: typing.Optional[SeldonMessageList] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessageList]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.aggregate2()


        asyncio.run(main())
        """
        _response = await self._raw_client.aggregate2(json=json, request_options=request_options)
        return _response.data

    async def transform_input4(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SeldonMessage

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.transform_input4(
                json=SeldonMessage(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transform_input4(json=json, request_options=request_options)
        return _response.data

    async def transform_input3(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.transform_input3()


        asyncio.run(main())
        """
        _response = await self._raw_client.transform_input3(json=json, request_options=request_options)
        return _response.data

    async def route2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SeldonMessage

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.route2(
                json=SeldonMessage(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.route2(json=json, request_options=request_options)
        return _response.data

    async def route(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.route()


        asyncio.run(main())
        """
        _response = await self._raw_client.route(json=json, request_options=request_options)
        return _response.data

    async def send_feedback2(
        self, *, json: Feedback, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : Feedback

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, Feedback

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.send_feedback2(
                json=Feedback(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_feedback2(json=json, request_options=request_options)
        return _response.data

    async def send_feedback(
        self, *, json: typing.Optional[Feedback] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[Feedback]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.send_feedback()


        asyncio.run(main())
        """
        _response = await self._raw_client.send_feedback(json=json, request_options=request_options)
        return _response.data

    async def transform_input2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SeldonMessage

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.transform_input2(
                json=SeldonMessage(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transform_input2(json=json, request_options=request_options)
        return _response.data

    async def transform_input(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.transform_input()


        asyncio.run(main())
        """
        _response = await self._raw_client.transform_input(json=json, request_options=request_options)
        return _response.data

    async def transform_output2(
        self, *, json: SeldonMessage, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : SeldonMessage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SeldonMessage

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.transform_output2(
                json=SeldonMessage(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.transform_output2(json=json, request_options=request_options)
        return _response.data

    async def transform_output(
        self, *, json: typing.Optional[SeldonMessage] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> SeldonMessage:
        """
        Parameters
        ----------
        json : typing.Optional[SeldonMessage]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SeldonMessage
            A successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.internal.transform_output()


        asyncio.run(main())
        """
        _response = await self._raw_client.transform_output(json=json, request_options=request_options)
        return _response.data
