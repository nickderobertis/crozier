

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_available_skills_response import ListAvailableSkillsResponse
from .raw_client import AsyncRawSkillsClient, RawSkillsClient


class SkillsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSkillsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSkillsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSkillsClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListAvailableSkillsResponse:
        """
        Configured skills as a slim name/description list for the composer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAvailableSkillsResponse
            All configured skills (chat projection).

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.skills.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncSkillsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSkillsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSkillsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSkillsClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListAvailableSkillsResponse:
        """
        Configured skills as a slim name/description list for the composer.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAvailableSkillsResponse
            All configured skills (chat projection).

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.skills.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
