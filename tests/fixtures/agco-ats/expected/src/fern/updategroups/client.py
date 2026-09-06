

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_paged_response_update_system_models_bundle import ApiPagedResponseUpdateSystemModelsBundle
from ..types.update_system_models_update_group import UpdateSystemModelsUpdateGroup
from .raw_client import AsyncRawUpdategroupsClient, RawUpdategroupsClient


OMIT = typing.cast(typing.Any, ...)


class UpdategroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUpdategroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUpdategroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUpdategroupsClient
        """
        return self._raw_client

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> UpdateSystemModelsUpdateGroup:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Update Group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsUpdateGroup
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroups.get(
            id="ID",
        )
        """
        _response = self._raw_client.get(id, request_options=request_options)
        return _response.data

    def post(
        self,
        *,
        description: str,
        priority: int,
        update_type: str,
        id: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        report_field: typing.Optional[str] = OMIT,
        validating_field: typing.Optional[str] = OMIT,
        value_to_validate: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the update group

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        update_type : str
            The update type name

        id : typing.Optional[str]

        inventory_frequency : typing.Optional[int]
            The time in minutes between inventory checks. Default value is 1440 minutes (one day).

        inventory_package : typing.Optional[str]
            The Package ID of the package used for inventory

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the update group

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the update group

        report_field : typing.Optional[str]
            A field to return in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        validating_field : typing.Optional[str]
            A field used for validation in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        value_to_validate : typing.Optional[str]
            The value to validate the ValidationField against.

        version : typing.Optional[str]
            The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType

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
        client.updategroups.post(
            description="Description",
            priority=1,
            update_type="UpdateType",
        )
        """
        _response = self._raw_client.post(
            description=description,
            priority=priority,
            update_type=update_type,
            id=id,
            inventory_frequency=inventory_frequency,
            inventory_package=inventory_package,
            localized_description=localized_description,
            localized_name=localized_name,
            report_field=report_field,
            validating_field=validating_field,
            value_to_validate=value_to_validate,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def put(
        self,
        id_: str,
        *,
        description: str,
        priority: int,
        update_type: str,
        id: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        report_field: typing.Optional[str] = OMIT,
        validating_field: typing.Optional[str] = OMIT,
        value_to_validate: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str
            ID of the Update Group

        description : str
            The description of the update group

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        update_type : str
            The update type name

        id : typing.Optional[str]

        inventory_frequency : typing.Optional[int]
            The time in minutes between inventory checks. Default value is 1440 minutes (one day).

        inventory_package : typing.Optional[str]
            The Package ID of the package used for inventory

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the update group

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the update group

        report_field : typing.Optional[str]
            A field to return in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        validating_field : typing.Optional[str]
            A field used for validation in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        value_to_validate : typing.Optional[str]
            The value to validate the ValidationField against.

        version : typing.Optional[str]
            The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroups.put(
            id_="ID",
            description="Description",
            priority=1,
            update_type="UpdateType",
        )
        """
        _response = self._raw_client.put(
            id_,
            description=description,
            priority=priority,
            update_type=update_type,
            id=id,
            inventory_frequency=inventory_frequency,
            inventory_package=inventory_package,
            localized_description=localized_description,
            localized_name=localized_name,
            report_field=report_field,
            validating_field=validating_field,
            value_to_validate=value_to_validate,
            version=version,
            request_options=request_options,
        )
        return _response.data

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Update Group to Delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroups.delete(
            id="ID",
        )
        """
        _response = self._raw_client.delete(id, request_options=request_options)
        return _response.data

    def getupdategroupbundles(
        self,
        id: str,
        *,
        include_inactive: bool,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsBundle:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        include_inactive : bool
            Include Inactive Bundles (true|false)

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsBundle
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroups.getupdategroupbundles(
            id="ID",
            include_inactive=True,
        )
        """
        _response = self._raw_client.getupdategroupbundles(
            id, include_inactive=include_inactive, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def addupdategroupuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the update group

        user_id : int
            The userID to link to the update group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroups.addupdategroupuser(
            id="id",
            user_id=1,
        )
        """
        _response = self._raw_client.addupdategroupuser(id, user_id, request_options=request_options)
        return _response.data

    def removeupdategroupuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the update group

        user_id : int
            The userID to link to the update group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.updategroups.removeupdategroupuser(
            id="id",
            user_id=1,
        )
        """
        _response = self._raw_client.removeupdategroupuser(id, user_id, request_options=request_options)
        return _response.data


class AsyncUpdategroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUpdategroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUpdategroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUpdategroupsClient
        """
        return self._raw_client

    async def get(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateSystemModelsUpdateGroup:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Update Group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSystemModelsUpdateGroup
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.updategroups.get(
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
        priority: int,
        update_type: str,
        id: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        report_field: typing.Optional[str] = OMIT,
        validating_field: typing.Optional[str] = OMIT,
        value_to_validate: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        No Documentation Found.

        Parameters
        ----------
        description : str
            The description of the update group

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        update_type : str
            The update type name

        id : typing.Optional[str]

        inventory_frequency : typing.Optional[int]
            The time in minutes between inventory checks. Default value is 1440 minutes (one day).

        inventory_package : typing.Optional[str]
            The Package ID of the package used for inventory

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the update group

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the update group

        report_field : typing.Optional[str]
            A field to return in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        validating_field : typing.Optional[str]
            A field used for validation in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        value_to_validate : typing.Optional[str]
            The value to validate the ValidationField against.

        version : typing.Optional[str]
            The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType

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
            await client.updategroups.post(
                description="Description",
                priority=1,
                update_type="UpdateType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post(
            description=description,
            priority=priority,
            update_type=update_type,
            id=id,
            inventory_frequency=inventory_frequency,
            inventory_package=inventory_package,
            localized_description=localized_description,
            localized_name=localized_name,
            report_field=report_field,
            validating_field=validating_field,
            value_to_validate=value_to_validate,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def put(
        self,
        id_: str,
        *,
        description: str,
        priority: int,
        update_type: str,
        id: typing.Optional[str] = OMIT,
        inventory_frequency: typing.Optional[int] = OMIT,
        inventory_package: typing.Optional[str] = OMIT,
        localized_description: typing.Optional[str] = OMIT,
        localized_name: typing.Optional[str] = OMIT,
        report_field: typing.Optional[str] = OMIT,
        validating_field: typing.Optional[str] = OMIT,
        value_to_validate: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id_ : str
            ID of the Update Group

        description : str
            The description of the update group

        priority : int
            The execution priority of the package relative to other packages in the bundle. Range 1 - 100, lower value indication higher priority.

        update_type : str
            The update type name

        id : typing.Optional[str]

        inventory_frequency : typing.Optional[int]
            The time in minutes between inventory checks. Default value is 1440 minutes (one day).

        inventory_package : typing.Optional[str]
            The Package ID of the package used for inventory

        localized_description : typing.Optional[str]
            Optional. The StringID used to localize the description of the update group

        localized_name : typing.Optional[str]
            Optional. The StringID used to localize the name of the update group

        report_field : typing.Optional[str]
            A field to return in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        validating_field : typing.Optional[str]
            A field used for validation in the status report for this update group.
                        Specify the field with the format [Label]: {[InventoryPackageID].[Category].[Attribute]}.  (i.e. example: {bec778ca-278d-424a-867a-4653a1a19e86.MyCategory.MyAttribute})

        value_to_validate : typing.Optional[str]
            The value to validate the ValidationField against.

        version : typing.Optional[str]
            The version of the UpdateGroup, this value is incremented with each modification to a related Bundle or PackageType

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
            await client.updategroups.put(
                id_="ID",
                description="Description",
                priority=1,
                update_type="UpdateType",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put(
            id_,
            description=description,
            priority=priority,
            update_type=update_type,
            id=id,
            inventory_frequency=inventory_frequency,
            inventory_package=inventory_package,
            localized_description=localized_description,
            localized_name=localized_name,
            report_field=report_field,
            validating_field=validating_field,
            value_to_validate=value_to_validate,
            version=version,
            request_options=request_options,
        )
        return _response.data

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the Update Group to Delete

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
            await client.updategroups.delete(
                id="ID",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, request_options=request_options)
        return _response.data

    async def getupdategroupbundles(
        self,
        id: str,
        *,
        include_inactive: bool,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiPagedResponseUpdateSystemModelsBundle:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The UpdateGroupID

        include_inactive : bool
            Include Inactive Bundles (true|false)

        limit : typing.Optional[int]
            Optional. The page limit. The default page limit is 10.

        offset : typing.Optional[int]
            Optional. The page offset. The default page offset is 0.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiPagedResponseUpdateSystemModelsBundle
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.updategroups.getupdategroupbundles(
                id="ID",
                include_inactive=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getupdategroupbundles(
            id, include_inactive=include_inactive, limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def addupdategroupuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the update group

        user_id : int
            The userID to link to the update group

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
            await client.updategroups.addupdategroupuser(
                id="id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.addupdategroupuser(id, user_id, request_options=request_options)
        return _response.data

    async def removeupdategroupuser(
        self, id: str, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the update group

        user_id : int
            The userID to link to the update group

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
            await client.updategroups.removeupdategroupuser(
                id="id",
                user_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.removeupdategroupuser(id, user_id, request_options=request_options)
        return _response.data
