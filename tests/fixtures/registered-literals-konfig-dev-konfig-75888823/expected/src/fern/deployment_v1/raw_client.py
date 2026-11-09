

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError as core_api_error_ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_error import ApiError as types_api_error_ApiError
from ..types.app_id import AppId
from ..types.build_id import BuildId
from ..types.container_port import ContainerPort
from ..types.deployment import Deployment
from ..types.deployment_id import DeploymentId
from ..types.num_rooms_per_process import NumRoomsPerProcess
from ..types.plan_name import PlanName
from ..types.transport_type import TransportType
from .types.deployment_config_env_item import DeploymentConfigEnvItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDeploymentV1Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_deployments_deprecated(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Deployment]]:
        """
        Returns an array of [deployments](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Deployment]]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"deployments/v1/{encode_path_param(app_id)}/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Deployment],
                    parse_obj_as(
                        type_=typing.List[Deployment],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def get_latest_deployment_deprecated(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Deployment]:
        """
        Get the latest [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deployment]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"deployments/v1/{encode_path_param(app_id)}/latest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deployment,
                    parse_obj_as(
                        type_=Deployment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def get_deployment_info_deprecated(
        self, app_id: AppId, deployment_id: DeploymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Deployment]:
        """
        Get details for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment).

        Parameters
        ----------
        app_id : AppId

        deployment_id : DeploymentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deployment]
            Ok
        """
        _response = self._client_wrapper.httpx_client.request(
            f"deployments/v1/{encode_path_param(app_id)}/info/{encode_path_param(deployment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deployment,
                    parse_obj_as(
                        type_=Deployment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    def create_deployment_deprecated(
        self,
        app_id: AppId,
        build_id: BuildId,
        *,
        env: typing.Sequence[DeploymentConfigEnvItem],
        rooms_per_process: NumRoomsPerProcess,
        plan_name: PlanName,
        transport_type: TransportType,
        container_port: int,
        idle_timeout_enabled: typing.Optional[bool] = OMIT,
        additional_container_ports: typing.Optional[typing.Sequence[ContainerPort]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Deployment]:
        """
        Create a new [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment). Creating a new deployment means all new rooms created will use the latest deployment configuration, but existing games in progress will not be affected.

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        env : typing.Sequence[DeploymentConfigEnvItem]
            The environment variable that our process will have access to at runtime.

        rooms_per_process : NumRoomsPerProcess

        plan_name : PlanName

        transport_type : TransportType

        container_port : int
            Default port the server listens on.

        idle_timeout_enabled : typing.Optional[bool]
            Option to shut down processes that have had no new connections or rooms
            for five minutes.

        additional_container_ports : typing.Optional[typing.Sequence[ContainerPort]]
            Additional ports your server listens on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Deployment]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"deployments/v1/{encode_path_param(app_id)}/create/{encode_path_param(build_id)}",
            method="POST",
            json={
                "idleTimeoutEnabled": idle_timeout_enabled,
                "env": convert_and_respect_annotation_metadata(
                    object_=env, annotation=typing.Sequence[DeploymentConfigEnvItem], direction="write"
                ),
                "roomsPerProcess": rooms_per_process,
                "planName": plan_name,
                "additionalContainerPorts": convert_and_respect_annotation_metadata(
                    object_=additional_container_ports, annotation=typing.Sequence[ContainerPort], direction="write"
                ),
                "transportType": transport_type,
                "containerPort": container_port,
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
                    Deployment,
                    parse_obj_as(
                        type_=Deployment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )


class AsyncRawDeploymentV1Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_deployments_deprecated(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Deployment]]:
        """
        Returns an array of [deployments](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Deployment]]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"deployments/v1/{encode_path_param(app_id)}/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Deployment],
                    parse_obj_as(
                        type_=typing.List[Deployment],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def get_latest_deployment_deprecated(
        self, app_id: AppId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deployment]:
        """
        Get the latest [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment) for an [application](https://hathora.dev/docs/concepts/hathora-entities#application).

        Parameters
        ----------
        app_id : AppId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deployment]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"deployments/v1/{encode_path_param(app_id)}/latest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deployment,
                    parse_obj_as(
                        type_=Deployment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def get_deployment_info_deprecated(
        self, app_id: AppId, deployment_id: DeploymentId, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Deployment]:
        """
        Get details for a [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment).

        Parameters
        ----------
        app_id : AppId

        deployment_id : DeploymentId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deployment]
            Ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"deployments/v1/{encode_path_param(app_id)}/info/{encode_path_param(deployment_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Deployment,
                    parse_obj_as(
                        type_=Deployment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )

    async def create_deployment_deprecated(
        self,
        app_id: AppId,
        build_id: BuildId,
        *,
        env: typing.Sequence[DeploymentConfigEnvItem],
        rooms_per_process: NumRoomsPerProcess,
        plan_name: PlanName,
        transport_type: TransportType,
        container_port: int,
        idle_timeout_enabled: typing.Optional[bool] = OMIT,
        additional_container_ports: typing.Optional[typing.Sequence[ContainerPort]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Deployment]:
        """
        Create a new [deployment](https://hathora.dev/docs/concepts/hathora-entities#deployment). Creating a new deployment means all new rooms created will use the latest deployment configuration, but existing games in progress will not be affected.

        Parameters
        ----------
        app_id : AppId

        build_id : BuildId

        env : typing.Sequence[DeploymentConfigEnvItem]
            The environment variable that our process will have access to at runtime.

        rooms_per_process : NumRoomsPerProcess

        plan_name : PlanName

        transport_type : TransportType

        container_port : int
            Default port the server listens on.

        idle_timeout_enabled : typing.Optional[bool]
            Option to shut down processes that have had no new connections or rooms
            for five minutes.

        additional_container_ports : typing.Optional[typing.Sequence[ContainerPort]]
            Additional ports your server listens on.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Deployment]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"deployments/v1/{encode_path_param(app_id)}/create/{encode_path_param(build_id)}",
            method="POST",
            json={
                "idleTimeoutEnabled": idle_timeout_enabled,
                "env": convert_and_respect_annotation_metadata(
                    object_=env, annotation=typing.Sequence[DeploymentConfigEnvItem], direction="write"
                ),
                "roomsPerProcess": rooms_per_process,
                "planName": plan_name,
                "additionalContainerPorts": convert_and_respect_annotation_metadata(
                    object_=additional_container_ports, annotation=typing.Sequence[ContainerPort], direction="write"
                ),
                "transportType": transport_type,
                "containerPort": container_port,
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
                    Deployment,
                    parse_obj_as(
                        type_=Deployment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        types_api_error_ApiError,
                        parse_obj_as(
                            type_=types_api_error_ApiError,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise core_api_error_ApiError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
            )
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise core_api_error_ApiError(
            status_code=_response.status_code, headers=dict(_response.headers), body=_response_json
        )
