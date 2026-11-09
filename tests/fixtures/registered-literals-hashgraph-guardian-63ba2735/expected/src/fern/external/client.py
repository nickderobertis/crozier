

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawExternalClient, RawExternalClient


OMIT = typing.cast(typing.Any, ...)


class ExternalClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawExternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawExternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawExternalClient
        """
        return self._raw_client

    def sends_data_from_an_external_source(
        self,
        *,
        owner: str,
        policy_tag: str,
        document: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sends data from an external source.

        Parameters
        ----------
        owner : str

        policy_tag : str

        document : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.external.sends_data_from_an_external_source(
            owner="owner",
            policy_tag="policyTag",
            document={"key": "value"},
        )
        """
        _response = self._raw_client.sends_data_from_an_external_source(
            owner=owner, policy_tag=policy_tag, document=document, request_options=request_options
        )
        return _response.data


class AsyncExternalClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawExternalClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawExternalClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawExternalClient
        """
        return self._raw_client

    async def sends_data_from_an_external_source(
        self,
        *,
        owner: str,
        policy_tag: str,
        document: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sends data from an external source.

        Parameters
        ----------
        owner : str

        policy_tag : str

        document : typing.Dict[str, typing.Any]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.external.sends_data_from_an_external_source(
                owner="owner",
                policy_tag="policyTag",
                document={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sends_data_from_an_external_source(
            owner=owner, policy_tag=policy_tag, document=document, request_options=request_options
        )
        return _response.data
