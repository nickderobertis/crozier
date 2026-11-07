

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.account_response import AccountResponse
from .raw_client import AsyncRawApplicationClient, RawApplicationClient
from .types.link_application_request_provider import LinkApplicationRequestProvider
from .types.unli_without_applicationnk_application_request_provider import (
    UnliWithoutApplicationnkApplicationRequestProvider,
)


OMIT = typing.cast(typing.Any, ...)


class ApplicationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawApplicationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawApplicationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawApplicationClient
        """
        return self._raw_client

    def link_application(
        self,
        provider: LinkApplicationRequestProvider,
        external_id: str,
        *,
        application: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountResponse:
        """
        Parameters
        ----------
        provider : LinkApplicationRequestProvider
            Provider of the account you want to assign an application to

        external_id : str
            External id of the account you want to assign an application to. This is channel dependent. For Facebook it will be your Facebook Page ID, for Viber your Viber Service Message ID and for WhatsApp your WhatsApp number.

        application : str
            There is just one application allowed per an account. The application type must be type "messages". For more information please see [Application API Spec](https://developer.nexmo.com/api/application.v2)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            OK.

        Examples
        --------
        from fern.application import LinkApplicationRequestProvider

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.application.link_application(
            provider=LinkApplicationRequestProvider.MESSENGER,
            external_id="external_id",
            application="applicationId",
        )
        """
        _response = self._raw_client.link_application(
            provider, external_id, application=application, request_options=request_options
        )
        return _response.data

    def unli_without_applicationnk_application(
        self,
        provider: UnliWithoutApplicationnkApplicationRequestProvider,
        external_id: str,
        application_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        provider : UnliWithoutApplicationnkApplicationRequestProvider
            Provider of the account you want to unlink an application from

        external_id : str
            External id of the account you want to unlink an application from

        application_id : str
            Id of the application you want to unlink

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.application import UnliWithoutApplicationnkApplicationRequestProvider

        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.application.unli_without_applicationnk_application(
            provider=UnliWithoutApplicationnkApplicationRequestProvider.MESSENGER,
            external_id="external_id",
            application_id="application_id",
        )
        """
        _response = self._raw_client.unli_without_applicationnk_application(
            provider, external_id, application_id, request_options=request_options
        )
        return _response.data


class AsyncApplicationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawApplicationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawApplicationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawApplicationClient
        """
        return self._raw_client

    async def link_application(
        self,
        provider: LinkApplicationRequestProvider,
        external_id: str,
        *,
        application: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AccountResponse:
        """
        Parameters
        ----------
        provider : LinkApplicationRequestProvider
            Provider of the account you want to assign an application to

        external_id : str
            External id of the account you want to assign an application to. This is channel dependent. For Facebook it will be your Facebook Page ID, for Viber your Viber Service Message ID and for WhatsApp your WhatsApp number.

        application : str
            There is just one application allowed per an account. The application type must be type "messages". For more information please see [Application API Spec](https://developer.nexmo.com/api/application.v2)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AccountResponse
            OK.

        Examples
        --------
        import asyncio

        from fern.application import LinkApplicationRequestProvider

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.application.link_application(
                provider=LinkApplicationRequestProvider.MESSENGER,
                external_id="external_id",
                application="applicationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.link_application(
            provider, external_id, application=application, request_options=request_options
        )
        return _response.data

    async def unli_without_applicationnk_application(
        self,
        provider: UnliWithoutApplicationnkApplicationRequestProvider,
        external_id: str,
        application_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        provider : UnliWithoutApplicationnkApplicationRequestProvider
            Provider of the account you want to unlink an application from

        external_id : str
            External id of the account you want to unlink an application from

        application_id : str
            Id of the application you want to unlink

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.application import UnliWithoutApplicationnkApplicationRequestProvider

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.application.unli_without_applicationnk_application(
                provider=UnliWithoutApplicationnkApplicationRequestProvider.MESSENGER,
                external_id="external_id",
                application_id="application_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.unli_without_applicationnk_application(
            provider, external_id, application_id, request_options=request_options
        )
        return _response.data
