

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.agco_power_services_models_ecu import AgcoPowerServicesModelsEcu
from ..types.agco_power_services_models_ecu_state import AgcoPowerServicesModelsEcuState
from ..types.agco_power_services_models_production_data import AgcoPowerServicesModelsProductionData
from ..types.agco_power_services_models_user_status import AgcoPowerServicesModelsUserStatus
from ..types.agco_power_services_models_user_status_state import AgcoPowerServicesModelsUserStatusState
from ..types.system_object import SystemObject
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAftermarketservicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def getcerts(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[SystemObject]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SystemObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/AftermarketServices/Certificates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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

    def putecu(
        self,
        serial_number_: str,
        *,
        edt_instance_id: str,
        engine_serial_number: str,
        serial_number: str,
        state: AgcoPowerServicesModelsEcuState,
        activation_code: typing.Optional[str] = OMIT,
        damaged_description: typing.Optional[str] = OMIT,
        replaces_ecu_serial_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AgcoPowerServicesModelsEcu]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number_ : str
            The serial number of the ECU.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        engine_serial_number : str
            The serial number of the ECU’s engine

        serial_number : str
            The serial number of the ECU

        state : AgcoPowerServicesModelsEcuState
            The state of the ECU

        activation_code : typing.Optional[str]
            The code used to activate the ECU. May not be modified. Returned only on activation.

        damaged_description : typing.Optional[str]
            A description why the ECU cannot be deactivated.

        replaces_ecu_serial_number : typing.Optional[str]
            The serial number of the ECU that this ECU replaces. Required if activating an ECU..

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgcoPowerServicesModelsEcu]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AftermarketServices/ECUs/{encode_path_param(serial_number_)}",
            method="PUT",
            params={
                "EDTInstanceId": edt_instance_id,
            },
            json={
                "ActivationCode": activation_code,
                "DamagedDescription": damaged_description,
                "EngineSerialNumber": engine_serial_number,
                "ReplacesECUSerialNumber": replaces_ecu_serial_number,
                "SerialNumber": serial_number,
                "State": state,
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
                    AgcoPowerServicesModelsEcu,
                    parse_obj_as(
                        type_=AgcoPowerServicesModelsEcu,
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

    def getengineiqacodes(
        self, serial_number: str, *, edt_instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[str]]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the engine.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[str]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AftermarketServices/Engines/{encode_path_param(serial_number)}/IQACodes",
            method="GET",
            params={
                "EDTInstanceId": edt_instance_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    def putiqacodes(
        self,
        serial_number: str,
        *,
        edt_instance_id: str,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the Engine

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AftermarketServices/Engines/{encode_path_param(serial_number)}/IQACodes",
            method="PUT",
            params={
                "EDTInstanceId": edt_instance_id,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
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

    def getproductiondata(
        self, serial_number: str, *, edt_instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[AgcoPowerServicesModelsProductionData]]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the engine.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[AgcoPowerServicesModelsProductionData]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/AftermarketServices/Engines/{encode_path_param(serial_number)}/ProductionData",
            method="GET",
            params={
                "EDTInstanceId": edt_instance_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgcoPowerServicesModelsProductionData],
                    parse_obj_as(
                        type_=typing.List[AgcoPowerServicesModelsProductionData],
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

    def getconnectionstatus(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[bool]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/AftermarketServices/Hello",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
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

    def getuserstatus(
        self, *, voucher_code: str, dealer_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AgcoPowerServicesModelsUserStatus]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str

        dealer_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AgcoPowerServicesModelsUserStatus]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/AftermarketServices/UserStatuses",
            method="GET",
            params={
                "voucherCode": voucher_code,
                "dealerCode": dealer_code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgcoPowerServicesModelsUserStatus,
                    parse_obj_as(
                        type_=AgcoPowerServicesModelsUserStatus,
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

    def updateuserstatus(
        self,
        *,
        dealer_code: str,
        voucher_code: str,
        state: typing.Optional[AgcoPowerServicesModelsUserStatusState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The dealer code of the voucher

        voucher_code : str
            The voucher code

        state : typing.Optional[AgcoPowerServicesModelsUserStatusState]
            The state of the voucher

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/AftermarketServices/UserStatuses",
            method="PUT",
            json={
                "DealerCode": dealer_code,
                "State": state,
                "VoucherCode": voucher_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
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


class AsyncRawAftermarketservicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def getcerts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SystemObject]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SystemObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/AftermarketServices/Certificates",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SystemObject,
                    parse_obj_as(
                        type_=SystemObject,
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

    async def putecu(
        self,
        serial_number_: str,
        *,
        edt_instance_id: str,
        engine_serial_number: str,
        serial_number: str,
        state: AgcoPowerServicesModelsEcuState,
        activation_code: typing.Optional[str] = OMIT,
        damaged_description: typing.Optional[str] = OMIT,
        replaces_ecu_serial_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AgcoPowerServicesModelsEcu]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number_ : str
            The serial number of the ECU.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        engine_serial_number : str
            The serial number of the ECU’s engine

        serial_number : str
            The serial number of the ECU

        state : AgcoPowerServicesModelsEcuState
            The state of the ECU

        activation_code : typing.Optional[str]
            The code used to activate the ECU. May not be modified. Returned only on activation.

        damaged_description : typing.Optional[str]
            A description why the ECU cannot be deactivated.

        replaces_ecu_serial_number : typing.Optional[str]
            The serial number of the ECU that this ECU replaces. Required if activating an ECU..

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgcoPowerServicesModelsEcu]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AftermarketServices/ECUs/{encode_path_param(serial_number_)}",
            method="PUT",
            params={
                "EDTInstanceId": edt_instance_id,
            },
            json={
                "ActivationCode": activation_code,
                "DamagedDescription": damaged_description,
                "EngineSerialNumber": engine_serial_number,
                "ReplacesECUSerialNumber": replaces_ecu_serial_number,
                "SerialNumber": serial_number,
                "State": state,
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
                    AgcoPowerServicesModelsEcu,
                    parse_obj_as(
                        type_=AgcoPowerServicesModelsEcu,
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

    async def getengineiqacodes(
        self, serial_number: str, *, edt_instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[str]]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the engine.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[str]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AftermarketServices/Engines/{encode_path_param(serial_number)}/IQACodes",
            method="GET",
            params={
                "EDTInstanceId": edt_instance_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[str],
                    parse_obj_as(
                        type_=typing.List[str],
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

    async def putiqacodes(
        self,
        serial_number: str,
        *,
        edt_instance_id: str,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the Engine

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AftermarketServices/Engines/{encode_path_param(serial_number)}/IQACodes",
            method="PUT",
            params={
                "EDTInstanceId": edt_instance_id,
            },
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
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

    async def getproductiondata(
        self, serial_number: str, *, edt_instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[AgcoPowerServicesModelsProductionData]]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the engine.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[AgcoPowerServicesModelsProductionData]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/AftermarketServices/Engines/{encode_path_param(serial_number)}/ProductionData",
            method="GET",
            params={
                "EDTInstanceId": edt_instance_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[AgcoPowerServicesModelsProductionData],
                    parse_obj_as(
                        type_=typing.List[AgcoPowerServicesModelsProductionData],
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

    async def getconnectionstatus(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[bool]:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/AftermarketServices/Hello",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
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

    async def getuserstatus(
        self, *, voucher_code: str, dealer_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AgcoPowerServicesModelsUserStatus]:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str

        dealer_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AgcoPowerServicesModelsUserStatus]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/AftermarketServices/UserStatuses",
            method="GET",
            params={
                "voucherCode": voucher_code,
                "dealerCode": dealer_code,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AgcoPowerServicesModelsUserStatus,
                    parse_obj_as(
                        type_=AgcoPowerServicesModelsUserStatus,
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

    async def updateuserstatus(
        self,
        *,
        dealer_code: str,
        voucher_code: str,
        state: typing.Optional[AgcoPowerServicesModelsUserStatusState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The dealer code of the voucher

        voucher_code : str
            The voucher code

        state : typing.Optional[AgcoPowerServicesModelsUserStatusState]
            The state of the voucher

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/AftermarketServices/UserStatuses",
            method="PUT",
            json={
                "DealerCode": dealer_code,
                "State": state,
                "VoucherCode": voucher_code,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    bool,
                    parse_obj_as(
                        type_=bool,
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
