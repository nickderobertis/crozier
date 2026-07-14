

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.rule import Rule
from ..types.rule_type import RuleType
from .raw_client import AsyncRawGlobalRulesClient, RawGlobalRulesClient


OMIT = typing.cast(typing.Any, ...)


class GlobalRulesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawGlobalRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawGlobalRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawGlobalRulesClient
        """
        return self._raw_client

    def list_global_rules(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[RuleType]:
        """
        Gets a list of all the currently configured global rules (if any).

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RuleType]
            The list of names of the globally configured rules.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_rules.list_global_rules()
        """
        _response = self._raw_client.list_global_rules(request_options=request_options)
        return _response.data

    def create_global_rule(
        self,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds a rule to the list of globally configured rules.

        This operation can fail for the following reasons:

        * The rule type is unknown (HTTP error `400`)
        * The rule already exists (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
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
        client.global_rules.create_global_rule(
            config="FULL",
            type=RuleType.VALIDITY,
        )
        """
        _response = self._raw_client.create_global_rule(config=config, type=type, request_options=request_options)
        return _response.data

    def delete_all_global_rules(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes all globally configured rules.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.global_rules.delete_all_global_rules()
        """
        _response = self._raw_client.delete_all_global_rules(request_options=request_options)
        return _response.data

    def get_global_rule_config(
        self, rule: RuleType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Rule:
        """
        Returns information about the named globally configured rule.

        This operation can fail for the following reasons:

        * Invalid rule name/type (HTTP error `400`)
        * No rule with name/type `rule` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        rule : RuleType
            The unique name/type of a rule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rule
            The global rule's configuration.

        Examples
        --------
        from fern import FernApi, RuleType

        client = FernApi()
        client.global_rules.get_global_rule_config(
            rule=RuleType.VALIDITY,
        )
        """
        _response = self._raw_client.get_global_rule_config(rule, request_options=request_options)
        return _response.data

    def update_global_rule_config(
        self,
        rule: RuleType,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rule:
        """
        Updates the configuration for a globally configured rule.

        This operation can fail for the following reasons:

        * Invalid rule name/type (HTTP error `400`)
        * No rule with name/type `rule` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        rule : RuleType
            The unique name/type of a rule.

        config : str

        type : typing.Optional[RuleType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rule
            The global rule's configuration was successfully updated.

        Examples
        --------
        from fern import FernApi, RuleType

        client = FernApi()
        client.global_rules.update_global_rule_config(
            rule=RuleType.VALIDITY,
            config="FULL",
            type=RuleType.VALIDITY,
        )
        """
        _response = self._raw_client.update_global_rule_config(
            rule, config=config, type=type, request_options=request_options
        )
        return _response.data

    def delete_global_rule(self, rule: RuleType, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes a single global rule.  If this is the only rule configured, this is the same
        as deleting **all** rules.

        This operation can fail for the following reasons:

        * Invalid rule name/type (HTTP error `400`)
        * No rule with name/type `rule` exists (HTTP error `404`)
        * Rule cannot be deleted (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        rule : RuleType
            The unique name/type of a rule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi, RuleType

        client = FernApi()
        client.global_rules.delete_global_rule(
            rule=RuleType.VALIDITY,
        )
        """
        _response = self._raw_client.delete_global_rule(rule, request_options=request_options)
        return _response.data


class AsyncGlobalRulesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawGlobalRulesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawGlobalRulesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawGlobalRulesClient
        """
        return self._raw_client

    async def list_global_rules(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[RuleType]:
        """
        Gets a list of all the currently configured global rules (if any).

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[RuleType]
            The list of names of the globally configured rules.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_rules.list_global_rules()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_global_rules(request_options=request_options)
        return _response.data

    async def create_global_rule(
        self,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adds a rule to the list of globally configured rules.

        This operation can fail for the following reasons:

        * The rule type is unknown (HTTP error `400`)
        * The rule already exists (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
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
            await client.global_rules.create_global_rule(
                config="FULL",
                type=RuleType.VALIDITY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_global_rule(config=config, type=type, request_options=request_options)
        return _response.data

    async def delete_all_global_rules(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes all globally configured rules.

        This operation can fail for the following reasons:

        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
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
            await client.global_rules.delete_all_global_rules()


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_all_global_rules(request_options=request_options)
        return _response.data

    async def get_global_rule_config(
        self, rule: RuleType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Rule:
        """
        Returns information about the named globally configured rule.

        This operation can fail for the following reasons:

        * Invalid rule name/type (HTTP error `400`)
        * No rule with name/type `rule` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        rule : RuleType
            The unique name/type of a rule.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rule
            The global rule's configuration.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RuleType

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_rules.get_global_rule_config(
                rule=RuleType.VALIDITY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_global_rule_config(rule, request_options=request_options)
        return _response.data

    async def update_global_rule_config(
        self,
        rule: RuleType,
        *,
        config: str,
        type: typing.Optional[RuleType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Rule:
        """
        Updates the configuration for a globally configured rule.

        This operation can fail for the following reasons:

        * Invalid rule name/type (HTTP error `400`)
        * No rule with name/type `rule` exists (HTTP error `404`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        rule : RuleType
            The unique name/type of a rule.

        config : str

        type : typing.Optional[RuleType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Rule
            The global rule's configuration was successfully updated.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, RuleType

        client = AsyncFernApi()


        async def main() -> None:
            await client.global_rules.update_global_rule_config(
                rule=RuleType.VALIDITY,
                config="FULL",
                type=RuleType.VALIDITY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_global_rule_config(
            rule, config=config, type=type, request_options=request_options
        )
        return _response.data

    async def delete_global_rule(
        self, rule: RuleType, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes a single global rule.  If this is the only rule configured, this is the same
        as deleting **all** rules.

        This operation can fail for the following reasons:

        * Invalid rule name/type (HTTP error `400`)
        * No rule with name/type `rule` exists (HTTP error `404`)
        * Rule cannot be deleted (HTTP error `409`)
        * A server error occurred (HTTP error `500`)

        Parameters
        ----------
        rule : RuleType
            The unique name/type of a rule.

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
            await client.global_rules.delete_global_rule(
                rule=RuleType.VALIDITY,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_global_rule(rule, request_options=request_options)
        return _response.data
