

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.settings_response import SettingsResponse
from .types.settings_update_default_locale import SettingsUpdateDefaultLocale
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSettingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_settings(
        self,
        *,
        brand_color: typing.Optional[str] = OMIT,
        default_locale: typing.Optional[SettingsUpdateDefaultLocale] = OMIT,
        export_preset: typing.Optional[str] = OMIT,
        monthly_cap_usd: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SettingsResponse]:
        """
        Read-modify-write the 4 workspace-level options into config.yaml.

        Retries up to ``_MAX_CHECKSUM_RETRIES`` times if the config drifted
        underneath us (concurrent provider save).  Inode-changed is treated
        identically to checksum-mismatch.

        Parameters
        ----------
        brand_color : typing.Optional[str]

        default_locale : typing.Optional[SettingsUpdateDefaultLocale]

        export_preset : typing.Optional[str]

        monthly_cap_usd : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SettingsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/settings",
            method="POST",
            json={
                "brand_color": brand_color,
                "default_locale": default_locale,
                "export_preset": export_preset,
                "monthly_cap_usd": monthly_cap_usd,
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
                    SettingsResponse,
                    parse_obj_as(
                        type_=SettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawSettingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_settings(
        self,
        *,
        brand_color: typing.Optional[str] = OMIT,
        default_locale: typing.Optional[SettingsUpdateDefaultLocale] = OMIT,
        export_preset: typing.Optional[str] = OMIT,
        monthly_cap_usd: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SettingsResponse]:
        """
        Read-modify-write the 4 workspace-level options into config.yaml.

        Retries up to ``_MAX_CHECKSUM_RETRIES`` times if the config drifted
        underneath us (concurrent provider save).  Inode-changed is treated
        identically to checksum-mismatch.

        Parameters
        ----------
        brand_color : typing.Optional[str]

        default_locale : typing.Optional[SettingsUpdateDefaultLocale]

        export_preset : typing.Optional[str]

        monthly_cap_usd : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SettingsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/settings",
            method="POST",
            json={
                "brand_color": brand_color,
                "default_locale": default_locale,
                "export_preset": export_preset,
                "monthly_cap_usd": monthly_cap_usd,
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
                    SettingsResponse,
                    parse_obj_as(
                        type_=SettingsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
