

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.webhook_envelope import WebhookEnvelope
from ..types.webhook_list import WebhookList
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.webhook_toevoegen_request_event import WebhookToevoegenRequestEvent
from .types.webhook_wijzigen_request_event import WebhookWijzigenRequestEvent


OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebhooksClient
        """
        return self._raw_client

    def alle_webhooks_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookList:
        """
        All webhooks of a list in an array of member objects. The webhook objects are formatted in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookList
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.webhooks.alle_webhooks_opvragen(
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.alle_webhooks_opvragen(list_id=list_id, request_options=request_options)
        return _response.data

    def webhook_toevoegen(
        self,
        *,
        list_id: str,
        event: WebhookToevoegenRequestEvent,
        url: str,
        blocked: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookEnvelope:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        event : WebhookToevoegenRequestEvent
            When will the webhook be requested? (subscribed, modified of deactivated)

        url : str
            The URL to be accessed

        blocked : bool
            Is the accessing of the webhook (temporarily) blocked? (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            The request succeeded.

        Examples
        --------
        from fern.webhooks import WebhookToevoegenRequestEvent

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.webhooks.webhook_toevoegen(
            list_id="BaImMu3JZA",
            event=WebhookToevoegenRequestEvent.SUBSCRIBED,
            url="https://example.net/laposta-webhook",
            blocked=True,
        )
        """
        _response = self._raw_client.webhook_toevoegen(
            list_id=list_id, event=event, url=url, blocked=blocked, request_options=request_options
        )
        return _response.data

    def webhook_opvragen(
        self, webhook_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookEnvelope:
        """
        All information about a webhook

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.webhooks.webhook_opvragen(
            webhook_id="k5RaJhbnLa",
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.webhook_opvragen(webhook_id, list_id=list_id, request_options=request_options)
        return _response.data

    def webhook_wijzigen(
        self,
        webhook_id: str,
        *,
        list_id: str,
        event: typing.Optional[WebhookWijzigenRequestEvent] = OMIT,
        url: typing.Optional[str] = OMIT,
        blocked: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookEnvelope:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. Fields that are not mentioned will keep their current value fields keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        event : typing.Optional[WebhookWijzigenRequestEvent]
            When will the webhook be requested? (subscribed, modified or deactivated)

        url : typing.Optional[str]
            The URL to be accessed

        blocked : typing.Optional[bool]
            Is the accessing of the webhook (temporarily) blocked? (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.webhooks.webhook_wijzigen(
            webhook_id="k5RaJhbnLa",
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.webhook_wijzigen(
            webhook_id, list_id=list_id, event=event, url=url, blocked=blocked, request_options=request_options
        )
        return _response.data

    def webhook_verwijderen(
        self, webhook_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookEnvelope:
        """
        This permanently deletes a webhook. Potentially outstanding requests from the webhook will still be completed. If the field does not exist, an error message is displayed. In response you are shown another webhook object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the webhook.

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            The request succeeded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )
        client.webhooks.webhook_verwijderen(
            webhook_id="k5RaJhbnLa",
            list_id="BaImMu3JZA",
        )
        """
        _response = self._raw_client.webhook_verwijderen(webhook_id, list_id=list_id, request_options=request_options)
        return _response.data


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebhooksClient
        """
        return self._raw_client

    async def alle_webhooks_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookList:
        """
        All webhooks of a list in an array of member objects. The webhook objects are formatted in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookList
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.webhooks.alle_webhooks_opvragen(
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.alle_webhooks_opvragen(list_id=list_id, request_options=request_options)
        return _response.data

    async def webhook_toevoegen(
        self,
        *,
        list_id: str,
        event: WebhookToevoegenRequestEvent,
        url: str,
        blocked: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookEnvelope:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        event : WebhookToevoegenRequestEvent
            When will the webhook be requested? (subscribed, modified of deactivated)

        url : str
            The URL to be accessed

        blocked : bool
            Is the accessing of the webhook (temporarily) blocked? (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern.webhooks import WebhookToevoegenRequestEvent

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.webhooks.webhook_toevoegen(
                list_id="BaImMu3JZA",
                event=WebhookToevoegenRequestEvent.SUBSCRIBED,
                url="https://example.net/laposta-webhook",
                blocked=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.webhook_toevoegen(
            list_id=list_id, event=event, url=url, blocked=blocked, request_options=request_options
        )
        return _response.data

    async def webhook_opvragen(
        self, webhook_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookEnvelope:
        """
        All information about a webhook

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.webhooks.webhook_opvragen(
                webhook_id="k5RaJhbnLa",
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.webhook_opvragen(
            webhook_id, list_id=list_id, request_options=request_options
        )
        return _response.data

    async def webhook_wijzigen(
        self,
        webhook_id: str,
        *,
        list_id: str,
        event: typing.Optional[WebhookWijzigenRequestEvent] = OMIT,
        url: typing.Optional[str] = OMIT,
        blocked: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookEnvelope:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. Fields that are not mentioned will keep their current value fields keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        event : typing.Optional[WebhookWijzigenRequestEvent]
            When will the webhook be requested? (subscribed, modified or deactivated)

        url : typing.Optional[str]
            The URL to be accessed

        blocked : typing.Optional[bool]
            Is the accessing of the webhook (temporarily) blocked? (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.webhooks.webhook_wijzigen(
                webhook_id="k5RaJhbnLa",
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.webhook_wijzigen(
            webhook_id, list_id=list_id, event=event, url=url, blocked=blocked, request_options=request_options
        )
        return _response.data

    async def webhook_verwijderen(
        self, webhook_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookEnvelope:
        """
        This permanently deletes a webhook. Potentially outstanding requests from the webhook will still be completed. If the field does not exist, an error message is displayed. In response you are shown another webhook object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the webhook.

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookEnvelope
            The request succeeded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            leave_empty="YOUR_LEAVE_EMPTY",
        )


        async def main() -> None:
            await client.webhooks.webhook_verwijderen(
                webhook_id="k5RaJhbnLa",
                list_id="BaImMu3JZA",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.webhook_verwijderen(
            webhook_id, list_id=list_id, request_options=request_options
        )
        return _response.data
