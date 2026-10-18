

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.storage_config_response_output import StorageConfigResponseOutput
from ..types.v1storage_bucket_response_output import V1StorageBucketResponseOutput
from .raw_client import AsyncRawStorageClient, RawStorageClient
from .types.update_storage_config_body_external import UpdateStorageConfigBodyExternal
from .types.update_storage_config_body_features import UpdateStorageConfigBodyFeatures


OMIT = typing.cast(typing.Any, ...)


class StorageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStorageClient
        """
        return self._raw_client

    def v1list_all_buckets(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1StorageBucketResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1StorageBucketResponseOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.storage.v1list_all_buckets(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_all_buckets(ref, request_options=request_options)
        return _response.data

    def v1get_storage_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StorageConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.storage.v1get_storage_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_storage_config(ref, request_options=request_options)
        return _response.data

    def v1update_storage_config(
        self,
        ref: str,
        *,
        file_size_limit: typing.Optional[int] = OMIT,
        features: typing.Optional[UpdateStorageConfigBodyFeatures] = OMIT,
        external: typing.Optional[UpdateStorageConfigBodyExternal] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        file_size_limit : typing.Optional[int]

        features : typing.Optional[UpdateStorageConfigBodyFeatures]

        external : typing.Optional[UpdateStorageConfigBodyExternal]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.storage import (
            UpdateStorageConfigBodyFeatures,
            UpdateStorageConfigBodyFeaturesImageTransformation,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.storage.v1update_storage_config(
            ref="abcdefghijklmnopqrst",
            file_size_limit=10485760,
            features=UpdateStorageConfigBodyFeatures(
                image_transformation=UpdateStorageConfigBodyFeaturesImageTransformation(
                    enabled=True,
                ),
            ),
        )
        """
        _response = self._raw_client.v1update_storage_config(
            ref, file_size_limit=file_size_limit, features=features, external=external, request_options=request_options
        )
        return _response.data


class AsyncStorageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStorageClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStorageClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStorageClient
        """
        return self._raw_client

    async def v1list_all_buckets(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[V1StorageBucketResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[V1StorageBucketResponseOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.storage.v1list_all_buckets(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_buckets(ref, request_options=request_options)
        return _response.data

    async def v1get_storage_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> StorageConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        StorageConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.storage.v1get_storage_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_storage_config(ref, request_options=request_options)
        return _response.data

    async def v1update_storage_config(
        self,
        ref: str,
        *,
        file_size_limit: typing.Optional[int] = OMIT,
        features: typing.Optional[UpdateStorageConfigBodyFeatures] = OMIT,
        external: typing.Optional[UpdateStorageConfigBodyExternal] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        file_size_limit : typing.Optional[int]

        features : typing.Optional[UpdateStorageConfigBodyFeatures]

        external : typing.Optional[UpdateStorageConfigBodyExternal]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.storage import (
            UpdateStorageConfigBodyFeatures,
            UpdateStorageConfigBodyFeaturesImageTransformation,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.storage.v1update_storage_config(
                ref="abcdefghijklmnopqrst",
                file_size_limit=10485760,
                features=UpdateStorageConfigBodyFeatures(
                    image_transformation=UpdateStorageConfigBodyFeaturesImageTransformation(
                        enabled=True,
                    ),
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_storage_config(
            ref, file_size_limit=file_size_limit, features=features, external=external, request_options=request_options
        )
        return _response.data
