

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.file_revision_metadata_v2 import FileRevisionMetadataV2
from pydantic import ValidationError


class RawFilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def query_val_file_by_id(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileRevisionMetadataV2]:
        """
        Get file metadata by file ID

        Parameters
        ----------
        file_id : str
            ID of a file in a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileRevisionMetadataV2]
            A File or Directory's Metadata
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v2/files/{encode_path_param(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileRevisionMetadataV2,
                    parse_obj_as(
                        type_=FileRevisionMetadataV2,
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


class AsyncRawFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def query_val_file_by_id(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileRevisionMetadataV2]:
        """
        Get file metadata by file ID

        Parameters
        ----------
        file_id : str
            ID of a file in a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileRevisionMetadataV2]
            A File or Directory's Metadata
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v2/files/{encode_path_param(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileRevisionMetadataV2,
                    parse_obj_as(
                        type_=FileRevisionMetadataV2,
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
