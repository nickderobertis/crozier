

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.prompt import Prompt
from .raw_client import AsyncRawPromptversionClient, RawPromptversionClient


OMIT = typing.cast(typing.Any, ...)


class PromptversionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPromptversionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPromptversionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPromptversionClient
        """
        return self._raw_client

    def update(
        self,
        name: str,
        version: int,
        *,
        new_labels: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Update labels for a specific prompt version

        Parameters
        ----------
        name : str
            The name of the prompt

        version : int
            Version of the prompt to update

        new_labels : typing.Sequence[str]
            New labels for the prompt version. Labels are unique across versions. The "latest" label is reserved and managed by Langfuse.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.promptversion.update(
            name="name",
            version=1,
            new_labels=["newLabels"],
        )
        """
        _response = self._raw_client.update(name, version, new_labels=new_labels, request_options=request_options)
        return _response.data


class AsyncPromptversionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPromptversionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPromptversionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPromptversionClient
        """
        return self._raw_client

    async def update(
        self,
        name: str,
        version: int,
        *,
        new_labels: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Prompt:
        """
        Update labels for a specific prompt version

        Parameters
        ----------
        name : str
            The name of the prompt

        version : int
            Version of the prompt to update

        new_labels : typing.Sequence[str]
            New labels for the prompt version. Labels are unique across versions. The "latest" label is reserved and managed by Langfuse.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Prompt


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.promptversion.update(
                name="name",
                version=1,
                new_labels=["newLabels"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update(name, version, new_labels=new_labels, request_options=request_options)
        return _response.data
