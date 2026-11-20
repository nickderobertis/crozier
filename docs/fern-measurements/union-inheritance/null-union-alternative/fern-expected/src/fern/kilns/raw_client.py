

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.adjust_kiln_settings_request_changes_item import AdjustKilnSettingsRequestChangesItem
from .types.register_kiln_request_settings_value import RegisterKilnRequestSettingsValue
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawKilnsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def register_kiln(
        self,
        *,
        name: str,
        settings: typing.Optional[typing.Dict[str, RegisterKilnRequestSettingsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        name : str

        settings : typing.Optional[typing.Dict[str, RegisterKilnRequestSettingsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "kilns",
            method="POST",
            json={
                "name": name,
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=typing.Dict[str, RegisterKilnRequestSettingsValue], direction="write"
                ),
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

    def adjust_kiln_settings(
        self,
        kiln_id: str,
        *,
        changes: typing.Sequence[AdjustKilnSettingsRequestChangesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        kiln_id : str

        changes : typing.Sequence[AdjustKilnSettingsRequestChangesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"kilns/{encode_path_param(kiln_id)}/settings",
            method="PATCH",
            json={
                "changes": convert_and_respect_annotation_metadata(
                    object_=changes, annotation=typing.Sequence[AdjustKilnSettingsRequestChangesItem], direction="write"
                ),
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


class AsyncRawKilnsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def register_kiln(
        self,
        *,
        name: str,
        settings: typing.Optional[typing.Dict[str, RegisterKilnRequestSettingsValue]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        name : str

        settings : typing.Optional[typing.Dict[str, RegisterKilnRequestSettingsValue]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "kilns",
            method="POST",
            json={
                "name": name,
                "settings": convert_and_respect_annotation_metadata(
                    object_=settings, annotation=typing.Dict[str, RegisterKilnRequestSettingsValue], direction="write"
                ),
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

    async def adjust_kiln_settings(
        self,
        kiln_id: str,
        *,
        changes: typing.Sequence[AdjustKilnSettingsRequestChangesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        kiln_id : str

        changes : typing.Sequence[AdjustKilnSettingsRequestChangesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"kilns/{encode_path_param(kiln_id)}/settings",
            method="PATCH",
            json={
                "changes": convert_and_respect_annotation_metadata(
                    object_=changes, annotation=typing.Sequence[AdjustKilnSettingsRequestChangesItem], direction="write"
                ),
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
