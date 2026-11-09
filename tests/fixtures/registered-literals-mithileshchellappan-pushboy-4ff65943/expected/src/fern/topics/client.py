

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.topic import Topic
from .raw_client import AsyncRawTopicsClient, RawTopicsClient
from .types.get_v1topics_topic_id_count_response import GetV1TopicsTopicIdCountResponse


OMIT = typing.cast(typing.Any, ...)


class TopicsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTopicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTopicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTopicsClient
        """
        return self._raw_client

    def list_topics(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Topic]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Topic]
            Topics.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.list_topics()
        """
        _response = self._raw_client.list_topics(request_options=request_options)
        return _response.data

    def create_a_topic(self, *, id: str, name: str, request_options: typing.Optional[RequestOptions] = None) -> Topic:
        """
        Parameters
        ----------
        id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Topic
            Topic created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.create_a_topic(
            id="broadcast",
            name="Broadcast",
        )
        """
        _response = self._raw_client.create_a_topic(id=id, name=name, request_options=request_options)
        return _response.data

    def get_a_topic(self, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Topic:
        """
        Parameters
        ----------
        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Topic
            Topic found.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.get_a_topic(
            topic_id="broadcast",
        )
        """
        _response = self._raw_client.get_a_topic(topic_id, request_options=request_options)
        return _response.data

    def delete_a_topic(self, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.delete_a_topic(
            topic_id="broadcast",
        )
        """
        _response = self._raw_client.delete_a_topic(topic_id, request_options=request_options)
        return _response.data

    def count_topic_subscribers(
        self, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1TopicsTopicIdCountResponse:
        """
        Parameters
        ----------
        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1TopicsTopicIdCountResponse
            Subscriber count. Missing topics currently can return 0.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.topics.count_topic_subscribers(
            topic_id="broadcast",
        )
        """
        _response = self._raw_client.count_topic_subscribers(topic_id, request_options=request_options)
        return _response.data


class AsyncTopicsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTopicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTopicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTopicsClient
        """
        return self._raw_client

    async def list_topics(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Topic]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Topic]
            Topics.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.list_topics()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_topics(request_options=request_options)
        return _response.data

    async def create_a_topic(
        self, *, id: str, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> Topic:
        """
        Parameters
        ----------
        id : str

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Topic
            Topic created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.create_a_topic(
                id="broadcast",
                name="Broadcast",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_topic(id=id, name=name, request_options=request_options)
        return _response.data

    async def get_a_topic(self, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Topic:
        """
        Parameters
        ----------
        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Topic
            Topic found.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.get_a_topic(
                topic_id="broadcast",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_topic(topic_id, request_options=request_options)
        return _response.data

    async def delete_a_topic(self, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.delete_a_topic(
                topic_id="broadcast",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_topic(topic_id, request_options=request_options)
        return _response.data

    async def count_topic_subscribers(
        self, topic_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetV1TopicsTopicIdCountResponse:
        """
        Parameters
        ----------
        topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetV1TopicsTopicIdCountResponse
            Subscriber count. Missing topics currently can return 0.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.topics.count_topic_subscribers(
                topic_id="broadcast",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.count_topic_subscribers(topic_id, request_options=request_options)
        return _response.data
