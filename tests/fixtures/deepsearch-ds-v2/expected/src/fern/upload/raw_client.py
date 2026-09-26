

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.project_scratch_files import ProjectScratchFiles
from ..types.project_scratch_files_paginated import ProjectScratchFilesPaginated
from ..types.temporary_upload_file_result import TemporaryUploadFileResult
from pydantic import ValidationError


class RawUploadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_project_scratch_files(
        self,
        proj_key: str,
        *,
        scratch_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ProjectScratchFiles]]:
        """
        Get temporary files uploaded to a project.

        Parameters
        ----------
        proj_key : str

        scratch_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ProjectScratchFiles]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/scratch/files",
            method="GET",
            params={
                "scratch_ids": scratch_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProjectScratchFiles],
                    parse_obj_as(
                        type_=typing.List[ProjectScratchFiles],
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

    def list_project_scratch_files_paginated(
        self,
        proj_key: str,
        *,
        page: typing.Optional[int] = None,
        items_per_page: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        begin_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectScratchFilesPaginated]:
        """
        Get paginated list of temporary files uploaded to a project.

        Parameters
        ----------
        proj_key : str

        page : typing.Optional[int]

        items_per_page : typing.Optional[int]

        search_string : typing.Optional[str]

        begin_date : typing.Optional[int]

        end_date : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectScratchFilesPaginated]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/scratch/files_paginated",
            method="GET",
            params={
                "page": page,
                "items_per_page": items_per_page,
                "search_string": search_string,
                "begin_date": begin_date,
                "end_date": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectScratchFilesPaginated,
                    parse_obj_as(
                        type_=ProjectScratchFilesPaginated,
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

    def create_project_scratch_file(
        self, proj_key: str, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TemporaryUploadFileResult]:
        """
        Create file pointers for temporary storage.

        Parameters
        ----------
        proj_key : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TemporaryUploadFileResult]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/scratch/files/upload/{encode_path_param(filename)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TemporaryUploadFileResult,
                    parse_obj_as(
                        type_=TemporaryUploadFileResult,
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


class AsyncRawUploadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_project_scratch_files(
        self,
        proj_key: str,
        *,
        scratch_ids: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ProjectScratchFiles]]:
        """
        Get temporary files uploaded to a project.

        Parameters
        ----------
        proj_key : str

        scratch_ids : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ProjectScratchFiles]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/scratch/files",
            method="GET",
            params={
                "scratch_ids": scratch_ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProjectScratchFiles],
                    parse_obj_as(
                        type_=typing.List[ProjectScratchFiles],
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

    async def list_project_scratch_files_paginated(
        self,
        proj_key: str,
        *,
        page: typing.Optional[int] = None,
        items_per_page: typing.Optional[int] = None,
        search_string: typing.Optional[str] = None,
        begin_date: typing.Optional[int] = None,
        end_date: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectScratchFilesPaginated]:
        """
        Get paginated list of temporary files uploaded to a project.

        Parameters
        ----------
        proj_key : str

        page : typing.Optional[int]

        items_per_page : typing.Optional[int]

        search_string : typing.Optional[str]

        begin_date : typing.Optional[int]

        end_date : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectScratchFilesPaginated]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/scratch/files_paginated",
            method="GET",
            params={
                "page": page,
                "items_per_page": items_per_page,
                "search_string": search_string,
                "begin_date": begin_date,
                "end_date": end_date,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectScratchFilesPaginated,
                    parse_obj_as(
                        type_=ProjectScratchFilesPaginated,
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

    async def create_project_scratch_file(
        self, proj_key: str, filename: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TemporaryUploadFileResult]:
        """
        Create file pointers for temporary storage.

        Parameters
        ----------
        proj_key : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TemporaryUploadFileResult]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/scratch/files/upload/{encode_path_param(filename)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TemporaryUploadFileResult,
                    parse_obj_as(
                        type_=TemporaryUploadFileResult,
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
