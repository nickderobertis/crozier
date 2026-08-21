

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.contexts_response import ContextsResponse
from .raw_client import AsyncRawFlagsClient, RawFlagsClient


class FlagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFlagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFlagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFlagsClient
        """
        return self._raw_client

    def get_personal_data_contexts(
        self, *, accept_language: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextsResponse:
        """
        The API exposes actions against contexts (logical groups) of personal data in the given system. The grouping should be based on usage, e.g., personal data used for marketing, personal data collected for usage analysis, or personal data processed for technical realisation of the service. The same personal data type (e.g., an email address) may be in several contexts; this does not imply it would be actually duplicated in the system, but it could be used in different contexts. Typically, a single context should not contain data that is processed under different basis of processing.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.flags.get_personal_data_contexts(
            accept_language="fi_FI",
        )
        """
        _response = self._raw_client.get_personal_data_contexts(
            accept_language=accept_language, request_options=request_options
        )
        return _response.data


class AsyncFlagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFlagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFlagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFlagsClient
        """
        return self._raw_client

    async def get_personal_data_contexts(
        self, *, accept_language: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ContextsResponse:
        """
        The API exposes actions against contexts (logical groups) of personal data in the given system. The grouping should be based on usage, e.g., personal data used for marketing, personal data collected for usage analysis, or personal data processed for technical realisation of the service. The same personal data type (e.g., an email address) may be in several contexts; this does not imply it would be actually duplicated in the system, but it could be used in different contexts. Typically, a single context should not contain data that is processed under different basis of processing.

        Parameters
        ----------
        accept_language : typing.Optional[str]
            A list of accepted languages.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ContextsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.flags.get_personal_data_contexts(
                accept_language="fi_FI",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_personal_data_contexts(
            accept_language=accept_language, request_options=request_options
        )
        return _response.data
