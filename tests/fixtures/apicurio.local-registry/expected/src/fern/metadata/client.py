

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact_id import ArtifactId
from ..types.artifact_meta_data import ArtifactMetaData
from ..types.artifact_owner import ArtifactOwner
from ..types.file_content import FileContent
from ..types.group_id import GroupId
from ..types.properties import Properties
from ..types.version import Version
from ..types.version_meta_data import VersionMetaData
from .raw_client import AsyncRawMetadataClient, RawMetadataClient


OMIT = typing.cast(typing.Any, ...)


class MetadataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawMetadataClient
        """
        return self._raw_client

    def get_artifact_meta_data(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtifactMetaData:
        """
        Gets the metadata for an artifact in the registry.  The returned metadata includes
        both generated (read-only) and editable metadata (such as name and description).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactMetaData
            The artifact's metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metadata.get_artifact_meta_data(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
        )
        """
        _response = self._raw_client.get_artifact_meta_data(group_id, artifact_id, request_options=request_options)
        return _response.data

    def get_artifact_version_meta_data_by_content(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        canonical: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VersionMetaData:
        """
        Gets the metadata for an artifact that matches the raw content.  Searches the registry
        for a version of the given artifact matching the content provided in the body of the
        POST.

        This operation can fail for the following reasons:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with the `artifactId` exists (HTTP error `404`)
        * No artifact version matching the provided content exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        canonical : typing.Optional[bool]
            Parameter that can be set to `true` to indicate that the server should "canonicalize" the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionMetaData
            The metadata of the artifact version matching the provided content.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metadata.get_artifact_version_meta_data_by_content(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            request="string",
        )
        """
        _response = self._raw_client.get_artifact_version_meta_data_by_content(
            group_id, artifact_id, request=request, canonical=canonical, request_options=request_options
        )
        return _response.data

    def update_artifact_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the editable parts of the artifact's metadata.  Not all metadata fields can
        be updated.  For example, `createdOn` and `createdBy` are both read-only properties.

        This operation can fail for the following reasons:

        * No artifact with the `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        description : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]


        name : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metadata.update_artifact_meta_data(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            description="The description of the artifact.",
            labels=["regional", "global"],
            name="Artifact Name",
            properties={"custom-1": "foo", "custom-2": "bar"},
        )
        """
        _response = self._raw_client.update_artifact_meta_data(
            group_id,
            artifact_id,
            description=description,
            labels=labels,
            name=name,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def get_artifact_owner(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtifactOwner:
        """
        Gets the owner of an artifact in the registry.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactOwner
            The artifact's owner.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metadata.get_artifact_owner(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
        )
        """
        _response = self._raw_client.get_artifact_owner(group_id, artifact_id, request_options=request_options)
        return _response.data

    def update_artifact_owner(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        owner: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Changes the ownership of an artifact.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        owner : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metadata.update_artifact_owner(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            owner="bwayne",
        )
        """
        _response = self._raw_client.update_artifact_owner(
            group_id, artifact_id, owner=owner, request_options=request_options
        )
        return _response.data

    def get_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VersionMetaData:
        """
        Retrieves the metadata for a single version of the artifact.  The version metadata is
        a subset of the artifact metadata and only includes the metadata that is specific to
        the version (for example, this doesn't include `modifiedOn`).

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
        VersionMetaData
            The artifact version's metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metadata.get_artifact_version_meta_data(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            version='"3.1.6"',
        )
        """
        _response = self._raw_client.get_artifact_version_meta_data(
            group_id, artifact_id, version, request_options=request_options
        )
        return _response.data

    def update_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the user-editable portion of the artifact version's metadata.  Only some of
        the metadata fields are editable by the user.  For example, `description` is editable,
        but `createdOn` is not.

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

        description : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]


        name : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metadata.update_artifact_version_meta_data(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            version='"3.1.6"',
            description="The description of the artifact.",
            labels=["regional", "global"],
            name="Artifact Name",
            properties={"custom-1": "foo", "custom-2": "bar"},
        )
        """
        _response = self._raw_client.update_artifact_version_meta_data(
            group_id,
            artifact_id,
            version,
            description=description,
            labels=labels,
            name=name,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    def delete_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes the user-editable metadata properties of the artifact version.  Any properties
        that are not user-editable are preserved.

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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.metadata.delete_artifact_version_meta_data(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            version='"3.1.6"',
        )
        """
        _response = self._raw_client.delete_artifact_version_meta_data(
            group_id, artifact_id, version, request_options=request_options
        )
        return _response.data


class AsyncMetadataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawMetadataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawMetadataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawMetadataClient
        """
        return self._raw_client

    async def get_artifact_meta_data(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtifactMetaData:
        """
        Gets the metadata for an artifact in the registry.  The returned metadata includes
        both generated (read-only) and editable metadata (such as name and description).

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactMetaData
            The artifact's metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metadata.get_artifact_meta_data(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact_meta_data(
            group_id, artifact_id, request_options=request_options
        )
        return _response.data

    async def get_artifact_version_meta_data_by_content(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        canonical: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VersionMetaData:
        """
        Gets the metadata for an artifact that matches the raw content.  Searches the registry
        for a version of the given artifact matching the content provided in the body of the
        POST.

        This operation can fail for the following reasons:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with the `artifactId` exists (HTTP error `404`)
        * No artifact version matching the provided content exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        canonical : typing.Optional[bool]
            Parameter that can be set to `true` to indicate that the server should "canonicalize" the content when searching for a matching version.  Canonicalization is unique to each artifact type, but typically involves removing any extra whitespace and formatting the content in a consistent manner.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        VersionMetaData
            The metadata of the artifact version matching the provided content.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metadata.get_artifact_version_meta_data_by_content(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact_version_meta_data_by_content(
            group_id, artifact_id, request=request, canonical=canonical, request_options=request_options
        )
        return _response.data

    async def update_artifact_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the editable parts of the artifact's metadata.  Not all metadata fields can
        be updated.  For example, `createdOn` and `createdBy` are both read-only properties.

        This operation can fail for the following reasons:

        * No artifact with the `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        description : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]


        name : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metadata.update_artifact_meta_data(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                description="The description of the artifact.",
                labels=["regional", "global"],
                name="Artifact Name",
                properties={"custom-1": "foo", "custom-2": "bar"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_artifact_meta_data(
            group_id,
            artifact_id,
            description=description,
            labels=labels,
            name=name,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def get_artifact_owner(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtifactOwner:
        """
        Gets the owner of an artifact in the registry.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactOwner
            The artifact's owner.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metadata.get_artifact_owner(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact_owner(group_id, artifact_id, request_options=request_options)
        return _response.data

    async def update_artifact_owner(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        owner: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Changes the ownership of an artifact.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        owner : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metadata.update_artifact_owner(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                owner="bwayne",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_artifact_owner(
            group_id, artifact_id, owner=owner, request_options=request_options
        )
        return _response.data

    async def get_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> VersionMetaData:
        """
        Retrieves the metadata for a single version of the artifact.  The version metadata is
        a subset of the artifact metadata and only includes the metadata that is specific to
        the version (for example, this doesn't include `modifiedOn`).

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
        VersionMetaData
            The artifact version's metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metadata.get_artifact_version_meta_data(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                version='"3.1.6"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact_version_meta_data(
            group_id, artifact_id, version, request_options=request_options
        )
        return _response.data

    async def update_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        description: typing.Optional[str] = OMIT,
        labels: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[Properties] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the user-editable portion of the artifact version's metadata.  Only some of
        the metadata fields are editable by the user.  For example, `description` is editable,
        but `createdOn` is not.

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

        description : typing.Optional[str]

        labels : typing.Optional[typing.Sequence[str]]


        name : typing.Optional[str]

        properties : typing.Optional[Properties]


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metadata.update_artifact_version_meta_data(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                version='"3.1.6"',
                description="The description of the artifact.",
                labels=["regional", "global"],
                name="Artifact Name",
                properties={"custom-1": "foo", "custom-2": "bar"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_artifact_version_meta_data(
            group_id,
            artifact_id,
            version,
            description=description,
            labels=labels,
            name=name,
            properties=properties,
            request_options=request_options,
        )
        return _response.data

    async def delete_artifact_version_meta_data(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        version: Version,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Deletes the user-editable metadata properties of the artifact version.  Any properties
        that are not user-editable are preserved.

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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.metadata.delete_artifact_version_meta_data(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                version='"3.1.6"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_artifact_version_meta_data(
            group_id, artifact_id, version, request_options=request_options
        )
        return _response.data
