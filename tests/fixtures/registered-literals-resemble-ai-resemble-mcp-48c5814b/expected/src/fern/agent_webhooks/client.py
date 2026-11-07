

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAgentWebhooksClient, RawAgentWebhooksClient
from .types.create_agent_webhook_request_webhook_type import CreateAgentWebhookRequestWebhookType
from .types.create_agent_webhook_response import CreateAgentWebhookResponse
from .types.delete_agent_webhook_response import DeleteAgentWebhookResponse
from .types.get_agent_webhook_response import GetAgentWebhookResponse
from .types.list_agent_webhooks_response import ListAgentWebhooksResponse
from .types.update_agent_webhook_response import UpdateAgentWebhookResponse


OMIT = typing.cast(typing.Any, ...)


class AgentWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAgentWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAgentWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAgentWebhooksClient
        """
        return self._raw_client

    def list_agent_webhooks(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAgentWebhooksResponse:
        """
        List all webhooks for an agent

        Parameters
        ----------
        agent_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentWebhooksResponse
            List of webhooks

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_webhooks.list_agent_webhooks(
            agent_uuid="agent_uuid",
        )
        """
        _response = self._raw_client.list_agent_webhooks(agent_uuid, request_options=request_options)
        return _response.data

    def create_agent_webhook(
        self,
        agent_uuid: str,
        *,
        webhook_type: CreateAgentWebhookRequestWebhookType,
        webhook_config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAgentWebhookResponse:
        """
        Create a new webhook for an agent

        Parameters
        ----------
        agent_uuid : str

        webhook_type : CreateAgentWebhookRequestWebhookType

        webhook_config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentWebhookResponse
            Webhook created

        Examples
        --------
        from fern.agent_webhooks import CreateAgentWebhookRequestWebhookType

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_webhooks.create_agent_webhook(
            agent_uuid="agent_uuid",
            webhook_type=CreateAgentWebhookRequestWebhookType.PRE_CALL,
            webhook_config={"key": "value"},
        )
        """
        _response = self._raw_client.create_agent_webhook(
            agent_uuid, webhook_type=webhook_type, webhook_config=webhook_config, request_options=request_options
        )
        return _response.data

    def get_agent_webhook(
        self, agent_uuid: str, webhook_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentWebhookResponse:
        """
        Get details of a specific webhook

        Parameters
        ----------
        agent_uuid : str

        webhook_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentWebhookResponse
            Webhook details

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_webhooks.get_agent_webhook(
            agent_uuid="agent_uuid",
            webhook_uuid="webhook_uuid",
        )
        """
        _response = self._raw_client.get_agent_webhook(agent_uuid, webhook_uuid, request_options=request_options)
        return _response.data

    def delete_agent_webhook(
        self, agent_uuid: str, webhook_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAgentWebhookResponse:
        """
        Delete a webhook

        Parameters
        ----------
        agent_uuid : str

        webhook_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAgentWebhookResponse
            Webhook deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_webhooks.delete_agent_webhook(
            agent_uuid="agent_uuid",
            webhook_uuid="webhook_uuid",
        )
        """
        _response = self._raw_client.delete_agent_webhook(agent_uuid, webhook_uuid, request_options=request_options)
        return _response.data

    def update_agent_webhook(
        self,
        agent_uuid: str,
        webhook_uuid: str,
        *,
        webhook_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAgentWebhookResponse:
        """
        Update an existing webhook

        Parameters
        ----------
        agent_uuid : str

        webhook_uuid : str

        webhook_config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAgentWebhookResponse
            Webhook updated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.agent_webhooks.update_agent_webhook(
            agent_uuid="agent_uuid",
            webhook_uuid="webhook_uuid",
        )
        """
        _response = self._raw_client.update_agent_webhook(
            agent_uuid, webhook_uuid, webhook_config=webhook_config, request_options=request_options
        )
        return _response.data


class AsyncAgentWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAgentWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAgentWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAgentWebhooksClient
        """
        return self._raw_client

    async def list_agent_webhooks(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAgentWebhooksResponse:
        """
        List all webhooks for an agent

        Parameters
        ----------
        agent_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAgentWebhooksResponse
            List of webhooks

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_webhooks.list_agent_webhooks(
                agent_uuid="agent_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_agent_webhooks(agent_uuid, request_options=request_options)
        return _response.data

    async def create_agent_webhook(
        self,
        agent_uuid: str,
        *,
        webhook_type: CreateAgentWebhookRequestWebhookType,
        webhook_config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateAgentWebhookResponse:
        """
        Create a new webhook for an agent

        Parameters
        ----------
        agent_uuid : str

        webhook_type : CreateAgentWebhookRequestWebhookType

        webhook_config : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateAgentWebhookResponse
            Webhook created

        Examples
        --------
        import asyncio

        from fern.agent_webhooks import CreateAgentWebhookRequestWebhookType

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_webhooks.create_agent_webhook(
                agent_uuid="agent_uuid",
                webhook_type=CreateAgentWebhookRequestWebhookType.PRE_CALL,
                webhook_config={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_agent_webhook(
            agent_uuid, webhook_type=webhook_type, webhook_config=webhook_config, request_options=request_options
        )
        return _response.data

    async def get_agent_webhook(
        self, agent_uuid: str, webhook_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAgentWebhookResponse:
        """
        Get details of a specific webhook

        Parameters
        ----------
        agent_uuid : str

        webhook_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAgentWebhookResponse
            Webhook details

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_webhooks.get_agent_webhook(
                agent_uuid="agent_uuid",
                webhook_uuid="webhook_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_agent_webhook(agent_uuid, webhook_uuid, request_options=request_options)
        return _response.data

    async def delete_agent_webhook(
        self, agent_uuid: str, webhook_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAgentWebhookResponse:
        """
        Delete a webhook

        Parameters
        ----------
        agent_uuid : str

        webhook_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAgentWebhookResponse
            Webhook deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_webhooks.delete_agent_webhook(
                agent_uuid="agent_uuid",
                webhook_uuid="webhook_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_agent_webhook(
            agent_uuid, webhook_uuid, request_options=request_options
        )
        return _response.data

    async def update_agent_webhook(
        self,
        agent_uuid: str,
        webhook_uuid: str,
        *,
        webhook_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateAgentWebhookResponse:
        """
        Update an existing webhook

        Parameters
        ----------
        agent_uuid : str

        webhook_uuid : str

        webhook_config : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateAgentWebhookResponse
            Webhook updated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.agent_webhooks.update_agent_webhook(
                agent_uuid="agent_uuid",
                webhook_uuid="webhook_uuid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_agent_webhook(
            agent_uuid, webhook_uuid, webhook_config=webhook_config, request_options=request_options
        )
        return _response.data
