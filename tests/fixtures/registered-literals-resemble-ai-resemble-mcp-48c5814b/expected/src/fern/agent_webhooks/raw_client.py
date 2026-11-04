

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from .types.create_agent_webhook_request_webhook_type import CreateAgentWebhookRequestWebhookType
from .types.create_agent_webhook_response import CreateAgentWebhookResponse
from .types.delete_agent_webhook_response import DeleteAgentWebhookResponse
from .types.get_agent_webhook_response import GetAgentWebhookResponse
from .types.list_agent_webhooks_response import ListAgentWebhooksResponse
from .types.update_agent_webhook_response import UpdateAgentWebhookResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAgentWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_agent_webhooks(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListAgentWebhooksResponse]:
        """
        List all webhooks for an agent

        Parameters
        ----------
        agent_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAgentWebhooksResponse]
            List of webhooks
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAgentWebhooksResponse,
                    parse_obj_as(
                        type_=ListAgentWebhooksResponse,
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

    def create_agent_webhook(
        self,
        agent_uuid: str,
        *,
        webhook_type: CreateAgentWebhookRequestWebhookType,
        webhook_config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAgentWebhookResponse]:
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
        HttpResponse[CreateAgentWebhookResponse]
            Webhook created
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "webhook_type": webhook_type,
                "webhook_config": webhook_config,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAgentWebhookResponse,
                    parse_obj_as(
                        type_=CreateAgentWebhookResponse,
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

    def get_agent_webhook(
        self, agent_uuid: str, webhook_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetAgentWebhookResponse]:
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
        HttpResponse[GetAgentWebhookResponse]
            Webhook details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks/{encode_path_param(webhook_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentWebhookResponse,
                    parse_obj_as(
                        type_=GetAgentWebhookResponse,
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

    def delete_agent_webhook(
        self, agent_uuid: str, webhook_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteAgentWebhookResponse]:
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
        HttpResponse[DeleteAgentWebhookResponse]
            Webhook deleted
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks/{encode_path_param(webhook_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAgentWebhookResponse,
                    parse_obj_as(
                        type_=DeleteAgentWebhookResponse,
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

    def update_agent_webhook(
        self,
        agent_uuid: str,
        webhook_uuid: str,
        *,
        webhook_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateAgentWebhookResponse]:
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
        HttpResponse[UpdateAgentWebhookResponse]
            Webhook updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks/{encode_path_param(webhook_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "webhook_config": webhook_config,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateAgentWebhookResponse,
                    parse_obj_as(
                        type_=UpdateAgentWebhookResponse,
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


class AsyncRawAgentWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_agent_webhooks(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListAgentWebhooksResponse]:
        """
        List all webhooks for an agent

        Parameters
        ----------
        agent_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAgentWebhooksResponse]
            List of webhooks
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAgentWebhooksResponse,
                    parse_obj_as(
                        type_=ListAgentWebhooksResponse,
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

    async def create_agent_webhook(
        self,
        agent_uuid: str,
        *,
        webhook_type: CreateAgentWebhookRequestWebhookType,
        webhook_config: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAgentWebhookResponse]:
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
        AsyncHttpResponse[CreateAgentWebhookResponse]
            Webhook created
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "webhook_type": webhook_type,
                "webhook_config": webhook_config,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateAgentWebhookResponse,
                    parse_obj_as(
                        type_=CreateAgentWebhookResponse,
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

    async def get_agent_webhook(
        self, agent_uuid: str, webhook_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetAgentWebhookResponse]:
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
        AsyncHttpResponse[GetAgentWebhookResponse]
            Webhook details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks/{encode_path_param(webhook_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetAgentWebhookResponse,
                    parse_obj_as(
                        type_=GetAgentWebhookResponse,
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

    async def delete_agent_webhook(
        self, agent_uuid: str, webhook_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteAgentWebhookResponse]:
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
        AsyncHttpResponse[DeleteAgentWebhookResponse]
            Webhook deleted
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks/{encode_path_param(webhook_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAgentWebhookResponse,
                    parse_obj_as(
                        type_=DeleteAgentWebhookResponse,
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

    async def update_agent_webhook(
        self,
        agent_uuid: str,
        webhook_uuid: str,
        *,
        webhook_config: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateAgentWebhookResponse]:
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
        AsyncHttpResponse[UpdateAgentWebhookResponse]
            Webhook updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/webhooks/{encode_path_param(webhook_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="PATCH",
            json={
                "webhook_config": webhook_config,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateAgentWebhookResponse,
                    parse_obj_as(
                        type_=UpdateAgentWebhookResponse,
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
