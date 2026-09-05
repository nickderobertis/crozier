

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.container import Container
from ..types.container_list import ContainerList
from ..types.container_spec import ContainerSpec
from ..types.container_status import ContainerStatus
from ..types.error import Error
from ..types.service_info import ServiceInfo
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawContainersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_containers(
        self,
        *,
        max_page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ContainerList]:
        """
        Retrieve a list of containers with pagination support

        Parameters
        ----------
        max_page_size : typing.Optional[int]
            Maximum number of resources to return in a single page

        page_token : typing.Optional[str]
            Token indicating the starting point for the page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContainerList]
            Successfully retrieved containers
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1alpha1/containers",
            method="GET",
            params={
                "max_page_size": max_page_size,
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContainerList,
                    parse_obj_as(
                        type_=ContainerList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def create_container(
        self,
        *,
        spec: ContainerSpec,
        id: typing.Optional[str] = None,
        container_id: typing.Optional[str] = OMIT,
        path: typing.Optional[str] = OMIT,
        status: typing.Optional[ContainerStatus] = OMIT,
        service: typing.Optional[ServiceInfo] = OMIT,
        create_time: typing.Optional[dt.datetime] = OMIT,
        update_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Container]:
        """
        Create a new container instance

        Parameters
        ----------
        spec : ContainerSpec

        id : typing.Optional[str]
            Optional client-specified ID for the container. If not provided,
            the server will generate an ID.

            Requirements (per AEP-122):
            - 1-63 characters long
            - Start with a lowercase letter or digit
            - Contain only lowercase letters, numbers, and hyphens
            - End with letter or number

        container_id : typing.Optional[str]
            Unique identifier for the container instance

        path : typing.Optional[str]
            Resource path identifier

        status : typing.Optional[ContainerStatus]

        service : typing.Optional[ServiceInfo]

        create_time : typing.Optional[dt.datetime]
            Timestamp when the container was created

        update_time : typing.Optional[dt.datetime]
            Timestamp when the container was last updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Container]
            Container created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1alpha1/containers",
            method="POST",
            params={
                "id": id,
            },
            json={
                "id": id,
                "path": path,
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=ContainerSpec, direction="write"
                ),
                "status": status,
                "service": convert_and_respect_annotation_metadata(
                    object_=service, annotation=ServiceInfo, direction="write"
                ),
                "create_time": create_time,
                "update_time": update_time,
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
                    Container,
                    parse_obj_as(
                        type_=Container,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_container(
        self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Container]:
        """
        Retrieve a specific container instance by ID

        Parameters
        ----------
        container_id : str
            Unique identifier for the container

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Container]
            Container retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1alpha1/containers/{encode_path_param(container_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Container,
                    parse_obj_as(
                        type_=Container,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def delete_container(
        self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a specific container instance

        Parameters
        ----------
        container_id : str
            Unique identifier for the container

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v1alpha1/containers/{encode_path_param(container_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawContainersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_containers(
        self,
        *,
        max_page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ContainerList]:
        """
        Retrieve a list of containers with pagination support

        Parameters
        ----------
        max_page_size : typing.Optional[int]
            Maximum number of resources to return in a single page

        page_token : typing.Optional[str]
            Token indicating the starting point for the page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContainerList]
            Successfully retrieved containers
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1alpha1/containers",
            method="GET",
            params={
                "max_page_size": max_page_size,
                "page_token": page_token,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContainerList,
                    parse_obj_as(
                        type_=ContainerList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def create_container(
        self,
        *,
        spec: ContainerSpec,
        id: typing.Optional[str] = None,
        container_id: typing.Optional[str] = OMIT,
        path: typing.Optional[str] = OMIT,
        status: typing.Optional[ContainerStatus] = OMIT,
        service: typing.Optional[ServiceInfo] = OMIT,
        create_time: typing.Optional[dt.datetime] = OMIT,
        update_time: typing.Optional[dt.datetime] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Container]:
        """
        Create a new container instance

        Parameters
        ----------
        spec : ContainerSpec

        id : typing.Optional[str]
            Optional client-specified ID for the container. If not provided,
            the server will generate an ID.

            Requirements (per AEP-122):
            - 1-63 characters long
            - Start with a lowercase letter or digit
            - Contain only lowercase letters, numbers, and hyphens
            - End with letter or number

        container_id : typing.Optional[str]
            Unique identifier for the container instance

        path : typing.Optional[str]
            Resource path identifier

        status : typing.Optional[ContainerStatus]

        service : typing.Optional[ServiceInfo]

        create_time : typing.Optional[dt.datetime]
            Timestamp when the container was created

        update_time : typing.Optional[dt.datetime]
            Timestamp when the container was last updated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Container]
            Container created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1alpha1/containers",
            method="POST",
            params={
                "id": id,
            },
            json={
                "id": id,
                "path": path,
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=ContainerSpec, direction="write"
                ),
                "status": status,
                "service": convert_and_respect_annotation_metadata(
                    object_=service, annotation=ServiceInfo, direction="write"
                ),
                "create_time": create_time,
                "update_time": update_time,
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
                    Container,
                    parse_obj_as(
                        type_=Container,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_container(
        self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Container]:
        """
        Retrieve a specific container instance by ID

        Parameters
        ----------
        container_id : str
            Unique identifier for the container

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Container]
            Container retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1alpha1/containers/{encode_path_param(container_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Container,
                    parse_obj_as(
                        type_=Container,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def delete_container(
        self, container_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a specific container instance

        Parameters
        ----------
        container_id : str
            Unique identifier for the container

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v1alpha1/containers/{encode_path_param(container_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
