

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.webhook_id import WebhookId
from .raw_client import AsyncRawManagementApiWebhooksClient, RawManagementApiWebhooksClient
from .types.create_webhook_request_source import CreateWebhookRequestSource
from .types.create_webhook_request_triggers_item import CreateWebhookRequestTriggersItem
from .types.create_webhook_response import CreateWebhookResponse
from .types.delete_webhook_response import DeleteWebhookResponse
from .types.get_webhook_response import GetWebhookResponse
from .types.get_webhooks_request_filter_date_field import GetWebhooksRequestFilterDateField
from .types.get_webhooks_request_order import GetWebhooksRequestOrder
from .types.get_webhooks_request_sort_by import GetWebhooksRequestSortBy
from .types.get_webhooks_response import GetWebhooksResponse
from .types.update_webhook_request_source import UpdateWebhookRequestSource
from .types.update_webhook_request_triggers_item import UpdateWebhookRequestTriggersItem
from .types.update_webhook_response import UpdateWebhookResponse


OMIT = typing.cast(typing.Any, ...)


class ManagementApiWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawManagementApiWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawManagementApiWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawManagementApiWebhooksClient
        """
        return self._raw_client

    def get_webhooks(
        self,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetWebhooksRequestSortBy] = None,
        order: typing.Optional[GetWebhooksRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetWebhooksRequestFilterDateField] = None,
        survey_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWebhooksResponse:
        """
        Gets webhooks from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetWebhooksRequestSortBy]
            Sort by field

        order : typing.Optional[GetWebhooksRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetWebhooksRequestFilterDateField]
            Date field to filter by

        survey_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Webhooks retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_webhooks.get_webhooks()
        """
        _response = self._raw_client.get_webhooks(
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            survey_ids=survey_ids,
            request_options=request_options,
        )
        return _response.data

    def create_webhook(
        self,
        *,
        url: str,
        source: CreateWebhookRequestSource,
        workspace_id: str,
        triggers: typing.Sequence[CreateWebhookRequestTriggersItem],
        survey_ids: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhookResponse:
        """
        Creates a webhook in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        url : str
            The URL of the webhook

        source : CreateWebhookRequestSource
            The source of the webhook

        workspace_id : str
            The ID of the Workspace

        triggers : typing.Sequence[CreateWebhookRequestTriggersItem]
            The triggers of the webhook

        survey_ids : typing.Sequence[str]
            The IDs of the surveys

        name : typing.Optional[str]
            The name of the webhook

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhookResponse
            Webhook created successfully.

        Examples
        --------
        from fern.management_api_webhooks import (
            CreateWebhookRequestSource,
            CreateWebhookRequestTriggersItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_webhooks.create_webhook(
            url="url",
            source=CreateWebhookRequestSource.USER,
            workspace_id="workspaceId",
            triggers=[CreateWebhookRequestTriggersItem.RESPONSE_FINISHED],
            survey_ids=["surveyIds"],
        )
        """
        _response = self._raw_client.create_webhook(
            url=url,
            source=source,
            workspace_id=workspace_id,
            triggers=triggers,
            survey_ids=survey_ids,
            name=name,
            environment_id=environment_id,
            request_options=request_options,
        )
        return _response.data

    def get_webhook(
        self, id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookResponse:
        """
        Gets a webhook from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        id : WebhookId
            The ID of the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookResponse
            Webhook retrieved successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_webhooks.get_webhook(
            id="id",
        )
        """
        _response = self._raw_client.get_webhook(id, request_options=request_options)
        return _response.data

    def update_webhook(
        self,
        id: WebhookId,
        *,
        url: str,
        source: UpdateWebhookRequestSource,
        workspace_id: str,
        triggers: typing.Sequence[UpdateWebhookRequestTriggersItem],
        survey_ids: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookResponse:
        """
        Updates a webhook in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        id : WebhookId
            The ID of the webhook

        url : str
            The URL of the webhook

        source : UpdateWebhookRequestSource
            The source of the webhook

        workspace_id : str
            The ID of the Workspace

        triggers : typing.Sequence[UpdateWebhookRequestTriggersItem]
            The triggers of the webhook

        survey_ids : typing.Sequence[str]
            The IDs of the surveys

        name : typing.Optional[str]
            The name of the webhook

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookResponse
            Webhook updated successfully.

        Examples
        --------
        from fern.management_api_webhooks import (
            UpdateWebhookRequestSource,
            UpdateWebhookRequestTriggersItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_webhooks.update_webhook(
            id="id",
            url="url",
            source=UpdateWebhookRequestSource.USER,
            workspace_id="workspaceId",
            triggers=[UpdateWebhookRequestTriggersItem.RESPONSE_FINISHED],
            survey_ids=["surveyIds"],
        )
        """
        _response = self._raw_client.update_webhook(
            id,
            url=url,
            source=source,
            workspace_id=workspace_id,
            triggers=triggers,
            survey_ids=survey_ids,
            name=name,
            environment_id=environment_id,
            request_options=request_options,
        )
        return _response.data

    def delete_webhook(
        self, id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWebhookResponse:
        """
        Deletes a webhook from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        id : WebhookId
            The ID of the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhookResponse
            Webhook deleted successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.management_api_webhooks.delete_webhook(
            id="id",
        )
        """
        _response = self._raw_client.delete_webhook(id, request_options=request_options)
        return _response.data


class AsyncManagementApiWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawManagementApiWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawManagementApiWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawManagementApiWebhooksClient
        """
        return self._raw_client

    async def get_webhooks(
        self,
        *,
        limit: typing.Optional[float] = None,
        skip: typing.Optional[float] = None,
        sort_by: typing.Optional[GetWebhooksRequestSortBy] = None,
        order: typing.Optional[GetWebhooksRequestOrder] = None,
        start_date: typing.Optional[str] = None,
        end_date: typing.Optional[str] = None,
        filter_date_field: typing.Optional[GetWebhooksRequestFilterDateField] = None,
        survey_ids: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetWebhooksResponse:
        """
        Gets webhooks from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        limit : typing.Optional[float]
            Number of items to return

        skip : typing.Optional[float]
            Number of items to skip

        sort_by : typing.Optional[GetWebhooksRequestSortBy]
            Sort by field

        order : typing.Optional[GetWebhooksRequestOrder]
            Sort order

        start_date : typing.Optional[str]
            Start date

        end_date : typing.Optional[str]
            End date

        filter_date_field : typing.Optional[GetWebhooksRequestFilterDateField]
            Date field to filter by

        survey_ids : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Webhooks retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_webhooks.get_webhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhooks(
            limit=limit,
            skip=skip,
            sort_by=sort_by,
            order=order,
            start_date=start_date,
            end_date=end_date,
            filter_date_field=filter_date_field,
            survey_ids=survey_ids,
            request_options=request_options,
        )
        return _response.data

    async def create_webhook(
        self,
        *,
        url: str,
        source: CreateWebhookRequestSource,
        workspace_id: str,
        triggers: typing.Sequence[CreateWebhookRequestTriggersItem],
        survey_ids: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateWebhookResponse:
        """
        Creates a webhook in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        url : str
            The URL of the webhook

        source : CreateWebhookRequestSource
            The source of the webhook

        workspace_id : str
            The ID of the Workspace

        triggers : typing.Sequence[CreateWebhookRequestTriggersItem]
            The triggers of the webhook

        survey_ids : typing.Sequence[str]
            The IDs of the surveys

        name : typing.Optional[str]
            The name of the webhook

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateWebhookResponse
            Webhook created successfully.

        Examples
        --------
        import asyncio

        from fern.management_api_webhooks import (
            CreateWebhookRequestSource,
            CreateWebhookRequestTriggersItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_webhooks.create_webhook(
                url="url",
                source=CreateWebhookRequestSource.USER,
                workspace_id="workspaceId",
                triggers=[CreateWebhookRequestTriggersItem.RESPONSE_FINISHED],
                survey_ids=["surveyIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook(
            url=url,
            source=source,
            workspace_id=workspace_id,
            triggers=triggers,
            survey_ids=survey_ids,
            name=name,
            environment_id=environment_id,
            request_options=request_options,
        )
        return _response.data

    async def get_webhook(
        self, id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhookResponse:
        """
        Gets a webhook from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        id : WebhookId
            The ID of the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhookResponse
            Webhook retrieved successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_webhooks.get_webhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhook(id, request_options=request_options)
        return _response.data

    async def update_webhook(
        self,
        id: WebhookId,
        *,
        url: str,
        source: UpdateWebhookRequestSource,
        workspace_id: str,
        triggers: typing.Sequence[UpdateWebhookRequestTriggersItem],
        survey_ids: typing.Sequence[str],
        name: typing.Optional[str] = OMIT,
        environment_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateWebhookResponse:
        """
        Updates a webhook in the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        id : WebhookId
            The ID of the webhook

        url : str
            The URL of the webhook

        source : UpdateWebhookRequestSource
            The source of the webhook

        workspace_id : str
            The ID of the Workspace

        triggers : typing.Sequence[UpdateWebhookRequestTriggersItem]
            The triggers of the webhook

        survey_ids : typing.Sequence[str]
            The IDs of the surveys

        name : typing.Optional[str]
            The name of the webhook

        environment_id : typing.Optional[str]
            Deprecated alias for workspaceId.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateWebhookResponse
            Webhook updated successfully.

        Examples
        --------
        import asyncio

        from fern.management_api_webhooks import (
            UpdateWebhookRequestSource,
            UpdateWebhookRequestTriggersItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_webhooks.update_webhook(
                id="id",
                url="url",
                source=UpdateWebhookRequestSource.USER,
                workspace_id="workspaceId",
                triggers=[UpdateWebhookRequestTriggersItem.RESPONSE_FINISHED],
                survey_ids=["surveyIds"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook(
            id,
            url=url,
            source=source,
            workspace_id=workspace_id,
            triggers=triggers,
            survey_ids=survey_ids,
            name=name,
            environment_id=environment_id,
            request_options=request_options,
        )
        return _response.data

    async def delete_webhook(
        self, id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteWebhookResponse:
        """
        Deletes a webhook from the database. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        id : WebhookId
            The ID of the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteWebhookResponse
            Webhook deleted successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.management_api_webhooks.delete_webhook(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhook(id, request_options=request_options)
        return _response.data
