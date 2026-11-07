

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.info import Info
from .raw_client import AsyncRawOrganizeClient, RawOrganizeClient
from .types.move_folder_by_id_request_action import MoveFolderByIdRequestAction


class OrganizeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizeClient
        """
        return self._raw_client

    def create_folder(
        self,
        *,
        parent_folder: int,
        folder_name: str,
        group_name: typing.Optional[str] = None,
        folder_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Create a new child folder with optional description

        Parameters
        ----------
        parent_folder : int
            Parent folder for the new folder

        folder_name : str
            Name of the new folder

        group_name : typing.Optional[str]
            The group name to chose while accessing folders

        folder_description : typing.Optional[str]
            Description of the new folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Folder with the same name already exists under the same parent

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organize.create_folder(
            parent_folder=1,
            folder_name="folderName",
        )
        """
        _response = self._raw_client.create_folder(
            parent_folder=parent_folder,
            folder_name=folder_name,
            group_name=group_name,
            folder_description=folder_description,
            request_options=request_options,
        )
        return _response.data

    def move_folder_by_id(
        self,
        id: int,
        *,
        parent: int,
        action: MoveFolderByIdRequestAction,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Copy or move a folder by id

        Parameters
        ----------
        id : int
            ID of the folder

        parent : int
            New parent folder id

        action : MoveFolderByIdRequestAction
            Action to be performed

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Folder will be copied/moved

        Examples
        --------
        from fern.organize import MoveFolderByIdRequestAction

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organize.move_folder_by_id(
            id=1,
            parent=1,
            action=MoveFolderByIdRequestAction.COPY,
        )
        """
        _response = self._raw_client.move_folder_by_id(
            id, parent=parent, action=action, group_name=group_name, request_options=request_options
        )
        return _response.data

    def delete_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Schedule a folder deletion

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Folder scheduled to be deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organize.delete_folder_by_id(
            id=1,
        )
        """
        _response = self._raw_client.delete_folder_by_id(id, group_name=group_name, request_options=request_options)
        return _response.data

    def patch_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Change a folder's name and/or description

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        name : typing.Optional[str]
            New name of the folder

        description : typing.Optional[str]
            New description of the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Folder is updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organize.patch_folder_by_id(
            id=1,
        )
        """
        _response = self._raw_client.patch_folder_by_id(
            id, group_name=group_name, name=name, description=description, request_options=request_options
        )
        return _response.data

    def create_group(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Create a new user group

        Parameters
        ----------
        name : str
            Name of the new group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Group has been added

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.organize.create_group(
            name="name",
        )
        """
        _response = self._raw_client.create_group(name=name, request_options=request_options)
        return _response.data


class AsyncOrganizeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizeClient
        """
        return self._raw_client

    async def create_folder(
        self,
        *,
        parent_folder: int,
        folder_name: str,
        group_name: typing.Optional[str] = None,
        folder_description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Create a new child folder with optional description

        Parameters
        ----------
        parent_folder : int
            Parent folder for the new folder

        folder_name : str
            Name of the new folder

        group_name : typing.Optional[str]
            The group name to chose while accessing folders

        folder_description : typing.Optional[str]
            Description of the new folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Folder with the same name already exists under the same parent

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organize.create_folder(
                parent_folder=1,
                folder_name="folderName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_folder(
            parent_folder=parent_folder,
            folder_name=folder_name,
            group_name=group_name,
            folder_description=folder_description,
            request_options=request_options,
        )
        return _response.data

    async def move_folder_by_id(
        self,
        id: int,
        *,
        parent: int,
        action: MoveFolderByIdRequestAction,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Copy or move a folder by id

        Parameters
        ----------
        id : int
            ID of the folder

        parent : int
            New parent folder id

        action : MoveFolderByIdRequestAction
            Action to be performed

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Folder will be copied/moved

        Examples
        --------
        import asyncio

        from fern.organize import MoveFolderByIdRequestAction

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organize.move_folder_by_id(
                id=1,
                parent=1,
                action=MoveFolderByIdRequestAction.COPY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.move_folder_by_id(
            id, parent=parent, action=action, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def delete_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Schedule a folder deletion

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Folder scheduled to be deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organize.delete_folder_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_folder_by_id(
            id, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def patch_folder_by_id(
        self,
        id: int,
        *,
        group_name: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Change a folder's name and/or description

        Parameters
        ----------
        id : int
            ID of the folder

        group_name : typing.Optional[str]
            The group name to chose while accessing the folder

        name : typing.Optional[str]
            New name of the folder

        description : typing.Optional[str]
            New description of the folder

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Folder is updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organize.patch_folder_by_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_folder_by_id(
            id, group_name=group_name, name=name, description=description, request_options=request_options
        )
        return _response.data

    async def create_group(self, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> Info:
        """
        Create a new user group

        Parameters
        ----------
        name : str
            Name of the new group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Group has been added

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.organize.create_group(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_group(name=name, request_options=request_options)
        return _response.data
