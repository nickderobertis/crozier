

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
from ..types.check_operation_read import CheckOperationRead
from ..types.connection_id import ConnectionId
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo
from ..types.operation_id import OperationId
from ..types.operation_read import OperationRead
from ..types.operation_read_list import OperationReadList
from ..types.operator_configuration import OperatorConfiguration
from ..types.operator_dbt import OperatorDbt
from ..types.operator_normalization import OperatorNormalization
from ..types.operator_type import OperatorType
from ..types.operator_webhook import OperatorWebhook
from ..types.workspace_id import WorkspaceId


OMIT = typing.cast(typing.Any, ...)


class RawOperationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def check_operation(
        self,
        *,
        operator_type: OperatorType,
        dbt: typing.Optional[OperatorDbt] = OMIT,
        normalization: typing.Optional[OperatorNormalization] = OMIT,
        webhook: typing.Optional[OperatorWebhook] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckOperationRead]:
        """
        Parameters
        ----------
        operator_type : OperatorType

        dbt : typing.Optional[OperatorDbt]

        normalization : typing.Optional[OperatorNormalization]

        webhook : typing.Optional[OperatorWebhook]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckOperationRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/operations/check",
            method="POST",
            json={
                "dbt": convert_and_respect_annotation_metadata(object_=dbt, annotation=OperatorDbt, direction="write"),
                "normalization": convert_and_respect_annotation_metadata(
                    object_=normalization, annotation=OperatorNormalization, direction="write"
                ),
                "operatorType": operator_type,
                "webhook": convert_and_respect_annotation_metadata(
                    object_=webhook, annotation=OperatorWebhook, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckOperationRead,
                    parse_obj_as(
                        type_=CheckOperationRead,
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

    def create_operation(
        self,
        *,
        name: str,
        operator_configuration: OperatorConfiguration,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OperationRead]:
        """
        Parameters
        ----------
        name : str

        operator_configuration : OperatorConfiguration

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OperationRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/operations/create",
            method="POST",
            json={
                "name": name,
                "operatorConfiguration": convert_and_respect_annotation_metadata(
                    object_=operator_configuration, annotation=OperatorConfiguration, direction="write"
                ),
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationRead,
                    parse_obj_as(
                        type_=OperationRead,
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

    def delete_operation(
        self, *, operation_id: OperationId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        operation_id : OperationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/operations/delete",
            method="POST",
            json={
                "operationId": operation_id,
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

    def get_operation(
        self, *, operation_id: OperationId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OperationRead]:
        """
        Parameters
        ----------
        operation_id : OperationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OperationRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/operations/get",
            method="POST",
            json={
                "operationId": operation_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationRead,
                    parse_obj_as(
                        type_=OperationRead,
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

    def list_operations_for_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OperationReadList]:
        """
        List operations for connection.

        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OperationReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/operations/list",
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
                    OperationReadList,
                    parse_obj_as(
                        type_=OperationReadList,
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

    def update_operation(
        self,
        *,
        name: str,
        operation_id: OperationId,
        operator_configuration: OperatorConfiguration,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OperationRead]:
        """
        Parameters
        ----------
        name : str

        operation_id : OperationId

        operator_configuration : OperatorConfiguration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OperationRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/operations/update",
            method="POST",
            json={
                "name": name,
                "operationId": operation_id,
                "operatorConfiguration": convert_and_respect_annotation_metadata(
                    object_=operator_configuration, annotation=OperatorConfiguration, direction="write"
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
                    OperationRead,
                    parse_obj_as(
                        type_=OperationRead,
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


class AsyncRawOperationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def check_operation(
        self,
        *,
        operator_type: OperatorType,
        dbt: typing.Optional[OperatorDbt] = OMIT,
        normalization: typing.Optional[OperatorNormalization] = OMIT,
        webhook: typing.Optional[OperatorWebhook] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckOperationRead]:
        """
        Parameters
        ----------
        operator_type : OperatorType

        dbt : typing.Optional[OperatorDbt]

        normalization : typing.Optional[OperatorNormalization]

        webhook : typing.Optional[OperatorWebhook]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckOperationRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/operations/check",
            method="POST",
            json={
                "dbt": convert_and_respect_annotation_metadata(object_=dbt, annotation=OperatorDbt, direction="write"),
                "normalization": convert_and_respect_annotation_metadata(
                    object_=normalization, annotation=OperatorNormalization, direction="write"
                ),
                "operatorType": operator_type,
                "webhook": convert_and_respect_annotation_metadata(
                    object_=webhook, annotation=OperatorWebhook, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckOperationRead,
                    parse_obj_as(
                        type_=CheckOperationRead,
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

    async def create_operation(
        self,
        *,
        name: str,
        operator_configuration: OperatorConfiguration,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OperationRead]:
        """
        Parameters
        ----------
        name : str

        operator_configuration : OperatorConfiguration

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OperationRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/operations/create",
            method="POST",
            json={
                "name": name,
                "operatorConfiguration": convert_and_respect_annotation_metadata(
                    object_=operator_configuration, annotation=OperatorConfiguration, direction="write"
                ),
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationRead,
                    parse_obj_as(
                        type_=OperationRead,
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

    async def delete_operation(
        self, *, operation_id: OperationId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        operation_id : OperationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/operations/delete",
            method="POST",
            json={
                "operationId": operation_id,
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

    async def get_operation(
        self, *, operation_id: OperationId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OperationRead]:
        """
        Parameters
        ----------
        operation_id : OperationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OperationRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/operations/get",
            method="POST",
            json={
                "operationId": operation_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OperationRead,
                    parse_obj_as(
                        type_=OperationRead,
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

    async def list_operations_for_connection(
        self, *, connection_id: ConnectionId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OperationReadList]:
        """
        List operations for connection.

        Parameters
        ----------
        connection_id : ConnectionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OperationReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/operations/list",
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
                    OperationReadList,
                    parse_obj_as(
                        type_=OperationReadList,
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

    async def update_operation(
        self,
        *,
        name: str,
        operation_id: OperationId,
        operator_configuration: OperatorConfiguration,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OperationRead]:
        """
        Parameters
        ----------
        name : str

        operation_id : OperationId

        operator_configuration : OperatorConfiguration

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OperationRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/operations/update",
            method="POST",
            json={
                "name": name,
                "operationId": operation_id,
                "operatorConfiguration": convert_and_respect_annotation_metadata(
                    object_=operator_configuration, annotation=OperatorConfiguration, direction="write"
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
                    OperationRead,
                    parse_obj_as(
                        type_=OperationRead,
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
