

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.build_secrets import BuildSecrets
from ..types.launcher_update_info import LauncherUpdateInfo
from ..types.updates_prepare_response import UpdatesPrepareResponse
from .raw_client import AsyncRawUpdatesClient, RawUpdatesClient
from .types.post_updates_check_variant_request_variant import PostUpdatesCheckVariantRequestVariant
from .types.post_updates_upload_variant_request_variant import PostUpdatesUploadVariantRequestVariant


OMIT = typing.cast(typing.Any, ...)


class UpdatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUpdatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUpdatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUpdatesClient
        """
        return self._raw_client

    def begin_the_launcher_self_update_challenge_response_flow_returns_a_random_blob_the_client_must_sign_with_its_build_private_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdatesPrepareResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatesPrepareResponse
            Challenge data.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.updates.begin_the_launcher_self_update_challenge_response_flow_returns_a_random_blob_the_client_must_sign_with_its_build_private_key()
        """
        _response = self._raw_client.begin_the_launcher_self_update_challenge_response_flow_returns_a_random_blob_the_client_must_sign_with_its_build_private_key(
            request_options=request_options
        )
        return _response.data

    def submit_the_signed_challenge_to_verify_the_build_identity_and_receive_update_information(
        self,
        variant: PostUpdatesCheckVariantRequestVariant,
        *,
        signed_data: str,
        public_key: str,
        jwt_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LauncherUpdateInfo:
        """
        Parameters
        ----------
        variant : PostUpdatesCheckVariantRequestVariant
            Update variant — identifies the target platform/binary.

        signed_data : str
            Base64-encoded ECDSA signature over the challenge data.

        public_key : str
            Base64-encoded DER-encoded ECDSA public key.

        jwt_token : str
            Token received from /updates/prepare.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LauncherUpdateInfo
            Update info for the launcher itself.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.updates.submit_the_signed_challenge_to_verify_the_build_identity_and_receive_update_information(
            variant="JAR",
            signed_data="signedData",
            public_key="publicKey",
            jwt_token="jwtToken",
        )
        """
        _response = (
            self._raw_client.submit_the_signed_challenge_to_verify_the_build_identity_and_receive_update_information(
                variant,
                signed_data=signed_data,
                public_key=public_key,
                jwt_token=jwt_token,
                request_options=request_options,
            )
        )
        return _response.data

    def upload_a_game_asset_update_file_admin_server_side_use(
        self,
        variant: PostUpdatesUploadVariantRequestVariant,
        *,
        secrets: BuildSecrets,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        variant : PostUpdatesUploadVariantRequestVariant
            Update variant — identifies the target platform/binary.

        secrets : BuildSecrets
            JSON-serialised BuildSecrets object (privateKey, publicKey).

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import BuildSecrets, FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.updates.upload_a_game_asset_update_file_admin_server_side_use(
            variant="JAR",
            secrets=BuildSecrets(
                private_key="privateKey",
                public_key="publicKey",
            ),
        )
        """
        _response = self._raw_client.upload_a_game_asset_update_file_admin_server_side_use(
            variant, secrets=secrets, file=file, request_options=request_options
        )
        return _response.data


class AsyncUpdatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUpdatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUpdatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUpdatesClient
        """
        return self._raw_client

    async def begin_the_launcher_self_update_challenge_response_flow_returns_a_random_blob_the_client_must_sign_with_its_build_private_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> UpdatesPrepareResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdatesPrepareResponse
            Challenge data.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.updates.begin_the_launcher_self_update_challenge_response_flow_returns_a_random_blob_the_client_must_sign_with_its_build_private_key()


        asyncio.run(main())
        """
        _response = await self._raw_client.begin_the_launcher_self_update_challenge_response_flow_returns_a_random_blob_the_client_must_sign_with_its_build_private_key(
            request_options=request_options
        )
        return _response.data

    async def submit_the_signed_challenge_to_verify_the_build_identity_and_receive_update_information(
        self,
        variant: PostUpdatesCheckVariantRequestVariant,
        *,
        signed_data: str,
        public_key: str,
        jwt_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> LauncherUpdateInfo:
        """
        Parameters
        ----------
        variant : PostUpdatesCheckVariantRequestVariant
            Update variant — identifies the target platform/binary.

        signed_data : str
            Base64-encoded ECDSA signature over the challenge data.

        public_key : str
            Base64-encoded DER-encoded ECDSA public key.

        jwt_token : str
            Token received from /updates/prepare.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        LauncherUpdateInfo
            Update info for the launcher itself.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.updates.submit_the_signed_challenge_to_verify_the_build_identity_and_receive_update_information(
                variant="JAR",
                signed_data="signedData",
                public_key="publicKey",
                jwt_token="jwtToken",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_the_signed_challenge_to_verify_the_build_identity_and_receive_update_information(
            variant,
            signed_data=signed_data,
            public_key=public_key,
            jwt_token=jwt_token,
            request_options=request_options,
        )
        return _response.data

    async def upload_a_game_asset_update_file_admin_server_side_use(
        self,
        variant: PostUpdatesUploadVariantRequestVariant,
        *,
        secrets: BuildSecrets,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        variant : PostUpdatesUploadVariantRequestVariant
            Update variant — identifies the target platform/binary.

        secrets : BuildSecrets
            JSON-serialised BuildSecrets object (privateKey, publicKey).

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BuildSecrets

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.updates.upload_a_game_asset_update_file_admin_server_side_use(
                variant="JAR",
                secrets=BuildSecrets(
                    private_key="privateKey",
                    public_key="publicKey",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_a_game_asset_update_file_admin_server_side_use(
            variant, secrets=secrets, file=file, request_options=request_options
        )
        return _response.data
