

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_package import ApiPagedResponseUpdateSystemModelsPackage
from ..types.update_system_models_package import UpdateSystemModelsPackage
from .raw_client import AsyncRawPackagesClient, RawPackagesClient


OMIT = typing.cast(typing.Any, ...)


class PackagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPackagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPackagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPackagesClient
        """
        return self._raw_client

    def getpackages(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        package_type_id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        released: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsPackage:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        package_type_id : typing.Optional[str]
            Optional. If provided, filters by PackageTypeID.

        version : typing.Optional[int]
            Optional. If provided, filters by Version.

        released : typing.Optional[bool]
            Optional. If provided, filters by Released.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsPackage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packages.getpackages()
        """
        _response = self._raw_client.getpackages(
            limit=limit,
            offset=offset,
            package_type_id=package_type_id,
            version=version,
            released=released,
            request_options=request_options,
        )
        return _response.data

    def postpackage(
        self,
        *,
        crc: str,
        description: str,
        package_type_id: str,
        release_date: dt.datetime,
        url: str,
        version: int,
        autorun: typing.Optional[bool] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The CRC used to validate the download.

        description : str
            The package description

        package_type_id : str
            The id of the package type this package belongs to.

        release_date : dt.datetime
            The date the package was released

        url : str
            The Url to download the package from.

        version : int
            The version.

        autorun : typing.Optional[bool]
            Value is true if package should run automatically. Default value is false.

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the Package

        notes : typing.Optional[str]
            Notes about the package

        package_id : typing.Optional[str]
            Read Only. The package ID

        previous_version : typing.Optional[int]
            For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.

        released : typing.Optional[bool]
            True if the package is released.  Default value is False.

        remove_on_success : typing.Optional[bool]
            True to remove the package after successful execution.  Default value is False.

        size : typing.Optional[int]
            The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.
                        If the size provided does not match the size in the response from the URL an error will be returned.

        switches : typing.Optional[str]
            The command line arguments for the package.  Default value is an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi()
        client.packages.postpackage(
            crc="CRC",
            description="Description",
            package_type_id="PackageTypeID",
            release_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            url="Url",
            version=1,
        )
        """
        _response = self._raw_client.postpackage(
            crc=crc,
            description=description,
            package_type_id=package_type_id,
            release_date=release_date,
            url=url,
            version=version,
            autorun=autorun,
            localized_name=localized_name,
            notes=notes,
            package_id=package_id,
            previous_version=previous_version,
            released=released,
            remove_on_success=remove_on_success,
            size=size,
            switches=switches,
            request_options=request_options,
        )
        return _response.data

    def getpackage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsPackage:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package ID to Search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsPackage
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packages.getpackage(
            id="ID",
        )
        """
        _response = self._raw_client.getpackage(id, request_options=request_options)
        return _response.data

    def putpackage(
        self,
        id: str,
        *,
        crc: str,
        description: str,
        package_type_id: str,
        release_date: dt.datetime,
        url: str,
        version: int,
        autorun: typing.Optional[bool] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The unique ID of the Package

        crc : str
            The CRC used to validate the download.

        description : str
            The package description

        package_type_id : str
            The id of the package type this package belongs to.

        release_date : dt.datetime
            The date the package was released

        url : str
            The Url to download the package from.

        version : int
            The version.

        autorun : typing.Optional[bool]
            Value is true if package should run automatically. Default value is false.

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the Package

        notes : typing.Optional[str]
            Notes about the package

        package_id : typing.Optional[str]
            Read Only. The package ID

        previous_version : typing.Optional[int]
            For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.

        released : typing.Optional[bool]
            True if the package is released.  Default value is False.

        remove_on_success : typing.Optional[bool]
            True to remove the package after successful execution.  Default value is False.

        size : typing.Optional[int]
            The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.
                        If the size provided does not match the size in the response from the URL an error will be returned.

        switches : typing.Optional[str]
            The command line arguments for the package.  Default value is an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi()
        client.packages.putpackage(
            id="ID",
            crc="CRC",
            description="Description",
            package_type_id="PackageTypeID",
            release_date=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            url="Url",
            version=1,
        )
        """
        _response = self._raw_client.putpackage(
            id,
            crc=crc,
            description=description,
            package_type_id=package_type_id,
            release_date=release_date,
            url=url,
            version=version,
            autorun=autorun,
            localized_name=localized_name,
            notes=notes,
            package_id=package_id,
            previous_version=previous_version,
            released=released,
            remove_on_success=remove_on_success,
            size=size,
            switches=switches,
            request_options=request_options,
        )
        return _response.data

    def deletepackage(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package ID to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packages.deletepackage(
            id="ID",
        )
        """
        _response = self._raw_client.deletepackage(id, request_options=request_options)
        return _response.data


class AsyncPackagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPackagesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPackagesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPackagesClient
        """
        return self._raw_client

    async def getpackages(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        package_type_id: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        released: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsPackage:
        """
        No Documentation Found.

        Parameters
        ----------
        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        package_type_id : typing.Optional[str]
            Optional. If provided, filters by PackageTypeID.

        version : typing.Optional[int]
            Optional. If provided, filters by Version.

        released : typing.Optional[bool]
            Optional. If provided, filters by Released.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsPackage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packages.getpackages()


        asyncio.run(main())
        """
        _response = await self._raw_client.getpackages(
            limit=limit,
            offset=offset,
            package_type_id=package_type_id,
            version=version,
            released=released,
            request_options=request_options,
        )
        return _response.data

    async def postpackage(
        self,
        *,
        crc: str,
        description: str,
        package_type_id: str,
        release_date: dt.datetime,
        url: str,
        version: int,
        autorun: typing.Optional[bool] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        crc : str
            The CRC used to validate the download.

        description : str
            The package description

        package_type_id : str
            The id of the package type this package belongs to.

        release_date : dt.datetime
            The date the package was released

        url : str
            The Url to download the package from.

        version : int
            The version.

        autorun : typing.Optional[bool]
            Value is true if package should run automatically. Default value is false.

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the Package

        notes : typing.Optional[str]
            Notes about the package

        package_id : typing.Optional[str]
            Read Only. The package ID

        previous_version : typing.Optional[int]
            For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.

        released : typing.Optional[bool]
            True if the package is released.  Default value is False.

        remove_on_success : typing.Optional[bool]
            True to remove the package after successful execution.  Default value is False.

        size : typing.Optional[int]
            The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.
                        If the size provided does not match the size in the response from the URL an error will be returned.

        switches : typing.Optional[str]
            The command line arguments for the package.  Default value is an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packages.postpackage(
                crc="CRC",
                description="Description",
                package_type_id="PackageTypeID",
                release_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                url="Url",
                version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.postpackage(
            crc=crc,
            description=description,
            package_type_id=package_type_id,
            release_date=release_date,
            url=url,
            version=version,
            autorun=autorun,
            localized_name=localized_name,
            notes=notes,
            package_id=package_id,
            previous_version=previous_version,
            released=released,
            remove_on_success=remove_on_success,
            size=size,
            switches=switches,
            request_options=request_options,
        )
        return _response.data

    async def getpackage(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsPackage:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package ID to Search for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsPackage
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packages.getpackage(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getpackage(id, request_options=request_options)
        return _response.data

    async def putpackage(
        self,
        id: str,
        *,
        crc: str,
        description: str,
        package_type_id: str,
        release_date: dt.datetime,
        url: str,
        version: int,
        autorun: typing.Optional[bool] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        notes: typing.Optional[str] = OMIT,
        package_id: typing.Optional[str] = OMIT,
        previous_version: typing.Optional[int] = OMIT,
        released: typing.Optional[bool] = OMIT,
        remove_on_success: typing.Optional[bool] = OMIT,
        size: typing.Optional[int] = OMIT,
        switches: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The unique ID of the Package

        crc : str
            The CRC used to validate the download.

        description : str
            The package description

        package_type_id : str
            The id of the package type this package belongs to.

        release_date : dt.datetime
            The date the package was released

        url : str
            The Url to download the package from.

        version : int
            The version.

        autorun : typing.Optional[bool]
            Value is true if package should run automatically. Default value is false.

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the Package

        notes : typing.Optional[str]
            Notes about the package

        package_id : typing.Optional[str]
            Read Only. The package ID

        previous_version : typing.Optional[int]
            For delta packages, the previous version required.  For non-delta packages, the Previous version is 0.  Default value is 0.

        released : typing.Optional[bool]
            True if the package is released.  Default value is False.

        remove_on_success : typing.Optional[bool]
            True to remove the package after successful execution.  Default value is False.

        size : typing.Optional[int]
            The size of the file at the specified URL.  If a size is not supplied at creation time, the size will be determined by the response from the URL.
                        If the size provided does not match the size in the response from the URL an error will be returned.

        switches : typing.Optional[str]
            The command line arguments for the package.  Default value is an empty string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packages.putpackage(
                id="ID",
                crc="CRC",
                description="Description",
                package_type_id="PackageTypeID",
                release_date=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                url="Url",
                version=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putpackage(
            id,
            crc=crc,
            description=description,
            package_type_id=package_type_id,
            release_date=release_date,
            url=url,
            version=version,
            autorun=autorun,
            localized_name=localized_name,
            notes=notes,
            package_id=package_id,
            previous_version=previous_version,
            released=released,
            remove_on_success=remove_on_success,
            size=size,
            switches=switches,
            request_options=request_options,
        )
        return _response.data

    async def deletepackage(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package ID to Delete

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
            await client.packages.deletepackage(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletepackage(id, request_options=request_options)
        return _response.data
