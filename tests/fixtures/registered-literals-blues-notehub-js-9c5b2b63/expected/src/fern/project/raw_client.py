

import contextlib
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
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.aws_role_config import AwsRoleConfig
from ..types.device_dfu_history import DeviceDfuHistory
from ..types.device_dfu_history_page import DeviceDfuHistoryPage
from ..types.device_dfu_status import DeviceDfuStatus
from ..types.device_dfu_status_page import DeviceDfuStatusPage
from ..types.env_tree_json_node import EnvTreeJsonNode
from ..types.environment_variables import EnvironmentVariables
from ..types.error import Error
from ..types.firmware_info import FirmwareInfo
from ..types.fleet import Fleet
from ..types.fleet_connectivity_assurance import FleetConnectivityAssurance
from ..types.fleet_rule import FleetRule
from ..types.get_project_secrets_response import GetProjectSecretsResponse
from ..types.notefile_schema import NotefileSchema
from ..types.product import Product
from ..types.project import Project
from ..types.project_secret import ProjectSecret
from .types.add_device_to_fleets_response import AddDeviceToFleetsResponse
from .types.delete_device_from_fleets_response import DeleteDeviceFromFleetsResponse
from .types.delete_firmware_request_firmware_type import DeleteFirmwareRequestFirmwareType
from .types.download_firmware_request_firmware_type import DownloadFirmwareRequestFirmwareType
from .types.get_device_dfu_history_request_firmware_type import GetDeviceDfuHistoryRequestFirmwareType
from .types.get_device_dfu_status_request_firmware_type import GetDeviceDfuStatusRequestFirmwareType
from .types.get_device_fleets_response import GetDeviceFleetsResponse
from .types.get_devices_dfu_history_request_firmware_type import GetDevicesDfuHistoryRequestFirmwareType
from .types.get_devices_dfu_history_request_sort_by import GetDevicesDfuHistoryRequestSortBy
from .types.get_devices_dfu_history_request_sort_order import GetDevicesDfuHistoryRequestSortOrder
from .types.get_devices_dfu_status_request_firmware_type import GetDevicesDfuStatusRequestFirmwareType
from .types.get_devices_dfu_status_request_sort_by import GetDevicesDfuStatusRequestSortBy
from .types.get_devices_dfu_status_request_sort_order import GetDevicesDfuStatusRequestSortOrder
from .types.get_firmware_info_request_sort_by import GetFirmwareInfoRequestSortBy
from .types.get_firmware_info_request_sort_order import GetFirmwareInfoRequestSortOrder
from .types.get_fleets_response import GetFleetsResponse
from .types.get_products_response import GetProductsResponse
from .types.get_project_members_response import GetProjectMembersResponse
from .types.get_projects_response import GetProjectsResponse
from .types.perform_dfu_action_request_action import PerformDfuActionRequestAction
from .types.perform_dfu_action_request_firmware_type import PerformDfuActionRequestFirmwareType
from .types.update_firmware_request_firmware_type import UpdateFirmwareRequestFirmwareType
from .types.upload_firmware_request_firmware_type import UploadFirmwareRequestFirmwareType
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawProjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_project_by_product(
        self, product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Project]:
        """
        Get a Project by ProductUID

        Parameters
        ----------
        product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Project]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/project",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    def get_projects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetProjectsResponse]:
        """
        Get Projects accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProjectsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/projects",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectsResponse,
                    parse_obj_as(
                        type_=GetProjectsResponse,
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

    def create_project(
        self, *, billing_account_uid: str, label: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Project]:
        """
        Create a Project

        Parameters
        ----------
        billing_account_uid : str
            The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.

        label : str
            The label for the project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Project]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/projects",
            method="POST",
            json={
                "billing_account_uid": billing_account_uid,
                "label": label,
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
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    def get_project(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Project]:
        """
        Get a Project by ProjectUID

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Project]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    def delete_project(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a Project by ProjectUID

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}",
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

    def get_aws_role_config(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AwsRoleConfig]:
        """
        Returns the AWS Account ID and External ID needed to configure an IAM role
        trust policy for role-based authentication on AWS routes.

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AwsRoleConfig]
            AWS role configuration
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/aws-role-config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AwsRoleConfig,
                    parse_obj_as(
                        type_=AwsRoleConfig,
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

    def clone_project(
        self,
        project_or_product_uid: str,
        *,
        billing_account_uid: str,
        label: str,
        disable_clone_fleets: typing.Optional[bool] = OMIT,
        disable_clone_routes: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Project]:
        """
        Clone a Project

        Parameters
        ----------
        project_or_product_uid : str

        billing_account_uid : str
            The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.

        label : str
            The label for the project.

        disable_clone_fleets : typing.Optional[bool]
            Whether to disallow the cloning of the fleets from the parent project.  Default is false if not specified.

        disable_clone_routes : typing.Optional[bool]
            Whether to disallow the cloning of the routes from the parent project.  Default is false if not specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Project]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/clone",
            method="POST",
            json={
                "billing_account_uid": billing_account_uid,
                "disable_clone_fleets": disable_clone_fleets,
                "disable_clone_routes": disable_clone_routes,
                "label": label,
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
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    def get_device_dfu_history(
        self,
        project_or_product_uid: str,
        device_uid: str,
        firmware_type: GetDeviceDfuHistoryRequestFirmwareType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeviceDfuHistory]:
        """
        Get device DFU history for host or Notecard firmware

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        firmware_type : GetDeviceDfuHistoryRequestFirmwareType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeviceDfuHistory]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/dfu/{encode_path_param(firmware_type)}/history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceDfuHistory,
                    parse_obj_as(
                        type_=DeviceDfuHistory,
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

    def get_device_dfu_status(
        self,
        project_or_product_uid: str,
        device_uid: str,
        firmware_type: GetDeviceDfuStatusRequestFirmwareType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeviceDfuStatus]:
        """
        Get device DFU history for host or Notecard firmware

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        firmware_type : GetDeviceDfuStatusRequestFirmwareType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeviceDfuStatus]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/dfu/{encode_path_param(firmware_type)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceDfuStatus,
                    parse_obj_as(
                        type_=DeviceDfuStatus,
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

    def get_device_fleets(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDeviceFleetsResponse]:
        """
        Get Device Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDeviceFleetsResponse]
            The response body from a fleets endpoint.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/fleets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceFleetsResponse,
                    parse_obj_as(
                        type_=GetDeviceFleetsResponse,
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

    def add_device_to_fleets(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        fleet_uids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AddDeviceToFleetsResponse]:
        """
        Add Device to Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        fleet_uids : typing.Sequence[str]
            The fleetUIDs to add to the device.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AddDeviceToFleetsResponse]
            The response body from a fleets endpoint.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/fleets",
            method="PUT",
            json={
                "fleet_uids": fleet_uids,
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
                    AddDeviceToFleetsResponse,
                    parse_obj_as(
                        type_=AddDeviceToFleetsResponse,
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

    def delete_device_from_fleets(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        fleet_uids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeleteDeviceFromFleetsResponse]:
        """
        Remove Device from Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        fleet_uids : typing.Sequence[str]
            The fleetUIDs to remove from the device.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteDeviceFromFleetsResponse]
            The response body from a fleets endpoint.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/fleets",
            method="DELETE",
            json={
                "fleet_uids": fleet_uids,
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
                    DeleteDeviceFromFleetsResponse,
                    parse_obj_as(
                        type_=DeleteDeviceFromFleetsResponse,
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

    def perform_dfu_action(
        self,
        project_or_product_uid: str,
        firmware_type: PerformDfuActionRequestFirmwareType,
        action: PerformDfuActionRequestAction,
        *,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Update/cancel host or notecard firmware updates

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : PerformDfuActionRequestFirmwareType

        action : PerformDfuActionRequestAction

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        filename : typing.Optional[str]
            The name of the firmware file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/dfu/{encode_path_param(firmware_type)}/{encode_path_param(action)}",
            method="POST",
            params={
                "deviceUID": device_uid,
                "tag": tag,
                "serialNumber": serial_number,
                "fleetUID": fleet_uid,
                "notecardFirmware": notecard_firmware,
                "location": location,
                "hostFirmware": host_firmware,
                "productUID": product_uid,
                "sku": sku,
            },
            json={
                "filename": filename,
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

    def get_devices_dfu_history(
        self,
        project_or_product_uid: str,
        firmware_type: GetDevicesDfuHistoryRequestFirmwareType,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        sort_by: typing.Optional[GetDevicesDfuHistoryRequestSortBy] = None,
        sort_order: typing.Optional[GetDevicesDfuHistoryRequestSortOrder] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeviceDfuHistoryPage]:
        """
        Get host or Notecard DFU history for all devices that match the filter criteria

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : GetDevicesDfuHistoryRequestFirmwareType

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        sort_by : typing.Optional[GetDevicesDfuHistoryRequestSortBy]

        sort_order : typing.Optional[GetDevicesDfuHistoryRequestSortOrder]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeviceDfuHistoryPage]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/dfu/{encode_path_param(firmware_type)}/history",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "deviceUID": device_uid,
                "tag": tag,
                "serialNumber": serial_number,
                "fleetUID": fleet_uid,
                "notecardFirmware": notecard_firmware,
                "location": location,
                "hostFirmware": host_firmware,
                "productUID": product_uid,
                "sku": sku,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceDfuHistoryPage,
                    parse_obj_as(
                        type_=DeviceDfuHistoryPage,
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

    def get_devices_dfu_status(
        self,
        project_or_product_uid: str,
        firmware_type: GetDevicesDfuStatusRequestFirmwareType,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        sort_by: typing.Optional[GetDevicesDfuStatusRequestSortBy] = None,
        sort_order: typing.Optional[GetDevicesDfuStatusRequestSortOrder] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DeviceDfuStatusPage]:
        """
        Get host or Notecard DFU history for all devices that match the filter criteria

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : GetDevicesDfuStatusRequestFirmwareType

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        sort_by : typing.Optional[GetDevicesDfuStatusRequestSortBy]

        sort_order : typing.Optional[GetDevicesDfuStatusRequestSortOrder]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeviceDfuStatusPage]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/dfu/{encode_path_param(firmware_type)}/status",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "deviceUID": device_uid,
                "tag": tag,
                "serialNumber": serial_number,
                "fleetUID": fleet_uid,
                "notecardFirmware": notecard_firmware,
                "location": location,
                "hostFirmware": host_firmware,
                "productUID": product_uid,
                "sku": sku,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceDfuStatusPage,
                    parse_obj_as(
                        type_=DeviceDfuStatusPage,
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

    def get_project_environment_hierarchy(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvTreeJsonNode]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvTreeJsonNode]
            Successfully retrieved project environment hierarchy
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/environment_hierarchy",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvTreeJsonNode,
                    parse_obj_as(
                        type_=EnvTreeJsonNode,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_project_environment_variables(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvironmentVariables]:
        """
        Get environment variables of a project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/environment_variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    def set_project_environment_variables(
        self,
        project_or_product_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariables]:
        """
        Set environment variables of a project

        Parameters
        ----------
        project_or_product_uid : str

        environment_variables : typing.Dict[str, str]

        environment_variable_notes : typing.Optional[typing.Dict[str, str]]
            Optional per-variable annotations, keyed by variable name. Setting a key to an empty string removes its note. A 400 error is returned for any key that does not already exist as a stored variable and is not included in environment_variables in the same request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/environment_variables",
            method="PUT",
            json={
                "environment_variable_notes": environment_variable_notes,
                "environment_variables": environment_variables,
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
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    def delete_project_environment_variable(
        self, project_or_product_uid: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvironmentVariables]:
        """
        Delete an environment variable of a project by key

        Parameters
        ----------
        project_or_product_uid : str

        key : str
            The environment variable key to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/environment_variables/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    def get_firmware_info(
        self,
        project_or_product_uid: str,
        *,
        product: typing.Optional[str] = None,
        firmware_type: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        md5: typing.Optional[str] = None,
        unpublished: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetFirmwareInfoRequestSortBy] = None,
        sort_order: typing.Optional[GetFirmwareInfoRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[FirmwareInfo]]:
        """
        Get Available Firmware Information

        Parameters
        ----------
        project_or_product_uid : str

        product : typing.Optional[str]

        firmware_type : typing.Optional[str]

        version : typing.Optional[str]

        target : typing.Optional[str]

        filename : typing.Optional[str]

        md5 : typing.Optional[str]

        unpublished : typing.Optional[bool]

        sort_by : typing.Optional[GetFirmwareInfoRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[GetFirmwareInfoRequestSortOrder]
            Sort order (asc for ascending, desc for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FirmwareInfo]]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware",
            method="GET",
            params={
                "product": product,
                "firmwareType": firmware_type,
                "version": version,
                "target": target,
                "filename": filename,
                "md5": md5,
                "unpublished": unpublished,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FirmwareInfo],
                    parse_obj_as(
                        type_=typing.List[FirmwareInfo],
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

    @contextlib.contextmanager
    def download_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: DownloadFirmwareRequestFirmwareType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Download firmware binary

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : DownloadFirmwareRequestFirmwareType

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Firmware binary
        """
        with self._client_wrapper.httpx_client.stream(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware/{encode_path_param(firmware_type)}/{encode_path_param(filename)}",
            method="GET",
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def update_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: UpdateFirmwareRequestFirmwareType,
        filename: str,
        *,
        info: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FirmwareInfo]:
        """
        Update the metadata of an existing host firmware entry. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : UpdateFirmwareRequestFirmwareType

        filename : str

        info : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary JSON metadata associated with this firmware entry.

        notes : typing.Optional[str]
            Notes describing this firmware version.

        version : typing.Optional[str]
            The firmware version string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FirmwareInfo]
            Update successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware/{encode_path_param(firmware_type)}/{encode_path_param(filename)}",
            method="POST",
            json={
                "info": info,
                "notes": notes,
                "version": version,
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
                    FirmwareInfo,
                    parse_obj_as(
                        type_=FirmwareInfo,
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

    def upload_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: UploadFirmwareRequestFirmwareType,
        filename: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        version: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FirmwareInfo]:
        """
        Upload firmware binary

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : UploadFirmwareRequestFirmwareType

        filename : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        version : typing.Optional[str]
            Firmware version (optional). If not provided, the version will be extracted from firmware binary if available, otherwise left empty

        notes : typing.Optional[str]
            Optional notes describing what's different about this firmware version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FirmwareInfo]
            Upload successful
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware/{encode_path_param(firmware_type)}/{encode_path_param(filename)}",
            method="PUT",
            params={
                "version": version,
                "notes": notes,
            },
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FirmwareInfo,
                    parse_obj_as(
                        type_=FirmwareInfo,
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

    def delete_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: DeleteFirmwareRequestFirmwareType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete a host firmware binary. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : DeleteFirmwareRequestFirmwareType

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware/{encode_path_param(firmware_type)}/{encode_path_param(filename)}",
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

    def get_fleets(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetFleetsResponse]:
        """
        Get Project Fleets

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFleetsResponse]
            The response body from a fleets endpoint.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFleetsResponse,
                    parse_obj_as(
                        type_=GetFleetsResponse,
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

    def create_fleet(
        self,
        project_or_product_uid: str,
        *,
        connectivity_assurance: typing.Optional[FleetConnectivityAssurance] = OMIT,
        label: typing.Optional[str] = OMIT,
        smart_rule: typing.Optional[FleetRule] = OMIT,
        smart_rule_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Fleet]:
        """
        Create Fleet

        Parameters
        ----------
        project_or_product_uid : str

        connectivity_assurance : typing.Optional[FleetConnectivityAssurance]

        label : typing.Optional[str]
            The label, or name,  for the Fleet.

        smart_rule : typing.Optional[FleetRule]

        smart_rule_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Fleet]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets",
            method="POST",
            json={
                "connectivity_assurance": convert_and_respect_annotation_metadata(
                    object_=connectivity_assurance,
                    annotation=typing.Optional[FleetConnectivityAssurance],
                    direction="write",
                ),
                "label": label,
                "smart_rule": smart_rule,
                "smart_rule_enabled": smart_rule_enabled,
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
                    Fleet,
                    parse_obj_as(
                        type_=Fleet,
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

    def get_fleet(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Fleet]:
        """
        Get Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Fleet]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Fleet,
                    parse_obj_as(
                        type_=Fleet,
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

    def update_fleet(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        add_devices: typing.Optional[typing.Sequence[str]] = OMIT,
        connectivity_assurance: typing.Optional[FleetConnectivityAssurance] = OMIT,
        label: typing.Optional[str] = OMIT,
        remove_devices: typing.Optional[typing.Sequence[str]] = OMIT,
        smart_rule: typing.Optional[FleetRule] = OMIT,
        smart_rule_enabled: typing.Optional[bool] = OMIT,
        watchdog_mins: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Fleet]:
        """
        Update Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        add_devices : typing.Optional[typing.Sequence[str]]
            List of DeviceUIDs to add to fleet

        connectivity_assurance : typing.Optional[FleetConnectivityAssurance]

        label : typing.Optional[str]
            The label for the Fleet.

        remove_devices : typing.Optional[typing.Sequence[str]]
            List of DeviceUIDs to remove from fleet

        smart_rule : typing.Optional[FleetRule]

        smart_rule_enabled : typing.Optional[bool]

        watchdog_mins : typing.Optional[int]
            A watchdog timer is used to generate an event every N minutes of inactivity. 0 means no watchdog

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Fleet]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}",
            method="PUT",
            json={
                "addDevices": add_devices,
                "connectivity_assurance": convert_and_respect_annotation_metadata(
                    object_=connectivity_assurance,
                    annotation=typing.Optional[FleetConnectivityAssurance],
                    direction="write",
                ),
                "label": label,
                "removeDevices": remove_devices,
                "smart_rule": smart_rule,
                "smart_rule_enabled": smart_rule_enabled,
                "watchdog_mins": watchdog_mins,
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
                    Fleet,
                    parse_obj_as(
                        type_=Fleet,
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

    def delete_fleet(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}",
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

    def get_fleet_environment_hierarchy(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvTreeJsonNode]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvTreeJsonNode]
            Successfully retrieved fleet environment hierarchy
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/environment_hierarchy",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvTreeJsonNode,
                    parse_obj_as(
                        type_=EnvTreeJsonNode,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    def get_fleet_environment_variables(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvironmentVariables]:
        """
        Get environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/environment_variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    def set_fleet_environment_variables(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariables]:
        """
        Set environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        environment_variables : typing.Dict[str, str]

        environment_variable_notes : typing.Optional[typing.Dict[str, str]]
            Optional per-variable annotations, keyed by variable name. Setting a key to an empty string removes its note. A 400 error is returned for any key that does not already exist as a stored variable and is not included in environment_variables in the same request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/environment_variables",
            method="PUT",
            json={
                "environment_variable_notes": environment_variable_notes,
                "environment_variables": environment_variables,
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
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    def delete_fleet_environment_variable(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariables]:
        """
        Delete environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        key : str
            The environment variable key to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/environment_variables/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    def set_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Set the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/global-transformation",
            method="POST",
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

    def disable_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Disable the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/global-transformation/disable",
            method="POST",
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

    def enable_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Enable the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/global-transformation/enable",
            method="POST",
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

    def get_project_members(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetProjectMembersResponse]:
        """
        Get Project Members

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProjectMembersResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/members",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectMembersResponse,
                    parse_obj_as(
                        type_=GetProjectMembersResponse,
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

    def get_products(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetProductsResponse]:
        """
        Get Products within a Project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProductsResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/products",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProductsResponse,
                    parse_obj_as(
                        type_=GetProductsResponse,
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

    def create_product(
        self,
        project_or_product_uid: str,
        *,
        label: str,
        product_uid: str,
        auto_provision_fleets: typing.Optional[typing.Sequence[str]] = OMIT,
        disable_devices_by_default: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Product]:
        """
        Create Product within a Project

        Parameters
        ----------
        project_or_product_uid : str

        label : str
            The label for the Product.

        product_uid : str
            The requested uid for the Product. Will be prefixed with the user's reversed email.

        auto_provision_fleets : typing.Optional[typing.Sequence[str]]

        disable_devices_by_default : typing.Optional[bool]
            If `true`, devices provisioned to this product will be automatically disabled by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Product]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/products",
            method="POST",
            json={
                "auto_provision_fleets": auto_provision_fleets,
                "disable_devices_by_default": disable_devices_by_default,
                "label": label,
                "product_uid": product_uid,
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
                    Product,
                    parse_obj_as(
                        type_=Product,
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

    def delete_product(
        self, project_or_product_uid: str, product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a product

        Parameters
        ----------
        project_or_product_uid : str

        product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/products/{encode_path_param(product_uid)}",
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

    def get_notefile_schemas(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[NotefileSchema]]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[NotefileSchema]]
            List of notefile schema definitions
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/schemas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotefileSchema],
                    parse_obj_as(
                        type_=typing.List[NotefileSchema],
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

    def get_project_secrets(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetProjectSecretsResponse]:
        """
        Get all secrets for a project (metadata only, values are never returned)

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetProjectSecretsResponse]
            The response body from a get project secrets request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/secrets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectSecretsResponse,
                    parse_obj_as(
                        type_=GetProjectSecretsResponse,
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

    def create_project_secret(
        self,
        project_or_product_uid: str,
        *,
        name: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectSecret]:
        """
        Create a new project secret

        Parameters
        ----------
        project_or_product_uid : str

        name : str
            The secret name (alphanumeric and underscores only).

        value : str
            The secret value (encrypted at rest, never returned after creation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectSecret]
            Secret created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/secrets",
            method="POST",
            json={
                "name": name,
                "value": value,
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
                    ProjectSecret,
                    parse_obj_as(
                        type_=ProjectSecret,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_project_secret(
        self,
        project_or_product_uid: str,
        secret_name: str,
        *,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectSecret]:
        """
        Update the value of an existing project secret

        Parameters
        ----------
        project_or_product_uid : str

        secret_name : str
            The name of the secret.

        value : str
            The new secret value (encrypted at rest, never returned).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectSecret]
            Secret updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/secrets/{encode_path_param(secret_name)}",
            method="PUT",
            json={
                "value": value,
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
                    ProjectSecret,
                    parse_obj_as(
                        type_=ProjectSecret,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    def delete_project_secret(
        self, project_or_product_uid: str, secret_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a project secret by name

        Parameters
        ----------
        project_or_product_uid : str

        secret_name : str
            The name of the secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/secrets/{encode_path_param(secret_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
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


class AsyncRawProjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_project_by_product(
        self, product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Project]:
        """
        Get a Project by ProductUID

        Parameters
        ----------
        product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Project]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/project",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    async def get_projects(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetProjectsResponse]:
        """
        Get Projects accessible by the api_key

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProjectsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/projects",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectsResponse,
                    parse_obj_as(
                        type_=GetProjectsResponse,
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

    async def create_project(
        self, *, billing_account_uid: str, label: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Project]:
        """
        Create a Project

        Parameters
        ----------
        billing_account_uid : str
            The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.

        label : str
            The label for the project.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Project]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/projects",
            method="POST",
            json={
                "billing_account_uid": billing_account_uid,
                "label": label,
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
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    async def get_project(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Project]:
        """
        Get a Project by ProjectUID

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Project]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    async def delete_project(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a Project by ProjectUID

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}",
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

    async def get_aws_role_config(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AwsRoleConfig]:
        """
        Returns the AWS Account ID and External ID needed to configure an IAM role
        trust policy for role-based authentication on AWS routes.

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AwsRoleConfig]
            AWS role configuration
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/aws-role-config",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AwsRoleConfig,
                    parse_obj_as(
                        type_=AwsRoleConfig,
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

    async def clone_project(
        self,
        project_or_product_uid: str,
        *,
        billing_account_uid: str,
        label: str,
        disable_clone_fleets: typing.Optional[bool] = OMIT,
        disable_clone_routes: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Project]:
        """
        Clone a Project

        Parameters
        ----------
        project_or_product_uid : str

        billing_account_uid : str
            The billing account UID for the project. The caller of the API must be able to create projects within the billing account, otherwise an error will be returned.

        label : str
            The label for the project.

        disable_clone_fleets : typing.Optional[bool]
            Whether to disallow the cloning of the fleets from the parent project.  Default is false if not specified.

        disable_clone_routes : typing.Optional[bool]
            Whether to disallow the cloning of the routes from the parent project.  Default is false if not specified.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Project]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/clone",
            method="POST",
            json={
                "billing_account_uid": billing_account_uid,
                "disable_clone_fleets": disable_clone_fleets,
                "disable_clone_routes": disable_clone_routes,
                "label": label,
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
                    Project,
                    parse_obj_as(
                        type_=Project,
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

    async def get_device_dfu_history(
        self,
        project_or_product_uid: str,
        device_uid: str,
        firmware_type: GetDeviceDfuHistoryRequestFirmwareType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeviceDfuHistory]:
        """
        Get device DFU history for host or Notecard firmware

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        firmware_type : GetDeviceDfuHistoryRequestFirmwareType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeviceDfuHistory]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/dfu/{encode_path_param(firmware_type)}/history",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceDfuHistory,
                    parse_obj_as(
                        type_=DeviceDfuHistory,
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

    async def get_device_dfu_status(
        self,
        project_or_product_uid: str,
        device_uid: str,
        firmware_type: GetDeviceDfuStatusRequestFirmwareType,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeviceDfuStatus]:
        """
        Get device DFU history for host or Notecard firmware

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        firmware_type : GetDeviceDfuStatusRequestFirmwareType

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeviceDfuStatus]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/dfu/{encode_path_param(firmware_type)}/status",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceDfuStatus,
                    parse_obj_as(
                        type_=DeviceDfuStatus,
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

    async def get_device_fleets(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDeviceFleetsResponse]:
        """
        Get Device Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDeviceFleetsResponse]
            The response body from a fleets endpoint.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/fleets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceFleetsResponse,
                    parse_obj_as(
                        type_=GetDeviceFleetsResponse,
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

    async def add_device_to_fleets(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        fleet_uids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AddDeviceToFleetsResponse]:
        """
        Add Device to Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        fleet_uids : typing.Sequence[str]
            The fleetUIDs to add to the device.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AddDeviceToFleetsResponse]
            The response body from a fleets endpoint.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/fleets",
            method="PUT",
            json={
                "fleet_uids": fleet_uids,
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
                    AddDeviceToFleetsResponse,
                    parse_obj_as(
                        type_=AddDeviceToFleetsResponse,
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

    async def delete_device_from_fleets(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        fleet_uids: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeleteDeviceFromFleetsResponse]:
        """
        Remove Device from Fleets

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        fleet_uids : typing.Sequence[str]
            The fleetUIDs to remove from the device.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteDeviceFromFleetsResponse]
            The response body from a fleets endpoint.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/fleets",
            method="DELETE",
            json={
                "fleet_uids": fleet_uids,
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
                    DeleteDeviceFromFleetsResponse,
                    parse_obj_as(
                        type_=DeleteDeviceFromFleetsResponse,
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

    async def perform_dfu_action(
        self,
        project_or_product_uid: str,
        firmware_type: PerformDfuActionRequestFirmwareType,
        action: PerformDfuActionRequestAction,
        *,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Update/cancel host or notecard firmware updates

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : PerformDfuActionRequestFirmwareType

        action : PerformDfuActionRequestAction

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        filename : typing.Optional[str]
            The name of the firmware file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/dfu/{encode_path_param(firmware_type)}/{encode_path_param(action)}",
            method="POST",
            params={
                "deviceUID": device_uid,
                "tag": tag,
                "serialNumber": serial_number,
                "fleetUID": fleet_uid,
                "notecardFirmware": notecard_firmware,
                "location": location,
                "hostFirmware": host_firmware,
                "productUID": product_uid,
                "sku": sku,
            },
            json={
                "filename": filename,
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

    async def get_devices_dfu_history(
        self,
        project_or_product_uid: str,
        firmware_type: GetDevicesDfuHistoryRequestFirmwareType,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        sort_by: typing.Optional[GetDevicesDfuHistoryRequestSortBy] = None,
        sort_order: typing.Optional[GetDevicesDfuHistoryRequestSortOrder] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeviceDfuHistoryPage]:
        """
        Get host or Notecard DFU history for all devices that match the filter criteria

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : GetDevicesDfuHistoryRequestFirmwareType

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        sort_by : typing.Optional[GetDevicesDfuHistoryRequestSortBy]

        sort_order : typing.Optional[GetDevicesDfuHistoryRequestSortOrder]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeviceDfuHistoryPage]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/dfu/{encode_path_param(firmware_type)}/history",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "deviceUID": device_uid,
                "tag": tag,
                "serialNumber": serial_number,
                "fleetUID": fleet_uid,
                "notecardFirmware": notecard_firmware,
                "location": location,
                "hostFirmware": host_firmware,
                "productUID": product_uid,
                "sku": sku,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceDfuHistoryPage,
                    parse_obj_as(
                        type_=DeviceDfuHistoryPage,
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

    async def get_devices_dfu_status(
        self,
        project_or_product_uid: str,
        firmware_type: GetDevicesDfuStatusRequestFirmwareType,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        sort_by: typing.Optional[GetDevicesDfuStatusRequestSortBy] = None,
        sort_order: typing.Optional[GetDevicesDfuStatusRequestSortOrder] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[str] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DeviceDfuStatusPage]:
        """
        Get host or Notecard DFU history for all devices that match the filter criteria

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : GetDevicesDfuStatusRequestFirmwareType

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        sort_by : typing.Optional[GetDevicesDfuStatusRequestSortBy]

        sort_order : typing.Optional[GetDevicesDfuStatusRequestSortOrder]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[str]

        notecard_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Firmware version filter

        location : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Location filter

        host_firmware : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Host firmware filter

        product_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

        sku : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            SKU filter

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeviceDfuStatusPage]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/dfu/{encode_path_param(firmware_type)}/status",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "sortBy": sort_by,
                "sortOrder": sort_order,
                "deviceUID": device_uid,
                "tag": tag,
                "serialNumber": serial_number,
                "fleetUID": fleet_uid,
                "notecardFirmware": notecard_firmware,
                "location": location,
                "hostFirmware": host_firmware,
                "productUID": product_uid,
                "sku": sku,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeviceDfuStatusPage,
                    parse_obj_as(
                        type_=DeviceDfuStatusPage,
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

    async def get_project_environment_hierarchy(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvTreeJsonNode]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvTreeJsonNode]
            Successfully retrieved project environment hierarchy
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/environment_hierarchy",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvTreeJsonNode,
                    parse_obj_as(
                        type_=EnvTreeJsonNode,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_project_environment_variables(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvironmentVariables]:
        """
        Get environment variables of a project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/environment_variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    async def set_project_environment_variables(
        self,
        project_or_product_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvironmentVariables]:
        """
        Set environment variables of a project

        Parameters
        ----------
        project_or_product_uid : str

        environment_variables : typing.Dict[str, str]

        environment_variable_notes : typing.Optional[typing.Dict[str, str]]
            Optional per-variable annotations, keyed by variable name. Setting a key to an empty string removes its note. A 400 error is returned for any key that does not already exist as a stored variable and is not included in environment_variables in the same request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/environment_variables",
            method="PUT",
            json={
                "environment_variable_notes": environment_variable_notes,
                "environment_variables": environment_variables,
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
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    async def delete_project_environment_variable(
        self, project_or_product_uid: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvironmentVariables]:
        """
        Delete an environment variable of a project by key

        Parameters
        ----------
        project_or_product_uid : str

        key : str
            The environment variable key to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/environment_variables/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    async def get_firmware_info(
        self,
        project_or_product_uid: str,
        *,
        product: typing.Optional[str] = None,
        firmware_type: typing.Optional[str] = None,
        version: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        filename: typing.Optional[str] = None,
        md5: typing.Optional[str] = None,
        unpublished: typing.Optional[bool] = None,
        sort_by: typing.Optional[GetFirmwareInfoRequestSortBy] = None,
        sort_order: typing.Optional[GetFirmwareInfoRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[FirmwareInfo]]:
        """
        Get Available Firmware Information

        Parameters
        ----------
        project_or_product_uid : str

        product : typing.Optional[str]

        firmware_type : typing.Optional[str]

        version : typing.Optional[str]

        target : typing.Optional[str]

        filename : typing.Optional[str]

        md5 : typing.Optional[str]

        unpublished : typing.Optional[bool]

        sort_by : typing.Optional[GetFirmwareInfoRequestSortBy]
            Field to sort by

        sort_order : typing.Optional[GetFirmwareInfoRequestSortOrder]
            Sort order (asc for ascending, desc for descending)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FirmwareInfo]]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware",
            method="GET",
            params={
                "product": product,
                "firmwareType": firmware_type,
                "version": version,
                "target": target,
                "filename": filename,
                "md5": md5,
                "unpublished": unpublished,
                "sortBy": sort_by,
                "sortOrder": sort_order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FirmwareInfo],
                    parse_obj_as(
                        type_=typing.List[FirmwareInfo],
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

    @contextlib.asynccontextmanager
    async def download_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: DownloadFirmwareRequestFirmwareType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Download firmware binary

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : DownloadFirmwareRequestFirmwareType

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Firmware binary
        """
        async with self._client_wrapper.httpx_client.stream(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware/{encode_path_param(firmware_type)}/{encode_path_param(filename)}",
            method="GET",
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def update_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: UpdateFirmwareRequestFirmwareType,
        filename: str,
        *,
        info: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        notes: typing.Optional[str] = OMIT,
        version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FirmwareInfo]:
        """
        Update the metadata of an existing host firmware entry. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : UpdateFirmwareRequestFirmwareType

        filename : str

        info : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary JSON metadata associated with this firmware entry.

        notes : typing.Optional[str]
            Notes describing this firmware version.

        version : typing.Optional[str]
            The firmware version string.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FirmwareInfo]
            Update successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware/{encode_path_param(firmware_type)}/{encode_path_param(filename)}",
            method="POST",
            json={
                "info": info,
                "notes": notes,
                "version": version,
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
                    FirmwareInfo,
                    parse_obj_as(
                        type_=FirmwareInfo,
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

    async def upload_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: UploadFirmwareRequestFirmwareType,
        filename: str,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        version: typing.Optional[str] = None,
        notes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FirmwareInfo]:
        """
        Upload firmware binary

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : UploadFirmwareRequestFirmwareType

        filename : str

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        version : typing.Optional[str]
            Firmware version (optional). If not provided, the version will be extracted from firmware binary if available, otherwise left empty

        notes : typing.Optional[str]
            Optional notes describing what's different about this firmware version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FirmwareInfo]
            Upload successful
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware/{encode_path_param(firmware_type)}/{encode_path_param(filename)}",
            method="PUT",
            params={
                "version": version,
                "notes": notes,
            },
            content=request,
            headers={
                "content-type": "application/octet-stream",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FirmwareInfo,
                    parse_obj_as(
                        type_=FirmwareInfo,
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

    async def delete_firmware(
        self,
        project_or_product_uid: str,
        firmware_type: DeleteFirmwareRequestFirmwareType,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete a host firmware binary. The filename must be the full stored filename including the timestamp suffix (e.g. test$20260324190911.bin) as returned by the firmware upload or list endpoints.

        Parameters
        ----------
        project_or_product_uid : str

        firmware_type : DeleteFirmwareRequestFirmwareType

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/firmware/{encode_path_param(firmware_type)}/{encode_path_param(filename)}",
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

    async def get_fleets(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetFleetsResponse]:
        """
        Get Project Fleets

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFleetsResponse]
            The response body from a fleets endpoint.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFleetsResponse,
                    parse_obj_as(
                        type_=GetFleetsResponse,
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

    async def create_fleet(
        self,
        project_or_product_uid: str,
        *,
        connectivity_assurance: typing.Optional[FleetConnectivityAssurance] = OMIT,
        label: typing.Optional[str] = OMIT,
        smart_rule: typing.Optional[FleetRule] = OMIT,
        smart_rule_enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Fleet]:
        """
        Create Fleet

        Parameters
        ----------
        project_or_product_uid : str

        connectivity_assurance : typing.Optional[FleetConnectivityAssurance]

        label : typing.Optional[str]
            The label, or name,  for the Fleet.

        smart_rule : typing.Optional[FleetRule]

        smart_rule_enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Fleet]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets",
            method="POST",
            json={
                "connectivity_assurance": convert_and_respect_annotation_metadata(
                    object_=connectivity_assurance,
                    annotation=typing.Optional[FleetConnectivityAssurance],
                    direction="write",
                ),
                "label": label,
                "smart_rule": smart_rule,
                "smart_rule_enabled": smart_rule_enabled,
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
                    Fleet,
                    parse_obj_as(
                        type_=Fleet,
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

    async def get_fleet(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Fleet]:
        """
        Get Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Fleet]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Fleet,
                    parse_obj_as(
                        type_=Fleet,
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

    async def update_fleet(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        add_devices: typing.Optional[typing.Sequence[str]] = OMIT,
        connectivity_assurance: typing.Optional[FleetConnectivityAssurance] = OMIT,
        label: typing.Optional[str] = OMIT,
        remove_devices: typing.Optional[typing.Sequence[str]] = OMIT,
        smart_rule: typing.Optional[FleetRule] = OMIT,
        smart_rule_enabled: typing.Optional[bool] = OMIT,
        watchdog_mins: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Fleet]:
        """
        Update Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        add_devices : typing.Optional[typing.Sequence[str]]
            List of DeviceUIDs to add to fleet

        connectivity_assurance : typing.Optional[FleetConnectivityAssurance]

        label : typing.Optional[str]
            The label for the Fleet.

        remove_devices : typing.Optional[typing.Sequence[str]]
            List of DeviceUIDs to remove from fleet

        smart_rule : typing.Optional[FleetRule]

        smart_rule_enabled : typing.Optional[bool]

        watchdog_mins : typing.Optional[int]
            A watchdog timer is used to generate an event every N minutes of inactivity. 0 means no watchdog

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Fleet]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}",
            method="PUT",
            json={
                "addDevices": add_devices,
                "connectivity_assurance": convert_and_respect_annotation_metadata(
                    object_=connectivity_assurance,
                    annotation=typing.Optional[FleetConnectivityAssurance],
                    direction="write",
                ),
                "label": label,
                "removeDevices": remove_devices,
                "smart_rule": smart_rule,
                "smart_rule_enabled": smart_rule_enabled,
                "watchdog_mins": watchdog_mins,
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
                    Fleet,
                    parse_obj_as(
                        type_=Fleet,
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

    async def delete_fleet(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete Fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}",
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

    async def get_fleet_environment_hierarchy(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvTreeJsonNode]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvTreeJsonNode]
            Successfully retrieved fleet environment hierarchy
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/environment_hierarchy",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvTreeJsonNode,
                    parse_obj_as(
                        type_=EnvTreeJsonNode,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
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

    async def get_fleet_environment_variables(
        self, project_or_product_uid: str, fleet_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvironmentVariables]:
        """
        Get environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/environment_variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    async def set_fleet_environment_variables(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvironmentVariables]:
        """
        Set environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        environment_variables : typing.Dict[str, str]

        environment_variable_notes : typing.Optional[typing.Dict[str, str]]
            Optional per-variable annotations, keyed by variable name. Setting a key to an empty string removes its note. A 400 error is returned for any key that does not already exist as a stored variable and is not included in environment_variables in the same request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/environment_variables",
            method="PUT",
            json={
                "environment_variable_notes": environment_variable_notes,
                "environment_variables": environment_variables,
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
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    async def delete_fleet_environment_variable(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvironmentVariables]:
        """
        Delete environment variables of a fleet

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        key : str
            The environment variable key to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvironmentVariables]
            The response body from an environment variables request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/environment_variables/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvironmentVariables,
                    parse_obj_as(
                        type_=EnvironmentVariables,
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

    async def set_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Set the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/global-transformation",
            method="POST",
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

    async def disable_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Disable the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/global-transformation/disable",
            method="POST",
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

    async def enable_global_event_transformation(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Enable the project-level event JSONata transformation

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/global-transformation/enable",
            method="POST",
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

    async def get_project_members(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetProjectMembersResponse]:
        """
        Get Project Members

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProjectMembersResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/members",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectMembersResponse,
                    parse_obj_as(
                        type_=GetProjectMembersResponse,
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

    async def get_products(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetProductsResponse]:
        """
        Get Products within a Project

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProductsResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/products",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProductsResponse,
                    parse_obj_as(
                        type_=GetProductsResponse,
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

    async def create_product(
        self,
        project_or_product_uid: str,
        *,
        label: str,
        product_uid: str,
        auto_provision_fleets: typing.Optional[typing.Sequence[str]] = OMIT,
        disable_devices_by_default: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Product]:
        """
        Create Product within a Project

        Parameters
        ----------
        project_or_product_uid : str

        label : str
            The label for the Product.

        product_uid : str
            The requested uid for the Product. Will be prefixed with the user's reversed email.

        auto_provision_fleets : typing.Optional[typing.Sequence[str]]

        disable_devices_by_default : typing.Optional[bool]
            If `true`, devices provisioned to this product will be automatically disabled by default.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Product]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/products",
            method="POST",
            json={
                "auto_provision_fleets": auto_provision_fleets,
                "disable_devices_by_default": disable_devices_by_default,
                "label": label,
                "product_uid": product_uid,
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
                    Product,
                    parse_obj_as(
                        type_=Product,
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

    async def delete_product(
        self, project_or_product_uid: str, product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a product

        Parameters
        ----------
        project_or_product_uid : str

        product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/products/{encode_path_param(product_uid)}",
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

    async def get_notefile_schemas(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[NotefileSchema]]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[NotefileSchema]]
            List of notefile schema definitions
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/schemas",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[NotefileSchema],
                    parse_obj_as(
                        type_=typing.List[NotefileSchema],
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

    async def get_project_secrets(
        self, project_or_product_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetProjectSecretsResponse]:
        """
        Get all secrets for a project (metadata only, values are never returned)

        Parameters
        ----------
        project_or_product_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetProjectSecretsResponse]
            The response body from a get project secrets request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/secrets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetProjectSecretsResponse,
                    parse_obj_as(
                        type_=GetProjectSecretsResponse,
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

    async def create_project_secret(
        self,
        project_or_product_uid: str,
        *,
        name: str,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectSecret]:
        """
        Create a new project secret

        Parameters
        ----------
        project_or_product_uid : str

        name : str
            The secret name (alphanumeric and underscores only).

        value : str
            The secret value (encrypted at rest, never returned after creation).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectSecret]
            Secret created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/secrets",
            method="POST",
            json={
                "name": name,
                "value": value,
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
                    ProjectSecret,
                    parse_obj_as(
                        type_=ProjectSecret,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_project_secret(
        self,
        project_or_product_uid: str,
        secret_name: str,
        *,
        value: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectSecret]:
        """
        Update the value of an existing project secret

        Parameters
        ----------
        project_or_product_uid : str

        secret_name : str
            The name of the secret.

        value : str
            The new secret value (encrypted at rest, never returned).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectSecret]
            Secret updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/secrets/{encode_path_param(secret_name)}",
            method="PUT",
            json={
                "value": value,
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
                    ProjectSecret,
                    parse_obj_as(
                        type_=ProjectSecret,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
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

    async def delete_project_secret(
        self, project_or_product_uid: str, secret_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a project secret by name

        Parameters
        ----------
        project_or_product_uid : str

        secret_name : str
            The name of the secret.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/secrets/{encode_path_param(secret_name)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 404:
                raise NotFoundError(
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
