

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.branch import Branch
from ..types.file_revision_metadata_v2 import FileRevisionMetadataV2
from ..types.t_environment_variable import TEnvironmentVariable
from ..types.val import Val
from .raw_client import AsyncRawValsClient, RawValsClient
from .types.branches_list2response import BranchesList2Response
from .types.file_content_update2request_type import FileContentUpdate2RequestType
from .types.files_create2request_body import FilesCreate2RequestBody
from .types.val_environment_variable_groups_list_response import ValEnvironmentVariableGroupsListResponse
from .types.val_environment_variables_list_response import ValEnvironmentVariablesListResponse
from .types.val_files_get2response import ValFilesGet2Response
from .types.vals_create2request_privacy import ValsCreate2RequestPrivacy
from .types.vals_list2request_privacy import ValsList2RequestPrivacy
from .types.vals_list2response import ValsList2Response


OMIT = typing.cast(typing.Any, ...)


class ValsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawValsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawValsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawValsClient
        """
        return self._raw_client

    def val_environment_variables_list(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ValEnvironmentVariablesListResponse:
        """
        List environment variables defined in this project. This only includes names, not values.

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValEnvironmentVariablesListResponse
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.val_environment_variables_list(
            val_id="val_id",
            offset=1,
            limit=1,
        )
        """
        _response = self._raw_client.val_environment_variables_list(
            val_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def val_environment_variables_create(
        self,
        val_id: str,
        *,
        value: str,
        key: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TEnvironmentVariable:
        """
        Create a new environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        value : str
            Value of the environment variable.

        key : str
            Name or key of the environment variable, accessible via Deno.env or process.env

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TEnvironmentVariable
            An environment variable

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.val_environment_variables_create(
            val_id="val_id",
            value="value",
            key="key",
        )
        """
        _response = self._raw_client.val_environment_variables_create(
            val_id, value=value, key=key, description=description, request_options=request_options
        )
        return _response.data

    def val_environment_variables_update(
        self,
        val_id: str,
        key: str,
        *,
        value: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TEnvironmentVariable:
        """
        Update a environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        key : str

        value : str
            Value of the environment variable.

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TEnvironmentVariable
            An environment variable

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.val_environment_variables_update(
            val_id="val_id",
            key="key",
            value="value",
        )
        """
        _response = self._raw_client.val_environment_variables_update(
            val_id, key, value=value, description=description, request_options=request_options
        )
        return _response.data

    def val_environment_variables_delete(
        self, val_id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.val_environment_variables_delete(
            val_id="val_id",
            key="key",
        )
        """
        _response = self._raw_client.val_environment_variables_delete(val_id, key, request_options=request_options)
        return _response.data

    def val_environment_variable_groups_list(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ValEnvironmentVariableGroupsListResponse:
        """
        List the environment variable groups attached to this val. This only includes the groups, not the variables in them.

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValEnvironmentVariableGroupsListResponse
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.val_environment_variable_groups_list(
            val_id="val_id",
            offset=1,
            limit=1,
        )
        """
        _response = self._raw_client.val_environment_variable_groups_list(
            val_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def val_environment_variable_groups_attach(
        self, val_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Attach an environment variable group to this val. Every variable in the group is injected into the val's environment. Variables defined on the val itself take precedence over variables with the same key in a group. Attaching a group that is already attached succeeds without doing anything.

        Parameters
        ----------
        val_id : str
            Id of a val

        group_id : str
            Id of an environment variable group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.val_environment_variable_groups_attach(
            val_id="val_id",
            group_id="group_id",
        )
        """
        _response = self._raw_client.val_environment_variable_groups_attach(
            val_id, group_id, request_options=request_options
        )
        return _response.data

    def val_environment_variable_groups_detach(
        self, val_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Detach an environment variable group from this val. The group itself, and the variables in it, are left alone.

        Parameters
        ----------
        val_id : str
            Id of a val

        group_id : str
            Id of an environment variable group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.val_environment_variable_groups_detach(
            val_id="val_id",
            group_id="group_id",
        )
        """
        _response = self._raw_client.val_environment_variable_groups_detach(
            val_id, group_id, request_options=request_options
        )
        return _response.data

    def vals_get2(self, val_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Val:
        """
        Get a val by id

        Parameters
        ----------
        val_id : str
            Id of a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Val
            A Val

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.vals_get2(
            val_id="val_id",
        )
        """
        _response = self._raw_client.vals_get2(val_id, request_options=request_options)
        return _response.data

    def projects_delete2(self, val_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a project

        Parameters
        ----------
        val_id : str
            Id of a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.projects_delete2(
            val_id="val_id",
        )
        """
        _response = self._raw_client.projects_delete2(val_id, request_options=request_options)
        return _response.data

    def vals_list2(
        self,
        *,
        limit: int,
        privacy: typing.Optional[ValsList2RequestPrivacy] = None,
        user_id: typing.Optional[str] = None,
        cursor: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValsList2Response:
        """
        Lists all vals including all public vals and your unlisted and private vals

        Parameters
        ----------
        limit : int
            Maximum items to return in each paginated response

        privacy : typing.Optional[ValsList2RequestPrivacy]
            This resource's privacy setting. Unlisted resources do not appear on profile pages or elsewhere, but you can link to them.

        user_id : typing.Optional[str]
            User ID to filter by

        cursor : typing.Optional[dt.datetime]
            Cursor to start the pagination from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValsList2Response
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.vals_list2(
            limit=1,
        )
        """
        _response = self._raw_client.vals_list2(
            limit=limit, privacy=privacy, user_id=user_id, cursor=cursor, request_options=request_options
        )
        return _response.data

    def vals_create2(
        self,
        *,
        name: str,
        privacy: ValsCreate2RequestPrivacy,
        description: typing.Optional[str] = OMIT,
        org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Val:
        """
        Create a new val

        Parameters
        ----------
        name : str

        privacy : ValsCreate2RequestPrivacy

        description : typing.Optional[str]

        org_id : typing.Optional[str]
            ID of the org to create the val in

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Val
            A Val

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.vals_create2(
            name="myVal",
            description="My val",
            privacy="public",
        )
        """
        _response = self._raw_client.vals_create2(
            name=name, privacy=privacy, description=description, org_id=org_id, request_options=request_options
        )
        return _response.data

    def branches_get2(
        self, val_id: str, branch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Branch:
        """
        Get a branch by id

        Parameters
        ----------
        val_id : str
            Id of a val

        branch_id : str
            Id of a branch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Branch
            A Branch

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.branches_get2(
            val_id="val_id",
            branch_id="branch_id",
        )
        """
        _response = self._raw_client.branches_get2(val_id, branch_id, request_options=request_options)
        return _response.data

    def branches_delete2(
        self, val_id: str, branch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a branch

        Parameters
        ----------
        val_id : str
            Id of a val

        branch_id : str
            Id of a branch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.branches_delete2(
            val_id="val_id",
            branch_id="branch_id",
        )
        """
        _response = self._raw_client.branches_delete2(val_id, branch_id, request_options=request_options)
        return _response.data

    def branches_list2(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> BranchesList2Response:
        """
        List all branches for a val

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchesList2Response
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.branches_list2(
            val_id="val_id",
            offset=1,
            limit=1,
        )
        """
        _response = self._raw_client.branches_list2(val_id, offset=offset, limit=limit, request_options=request_options)
        return _response.data

    def branches_create2(
        self,
        val_id: str,
        *,
        name: str,
        branch_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Branch:
        """
        Create a new branch

        Parameters
        ----------
        val_id : str
            Id of a val

        name : str

        branch_id : typing.Optional[str]
            The branch ID to fork from. If this is not specified, the new branch will be forked from main.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Branch
            A Branch

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.branches_create2(
            val_id="val_id",
            name="my-branch",
            branch_id="00000000-0000-0000-0000-000000000000",
        )
        """
        _response = self._raw_client.branches_create2(
            val_id, name=name, branch_id=branch_id, request_options=request_options
        )
        return _response.data

    def val_files_get2(
        self,
        val_id: str,
        *,
        path: str,
        recursive: bool,
        offset: int,
        limit: int,
        version: typing.Optional[int] = None,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValFilesGet2Response:
        """
        Get metadata for files and directories in a val. If path is an empty string, returns files at the root directory.

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        recursive : bool
            Whether to recursively act on all files in the project

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        version : typing.Optional[int]
            Specific branch version to query

        branch_id : typing.Optional[str]
            Id to query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValFilesGet2Response
            A paginated result set

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.val_files_get2(
            val_id="val_id",
            path="path",
            recursive=True,
            offset=1,
            limit=1,
        )
        """
        _response = self._raw_client.val_files_get2(
            val_id,
            path=path,
            recursive=recursive,
            offset=offset,
            limit=limit,
            version=version,
            branch_id=branch_id,
            request_options=request_options,
        )
        return _response.data

    def files_create2(
        self,
        val_id: str,
        *,
        path: str,
        request: FilesCreate2RequestBody,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileRevisionMetadataV2:
        """
        Create a new file, project val or directory

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        request : FilesCreate2RequestBody

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileRevisionMetadataV2
            A File or Directory's Metadata

        Examples
        --------
        from fern.vals import FilesCreate2RequestBodyZero

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.files_create2(
            val_id="val_id",
            path="path",
            request=FilesCreate2RequestBodyZero(
                type="directory",
            ),
        )
        """
        _response = self._raw_client.files_create2(
            val_id, path=path, request=request, branch_id=branch_id, request_options=request_options
        )
        return _response.data

    def file_content_update2(
        self,
        val_id: str,
        *,
        path: str,
        branch_id: typing.Optional[str] = None,
        content: typing.Optional[str] = OMIT,
        type: typing.Optional[FileContentUpdate2RequestType] = OMIT,
        parent_path: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileRevisionMetadataV2:
        """
        Update a file's content

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        content : typing.Optional[str]
            File and val content. An empty string will create an empty file. When creating a directory, the content should be null or undefined.

        type : typing.Optional[FileContentUpdate2RequestType]

        parent_path : typing.Optional[str]
            Path to the directory you'd like to move this file to (e.g. 'folder1/folder2')

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileRevisionMetadataV2
            A File or Directory's Metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.file_content_update2(
            val_id="val_id",
            path="path",
        )
        """
        _response = self._raw_client.file_content_update2(
            val_id,
            path=path,
            branch_id=branch_id,
            content=content,
            type=type,
            parent_path=parent_path,
            name=name,
            request_options=request_options,
        )
        return _response.data

    def files_delete2(
        self,
        val_id: str,
        *,
        path: str,
        recursive: bool,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a file or a directory. To delete a directory and all of its children, use the recursive flag. To delete all files, pass in an empty path and the recursive flag.

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        recursive : bool
            Whether to recursively act on all files in the project

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.files_delete2(
            val_id="val_id",
            path="path",
            recursive=True,
        )
        """
        _response = self._raw_client.files_delete2(
            val_id, path=path, recursive=recursive, branch_id=branch_id, request_options=request_options
        )
        return _response.data

    def files_content_get2(
        self,
        val_id: str,
        *,
        path: str,
        version: typing.Optional[int] = None,
        branch_id: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
        if_unmodified_since: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        if_modified_since: typing.Optional[str] = None,
        cache_control: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Download file content

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        version : typing.Optional[int]
            Specific branch version to query

        branch_id : typing.Optional[str]
            Id to query

        if_match : typing.Optional[str]

        if_unmodified_since : typing.Optional[str]

        if_none_match : typing.Optional[str]

        if_modified_since : typing.Optional[str]

        cache_control : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Contents of the file

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.vals.files_content_get2(
            val_id="val_id",
            path="path",
        )
        """
        with self._raw_client.files_content_get2(
            val_id,
            path=path,
            version=version,
            branch_id=branch_id,
            if_match=if_match,
            if_unmodified_since=if_unmodified_since,
            if_none_match=if_none_match,
            if_modified_since=if_modified_since,
            cache_control=cache_control,
            request_options=request_options,
        ) as r:
            yield from r.data


class AsyncValsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawValsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawValsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawValsClient
        """
        return self._raw_client

    async def val_environment_variables_list(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ValEnvironmentVariablesListResponse:
        """
        List environment variables defined in this project. This only includes names, not values.

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValEnvironmentVariablesListResponse
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.val_environment_variables_list(
                val_id="val_id",
                offset=1,
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.val_environment_variables_list(
            val_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def val_environment_variables_create(
        self,
        val_id: str,
        *,
        value: str,
        key: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TEnvironmentVariable:
        """
        Create a new environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        value : str
            Value of the environment variable.

        key : str
            Name or key of the environment variable, accessible via Deno.env or process.env

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TEnvironmentVariable
            An environment variable

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.val_environment_variables_create(
                val_id="val_id",
                value="value",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.val_environment_variables_create(
            val_id, value=value, key=key, description=description, request_options=request_options
        )
        return _response.data

    async def val_environment_variables_update(
        self,
        val_id: str,
        key: str,
        *,
        value: str,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TEnvironmentVariable:
        """
        Update a environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        key : str

        value : str
            Value of the environment variable.

        description : typing.Optional[str]
            Optional description of the environment variable. Send null to clear an existing description; omit it to leave the description unchanged.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TEnvironmentVariable
            An environment variable

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.val_environment_variables_update(
                val_id="val_id",
                key="key",
                value="value",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.val_environment_variables_update(
            val_id, key, value=value, description=description, request_options=request_options
        )
        return _response.data

    async def val_environment_variables_delete(
        self, val_id: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a environment variable scoped to this project.

        Parameters
        ----------
        val_id : str
            Id of a val

        key : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.val_environment_variables_delete(
                val_id="val_id",
                key="key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.val_environment_variables_delete(
            val_id, key, request_options=request_options
        )
        return _response.data

    async def val_environment_variable_groups_list(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> ValEnvironmentVariableGroupsListResponse:
        """
        List the environment variable groups attached to this val. This only includes the groups, not the variables in them.

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValEnvironmentVariableGroupsListResponse
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.val_environment_variable_groups_list(
                val_id="val_id",
                offset=1,
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.val_environment_variable_groups_list(
            val_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def val_environment_variable_groups_attach(
        self, val_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Attach an environment variable group to this val. Every variable in the group is injected into the val's environment. Variables defined on the val itself take precedence over variables with the same key in a group. Attaching a group that is already attached succeeds without doing anything.

        Parameters
        ----------
        val_id : str
            Id of a val

        group_id : str
            Id of an environment variable group

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.val_environment_variable_groups_attach(
                val_id="val_id",
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.val_environment_variable_groups_attach(
            val_id, group_id, request_options=request_options
        )
        return _response.data

    async def val_environment_variable_groups_detach(
        self, val_id: str, group_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Detach an environment variable group from this val. The group itself, and the variables in it, are left alone.

        Parameters
        ----------
        val_id : str
            Id of a val

        group_id : str
            Id of an environment variable group

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.val_environment_variable_groups_detach(
                val_id="val_id",
                group_id="group_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.val_environment_variable_groups_detach(
            val_id, group_id, request_options=request_options
        )
        return _response.data

    async def vals_get2(self, val_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Val:
        """
        Get a val by id

        Parameters
        ----------
        val_id : str
            Id of a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Val
            A Val

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.vals_get2(
                val_id="val_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vals_get2(val_id, request_options=request_options)
        return _response.data

    async def projects_delete2(self, val_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Delete a project

        Parameters
        ----------
        val_id : str
            Id of a val

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.projects_delete2(
                val_id="val_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.projects_delete2(val_id, request_options=request_options)
        return _response.data

    async def vals_list2(
        self,
        *,
        limit: int,
        privacy: typing.Optional[ValsList2RequestPrivacy] = None,
        user_id: typing.Optional[str] = None,
        cursor: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValsList2Response:
        """
        Lists all vals including all public vals and your unlisted and private vals

        Parameters
        ----------
        limit : int
            Maximum items to return in each paginated response

        privacy : typing.Optional[ValsList2RequestPrivacy]
            This resource's privacy setting. Unlisted resources do not appear on profile pages or elsewhere, but you can link to them.

        user_id : typing.Optional[str]
            User ID to filter by

        cursor : typing.Optional[dt.datetime]
            Cursor to start the pagination from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValsList2Response
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.vals_list2(
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vals_list2(
            limit=limit, privacy=privacy, user_id=user_id, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def vals_create2(
        self,
        *,
        name: str,
        privacy: ValsCreate2RequestPrivacy,
        description: typing.Optional[str] = OMIT,
        org_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Val:
        """
        Create a new val

        Parameters
        ----------
        name : str

        privacy : ValsCreate2RequestPrivacy

        description : typing.Optional[str]

        org_id : typing.Optional[str]
            ID of the org to create the val in

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Val
            A Val

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.vals_create2(
                name="myVal",
                description="My val",
                privacy="public",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.vals_create2(
            name=name, privacy=privacy, description=description, org_id=org_id, request_options=request_options
        )
        return _response.data

    async def branches_get2(
        self, val_id: str, branch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Branch:
        """
        Get a branch by id

        Parameters
        ----------
        val_id : str
            Id of a val

        branch_id : str
            Id of a branch

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Branch
            A Branch

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.branches_get2(
                val_id="val_id",
                branch_id="branch_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.branches_get2(val_id, branch_id, request_options=request_options)
        return _response.data

    async def branches_delete2(
        self, val_id: str, branch_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a branch

        Parameters
        ----------
        val_id : str
            Id of a val

        branch_id : str
            Id of a branch

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.branches_delete2(
                val_id="val_id",
                branch_id="branch_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.branches_delete2(val_id, branch_id, request_options=request_options)
        return _response.data

    async def branches_list2(
        self, val_id: str, *, offset: int, limit: int, request_options: typing.Optional[RequestOptions] = None
    ) -> BranchesList2Response:
        """
        List all branches for a val

        Parameters
        ----------
        val_id : str
            Id of a val

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchesList2Response
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.branches_list2(
                val_id="val_id",
                offset=1,
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.branches_list2(
            val_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def branches_create2(
        self,
        val_id: str,
        *,
        name: str,
        branch_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Branch:
        """
        Create a new branch

        Parameters
        ----------
        val_id : str
            Id of a val

        name : str

        branch_id : typing.Optional[str]
            The branch ID to fork from. If this is not specified, the new branch will be forked from main.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Branch
            A Branch

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.branches_create2(
                val_id="val_id",
                name="my-branch",
                branch_id="00000000-0000-0000-0000-000000000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.branches_create2(
            val_id, name=name, branch_id=branch_id, request_options=request_options
        )
        return _response.data

    async def val_files_get2(
        self,
        val_id: str,
        *,
        path: str,
        recursive: bool,
        offset: int,
        limit: int,
        version: typing.Optional[int] = None,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValFilesGet2Response:
        """
        Get metadata for files and directories in a val. If path is an empty string, returns files at the root directory.

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        recursive : bool
            Whether to recursively act on all files in the project

        offset : int
            Number of items to skip in order to deliver paginated results

        limit : int
            Maximum items to return in each paginated response

        version : typing.Optional[int]
            Specific branch version to query

        branch_id : typing.Optional[str]
            Id to query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValFilesGet2Response
            A paginated result set

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.val_files_get2(
                val_id="val_id",
                path="path",
                recursive=True,
                offset=1,
                limit=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.val_files_get2(
            val_id,
            path=path,
            recursive=recursive,
            offset=offset,
            limit=limit,
            version=version,
            branch_id=branch_id,
            request_options=request_options,
        )
        return _response.data

    async def files_create2(
        self,
        val_id: str,
        *,
        path: str,
        request: FilesCreate2RequestBody,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileRevisionMetadataV2:
        """
        Create a new file, project val or directory

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        request : FilesCreate2RequestBody

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileRevisionMetadataV2
            A File or Directory's Metadata

        Examples
        --------
        import asyncio

        from fern.vals import FilesCreate2RequestBodyZero

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.files_create2(
                val_id="val_id",
                path="path",
                request=FilesCreate2RequestBodyZero(
                    type="directory",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.files_create2(
            val_id, path=path, request=request, branch_id=branch_id, request_options=request_options
        )
        return _response.data

    async def file_content_update2(
        self,
        val_id: str,
        *,
        path: str,
        branch_id: typing.Optional[str] = None,
        content: typing.Optional[str] = OMIT,
        type: typing.Optional[FileContentUpdate2RequestType] = OMIT,
        parent_path: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileRevisionMetadataV2:
        """
        Update a file's content

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

        content : typing.Optional[str]
            File and val content. An empty string will create an empty file. When creating a directory, the content should be null or undefined.

        type : typing.Optional[FileContentUpdate2RequestType]

        parent_path : typing.Optional[str]
            Path to the directory you'd like to move this file to (e.g. 'folder1/folder2')

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileRevisionMetadataV2
            A File or Directory's Metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.file_content_update2(
                val_id="val_id",
                path="path",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.file_content_update2(
            val_id,
            path=path,
            branch_id=branch_id,
            content=content,
            type=type,
            parent_path=parent_path,
            name=name,
            request_options=request_options,
        )
        return _response.data

    async def files_delete2(
        self,
        val_id: str,
        *,
        path: str,
        recursive: bool,
        branch_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes a file or a directory. To delete a directory and all of its children, use the recursive flag. To delete all files, pass in an empty path and the recursive flag.

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        recursive : bool
            Whether to recursively act on all files in the project

        branch_id : typing.Optional[str]
            The specified branch of the resource. Defaults to main if not provided.

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.files_delete2(
                val_id="val_id",
                path="path",
                recursive=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.files_delete2(
            val_id, path=path, recursive=recursive, branch_id=branch_id, request_options=request_options
        )
        return _response.data

    async def files_content_get2(
        self,
        val_id: str,
        *,
        path: str,
        version: typing.Optional[int] = None,
        branch_id: typing.Optional[str] = None,
        if_match: typing.Optional[str] = None,
        if_unmodified_since: typing.Optional[str] = None,
        if_none_match: typing.Optional[str] = None,
        if_modified_since: typing.Optional[str] = None,
        cache_control: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Download file content

        Parameters
        ----------
        val_id : str
            Id of a val

        path : str
            Path to a file or directory (e.g. 'dir/subdir/file.ts'). Pass in an empty string to represent the root directory.

        version : typing.Optional[int]
            Specific branch version to query

        branch_id : typing.Optional[str]
            Id to query

        if_match : typing.Optional[str]

        if_unmodified_since : typing.Optional[str]

        if_none_match : typing.Optional[str]

        if_modified_since : typing.Optional[str]

        cache_control : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Contents of the file

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.vals.files_content_get2(
                val_id="val_id",
                path="path",
            )


        asyncio.run(main())
        """
        async with self._raw_client.files_content_get2(
            val_id,
            path=path,
            version=version,
            branch_id=branch_id,
            if_match=if_match,
            if_unmodified_since=if_unmodified_since,
            if_none_match=if_none_match,
            if_modified_since=if_modified_since,
            cache_control=cache_control,
            request_options=request_options,
        ) as r:
            async for _chunk in r.data:
                yield _chunk
