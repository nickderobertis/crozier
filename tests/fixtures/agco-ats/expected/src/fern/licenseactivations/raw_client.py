

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
from ..types.dealer_db_models_license_activation import DealerDbModelsLicenseActivation
from .types.dealer_db_models_license_activation_create_license_activation_type import (
    DealerDbModelsLicenseActivationCreateLicenseActivationType,
)
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawLicenseactivationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post(
        self,
        *,
        dealer_code: str,
        postal_code: str,
        system_info: str,
        voucher_code: str,
        license_activation_type: typing.Optional[DealerDbModelsLicenseActivationCreateLicenseActivationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DealerDbModelsLicenseActivation]:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The Dealer Code of the dealer activating the license

        postal_code : str
            The dealer's postal code (zip code)

        system_info : str
            Information about  the system being activated

        voucher_code : str
            The Voucher Code to use for activation

        license_activation_type : typing.Optional[DealerDbModelsLicenseActivationCreateLicenseActivationType]
            The type of license to create (e.g. EDT, EDT Lite)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DealerDbModelsLicenseActivation]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/LicenseActivations",
            method="POST",
            json={
                "DealerCode": dealer_code,
                "LicenseActivationType": license_activation_type,
                "PostalCode": postal_code,
                "SystemInfo": system_info,
                "VoucherCode": voucher_code,
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
                    DealerDbModelsLicenseActivation,
                    parse_obj_as(
                        type_=DealerDbModelsLicenseActivation,
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

    def postregisteredtlite(
        self,
        *,
        expiration_date: dt.datetime,
        instance_id: str,
        voucher_code: str,
        dealer_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[bool]:
        """
        No Documentation Found.

        Parameters
        ----------
        expiration_date : dt.datetime
            The date at which the content of the EDT Lite expires.

        instance_id : str
            The identifier for the EDT Lite.

        voucher_code : str
            The voucher code with which the EDT Lite was created.

        dealer_code : typing.Optional[str]
            The dealer code with which the EDT Lite was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[bool]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v2/LicenseActivations/RegisterEDTLite",
            method="POST",
            json={
                "DealerCode": dealer_code,
                "ExpirationDate": expiration_date,
                "InstanceID": instance_id,
                "VoucherCode": voucher_code,
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

    def put(
        self,
        id: str,
        *,
        license_version: str,
        system_info: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DealerDbModelsLicenseActivation]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license.

        license_version : str
            The license version to update

        system_info : typing.Optional[str]
            Information about  the system being activated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DealerDbModelsLicenseActivation]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/LicenseActivations/{encode_path_param(id)}",
            method="PUT",
            json={
                "LicenseVersion": license_version,
                "SystemInfo": system_info,
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
                    DealerDbModelsLicenseActivation,
                    parse_obj_as(
                        type_=DealerDbModelsLicenseActivation,
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

    def putconfirm(
        self, id: str, *, license_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license

        license_version : str
            The license version to confirm

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/v2/LicenseActivations/{encode_path_param(id)}/Confirm",
            method="PUT",
            json={
                "LicenseVersion": license_version,
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


class AsyncRawLicenseactivationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post(
        self,
        *,
        dealer_code: str,
        postal_code: str,
        system_info: str,
        voucher_code: str,
        license_activation_type: typing.Optional[DealerDbModelsLicenseActivationCreateLicenseActivationType] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DealerDbModelsLicenseActivation]:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The Dealer Code of the dealer activating the license

        postal_code : str
            The dealer's postal code (zip code)

        system_info : str
            Information about  the system being activated

        voucher_code : str
            The Voucher Code to use for activation

        license_activation_type : typing.Optional[DealerDbModelsLicenseActivationCreateLicenseActivationType]
            The type of license to create (e.g. EDT, EDT Lite)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DealerDbModelsLicenseActivation]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/LicenseActivations",
            method="POST",
            json={
                "DealerCode": dealer_code,
                "LicenseActivationType": license_activation_type,
                "PostalCode": postal_code,
                "SystemInfo": system_info,
                "VoucherCode": voucher_code,
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
                    DealerDbModelsLicenseActivation,
                    parse_obj_as(
                        type_=DealerDbModelsLicenseActivation,
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

    async def postregisteredtlite(
        self,
        *,
        expiration_date: dt.datetime,
        instance_id: str,
        voucher_code: str,
        dealer_code: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[bool]:
        """
        No Documentation Found.

        Parameters
        ----------
        expiration_date : dt.datetime
            The date at which the content of the EDT Lite expires.

        instance_id : str
            The identifier for the EDT Lite.

        voucher_code : str
            The voucher code with which the EDT Lite was created.

        dealer_code : typing.Optional[str]
            The dealer code with which the EDT Lite was created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[bool]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v2/LicenseActivations/RegisterEDTLite",
            method="POST",
            json={
                "DealerCode": dealer_code,
                "ExpirationDate": expiration_date,
                "InstanceID": instance_id,
                "VoucherCode": voucher_code,
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

    async def put(
        self,
        id: str,
        *,
        license_version: str,
        system_info: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DealerDbModelsLicenseActivation]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license.

        license_version : str
            The license version to update

        system_info : typing.Optional[str]
            Information about  the system being activated

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DealerDbModelsLicenseActivation]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/LicenseActivations/{encode_path_param(id)}",
            method="PUT",
            json={
                "LicenseVersion": license_version,
                "SystemInfo": system_info,
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
                    DealerDbModelsLicenseActivation,
                    parse_obj_as(
                        type_=DealerDbModelsLicenseActivation,
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

    async def putconfirm(
        self, id: str, *, license_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        No Documentation Found.

        Parameters
        ----------
        id : str
            The ID of the license

        license_version : str
            The license version to confirm

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/v2/LicenseActivations/{encode_path_param(id)}/Confirm",
            method="PUT",
            json={
                "LicenseVersion": license_version,
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
