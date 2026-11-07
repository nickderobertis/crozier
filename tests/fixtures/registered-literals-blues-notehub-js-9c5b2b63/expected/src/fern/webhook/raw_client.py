

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.webhook_settings import WebhookSettings
from .types.get_webhooks_response import GetWebhooksResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebhookClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_legacy_webhook_event(
        self,
        product_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/devices/{encode_path_param(device_uid)}/webhook-event",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_legacy_webhook_session(
        self,
        product_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/devices/{encode_path_param(device_uid)}/webhook-session",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_webhook_device_event_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/webhooks/{encode_path_param(webhook_uid)}/devices/{encode_path_param(device_uid)}/event",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_webhook_event_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/webhooks/{encode_path_param(webhook_uid)}/event",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_webhook_settings_by_product(
        self, product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhookSettings]:
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
        HttpResponse[WebhookSettings]
            Webhook settings retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/webhooks/{encode_path_param(webhook_uid)}/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookSettings,
                    parse_obj_as(
                        type_=WebhookSettings,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_webhook_settings_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/webhooks/{encode_path_param(webhook_uid)}/settings",
            method="PUT",
            json={
                "disabled": disabled,
                "id": id,
                "transform": transform,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_webhooks(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetWebhooksResponse]:
        """
        Retrieves all webhooks for the specified project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetWebhooksResponse]
            Webhooks retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebhooksResponse,
                    parse_obj_as(
                        type_=GetWebhooksResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_webhook(
        self, project_or_product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhookSettings]:
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
        HttpResponse[WebhookSettings]
            Webhook settings retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks/{encode_path_param(webhook_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookSettings,
                    parse_obj_as(
                        type_=WebhookSettings,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_webhook(
        self,
        project_or_product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks/{encode_path_param(webhook_uid)}",
            method="POST",
            json={
                "disabled": disabled,
                "id": id,
                "transform": transform,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_webhook(
        self,
        project_or_product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks/{encode_path_param(webhook_uid)}",
            method="PUT",
            json={
                "disabled": disabled,
                "id": id,
                "transform": transform,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_webhook(
        self, project_or_product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks/{encode_path_param(webhook_uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWebhookClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_legacy_webhook_event(
        self,
        product_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/devices/{encode_path_param(device_uid)}/webhook-event",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_legacy_webhook_session(
        self,
        product_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/devices/{encode_path_param(device_uid)}/webhook-session",
            method="PUT",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_webhook_device_event_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        device_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/webhooks/{encode_path_param(webhook_uid)}/devices/{encode_path_param(device_uid)}/event",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_webhook_event_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/webhooks/{encode_path_param(webhook_uid)}/event",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_webhook_settings_by_product(
        self, product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhookSettings]:
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
        AsyncHttpResponse[WebhookSettings]
            Webhook settings retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/webhooks/{encode_path_param(webhook_uid)}/settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookSettings,
                    parse_obj_as(
                        type_=WebhookSettings,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_webhook_settings_by_product(
        self,
        product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/webhooks/{encode_path_param(webhook_uid)}/settings",
            method="PUT",
            json={
                "disabled": disabled,
                "id": id,
                "transform": transform,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_webhooks(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetWebhooksResponse]:
        """
        Retrieves all webhooks for the specified project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetWebhooksResponse]
            Webhooks retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebhooksResponse,
                    parse_obj_as(
                        type_=GetWebhooksResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_webhook(
        self, project_or_product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhookSettings]:
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
        AsyncHttpResponse[WebhookSettings]
            Webhook settings retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks/{encode_path_param(webhook_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookSettings,
                    parse_obj_as(
                        type_=WebhookSettings,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_webhook(
        self,
        project_or_product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks/{encode_path_param(webhook_uid)}",
            method="POST",
            json={
                "disabled": disabled,
                "id": id,
                "transform": transform,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_webhook(
        self,
        project_or_product_uid: str,
        webhook_uid: str,
        *,
        disabled: typing.Optional[bool] = OMIT,
        id: typing.Optional[str] = OMIT,
        transform: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks/{encode_path_param(webhook_uid)}",
            method="PUT",
            json={
                "disabled": disabled,
                "id": id,
                "transform": transform,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_webhook(
        self, project_or_product_uid: str, webhook_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/webhooks/{encode_path_param(webhook_uid)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
