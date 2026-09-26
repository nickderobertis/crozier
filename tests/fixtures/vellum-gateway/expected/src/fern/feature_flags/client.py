

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFeatureFlagsClient, RawFeatureFlagsClient
from .types.feature_flags_get_response import FeatureFlagsGetResponse
from .types.feature_flags_patch_request_enabled import FeatureFlagsPatchRequestEnabled
from .types.feature_flags_patch_response import FeatureFlagsPatchResponse


OMIT = typing.cast(typing.Any, ...)


class FeatureFlagsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFeatureFlagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFeatureFlagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFeatureFlagsClient
        """
        return self._raw_client

    def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> FeatureFlagsGetResponse:
        """
        Returns all feature flags with their current values.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureFlagsGetResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.feature_flags.get()
        """
        _response = self._raw_client.get(request_options=request_options)
        return _response.data

    def patch(
        self,
        flag_key: str,
        *,
        enabled: FeatureFlagsPatchRequestEnabled,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeatureFlagsPatchResponse:
        """
        Set the enabled state of a single feature flag.

        Parameters
        ----------
        flag_key : str
            The kebab-case flag identifier

        enabled : FeatureFlagsPatchRequestEnabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureFlagsPatchResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.feature_flags.patch(
            flag_key="flag_key",
            enabled=True,
        )
        """
        _response = self._raw_client.patch(flag_key, enabled=enabled, request_options=request_options)
        return _response.data


class AsyncFeatureFlagsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFeatureFlagsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFeatureFlagsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFeatureFlagsClient
        """
        return self._raw_client

    async def get(self, *, request_options: typing.Optional[RequestOptions] = None) -> FeatureFlagsGetResponse:
        """
        Returns all feature flags with their current values.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureFlagsGetResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.feature_flags.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(request_options=request_options)
        return _response.data

    async def patch(
        self,
        flag_key: str,
        *,
        enabled: FeatureFlagsPatchRequestEnabled,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FeatureFlagsPatchResponse:
        """
        Set the enabled state of a single feature flag.

        Parameters
        ----------
        flag_key : str
            The kebab-case flag identifier

        enabled : FeatureFlagsPatchRequestEnabled

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureFlagsPatchResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.feature_flags.patch(
                flag_key="flag_key",
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch(flag_key, enabled=enabled, request_options=request_options)
        return _response.data
