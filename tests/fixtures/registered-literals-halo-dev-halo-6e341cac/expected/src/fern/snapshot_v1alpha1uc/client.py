

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.snapshot import Snapshot
from .raw_client import AsyncRawSnapshotV1Alpha1UcClient, RawSnapshotV1Alpha1UcClient


class SnapshotV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSnapshotV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSnapshotV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSnapshotV1Alpha1UcClient
        """
        return self._raw_client

    def get_snapshot_for_post(
        self,
        name: str,
        *,
        post_name: str,
        patched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Get a content snapshot for a post owned by the current user. The snapshot must belong to the post specified by postName.

        Parameters
        ----------
        name : str
            metadata.name of the snapshot to fetch.

        post_name : str
            metadata.name of the post that owns the snapshot. The post must belong to the current user.

        patched : typing.Optional[bool]
            Whether to return the snapshot patched against the post base snapshot. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.snapshot_v1alpha1uc.get_snapshot_for_post(
            name="name",
            post_name="postName",
        )
        """
        _response = self._raw_client.get_snapshot_for_post(
            name, post_name=post_name, patched=patched, request_options=request_options
        )
        return _response.data


class AsyncSnapshotV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSnapshotV1Alpha1UcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSnapshotV1Alpha1UcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSnapshotV1Alpha1UcClient
        """
        return self._raw_client

    async def get_snapshot_for_post(
        self,
        name: str,
        *,
        post_name: str,
        patched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Snapshot:
        """
        Get a content snapshot for a post owned by the current user. The snapshot must belong to the post specified by postName.

        Parameters
        ----------
        name : str
            metadata.name of the snapshot to fetch.

        post_name : str
            metadata.name of the post that owns the snapshot. The post must belong to the current user.

        patched : typing.Optional[bool]
            Whether to return the snapshot patched against the post base snapshot. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Snapshot
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.snapshot_v1alpha1uc.get_snapshot_for_post(
                name="name",
                post_name="postName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_snapshot_for_post(
            name, post_name=post_name, patched=patched, request_options=request_options
        )
        return _response.data
