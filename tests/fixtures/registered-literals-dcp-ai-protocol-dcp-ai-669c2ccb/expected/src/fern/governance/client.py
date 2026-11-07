

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.governance_key_set import GovernanceKeySet
from .raw_client import AsyncRawGovernanceClient, RawGovernanceClient
from .types.register_governance_response import RegisterGovernanceResponse


OMIT = typing.cast(typing.Any, ...)


class GovernanceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGovernanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGovernanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGovernanceClient
        """
        return self._raw_client

    def get_governance_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> GovernanceKeySet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GovernanceKeySet
            Governance key set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.governance.get_governance_keys()
        """
        _response = self._raw_client.get_governance_keys(request_options=request_options)
        return _response.data

    def register_governance(
        self, *, governance_key_set: GovernanceKeySet, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterGovernanceResponse:
        """
        Parameters
        ----------
        governance_key_set : GovernanceKeySet

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterGovernanceResponse
            Governance key set registered

        Examples
        --------
        from fern import FernApi, GovernanceKeySet, KeyEntryV2

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.governance.register_governance(
            governance_key_set=GovernanceKeySet(
                governance_id="governance_id",
                keys=[KeyEntryV2()],
                threshold=1,
            ),
        )
        """
        _response = self._raw_client.register_governance(
            governance_key_set=governance_key_set, request_options=request_options
        )
        return _response.data


class AsyncGovernanceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGovernanceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGovernanceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGovernanceClient
        """
        return self._raw_client

    async def get_governance_keys(self, *, request_options: typing.Optional[RequestOptions] = None) -> GovernanceKeySet:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GovernanceKeySet
            Governance key set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.governance.get_governance_keys()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_governance_keys(request_options=request_options)
        return _response.data

    async def register_governance(
        self, *, governance_key_set: GovernanceKeySet, request_options: typing.Optional[RequestOptions] = None
    ) -> RegisterGovernanceResponse:
        """
        Parameters
        ----------
        governance_key_set : GovernanceKeySet

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RegisterGovernanceResponse
            Governance key set registered

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, GovernanceKeySet, KeyEntryV2

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.governance.register_governance(
                governance_key_set=GovernanceKeySet(
                    governance_id="governance_id",
                    keys=[KeyEntryV2()],
                    threshold=1,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.register_governance(
            governance_key_set=governance_key_set, request_options=request_options
        )
        return _response.data
