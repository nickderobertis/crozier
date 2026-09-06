

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.update_system_models_category import UpdateSystemModelsCategory
from ..types.update_system_models_package_report import UpdateSystemModelsPackageReport
from .raw_client import AsyncRawPackagereportsClient, RawPackagereportsClient


OMIT = typing.cast(typing.Any, ...)


class PackagereportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPackagereportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPackagereportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPackagereportsClient
        """
        return self._raw_client

    def default(
        self,
        client_id: str,
        *,
        categories: typing.Optional[typing.Sequence[UpdateSystemModelsCategory]] = OMIT,
        package_description: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        categories : typing.Optional[typing.Sequence[UpdateSystemModelsCategory]]
            The package report's categories.

        package_description : typing.Optional[str]
            Read Only. The package description

        package_id : typing.Optional[str]
            The PackageID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagereports.default(
            client_id="ClientID",
        )
        """
        _response = self._raw_client.default(
            client_id,
            categories=categories,
            package_description=package_description,
            package_id=package_id,
            request_options=request_options,
        )
        return _response.data

    def batch(
        self,
        client_id: str,
        *,
        request: typing.Sequence[UpdateSystemModelsPackageReport],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        request : typing.Sequence[UpdateSystemModelsPackageReport]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, UpdateSystemModelsPackageReport

        client = FernApi()
        client.packagereports.batch(
            client_id="ClientID",
            request=[UpdateSystemModelsPackageReport()],
        )
        """
        _response = self._raw_client.batch(client_id, request=request, request_options=request_options)
        return _response.data


class AsyncPackagereportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPackagereportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPackagereportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPackagereportsClient
        """
        return self._raw_client

    async def default(
        self,
        client_id: str,
        *,
        categories: typing.Optional[typing.Sequence[UpdateSystemModelsCategory]] = OMIT,
        package_description: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        categories : typing.Optional[typing.Sequence[UpdateSystemModelsCategory]]
            The package report's categories.

        package_description : typing.Optional[str]
            Read Only. The package description

        package_id : typing.Optional[str]
            The PackageID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packagereports.default(
                client_id="ClientID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.default(
            client_id,
            categories=categories,
            package_description=package_description,
            package_id=package_id,
            request_options=request_options,
        )
        return _response.data

    async def batch(
        self,
        client_id: str,
        *,
        request: typing.Sequence[UpdateSystemModelsPackageReport],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The Client ID

        request : typing.Sequence[UpdateSystemModelsPackageReport]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, UpdateSystemModelsPackageReport

        client = AsyncFernApi()


        async def main() -> None:
            await client.packagereports.batch(
                client_id="ClientID",
                request=[UpdateSystemModelsPackageReport()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch(client_id, request=request, request_options=request_options)
        return _response.data
