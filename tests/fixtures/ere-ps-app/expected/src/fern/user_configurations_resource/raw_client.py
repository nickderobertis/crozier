

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserConfigurationsResourceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "config",
            method="GET",
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

    def put_config(
        self,
        *,
        erixa_hotfolder: typing.Optional[str] = OMIT,
        erixa_drugstore_email: typing.Optional[str] = OMIT,
        erixa_user_email: typing.Optional[str] = OMIT,
        erixa_user_password: typing.Optional[str] = OMIT,
        erixa_api_key: typing.Optional[str] = OMIT,
        extractor_template_profile: typing.Optional[str] = OMIT,
        connector_base_url: typing.Optional[str] = OMIT,
        connector_mandant_id: typing.Optional[str] = OMIT,
        connector_workplace_id: typing.Optional[str] = OMIT,
        connector_client_system_id: typing.Optional[str] = OMIT,
        connector_user_id: typing.Optional[str] = OMIT,
        connector_version: typing.Optional[str] = OMIT,
        connector_tv_mode: typing.Optional[str] = OMIT,
        connector_client_certificate: typing.Optional[str] = OMIT,
        connector_client_certificate_password: typing.Optional[str] = OMIT,
        connector_basic_auth_username: typing.Optional[str] = OMIT,
        connector_basic_auth_password: typing.Optional[str] = OMIT,
        kbv_pruefnummer: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        erixa_hotfolder : typing.Optional[str]

        erixa_drugstore_email : typing.Optional[str]

        erixa_user_email : typing.Optional[str]

        erixa_user_password : typing.Optional[str]

        erixa_api_key : typing.Optional[str]

        extractor_template_profile : typing.Optional[str]

        connector_base_url : typing.Optional[str]

        connector_mandant_id : typing.Optional[str]

        connector_workplace_id : typing.Optional[str]

        connector_client_system_id : typing.Optional[str]

        connector_user_id : typing.Optional[str]

        connector_version : typing.Optional[str]

        connector_tv_mode : typing.Optional[str]

        connector_client_certificate : typing.Optional[str]

        connector_client_certificate_password : typing.Optional[str]

        connector_basic_auth_username : typing.Optional[str]

        connector_basic_auth_password : typing.Optional[str]

        kbv_pruefnummer : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "config",
            method="PUT",
            json={
                "erixa.hotfolder": erixa_hotfolder,
                "erixa.drugstore.email": erixa_drugstore_email,
                "erixa.user.email": erixa_user_email,
                "erixa.user.password": erixa_user_password,
                "erixa.api.key": erixa_api_key,
                "extractor.template.profile": extractor_template_profile,
                "connector.base-url": connector_base_url,
                "connector.mandant-id": connector_mandant_id,
                "connector.workplace-id": connector_workplace_id,
                "connector.client-system-id": connector_client_system_id,
                "connector.user-id": connector_user_id,
                "connector.version": connector_version,
                "connector.tvMode": connector_tv_mode,
                "connector.client-certificate": connector_client_certificate,
                "connector.client-certificate-password": connector_client_certificate_password,
                "connector.basic-auth-username": connector_basic_auth_username,
                "connector.basic-auth-password": connector_basic_auth_password,
                "kbv.pruefnummer": kbv_pruefnummer,
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


class AsyncRawUserConfigurationsResourceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "config",
            method="GET",
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

    async def put_config(
        self,
        *,
        erixa_hotfolder: typing.Optional[str] = OMIT,
        erixa_drugstore_email: typing.Optional[str] = OMIT,
        erixa_user_email: typing.Optional[str] = OMIT,
        erixa_user_password: typing.Optional[str] = OMIT,
        erixa_api_key: typing.Optional[str] = OMIT,
        extractor_template_profile: typing.Optional[str] = OMIT,
        connector_base_url: typing.Optional[str] = OMIT,
        connector_mandant_id: typing.Optional[str] = OMIT,
        connector_workplace_id: typing.Optional[str] = OMIT,
        connector_client_system_id: typing.Optional[str] = OMIT,
        connector_user_id: typing.Optional[str] = OMIT,
        connector_version: typing.Optional[str] = OMIT,
        connector_tv_mode: typing.Optional[str] = OMIT,
        connector_client_certificate: typing.Optional[str] = OMIT,
        connector_client_certificate_password: typing.Optional[str] = OMIT,
        connector_basic_auth_username: typing.Optional[str] = OMIT,
        connector_basic_auth_password: typing.Optional[str] = OMIT,
        kbv_pruefnummer: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        erixa_hotfolder : typing.Optional[str]

        erixa_drugstore_email : typing.Optional[str]

        erixa_user_email : typing.Optional[str]

        erixa_user_password : typing.Optional[str]

        erixa_api_key : typing.Optional[str]

        extractor_template_profile : typing.Optional[str]

        connector_base_url : typing.Optional[str]

        connector_mandant_id : typing.Optional[str]

        connector_workplace_id : typing.Optional[str]

        connector_client_system_id : typing.Optional[str]

        connector_user_id : typing.Optional[str]

        connector_version : typing.Optional[str]

        connector_tv_mode : typing.Optional[str]

        connector_client_certificate : typing.Optional[str]

        connector_client_certificate_password : typing.Optional[str]

        connector_basic_auth_username : typing.Optional[str]

        connector_basic_auth_password : typing.Optional[str]

        kbv_pruefnummer : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "config",
            method="PUT",
            json={
                "erixa.hotfolder": erixa_hotfolder,
                "erixa.drugstore.email": erixa_drugstore_email,
                "erixa.user.email": erixa_user_email,
                "erixa.user.password": erixa_user_password,
                "erixa.api.key": erixa_api_key,
                "extractor.template.profile": extractor_template_profile,
                "connector.base-url": connector_base_url,
                "connector.mandant-id": connector_mandant_id,
                "connector.workplace-id": connector_workplace_id,
                "connector.client-system-id": connector_client_system_id,
                "connector.user-id": connector_user_id,
                "connector.version": connector_version,
                "connector.tvMode": connector_tv_mode,
                "connector.client-certificate": connector_client_certificate,
                "connector.client-certificate-password": connector_client_certificate_password,
                "connector.basic-auth-username": connector_basic_auth_username,
                "connector.basic-auth-password": connector_basic_auth_password,
                "kbv.pruefnummer": kbv_pruefnummer,
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
