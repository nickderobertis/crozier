

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.refresh_profile_telemetry_properties_response import RefreshProfileTelemetryPropertiesResponse
from .raw_client import AsyncRawPrivacyClient, RawPrivacyClient


OMIT = typing.cast(typing.Any, ...)


class PrivacyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrivacyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrivacyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrivacyClient
        """
        return self._raw_client

    def post_api_v1geneva_actions_privacy_refresh_profile_telemetry_properties(
        self,
        *,
        partner: typing.Optional[str] = OMIT,
        tenant_id: typing.Optional[str] = OMIT,
        user_ids: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefreshProfileTelemetryPropertiesResponse:
        """
        Parameters
        ----------
        partner : typing.Optional[str]

        tenant_id : typing.Optional[str]

        user_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefreshProfileTelemetryPropertiesResponse
            Success

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.privacy.post_api_v1geneva_actions_privacy_refresh_profile_telemetry_properties()
        """
        _response = self._raw_client.post_api_v1geneva_actions_privacy_refresh_profile_telemetry_properties(
            partner=partner, tenant_id=tenant_id, user_ids=user_ids, request_options=request_options
        )
        return _response.data


class AsyncPrivacyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrivacyClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrivacyClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrivacyClient
        """
        return self._raw_client

    async def post_api_v1geneva_actions_privacy_refresh_profile_telemetry_properties(
        self,
        *,
        partner: typing.Optional[str] = OMIT,
        tenant_id: typing.Optional[str] = OMIT,
        user_ids: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RefreshProfileTelemetryPropertiesResponse:
        """
        Parameters
        ----------
        partner : typing.Optional[str]

        tenant_id : typing.Optional[str]

        user_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RefreshProfileTelemetryPropertiesResponse
            Success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.privacy.post_api_v1geneva_actions_privacy_refresh_profile_telemetry_properties()


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1geneva_actions_privacy_refresh_profile_telemetry_properties(
            partner=partner, tenant_id=tenant_id, user_ids=user_ids, request_options=request_options
        )
        return _response.data
