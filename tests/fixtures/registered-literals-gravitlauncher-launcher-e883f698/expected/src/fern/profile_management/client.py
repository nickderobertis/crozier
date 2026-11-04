

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.client_profile import ClientProfile
from ..types.completed_profile import CompletedProfile
from ..types.file_upload_response import FileUploadResponse
from ..types.hashed_dir import HashedDir
from ..types.uncompleted_profile import UncompletedProfile
from .raw_client import AsyncRawProfileManagementClient, RawProfileManagementClient


OMIT = typing.cast(typing.Any, ...)


class ProfileManagementClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProfileManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProfileManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProfileManagementClient
        """
        return self._raw_client

    def create_a_new_profile(
        self,
        *,
        name: str,
        profile: ClientProfile,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UncompletedProfile:
        """
        Parameters
        ----------
        name : str

        profile : ClientProfile

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UncompletedProfile
            The newly created uncompleted profile.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profile_management.create_a_new_profile(
            name="name",
            profile={"key": "value"},
        )
        """
        _response = self._raw_client.create_a_new_profile(
            name=name, profile=profile, description=description, request_options=request_options
        )
        return _response.data

    def get_a_completed_profile_by_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CompletedProfile:
        """
        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompletedProfile
            Completed profile.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profile_management.get_a_completed_profile_by_uuid(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.get_a_completed_profile_by_uuid(uuid_, request_options=request_options)
        return _response.data

    def delete_a_profile_by_uuid(self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        uuid_ : str

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
        client.profile_management.delete_a_profile_by_uuid(
            uuid_="uuid",
        )
        """
        _response = self._raw_client.delete_a_profile_by_uuid(uuid_, request_options=request_options)
        return _response.data

    def push_updated_client_profile_client_dir_and_asset_dir_for_a_profile(
        self,
        uuid_: str,
        *,
        profile: ClientProfile,
        client_dir: HashedDir,
        asset_dir: HashedDir,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompletedProfile:
        """
        Parameters
        ----------
        uuid_ : str

        profile : ClientProfile

        client_dir : HashedDir

        asset_dir : HashedDir

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompletedProfile
            Updated completed profile.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profile_management.push_updated_client_profile_client_dir_and_asset_dir_for_a_profile(
            uuid_="uuid",
            profile={"key": "value"},
            client_dir={"key": "value"},
            asset_dir={"key": "value"},
        )
        """
        _response = self._raw_client.push_updated_client_profile_client_dir_and_asset_dir_for_a_profile(
            uuid_, profile=profile, client_dir=client_dir, asset_dir=asset_dir, request_options=request_options
        )
        return _response.data

    def get_a_completed_profile_by_name(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CompletedProfile:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompletedProfile
            Completed profile.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profile_management.get_a_completed_profile_by_name(
            name="name",
        )
        """
        _response = self._raw_client.get_a_completed_profile_by_name(name, request_options=request_options)
        return _response.data

    def fetch_a_hashed_dir_for_a_named_directory_that_is_not_yet_associated_with_any_profile_ega_default_assets_directory(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HashedDir:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HashedDir
            HashedDir for the requested unconnected directory.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profile_management.fetch_a_hashed_dir_for_a_named_directory_that_is_not_yet_associated_with_any_profile_ega_default_assets_directory(
            name="name",
        )
        """
        _response = self._raw_client.fetch_a_hashed_dir_for_a_named_directory_that_is_not_yet_associated_with_any_profile_ega_default_assets_directory(
            name, request_options=request_options
        )
        return _response.data

    def upload_an_arbitrary_file_and_receive_a_url_reference_back_used_internally_by_push_update_to_stage_individual_files_before_committing_a_profile_update(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileUploadResponse:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileUploadResponse
            URL where the uploaded file is now available.
        """
        _response = self._raw_client.upload_an_arbitrary_file_and_receive_a_url_reference_back_used_internally_by_push_update_to_stage_individual_files_before_committing_a_profile_update(
            request=request, request_options=request_options
        )
        return _response.data


class AsyncProfileManagementClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProfileManagementClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProfileManagementClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProfileManagementClient
        """
        return self._raw_client

    async def create_a_new_profile(
        self,
        *,
        name: str,
        profile: ClientProfile,
        description: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UncompletedProfile:
        """
        Parameters
        ----------
        name : str

        profile : ClientProfile

        description : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UncompletedProfile
            The newly created uncompleted profile.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profile_management.create_a_new_profile(
                name="name",
                profile={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_profile(
            name=name, profile=profile, description=description, request_options=request_options
        )
        return _response.data

    async def get_a_completed_profile_by_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CompletedProfile:
        """
        Parameters
        ----------
        uuid_ : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompletedProfile
            Completed profile.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profile_management.get_a_completed_profile_by_uuid(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_completed_profile_by_uuid(uuid_, request_options=request_options)
        return _response.data

    async def delete_a_profile_by_uuid(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        uuid_ : str

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
            await client.profile_management.delete_a_profile_by_uuid(
                uuid_="uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_a_profile_by_uuid(uuid_, request_options=request_options)
        return _response.data

    async def push_updated_client_profile_client_dir_and_asset_dir_for_a_profile(
        self,
        uuid_: str,
        *,
        profile: ClientProfile,
        client_dir: HashedDir,
        asset_dir: HashedDir,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompletedProfile:
        """
        Parameters
        ----------
        uuid_ : str

        profile : ClientProfile

        client_dir : HashedDir

        asset_dir : HashedDir

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompletedProfile
            Updated completed profile.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profile_management.push_updated_client_profile_client_dir_and_asset_dir_for_a_profile(
                uuid_="uuid",
                profile={"key": "value"},
                client_dir={"key": "value"},
                asset_dir={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.push_updated_client_profile_client_dir_and_asset_dir_for_a_profile(
            uuid_, profile=profile, client_dir=client_dir, asset_dir=asset_dir, request_options=request_options
        )
        return _response.data

    async def get_a_completed_profile_by_name(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CompletedProfile:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompletedProfile
            Completed profile.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profile_management.get_a_completed_profile_by_name(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_completed_profile_by_name(name, request_options=request_options)
        return _response.data

    async def fetch_a_hashed_dir_for_a_named_directory_that_is_not_yet_associated_with_any_profile_ega_default_assets_directory(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HashedDir:
        """
        Parameters
        ----------
        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HashedDir
            HashedDir for the requested unconnected directory.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profile_management.fetch_a_hashed_dir_for_a_named_directory_that_is_not_yet_associated_with_any_profile_ega_default_assets_directory(
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_a_hashed_dir_for_a_named_directory_that_is_not_yet_associated_with_any_profile_ega_default_assets_directory(
            name, request_options=request_options
        )
        return _response.data

    async def upload_an_arbitrary_file_and_receive_a_url_reference_back_used_internally_by_push_update_to_stage_individual_files_before_committing_a_profile_update(
        self,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> FileUploadResponse:
        """
        Parameters
        ----------
        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileUploadResponse
            URL where the uploaded file is now available.
        """
        _response = await self._raw_client.upload_an_arbitrary_file_and_receive_a_url_reference_back_used_internally_by_push_update_to_stage_individual_files_before_committing_a_profile_update(
            request=request, request_options=request_options
        )
        return _response.data
