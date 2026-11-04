

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.list_profiles_response import ListProfilesResponse
from ..types.update_info import UpdateInfo
from .raw_client import AsyncRawProfilesClient, RawProfilesClient


class ProfilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProfilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProfilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProfilesClient
        """
        return self._raw_client

    def list_all_available_client_profiles(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListProfilesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProfilesResponse
            Profile list.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.list_all_available_client_profiles()
        """
        _response = self._raw_client.list_all_available_client_profiles(request_options=request_options)
        return _response.data

    def fetch_hashed_directory_update_info_for_a_named_directory_of_a_profile(
        self, profile_uuid: str, dir_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateInfo:
        """
        Parameters
        ----------
        profile_uuid : str

        dir_name : str
            Directory name, e.g. "client" or "assets".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateInfo
            Update info including HashedDir and base download URL.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.profiles.fetch_hashed_directory_update_info_for_a_named_directory_of_a_profile(
            profile_uuid="profileUuid",
            dir_name="dirName",
        )
        """
        _response = self._raw_client.fetch_hashed_directory_update_info_for_a_named_directory_of_a_profile(
            profile_uuid, dir_name, request_options=request_options
        )
        return _response.data


class AsyncProfilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProfilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProfilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProfilesClient
        """
        return self._raw_client

    async def list_all_available_client_profiles(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListProfilesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListProfilesResponse
            Profile list.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.list_all_available_client_profiles()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_all_available_client_profiles(request_options=request_options)
        return _response.data

    async def fetch_hashed_directory_update_info_for_a_named_directory_of_a_profile(
        self, profile_uuid: str, dir_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdateInfo:
        """
        Parameters
        ----------
        profile_uuid : str

        dir_name : str
            Directory name, e.g. "client" or "assets".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateInfo
            Update info including HashedDir and base download URL.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.profiles.fetch_hashed_directory_update_info_for_a_named_directory_of_a_profile(
                profile_uuid="profileUuid",
                dir_name="dirName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_hashed_directory_update_info_for_a_named_directory_of_a_profile(
            profile_uuid, dir_name, request_options=request_options
        )
        return _response.data
