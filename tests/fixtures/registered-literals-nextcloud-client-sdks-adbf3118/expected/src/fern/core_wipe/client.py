

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.core_wipe_check_wipe200response import CoreWipeCheckWipe200Response
from .raw_client import AsyncRawCoreWipeClient, RawCoreWipeClient


class CoreWipeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCoreWipeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCoreWipeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCoreWipeClient
        """
        return self._raw_client

    def check_wipe(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWipeCheckWipe200Response:
        """
        Parameters
        ----------
        token : str
            App password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWipeCheckWipe200Response
            Device should be wiped

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_wipe.check_wipe(
            token="token",
        )
        """
        _response = self._raw_client.check_wipe(token=token, request_options=request_options)
        return _response.data

    def wipe_done(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        token : str
            App password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Wipe finished successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            ocs_api_request="YOUR_OCS_API_REQUEST",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.core_wipe.wipe_done(
            token="token",
        )
        """
        _response = self._raw_client.wipe_done(token=token, request_options=request_options)
        return _response.data


class AsyncCoreWipeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCoreWipeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCoreWipeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCoreWipeClient
        """
        return self._raw_client

    async def check_wipe(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> CoreWipeCheckWipe200Response:
        """
        Parameters
        ----------
        token : str
            App password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CoreWipeCheckWipe200Response
            Device should be wiped

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
            await client.core_wipe.check_wipe(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_wipe(token=token, request_options=request_options)
        return _response.data

    async def wipe_done(
        self, *, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        token : str
            App password

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Wipe finished successfully

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
            await client.core_wipe.wipe_done(
                token="token",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.wipe_done(token=token, request_options=request_options)
        return _response.data
