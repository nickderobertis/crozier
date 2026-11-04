

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.core_whats_new_dismiss200response import CoreWhatsNewDismiss200Response
from ..types.provisioning_api_app_config_get_apps200response import ProvisioningApiAppConfigGetApps200Response
from ..types.provisioning_api_app_config_get_value200response import ProvisioningApiAppConfigGetValue200Response
from pydantic import ValidationError


class RawProvisioningApiAppConfigClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_apps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiAppConfigGetApps200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiAppConfigGetApps200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/provisioning_api/api/v1/config/apps",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiAppConfigGetApps200Response,
                    parse_obj_as(
                        type_=ProvisioningApiAppConfigGetApps200Response,
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

    def get_keys(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProvisioningApiAppConfigGetApps200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiAppConfigGetApps200Response]
            Keys returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/provisioning_api/api/v1/config/apps/{encode_path_param(app)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiAppConfigGetApps200Response,
                    parse_obj_as(
                        type_=ProvisioningApiAppConfigGetApps200Response,
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

    def get_value(
        self,
        app: str,
        key: str,
        *,
        default_value: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProvisioningApiAppConfigGetValue200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID if the app

        key : str
            Key

        default_value : typing.Optional[str]
            Default returned value if the value is empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProvisioningApiAppConfigGetValue200Response]
            Value returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/provisioning_api/api/v1/config/apps/{encode_path_param(app)}/{encode_path_param(key)}",
            method="GET",
            params={
                "defaultValue": default_value,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiAppConfigGetValue200Response,
                    parse_obj_as(
                        type_=ProvisioningApiAppConfigGetValue200Response,
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

    def set_value(
        self, app: str, key: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        app : str
            ID of the app

        key : str
            Key to update

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]
            Value updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/provisioning_api/api/v1/config/apps/{encode_path_param(app)}/{encode_path_param(key)}",
            method="POST",
            params={
                "value": value,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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

    def delete_key(
        self, app: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        key : str
            Key to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]
            Key deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/provisioning_api/api/v1/config/apps/{encode_path_param(app)}/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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


class AsyncRawProvisioningApiAppConfigClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_apps(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiAppConfigGetApps200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiAppConfigGetApps200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/provisioning_api/api/v1/config/apps",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiAppConfigGetApps200Response,
                    parse_obj_as(
                        type_=ProvisioningApiAppConfigGetApps200Response,
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

    async def get_keys(
        self, app: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProvisioningApiAppConfigGetApps200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiAppConfigGetApps200Response]
            Keys returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/provisioning_api/api/v1/config/apps/{encode_path_param(app)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiAppConfigGetApps200Response,
                    parse_obj_as(
                        type_=ProvisioningApiAppConfigGetApps200Response,
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

    async def get_value(
        self,
        app: str,
        key: str,
        *,
        default_value: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProvisioningApiAppConfigGetValue200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID if the app

        key : str
            Key

        default_value : typing.Optional[str]
            Default returned value if the value is empty

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProvisioningApiAppConfigGetValue200Response]
            Value returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/provisioning_api/api/v1/config/apps/{encode_path_param(app)}/{encode_path_param(key)}",
            method="GET",
            params={
                "defaultValue": default_value,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProvisioningApiAppConfigGetValue200Response,
                    parse_obj_as(
                        type_=ProvisioningApiAppConfigGetValue200Response,
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

    async def set_value(
        self, app: str, key: str, *, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        app : str
            ID of the app

        key : str
            Key to update

        value : str
            New value for the key

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]
            Value updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/provisioning_api/api/v1/config/apps/{encode_path_param(app)}/{encode_path_param(key)}",
            method="POST",
            params={
                "value": value,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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

    async def delete_key(
        self, app: str, key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        This endpoint requires admin access

        Parameters
        ----------
        app : str
            ID of the app

        key : str
            Key to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]
            Key deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/provisioning_api/api/v1/config/apps/{encode_path_param(app)}/{encode_path_param(key)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CoreWhatsNewDismiss200Response,
                    parse_obj_as(
                        type_=CoreWhatsNewDismiss200Response,
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
