

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.api_response import ApiResponse
from ..types.group import Group
from ..types.group_user_settings import GroupUserSettings
from ..types.virtual_folder import VirtualFolder
from .raw_client import AsyncRawGroupsClient, RawGroupsClient
from .types.get_groups_request_order import GetGroupsRequestOrder


OMIT = typing.cast(typing.Any, ...)


class GroupsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGroupsClient
        """
        return self._raw_client

    def get_groups(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Group]:
        """
        Returns an array with one or more groups

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetGroupsRequestOrder]
            Ordering groups by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.get_groups()
        """
        _response = self._raw_client.get_groups(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    def add_group(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        user_settings: typing.Optional[GroupUserSettings] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Adds a new group

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        user_settings : typing.Optional[GroupUserSettings]

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and folders

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.add_group()
        """
        _response = self._raw_client.add_group(
            confidential_data=confidential_data,
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            user_settings=user_settings,
            virtual_folders=virtual_folders,
            users=users,
            admins=admins,
            request_options=request_options,
        )
        return _response.data

    def get_group_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Returns the group with the given name if it exists.

        Parameters
        ----------
        name : str
            group name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.get_group_by_name(
            name="name",
        )
        """
        _response = self._raw_client.get_group_by_name(
            name, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    def update_group(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        user_settings: typing.Optional[GroupUserSettings] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing group

        Parameters
        ----------
        name_ : str
            group name

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        user_settings : typing.Optional[GroupUserSettings]

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and folders

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.update_group(
            name_="name",
        )
        """
        _response = self._raw_client.update_group(
            name_,
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            user_settings=user_settings,
            virtual_folders=virtual_folders,
            users=users,
            admins=admins,
            request_options=request_options,
        )
        return _response.data

    def delete_group(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing group. A group referenced by users or admins cannot be deleted, remove the references first

        Parameters
        ----------
        name : str
            group name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.groups.delete_group(
            name="name",
        )
        """
        _response = self._raw_client.delete_group(name, request_options=request_options)
        return _response.data


class AsyncGroupsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGroupsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGroupsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGroupsClient
        """
        return self._raw_client

    async def get_groups(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        order: typing.Optional[GetGroupsRequestOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Group]:
        """
        Returns an array with one or more groups

        Parameters
        ----------
        offset : typing.Optional[int]

        limit : typing.Optional[int]
            The maximum number of items to return. Max value is 500, default is 100

        order : typing.Optional[GetGroupsRequestOrder]
            Ordering groups by name. Default ASC

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Group]
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.get_groups()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_groups(
            offset=offset, limit=limit, order=order, request_options=request_options
        )
        return _response.data

    async def add_group(
        self,
        *,
        confidential_data: typing.Optional[int] = None,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        user_settings: typing.Optional[GroupUserSettings] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Adds a new group

        Parameters
        ----------
        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        user_settings : typing.Optional[GroupUserSettings]

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and folders

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.add_group()


        asyncio.run(main())
        """
        _response = await self._raw_client.add_group(
            confidential_data=confidential_data,
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            user_settings=user_settings,
            virtual_folders=virtual_folders,
            users=users,
            admins=admins,
            request_options=request_options,
        )
        return _response.data

    async def get_group_by_name(
        self,
        name: str,
        *,
        confidential_data: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Group:
        """
        Returns the group with the given name if it exists.

        Parameters
        ----------
        name : str
            group name

        confidential_data : typing.Optional[int]
            If set to 1 confidential data will not be hidden. This means that the response will contain the key and additional data for secrets. If a master key is not set or an external KMS is used, the data returned are enough to get the secrets in cleartext. Ignored if the * permission is not granted.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Group
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.get_group_by_name(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_group_by_name(
            name, confidential_data=confidential_data, request_options=request_options
        )
        return _response.data

    async def update_group(
        self,
        name_: str,
        *,
        id: typing.Optional[int] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        created_at: typing.Optional[int] = OMIT,
        updated_at: typing.Optional[int] = OMIT,
        user_settings: typing.Optional[GroupUserSettings] = OMIT,
        virtual_folders: typing.Optional[typing.Sequence[VirtualFolder]] = OMIT,
        users: typing.Optional[typing.Sequence[str]] = OMIT,
        admins: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ApiResponse:
        """
        Updates an existing group

        Parameters
        ----------
        name_ : str
            group name

        id : typing.Optional[int]

        name : typing.Optional[str]
            name is unique

        description : typing.Optional[str]
            optional description

        created_at : typing.Optional[int]
            creation time as unix timestamp in milliseconds

        updated_at : typing.Optional[int]
            last update time as unix timestamp in milliseconds

        user_settings : typing.Optional[GroupUserSettings]

        virtual_folders : typing.Optional[typing.Sequence[VirtualFolder]]
            mapping between virtual SFTPGo paths and folders

        users : typing.Optional[typing.Sequence[str]]
            list of usernames associated with this group

        admins : typing.Optional[typing.Sequence[str]]
            list of admins usernames associated with this group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.update_group(
                name_="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_group(
            name_,
            id=id,
            name=name,
            description=description,
            created_at=created_at,
            updated_at=updated_at,
            user_settings=user_settings,
            virtual_folders=virtual_folders,
            users=users,
            admins=admins,
            request_options=request_options,
        )
        return _response.data

    async def delete_group(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> ApiResponse:
        """
        Deletes an existing group. A group referenced by users or admins cannot be deleted, remove the references first

        Parameters
        ----------
        name : str
            group name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ApiResponse
            successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            sftpgo_api_key="YOUR_SFTPGO_API_KEY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.groups.delete_group(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_group(name, request_options=request_options)
        return _response.data
