

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.connection_id import ConnectionId
from ..types.geography import Geography
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo
from ..types.notification import Notification
from ..types.webhook_config_write import WebhookConfigWrite
from ..types.workspace_id import WorkspaceId
from ..types.workspace_read import WorkspaceRead
from ..types.workspace_read_list import WorkspaceReadList


OMIT = typing.cast(typing.Any, ...)


class RawWorkspaceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_workspace(
        self,
        *,
        name: str,
        anonymous_data_collection: typing.Optional[bool] = OMIT,
        default_geography: typing.Optional[Geography] = OMIT,
        display_setup_wizard: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        news: typing.Optional[bool] = OMIT,
        notifications: typing.Optional[typing.Sequence[Notification]] = OMIT,
        security_updates: typing.Optional[bool] = OMIT,
        webhook_configs: typing.Optional[typing.Sequence[WebhookConfigWrite]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        name : str

        anonymous_data_collection : typing.Optional[bool]

        default_geography : typing.Optional[Geography]

        display_setup_wizard : typing.Optional[bool]

        email : typing.Optional[str]

        news : typing.Optional[bool]

        notifications : typing.Optional[typing.Sequence[Notification]]

        security_updates : typing.Optional[bool]

        webhook_configs : typing.Optional[typing.Sequence[WebhookConfigWrite]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/create",
            method="POST",
            json={
                "anonymousDataCollection": anonymous_data_collection,
                "defaultGeography": default_geography,
                "displaySetupWizard": display_setup_wizard,
                "email": email,
                "name": name,
                "news": news,
                "notifications": convert_and_respect_annotation_metadata(
                    object_=notifications, annotation=typing.Sequence[Notification], direction="write"
                ),
                "securityUpdates": security_updates,
                "webhookConfigs": convert_and_respect_annotation_metadata(
                    object_=webhook_configs, annotation=typing.Sequence[WebhookConfigWrite], direction="write"
                ),
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
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/delete",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/get",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_workspace_by_connection_id(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/get_by_connection_id",
            method="POST",
            json={
                "connectionId": connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_workspace_by_slug(
        self, *, slug: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/get_by_slug",
            method="POST",
            json={
                "slug": slug,
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
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_workspaces(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceReadList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/list",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkspaceReadList,
                    parse_obj_as(
                        type_=WorkspaceReadList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_workspace_feedback(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/tag_feedback_status_as_done",
            method="POST",
            json={
                "workspaceId": workspace_id,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_workspace(
        self,
        *,
        workspace_id: WorkspaceId,
        anonymous_data_collection: typing.Optional[bool] = OMIT,
        default_geography: typing.Optional[Geography] = OMIT,
        display_setup_wizard: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        initial_setup_complete: typing.Optional[bool] = OMIT,
        news: typing.Optional[bool] = OMIT,
        notifications: typing.Optional[typing.Sequence[Notification]] = OMIT,
        security_updates: typing.Optional[bool] = OMIT,
        webhook_configs: typing.Optional[typing.Sequence[WebhookConfigWrite]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        anonymous_data_collection : typing.Optional[bool]

        default_geography : typing.Optional[Geography]

        display_setup_wizard : typing.Optional[bool]

        email : typing.Optional[str]

        initial_setup_complete : typing.Optional[bool]

        news : typing.Optional[bool]

        notifications : typing.Optional[typing.Sequence[Notification]]

        security_updates : typing.Optional[bool]

        webhook_configs : typing.Optional[typing.Sequence[WebhookConfigWrite]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/update",
            method="POST",
            json={
                "anonymousDataCollection": anonymous_data_collection,
                "defaultGeography": default_geography,
                "displaySetupWizard": display_setup_wizard,
                "email": email,
                "initialSetupComplete": initial_setup_complete,
                "news": news,
                "notifications": convert_and_respect_annotation_metadata(
                    object_=notifications, annotation=typing.Sequence[Notification], direction="write"
                ),
                "securityUpdates": security_updates,
                "webhookConfigs": convert_and_respect_annotation_metadata(
                    object_=webhook_configs, annotation=typing.Sequence[WebhookConfigWrite], direction="write"
                ),
                "workspaceId": workspace_id,
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
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_workspace_name(
        self, *, name: str, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        name : str

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/workspaces/update_name",
            method="POST",
            json={
                "name": name,
                "workspaceId": workspace_id,
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
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWorkspaceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_workspace(
        self,
        *,
        name: str,
        anonymous_data_collection: typing.Optional[bool] = OMIT,
        default_geography: typing.Optional[Geography] = OMIT,
        display_setup_wizard: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        news: typing.Optional[bool] = OMIT,
        notifications: typing.Optional[typing.Sequence[Notification]] = OMIT,
        security_updates: typing.Optional[bool] = OMIT,
        webhook_configs: typing.Optional[typing.Sequence[WebhookConfigWrite]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        name : str

        anonymous_data_collection : typing.Optional[bool]

        default_geography : typing.Optional[Geography]

        display_setup_wizard : typing.Optional[bool]

        email : typing.Optional[str]

        news : typing.Optional[bool]

        notifications : typing.Optional[typing.Sequence[Notification]]

        security_updates : typing.Optional[bool]

        webhook_configs : typing.Optional[typing.Sequence[WebhookConfigWrite]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/create",
            method="POST",
            json={
                "anonymousDataCollection": anonymous_data_collection,
                "defaultGeography": default_geography,
                "displaySetupWizard": display_setup_wizard,
                "email": email,
                "name": name,
                "news": news,
                "notifications": convert_and_respect_annotation_metadata(
                    object_=notifications, annotation=typing.Sequence[Notification], direction="write"
                ),
                "securityUpdates": security_updates,
                "webhookConfigs": convert_and_respect_annotation_metadata(
                    object_=webhook_configs, annotation=typing.Sequence[WebhookConfigWrite], direction="write"
                ),
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
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/delete",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/get",
            method="POST",
            json={
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_workspace_by_connection_id(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/get_by_connection_id",
            method="POST",
            json={
                "connectionId": connection_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_workspace_by_slug(
        self, *, slug: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        slug : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/get_by_slug",
            method="POST",
            json={
                "slug": slug,
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
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_workspaces(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceReadList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/list",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WorkspaceReadList,
                    parse_obj_as(
                        type_=WorkspaceReadList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_workspace_feedback(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/tag_feedback_status_as_done",
            method="POST",
            json={
                "workspaceId": workspace_id,
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
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_workspace(
        self,
        *,
        workspace_id: WorkspaceId,
        anonymous_data_collection: typing.Optional[bool] = OMIT,
        default_geography: typing.Optional[Geography] = OMIT,
        display_setup_wizard: typing.Optional[bool] = OMIT,
        email: typing.Optional[str] = OMIT,
        initial_setup_complete: typing.Optional[bool] = OMIT,
        news: typing.Optional[bool] = OMIT,
        notifications: typing.Optional[typing.Sequence[Notification]] = OMIT,
        security_updates: typing.Optional[bool] = OMIT,
        webhook_configs: typing.Optional[typing.Sequence[WebhookConfigWrite]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        anonymous_data_collection : typing.Optional[bool]

        default_geography : typing.Optional[Geography]

        display_setup_wizard : typing.Optional[bool]

        email : typing.Optional[str]

        initial_setup_complete : typing.Optional[bool]

        news : typing.Optional[bool]

        notifications : typing.Optional[typing.Sequence[Notification]]

        security_updates : typing.Optional[bool]

        webhook_configs : typing.Optional[typing.Sequence[WebhookConfigWrite]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/update",
            method="POST",
            json={
                "anonymousDataCollection": anonymous_data_collection,
                "defaultGeography": default_geography,
                "displaySetupWizard": display_setup_wizard,
                "email": email,
                "initialSetupComplete": initial_setup_complete,
                "news": news,
                "notifications": convert_and_respect_annotation_metadata(
                    object_=notifications, annotation=typing.Sequence[Notification], direction="write"
                ),
                "securityUpdates": security_updates,
                "webhookConfigs": convert_and_respect_annotation_metadata(
                    object_=webhook_configs, annotation=typing.Sequence[WebhookConfigWrite], direction="write"
                ),
                "workspaceId": workspace_id,
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
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_workspace_name(
        self, *, name: str, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WorkspaceRead]:
        """
        Parameters
        ----------
        name : str

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WorkspaceRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/workspaces/update_name",
            method="POST",
            json={
                "name": name,
                "workspaceId": workspace_id,
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
                    WorkspaceRead,
                    parse_obj_as(
                        type_=WorkspaceRead,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        NotFoundKnownExceptionInfo,
                        parse_obj_as(
                            type_=NotFoundKnownExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        InvalidInputExceptionInfo,
                        parse_obj_as(
                            type_=InvalidInputExceptionInfo,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
