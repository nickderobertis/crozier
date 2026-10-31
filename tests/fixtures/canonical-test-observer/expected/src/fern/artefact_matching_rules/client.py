

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.artefact_matching_rule_response import ArtefactMatchingRuleResponse
from ..types.family_name import FamilyName
from ..types.permission import Permission
from .raw_client import AsyncRawArtefactMatchingRulesClient, RawArtefactMatchingRulesClient


OMIT = typing.cast(typing.Any, ...)


class ArtefactMatchingRulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawArtefactMatchingRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawArtefactMatchingRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawArtefactMatchingRulesClient
        """
        return self._raw_client

    def get_artefact_matching_rules(
        self, *, family: typing.Optional[FamilyName] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactMatchingRuleResponse]:
        """
        Get all artefact matching rules, optionally filtered by family

        Parameters
        ----------
        family : typing.Optional[FamilyName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactMatchingRuleResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefact_matching_rules.get_artefact_matching_rules()
        """
        _response = self._raw_client.get_artefact_matching_rules(family=family, request_options=request_options)
        return _response.data

    def create_artefact_matching_rule(
        self,
        *,
        family: FamilyName,
        team_ids: typing.Sequence[int],
        name: typing.Optional[str] = OMIT,
        stage: typing.Optional[str] = OMIT,
        track: typing.Optional[str] = OMIT,
        branch: typing.Optional[str] = OMIT,
        store: typing.Optional[str] = OMIT,
        series: typing.Optional[str] = OMIT,
        os: typing.Optional[str] = OMIT,
        release: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        grant_permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactMatchingRuleResponse:
        """
        Create a new artefact matching rule with at least one team

        Parameters
        ----------
        family : FamilyName

        team_ids : typing.Sequence[int]

        name : typing.Optional[str]

        stage : typing.Optional[str]

        track : typing.Optional[str]

        branch : typing.Optional[str]

        store : typing.Optional[str]

        series : typing.Optional[str]

        os : typing.Optional[str]

        release : typing.Optional[str]

        owner : typing.Optional[str]

        grant_permissions : typing.Optional[typing.Sequence[Permission]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactMatchingRuleResponse
            Successful Response

        Examples
        --------
        from fern import FamilyName, FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefact_matching_rules.create_artefact_matching_rule(
            family=FamilyName.SNAP,
            team_ids=[1],
        )
        """
        _response = self._raw_client.create_artefact_matching_rule(
            family=family,
            team_ids=team_ids,
            name=name,
            stage=stage,
            track=track,
            branch=branch,
            store=store,
            series=series,
            os=os,
            release=release,
            owner=owner,
            grant_permissions=grant_permissions,
            request_options=request_options,
        )
        return _response.data

    def get_artefact_matching_rule(
        self, rule_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtefactMatchingRuleResponse:
        """
        Get a specific artefact matching rule by ID

        Parameters
        ----------
        rule_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactMatchingRuleResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefact_matching_rules.get_artefact_matching_rule(
            rule_id=1,
        )
        """
        _response = self._raw_client.get_artefact_matching_rule(rule_id, request_options=request_options)
        return _response.data

    def delete_artefact_matching_rule(
        self, rule_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an artefact matching rule

        Parameters
        ----------
        rule_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefact_matching_rules.delete_artefact_matching_rule(
            rule_id=1,
        )
        """
        _response = self._raw_client.delete_artefact_matching_rule(rule_id, request_options=request_options)
        return _response.data

    def update_artefact_matching_rule(
        self,
        rule_id: int,
        *,
        name: typing.Optional[str] = OMIT,
        family: typing.Optional[FamilyName] = OMIT,
        stage: typing.Optional[str] = OMIT,
        track: typing.Optional[str] = OMIT,
        branch: typing.Optional[str] = OMIT,
        store: typing.Optional[str] = OMIT,
        series: typing.Optional[str] = OMIT,
        os: typing.Optional[str] = OMIT,
        release: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        team_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        grant_permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactMatchingRuleResponse:
        """
        Update an artefact matching rule

        Parameters
        ----------
        rule_id : int

        name : typing.Optional[str]

        family : typing.Optional[FamilyName]

        stage : typing.Optional[str]

        track : typing.Optional[str]

        branch : typing.Optional[str]

        store : typing.Optional[str]

        series : typing.Optional[str]

        os : typing.Optional[str]

        release : typing.Optional[str]

        owner : typing.Optional[str]

        team_ids : typing.Optional[typing.Sequence[int]]

        grant_permissions : typing.Optional[typing.Sequence[Permission]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactMatchingRuleResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.artefact_matching_rules.update_artefact_matching_rule(
            rule_id=1,
        )
        """
        _response = self._raw_client.update_artefact_matching_rule(
            rule_id,
            name=name,
            family=family,
            stage=stage,
            track=track,
            branch=branch,
            store=store,
            series=series,
            os=os,
            release=release,
            owner=owner,
            team_ids=team_ids,
            grant_permissions=grant_permissions,
            request_options=request_options,
        )
        return _response.data


class AsyncArtefactMatchingRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawArtefactMatchingRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawArtefactMatchingRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawArtefactMatchingRulesClient
        """
        return self._raw_client

    async def get_artefact_matching_rules(
        self, *, family: typing.Optional[FamilyName] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[ArtefactMatchingRuleResponse]:
        """
        Get all artefact matching rules, optionally filtered by family

        Parameters
        ----------
        family : typing.Optional[FamilyName]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ArtefactMatchingRuleResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.artefact_matching_rules.get_artefact_matching_rules()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artefact_matching_rules(family=family, request_options=request_options)
        return _response.data

    async def create_artefact_matching_rule(
        self,
        *,
        family: FamilyName,
        team_ids: typing.Sequence[int],
        name: typing.Optional[str] = OMIT,
        stage: typing.Optional[str] = OMIT,
        track: typing.Optional[str] = OMIT,
        branch: typing.Optional[str] = OMIT,
        store: typing.Optional[str] = OMIT,
        series: typing.Optional[str] = OMIT,
        os: typing.Optional[str] = OMIT,
        release: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        grant_permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactMatchingRuleResponse:
        """
        Create a new artefact matching rule with at least one team

        Parameters
        ----------
        family : FamilyName

        team_ids : typing.Sequence[int]

        name : typing.Optional[str]

        stage : typing.Optional[str]

        track : typing.Optional[str]

        branch : typing.Optional[str]

        store : typing.Optional[str]

        series : typing.Optional[str]

        os : typing.Optional[str]

        release : typing.Optional[str]

        owner : typing.Optional[str]

        grant_permissions : typing.Optional[typing.Sequence[Permission]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactMatchingRuleResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, FamilyName

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.artefact_matching_rules.create_artefact_matching_rule(
                family=FamilyName.SNAP,
                team_ids=[1],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_artefact_matching_rule(
            family=family,
            team_ids=team_ids,
            name=name,
            stage=stage,
            track=track,
            branch=branch,
            store=store,
            series=series,
            os=os,
            release=release,
            owner=owner,
            grant_permissions=grant_permissions,
            request_options=request_options,
        )
        return _response.data

    async def get_artefact_matching_rule(
        self, rule_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ArtefactMatchingRuleResponse:
        """
        Get a specific artefact matching rule by ID

        Parameters
        ----------
        rule_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactMatchingRuleResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.artefact_matching_rules.get_artefact_matching_rule(
                rule_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_artefact_matching_rule(rule_id, request_options=request_options)
        return _response.data

    async def delete_artefact_matching_rule(
        self, rule_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete an artefact matching rule

        Parameters
        ----------
        rule_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.artefact_matching_rules.delete_artefact_matching_rule(
                rule_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_artefact_matching_rule(rule_id, request_options=request_options)
        return _response.data

    async def update_artefact_matching_rule(
        self,
        rule_id: int,
        *,
        name: typing.Optional[str] = OMIT,
        family: typing.Optional[FamilyName] = OMIT,
        stage: typing.Optional[str] = OMIT,
        track: typing.Optional[str] = OMIT,
        branch: typing.Optional[str] = OMIT,
        store: typing.Optional[str] = OMIT,
        series: typing.Optional[str] = OMIT,
        os: typing.Optional[str] = OMIT,
        release: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        team_ids: typing.Optional[typing.Sequence[int]] = OMIT,
        grant_permissions: typing.Optional[typing.Sequence[Permission]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ArtefactMatchingRuleResponse:
        """
        Update an artefact matching rule

        Parameters
        ----------
        rule_id : int

        name : typing.Optional[str]

        family : typing.Optional[FamilyName]

        stage : typing.Optional[str]

        track : typing.Optional[str]

        branch : typing.Optional[str]

        store : typing.Optional[str]

        series : typing.Optional[str]

        os : typing.Optional[str]

        release : typing.Optional[str]

        owner : typing.Optional[str]

        team_ids : typing.Optional[typing.Sequence[int]]

        grant_permissions : typing.Optional[typing.Sequence[Permission]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ArtefactMatchingRuleResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            csrf_token="YOUR_CSRF_TOKEN",
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.artefact_matching_rules.update_artefact_matching_rule(
                rule_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_artefact_matching_rule(
            rule_id,
            name=name,
            family=family,
            stage=stage,
            track=track,
            branch=branch,
            store=store,
            series=series,
            os=os,
            release=release,
            owner=owner,
            team_ids=team_ids,
            grant_permissions=grant_permissions,
            request_options=request_options,
        )
        return _response.data
