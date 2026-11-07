

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.device import Device
from ..types.env_tree_json_node import EnvTreeJsonNode
from ..types.environment_variables import EnvironmentVariables
from ..types.notefile_list import NotefileList
from .types.get_db_note_response import GetDbNoteResponse
from .types.get_device_environment_variables_by_pin_response import GetDeviceEnvironmentVariablesByPinResponse
from .types.get_device_environment_variables_response import GetDeviceEnvironmentVariablesResponse
from .types.get_device_health_log_request_log_type_item import GetDeviceHealthLogRequestLogTypeItem
from .types.get_device_health_log_response import GetDeviceHealthLogResponse
from .types.get_device_journey_response import GetDeviceJourneyResponse
from .types.get_device_journeys_response import GetDeviceJourneysResponse
from .types.get_device_latest_events_response import GetDeviceLatestEventsResponse
from .types.get_device_plans_response import GetDevicePlansResponse
from .types.get_device_public_key_response import GetDevicePublicKeyResponse
from .types.get_device_public_keys_response import GetDevicePublicKeysResponse
from .types.get_device_sessions_response import GetDeviceSessionsResponse
from .types.get_devices_response import GetDevicesResponse
from .types.get_fleet_devices_response import GetFleetDevicesResponse
from .types.get_notefile_response import GetNotefileResponse
from .types.signal_device_response import SignalDeviceResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDeviceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_device_environment_variables_by_pin(
        self,
        product_uid: str,
        device_uid: str,
        *,
        auth_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDeviceEnvironmentVariablesByPinResponse]:
        """
        Get environment variables of a device with device pin authorization

        Parameters
        ----------
        product_uid : str

        device_uid : str

        auth_token : str
            For accessing endpoints by Device pin.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDeviceEnvironmentVariablesByPinResponse]
            The response body from a get device environment variables request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables_with_pin",
            method="GET",
            headers={
                "X-Auth-Token": str(auth_token) if auth_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceEnvironmentVariablesByPinResponse,
                    parse_obj_as(
                        type_=GetDeviceEnvironmentVariablesByPinResponse,
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

    def set_device_environment_variables_by_pin(
        self,
        product_uid: str,
        device_uid: str,
        *,
        auth_token: str,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariables]:
        """
        Set environment variables of a device with device pin authorization

        Parameters
        ----------
        product_uid : str

        device_uid : str

        auth_token : str
            For accessing endpoints by Device pin.

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
            f"v1/products/{encode_path_param(product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables_with_pin",
            method="PUT",
            json={
                "environment_variable_notes": environment_variable_notes,
                "environment_variables": environment_variables,
            },
            headers={
                "content-type": "application/json",
                "X-Auth-Token": str(auth_token) if auth_token is not None else None,
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

    def get_devices(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDevicesResponse]:
        """
        Get Devices of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

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
        HttpResponse[GetDevicesResponse]
            List of Devices
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
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
                    GetDevicesResponse,
                    parse_obj_as(
                        type_=GetDevicesResponse,
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

    def get_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Device]:
        """
        Get Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Device]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Device,
                    parse_obj_as(
                        type_=Device,
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

    def delete_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}",
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

    def disable_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Disable Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/disable",
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

    def enable_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Enable Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/enable",
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

    def get_device_environment_hierarchy(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvTreeJsonNode]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvTreeJsonNode]
            Successfully retrieved device environment hierarchy
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/environment_hierarchy",
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

    def get_device_environment_variables(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDeviceEnvironmentVariablesResponse]:
        """
        Get environment variables of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDeviceEnvironmentVariablesResponse]
            The response body from a get device environment variables request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceEnvironmentVariablesResponse,
                    parse_obj_as(
                        type_=GetDeviceEnvironmentVariablesResponse,
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

    def set_device_environment_variables(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariables]:
        """
        Set environment variables of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables",
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

    def delete_device_environment_variable(
        self,
        project_or_product_uid: str,
        device_uid: str,
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvironmentVariables]:
        """
        Delete environment variable of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables/{encode_path_param(key)}",
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

    def list_notefiles(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        files: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[NotefileList]:
        """
        Lists .qi and .db files for the device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        files : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One or more files to obtain change information from.

        pending : typing.Optional[bool]
            show only files that are pending sync to the Notecard

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[NotefileList]
            All notefiles and their notes
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/files",
            method="GET",
            params={
                "files": files,
                "pending": pending,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotefileList,
                    parse_obj_as(
                        type_=NotefileList,
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

    def delete_notefiles(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        files: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Deletes Notefiles and the Notes they contain.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        files : typing.Optional[typing.Sequence[str]]
            Name of notefiles to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/files",
            method="DELETE",
            json={
                "files": files,
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

    def get_device_health_log(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        log_type: typing.Optional[
            typing.Union[GetDeviceHealthLogRequestLogTypeItem, typing.Sequence[GetDeviceHealthLogRequestLogTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDeviceHealthLogResponse]:
        """
        Get Device Health Log

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        log_type : typing.Optional[typing.Union[GetDeviceHealthLogRequestLogTypeItem, typing.Sequence[GetDeviceHealthLogRequestLogTypeItem]]]
            Return only specified log types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDeviceHealthLogResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/health-log",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "log_type": log_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceHealthLogResponse,
                    parse_obj_as(
                        type_=GetDeviceHealthLogResponse,
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

    def get_device_journeys(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDeviceJourneysResponse]:
        """
        Get the list of journeys for a device, derived from events whose body contains `journey` and `jcount` fields. Returns journey metadata only (no event payloads). Capped at 100 most recent journeys; `has_more` is true when the cap is hit.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDeviceJourneysResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/journeys",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceJourneysResponse,
                    parse_obj_as(
                        type_=GetDeviceJourneysResponse,
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

    def get_device_journey(
        self,
        project_or_product_uid: str,
        device_uid: str,
        journey_id: int,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDeviceJourneyResponse]:
        """
        Get a single journey for a device along with its events. The events array is paginated via `pageSize` / `pageNum`; use `journey.has_more` to detect additional pages.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        journey_id : int
            Identifier of the journey, taken from the numeric `journey` field in the event body (a Unix timestamp marking the start of the journey).

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDeviceJourneyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/journeys/{encode_path_param(journey_id)}",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceJourneyResponse,
                    parse_obj_as(
                        type_=GetDeviceJourneyResponse,
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

    def get_device_latest_events(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDeviceLatestEventsResponse]:
        """
        Get Device Latest Events

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDeviceLatestEventsResponse]
            The response body for a Latest Events request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/latest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceLatestEventsResponse,
                    parse_obj_as(
                        type_=GetDeviceLatestEventsResponse,
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

    def create_notefile(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Creates an empty Notefile on the device.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notefiles/{encode_path_param(notefile_id)}",
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

    def get_notefile(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        max: typing.Optional[int] = None,
        deleted: typing.Optional[bool] = None,
        delete: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetNotefileResponse]:
        """
        For .qi files, returns the queued up notes.  For .db files, returns all notes in the notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        max : typing.Optional[int]
            The maximum number of Notes to return in the request.

        deleted : typing.Optional[bool]
            true to return deleted notes.

        delete : typing.Optional[bool]
            true to delete the notes returned by the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetNotefileResponse]
            The note changes object
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}",
            method="GET",
            params={
                "max": max,
                "deleted": deleted,
                "delete": delete,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNotefileResponse,
                    parse_obj_as(
                        type_=GetNotefileResponse,
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

    def add_qi_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Adds a Note to a Notefile, creating the Notefile if it doesn't yet exist.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}",
            method="POST",
            json={
                "body": body,
                "payload": payload,
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

    def get_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        delete: typing.Optional[bool] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDbNoteResponse]:
        """
        Get a note from a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        delete : typing.Optional[bool]
            Whether to delete the note from the DB notefile

        deleted : typing.Optional[bool]
            Whether to return deleted notes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDbNoteResponse]
            The requested note
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}/{encode_path_param(note_id)}",
            method="GET",
            params={
                "delete": delete,
                "deleted": deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDbNoteResponse,
                    parse_obj_as(
                        type_=GetDbNoteResponse,
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

    def add_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Add a Note to a .db notefile.  if noteID is '-' then payload is ignored and empty notefile is created

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}/{encode_path_param(note_id)}",
            method="POST",
            json={
                "body": body,
                "payload": payload,
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

    def update_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Update a note in a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}/{encode_path_param(note_id)}",
            method="PUT",
            json={
                "body": body,
                "payload": payload,
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

    def delete_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Delete a note from a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}/{encode_path_param(note_id)}",
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

    def get_device_plans(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDevicePlansResponse]:
        """
        Get Data Plans associated with the device, this include the primary sim, any external sim, as well as any satellite connections.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDevicePlansResponse]
            Response body for /plans
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/plans",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDevicePlansResponse,
                    parse_obj_as(
                        type_=GetDevicePlansResponse,
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

    def provision_device(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        product_uid: str,
        device_sn: typing.Optional[str] = OMIT,
        fleet_uids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Dict[str, typing.Any]]:
        """
        Provision Device for a Project

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        product_uid : str
            The ProductUID that the device should use.

        device_sn : typing.Optional[str]
            The serial number to assign to the device.

        fleet_uids : typing.Optional[typing.Sequence[str]]
            The fleetUIDs to provision the device to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/provision",
            method="POST",
            json={
                "device_sn": device_sn,
                "fleet_uids": fleet_uids,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    def get_device_public_key(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetDevicePublicKeyResponse]:
        """
        Get Device Public Key

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDevicePublicKeyResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/public-key",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDevicePublicKeyResponse,
                    parse_obj_as(
                        type_=GetDevicePublicKeyResponse,
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

    def get_device_sessions(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        first_sync: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDeviceSessionsResponse]:
        """
        Get Device Sessions

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        first_sync : typing.Optional[bool]
            When true, filters results to only show first sync sessions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDeviceSessionsResponse]
            The response body for a session request.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/sessions",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "startDate": start_date,
                "endDate": end_date,
                "firstSync": first_sync,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceSessionsResponse,
                    parse_obj_as(
                        type_=GetDeviceSessionsResponse,
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

    def signal_device(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SignalDeviceResponse]:
        """
        Send a signal from Notehub to a Notecard.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        body : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SignalDeviceResponse]
            A status response.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/signal",
            method="POST",
            json={
                "body": body,
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
                    SignalDeviceResponse,
                    parse_obj_as(
                        type_=SignalDeviceResponse,
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

    def get_device_public_keys(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetDevicePublicKeysResponse]:
        """
        Get Device Public Keys of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDevicePublicKeysResponse]
            Successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/public-keys",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDevicePublicKeysResponse,
                    parse_obj_as(
                        type_=GetDevicePublicKeysResponse,
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

    def get_fleet_devices(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GetFleetDevicesResponse]:
        """
        Get Devices of a Fleet within a Project

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

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
        HttpResponse[GetFleetDevicesResponse]
            List of Devices
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/devices",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "deviceUID": device_uid,
                "tag": tag,
                "serialNumber": serial_number,
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
                    GetFleetDevicesResponse,
                    parse_obj_as(
                        type_=GetFleetDevicesResponse,
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


class AsyncRawDeviceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_device_environment_variables_by_pin(
        self,
        product_uid: str,
        device_uid: str,
        *,
        auth_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDeviceEnvironmentVariablesByPinResponse]:
        """
        Get environment variables of a device with device pin authorization

        Parameters
        ----------
        product_uid : str

        device_uid : str

        auth_token : str
            For accessing endpoints by Device pin.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDeviceEnvironmentVariablesByPinResponse]
            The response body from a get device environment variables request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/products/{encode_path_param(product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables_with_pin",
            method="GET",
            headers={
                "X-Auth-Token": str(auth_token) if auth_token is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceEnvironmentVariablesByPinResponse,
                    parse_obj_as(
                        type_=GetDeviceEnvironmentVariablesByPinResponse,
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

    async def set_device_environment_variables_by_pin(
        self,
        product_uid: str,
        device_uid: str,
        *,
        auth_token: str,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvironmentVariables]:
        """
        Set environment variables of a device with device pin authorization

        Parameters
        ----------
        product_uid : str

        device_uid : str

        auth_token : str
            For accessing endpoints by Device pin.

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
            f"v1/products/{encode_path_param(product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables_with_pin",
            method="PUT",
            json={
                "environment_variable_notes": environment_variable_notes,
                "environment_variables": environment_variables,
            },
            headers={
                "content-type": "application/json",
                "X-Auth-Token": str(auth_token) if auth_token is not None else None,
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

    async def get_devices(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        fleet_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDevicesResponse]:
        """
        Get Devices of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

        fleet_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]

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
        AsyncHttpResponse[GetDevicesResponse]
            List of Devices
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
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
                    GetDevicesResponse,
                    parse_obj_as(
                        type_=GetDevicesResponse,
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

    async def get_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Device]:
        """
        Get Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Device]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Device,
                    parse_obj_as(
                        type_=Device,
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

    async def delete_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}",
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

    async def disable_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Disable Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/disable",
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

    async def enable_device(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Enable Device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/enable",
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

    async def get_device_environment_hierarchy(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvTreeJsonNode]:
        """
        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvTreeJsonNode]
            Successfully retrieved device environment hierarchy
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/environment_hierarchy",
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

    async def get_device_environment_variables(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDeviceEnvironmentVariablesResponse]:
        """
        Get environment variables of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDeviceEnvironmentVariablesResponse]
            The response body from a get device environment variables request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceEnvironmentVariablesResponse,
                    parse_obj_as(
                        type_=GetDeviceEnvironmentVariablesResponse,
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

    async def set_device_environment_variables(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        environment_variables: typing.Dict[str, str],
        environment_variable_notes: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvironmentVariables]:
        """
        Set environment variables of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables",
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

    async def delete_device_environment_variable(
        self,
        project_or_product_uid: str,
        device_uid: str,
        key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvironmentVariables]:
        """
        Delete environment variable of a device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

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
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/environment_variables/{encode_path_param(key)}",
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

    async def list_notefiles(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        files: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        pending: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[NotefileList]:
        """
        Lists .qi and .db files for the device

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        files : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            One or more files to obtain change information from.

        pending : typing.Optional[bool]
            show only files that are pending sync to the Notecard

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[NotefileList]
            All notefiles and their notes
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/files",
            method="GET",
            params={
                "files": files,
                "pending": pending,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    NotefileList,
                    parse_obj_as(
                        type_=NotefileList,
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

    async def delete_notefiles(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        files: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Deletes Notefiles and the Notes they contain.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        files : typing.Optional[typing.Sequence[str]]
            Name of notefiles to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/files",
            method="DELETE",
            json={
                "files": files,
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

    async def get_device_health_log(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        log_type: typing.Optional[
            typing.Union[GetDeviceHealthLogRequestLogTypeItem, typing.Sequence[GetDeviceHealthLogRequestLogTypeItem]]
        ] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDeviceHealthLogResponse]:
        """
        Get Device Health Log

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        log_type : typing.Optional[typing.Union[GetDeviceHealthLogRequestLogTypeItem, typing.Sequence[GetDeviceHealthLogRequestLogTypeItem]]]
            Return only specified log types

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDeviceHealthLogResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/health-log",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
                "log_type": log_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceHealthLogResponse,
                    parse_obj_as(
                        type_=GetDeviceHealthLogResponse,
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

    async def get_device_journeys(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDeviceJourneysResponse]:
        """
        Get the list of journeys for a device, derived from events whose body contains `journey` and `jcount` fields. Returns journey metadata only (no event payloads). Capped at 100 most recent journeys; `has_more` is true when the cap is hit.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDeviceJourneysResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/journeys",
            method="GET",
            params={
                "startDate": start_date,
                "endDate": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceJourneysResponse,
                    parse_obj_as(
                        type_=GetDeviceJourneysResponse,
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

    async def get_device_journey(
        self,
        project_or_product_uid: str,
        device_uid: str,
        journey_id: int,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDeviceJourneyResponse]:
        """
        Get a single journey for a device along with its events. The events array is paginated via `pageSize` / `pageNum`; use `journey.has_more` to detect additional pages.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        journey_id : int
            Identifier of the journey, taken from the numeric `journey` field in the event body (a Unix timestamp marking the start of the journey).

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDeviceJourneyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/journeys/{encode_path_param(journey_id)}",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceJourneyResponse,
                    parse_obj_as(
                        type_=GetDeviceJourneyResponse,
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

    async def get_device_latest_events(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDeviceLatestEventsResponse]:
        """
        Get Device Latest Events

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDeviceLatestEventsResponse]
            The response body for a Latest Events request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/latest",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceLatestEventsResponse,
                    parse_obj_as(
                        type_=GetDeviceLatestEventsResponse,
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

    async def create_notefile(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Creates an empty Notefile on the device.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notefiles/{encode_path_param(notefile_id)}",
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

    async def get_notefile(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        max: typing.Optional[int] = None,
        deleted: typing.Optional[bool] = None,
        delete: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetNotefileResponse]:
        """
        For .qi files, returns the queued up notes.  For .db files, returns all notes in the notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        max : typing.Optional[int]
            The maximum number of Notes to return in the request.

        deleted : typing.Optional[bool]
            true to return deleted notes.

        delete : typing.Optional[bool]
            true to delete the notes returned by the request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetNotefileResponse]
            The note changes object
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}",
            method="GET",
            params={
                "max": max,
                "deleted": deleted,
                "delete": delete,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetNotefileResponse,
                    parse_obj_as(
                        type_=GetNotefileResponse,
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

    async def add_qi_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Adds a Note to a Notefile, creating the Notefile if it doesn't yet exist.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}",
            method="POST",
            json={
                "body": body,
                "payload": payload,
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

    async def get_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        delete: typing.Optional[bool] = None,
        deleted: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDbNoteResponse]:
        """
        Get a note from a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        delete : typing.Optional[bool]
            Whether to delete the note from the DB notefile

        deleted : typing.Optional[bool]
            Whether to return deleted notes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDbNoteResponse]
            The requested note
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}/{encode_path_param(note_id)}",
            method="GET",
            params={
                "delete": delete,
                "deleted": deleted,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDbNoteResponse,
                    parse_obj_as(
                        type_=GetDbNoteResponse,
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

    async def add_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Add a Note to a .db notefile.  if noteID is '-' then payload is ignored and empty notefile is created

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}/{encode_path_param(note_id)}",
            method="POST",
            json={
                "body": body,
                "payload": payload,
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

    async def update_db_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        payload: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Update a note in a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        body : typing.Optional[typing.Dict[str, typing.Any]]
            Arbitrary user-defined JSON for the note.

        payload : typing.Optional[str]
            Optional base64-encoded payload.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}/{encode_path_param(note_id)}",
            method="PUT",
            json={
                "body": body,
                "payload": payload,
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

    async def delete_note(
        self,
        project_or_product_uid: str,
        device_uid: str,
        notefile_id: str,
        note_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Delete a note from a .db or .qi notefile

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        notefile_id : str

        note_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/notes/{encode_path_param(notefile_id)}/{encode_path_param(note_id)}",
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

    async def get_device_plans(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDevicePlansResponse]:
        """
        Get Data Plans associated with the device, this include the primary sim, any external sim, as well as any satellite connections.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDevicePlansResponse]
            Response body for /plans
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/plans",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDevicePlansResponse,
                    parse_obj_as(
                        type_=GetDevicePlansResponse,
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

    async def provision_device(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        product_uid: str,
        device_sn: typing.Optional[str] = OMIT,
        fleet_uids: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Dict[str, typing.Any]]:
        """
        Provision Device for a Project

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        product_uid : str
            The ProductUID that the device should use.

        device_sn : typing.Optional[str]
            The serial number to assign to the device.

        fleet_uids : typing.Optional[typing.Sequence[str]]
            The fleetUIDs to provision the device to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Dict[str, typing.Any]]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/provision",
            method="POST",
            json={
                "device_sn": device_sn,
                "fleet_uids": fleet_uids,
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
                    typing.Dict[str, typing.Any],
                    parse_obj_as(
                        type_=typing.Dict[str, typing.Any],
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

    async def get_device_public_key(
        self, project_or_product_uid: str, device_uid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDevicePublicKeyResponse]:
        """
        Get Device Public Key

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDevicePublicKeyResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/public-key",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDevicePublicKeyResponse,
                    parse_obj_as(
                        type_=GetDevicePublicKeyResponse,
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

    async def get_device_sessions(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        start_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        first_sync: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDeviceSessionsResponse]:
        """
        Get Device Sessions

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        start_date : typing.Optional[int]
            Start date for filtering results, specified as a Unix timestamp

        end_date : typing.Optional[int]
            End date for filtering results, specified as a Unix timestamp

        first_sync : typing.Optional[bool]
            When true, filters results to only show first sync sessions

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDeviceSessionsResponse]
            The response body for a session request.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/sessions",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "startDate": start_date,
                "endDate": end_date,
                "firstSync": first_sync,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDeviceSessionsResponse,
                    parse_obj_as(
                        type_=GetDeviceSessionsResponse,
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

    async def signal_device(
        self,
        project_or_product_uid: str,
        device_uid: str,
        *,
        body: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SignalDeviceResponse]:
        """
        Send a signal from Notehub to a Notecard.

        Parameters
        ----------
        project_or_product_uid : str

        device_uid : str

        body : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SignalDeviceResponse]
            A status response.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/{encode_path_param(device_uid)}/signal",
            method="POST",
            json={
                "body": body,
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
                    SignalDeviceResponse,
                    parse_obj_as(
                        type_=SignalDeviceResponse,
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

    async def get_device_public_keys(
        self,
        project_or_product_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetDevicePublicKeysResponse]:
        """
        Get Device Public Keys of a Project

        Parameters
        ----------
        project_or_product_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDevicePublicKeysResponse]
            Successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/devices/public-keys",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDevicePublicKeysResponse,
                    parse_obj_as(
                        type_=GetDevicePublicKeysResponse,
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

    async def get_fleet_devices(
        self,
        project_or_product_uid: str,
        fleet_uid: str,
        *,
        page_size: typing.Optional[int] = None,
        page_num: typing.Optional[int] = None,
        device_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        serial_number: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        notecard_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        location: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        host_firmware: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        product_uid: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sku: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GetFleetDevicesResponse]:
        """
        Get Devices of a Fleet within a Project

        Parameters
        ----------
        project_or_product_uid : str

        fleet_uid : str

        page_size : typing.Optional[int]

        page_num : typing.Optional[int]

        device_uid : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A Device UID.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Tag filter

        serial_number : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Serial number filter

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
        AsyncHttpResponse[GetFleetDevicesResponse]
            List of Devices
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v1/projects/{encode_path_param(project_or_product_uid)}/fleets/{encode_path_param(fleet_uid)}/devices",
            method="GET",
            params={
                "pageSize": page_size,
                "pageNum": page_num,
                "deviceUID": device_uid,
                "tag": tag,
                "serialNumber": serial_number,
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
                    GetFleetDevicesResponse,
                    parse_obj_as(
                        type_=GetFleetDevicesResponse,
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
