

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawTargetsClient, RawTargetsClient
from .types.list_targets_request_kinds_item import ListTargetsRequestKindsItem


class TargetsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTargetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTargetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTargetsClient
        """
        return self._raw_client

    def list_targets(
        self,
        *,
        kinds: typing.Optional[
            typing.Union[ListTargetsRequestKindsItem, typing.Sequence[ListTargetsRequestKindsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        kinds : typing.Optional[typing.Union[ListTargetsRequestKindsItem, typing.Sequence[ListTargetsRequestKindsItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Targets of the given kinds.

        Examples
        --------
        from fern.targets import ListTargetsRequestKindsItemZero

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.targets.list_targets(
            kinds=[ListTargetsRequestKindsItemZero.NEBULA],
        )
        """
        _response = self._raw_client.list_targets(kinds=kinds, request_options=request_options)
        return _response.data


class AsyncTargetsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTargetsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTargetsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTargetsClient
        """
        return self._raw_client

    async def list_targets(
        self,
        *,
        kinds: typing.Optional[
            typing.Union[ListTargetsRequestKindsItem, typing.Sequence[ListTargetsRequestKindsItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[str]:
        """
        Parameters
        ----------
        kinds : typing.Optional[typing.Union[ListTargetsRequestKindsItem, typing.Sequence[ListTargetsRequestKindsItem]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Targets of the given kinds.

        Examples
        --------
        import asyncio

        from fern.targets import ListTargetsRequestKindsItemZero

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.targets.list_targets(
                kinds=[ListTargetsRequestKindsItemZero.NEBULA],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_targets(kinds=kinds, request_options=request_options)
        return _response.data
