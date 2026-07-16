

import contextlib
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
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
from ..types.error import Error
from ..types.file_content import FileContent
from ..types.group_id import GroupId
from ..types.if_exists import IfExists
from ..types.sort_by import SortBy
from ..types.sort_order import SortOrder
from ..types.version import Version
from .types.create_artifact_request_x_registry_hash_algorithm import CreateArtifactRequestXRegistryHashAlgorithm
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawArtifactsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_artifacts_in_group(
        self,
        group_id: GroupId,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ArtifactSearchResults]:
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
        HttpResponse[ArtifactSearchResults]
            On a successful response, returns a bounded set of artifacts.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order": order,
                "orderby": orderby,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactSearchResults,
                    parse_obj_as(
                        type_=ArtifactSearchResults,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[ArtifactMetaData]:
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
        HttpResponse[ArtifactMetaData]
            Artifact was successfully created.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts",
            method="POST",
            params={
                "ifExists": if_exists,
                "canonical": canonical,
            },
            json=request,
            headers={
                "X-Registry-ArtifactType": str(registry_artifact_type) if registry_artifact_type is not None else None,
                "X-Registry-ArtifactId": str(registry_artifact_id) if registry_artifact_id is not None else None,
                "X-Registry-Version": str(registry_version) if registry_version is not None else None,
                "X-Registry-Description": str(registry_description) if registry_description is not None else None,
                "X-Registry-Description-Encoded": str(registry_description_encoded)
                if registry_description_encoded is not None
                else None,
                "X-Registry-Name": str(registry_name) if registry_name is not None else None,
                "X-Registry-Name-Encoded": str(registry_name_encoded) if registry_name_encoded is not None else None,
                "X-Registry-Content-Hash": str(registry_content_hash) if registry_content_hash is not None else None,
                "X-Registry-Hash-Algorithm": registry_hash_algorithm.value
                if registry_hash_algorithm is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactMetaData,
                    parse_obj_as(
                        type_=ArtifactMetaData,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_artifacts_in_group(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_latest_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The content of one version of one artifact.
        """
        with self._client_wrapper.httpx_client.stream(
            f"groups/{encode_path_param(group_id)}/artifacts/{encode_path_param(artifact_id)}",
            method="GET",
            params={
                "dereference": dereference,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

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
    ) -> HttpResponse[ArtifactMetaData]:
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
        HttpResponse[ArtifactMetaData]
            When successful, returns the updated artifact metadata.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts/{encode_path_param(artifact_id)}",
            method="PUT",
            json=request,
            headers={
                "X-Registry-Version": str(registry_version) if registry_version is not None else None,
                "X-Registry-Name": str(registry_name) if registry_name is not None else None,
                "X-Registry-Name-Encoded": str(registry_name_encoded) if registry_name_encoded is not None else None,
                "X-Registry-Description": str(registry_description) if registry_description is not None else None,
                "X-Registry-Description-Encoded": str(registry_description_encoded)
                if registry_description_encoded is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactMetaData,
                    parse_obj_as(
                        type_=ArtifactMetaData,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_artifact(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts/{encode_path_param(artifact_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_artifact_state(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        state: ArtifactState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts/{encode_path_param(artifact_id)}/state",
            method="PUT",
            json={
                "state": state,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_content_by_hash(
        self, content_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The content of one version of one artifact.
        """
        with self._client_wrapper.httpx_client.stream(
            f"ids/contentHashes/{encode_path_param(content_hash)}/",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def references_by_content_hash(
        self, content_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ArtifactReference]]:
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
        HttpResponse[typing.List[ArtifactReference]]
            A list containing all the references for the artifact with the given content hash.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ids/contentHashes/{encode_path_param(content_hash)}/references",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtifactReference],
                    parse_obj_as(
                        type_=typing.List[ArtifactReference],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_content_by_id(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The content of one version of one artifact.
        """
        with self._client_wrapper.httpx_client.stream(
            f"ids/contentIds/{encode_path_param(content_id)}/",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def references_by_content_id(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ArtifactReference]]:
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
        HttpResponse[typing.List[ArtifactReference]]
            A list containing all the references for the artifact with the given content id.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ids/contentIds/{encode_path_param(content_id)}/references",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtifactReference],
                    parse_obj_as(
                        type_=typing.List[ArtifactReference],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.contextmanager
    def get_content_by_global_id(
        self,
        global_id: int,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
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
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            The content of one version of one artifact.
        """
        with self._client_wrapper.httpx_client.stream(
            f"ids/globalIds/{encode_path_param(global_id)}",
            method="GET",
            params={
                "dereference": dereference,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def references_by_global_id(
        self, global_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ArtifactReference]]:
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
        HttpResponse[typing.List[ArtifactReference]]
            A list containing all the references for the artifact with the given global id.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ids/globalIds/{encode_path_param(global_id)}/references",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtifactReference],
                    parse_obj_as(
                        type_=typing.List[ArtifactReference],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawArtifactsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_artifacts_in_group(
        self,
        group_id: GroupId,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order: typing.Optional[SortOrder] = None,
        orderby: typing.Optional[SortBy] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ArtifactSearchResults]:
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
        AsyncHttpResponse[ArtifactSearchResults]
            On a successful response, returns a bounded set of artifacts.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
                "order": order,
                "orderby": orderby,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactSearchResults,
                    parse_obj_as(
                        type_=ArtifactSearchResults,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[ArtifactMetaData]:
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
        AsyncHttpResponse[ArtifactMetaData]
            Artifact was successfully created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts",
            method="POST",
            params={
                "ifExists": if_exists,
                "canonical": canonical,
            },
            json=request,
            headers={
                "X-Registry-ArtifactType": str(registry_artifact_type) if registry_artifact_type is not None else None,
                "X-Registry-ArtifactId": str(registry_artifact_id) if registry_artifact_id is not None else None,
                "X-Registry-Version": str(registry_version) if registry_version is not None else None,
                "X-Registry-Description": str(registry_description) if registry_description is not None else None,
                "X-Registry-Description-Encoded": str(registry_description_encoded)
                if registry_description_encoded is not None
                else None,
                "X-Registry-Name": str(registry_name) if registry_name is not None else None,
                "X-Registry-Name-Encoded": str(registry_name_encoded) if registry_name_encoded is not None else None,
                "X-Registry-Content-Hash": str(registry_content_hash) if registry_content_hash is not None else None,
                "X-Registry-Hash-Algorithm": registry_hash_algorithm.value
                if registry_hash_algorithm is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactMetaData,
                    parse_obj_as(
                        type_=ArtifactMetaData,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_artifacts_in_group(
        self, group_id: GroupId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_latest_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The content of one version of one artifact.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"groups/{encode_path_param(group_id)}/artifacts/{encode_path_param(artifact_id)}",
            method="GET",
            params={
                "dereference": dereference,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

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
    ) -> AsyncHttpResponse[ArtifactMetaData]:
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
        AsyncHttpResponse[ArtifactMetaData]
            When successful, returns the updated artifact metadata.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts/{encode_path_param(artifact_id)}",
            method="PUT",
            json=request,
            headers={
                "X-Registry-Version": str(registry_version) if registry_version is not None else None,
                "X-Registry-Name": str(registry_name) if registry_name is not None else None,
                "X-Registry-Name-Encoded": str(registry_name_encoded) if registry_name_encoded is not None else None,
                "X-Registry-Description": str(registry_description) if registry_description is not None else None,
                "X-Registry-Description-Encoded": str(registry_description_encoded)
                if registry_description_encoded is not None
                else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ArtifactMetaData,
                    parse_obj_as(
                        type_=ArtifactMetaData,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_artifact(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts/{encode_path_param(artifact_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_artifact_state(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        state: ArtifactState,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{encode_path_param(group_id)}/artifacts/{encode_path_param(artifact_id)}/state",
            method="PUT",
            json={
                "state": state,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_content_by_hash(
        self, content_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The content of one version of one artifact.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"ids/contentHashes/{encode_path_param(content_hash)}/",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def references_by_content_hash(
        self, content_hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ArtifactReference]]:
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
        AsyncHttpResponse[typing.List[ArtifactReference]]
            A list containing all the references for the artifact with the given content hash.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ids/contentHashes/{encode_path_param(content_hash)}/references",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtifactReference],
                    parse_obj_as(
                        type_=typing.List[ArtifactReference],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_content_by_id(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The content of one version of one artifact.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"ids/contentIds/{encode_path_param(content_id)}/",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def references_by_content_id(
        self, content_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ArtifactReference]]:
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
        AsyncHttpResponse[typing.List[ArtifactReference]]
            A list containing all the references for the artifact with the given content id.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ids/contentIds/{encode_path_param(content_id)}/references",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtifactReference],
                    parse_obj_as(
                        type_=typing.List[ArtifactReference],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    @contextlib.asynccontextmanager
    async def get_content_by_global_id(
        self,
        global_id: int,
        *,
        dereference: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
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
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            The content of one version of one artifact.
        """
        async with self._client_wrapper.httpx_client.stream(
            f"ids/globalIds/{encode_path_param(global_id)}",
            method="GET",
            params={
                "dereference": dereference,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    if _response.status_code == 404:
                        raise NotFoundError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    if _response.status_code == 500:
                        raise InternalServerError(
                            headers=dict(_response.headers),
                            body=typing.cast(
                                Error,
                                parse_obj_as(
                                    type_=Error,
                                    object_=_response.json(),
                                ),
                            ),
                        )
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def references_by_global_id(
        self, global_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ArtifactReference]]:
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
        AsyncHttpResponse[typing.List[ArtifactReference]]
            A list containing all the references for the artifact with the given global id.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ids/globalIds/{encode_path_param(global_id)}/references",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ArtifactReference],
                    parse_obj_as(
                        type_=typing.List[ArtifactReference],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
