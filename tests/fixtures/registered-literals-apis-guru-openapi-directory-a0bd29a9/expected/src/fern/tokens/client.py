

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.delegate_identity import DelegateIdentity
from ..types.plan_resource_headers import PlanResourceHeaders
from ..types.plan_resource_identity import PlanResourceIdentity
from ..types.plan_resource_properties import PlanResourceProperties
from .raw_client import AsyncRawTokensClient, RawTokensClient


OMIT = typing.cast(typing.Any, ...)


class TokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTokensClient
        """
        return self._raw_client

    def post_api_v1tokens_plans_plan_name_delete_all_codespaces(
        self,
        plan_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        subscription_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        plan_name : str

        expiration : typing.Optional[dt.datetime]

        subscription_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.post_api_v1tokens_plans_plan_name_delete_all_codespaces(
            plan_name="planName",
        )
        """
        _response = self._raw_client.post_api_v1tokens_plans_plan_name_delete_all_codespaces(
            plan_name, expiration=expiration, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    def post_api_v1tokens_plans_plan_name_read_all_codespaces(
        self,
        plan_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        subscription_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        plan_name : str

        expiration : typing.Optional[dt.datetime]

        subscription_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.post_api_v1tokens_plans_plan_name_read_all_codespaces(
            plan_name="planName",
        )
        """
        _response = self._raw_client.post_api_v1tokens_plans_plan_name_read_all_codespaces(
            plan_name, expiration=expiration, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    def post_api_v1tokens_plans_plan_name_write_codespaces(
        self,
        plan_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        subscription_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        plan_name : str

        expiration : typing.Optional[dt.datetime]

        subscription_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.post_api_v1tokens_plans_plan_name_write_codespaces(
            plan_name="planName",
        )
        """
        _response = self._raw_client.post_api_v1tokens_plans_plan_name_write_codespaces(
            plan_name, expiration=expiration, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    def post_api_v1tokens_plans_plan_name_write_delegates(
        self,
        plan_name: str,
        *,
        subscription_id: typing.Optional[str] = None,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        plan_name : str

        subscription_id : typing.Optional[str]

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.post_api_v1tokens_plans_plan_name_write_delegates(
            plan_name="planName",
        )
        """
        _response = self._raw_client.post_api_v1tokens_plans_plan_name_write_delegates(
            plan_name,
            subscription_id=subscription_id,
            environment_ids=environment_ids,
            expiration=expiration,
            identity=identity,
            port_numbers=port_numbers,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    def put_api_v1tokens_subscriptions_subscription_id_resource_groups_resource_group_providers_provider_namespace_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        provider_namespace: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        provider_namespace : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.tokens.put_api_v1tokens_subscriptions_subscription_id_resource_groups_resource_group_providers_provider_namespace_plans_resource_name(
            subscription_id="subscriptionId",
            resource_group="resourceGroup",
            provider_namespace="providerNamespace",
            resource_name="resourceName",
        )
        """
        _response = self._raw_client.put_api_v1tokens_subscriptions_subscription_id_resource_groups_resource_group_providers_provider_namespace_plans_resource_name(
            subscription_id,
            resource_group,
            provider_namespace,
            resource_name,
            headers=headers,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data


class AsyncTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTokensClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTokensClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTokensClient
        """
        return self._raw_client

    async def post_api_v1tokens_plans_plan_name_delete_all_codespaces(
        self,
        plan_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        subscription_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        plan_name : str

        expiration : typing.Optional[dt.datetime]

        subscription_id : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.post_api_v1tokens_plans_plan_name_delete_all_codespaces(
                plan_name="planName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1tokens_plans_plan_name_delete_all_codespaces(
            plan_name, expiration=expiration, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    async def post_api_v1tokens_plans_plan_name_read_all_codespaces(
        self,
        plan_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        subscription_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        plan_name : str

        expiration : typing.Optional[dt.datetime]

        subscription_id : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.post_api_v1tokens_plans_plan_name_read_all_codespaces(
                plan_name="planName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1tokens_plans_plan_name_read_all_codespaces(
            plan_name, expiration=expiration, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    async def post_api_v1tokens_plans_plan_name_write_codespaces(
        self,
        plan_name: str,
        *,
        expiration: typing.Optional[dt.datetime] = None,
        subscription_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        plan_name : str

        expiration : typing.Optional[dt.datetime]

        subscription_id : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.post_api_v1tokens_plans_plan_name_write_codespaces(
                plan_name="planName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1tokens_plans_plan_name_write_codespaces(
            plan_name, expiration=expiration, subscription_id=subscription_id, request_options=request_options
        )
        return _response.data

    async def post_api_v1tokens_plans_plan_name_write_delegates(
        self,
        plan_name: str,
        *,
        subscription_id: typing.Optional[str] = None,
        environment_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        expiration: typing.Optional[dt.datetime] = OMIT,
        identity: typing.Optional[DelegateIdentity] = OMIT,
        port_numbers: typing.Optional[typing.Sequence[int]] = OMIT,
        scope: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        plan_name : str

        subscription_id : typing.Optional[str]

        environment_ids : typing.Optional[typing.Sequence[str]]

        expiration : typing.Optional[dt.datetime]

        identity : typing.Optional[DelegateIdentity]

        port_numbers : typing.Optional[typing.Sequence[int]]

        scope : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.post_api_v1tokens_plans_plan_name_write_delegates(
                plan_name="planName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_v1tokens_plans_plan_name_write_delegates(
            plan_name,
            subscription_id=subscription_id,
            environment_ids=environment_ids,
            expiration=expiration,
            identity=identity,
            port_numbers=port_numbers,
            scope=scope,
            request_options=request_options,
        )
        return _response.data

    async def put_api_v1tokens_subscriptions_subscription_id_resource_groups_resource_group_providers_provider_namespace_plans_resource_name(
        self,
        subscription_id: str,
        resource_group: str,
        provider_namespace: str,
        resource_name: str,
        *,
        headers: typing.Optional[PlanResourceHeaders] = None,
        id: typing.Optional[str] = OMIT,
        identity: typing.Optional[PlanResourceIdentity] = OMIT,
        location: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        properties: typing.Optional[PlanResourceProperties] = OMIT,
        provisioning_state: typing.Optional[str] = OMIT,
        tags: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        type: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        subscription_id : str

        resource_group : str

        provider_namespace : str

        resource_name : str

        headers : typing.Optional[PlanResourceHeaders]

        id : typing.Optional[str]

        identity : typing.Optional[PlanResourceIdentity]

        location : typing.Optional[str]

        name : typing.Optional[str]

        properties : typing.Optional[PlanResourceProperties]

        provisioning_state : typing.Optional[str]

        tags : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        type : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.tokens.put_api_v1tokens_subscriptions_subscription_id_resource_groups_resource_group_providers_provider_namespace_plans_resource_name(
                subscription_id="subscriptionId",
                resource_group="resourceGroup",
                provider_namespace="providerNamespace",
                resource_name="resourceName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_v1tokens_subscriptions_subscription_id_resource_groups_resource_group_providers_provider_namespace_plans_resource_name(
            subscription_id,
            resource_group,
            provider_namespace,
            resource_name,
            headers=headers,
            id=id,
            identity=identity,
            location=location,
            name=name,
            properties=properties,
            provisioning_state=provisioning_state,
            tags=tags,
            type=type,
            request_options=request_options,
        )
        return _response.data
