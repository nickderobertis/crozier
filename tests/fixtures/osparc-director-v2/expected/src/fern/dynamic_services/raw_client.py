

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.get_project_inactivity_response import GetProjectInactivityResponse
from ..types.hardware_info import HardwareInfo
from ..types.pricing_info import PricingInfo
from ..types.retrieve_data_out_enveloped import RetrieveDataOutEnveloped
from ..types.running_dynamic_service_details import RunningDynamicServiceDetails
from ..types.user_id_int import UserIdInt
from ..types.wallet_info_input import WalletInfoInput
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDynamicServicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_tracked_dynamic_services(
        self,
        *,
        user_id: typing.Optional[UserIdInt] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[RunningDynamicServiceDetails]]:
        """
        Parameters
        ----------
        user_id : typing.Optional[UserIdInt]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[RunningDynamicServiceDetails]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/dynamic_services",
            method="GET",
            params={
                "user_id": user_id,
                "project_id": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RunningDynamicServiceDetails],
                    parse_obj_as(
                        type_=typing.List[RunningDynamicServiceDetails],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def create_dynamic_service(
        self,
        *,
        dynamic_sidecar_request_dns: str,
        dynamic_sidecar_request_scheme: str,
        simcore_user_agent: str,
        service_key: str,
        service_version: str,
        user_id: UserIdInt,
        project_id: str,
        service_uuid: str,
        service_resources: typing.Dict[str, typing.Any],
        product_name: str,
        product_api_base_url: str,
        can_save: bool,
        service_basepath: typing.Optional[str] = OMIT,
        wallet_info: typing.Optional[WalletInfoInput] = OMIT,
        pricing_info: typing.Optional[PricingInfo] = OMIT,
        hardware_info: typing.Optional[HardwareInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunningDynamicServiceDetails]:
        """
        Parameters
        ----------
        dynamic_sidecar_request_dns : str

        dynamic_sidecar_request_scheme : str

        simcore_user_agent : str

        service_key : str
            distinctive name for the node based on the docker registry path

        service_version : str
            semantic version number of the node

        user_id : UserIdInt

        project_id : str

        service_uuid : str

        service_resources : typing.Dict[str, typing.Any]

        product_name : str
            Current product name

        product_api_base_url : str
            Current product API base URL

        can_save : bool
            the service data must be saved when closing

        service_basepath : typing.Optional[str]
            predefined path where the dynamic service should be served. If empty, the service shall use the root endpoint.

        wallet_info : typing.Optional[WalletInfoInput]
            contains information about the wallet used to bill the running service

        pricing_info : typing.Optional[PricingInfo]
            contains pricing information (ex. pricing plan and unit ids)

        hardware_info : typing.Optional[HardwareInfo]
            contains hardware information (ex. aws_ec2_instances)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunningDynamicServiceDetails]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v2/dynamic_services",
            method="POST",
            json={
                "service_key": service_key,
                "service_version": service_version,
                "user_id": user_id,
                "project_id": project_id,
                "service_uuid": service_uuid,
                "service_basepath": service_basepath,
                "service_resources": service_resources,
                "product_name": product_name,
                "product_api_base_url": product_api_base_url,
                "can_save": can_save,
                "wallet_info": convert_and_respect_annotation_metadata(
                    object_=wallet_info, annotation=typing.Optional[WalletInfoInput], direction="write"
                ),
                "pricing_info": convert_and_respect_annotation_metadata(
                    object_=pricing_info, annotation=typing.Optional[PricingInfo], direction="write"
                ),
                "hardware_info": convert_and_respect_annotation_metadata(
                    object_=hardware_info, annotation=typing.Optional[HardwareInfo], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-dynamic-sidecar-request-dns": str(dynamic_sidecar_request_dns)
                if dynamic_sidecar_request_dns is not None
                else None,
                "x-dynamic-sidecar-request-scheme": str(dynamic_sidecar_request_scheme)
                if dynamic_sidecar_request_scheme is not None
                else None,
                "x-simcore-user-agent": str(simcore_user_agent) if simcore_user_agent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunningDynamicServiceDetails,
                    parse_obj_as(
                        type_=RunningDynamicServiceDetails,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_dynamic_sidecar_status(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunningDynamicServiceDetails]:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunningDynamicServiceDetails]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/{encode_path_param(node_uuid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunningDynamicServiceDetails,
                    parse_obj_as(
                        type_=RunningDynamicServiceDetails,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def stop_dynamic_service(
        self,
        node_uuid: str,
        *,
        can_save: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        node_uuid : str

        can_save : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/{encode_path_param(node_uuid)}",
            method="DELETE",
            params={
                "can_save": can_save,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def service_retrieve_data_on_ports(
        self,
        node_uuid: str,
        *,
        port_keys: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RetrieveDataOutEnveloped]:
        """
        Parameters
        ----------
        node_uuid : str

        port_keys : typing.Sequence[str]
            The port keys to retrieve data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveDataOutEnveloped]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/{encode_path_param(node_uuid)}:retrieve",
            method="POST",
            json={
                "port_keys": port_keys,
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
                    RetrieveDataOutEnveloped,
                    parse_obj_as(
                        type_=RetrieveDataOutEnveloped,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def service_restart_containers(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/{encode_path_param(node_uuid)}:restart",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def update_projects_networks_v2dynamic_services_projects_project_id_networks_patch(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/projects/{encode_path_param(project_id)}/-/networks",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    def get_project_inactivity(
        self, project_id: str, *, max_inactivity_seconds: float, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetProjectInactivityResponse]:
        """
        Parameters
        ----------
        project_id : str

        max_inactivity_seconds : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProjectInactivityResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/projects/{encode_path_param(project_id)}/inactivity",
            method="GET",
            params={
                "max_inactivity_seconds": max_inactivity_seconds,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectInactivityResponse,
                    parse_obj_as(
                        type_=GetProjectInactivityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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


class AsyncRawDynamicServicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_tracked_dynamic_services(
        self,
        *,
        user_id: typing.Optional[UserIdInt] = None,
        project_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[RunningDynamicServiceDetails]]:
        """
        Parameters
        ----------
        user_id : typing.Optional[UserIdInt]

        project_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[RunningDynamicServiceDetails]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/dynamic_services",
            method="GET",
            params={
                "user_id": user_id,
                "project_id": project_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[RunningDynamicServiceDetails],
                    parse_obj_as(
                        type_=typing.List[RunningDynamicServiceDetails],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def create_dynamic_service(
        self,
        *,
        dynamic_sidecar_request_dns: str,
        dynamic_sidecar_request_scheme: str,
        simcore_user_agent: str,
        service_key: str,
        service_version: str,
        user_id: UserIdInt,
        project_id: str,
        service_uuid: str,
        service_resources: typing.Dict[str, typing.Any],
        product_name: str,
        product_api_base_url: str,
        can_save: bool,
        service_basepath: typing.Optional[str] = OMIT,
        wallet_info: typing.Optional[WalletInfoInput] = OMIT,
        pricing_info: typing.Optional[PricingInfo] = OMIT,
        hardware_info: typing.Optional[HardwareInfo] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunningDynamicServiceDetails]:
        """
        Parameters
        ----------
        dynamic_sidecar_request_dns : str

        dynamic_sidecar_request_scheme : str

        simcore_user_agent : str

        service_key : str
            distinctive name for the node based on the docker registry path

        service_version : str
            semantic version number of the node

        user_id : UserIdInt

        project_id : str

        service_uuid : str

        service_resources : typing.Dict[str, typing.Any]

        product_name : str
            Current product name

        product_api_base_url : str
            Current product API base URL

        can_save : bool
            the service data must be saved when closing

        service_basepath : typing.Optional[str]
            predefined path where the dynamic service should be served. If empty, the service shall use the root endpoint.

        wallet_info : typing.Optional[WalletInfoInput]
            contains information about the wallet used to bill the running service

        pricing_info : typing.Optional[PricingInfo]
            contains pricing information (ex. pricing plan and unit ids)

        hardware_info : typing.Optional[HardwareInfo]
            contains hardware information (ex. aws_ec2_instances)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunningDynamicServiceDetails]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v2/dynamic_services",
            method="POST",
            json={
                "service_key": service_key,
                "service_version": service_version,
                "user_id": user_id,
                "project_id": project_id,
                "service_uuid": service_uuid,
                "service_basepath": service_basepath,
                "service_resources": service_resources,
                "product_name": product_name,
                "product_api_base_url": product_api_base_url,
                "can_save": can_save,
                "wallet_info": convert_and_respect_annotation_metadata(
                    object_=wallet_info, annotation=typing.Optional[WalletInfoInput], direction="write"
                ),
                "pricing_info": convert_and_respect_annotation_metadata(
                    object_=pricing_info, annotation=typing.Optional[PricingInfo], direction="write"
                ),
                "hardware_info": convert_and_respect_annotation_metadata(
                    object_=hardware_info, annotation=typing.Optional[HardwareInfo], direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
                "x-dynamic-sidecar-request-dns": str(dynamic_sidecar_request_dns)
                if dynamic_sidecar_request_dns is not None
                else None,
                "x-dynamic-sidecar-request-scheme": str(dynamic_sidecar_request_scheme)
                if dynamic_sidecar_request_scheme is not None
                else None,
                "x-simcore-user-agent": str(simcore_user_agent) if simcore_user_agent is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunningDynamicServiceDetails,
                    parse_obj_as(
                        type_=RunningDynamicServiceDetails,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_dynamic_sidecar_status(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunningDynamicServiceDetails]:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunningDynamicServiceDetails]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/{encode_path_param(node_uuid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunningDynamicServiceDetails,
                    parse_obj_as(
                        type_=RunningDynamicServiceDetails,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def stop_dynamic_service(
        self,
        node_uuid: str,
        *,
        can_save: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        node_uuid : str

        can_save : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/{encode_path_param(node_uuid)}",
            method="DELETE",
            params={
                "can_save": can_save,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def service_retrieve_data_on_ports(
        self,
        node_uuid: str,
        *,
        port_keys: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RetrieveDataOutEnveloped]:
        """
        Parameters
        ----------
        node_uuid : str

        port_keys : typing.Sequence[str]
            The port keys to retrieve data from

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveDataOutEnveloped]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/{encode_path_param(node_uuid)}:retrieve",
            method="POST",
            json={
                "port_keys": port_keys,
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
                    RetrieveDataOutEnveloped,
                    parse_obj_as(
                        type_=RetrieveDataOutEnveloped,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def service_restart_containers(
        self, node_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        node_uuid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/{encode_path_param(node_uuid)}:restart",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def update_projects_networks_v2dynamic_services_projects_project_id_networks_patch(
        self, project_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        project_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/projects/{encode_path_param(project_id)}/-/networks",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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

    async def get_project_inactivity(
        self, project_id: str, *, max_inactivity_seconds: float, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetProjectInactivityResponse]:
        """
        Parameters
        ----------
        project_id : str

        max_inactivity_seconds : float

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProjectInactivityResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/dynamic_services/projects/{encode_path_param(project_id)}/inactivity",
            method="GET",
            params={
                "max_inactivity_seconds": max_inactivity_seconds,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectInactivityResponse,
                    parse_obj_as(
                        type_=GetProjectInactivityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
