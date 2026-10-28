

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawOsamServiceClient, RawOsamServiceClient


class OsamServiceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOsamServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOsamServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOsamServiceClient
        """
        return self._raw_client

    def create_and_delete_obs_accounts(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        This endpoint is called by an RS operator with the *rs_osam_update* role.
        It triggers the synchronization of the creation and deletion of S3 Object Storage (OBS) accounts for all RS users,
        associated to their Keycloak account.

        How it works:

        1. When a new Keycloak user account is created, an associated OBS access account **with no rights** is created
        and linked to it.

        2. When a Keycloak user account is deleted, the associated OBS access account is also deleted.

        NOTE: to synchronize OBS user rights from Keycloak you then need to call the endpoint
        * /storage/account/{user}/update*.

        ### Returns:
        JSONResponse — Always a success message saying that the synchronization algorithm of the accounts started.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.osam_service.create_and_delete_obs_accounts()
        """
        _response = self._raw_client.create_and_delete_obs_accounts(request_options=request_options)
        return _response.data

    def update_obs_user_rights(
        self, user: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This endpoint is called by an RS operator with the *rs_osam_update* role. It updates the S3 Object Storage (OBS)
        rights of any user, calculated from their associated Keycloak account.

        When called, this endpoint will:

        1. Read the user's roles from their Keycloak account.

        2. Calculate the associated OBS access policy rights: they describe the buckets, paths, and permission levels
        (such as read, write and download) that the user has access to.

        3. Apply the access policy to the user's OBS account.

        The operation ensures that the user's OBS permissions match their Keycloak permissions.

        ### Args
        user (str) — The Keycloak username for which the access policy should be applied.

        ### Returns
        JSONResponse — A JSON response confirming that the access policy has been applied.

        ### Raises
        404 — If the user does not exist in Keycloak.<br>
        400 — If the policy could not be applied by the Object Storage provider.

        Parameters
        ----------
        user : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.osam_service.update_obs_user_rights(
            user="user",
        )
        """
        _response = self._raw_client.update_obs_user_rights(user, request_options=request_options)
        return _response.data

    def get_your_s3credentials(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        This endpoint is called by any anthenticated user.
        It returns your personnal S3 credentials, so you can connect to the bucket where your products have been generated.

        ### Returns
        dict — A dictionary containing 'access_key', 'secret_key', 'endpoint', 'region' for the user's S3 storage.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )
        client.osam_service.get_your_s3credentials()
        """
        _response = self._raw_client.get_your_s3credentials(request_options=request_options)
        return _response.data


class AsyncOsamServiceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOsamServiceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOsamServiceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOsamServiceClient
        """
        return self._raw_client

    async def create_and_delete_obs_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This endpoint is called by an RS operator with the *rs_osam_update* role.
        It triggers the synchronization of the creation and deletion of S3 Object Storage (OBS) accounts for all RS users,
        associated to their Keycloak account.

        How it works:

        1. When a new Keycloak user account is created, an associated OBS access account **with no rights** is created
        and linked to it.

        2. When a Keycloak user account is deleted, the associated OBS access account is also deleted.

        NOTE: to synchronize OBS user rights from Keycloak you then need to call the endpoint
        * /storage/account/{user}/update*.

        ### Returns:
        JSONResponse — Always a success message saying that the synchronization algorithm of the accounts started.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.osam_service.create_and_delete_obs_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_and_delete_obs_accounts(request_options=request_options)
        return _response.data

    async def update_obs_user_rights(
        self, user: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        This endpoint is called by an RS operator with the *rs_osam_update* role. It updates the S3 Object Storage (OBS)
        rights of any user, calculated from their associated Keycloak account.

        When called, this endpoint will:

        1. Read the user's roles from their Keycloak account.

        2. Calculate the associated OBS access policy rights: they describe the buckets, paths, and permission levels
        (such as read, write and download) that the user has access to.

        3. Apply the access policy to the user's OBS account.

        The operation ensures that the user's OBS permissions match their Keycloak permissions.

        ### Args
        user (str) — The Keycloak username for which the access policy should be applied.

        ### Returns
        JSONResponse — A JSON response confirming that the access policy has been applied.

        ### Raises
        404 — If the user does not exist in Keycloak.<br>
        400 — If the policy could not be applied by the Object Storage provider.

        Parameters
        ----------
        user : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.osam_service.update_obs_user_rights(
                user="user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_obs_user_rights(user, request_options=request_options)
        return _response.data

    async def get_your_s3credentials(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        This endpoint is called by any anthenticated user.
        It returns your personnal S3 credentials, so you can connect to the bucket where your products have been generated.

        ### Returns
        dict — A dictionary containing 'access_key', 'secret_key', 'endpoint', 'region' for the user's S3 storage.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.osam_service.get_your_s3credentials()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_your_s3credentials(request_options=request_options)
        return _response.data
