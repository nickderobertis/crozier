

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.check_connection_read import CheckConnectionRead
from ..types.destination_clone_configuration import DestinationCloneConfiguration
from ..types.destination_configuration import DestinationConfiguration
from ..types.destination_definition_id import DestinationDefinitionId
from ..types.destination_id import DestinationId
from ..types.destination_read import DestinationRead
from ..types.destination_read_list import DestinationReadList
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo
from ..types.workspace_id import WorkspaceId
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDestinationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def check_connection_to_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CheckConnectionRead]:
        """
        Parameters
        ----------
        destination_id : DestinationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destinations/check_connection",
            method="POST",
            json={
                "destinationId": destination_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckConnectionRead,
                    parse_obj_as(
                        type_=CheckConnectionRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def check_connection_to_destination_for_update(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_id: DestinationId,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CheckConnectionRead]:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_id : DestinationId

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CheckConnectionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destinations/check_connection_for_update",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "destinationId": destination_id,
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckConnectionRead,
                    parse_obj_as(
                        type_=CheckConnectionRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def clone_destination(
        self,
        *,
        destination_clone_id: DestinationId,
        destination_configuration: typing.Optional[DestinationCloneConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DestinationRead]:
        """
        Parameters
        ----------
        destination_clone_id : DestinationId

        destination_configuration : typing.Optional[DestinationCloneConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destinations/clone",
            method="POST",
            json={
                "destinationCloneId": destination_clone_id,
                "destinationConfiguration": convert_and_respect_annotation_metadata(
                    object_=destination_configuration, annotation=DestinationCloneConfiguration, direction="write"
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
                    DestinationRead,
                    parse_obj_as(
                        type_=DestinationRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_destination(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_definition_id: DestinationDefinitionId,
        name: str,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DestinationRead]:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_definition_id : DestinationDefinitionId

        name : str

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destinations/create",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "destinationDefinitionId": destination_definition_id,
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
                    DestinationRead,
                    parse_obj_as(
                        type_=DestinationRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        destination_id : DestinationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destinations/delete",
            method="POST",
            json={
                "destinationId": destination_id,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DestinationRead]:
        """
        Parameters
        ----------
        destination_id : DestinationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destinations/get",
            method="POST",
            json={
                "destinationId": destination_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationRead,
                    parse_obj_as(
                        type_=DestinationRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_destinations_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DestinationReadList]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destinations/list",
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
                    DestinationReadList,
                    parse_obj_as(
                        type_=DestinationReadList,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def search_destinations(
        self,
        *,
        connection_configuration: typing.Optional[DestinationConfiguration] = OMIT,
        destination_definition_id: typing.Optional[DestinationDefinitionId] = OMIT,
        destination_id: typing.Optional[DestinationId] = OMIT,
        destination_name: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        workspace_id: typing.Optional[WorkspaceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DestinationReadList]:
        """
        Parameters
        ----------
        connection_configuration : typing.Optional[DestinationConfiguration]

        destination_definition_id : typing.Optional[DestinationDefinitionId]

        destination_id : typing.Optional[DestinationId]

        destination_name : typing.Optional[str]

        name : typing.Optional[str]

        workspace_id : typing.Optional[WorkspaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destinations/search",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "destinationDefinitionId": destination_definition_id,
                "destinationId": destination_id,
                "destinationName": destination_name,
                "name": name,
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationReadList,
                    parse_obj_as(
                        type_=DestinationReadList,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_destination(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_id: DestinationId,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DestinationRead]:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_id : DestinationId

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destinations/update",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "destinationId": destination_id,
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationRead,
                    parse_obj_as(
                        type_=DestinationRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawDestinationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def check_connection_to_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CheckConnectionRead]:
        """
        Parameters
        ----------
        destination_id : DestinationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destinations/check_connection",
            method="POST",
            json={
                "destinationId": destination_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckConnectionRead,
                    parse_obj_as(
                        type_=CheckConnectionRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def check_connection_to_destination_for_update(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_id: DestinationId,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CheckConnectionRead]:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_id : DestinationId

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CheckConnectionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destinations/check_connection_for_update",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "destinationId": destination_id,
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CheckConnectionRead,
                    parse_obj_as(
                        type_=CheckConnectionRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def clone_destination(
        self,
        *,
        destination_clone_id: DestinationId,
        destination_configuration: typing.Optional[DestinationCloneConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DestinationRead]:
        """
        Parameters
        ----------
        destination_clone_id : DestinationId

        destination_configuration : typing.Optional[DestinationCloneConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destinations/clone",
            method="POST",
            json={
                "destinationCloneId": destination_clone_id,
                "destinationConfiguration": convert_and_respect_annotation_metadata(
                    object_=destination_configuration, annotation=DestinationCloneConfiguration, direction="write"
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
                    DestinationRead,
                    parse_obj_as(
                        type_=DestinationRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_destination(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_definition_id: DestinationDefinitionId,
        name: str,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DestinationRead]:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_definition_id : DestinationDefinitionId

        name : str

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destinations/create",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "destinationDefinitionId": destination_definition_id,
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
                    DestinationRead,
                    parse_obj_as(
                        type_=DestinationRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        destination_id : DestinationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destinations/delete",
            method="POST",
            json={
                "destinationId": destination_id,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_destination(
        self, *, destination_id: DestinationId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DestinationRead]:
        """
        Parameters
        ----------
        destination_id : DestinationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destinations/get",
            method="POST",
            json={
                "destinationId": destination_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationRead,
                    parse_obj_as(
                        type_=DestinationRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_destinations_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DestinationReadList]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destinations/list",
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
                    DestinationReadList,
                    parse_obj_as(
                        type_=DestinationReadList,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def search_destinations(
        self,
        *,
        connection_configuration: typing.Optional[DestinationConfiguration] = OMIT,
        destination_definition_id: typing.Optional[DestinationDefinitionId] = OMIT,
        destination_id: typing.Optional[DestinationId] = OMIT,
        destination_name: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        workspace_id: typing.Optional[WorkspaceId] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DestinationReadList]:
        """
        Parameters
        ----------
        connection_configuration : typing.Optional[DestinationConfiguration]

        destination_definition_id : typing.Optional[DestinationDefinitionId]

        destination_id : typing.Optional[DestinationId]

        destination_name : typing.Optional[str]

        name : typing.Optional[str]

        workspace_id : typing.Optional[WorkspaceId]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destinations/search",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "destinationDefinitionId": destination_definition_id,
                "destinationId": destination_id,
                "destinationName": destination_name,
                "name": name,
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationReadList,
                    parse_obj_as(
                        type_=DestinationReadList,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_destination(
        self,
        *,
        connection_configuration: DestinationConfiguration,
        destination_id: DestinationId,
        name: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DestinationRead]:
        """
        Parameters
        ----------
        connection_configuration : DestinationConfiguration

        destination_id : DestinationId

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destinations/update",
            method="POST",
            json={
                "connectionConfiguration": connection_configuration,
                "destinationId": destination_id,
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationRead,
                    parse_obj_as(
                        type_=DestinationRead,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
