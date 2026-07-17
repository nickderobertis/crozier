

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
from ..types.actor_definition_resource_requirements import ActorDefinitionResourceRequirements
from ..types.destination_definition_create import DestinationDefinitionCreate
from ..types.destination_definition_id import DestinationDefinitionId
from ..types.destination_definition_read import DestinationDefinitionRead
from ..types.destination_definition_read_list import DestinationDefinitionReadList
from ..types.invalid_input_exception_info import InvalidInputExceptionInfo
from ..types.not_found_known_exception_info import NotFoundKnownExceptionInfo
from ..types.private_destination_definition_read import PrivateDestinationDefinitionRead
from ..types.private_destination_definition_read_list import PrivateDestinationDefinitionReadList
from ..types.workspace_id import WorkspaceId
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDestinationDefinitionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_custom_destination_definition(
        self,
        *,
        destination_definition: DestinationDefinitionCreate,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition : DestinationDefinitionCreate

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationDefinitionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/create_custom",
            method="POST",
            json={
                "destinationDefinition": convert_and_respect_annotation_metadata(
                    object_=destination_definition, annotation=DestinationDefinitionCreate, direction="write"
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
                    DestinationDefinitionRead,
                    parse_obj_as(
                        type_=DestinationDefinitionRead,
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

    def delete_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/delete",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
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

    def get_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationDefinitionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/get",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationDefinitionRead,
                    parse_obj_as(
                        type_=DestinationDefinitionRead,
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

    def get_destination_definition_for_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationDefinitionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/get_for_workspace",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationDefinitionRead,
                    parse_obj_as(
                        type_=DestinationDefinitionRead,
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

    def grant_destination_definition_to_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PrivateDestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrivateDestinationDefinitionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/grant_definition",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateDestinationDefinitionRead,
                    parse_obj_as(
                        type_=PrivateDestinationDefinitionRead,
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

    def list_destination_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DestinationDefinitionReadList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationDefinitionReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/list",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationDefinitionReadList,
                    parse_obj_as(
                        type_=DestinationDefinitionReadList,
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

    def list_destination_definitions_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DestinationDefinitionReadList]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationDefinitionReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/list_for_workspace",
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
                    DestinationDefinitionReadList,
                    parse_obj_as(
                        type_=DestinationDefinitionReadList,
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

    def list_latest_destination_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DestinationDefinitionReadList]:
        """
        Guaranteed to retrieve the latest information on supported destinations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationDefinitionReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/list_latest",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationDefinitionReadList,
                    parse_obj_as(
                        type_=DestinationDefinitionReadList,
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

    def list_private_destination_definitions(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PrivateDestinationDefinitionReadList]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PrivateDestinationDefinitionReadList]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/list_private",
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
                    PrivateDestinationDefinitionReadList,
                    parse_obj_as(
                        type_=PrivateDestinationDefinitionReadList,
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

    def revoke_destination_definition_from_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/revoke_definition",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        docker_image_tag: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ActorDefinitionResourceRequirements] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        docker_image_tag : typing.Optional[str]

        resource_requirements : typing.Optional[ActorDefinitionResourceRequirements]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DestinationDefinitionRead]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/update",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
                "dockerImageTag": docker_image_tag,
                "resourceRequirements": convert_and_respect_annotation_metadata(
                    object_=resource_requirements, annotation=ActorDefinitionResourceRequirements, direction="write"
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
                    DestinationDefinitionRead,
                    parse_obj_as(
                        type_=DestinationDefinitionRead,
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


class AsyncRawDestinationDefinitionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_custom_destination_definition(
        self,
        *,
        destination_definition: DestinationDefinitionCreate,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition : DestinationDefinitionCreate

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationDefinitionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/create_custom",
            method="POST",
            json={
                "destinationDefinition": convert_and_respect_annotation_metadata(
                    object_=destination_definition, annotation=DestinationDefinitionCreate, direction="write"
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
                    DestinationDefinitionRead,
                    parse_obj_as(
                        type_=DestinationDefinitionRead,
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

    async def delete_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/delete",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
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

    async def get_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationDefinitionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/get",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationDefinitionRead,
                    parse_obj_as(
                        type_=DestinationDefinitionRead,
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

    async def get_destination_definition_for_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationDefinitionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/get_for_workspace",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationDefinitionRead,
                    parse_obj_as(
                        type_=DestinationDefinitionRead,
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

    async def grant_destination_definition_to_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PrivateDestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrivateDestinationDefinitionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/grant_definition",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
                "workspaceId": workspace_id,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PrivateDestinationDefinitionRead,
                    parse_obj_as(
                        type_=PrivateDestinationDefinitionRead,
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

    async def list_destination_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DestinationDefinitionReadList]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationDefinitionReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/list",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationDefinitionReadList,
                    parse_obj_as(
                        type_=DestinationDefinitionReadList,
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

    async def list_destination_definitions_for_workspace(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DestinationDefinitionReadList]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationDefinitionReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/list_for_workspace",
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
                    DestinationDefinitionReadList,
                    parse_obj_as(
                        type_=DestinationDefinitionReadList,
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

    async def list_latest_destination_definitions(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DestinationDefinitionReadList]:
        """
        Guaranteed to retrieve the latest information on supported destinations.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationDefinitionReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/list_latest",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DestinationDefinitionReadList,
                    parse_obj_as(
                        type_=DestinationDefinitionReadList,
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

    async def list_private_destination_definitions(
        self, *, workspace_id: WorkspaceId, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PrivateDestinationDefinitionReadList]:
        """
        Parameters
        ----------
        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PrivateDestinationDefinitionReadList]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/list_private",
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
                    PrivateDestinationDefinitionReadList,
                    parse_obj_as(
                        type_=PrivateDestinationDefinitionReadList,
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

    async def revoke_destination_definition_from_workspace(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        workspace_id: WorkspaceId,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        workspace_id : WorkspaceId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/revoke_definition",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
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
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_destination_definition(
        self,
        *,
        destination_definition_id: DestinationDefinitionId,
        docker_image_tag: typing.Optional[str] = OMIT,
        resource_requirements: typing.Optional[ActorDefinitionResourceRequirements] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DestinationDefinitionRead]:
        """
        Parameters
        ----------
        destination_definition_id : DestinationDefinitionId

        docker_image_tag : typing.Optional[str]

        resource_requirements : typing.Optional[ActorDefinitionResourceRequirements]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DestinationDefinitionRead]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/destination_definitions/update",
            method="POST",
            json={
                "destinationDefinitionId": destination_definition_id,
                "dockerImageTag": docker_image_tag,
                "resourceRequirements": convert_and_respect_annotation_metadata(
                    object_=resource_requirements, annotation=ActorDefinitionResourceRequirements, direction="write"
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
                    DestinationDefinitionRead,
                    parse_obj_as(
                        type_=DestinationDefinitionRead,
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
