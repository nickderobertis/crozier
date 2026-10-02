

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPermissionsClient, RawPermissionsClient
from .types.conversation_threshold_get_response import ConversationThresholdGetResponse
from .types.conversation_threshold_put_request_threshold import ConversationThresholdPutRequestThreshold
from .types.conversation_threshold_put_response import ConversationThresholdPutResponse
from .types.permissions_thresholds_get_response import PermissionsThresholdsGetResponse
from .types.permissions_thresholds_put_request_autonomous import PermissionsThresholdsPutRequestAutonomous
from .types.permissions_thresholds_put_request_headless import PermissionsThresholdsPutRequestHeadless
from .types.permissions_thresholds_put_request_interactive import PermissionsThresholdsPutRequestInteractive
from .types.permissions_thresholds_put_response import PermissionsThresholdsPutResponse


OMIT = typing.cast(typing.Any, ...)


class PermissionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPermissionsClient
        """
        return self._raw_client

    def thresholds_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PermissionsThresholdsGetResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermissionsThresholdsGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.permissions.thresholds_get()
        """
        _response = self._raw_client.thresholds_get(request_options=request_options)
        return _response.data

    def thresholds_put(
        self,
        *,
        interactive: typing.Optional[PermissionsThresholdsPutRequestInteractive] = OMIT,
        autonomous: typing.Optional[PermissionsThresholdsPutRequestAutonomous] = OMIT,
        headless: typing.Optional[PermissionsThresholdsPutRequestHeadless] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PermissionsThresholdsPutResponse:
        """
        Partial update — omitted modes keep their current value. Returns the full post-update set.

        Parameters
        ----------
        interactive : typing.Optional[PermissionsThresholdsPutRequestInteractive]

        autonomous : typing.Optional[PermissionsThresholdsPutRequestAutonomous]

        headless : typing.Optional[PermissionsThresholdsPutRequestHeadless]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermissionsThresholdsPutResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.permissions.thresholds_put()
        """
        _response = self._raw_client.thresholds_put(
            interactive=interactive, autonomous=autonomous, headless=headless, request_options=request_options
        )
        return _response.data

    def conversation_threshold_get(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConversationThresholdGetResponse:
        """
        Returns { threshold: null } when no override exists. (Gateways predating that behavior returned 404 for the same condition; clients tolerate both during rollout.)

        Parameters
        ----------
        conversation_id : str
            The conversation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationThresholdGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.permissions.conversation_threshold_get(
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.conversation_threshold_get(conversation_id, request_options=request_options)
        return _response.data

    def conversation_threshold_put(
        self,
        conversation_id: str,
        *,
        threshold: ConversationThresholdPutRequestThreshold,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationThresholdPutResponse:
        """
        Parameters
        ----------
        conversation_id : str
            The conversation id

        threshold : ConversationThresholdPutRequestThreshold

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationThresholdPutResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.permissions.conversation_threshold_put(
            conversation_id="conversation_id",
            threshold="none",
        )
        """
        _response = self._raw_client.conversation_threshold_put(
            conversation_id, threshold=threshold, request_options=request_options
        )
        return _response.data

    def conversation_threshold_delete(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Idempotent — succeeds even when no override exists.

        Parameters
        ----------
        conversation_id : str
            The conversation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.permissions.conversation_threshold_delete(
            conversation_id="conversation_id",
        )
        """
        _response = self._raw_client.conversation_threshold_delete(conversation_id, request_options=request_options)
        return _response.data


class AsyncPermissionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPermissionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPermissionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPermissionsClient
        """
        return self._raw_client

    async def thresholds_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PermissionsThresholdsGetResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermissionsThresholdsGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.permissions.thresholds_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.thresholds_get(request_options=request_options)
        return _response.data

    async def thresholds_put(
        self,
        *,
        interactive: typing.Optional[PermissionsThresholdsPutRequestInteractive] = OMIT,
        autonomous: typing.Optional[PermissionsThresholdsPutRequestAutonomous] = OMIT,
        headless: typing.Optional[PermissionsThresholdsPutRequestHeadless] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PermissionsThresholdsPutResponse:
        """
        Partial update — omitted modes keep their current value. Returns the full post-update set.

        Parameters
        ----------
        interactive : typing.Optional[PermissionsThresholdsPutRequestInteractive]

        autonomous : typing.Optional[PermissionsThresholdsPutRequestAutonomous]

        headless : typing.Optional[PermissionsThresholdsPutRequestHeadless]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PermissionsThresholdsPutResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.permissions.thresholds_put()


        asyncio.run(main())
        """
        _response = await self._raw_client.thresholds_put(
            interactive=interactive, autonomous=autonomous, headless=headless, request_options=request_options
        )
        return _response.data

    async def conversation_threshold_get(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ConversationThresholdGetResponse:
        """
        Returns { threshold: null } when no override exists. (Gateways predating that behavior returned 404 for the same condition; clients tolerate both during rollout.)

        Parameters
        ----------
        conversation_id : str
            The conversation id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationThresholdGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.permissions.conversation_threshold_get(
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.conversation_threshold_get(conversation_id, request_options=request_options)
        return _response.data

    async def conversation_threshold_put(
        self,
        conversation_id: str,
        *,
        threshold: ConversationThresholdPutRequestThreshold,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConversationThresholdPutResponse:
        """
        Parameters
        ----------
        conversation_id : str
            The conversation id

        threshold : ConversationThresholdPutRequestThreshold

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConversationThresholdPutResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.permissions.conversation_threshold_put(
                conversation_id="conversation_id",
                threshold="none",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.conversation_threshold_put(
            conversation_id, threshold=threshold, request_options=request_options
        )
        return _response.data

    async def conversation_threshold_delete(
        self, conversation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Idempotent — succeeds even when no override exists.

        Parameters
        ----------
        conversation_id : str
            The conversation id

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
            await client.permissions.conversation_threshold_delete(
                conversation_id="conversation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.conversation_threshold_delete(
            conversation_id, request_options=request_options
        )
        return _response.data
