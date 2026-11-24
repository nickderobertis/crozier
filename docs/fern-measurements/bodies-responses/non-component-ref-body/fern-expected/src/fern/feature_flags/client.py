

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.feature_flag import FeatureFlag
from .raw_client import AsyncRawFeatureFlagsClient, RawFeatureFlagsClient


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

    def list_feature_flags(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FeatureFlag]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeatureFlag]
            The flags.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.feature_flags.list_feature_flags()
        """
        _response = self._raw_client.list_feature_flags(request_options=request_options)
        return _response.data

    def create_feature_flag(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> FeatureFlag:
        """
        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureFlag
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.feature_flags.create_feature_flag(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_feature_flag(request=request, request_options=request_options)
        return _response.data

    def update_feature_flag(
        self, flag_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> FeatureFlag:
        """
        Parameters
        ----------
        flag_id : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureFlag
            Updated.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.feature_flags.update_feature_flag(
            flag_id="flagId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_feature_flag(flag_id, request=request, request_options=request_options)
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

    async def list_feature_flags(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[FeatureFlag]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[FeatureFlag]
            The flags.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.feature_flags.list_feature_flags()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_feature_flags(request_options=request_options)
        return _response.data

    async def create_feature_flag(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> FeatureFlag:
        """
        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureFlag
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.feature_flags.create_feature_flag(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_feature_flag(request=request, request_options=request_options)
        return _response.data

    async def update_feature_flag(
        self, flag_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> FeatureFlag:
        """
        Parameters
        ----------
        flag_id : str

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FeatureFlag
            Updated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.feature_flags.update_feature_flag(
                flag_id="flagId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_feature_flag(
            flag_id, request=request, request_options=request_options
        )
        return _response.data
