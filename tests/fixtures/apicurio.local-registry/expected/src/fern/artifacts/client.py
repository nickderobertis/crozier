

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact_description import ArtifactDescription
from ..types.artifact_id import ArtifactId
from ..types.artifact_meta_data import ArtifactMetaData
from ..types.artifact_name import ArtifactName
from ..types.artifact_reference import ArtifactReference
from ..types.artifact_search_results import ArtifactSearchResults
from ..types.artifact_state import ArtifactState
from ..types.artifact_type import ArtifactType
from ..types.encoded_artifact_description import EncodedArtifactDescription
from ..types.encoded_artifact_name import EncodedArtifactName
from ..types.file_content import FileContent
from ..types.group_id import GroupId
from ..types.if_exists import IfExists
from ..types.sort_by import SortBy
from ..types.sort_order import SortOrder
from ..types.version import Version
from .raw_client import AsyncRawArtifactsClient, RawArtifactsClient
from .types.create_artifact_request_x_registry_hash_algorithm import CreateArtifactRequestXRegistryHashAlgorithm


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

    def list_artifacts_in_group(
        self,
        group_id: GroupId,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtifactSearchResults:
        """
        Returns a list of all artifacts in the group.  This list is paged.

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        limit : typing.Optional[int]
            The number of artifacts to return.  Defaults to 20.

        offset : typing.Optional[int]
            The number of artifacts to skip before starting the result set.  Defaults to 0.

        order : typing.Optional[SortOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SortBy]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactSearchResults
            On a successful response, returns a bounded set of artifacts.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifacts.list_artifacts_in_group(
            group_id='"my-group"',
        )
        """
        _response = self._raw_client.list_artifacts_in_group(
            group_id, limit=limit, offset=offset, order=order, orderby=orderby, request_options=request_options
        )
        return _response.data

    def create_artifact(
        self,
        group_id: GroupId,
        *,
        request: FileContent,
        if_exists: typing.Optional[IfExists] = None,
        canonical: typing.Optional[bool] = None,
        registry_artifact_type: typing.Optional[ArtifactType] = None,
        registry_artifact_id: typing.Optional[str] = None,
        registry_version: typing.Optional[Version] = None,
        registry_description: typing.Optional[ArtifactDescription] = None,
        registry_description_encoded: typing.Optional[EncodedArtifactDescription] = None,
        registry_name: typing.Optional[ArtifactName] = None,
        registry_name_encoded: typing.Optional[EncodedArtifactName] = None,
        registry_content_hash: typing.Optional[str] = None,
        registry_hash_algorithm: typing.Optional[CreateArtifactRequestXRegistryHashAlgorithm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtifactMetaData:
        """
        Creates a new artifact by posting the artifact content.  The body of the request should
        be the raw content of the artifact.  This is typically in JSON format for *most* of the
        supported types, but may be in another format for a few (for example, `PROTOBUF`).

        The registry attempts to figure out what kind of artifact is being added from the
        following supported list:

        * Avro (`AVRO`)
        * Protobuf (`PROTOBUF`)
        * JSON Schema (`JSON`)
        * Kafka Connect (`KCONNECT`)
        * OpenAPI (`OPENAPI`)
        * AsyncAPI (`ASYNCAPI`)
        * GraphQL (`GRAPHQL`)
        * Web Services Description Language (`WSDL`)
        * XML Schema (`XSD`)

        Alternatively, you can specify the artifact type using the `X-Registry-ArtifactType`
        HTTP request header, or include a hint in the request's `Content-Type`.  For example:

        ```
        Content-Type: application/json; artifactType=AVRO
        ```

        An artifact is created using the content provided in the body of the request.  This
        content is created under a unique artifact ID that can be provided in the request
        using the `X-Registry-ArtifactId` request header.  If not provided in the request,
        the server generates a unique ID for the artifact.  It is typically recommended
        that callers provide the ID, because this is typically a meaningful identifier,
        and for most use cases should be supplied by the caller.

        If an artifact with the provided artifact ID already exists, the default behavior
        is for the server to reject the content with a 409 error.  However, the caller can
        supply the `ifExists` query parameter to alter this default behavior. The `ifExists`
        query parameter can have one of the following values:

        * `FAIL` (*default*) - server rejects the content with a 409 error
        * `UPDATE` - server updates the existing artifact and returns the new metadata
        * `RETURN` - server does not create or add content to the server, but instead
        returns the metadata for the existing artifact
        * `RETURN_OR_UPDATE` - server returns an existing **version** that matches the
        provided content if such a version exists, otherwise a new version is created

        This operation may fail for one of the following reasons:

        * An invalid `ArtifactType` was indicated (HTTP error `400`)
        * No `ArtifactType` was indicated and the server could not determine one from the content (HTTP error `400`)
        * Provided content (request body) was empty (HTTP error `400`)
        * An artifact with the provided ID already exists (HTTP error `409`)
        * The content violates one of the configured global rules (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request : FileContent

        if_exists : typing.Optional[IfExists]
            Set this option to instruct the server on what to do if the artifact already exists.

        canonical : typing.Optional[bool]
            Used only when the `ifExists` query parameter is set to `RETURN_OR_UPDATE`, this parameter can be set to `true` to indicate that the server should "canonicalize" the content when searching for a matching version.  The canonicalization algorithm is unique to each artifact type, but typically involves removing extra whitespace and formatting the content in a consistent manner.

        registry_artifact_type : typing.Optional[ArtifactType]
            Specifies the type of the artifact being added. Possible values include:

            * Avro (`AVRO`)
            * Protobuf (`PROTOBUF`)
            * JSON Schema (`JSON`)
            * Kafka Connect (`KCONNECT`)
            * OpenAPI (`OPENAPI`)
            * AsyncAPI (`ASYNCAPI`)
            * GraphQL (`GRAPHQL`)
            * Web Services Description Language (`WSDL`)
            * XML Schema (`XSD`)

        registry_artifact_id : typing.Optional[str]
            A client-provided, globally unique identifier for the new artifact.

        registry_version : typing.Optional[Version]
            Specifies the version number of this initial version of the artifact content.  This would typically
            be a simple integer or a SemVer value.  If not provided, the server will assign a version number
            automatically (starting with version `1`).

        registry_description : typing.Optional[ArtifactDescription]
            Specifies the description of artifact being added. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.

        registry_description_encoded : typing.Optional[EncodedArtifactDescription]
            Specifies the description of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.

        registry_name : typing.Optional[ArtifactName]
            Specifies the name of artifact being added. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.

        registry_name_encoded : typing.Optional[EncodedArtifactName]
            Specifies the name of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.

        registry_content_hash : typing.Optional[str]
            Specifies the (optional) hash of the artifact to be verified.

        registry_hash_algorithm : typing.Optional[CreateArtifactRequestXRegistryHashAlgorithm]
            The algorithm to use when checking the content validity. (available: SHA256, MD5; default: SHA256)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactMetaData
            Artifact was successfully created.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifacts.create_artifact(
            group_id='"my-group"',
            registry_artifact_type="AVRO",
            registry_version='"3.1.6"',
            registry_description='"Artifact description"',
            registry_description_encoded='"QXJ0aWZhY3QgZGVzY3JpcHRpb24K"',
            registry_name='"Artifact name"',
            registry_name_encoded='"QXJ0aWZhY3QgbmFtZQo="',
            request="string",
        )
        """
        _response = self._raw_client.create_artifact(
            group_id,
            request=request,
            if_exists=if_exists,
            canonical=canonical,
            registry_artifact_type=registry_artifact_type,
            registry_artifact_id=registry_artifact_id,
            registry_version=registry_version,
            registry_description=registry_description,
            registry_description_encoded=registry_description_encoded,
            registry_name=registry_name,
            registry_name_encoded=registry_name_encoded,
            registry_content_hash=registry_content_hash,
            registry_hash_algorithm=registry_hash_algorithm,
            request_options=request_options,
        )
        return _response.data

    def delete_artifacts_in_group(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all of the artifacts that exist in a given group.

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifacts.delete_artifacts_in_group(
            group_id='"my-group"',
        )
        """
        _response = self._raw_client.delete_artifacts_in_group(group_id, request_options=request_options)
        return _response.data

    def get_latest_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Returns the latest version of the artifact in its raw form.  The `Content-Type` of the
        response depends on the artifact type.  In most cases, this is `application/json`, but
        for some types it may be different (for example, `PROTOBUF`).

        This operation may fail for one of the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

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
        client.artifacts.get_latest_artifact(
            group_id="groupId",
            artifact_id="artifactId",
        )
        """
        with self._raw_client.get_latest_artifact(
            group_id, artifact_id, dereference=dereference, request_options=request_options
        ) as r:
            yield from r.data

    def update_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        registry_version: typing.Optional[Version] = None,
        registry_name: typing.Optional[ArtifactName] = None,
        registry_name_encoded: typing.Optional[EncodedArtifactName] = None,
        registry_description: typing.Optional[ArtifactDescription] = None,
        registry_description_encoded: typing.Optional[EncodedArtifactDescription] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtifactMetaData:
        """
        Updates an artifact by uploading new content.  The body of the request can
        be the raw content of the artifact or a JSON object containing both the raw content and
        a set of references to other artifacts..  This is typically in JSON format for *most*
        of the supported types, but may be in another format for a few (for example, `PROTOBUF`).
        The type of the content should be compatible with the artifact's type (it would be
        an error to update an `AVRO` artifact with new `OPENAPI` content, for example).

        The update could fail for a number of reasons including:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with the `artifactId` exists (HTTP error `404`)
        * The new content violates one of the rules configured for the artifact (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        When successful, this creates a new version of the artifact, making it the most recent
        (and therefore official) version of the artifact.

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        registry_version : typing.Optional[Version]
            Specifies the version number of this new version of the artifact content.  This would typically
            be a simple integer or a SemVer value.  If not provided, the server will assign a version number
            automatically.

        registry_name : typing.Optional[ArtifactName]
            Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not
            provided, the server will extract the name from the artifact content.

        registry_name_encoded : typing.Optional[EncodedArtifactName]
            Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.

        registry_description : typing.Optional[ArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.

        registry_description_encoded : typing.Optional[EncodedArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactMetaData
            When successful, returns the updated artifact metadata.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifacts.update_artifact(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            registry_version='"3.1.6"',
            registry_name='"Artifact name"',
            registry_name_encoded='"QXJ0aWZhY3QgbmFtZQo="',
            registry_description='"Artifact description"',
            registry_description_encoded='"QXJ0aWZhY3QgZGVzY3JpcHRpb24K"',
            request="string",
        )
        """
        _response = self._raw_client.update_artifact(
            group_id,
            artifact_id,
            request=request,
            registry_version=registry_version,
            registry_name=registry_name,
            registry_name_encoded=registry_name_encoded,
            registry_description=registry_description,
            registry_description_encoded=registry_description_encoded,
            request_options=request_options,
        )
        return _response.data

    def delete_artifact(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an artifact completely, resulting in all versions of the artifact also being
        deleted.  This may fail for one of the following reasons:

        * No artifact with the `artifactId` exists (HTTP error `404`)
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifacts.delete_artifact(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
        )
        """
        _response = self._raw_client.delete_artifact(group_id, artifact_id, request_options=request_options)
        return _response.data

    def update_artifact_state(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        state: ArtifactState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the state of the artifact.  For example, you can use this to mark the latest
        version of an artifact as `DEPRECATED`.  The operation changes the state of the latest
        version of the artifact.  If multiple versions exist, only the most recent is changed.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

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
        client.artifacts.update_artifact_state(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            state=ArtifactState.DISABLED,
        )
        """
        _response = self._raw_client.update_artifact_state(
            group_id, artifact_id, state=state, request_options=request_options
        )
        return _response.data

    def get_content_by_hash(
        self, content_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Gets the content for an artifact version in the registry using the
        SHA-256 hash of the content.  This content hash may be shared by multiple artifact
        versions in the case where the artifact versions have identical content.

        This operation may fail for one of the following reasons:

        * No content with this `contentHash` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        content_hash : str
            SHA-256 content hash for a single artifact content.

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
        client.artifacts.get_content_by_hash(
            content_hash="contentHash",
        )
        """
        with self._raw_client.get_content_by_hash(content_hash, request_options=request_options) as r:
            yield from r.data

    def references_by_content_hash(
        self, content_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactReference]:
        """
        Returns a list containing all the artifact references using the artifact content hash.

        This operation may fail for one of the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        content_hash : str
            SHA-256 content hash for a single artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactReference]
            A list containing all the references for the artifact with the given content hash.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifacts.references_by_content_hash(
            content_hash="contentHash",
        )
        """
        _response = self._raw_client.references_by_content_hash(content_hash, request_options=request_options)
        return _response.data

    def get_content_by_id(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Gets the content for an artifact version in the registry using the unique content
        identifier for that content.  This content ID may be shared by multiple artifact
        versions in the case where the artifact versions are identical.

        This operation may fail for one of the following reasons:

        * No content with this `contentId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        content_id : int
            Global identifier for a single artifact content.

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
        client.artifacts.get_content_by_id(
            content_id=1000000,
        )
        """
        with self._raw_client.get_content_by_id(content_id, request_options=request_options) as r:
            yield from r.data

    def references_by_content_id(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactReference]:
        """
        Returns a list containing all the artifact references using the artifact content ID.

        This operation may fail for one of the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        content_id : int
            Global identifier for a single artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactReference]
            A list containing all the references for the artifact with the given content id.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifacts.references_by_content_id(
            content_id=1000000,
        )
        """
        _response = self._raw_client.references_by_content_id(content_id, request_options=request_options)
        return _response.data

    def get_content_by_global_id(
        self,
        global_id: int,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[bytes]:
        """
        Gets the content for an artifact version in the registry using its globally unique
        identifier.

        This operation may fail for one of the following reasons:

        * No artifact version with this `globalId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        global_id : int
            Global identifier for an artifact version.

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
        client.artifacts.get_content_by_global_id(
            global_id=1000000,
        )
        """
        with self._raw_client.get_content_by_global_id(
            global_id, dereference=dereference, request_options=request_options
        ) as r:
            yield from r.data

    def references_by_global_id(
        self, global_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactReference]:
        """
        Returns a list containing all the artifact references using the artifact global ID.

        This operation may fail for one of the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        global_id : int
            Global identifier for an artifact version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactReference]
            A list containing all the references for the artifact with the given global id.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifacts.references_by_global_id(
            global_id=1000000,
        )
        """
        _response = self._raw_client.references_by_global_id(global_id, request_options=request_options)
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

    async def list_artifacts_in_group(
        self,
        group_id: GroupId,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtifactSearchResults:
        """
        Returns a list of all artifacts in the group.  This list is paged.

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        limit : typing.Optional[int]
            The number of artifacts to return.  Defaults to 20.

        offset : typing.Optional[int]
            The number of artifacts to skip before starting the result set.  Defaults to 0.

        order : typing.Optional[SortOrder]
            Sort order, ascending (`asc`) or descending (`desc`).

        orderby : typing.Optional[SortBy]
            The field to sort by.  Can be one of:

            * `name`
            * `createdOn`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactSearchResults
            On a successful response, returns a bounded set of artifacts.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifacts.list_artifacts_in_group(
                group_id='"my-group"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_artifacts_in_group(
            group_id, limit=limit, offset=offset, order=order, orderby=orderby, request_options=request_options
        )
        return _response.data

    async def create_artifact(
        self,
        group_id: GroupId,
        *,
        request: FileContent,
        if_exists: typing.Optional[IfExists] = None,
        canonical: typing.Optional[bool] = None,
        registry_artifact_type: typing.Optional[ArtifactType] = None,
        registry_artifact_id: typing.Optional[str] = None,
        registry_version: typing.Optional[Version] = None,
        registry_description: typing.Optional[ArtifactDescription] = None,
        registry_description_encoded: typing.Optional[EncodedArtifactDescription] = None,
        registry_name: typing.Optional[ArtifactName] = None,
        registry_name_encoded: typing.Optional[EncodedArtifactName] = None,
        registry_content_hash: typing.Optional[str] = None,
        registry_hash_algorithm: typing.Optional[CreateArtifactRequestXRegistryHashAlgorithm] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtifactMetaData:
        """
        Creates a new artifact by posting the artifact content.  The body of the request should
        be the raw content of the artifact.  This is typically in JSON format for *most* of the
        supported types, but may be in another format for a few (for example, `PROTOBUF`).

        The registry attempts to figure out what kind of artifact is being added from the
        following supported list:

        * Avro (`AVRO`)
        * Protobuf (`PROTOBUF`)
        * JSON Schema (`JSON`)
        * Kafka Connect (`KCONNECT`)
        * OpenAPI (`OPENAPI`)
        * AsyncAPI (`ASYNCAPI`)
        * GraphQL (`GRAPHQL`)
        * Web Services Description Language (`WSDL`)
        * XML Schema (`XSD`)

        Alternatively, you can specify the artifact type using the `X-Registry-ArtifactType`
        HTTP request header, or include a hint in the request's `Content-Type`.  For example:

        ```
        Content-Type: application/json; artifactType=AVRO
        ```

        An artifact is created using the content provided in the body of the request.  This
        content is created under a unique artifact ID that can be provided in the request
        using the `X-Registry-ArtifactId` request header.  If not provided in the request,
        the server generates a unique ID for the artifact.  It is typically recommended
        that callers provide the ID, because this is typically a meaningful identifier,
        and for most use cases should be supplied by the caller.

        If an artifact with the provided artifact ID already exists, the default behavior
        is for the server to reject the content with a 409 error.  However, the caller can
        supply the `ifExists` query parameter to alter this default behavior. The `ifExists`
        query parameter can have one of the following values:

        * `FAIL` (*default*) - server rejects the content with a 409 error
        * `UPDATE` - server updates the existing artifact and returns the new metadata
        * `RETURN` - server does not create or add content to the server, but instead
        returns the metadata for the existing artifact
        * `RETURN_OR_UPDATE` - server returns an existing **version** that matches the
        provided content if such a version exists, otherwise a new version is created

        This operation may fail for one of the following reasons:

        * An invalid `ArtifactType` was indicated (HTTP error `400`)
        * No `ArtifactType` was indicated and the server could not determine one from the content (HTTP error `400`)
        * Provided content (request body) was empty (HTTP error `400`)
        * An artifact with the provided ID already exists (HTTP error `409`)
        * The content violates one of the configured global rules (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        request : FileContent

        if_exists : typing.Optional[IfExists]
            Set this option to instruct the server on what to do if the artifact already exists.

        canonical : typing.Optional[bool]
            Used only when the `ifExists` query parameter is set to `RETURN_OR_UPDATE`, this parameter can be set to `true` to indicate that the server should "canonicalize" the content when searching for a matching version.  The canonicalization algorithm is unique to each artifact type, but typically involves removing extra whitespace and formatting the content in a consistent manner.

        registry_artifact_type : typing.Optional[ArtifactType]
            Specifies the type of the artifact being added. Possible values include:

            * Avro (`AVRO`)
            * Protobuf (`PROTOBUF`)
            * JSON Schema (`JSON`)
            * Kafka Connect (`KCONNECT`)
            * OpenAPI (`OPENAPI`)
            * AsyncAPI (`ASYNCAPI`)
            * GraphQL (`GRAPHQL`)
            * Web Services Description Language (`WSDL`)
            * XML Schema (`XSD`)

        registry_artifact_id : typing.Optional[str]
            A client-provided, globally unique identifier for the new artifact.

        registry_version : typing.Optional[Version]
            Specifies the version number of this initial version of the artifact content.  This would typically
            be a simple integer or a SemVer value.  If not provided, the server will assign a version number
            automatically (starting with version `1`).

        registry_description : typing.Optional[ArtifactDescription]
            Specifies the description of artifact being added. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.

        registry_description_encoded : typing.Optional[EncodedArtifactDescription]
            Specifies the description of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.

        registry_name : typing.Optional[ArtifactName]
            Specifies the name of artifact being added. Name must be ASCII-only string. If this is not provided, the server will extract the name from the artifact content.

        registry_name_encoded : typing.Optional[EncodedArtifactName]
            Specifies the name of artifact being added. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.

        registry_content_hash : typing.Optional[str]
            Specifies the (optional) hash of the artifact to be verified.

        registry_hash_algorithm : typing.Optional[CreateArtifactRequestXRegistryHashAlgorithm]
            The algorithm to use when checking the content validity. (available: SHA256, MD5; default: SHA256)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactMetaData
            Artifact was successfully created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifacts.create_artifact(
                group_id='"my-group"',
                registry_artifact_type="AVRO",
                registry_version='"3.1.6"',
                registry_description='"Artifact description"',
                registry_description_encoded='"QXJ0aWZhY3QgZGVzY3JpcHRpb24K"',
                registry_name='"Artifact name"',
                registry_name_encoded='"QXJ0aWZhY3QgbmFtZQo="',
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_artifact(
            group_id,
            request=request,
            if_exists=if_exists,
            canonical=canonical,
            registry_artifact_type=registry_artifact_type,
            registry_artifact_id=registry_artifact_id,
            registry_version=registry_version,
            registry_description=registry_description,
            registry_description_encoded=registry_description_encoded,
            registry_name=registry_name,
            registry_name_encoded=registry_name_encoded,
            registry_content_hash=registry_content_hash,
            registry_hash_algorithm=registry_hash_algorithm,
            request_options=request_options,
        )
        return _response.data

    async def delete_artifacts_in_group(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes all of the artifacts that exist in a given group.

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

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
            await client.artifacts.delete_artifacts_in_group(
                group_id='"my-group"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_artifacts_in_group(group_id, request_options=request_options)
        return _response.data

    async def get_latest_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns the latest version of the artifact in its raw form.  The `Content-Type` of the
        response depends on the artifact type.  In most cases, this is `application/json`, but
        for some types it may be different (for example, `PROTOBUF`).

        This operation may fail for one of the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

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
            await client.artifacts.get_latest_artifact(
                group_id="groupId",
                artifact_id="artifactId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_latest_artifact(
            group_id, artifact_id, dereference=dereference, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def update_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        registry_version: typing.Optional[Version] = None,
        registry_name: typing.Optional[ArtifactName] = None,
        registry_name_encoded: typing.Optional[EncodedArtifactName] = None,
        registry_description: typing.Optional[ArtifactDescription] = None,
        registry_description_encoded: typing.Optional[EncodedArtifactDescription] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtifactMetaData:
        """
        Updates an artifact by uploading new content.  The body of the request can
        be the raw content of the artifact or a JSON object containing both the raw content and
        a set of references to other artifacts..  This is typically in JSON format for *most*
        of the supported types, but may be in another format for a few (for example, `PROTOBUF`).
        The type of the content should be compatible with the artifact's type (it would be
        an error to update an `AVRO` artifact with new `OPENAPI` content, for example).

        The update could fail for a number of reasons including:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with the `artifactId` exists (HTTP error `404`)
        * The new content violates one of the rules configured for the artifact (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        When successful, this creates a new version of the artifact, making it the most recent
        (and therefore official) version of the artifact.

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        registry_version : typing.Optional[Version]
            Specifies the version number of this new version of the artifact content.  This would typically
            be a simple integer or a SemVer value.  If not provided, the server will assign a version number
            automatically.

        registry_name : typing.Optional[ArtifactName]
            Specifies the artifact name of this new version of the artifact content. Name must be ASCII-only string. If this is not
            provided, the server will extract the name from the artifact content.

        registry_name_encoded : typing.Optional[EncodedArtifactName]
            Specifies the artifact name of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the name from the artifact content.

        registry_description : typing.Optional[ArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Description must be ASCII-only string. If this is not provided, the server will extract the description from the artifact content.

        registry_description_encoded : typing.Optional[EncodedArtifactDescription]
            Specifies the artifact description of this new version of the artifact content. Value of this must be Base64 encoded string. If this is not provided, the server will extract the description from the artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtifactMetaData
            When successful, returns the updated artifact metadata.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifacts.update_artifact(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                registry_version='"3.1.6"',
                registry_name='"Artifact name"',
                registry_name_encoded='"QXJ0aWZhY3QgbmFtZQo="',
                registry_description='"Artifact description"',
                registry_description_encoded='"QXJ0aWZhY3QgZGVzY3JpcHRpb24K"',
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_artifact(
            group_id,
            artifact_id,
            request=request,
            registry_version=registry_version,
            registry_name=registry_name,
            registry_name_encoded=registry_name_encoded,
            registry_description=registry_description,
            registry_description_encoded=registry_description_encoded,
            request_options=request_options,
        )
        return _response.data

    async def delete_artifact(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes an artifact completely, resulting in all versions of the artifact also being
        deleted.  This may fail for one of the following reasons:

        * No artifact with the `artifactId` exists (HTTP error `404`)
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifacts.delete_artifact(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_artifact(group_id, artifact_id, request_options=request_options)
        return _response.data

    async def update_artifact_state(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        state: ArtifactState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the state of the artifact.  For example, you can use this to mark the latest
        version of an artifact as `DEPRECATED`.  The operation changes the state of the latest
        version of the artifact.  If multiple versions exist, only the most recent is changed.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

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
            await client.artifacts.update_artifact_state(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                state=ArtifactState.DISABLED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_artifact_state(
            group_id, artifact_id, state=state, request_options=request_options
        )
        return _response.data

    async def get_content_by_hash(
        self, content_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Gets the content for an artifact version in the registry using the
        SHA-256 hash of the content.  This content hash may be shared by multiple artifact
        versions in the case where the artifact versions have identical content.

        This operation may fail for one of the following reasons:

        * No content with this `contentHash` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        content_hash : str
            SHA-256 content hash for a single artifact content.

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
            await client.artifacts.get_content_by_hash(
                content_hash="contentHash",
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_content_by_hash(content_hash, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def references_by_content_hash(
        self, content_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactReference]:
        """
        Returns a list containing all the artifact references using the artifact content hash.

        This operation may fail for one of the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        content_hash : str
            SHA-256 content hash for a single artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactReference]
            A list containing all the references for the artifact with the given content hash.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifacts.references_by_content_hash(
                content_hash="contentHash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.references_by_content_hash(content_hash, request_options=request_options)
        return _response.data

    async def get_content_by_id(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Gets the content for an artifact version in the registry using the unique content
        identifier for that content.  This content ID may be shared by multiple artifact
        versions in the case where the artifact versions are identical.

        This operation may fail for one of the following reasons:

        * No content with this `contentId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        content_id : int
            Global identifier for a single artifact content.

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
            await client.artifacts.get_content_by_id(
                content_id=1000000,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_content_by_id(content_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def references_by_content_id(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactReference]:
        """
        Returns a list containing all the artifact references using the artifact content ID.

        This operation may fail for one of the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        content_id : int
            Global identifier for a single artifact content.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactReference]
            A list containing all the references for the artifact with the given content id.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifacts.references_by_content_id(
                content_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.references_by_content_id(content_id, request_options=request_options)
        return _response.data

    async def get_content_by_global_id(
        self,
        global_id: int,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[bytes]:
        """
        Gets the content for an artifact version in the registry using its globally unique
        identifier.

        This operation may fail for one of the following reasons:

        * No artifact version with this `globalId` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        global_id : int
            Global identifier for an artifact version.

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
            await client.artifacts.get_content_by_global_id(
                global_id=1000000,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_content_by_global_id(
            global_id, dereference=dereference, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def references_by_global_id(
        self, global_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtifactReference]:
        """
        Returns a list containing all the artifact references using the artifact global ID.

        This operation may fail for one of the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        global_id : int
            Global identifier for an artifact version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtifactReference]
            A list containing all the references for the artifact with the given global id.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifacts.references_by_global_id(
                global_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.references_by_global_id(global_id, request_options=request_options)
        return _response.data
