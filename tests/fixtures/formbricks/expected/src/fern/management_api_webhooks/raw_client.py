

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.webhook_id import WebhookId
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawManagementApiWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[GetWebhooksResponse]:
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
        HttpResponse[GetWebhooksResponse]
            Webhooks retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "management/webhooks",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "surveyIds": survey_ids,
            },
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
    ) -> HttpResponse[CreateWebhookResponse]:
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
        HttpResponse[CreateWebhookResponse]
            Webhook created successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            "management/webhooks",
            method="POST",
            json={
                "name": name,
                "url": url,
                "source": source,
                "workspaceId": workspace_id,
                "environmentId": environment_id,
                "triggers": triggers,
                "surveyIds": survey_ids,
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
                    CreateWebhookResponse,
                    parse_obj_as(
                        type_=CreateWebhookResponse,
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
        self, id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetWebhookResponse]:
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
        HttpResponse[GetWebhookResponse]
            Webhook retrieved successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/webhooks/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebhookResponse,
                    parse_obj_as(
                        type_=GetWebhookResponse,
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
    ) -> HttpResponse[UpdateWebhookResponse]:
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
        HttpResponse[UpdateWebhookResponse]
            Webhook updated successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/webhooks/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "url": url,
                "source": source,
                "workspaceId": workspace_id,
                "environmentId": environment_id,
                "triggers": triggers,
                "surveyIds": survey_ids,
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
                    UpdateWebhookResponse,
                    parse_obj_as(
                        type_=UpdateWebhookResponse,
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

    def delete_webhook(
        self, id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteWebhookResponse]:
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
        HttpResponse[DeleteWebhookResponse]
            Webhook deleted successfully.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"management/webhooks/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteWebhookResponse,
                    parse_obj_as(
                        type_=DeleteWebhookResponse,
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


class AsyncRawManagementApiWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[GetWebhooksResponse]:
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
        AsyncHttpResponse[GetWebhooksResponse]
            Webhooks retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "management/webhooks",
            method="GET",
            params={
                "limit": limit,
                "skip": skip,
                "sortBy": sort_by,
                "order": order,
                "startDate": start_date,
                "endDate": end_date,
                "filterDateField": filter_date_field,
                "surveyIds": survey_ids,
            },
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
    ) -> AsyncHttpResponse[CreateWebhookResponse]:
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
        AsyncHttpResponse[CreateWebhookResponse]
            Webhook created successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "management/webhooks",
            method="POST",
            json={
                "name": name,
                "url": url,
                "source": source,
                "workspaceId": workspace_id,
                "environmentId": environment_id,
                "triggers": triggers,
                "surveyIds": survey_ids,
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
                    CreateWebhookResponse,
                    parse_obj_as(
                        type_=CreateWebhookResponse,
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
        self, id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetWebhookResponse]:
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
        AsyncHttpResponse[GetWebhookResponse]
            Webhook retrieved successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/webhooks/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetWebhookResponse,
                    parse_obj_as(
                        type_=GetWebhookResponse,
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
    ) -> AsyncHttpResponse[UpdateWebhookResponse]:
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
        AsyncHttpResponse[UpdateWebhookResponse]
            Webhook updated successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/webhooks/{encode_path_param(id)}",
            method="PUT",
            json={
                "name": name,
                "url": url,
                "source": source,
                "workspaceId": workspace_id,
                "environmentId": environment_id,
                "triggers": triggers,
                "surveyIds": survey_ids,
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
                    UpdateWebhookResponse,
                    parse_obj_as(
                        type_=UpdateWebhookResponse,
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

    async def delete_webhook(
        self, id: WebhookId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteWebhookResponse]:
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
        AsyncHttpResponse[DeleteWebhookResponse]
            Webhook deleted successfully.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"management/webhooks/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteWebhookResponse,
                    parse_obj_as(
                        type_=DeleteWebhookResponse,
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
