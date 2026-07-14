

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artifact_id import ArtifactId
from ..types.file_content import FileContent
from ..types.group_id import GroupId
from ..types.rule import Rule
from ..types.rule_type import RuleType
from .raw_client import AsyncRawArtifactRulesClient, RawArtifactRulesClient
from .types.delete_artifact_rule_request_rule import DeleteArtifactRuleRequestRule
from .types.get_artifact_rule_config_request_rule import GetArtifactRuleConfigRequestRule
from .types.update_artifact_rule_config_request_rule import UpdateArtifactRuleConfigRequestRule


OMIT = typing.cast(typing.Any, ...)


class ArtifactRulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArtifactRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArtifactRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArtifactRulesClient
        """
        return self._raw_client

    def list_artifact_rules(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RuleType]:
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
        typing.List[RuleType]
            Returns the names of the rules configured for the artifact.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifact_rules.list_artifact_rules(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
        )
        """
        _response = self._raw_client.list_artifact_rules(group_id, artifact_id, request_options=request_options)
        return _response.data

    def create_artifact_rule(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi, RuleType

        client = FernApi()
        client.artifact_rules.create_artifact_rule(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            config="FULL",
            type=RuleType.VALIDITY,
        )
        """
        _response = self._raw_client.create_artifact_rule(
            group_id, artifact_id, config=config, type=type, request_options=request_options
        )
        return _response.data

    def delete_artifact_rules(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifact_rules.delete_artifact_rules(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
        )
        """
        _response = self._raw_client.delete_artifact_rules(group_id, artifact_id, request_options=request_options)
        return _response.data

    def get_artifact_rule_config(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: GetArtifactRuleConfigRequestRule,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rule:
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
        Rule
            Information about a rule.

        Examples
        --------
        from fern.artifact_rules import GetArtifactRuleConfigRequestRule

        from fern import FernApi

        client = FernApi()
        client.artifact_rules.get_artifact_rule_config(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            rule=GetArtifactRuleConfigRequestRule.VALIDITY,
        )
        """
        _response = self._raw_client.get_artifact_rule_config(
            group_id, artifact_id, rule, request_options=request_options
        )
        return _response.data

    def update_artifact_rule_config(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: UpdateArtifactRuleConfigRequestRule,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rule:
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
        Rule
            Rule configuration was updated.

        Examples
        --------
        from fern.artifact_rules import UpdateArtifactRuleConfigRequestRule

        from fern import FernApi, RuleType

        client = FernApi()
        client.artifact_rules.update_artifact_rule_config(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            rule=UpdateArtifactRuleConfigRequestRule.VALIDITY,
            config="FULL",
            type=RuleType.VALIDITY,
        )
        """
        _response = self._raw_client.update_artifact_rule_config(
            group_id, artifact_id, rule, config=config, type=type, request_options=request_options
        )
        return _response.data

    def delete_artifact_rule(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: DeleteArtifactRuleRequestRule,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern.artifact_rules import DeleteArtifactRuleRequestRule

        from fern import FernApi

        client = FernApi()
        client.artifact_rules.delete_artifact_rule(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            rule=DeleteArtifactRuleRequestRule.VALIDITY,
        )
        """
        _response = self._raw_client.delete_artifact_rule(group_id, artifact_id, rule, request_options=request_options)
        return _response.data

    def test_update_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.artifact_rules.test_update_artifact(
            group_id='"my-group"',
            artifact_id='"example-artifact"',
            request="string",
        )
        """
        _response = self._raw_client.test_update_artifact(
            group_id, artifact_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncArtifactRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArtifactRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArtifactRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArtifactRulesClient
        """
        return self._raw_client

    async def list_artifact_rules(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RuleType]:
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
        typing.List[RuleType]
            Returns the names of the rules configured for the artifact.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifact_rules.list_artifact_rules(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_artifact_rules(group_id, artifact_id, request_options=request_options)
        return _response.data

    async def create_artifact_rule(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RuleType

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifact_rules.create_artifact_rule(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                config="FULL",
                type=RuleType.VALIDITY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_artifact_rule(
            group_id, artifact_id, config=config, type=type, request_options=request_options
        )
        return _response.data

    async def delete_artifact_rules(
        self, group_id: GroupId, artifact_id: ArtifactId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifact_rules.delete_artifact_rules(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_artifact_rules(group_id, artifact_id, request_options=request_options)
        return _response.data

    async def get_artifact_rule_config(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: GetArtifactRuleConfigRequestRule,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rule:
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
        Rule
            Information about a rule.

        Examples
        --------
        import asyncio

        from fern.artifact_rules import GetArtifactRuleConfigRequestRule

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifact_rules.get_artifact_rule_config(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                rule=GetArtifactRuleConfigRequestRule.VALIDITY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artifact_rule_config(
            group_id, artifact_id, rule, request_options=request_options
        )
        return _response.data

    async def update_artifact_rule_config(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: UpdateArtifactRuleConfigRequestRule,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rule:
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
        Rule
            Rule configuration was updated.

        Examples
        --------
        import asyncio

        from fern.artifact_rules import UpdateArtifactRuleConfigRequestRule

        from fern import AsyncFernApi, RuleType

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifact_rules.update_artifact_rule_config(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                rule=UpdateArtifactRuleConfigRequestRule.VALIDITY,
                config="FULL",
                type=RuleType.VALIDITY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_artifact_rule_config(
            group_id, artifact_id, rule, config=config, type=type, request_options=request_options
        )
        return _response.data

    async def delete_artifact_rule(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        rule: DeleteArtifactRuleRequestRule,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern.artifact_rules import DeleteArtifactRuleRequestRule

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifact_rules.delete_artifact_rule(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                rule=DeleteArtifactRuleRequestRule.VALIDITY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_artifact_rule(
            group_id, artifact_id, rule, request_options=request_options
        )
        return _response.data

    async def test_update_artifact(
        self,
        group_id: GroupId,
        artifact_id: ArtifactId,
        *,
        request: FileContent,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
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
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.artifact_rules.test_update_artifact(
                group_id='"my-group"',
                artifact_id='"example-artifact"',
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.test_update_artifact(
            group_id, artifact_id, request=request, request_options=request_options
        )
        return _response.data
