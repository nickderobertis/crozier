

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_app_password_get_app_password200response import CoreAppPasswordGetAppPassword200Response
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from .raw_client import AsyncRawCoreAppPasswordClient, RawCoreAppPasswordClient


class CoreAppPasswordClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreAppPasswordClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreAppPasswordClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreAppPasswordClient
        """
        return self._raw_client

    def get_app_password(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreAppPasswordGetAppPassword200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreAppPasswordGetAppPassword200Response
            App password returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_app_password.get_app_password()
        """
        _response = self._raw_client.get_app_password(request_options=request_options)
        return _response.data

    def rotate_app_password(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreAppPasswordGetAppPassword200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreAppPasswordGetAppPassword200Response
            App password returned

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_app_password.rotate_app_password()
        """
        _response = self._raw_client.rotate_app_password(request_options=request_options)
        return _response.data

    def delete_app_password(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            App password deleted successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_app_password.delete_app_password()
        """
        _response = self._raw_client.delete_app_password(request_options=request_options)
        return _response.data


class AsyncCoreAppPasswordClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreAppPasswordClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreAppPasswordClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreAppPasswordClient
        """
        return self._raw_client

    async def get_app_password(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreAppPasswordGetAppPassword200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreAppPasswordGetAppPassword200Response
            App password returned

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
            await client.core_app_password.get_app_password()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_app_password(request_options=request_options)
        return _response.data

    async def rotate_app_password(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreAppPasswordGetAppPassword200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreAppPasswordGetAppPassword200Response
            App password returned

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
            await client.core_app_password.rotate_app_password()


        asyncio.run(main())
        """
        _response = await self._raw_client.rotate_app_password(request_options=request_options)
        return _response.data

    async def delete_app_password(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWhatsNewDismiss200Response:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWhatsNewDismiss200Response
            App password deleted successfully

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
            await client.core_app_password.delete_app_password()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_app_password(request_options=request_options)
        return _response.data
