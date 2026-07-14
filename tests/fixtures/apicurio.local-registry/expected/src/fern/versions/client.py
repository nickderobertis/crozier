

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact_description import ArtifactDescription
from ..types.artifact_id import ArtifactId
from ..types.artifact_name import ArtifactName
from ..types.artifact_reference import ArtifactReference
from ..types.artifact_state import ArtifactState
from ..types.encoded_artifact_description import EncodedArtifactDescription
from ..types.encoded_artifact_name import EncodedArtifactName
from ..types.file_content import FileContent
from ..types.group_id import GroupId
from ..types.version import Version
from ..types.version_meta_data import VersionMetaData
from ..types.version_search_results import VersionSearchResults
from .raw_client import AsyncRawVersionsClient, RawVersionsClient


OMIT = typing.cast(typing.Any, ...)


class VersionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVersionsClient
        """
        return self._raw_client

    def list_artifact_versions(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VersionSearchResults:
        """
        Returns a list of all versions of the artifact.  The result set is paged.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        offset : typing.Optional[int]
            The number of versions to skip before starting to collect the result set.  Defaults to 0.

        limit : typing.Optional[int]
            The number of versions to return.  Defaults to 20.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionSearchResults
            List of all artifact versions.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.versions.list_artifact_versions(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
        )
        """
        _response = self._raw_client.list_artifact_versions(
            group_id, artifact_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def create_artifact_version(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        registry_version: typing.Optional[Version] = None,
        registry_name: typing.Optional[ArtifactName] = None,
        registry_description: typing.Optional[ArtifactDescription] = None,
        registry_description_encoded: typing.Optional[EncodedArtifactDescription] = None,
        registry_name_encoded: typing.Optional[EncodedArtifactName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VersionMetaData:
        """
        Creates a new version of the artifact by uploading new content.  The configured rules for
        the artifact are applied, and if they all pass, the new content is added as the most recent
        version of the artifact.  If any of the rules fail, an error is returned.

        The body of the request can be the raw content of the new artifact version, or the raw content
        and a set of references pointing to other artifacts, and the type
        of that content should match the artifact's type (for example if the artifact type is `AVRO`
        then the content of the request should be an Apache Avro document).

        This operation can fail for the following reasons:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with this `artifactId` exists (HTTP error `404`)
        * The new content violates one of the rules configured for the artifact (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        registry_version : typing.Optional[Version]
            Specifies the version number of this new version of the artifact content.  This would typically
            be a simple integer or a SemVer value.  It must be unique within the artifact.  If this is not
            provided, the server will generate a new, unique version number for this new updated content.

        registry_name : typing.Optional[ArtifactName]
            Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not
            provided, the server will extract the name from the artifact content.

        registry_description : typing.Optional[ArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.

        registry_description_encoded : typing.Optional[EncodedArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.

        registry_name_encoded : typing.Optional[EncodedArtifactName]
            Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionMetaData
            The artifact version was successfully created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.versions.create_artifact_version(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            registry_version='"3.1.6"',
            registry_name='"Artifact name"',
            registry_description='"Artifact description"',
            registry_description_encoded='"QXJ0aWZhY3QgZGVzY3JpcHRpb24K"',
            registry_name_encoded='"QXJ0aWZhY3QgbmFtZQo="',
            request="string",
        )
        """
        _response = self._raw_client.create_artifact_version(
            group_id,
            artifact_id,
            request=request,
            registry_version=registry_version,
            registry_name=registry_name,
            registry_description=registry_description,
            registry_description_encoded=registry_description_encoded,
            registry_name_encoded=registry_name_encoded,
            request_options=request_options,
        )
        return _response.data

    def get_artifact_version(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Retrieves a single version of the artifact content.  Both the `artifactId` and the
        unique `version` number must be provided.  The `Content-Type` of the response depends
        on the artifact type.  In most cases, this is `application/json`, but for some types
        it may be different (for example, `PROTOBUF`).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        dereference : typing.Optional[bool]
            Allows the user to specify if the content should be dereferenced when being returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            The content of one version of one artifact.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.versions.get_artifact_version(
            group_id="groupId",
            artifact_id="artifactId",
            version="version",
        )
        """
        with self._raw_client.get_artifact_version(
            group_id, artifact_id, version, dereference=dereference, request_options=request_options
        ) as r:
            yield from r.data

    def get_artifact_version_references(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ArtifactReference]:
        """
        Retrieves a single version of the artifact content.  Both the `artifactId` and the
        unique `version` number must be provided.  The `Content-Type` of the response depends
        on the artifact type.  In most cases, this is `application/json`, but for some types
        it may be different (for example, `PROTOBUF`).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactReference]
            List of all the artifact references for this artifact.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.versions.get_artifact_version_references(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            version='"3.1.6"',
        )
        """
        _response = self._raw_client.get_artifact_version_references(
            group_id, artifact_id, version, request_options=request_options
        )
        return _response.data

    def update_artifact_version_state(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        state: ArtifactState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the state of a specific version of an artifact.  For example, you can use
        this operation to disable a specific version.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        state : ArtifactState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import ArtifactState, FernApi

        client = FernApi()
        client.versions.update_artifact_version_state(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            version='"3.1.6"',
            state=ArtifactState.DISABLED,
        )
        """
        _response = self._raw_client.update_artifact_version_state(
            group_id, artifact_id, version, state=state, request_options=request_options
        )
        return _response.data


class AsyncVersionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVersionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVersionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVersionsClient
        """
        return self._raw_client

    async def list_artifact_versions(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VersionSearchResults:
        """
        Returns a list of all versions of the artifact.  The result set is paged.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        offset : typing.Optional[int]
            The number of versions to skip before starting to collect the result set.  Defaults to 0.

        limit : typing.Optional[int]
            The number of versions to return.  Defaults to 20.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionSearchResults
            List of all artifact versions.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.versions.list_artifact_versions(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_artifact_versions(
            group_id, artifact_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def create_artifact_version(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        registry_version: typing.Optional[Version] = None,
        registry_name: typing.Optional[ArtifactName] = None,
        registry_description: typing.Optional[ArtifactDescription] = None,
        registry_description_encoded: typing.Optional[EncodedArtifactDescription] = None,
        registry_name_encoded: typing.Optional[EncodedArtifactName] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VersionMetaData:
        """
        Creates a new version of the artifact by uploading new content.  The configured rules for
        the artifact are applied, and if they all pass, the new content is added as the most recent
        version of the artifact.  If any of the rules fail, an error is returned.

        The body of the request can be the raw content of the new artifact version, or the raw content
        and a set of references pointing to other artifacts, and the type
        of that content should match the artifact's type (for example if the artifact type is `AVRO`
        then the content of the request should be an Apache Avro document).

        This operation can fail for the following reasons:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with this `artifactId` exists (HTTP error `404`)
        * The new content violates one of the rules configured for the artifact (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        registry_version : typing.Optional[Version]
            Specifies the version number of this new version of the artifact content.  This would typically
            be a simple integer or a SemVer value.  It must be unique within the artifact.  If this is not
            provided, the server will generate a new, unique version number for this new updated content.

        registry_name : typing.Optional[ArtifactName]
            Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not
            provided, the server will extract the name from the artifact content.

        registry_description : typing.Optional[ArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.

        registry_description_encoded : typing.Optional[EncodedArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.

        registry_name_encoded : typing.Optional[EncodedArtifactName]
            Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionMetaData
            The artifact version was successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.versions.create_artifact_version(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                registry_version='"3.1.6"',
                registry_name='"Artifact name"',
                registry_description='"Artifact description"',
                registry_description_encoded='"QXJ0aWZhY3QgZGVzY3JpcHRpb24K"',
                registry_name_encoded='"QXJ0aWZhY3QgbmFtZQo="',
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_artifact_version(
            group_id,
            artifact_id,
            request=request,
            registry_version=registry_version,
            registry_name=registry_name,
            registry_description=registry_description,
            registry_description_encoded=registry_description_encoded,
            registry_name_encoded=registry_name_encoded,
            request_options=request_options,
        )
        return _response.data

    async def get_artifact_version(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Retrieves a single version of the artifact content.  Both the `artifactId` and the
        unique `version` number must be provided.  The `Content-Type` of the response depends
        on the artifact type.  In most cases, this is `application/json`, but for some types
        it may be different (for example, `PROTOBUF`).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        dereference : typing.Optional[bool]
            Allows the user to specify if the content should be dereferenced when being returned

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            The content of one version of one artifact.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.versions.get_artifact_version(
                group_id="groupId",
                artifact_id="artifactId",
                version="version",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_artifact_version(
            group_id, artifact_id, version, dereference=dereference, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_artifact_version_references(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ArtifactReference]:
        """
        Retrieves a single version of the artifact content.  Both the `artifactId` and the
        unique `version` number must be provided.  The `Content-Type` of the response depends
        on the artifact type.  In most cases, this is `application/json`, but for some types
        it may be different (for example, `PROTOBUF`).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactReference]
            List of all the artifact references for this artifact.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.versions.get_artifact_version_references(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                version='"3.1.6"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact_version_references(
            group_id, artifact_id, version, request_options=request_options
        )
        return _response.data

    async def update_artifact_version_state(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        state: ArtifactState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the state of a specific version of an artifact.  For example, you can use
        this operation to disable a specific version.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No version with this `version` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        version : Version
            The unique identifier of a specific version of the artifact content.

        state : ArtifactState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import ArtifactState, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.versions.update_artifact_version_state(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                version='"3.1.6"',
                state=ArtifactState.DISABLED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_artifact_version_state(
            group_id, artifact_id, version, state=state, request_options=request_options
        )
        return _response.data
