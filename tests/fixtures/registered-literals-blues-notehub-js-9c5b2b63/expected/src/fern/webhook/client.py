

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.webhook_settings import WebhookSettings
from .raw_client import AsyncRawWebhookClient, RawWebhookClient
from .types.get_webhooks_response import GetWebhooksResponse


OMIT = typing.cast(typing.Any, ...)


class WebhookClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebhookClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebhookClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebhookClient
        """
        return self._raw_client

    def create_legacy_webhook_event(
        self,
        product_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Legacy endpoint for sending an event from a webhook, associated with the given device (provisioning it if necessary). The request body is a Note-shaped object containing the notefile name, body, and optional payload.

        Parameters
        ----------
        product_uid : str

        device_uid : str

        request : typing.Dict[str, typing.Any]

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
        client.webhook.create_legacy_webhook_event(
            product_uid="com.blues.bridge:sensors",
            device_uid="dev:000000000000000",
            request={
                "body": {"key": "value"},
                "file": "data.qo",
                "payload": "SGVsbG8sIFdvcmxkIQ==",
            },
        )
        """
        _response = self._raw_client.create_legacy_webhook_event(
            product_uid, device_uid, request=request, request_options=request_options
        )
        return _response.data

    def update_legacy_webhook_session(
        self,
        product_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Legacy endpoint for opening or updating a webhook session for the given device (provisioning the device if necessary). Used by external services that need to maintain a callable session against a device behind a webhook.

        Parameters
        ----------
        product_uid : str

        device_uid : str

        request : typing.Dict[str, typing.Any]

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
        client.webhook.update_legacy_webhook_session(
            product_uid="com.blues.bridge:sensors",
            device_uid="dev:000000000000000",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.update_legacy_webhook_session(
            product_uid, device_uid, request=request, request_options=request_options
        )
        return _response.data

    def create_webhook_device_event_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sends an event to be processed by the specified webhook, addressed by productUID, associated with the given device (provisioning it if necessary). The entire request body becomes the event body. The webhook's configured JSONata transform, if any, is applied before routing.

        Parameters
        ----------
        product_uid : str

        webhook_uid : str
            Webhook UID

        device_uid : str

        request : typing.Dict[str, typing.Any]

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
        client.webhook.create_webhook_device_event_by_product(
            product_uid="com.blues.bridge:sensors",
            webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
            device_uid="dev:000000000000000",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_webhook_device_event_by_product(
            product_uid, webhook_uid, device_uid, request=request, request_options=request_options
        )
        return _response.data

    def create_webhook_event_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sends an event to be processed by the specified webhook, addressed by productUID. The entire request body becomes the event body. The webhook's configured JSONata transform, if any, is applied before routing. The event is not associated with a specific device.

        Parameters
        ----------
        product_uid : str

        webhook_uid : str
            Webhook UID

        request : typing.Dict[str, typing.Any]

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
        client.webhook.create_webhook_event_by_product(
            product_uid="com.blues.bridge:sensors",
            webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.create_webhook_event_by_product(
            product_uid, webhook_uid, request=request, request_options=request_options
        )
        return _response.data

    def get_webhook_settings_by_product(
        self, product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookSettings:
        """
        Retrieves the configuration settings for the specified webhook, addressed by productUID.

        Parameters
        ----------
        product_uid : str

        webhook_uid : str
            Webhook UID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookSettings
            Webhook settings retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhook.get_webhook_settings_by_product(
            product_uid="com.blues.bridge:sensors",
            webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
        )
        """
        _response = self._raw_client.get_webhook_settings_by_product(
            product_uid, webhook_uid, request_options=request_options
        )
        return _response.data

    def update_webhook_settings_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the configuration settings for the specified webhook, addressed by productUID. Update body will completely replace the existing settings.

        Parameters
        ----------
        product_uid : str

        webhook_uid : str
            Webhook UID

        disabled : typing.Optional[bool]
            Flag indicating if the webhook is disabled

        id : typing.Optional[str]
            Webhook ID

        transform : typing.Optional[str]
            Transformation to be applied to the event

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
        client.webhook.update_webhook_settings_by_product(
            product_uid="com.blues.bridge:sensors",
            webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
            disabled=False,
            transform='{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
        )
        """
        _response = self._raw_client.update_webhook_settings_by_product(
            product_uid, webhook_uid, disabled=disabled, id=id, transform=transform, request_options=request_options
        )
        return _response.data

    def get_webhooks(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhooksResponse:
        """
        Retrieves all webhooks for the specified project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Webhooks retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhook.get_webhooks(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
        )
        """
        _response = self._raw_client.get_webhooks(project_or_product_uid, request_options=request_options)
        return _response.data

    def get_webhook(
        self, project_or_product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookSettings:
        """
        Retrieves the configuration settings for the specified webhook

        Parameters
        ----------
        project_or_product_uid : str

        webhook_uid : str
            Webhook UID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookSettings
            Webhook settings retrieved successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.webhook.get_webhook(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
        )
        """
        _response = self._raw_client.get_webhook(project_or_product_uid, webhook_uid, request_options=request_options)
        return _response.data

    def create_webhook(
        self,
        project_or_product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a webhook for the specified product with the given name. The name | must be unique within the project.

        Parameters
        ----------
        project_or_product_uid : str

        webhook_uid : str
            Webhook UID

        disabled : typing.Optional[bool]
            Flag indicating if the webhook is disabled

        id : typing.Optional[str]
            Webhook ID

        transform : typing.Optional[str]
            Transformation to be applied to the event

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
        client.webhook.create_webhook(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
        )
        """
        _response = self._raw_client.create_webhook(
            project_or_product_uid,
            webhook_uid,
            disabled=disabled,
            id=id,
            transform=transform,
            request_options=request_options,
        )
        return _response.data

    def update_webhook(
        self,
        project_or_product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the configuration settings for the specified webhook. | Webhook will be created if it does not exist. Update body will completely replace the existing settings.

        Parameters
        ----------
        project_or_product_uid : str

        webhook_uid : str
            Webhook UID

        disabled : typing.Optional[bool]
            Flag indicating if the webhook is disabled

        id : typing.Optional[str]
            Webhook ID

        transform : typing.Optional[str]
            Transformation to be applied to the event

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
        client.webhook.update_webhook(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
            disabled=False,
            transform='{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
        )
        """
        _response = self._raw_client.update_webhook(
            project_or_product_uid,
            webhook_uid,
            disabled=disabled,
            id=id,
            transform=transform,
            request_options=request_options,
        )
        return _response.data

    def delete_webhook(
        self, project_or_product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the specified webhook

        Parameters
        ----------
        project_or_product_uid : str

        webhook_uid : str
            Webhook UID

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
        client.webhook.delete_webhook(
            project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
        )
        """
        _response = self._raw_client.delete_webhook(
            project_or_product_uid, webhook_uid, request_options=request_options
        )
        return _response.data


class AsyncWebhookClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebhookClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebhookClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebhookClient
        """
        return self._raw_client

    async def create_legacy_webhook_event(
        self,
        product_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Legacy endpoint for sending an event from a webhook, associated with the given device (provisioning it if necessary). The request body is a Note-shaped object containing the notefile name, body, and optional payload.

        Parameters
        ----------
        product_uid : str

        device_uid : str

        request : typing.Dict[str, typing.Any]

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
            await client.webhook.create_legacy_webhook_event(
                product_uid="com.blues.bridge:sensors",
                device_uid="dev:000000000000000",
                request={
                    "body": {"key": "value"},
                    "file": "data.qo",
                    "payload": "SGVsbG8sIFdvcmxkIQ==",
                },
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_legacy_webhook_event(
            product_uid, device_uid, request=request, request_options=request_options
        )
        return _response.data

    async def update_legacy_webhook_session(
        self,
        product_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Legacy endpoint for opening or updating a webhook session for the given device (provisioning the device if necessary). Used by external services that need to maintain a callable session against a device behind a webhook.

        Parameters
        ----------
        product_uid : str

        device_uid : str

        request : typing.Dict[str, typing.Any]

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
            await client.webhook.update_legacy_webhook_session(
                product_uid="com.blues.bridge:sensors",
                device_uid="dev:000000000000000",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_legacy_webhook_session(
            product_uid, device_uid, request=request, request_options=request_options
        )
        return _response.data

    async def create_webhook_device_event_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sends an event to be processed by the specified webhook, addressed by productUID, associated with the given device (provisioning it if necessary). The entire request body becomes the event body. The webhook's configured JSONata transform, if any, is applied before routing.

        Parameters
        ----------
        product_uid : str

        webhook_uid : str
            Webhook UID

        device_uid : str

        request : typing.Dict[str, typing.Any]

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
            await client.webhook.create_webhook_device_event_by_product(
                product_uid="com.blues.bridge:sensors",
                webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
                device_uid="dev:000000000000000",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook_device_event_by_product(
            product_uid, webhook_uid, device_uid, request=request, request_options=request_options
        )
        return _response.data

    async def create_webhook_event_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Sends an event to be processed by the specified webhook, addressed by productUID. The entire request body becomes the event body. The webhook's configured JSONata transform, if any, is applied before routing. The event is not associated with a specific device.

        Parameters
        ----------
        product_uid : str

        webhook_uid : str
            Webhook UID

        request : typing.Dict[str, typing.Any]

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
            await client.webhook.create_webhook_event_by_product(
                product_uid="com.blues.bridge:sensors",
                webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook_event_by_product(
            product_uid, webhook_uid, request=request, request_options=request_options
        )
        return _response.data

    async def get_webhook_settings_by_product(
        self, product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookSettings:
        """
        Retrieves the configuration settings for the specified webhook, addressed by productUID.

        Parameters
        ----------
        product_uid : str

        webhook_uid : str
            Webhook UID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookSettings
            Webhook settings retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhook.get_webhook_settings_by_product(
                product_uid="com.blues.bridge:sensors",
                webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhook_settings_by_product(
            product_uid, webhook_uid, request_options=request_options
        )
        return _response.data

    async def update_webhook_settings_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the configuration settings for the specified webhook, addressed by productUID. Update body will completely replace the existing settings.

        Parameters
        ----------
        product_uid : str

        webhook_uid : str
            Webhook UID

        disabled : typing.Optional[bool]
            Flag indicating if the webhook is disabled

        id : typing.Optional[str]
            Webhook ID

        transform : typing.Optional[str]
            Transformation to be applied to the event

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
            await client.webhook.update_webhook_settings_by_product(
                product_uid="com.blues.bridge:sensors",
                webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
                disabled=False,
                transform='{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook_settings_by_product(
            product_uid, webhook_uid, disabled=disabled, id=id, transform=transform, request_options=request_options
        )
        return _response.data

    async def get_webhooks(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetWebhooksResponse:
        """
        Retrieves all webhooks for the specified project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetWebhooksResponse
            Webhooks retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhook.get_webhooks(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhooks(project_or_product_uid, request_options=request_options)
        return _response.data

    async def get_webhook(
        self, project_or_product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookSettings:
        """
        Retrieves the configuration settings for the specified webhook

        Parameters
        ----------
        project_or_product_uid : str

        webhook_uid : str
            Webhook UID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookSettings
            Webhook settings retrieved successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.webhook.get_webhook(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhook(
            project_or_product_uid, webhook_uid, request_options=request_options
        )
        return _response.data

    async def create_webhook(
        self,
        project_or_product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Creates a webhook for the specified product with the given name. The name | must be unique within the project.

        Parameters
        ----------
        project_or_product_uid : str

        webhook_uid : str
            Webhook UID

        disabled : typing.Optional[bool]
            Flag indicating if the webhook is disabled

        id : typing.Optional[str]
            Webhook ID

        transform : typing.Optional[str]
            Transformation to be applied to the event

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
            await client.webhook.create_webhook(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_webhook(
            project_or_product_uid,
            webhook_uid,
            disabled=disabled,
            id=id,
            transform=transform,
            request_options=request_options,
        )
        return _response.data

    async def update_webhook(
        self,
        project_or_product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Updates the configuration settings for the specified webhook. | Webhook will be created if it does not exist. Update body will completely replace the existing settings.

        Parameters
        ----------
        project_or_product_uid : str

        webhook_uid : str
            Webhook UID

        disabled : typing.Optional[bool]
            Flag indicating if the webhook is disabled

        id : typing.Optional[str]
            Webhook ID

        transform : typing.Optional[str]
            Transformation to be applied to the event

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
            await client.webhook.update_webhook(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
                disabled=False,
                transform='{"device":body.end_device_ids.dev_eui,"sn":body.end_device_ids.device_id,"body":body.uplink_message.decoded_payload,"details":body}',
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_webhook(
            project_or_product_uid,
            webhook_uid,
            disabled=disabled,
            id=id,
            transform=transform,
            request_options=request_options,
        )
        return _response.data

    async def delete_webhook(
        self, project_or_product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the specified webhook

        Parameters
        ----------
        project_or_product_uid : str

        webhook_uid : str
            Webhook UID

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
            await client.webhook.delete_webhook(
                project_or_product_uid="app:2606f411-dea6-44a0-9743-1130f57d77d8",
                webhook_uid="Abc_123-2646f411-dc56-44a0-9743-4130f47a74h8",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhook(
            project_or_product_uid, webhook_uid, request_options=request_options
        )
        return _response.data
