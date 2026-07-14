

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.artifact_id import ArtifactId
from ..types.error import Error
from ..types.file_content import FileContent
from ..types.group_id import GroupId
from ..types.rule import Rule
from ..types.rule_type import RuleType
from .types.delete_artifact_rule_request_rule import DeleteArtifactRuleRequestRule
from .types.get_artifact_rule_config_request_rule import GetArtifactRuleConfigRequestRule
from .types.update_artifact_rule_config_request_rule import UpdateArtifactRuleConfigRequestRule


OMIT = typing.cast(typing.Any, ...)


class RawArtifactRulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_artifact_rules(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[RuleType]]:
        """
        Returns a list of all rules configured for the artifact.  The set of rules determines
        how the content of an artifact can evolve over time.  If no rules are configured for
        an artifact, the set of globally configured rules are used.  If no global rules
        are defined, there are no restrictions on content evolution.

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
        HttpResponse[typing.List[RuleType]]
            Returns the names of the rules configured for the artifact.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RuleType],
                    parse_obj_as(
                        type_=typing.List[RuleType],
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_artifact_rule(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Adds a rule to the list of rules that get applied to the artifact when adding new
        versions.  All configured rules must pass to successfully add a new artifact version.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * Rule (named in the request body) is unknown (HTTP error `400`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        config : str

        type : typing.Optional[RuleType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules",
            method="POST",
            json={
                "config": config,
                "type": type,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_artifact_rules(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes all of the rules configured for the artifact.  After this is done, the global
        rules apply to the artifact again.

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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules",
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_artifact_rule_config(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: GetArtifactRuleConfigRequestRule,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Rule]:
        """
        Returns information about a single rule configured for an artifact.  This is useful
        when you want to know what the current configuration settings are for a specific rule.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No rule with this name/type is configured for this artifact (HTTP error `404`)
        * Invalid rule type (HTTP error `400`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        rule : GetArtifactRuleConfigRequestRule
            The unique name/type of a rule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Rule]
            Information about a rule.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules/{jsonable_encoder(rule)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Rule,
                    parse_obj_as(
                        type_=Rule,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_artifact_rule_config(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: UpdateArtifactRuleConfigRequestRule,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Rule]:
        """
        Updates the configuration of a single rule for the artifact.  The configuration data
        is specific to each rule type, so the configuration of the `COMPATIBILITY` rule
        is in a different format from the configuration of the `VALIDITY` rule.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No rule with this name/type is configured for this artifact (HTTP error `404`)
        * Invalid rule type (HTTP error `400`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        rule : UpdateArtifactRuleConfigRequestRule
            The unique name/type of a rule.

        config : str

        type : typing.Optional[RuleType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Rule]
            Rule configuration was updated.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules/{jsonable_encoder(rule)}",
            method="PUT",
            json={
                "config": config,
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Rule,
                    parse_obj_as(
                        type_=Rule,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_artifact_rule(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: DeleteArtifactRuleRequestRule,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Deletes a rule from the artifact.  This results in the rule no longer applying for
        this artifact.  If this is the only rule configured for the artifact, this is the
        same as deleting **all** rules, and the globally configured rules now apply to
        this artifact.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No rule with this name/type is configured for this artifact (HTTP error `404`)
        * Invalid rule type (HTTP error `400`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        rule : DeleteArtifactRuleRequestRule
            The unique name/type of a rule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules/{jsonable_encoder(rule)}",
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def test_update_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Tests whether an update to the artifact's content *would* succeed for the provided content.
        Ultimately, this applies any rules configured for the artifact against the given content
        to determine whether the rules would pass or fail, but without actually updating the artifact
        content.

        The body of the request should be the raw content of the artifact.  This is typically in
        JSON format for *most* of the supported types, but may be in another format for a few
        (for example, `PROTOBUF`).

        The update could fail for a number of reasons including:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with the `artifactId` exists (HTTP error `404`)
        * The new content violates one of the rules configured for the artifact (HTTP error `409`)
        * The provided artifact type is not recognized (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        When successful, this operation simply returns a *No Content* response.  This response
        indicates that the content is valid against the configured content rules for the
        artifact (or the global rules if no artifact rules are enabled).

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/test",
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawArtifactRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_artifact_rules(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[RuleType]]:
        """
        Returns a list of all rules configured for the artifact.  The set of rules determines
        how the content of an artifact can evolve over time.  If no rules are configured for
        an artifact, the set of globally configured rules are used.  If no global rules
        are defined, there are no restrictions on content evolution.

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
        AsyncHttpResponse[typing.List[RuleType]]
            Returns the names of the rules configured for the artifact.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RuleType],
                    parse_obj_as(
                        type_=typing.List[RuleType],
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_artifact_rule(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Adds a rule to the list of rules that get applied to the artifact when adding new
        versions.  All configured rules must pass to successfully add a new artifact version.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * Rule (named in the request body) is unknown (HTTP error `400`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        config : str

        type : typing.Optional[RuleType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules",
            method="POST",
            json={
                "config": config,
                "type": type,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_artifact_rules(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes all of the rules configured for the artifact.  After this is done, the global
        rules apply to the artifact again.

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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules",
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_artifact_rule_config(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: GetArtifactRuleConfigRequestRule,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Rule]:
        """
        Returns information about a single rule configured for an artifact.  This is useful
        when you want to know what the current configuration settings are for a specific rule.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No rule with this name/type is configured for this artifact (HTTP error `404`)
        * Invalid rule type (HTTP error `400`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        rule : GetArtifactRuleConfigRequestRule
            The unique name/type of a rule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Rule]
            Information about a rule.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules/{jsonable_encoder(rule)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Rule,
                    parse_obj_as(
                        type_=Rule,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_artifact_rule_config(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: UpdateArtifactRuleConfigRequestRule,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Rule]:
        """
        Updates the configuration of a single rule for the artifact.  The configuration data
        is specific to each rule type, so the configuration of the `COMPATIBILITY` rule
        is in a different format from the configuration of the `VALIDITY` rule.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No rule with this name/type is configured for this artifact (HTTP error `404`)
        * Invalid rule type (HTTP error `400`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        rule : UpdateArtifactRuleConfigRequestRule
            The unique name/type of a rule.

        config : str

        type : typing.Optional[RuleType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Rule]
            Rule configuration was updated.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules/{jsonable_encoder(rule)}",
            method="PUT",
            json={
                "config": config,
                "type": type,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Rule,
                    parse_obj_as(
                        type_=Rule,
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_artifact_rule(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: DeleteArtifactRuleRequestRule,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a rule from the artifact.  This results in the rule no longer applying for
        this artifact.  If this is the only rule configured for the artifact, this is the
        same as deleting **all** rules, and the globally configured rules now apply to
        this artifact.

        This operation can fail for the following reasons:

        * No artifact with this `artifactId` exists (HTTP error `404`)
        * No rule with this name/type is configured for this artifact (HTTP error `404`)
        * Invalid rule type (HTTP error `400`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        rule : DeleteArtifactRuleRequestRule
            The unique name/type of a rule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/rules/{jsonable_encoder(rule)}",
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def test_update_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Tests whether an update to the artifact's content *would* succeed for the provided content.
        Ultimately, this applies any rules configured for the artifact against the given content
        to determine whether the rules would pass or fail, but without actually updating the artifact
        content.

        The body of the request should be the raw content of the artifact.  This is typically in
        JSON format for *most* of the supported types, but may be in another format for a few
        (for example, `PROTOBUF`).

        The update could fail for a number of reasons including:

        * Provided content (request body) was empty (HTTP error `400`)
        * No artifact with the `artifactId` exists (HTTP error `404`)
        * The new content violates one of the rules configured for the artifact (HTTP error `409`)
        * The provided artifact type is not recognized (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        When successful, this operation simply returns a *No Content* response.  This response
        indicates that the content is valid against the configured content rules for the
        artifact (or the global rules if no artifact rules are enabled).

        Parameters
        ----------
        group_id : GroupId
            The artifact group ID.  Must be a string provided by the client, representing the name of the grouping of artifacts.

        artifact_id : ArtifactId
            The artifact ID.  Can be a string (client-provided) or UUID (server-generated), representing the unique artifact identifier.

        request : FileContent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"groups/{jsonable_encoder(group_id)}/artifacts/{jsonable_encoder(artifact_id)}/test",
            method="PUT",
            json=request,
            request_options=request_options,
            omit=OMIT,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Optional[typing.Any],
                        parse_obj_as(
                            type_=typing.Optional[typing.Any],
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
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
