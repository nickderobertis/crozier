

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAppsClient, RawAppsClient


class AppsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAppsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAppsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAppsClient
        """
        return self._raw_client

    def app_list(self, *, sdpath: str, request_options: typing.Optional[RequestOptions] = None) -> typing.List[str]:
        """
        <ul>
        <li>Retrieve the list of the registered applications in the seismic store.</li>
        <li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store tenant path, sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Retrieved a list of all the registered applications successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.apps.app_list(
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.app_list(sdpath=sdpath, request_options=request_options)
        return _response.data

    def app_register(self, *, email: str, sdpath: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        <ul><li>Register a new application in the seismic store.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        email : str
            Service account email of the application.

        sdpath : str
            Seismic store tenant path, sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.apps.app_register(
            email="email",
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.app_register(email=email, sdpath=sdpath, request_options=request_options)
        return _response.data

    def trustedapp_list(
        self, *, sdpath: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        <ul>
        <li>Return the list of the trusted application in seismic store tenant.
        </li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store tenant path in the format sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Retrieved the list of all the trusted applications in the tenant.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.apps.trustedapp_list(
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.trustedapp_list(sdpath=sdpath, request_options=request_options)
        return _response.data

    def trustedapp_register(
        self, *, email: str, sdpath: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        <ul>
        <li>Set a registered application as a trusted application in the seismic store.</li>
        <li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        email : str
            Service account email of the application.

        sdpath : str
            Seismic store tenant path, sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.apps.trustedapp_register(
            email="email",
            sdpath="sdpath",
        )
        """
        _response = self._raw_client.trustedapp_register(email=email, sdpath=sdpath, request_options=request_options)
        return _response.data


class AsyncAppsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAppsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAppsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAppsClient
        """
        return self._raw_client

    async def app_list(
        self, *, sdpath: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        <ul>
        <li>Retrieve the list of the registered applications in the seismic store.</li>
        <li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store tenant path, sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Retrieved a list of all the registered applications successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.apps.app_list(
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_list(sdpath=sdpath, request_options=request_options)
        return _response.data

    async def app_register(
        self, *, email: str, sdpath: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        <ul><li>Register a new application in the seismic store.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        email : str
            Service account email of the application.

        sdpath : str
            Seismic store tenant path, sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.apps.app_register(
                email="email",
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.app_register(email=email, sdpath=sdpath, request_options=request_options)
        return _response.data

    async def trustedapp_list(
        self, *, sdpath: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        <ul>
        <li>Return the list of the trusted application in seismic store tenant.
        </li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        sdpath : str
            Seismic store tenant path in the format sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            Retrieved the list of all the trusted applications in the tenant.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.apps.trustedapp_list(
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trustedapp_list(sdpath=sdpath, request_options=request_options)
        return _response.data

    async def trustedapp_register(
        self, *, email: str, sdpath: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        <ul>
        <li>Set a registered application as a trusted application in the seismic store.</li>
        <li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        email : str
            Service account email of the application.

        sdpath : str
            Seismic store tenant path, sd://tenant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.apps.trustedapp_register(
                email="email",
                sdpath="sdpath",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.trustedapp_register(
            email=email, sdpath=sdpath, request_options=request_options
        )
        return _response.data
