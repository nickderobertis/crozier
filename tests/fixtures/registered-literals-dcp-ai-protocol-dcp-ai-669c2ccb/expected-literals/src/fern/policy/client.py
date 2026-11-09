

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPolicyClient, RawPolicyClient
from .types.get_policy_response import GetPolicyResponse
from .types.switch_policy_mode_request_mode import SwitchPolicyModeRequestMode
from .types.switch_policy_mode_response import SwitchPolicyModeResponse


OMIT = typing.cast(typing.Any, ...)


class PolicyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPolicyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPolicyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPolicyClient
        """
        return self._raw_client

    def get_policy(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetPolicyResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPolicyResponse
            Current verifier policy

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.policy.get_policy()
        """
        _response = self._raw_client.get_policy(request_options=request_options)
        return _response.data

    def switch_policy_mode(
        self, *, mode: SwitchPolicyModeRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> SwitchPolicyModeResponse:
        """
        Parameters
        ----------
        mode : SwitchPolicyModeRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SwitchPolicyModeResponse
            Mode switched

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.policy.switch_policy_mode(
            mode="hybrid_required",
        )
        """
        _response = self._raw_client.switch_policy_mode(mode=mode, request_options=request_options)
        return _response.data


class AsyncPolicyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPolicyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPolicyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPolicyClient
        """
        return self._raw_client

    async def get_policy(self, *, request_options: typing.Optional[RequestOptions] = None) -> GetPolicyResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPolicyResponse
            Current verifier policy

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policy.get_policy()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_policy(request_options=request_options)
        return _response.data

    async def switch_policy_mode(
        self, *, mode: SwitchPolicyModeRequestMode, request_options: typing.Optional[RequestOptions] = None
    ) -> SwitchPolicyModeResponse:
        """
        Parameters
        ----------
        mode : SwitchPolicyModeRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SwitchPolicyModeResponse
            Mode switched

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policy.switch_policy_mode(
                mode="hybrid_required",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.switch_policy_mode(mode=mode, request_options=request_options)
        return _response.data
