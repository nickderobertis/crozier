

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact import Artifact
from ..types.artifact_dto_item import ArtifactDtoItem
from .raw_client import AsyncRawArtifactsClient, RawArtifactsClient


OMIT = typing.cast(typing.Any, ...)


class ArtifactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArtifactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArtifactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArtifactsClient
        """
        return self._raw_client

    def returns_all_artifacts(
        self,
        *,
        policy_id: typing.Optional[str] = None,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Artifact]:
        """
        Returns all artifacts.

        Parameters
        ----------
        policy_id : typing.Optional[str]
            Policy identifier

        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Artifact]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.artifacts.returns_all_artifacts()
        """
        _response = self._raw_client.returns_all_artifacts(
            policy_id=policy_id, page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    def artifact_api_upload_artifacts(
        self, parent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactDtoItem]:
        """
        Upload artifact. For users with the Standard Registry role only.

        Parameters
        ----------
        parent_id : str
            Parent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactDtoItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.artifacts.artifact_api_upload_artifacts(
            parent_id="parentId",
        )
        """
        _response = self._raw_client.artifact_api_upload_artifacts(parent_id, request_options=request_options)
        return _response.data

    def delete_artifact(self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        Delete artifact.

        Parameters
        ----------
        artifact_id : str
            Artifact identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.artifacts.delete_artifact(
            artifact_id="artifactId",
        )
        """
        _response = self._raw_client.delete_artifact(artifact_id, request_options=request_options)
        return _response.data

    def upload_artifact(
        self,
        policy_id: str,
        *,
        artifacts: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Artifact]:
        """
        Upload artifact. For users with the Standard Registry role only.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        artifacts : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Artifact]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.artifacts.upload_artifact(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.upload_artifact(policy_id, artifacts=artifacts, request_options=request_options)
        return _response.data


class AsyncArtifactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArtifactsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArtifactsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArtifactsClient
        """
        return self._raw_client

    async def returns_all_artifacts(
        self,
        *,
        policy_id: typing.Optional[str] = None,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Artifact]:
        """
        Returns all artifacts.

        Parameters
        ----------
        policy_id : typing.Optional[str]
            Policy identifier

        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Artifact]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.artifacts.returns_all_artifacts()


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_artifacts(
            policy_id=policy_id, page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def artifact_api_upload_artifacts(
        self, parent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactDtoItem]:
        """
        Upload artifact. For users with the Standard Registry role only.

        Parameters
        ----------
        parent_id : str
            Parent ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactDtoItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.artifacts.artifact_api_upload_artifacts(
                parent_id="parentId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.artifact_api_upload_artifacts(parent_id, request_options=request_options)
        return _response.data

    async def delete_artifact(
        self, artifact_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Delete artifact.

        Parameters
        ----------
        artifact_id : str
            Artifact identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.artifacts.delete_artifact(
                artifact_id="artifactId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_artifact(artifact_id, request_options=request_options)
        return _response.data

    async def upload_artifact(
        self,
        policy_id: str,
        *,
        artifacts: typing.Optional[typing.List[core.File]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Artifact]:
        """
        Upload artifact. For users with the Standard Registry role only.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        artifacts : typing.Optional[typing.List[core.File]]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Artifact]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.artifacts.upload_artifact(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_artifact(
            policy_id, artifacts=artifacts, request_options=request_options
        )
        return _response.data
