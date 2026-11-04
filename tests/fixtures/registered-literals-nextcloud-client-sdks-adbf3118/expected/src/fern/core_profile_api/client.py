

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from .raw_client import AsyncRawCoreProfileApiClient, RawCoreProfileApiClient


class CoreProfileApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreProfileApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreProfileApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreProfileApiClient
        """
        return self._raw_client

    def set_visibility(
        self,
        target_user_id: str,
        *,
        param_id: str,
        visibility: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        target_user_id : str
            ID of the user

        param_id : str
            ID of the parameter

        visibility : str
            New visibility

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Visibility updated successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_profile_api.set_visibility(
            target_user_id="targetUserId",
            param_id="paramId",
            visibility="visibility",
        )
        """
        _response = self._raw_client.set_visibility(
            target_user_id, param_id=param_id, visibility=visibility, request_options=request_options
        )
        return _response.data


class AsyncCoreProfileApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreProfileApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreProfileApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreProfileApiClient
        """
        return self._raw_client

    async def set_visibility(
        self,
        target_user_id: str,
        *,
        param_id: str,
        visibility: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        target_user_id : str
            ID of the user

        param_id : str
            ID of the parameter

        visibility : str
            New visibility

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            Visibility updated successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.core_profile_api.set_visibility(
                target_user_id="targetUserId",
                param_id="paramId",
                visibility="visibility",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_visibility(
            target_user_id, param_id=param_id, visibility=visibility, request_options=request_options
        )
        return _response.data
