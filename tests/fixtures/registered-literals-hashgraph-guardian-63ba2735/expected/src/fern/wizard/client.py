

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.wizard_config_policy import WizardConfigPolicy
from ..types.wizard_config_schemas_item import WizardConfigSchemasItem
from ..types.wizard_config_trust_chain_item import WizardConfigTrustChainItem
from .raw_client import AsyncRawWizardClient, RawWizardClient
from .types.post_wizard_policy_id_config_response import PostWizardPolicyIdConfigResponse
from .types.post_wizard_policy_response import PostWizardPolicyResponse
from .types.wizard_api_set_policy_async_request_wizard_config import WizardApiSetPolicyAsyncRequestWizardConfig


OMIT = typing.cast(typing.Any, ...)


class WizardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWizardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWizardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWizardClient
        """
        return self._raw_client

    def creates_a_new_policy(
        self,
        *,
        roles: typing.Sequence[str],
        policy: WizardConfigPolicy,
        schemas: typing.Sequence[WizardConfigSchemasItem],
        trust_chain: typing.Sequence[WizardConfigTrustChainItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWizardPolicyResponse:
        """
        Creates a new policy by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        roles : typing.Sequence[str]

        policy : WizardConfigPolicy

        schemas : typing.Sequence[WizardConfigSchemasItem]

        trust_chain : typing.Sequence[WizardConfigTrustChainItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWizardPolicyResponse
            Successful operation.

        Examples
        --------
        from fern import (
            FernApi,
            WizardConfigPolicy,
            WizardConfigSchemasItem,
            WizardConfigTrustChainItem,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wizard.creates_a_new_policy(
            roles=["roles"],
            policy=WizardConfigPolicy(),
            schemas=[WizardConfigSchemasItem()],
            trust_chain=[WizardConfigTrustChainItem()],
        )
        """
        _response = self._raw_client.creates_a_new_policy(
            roles=roles, policy=policy, schemas=schemas, trust_chain=trust_chain, request_options=request_options
        )
        return _response.data

    def wizard_api_set_policy_async(
        self,
        *,
        save_state: typing.Optional[bool] = OMIT,
        wizard_config: typing.Optional[WizardApiSetPolicyAsyncRequestWizardConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Creates a new policy by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        save_state : typing.Optional[bool]

        wizard_config : typing.Optional[WizardApiSetPolicyAsyncRequestWizardConfig]

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
        client.wizard.wizard_api_set_policy_async()
        """
        _response = self._raw_client.wizard_api_set_policy_async(
            save_state=save_state, wizard_config=wizard_config, request_options=request_options
        )
        return _response.data

    def get_policy_config(
        self,
        policy_id: str,
        *,
        roles: typing.Sequence[str],
        policy: WizardConfigPolicy,
        schemas: typing.Sequence[WizardConfigSchemasItem],
        trust_chain: typing.Sequence[WizardConfigTrustChainItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWizardPolicyIdConfigResponse:
        """
        Get policy config by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy identifier.

        roles : typing.Sequence[str]

        policy : WizardConfigPolicy

        schemas : typing.Sequence[WizardConfigSchemasItem]

        trust_chain : typing.Sequence[WizardConfigTrustChainItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWizardPolicyIdConfigResponse
            Successful operation.

        Examples
        --------
        from fern import (
            FernApi,
            WizardConfigPolicy,
            WizardConfigSchemasItem,
            WizardConfigTrustChainItem,
        )

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.wizard.get_policy_config(
            policy_id="policyId",
            roles=["roles"],
            policy=WizardConfigPolicy(),
            schemas=[WizardConfigSchemasItem()],
            trust_chain=[WizardConfigTrustChainItem()],
        )
        """
        _response = self._raw_client.get_policy_config(
            policy_id,
            roles=roles,
            policy=policy,
            schemas=schemas,
            trust_chain=trust_chain,
            request_options=request_options,
        )
        return _response.data


class AsyncWizardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWizardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWizardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWizardClient
        """
        return self._raw_client

    async def creates_a_new_policy(
        self,
        *,
        roles: typing.Sequence[str],
        policy: WizardConfigPolicy,
        schemas: typing.Sequence[WizardConfigSchemasItem],
        trust_chain: typing.Sequence[WizardConfigTrustChainItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWizardPolicyResponse:
        """
        Creates a new policy by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        roles : typing.Sequence[str]

        policy : WizardConfigPolicy

        schemas : typing.Sequence[WizardConfigSchemasItem]

        trust_chain : typing.Sequence[WizardConfigTrustChainItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWizardPolicyResponse
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            WizardConfigPolicy,
            WizardConfigSchemasItem,
            WizardConfigTrustChainItem,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wizard.creates_a_new_policy(
                roles=["roles"],
                policy=WizardConfigPolicy(),
                schemas=[WizardConfigSchemasItem()],
                trust_chain=[WizardConfigTrustChainItem()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_new_policy(
            roles=roles, policy=policy, schemas=schemas, trust_chain=trust_chain, request_options=request_options
        )
        return _response.data

    async def wizard_api_set_policy_async(
        self,
        *,
        save_state: typing.Optional[bool] = OMIT,
        wizard_config: typing.Optional[WizardApiSetPolicyAsyncRequestWizardConfig] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        Creates a new policy by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        save_state : typing.Optional[bool]

        wizard_config : typing.Optional[WizardApiSetPolicyAsyncRequestWizardConfig]

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
            await client.wizard.wizard_api_set_policy_async()


        asyncio.run(main())
        """
        _response = await self._raw_client.wizard_api_set_policy_async(
            save_state=save_state, wizard_config=wizard_config, request_options=request_options
        )
        return _response.data

    async def get_policy_config(
        self,
        policy_id: str,
        *,
        roles: typing.Sequence[str],
        policy: WizardConfigPolicy,
        schemas: typing.Sequence[WizardConfigSchemasItem],
        trust_chain: typing.Sequence[WizardConfigTrustChainItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostWizardPolicyIdConfigResponse:
        """
        Get policy config by wizard. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy identifier.

        roles : typing.Sequence[str]

        policy : WizardConfigPolicy

        schemas : typing.Sequence[WizardConfigSchemasItem]

        trust_chain : typing.Sequence[WizardConfigTrustChainItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostWizardPolicyIdConfigResponse
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            WizardConfigPolicy,
            WizardConfigSchemasItem,
            WizardConfigTrustChainItem,
        )

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.wizard.get_policy_config(
                policy_id="policyId",
                roles=["roles"],
                policy=WizardConfigPolicy(),
                schemas=[WizardConfigSchemasItem()],
                trust_chain=[WizardConfigTrustChainItem()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_policy_config(
            policy_id,
            roles=roles,
            policy=policy,
            schemas=schemas,
            trust_chain=trust_chain,
            request_options=request_options,
        )
        return _response.data
