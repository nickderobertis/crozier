

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
from ..types.files_sharing_deleted_shareapi_list200response import FilesSharingDeletedShareapiList200Response
from pydantic import ValidationError


class RawFilesSharingDeletedShareapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FilesSharingDeletedShareapiList200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilesSharingDeletedShareapiList200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/deletedshares",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingDeletedShareapiList200Response,
                    parse_obj_as(
                        type_=FilesSharingDeletedShareapiList200Response,
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

    def undelete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        id : str
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CoreWhatsNewDismiss200Response]
            Share undeleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/deletedshares/{encode_path_param(id)}",
            method="POST",
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


class AsyncRawFilesSharingDeletedShareapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FilesSharingDeletedShareapiList200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilesSharingDeletedShareapiList200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/deletedshares",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingDeletedShareapiList200Response,
                    parse_obj_as(
                        type_=FilesSharingDeletedShareapiList200Response,
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

    async def undelete(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CoreWhatsNewDismiss200Response]:
        """
        Parameters
        ----------
        id : str
            ID of the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CoreWhatsNewDismiss200Response]
            Share undeleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/deletedshares/{encode_path_param(id)}",
            method="POST",
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
