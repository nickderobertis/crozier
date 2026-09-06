

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.update_system_models_package_type import UpdateSystemModelsPackageType
from .raw_client import AsyncRawPackagetypesClient, RawPackagetypesClient


OMIT = typing.cast(typing.Any, ...)


class PackagetypesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPackagetypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPackagetypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPackagetypesClient
        """
        return self._raw_client

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> UpdateSystemModelsPackageType:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package Type ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsPackageType
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagetypes.get(
            id="ID",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def post(
        self,
        *,
        description: str,
        attribute: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        max_delta_packages: typing.Optional[int] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the package type

        attribute : typing.Optional[str]
            The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.

        category : typing.Optional[str]
            The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.

        icon : typing.Optional[str]
            Optional.  The icon to use for the PackageType, in base 64

        inventory_frequency : typing.Optional[int]
            The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).

        inventory_package : typing.Optional[str]
            The inventory package used to determine what version of this package type is installed.

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the PackageType

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the PackageType

        max_delta_packages : typing.Optional[int]
            The maximum number of "chained" delta packages to use when updating the client

        package_type_id : typing.Optional[str]
            Read Only. The package type id.

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
        client.packagetypes.post(
            description="Description",
        )
        """
        _response = self._raw_client.post(
            description=description,
            attribute=attribute,
            category=category,
            icon=icon,
            inventory_frequency=inventory_frequency,
            inventory_package=inventory_package,
            localized_description=localized_description,
            localized_name=localized_name,
            max_delta_packages=max_delta_packages,
            package_type_id=package_type_id,
            request_options=request_options,
        )
        return _response.data

    def put(
        self,
        id: str,
        *,
        description: str,
        attribute: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        max_delta_packages: typing.Optional[int] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        description : str
            The description of the package type

        attribute : typing.Optional[str]
            The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.

        category : typing.Optional[str]
            The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.

        icon : typing.Optional[str]
            Optional.  The icon to use for the PackageType, in base 64

        inventory_frequency : typing.Optional[int]
            The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).

        inventory_package : typing.Optional[str]
            The inventory package used to determine what version of this package type is installed.

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the PackageType

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the PackageType

        max_delta_packages : typing.Optional[int]
            The maximum number of "chained" delta packages to use when updating the client

        package_type_id : typing.Optional[str]
            Read Only. The package type id.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagetypes.put(
            id="ID",
            description="Description",
        )
        """
        _response = self._raw_client.put(
            id,
            description=description,
            attribute=attribute,
            category=category,
            icon=icon,
            inventory_frequency=inventory_frequency,
            inventory_package=inventory_package,
            localized_description=localized_description,
            localized_name=localized_name,
            max_delta_packages=max_delta_packages,
            package_type_id=package_type_id,
            request_options=request_options,
        )
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package Type ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagetypes.delete(
            id="ID",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def addpackagetypeuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        user_id : int
            The userID to link to the package type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagetypes.addpackagetypeuser(
            id="id",
            user_id=1,
        )
        """
        _response = self._raw_client.addpackagetypeuser(id, user_id, request_options=request_options)
        return _response.data

    def removepackagetypeuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        user_id : int
            The userID to link to the package type

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.packagetypes.removepackagetypeuser(
            id="id",
            user_id=1,
        )
        """
        _response = self._raw_client.removepackagetypeuser(id, user_id, request_options=request_options)
        return _response.data


class AsyncPackagetypesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPackagetypesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPackagetypesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPackagetypesClient
        """
        return self._raw_client

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsPackageType:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package Type ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsPackageType
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.packagetypes.get(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(id, request_options=request_options)
        return _response.data

    async def post(
        self,
        *,
        description: str,
        attribute: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        max_delta_packages: typing.Optional[int] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the package type

        attribute : typing.Optional[str]
            The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.

        category : typing.Optional[str]
            The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.

        icon : typing.Optional[str]
            Optional.  The icon to use for the PackageType, in base 64

        inventory_frequency : typing.Optional[int]
            The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).

        inventory_package : typing.Optional[str]
            The inventory package used to determine what version of this package type is installed.

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the PackageType

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the PackageType

        max_delta_packages : typing.Optional[int]
            The maximum number of "chained" delta packages to use when updating the client

        package_type_id : typing.Optional[str]
            Read Only. The package type id.

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
            await client.packagetypes.post(
                description="Description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post(
            description=description,
            attribute=attribute,
            category=category,
            icon=icon,
            inventory_frequency=inventory_frequency,
            inventory_package=inventory_package,
            localized_description=localized_description,
            localized_name=localized_name,
            max_delta_packages=max_delta_packages,
            package_type_id=package_type_id,
            request_options=request_options,
        )
        return _response.data

    async def put(
        self,
        id: str,
        *,
        description: str,
        attribute: typing.Optional[str] = OMIT,
        category: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        max_delta_packages: typing.Optional[int] = OMIT,
        package_type_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        description : str
            The description of the package type

        attribute : typing.Optional[str]
            The inventory attribute (from the InventoryPackage) used to determine what version of this package type is installed.

        category : typing.Optional[str]
            The inventory category (from the InventoryPackage) used to determine what version of this package type is installed.

        icon : typing.Optional[str]
            Optional.  The icon to use for the PackageType, in base 64

        inventory_frequency : typing.Optional[int]
            The number of minutes to wait before requesting another inventory.  The default value is 1440 (24 hours).

        inventory_package : typing.Optional[str]
            The inventory package used to determine what version of this package type is installed.

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the PackageType

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the PackageType

        max_delta_packages : typing.Optional[int]
            The maximum number of "chained" delta packages to use when updating the client

        package_type_id : typing.Optional[str]
            Read Only. The package type id.

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
            await client.packagetypes.put(
                id="ID",
                description="Description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(
            id,
            description=description,
            attribute=attribute,
            category=category,
            icon=icon,
            inventory_frequency=inventory_frequency,
            inventory_package=inventory_package,
            localized_description=localized_description,
            localized_name=localized_name,
            max_delta_packages=max_delta_packages,
            package_type_id=package_type_id,
            request_options=request_options,
        )
        return _response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The Package Type ID

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
            await client.packagetypes.delete(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def addpackagetypeuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        user_id : int
            The userID to link to the package type

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
            await client.packagetypes.addpackagetypeuser(
                id="id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addpackagetypeuser(id, user_id, request_options=request_options)
        return _response.data

    async def removepackagetypeuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Package Type

        user_id : int
            The userID to link to the package type

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
            await client.packagetypes.removepackagetypeuser(
                id="id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removepackagetypeuser(id, user_id, request_options=request_options)
        return _response.data
