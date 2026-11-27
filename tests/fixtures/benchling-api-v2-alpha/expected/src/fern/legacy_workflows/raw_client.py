

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..types.entry_external_file_by_id import EntryExternalFileById
from ..types.stage_entry import StageEntry
from pydantic import ValidationError


class RawLegacyWorkflowsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_stage_entry(
        self, stage_entry_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[StageEntry]:
        """
        Get a stage entry by ID

        Parameters
        ----------
        stage_entry_id : str
            ID of the stage entry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[StageEntry]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"stage-entries/{encode_path_param(stage_entry_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageEntry,
                    parse_obj_as(
                        type_=StageEntry,
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

    def get_external_file_metadata(
        self, stage_entry_id: str, external_file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EntryExternalFileById]:
        """
        Retrieves the metadata for an external file. Use the 'downloadURL' to download the actual file. (Expand the schema view for details)

        Parameters
        ----------
        stage_entry_id : str
            ID of the legacy workflow stage entry the file was uploaded to

        external_file_id : str
            ID of the external file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EntryExternalFileById]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"stage-entries/{encode_path_param(stage_entry_id)}/external-files/{encode_path_param(external_file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntryExternalFileById,
                    parse_obj_as(
                        type_=EntryExternalFileById,
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


class AsyncRawLegacyWorkflowsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_stage_entry(
        self, stage_entry_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[StageEntry]:
        """
        Get a stage entry by ID

        Parameters
        ----------
        stage_entry_id : str
            ID of the stage entry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[StageEntry]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"stage-entries/{encode_path_param(stage_entry_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    StageEntry,
                    parse_obj_as(
                        type_=StageEntry,
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

    async def get_external_file_metadata(
        self, stage_entry_id: str, external_file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EntryExternalFileById]:
        """
        Retrieves the metadata for an external file. Use the 'downloadURL' to download the actual file. (Expand the schema view for details)

        Parameters
        ----------
        stage_entry_id : str
            ID of the legacy workflow stage entry the file was uploaded to

        external_file_id : str
            ID of the external file

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EntryExternalFileById]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"stage-entries/{encode_path_param(stage_entry_id)}/external-files/{encode_path_param(external_file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EntryExternalFileById,
                    parse_obj_as(
                        type_=EntryExternalFileById,
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
