

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_package_type_i_dto_bundle import (
    ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle,
)
from ..types.update_system_models_package_type_i_dto_bundle_subscription_type import (
    UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType,
)
from .raw_client import AsyncRawPackagetypetobundlesClient, RawPackagetypetobundlesClient


OMIT = typing.cast(typing.Any, ...)


class PackagetypetobundlesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPackagetypetobundlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPackagetypetobundlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPackagetypetobundlesClient
        """
        return self._raw_client

    def get(
        self,
        *,
        bundle_id: typing.Optional[str] = None,
        package_type_id: typing.Optional[str] = None,
        package_version: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : typing.Optional[str]
            Optional. Filter by BundleID.

        package_type_id : typing.Optional[str]
            Optional. Filter by PackageTypeID.

        package_version : typing.Optional[int]
            Optional. Filter by PackageVersion.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagetypetobundles.get()
        """
        _response = self._raw_client.get(
            bundle_id=bundle_id,
            package_type_id=package_type_id,
            package_version=package_version,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    def post(
        self,
        *,
        bundle_id: str,
        package_type_id: str,
        package_version: int,
        priority: int,
        subscription_type: typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The bundle to include the package in.

        package_type_id : str
            The package type id of the package to include

        package_version : int
            The package version of the package to include

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        subscription_type : typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType]
            Optional. The type of subscription supported.  The default subscription type is Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagetypetobundles.post(
            bundle_id="BundleID",
            package_type_id="PackageTypeID",
            package_version=1,
            priority=1,
        )
        """
        _response = self._raw_client.post(
            bundle_id=bundle_id,
            package_type_id=package_type_id,
            package_version=package_version,
            priority=priority,
            subscription_type=subscription_type,
            request_options=request_options,
        )
        return _response.data

    def put(
        self,
        *,
        bundle_id: str,
        package_type_id: str,
        package_version: int,
        priority: int,
        subscription_type: typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The bundle to include the package in.

        package_type_id : str
            The package type id of the package to include

        package_version : int
            The package version of the package to include

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        subscription_type : typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType]
            Optional. The type of subscription supported.  The default subscription type is Required.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagetypetobundles.put(
            bundle_id="BundleID",
            package_type_id="PackageTypeID",
            package_version=1,
            priority=1,
        )
        """
        _response = self._raw_client.put(
            bundle_id=bundle_id,
            package_type_id=package_type_id,
            package_version=package_version,
            priority=priority,
            subscription_type=subscription_type,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self, *, bundle_id: str, package_type_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The BundleID

        package_type_id : str
            The PackageTypeID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagetypetobundles.delete(
            bundle_id="BundleID",
            package_type_id="PackageTypeID",
        )
        """
        _response = self._raw_client.delete(
            bundle_id=bundle_id, package_type_id=package_type_id, request_options=request_options
        )
        return _response.data


class AsyncPackagetypetobundlesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPackagetypetobundlesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPackagetypetobundlesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPackagetypetobundlesClient
        """
        return self._raw_client

    async def get(
        self,
        *,
        bundle_id: typing.Optional[str] = None,
        package_type_id: typing.Optional[str] = None,
        package_version: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : typing.Optional[str]
            Optional. Filter by BundleID.

        package_type_id : typing.Optional[str]
            Optional. Filter by PackageTypeID.

        package_version : typing.Optional[int]
            Optional. Filter by PackageVersion.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsPackageTypeIDtoBundle
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packagetypetobundles.get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            bundle_id=bundle_id,
            package_type_id=package_type_id,
            package_version=package_version,
            limit=limit,
            offset=offset,
            request_options=request_options,
        )
        return _response.data

    async def post(
        self,
        *,
        bundle_id: str,
        package_type_id: str,
        package_version: int,
        priority: int,
        subscription_type: typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The bundle to include the package in.

        package_type_id : str
            The package type id of the package to include

        package_version : int
            The package version of the package to include

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        subscription_type : typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType]
            Optional. The type of subscription supported.  The default subscription type is Required.

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
            await client.packagetypetobundles.post(
                bundle_id="BundleID",
                package_type_id="PackageTypeID",
                package_version=1,
                priority=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post(
            bundle_id=bundle_id,
            package_type_id=package_type_id,
            package_version=package_version,
            priority=priority,
            subscription_type=subscription_type,
            request_options=request_options,
        )
        return _response.data

    async def put(
        self,
        *,
        bundle_id: str,
        package_type_id: str,
        package_version: int,
        priority: int,
        subscription_type: typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The bundle to include the package in.

        package_type_id : str
            The package type id of the package to include

        package_version : int
            The package version of the package to include

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        subscription_type : typing.Optional[UpdateSystemModelsPackageTypeIDtoBundleSubscriptionType]
            Optional. The type of subscription supported.  The default subscription type is Required.

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
            await client.packagetypetobundles.put(
                bundle_id="BundleID",
                package_type_id="PackageTypeID",
                package_version=1,
                priority=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(
            bundle_id=bundle_id,
            package_type_id=package_type_id,
            package_version=package_version,
            priority=priority,
            subscription_type=subscription_type,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, *, bundle_id: str, package_type_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        bundle_id : str
            The BundleID

        package_type_id : str
            The PackageTypeID

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
            await client.packagetypetobundles.delete(
                bundle_id="BundleID",
                package_type_id="PackageTypeID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(
            bundle_id=bundle_id, package_type_id=package_type_id, request_options=request_options
        )
        return _response.data
