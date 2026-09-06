

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_priority_package import (
    ApiPagedResponseUpdateSystemModelsPriorityPackage,
)
from ..types.update_system_models_priority_package import UpdateSystemModelsPriorityPackage
from .raw_client import AsyncRawPrioritypackagesClient, RawPrioritypackagesClient
from .types.priority_packages_get_priority_packages_request_status import (
    PriorityPackagesGetPriorityPackagesRequestStatus,
)


OMIT = typing.cast(typing.Any, ...)


class PrioritypackagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPrioritypackagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPrioritypackagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPrioritypackagesClient
        """
        return self._raw_client

    def getprioritypackages(
        self,
        *,
        client_id: typing.Optional[str] = None,
        status: typing.Optional[PriorityPackagesGetPriorityPackagesRequestStatus] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsPriorityPackage:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter priority packages by ClientID.

        status : typing.Optional[PriorityPackagesGetPriorityPackagesRequestStatus]
            Optional. Filter returned packages by status. By default only active packages will be returned.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsPriorityPackage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.prioritypackages.getprioritypackages()
        """
        _response = self._raw_client.getprioritypackages(
            client_id=client_id, status=status, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def postprioritypackages(
        self,
        *,
        client_id: str,
        package_id: str,
        autorun: typing.Optional[bool] = OMIT,
        crc: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        priority_package_id: typing.Optional[str] = OMIT,
        release_date: typing.Optional[dt.datetime] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        time_stamp: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ID of the client to receive the priority package

        package_id : str
            The ID of the package to push as a priority package.

        autorun : typing.Optional[bool]
            Read Only. From the package specified by package ID.
                        Value is true if package should run automatically. Default value is false.

        crc : typing.Optional[str]
            Read Only. From the package specified by package ID.

        description : typing.Optional[str]
            Read Only. From the package specified by package ID.

        notes : typing.Optional[str]
            Read Only. From the package specified by package ID.

        package_type_id : typing.Optional[str]
            Read Only. From the package specified by package ID.

        previous_version : typing.Optional[int]
            Read Only. From the package specified by package ID.

        priority_package_id : typing.Optional[str]
            Read Only. The ID of the priority package.

        release_date : typing.Optional[dt.datetime]
            Read Only. From the package specified by package ID.
                        The date the package was released

        released : typing.Optional[bool]
            Read Only. From the package specified by package ID.

        remove_on_success : typing.Optional[bool]
            Read Only. From the package specified by package ID.

        size : typing.Optional[int]
            Read Only. From the package specified by package ID.

        switches : typing.Optional[str]
            The command line arguments for the priority package.  Default value is an empty string.

        time_stamp : typing.Optional[dt.datetime]
            Read Only. The timestamp of the priority package.

        url : typing.Optional[str]
            Read Only. From the package specified by package ID.

        version : typing.Optional[int]
            Read Only. From the package specified by package ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.prioritypackages.postprioritypackages(
            client_id="ClientID",
            package_id="PackageID",
        )
        """
        _response = self._raw_client.postprioritypackages(
            client_id=client_id,
            package_id=package_id,
            autorun=autorun,
            crc=crc,
            description=description,
            notes=notes,
            package_type_id=package_type_id,
            previous_version=previous_version,
            priority_package_id=priority_package_id,
            release_date=release_date,
            released=released,
            remove_on_success=remove_on_success,
            size=size,
            switches=switches,
            time_stamp=time_stamp,
            url=url,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def getprioritypackage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsPriorityPackage:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Priority Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsPriorityPackage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.prioritypackages.getprioritypackage(
            id="ID",
        )
        """
        _response = self._raw_client.getprioritypackage(id, request_options=request_options)
        return _response.data

    def deleteprioritypackages(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Priority Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.prioritypackages.deleteprioritypackages(
            id="ID",
        )
        """
        _response = self._raw_client.deleteprioritypackages(id, request_options=request_options)
        return _response.data


class AsyncPrioritypackagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPrioritypackagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPrioritypackagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPrioritypackagesClient
        """
        return self._raw_client

    async def getprioritypackages(
        self,
        *,
        client_id: typing.Optional[str] = None,
        status: typing.Optional[PriorityPackagesGetPriorityPackagesRequestStatus] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsPriorityPackage:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : typing.Optional[str]
            Optional. Filter priority packages by ClientID.

        status : typing.Optional[PriorityPackagesGetPriorityPackagesRequestStatus]
            Optional. Filter returned packages by status. By default only active packages will be returned.

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsPriorityPackage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.prioritypackages.getprioritypackages()


        asyncio.run(main())
        """
        _response = await self._raw_client.getprioritypackages(
            client_id=client_id, status=status, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def postprioritypackages(
        self,
        *,
        client_id: str,
        package_id: str,
        autorun: typing.Optional[bool] = OMIT,
        crc: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        priority_package_id: typing.Optional[str] = OMIT,
        release_date: typing.Optional[dt.datetime] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        time_stamp: typing.Optional[dt.datetime] = OMIT,
        url: typing.Optional[str] = OMIT,
        version: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        client_id : str
            The ID of the client to receive the priority package

        package_id : str
            The ID of the package to push as a priority package.

        autorun : typing.Optional[bool]
            Read Only. From the package specified by package ID.
                        Value is true if package should run automatically. Default value is false.

        crc : typing.Optional[str]
            Read Only. From the package specified by package ID.

        description : typing.Optional[str]
            Read Only. From the package specified by package ID.

        notes : typing.Optional[str]
            Read Only. From the package specified by package ID.

        package_type_id : typing.Optional[str]
            Read Only. From the package specified by package ID.

        previous_version : typing.Optional[int]
            Read Only. From the package specified by package ID.

        priority_package_id : typing.Optional[str]
            Read Only. The ID of the priority package.

        release_date : typing.Optional[dt.datetime]
            Read Only. From the package specified by package ID.
                        The date the package was released

        released : typing.Optional[bool]
            Read Only. From the package specified by package ID.

        remove_on_success : typing.Optional[bool]
            Read Only. From the package specified by package ID.

        size : typing.Optional[int]
            Read Only. From the package specified by package ID.

        switches : typing.Optional[str]
            The command line arguments for the priority package.  Default value is an empty string.

        time_stamp : typing.Optional[dt.datetime]
            Read Only. The timestamp of the priority package.

        url : typing.Optional[str]
            Read Only. From the package specified by package ID.

        version : typing.Optional[int]
            Read Only. From the package specified by package ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.prioritypackages.postprioritypackages(
                client_id="ClientID",
                package_id="PackageID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postprioritypackages(
            client_id=client_id,
            package_id=package_id,
            autorun=autorun,
            crc=crc,
            description=description,
            notes=notes,
            package_type_id=package_type_id,
            previous_version=previous_version,
            priority_package_id=priority_package_id,
            release_date=release_date,
            released=released,
            remove_on_success=remove_on_success,
            size=size,
            switches=switches,
            time_stamp=time_stamp,
            url=url,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def getprioritypackage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsPriorityPackage:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Priority Package ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsPriorityPackage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.prioritypackages.getprioritypackage(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getprioritypackage(id, request_options=request_options)
        return _response.data

    async def deleteprioritypackages(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Priority Package ID

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
            await client.prioritypackages.deleteprioritypackages(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteprioritypackages(id, request_options=request_options)
        return _response.data
