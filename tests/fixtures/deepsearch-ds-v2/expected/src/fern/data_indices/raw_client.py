

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.ocr_options import OcrOptions
from ..types.project_data_index_conversion_settings_output import ProjectDataIndexConversionSettingsOutput
from ..types.project_data_index_with_status import ProjectDataIndexWithStatus
from ..types.table_structure_options import TableStructureOptions
from ..types.token_response import TokenResponse
from .types.create_project_data_index_request_body import CreateProjectDataIndexRequestBody
from .types.update_project_data_index_request_body import UpdateProjectDataIndexRequestBody
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDataIndicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_project_data_indices(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ProjectDataIndexWithStatus]]:
        """
        Get project data indices.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ProjectDataIndexWithStatus]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProjectDataIndexWithStatus],
                    parse_obj_as(
                        type_=typing.List[ProjectDataIndexWithStatus],
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

    def create_project_data_index(
        self,
        proj_key: str,
        *,
        request: CreateProjectDataIndexRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectDataIndexWithStatus]:
        """
        Create a project data index.

        Parameters
        ----------
        proj_key : str

        request : CreateProjectDataIndexRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDataIndexWithStatus]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateProjectDataIndexRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDataIndexWithStatus,
                    parse_obj_as(
                        type_=ProjectDataIndexWithStatus,
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

    def get_project_data_index(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProjectDataIndexWithStatus]:
        """
        Get project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDataIndexWithStatus]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDataIndexWithStatus,
                    parse_obj_as(
                        type_=ProjectDataIndexWithStatus,
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

    def delete_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        confirmation_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Any]:
        """
        Delete a project index data.

        Parameters
        ----------
        proj_key : str

        index_key : str

        confirmation_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}",
            method="DELETE",
            params={
                "confirmation_token": confirmation_token,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    def update_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        request: UpdateProjectDataIndexRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ProjectDataIndexWithStatus]:
        """
        Update a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request : UpdateProjectDataIndexRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProjectDataIndexWithStatus]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateProjectDataIndexRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDataIndexWithStatus,
                    parse_obj_as(
                        type_=ProjectDataIndexWithStatus,
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

    def create_project_data_index_delete_token(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[TokenResponse]:
        """
        Get a token used to confirm the deletion of a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TokenResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/delete_token",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokenResponse,
                    parse_obj_as(
                        type_=TokenResponse,
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

    def get_project_data_index_conversion_settings(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Optional[ProjectDataIndexConversionSettingsOutput]]:
        """
        Get project data index conversion settings.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[ProjectDataIndexConversionSettingsOutput]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/conversion_settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProjectDataIndexConversionSettingsOutput],
                    parse_obj_as(
                        type_=typing.Optional[ProjectDataIndexConversionSettingsOutput],
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

    def update_project_data_index_conversion_settings(
        self,
        proj_key: str,
        index_key: str,
        *,
        ocr: typing.Optional[OcrOptions] = OMIT,
        table_structure: typing.Optional[TableStructureOptions] = OMIT,
        generate_page_images: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.Optional[ProjectDataIndexConversionSettingsOutput]]:
        """
        Update a project data index conversion settings.

        Parameters
        ----------
        proj_key : str

        index_key : str

        ocr : typing.Optional[OcrOptions]

        table_structure : typing.Optional[TableStructureOptions]

        generate_page_images : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Optional[ProjectDataIndexConversionSettingsOutput]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/conversion_settings",
            method="PATCH",
            json={
                "ocr": convert_and_respect_annotation_metadata(object_=ocr, annotation=OcrOptions, direction="write"),
                "table_structure": convert_and_respect_annotation_metadata(
                    object_=table_structure, annotation=TableStructureOptions, direction="write"
                ),
                "generate_page_images": generate_page_images,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return HttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProjectDataIndexConversionSettingsOutput],
                    parse_obj_as(
                        type_=typing.Optional[ProjectDataIndexConversionSettingsOutput],
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


class AsyncRawDataIndicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_project_data_indices(
        self, proj_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ProjectDataIndexWithStatus]]:
        """
        Get project data indices.

        Parameters
        ----------
        proj_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ProjectDataIndexWithStatus]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ProjectDataIndexWithStatus],
                    parse_obj_as(
                        type_=typing.List[ProjectDataIndexWithStatus],
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

    async def create_project_data_index(
        self,
        proj_key: str,
        *,
        request: CreateProjectDataIndexRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectDataIndexWithStatus]:
        """
        Create a project data index.

        Parameters
        ----------
        proj_key : str

        request : CreateProjectDataIndexRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDataIndexWithStatus]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=CreateProjectDataIndexRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDataIndexWithStatus,
                    parse_obj_as(
                        type_=ProjectDataIndexWithStatus,
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

    async def get_project_data_index(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProjectDataIndexWithStatus]:
        """
        Get project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDataIndexWithStatus]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDataIndexWithStatus,
                    parse_obj_as(
                        type_=ProjectDataIndexWithStatus,
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

    async def delete_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        confirmation_token: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Delete a project index data.

        Parameters
        ----------
        proj_key : str

        index_key : str

        confirmation_token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}",
            method="DELETE",
            params={
                "confirmation_token": confirmation_token,
            },
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Any,
                    parse_obj_as(
                        type_=typing.Any,
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

    async def update_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        request: UpdateProjectDataIndexRequestBody,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ProjectDataIndexWithStatus]:
        """
        Update a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request : UpdateProjectDataIndexRequestBody

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProjectDataIndexWithStatus]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}",
            method="PATCH",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=UpdateProjectDataIndexRequestBody, direction="write"
            ),
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProjectDataIndexWithStatus,
                    parse_obj_as(
                        type_=ProjectDataIndexWithStatus,
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

    async def create_project_data_index_delete_token(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[TokenResponse]:
        """
        Get a token used to confirm the deletion of a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TokenResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/delete_token",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TokenResponse,
                    parse_obj_as(
                        type_=TokenResponse,
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

    async def get_project_data_index_conversion_settings(
        self, proj_key: str, index_key: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Optional[ProjectDataIndexConversionSettingsOutput]]:
        """
        Get project data index conversion settings.

        Parameters
        ----------
        proj_key : str

        index_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[ProjectDataIndexConversionSettingsOutput]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/conversion_settings",
            method="GET",
            request_options=request_options,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProjectDataIndexConversionSettingsOutput],
                    parse_obj_as(
                        type_=typing.Optional[ProjectDataIndexConversionSettingsOutput],
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

    async def update_project_data_index_conversion_settings(
        self,
        proj_key: str,
        index_key: str,
        *,
        ocr: typing.Optional[OcrOptions] = OMIT,
        table_structure: typing.Optional[TableStructureOptions] = OMIT,
        generate_page_images: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.Optional[ProjectDataIndexConversionSettingsOutput]]:
        """
        Update a project data index conversion settings.

        Parameters
        ----------
        proj_key : str

        index_key : str

        ocr : typing.Optional[OcrOptions]

        table_structure : typing.Optional[TableStructureOptions]

        generate_page_images : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Optional[ProjectDataIndexConversionSettingsOutput]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/conversion_settings",
            method="PATCH",
            json={
                "ocr": convert_and_respect_annotation_metadata(object_=ocr, annotation=OcrOptions, direction="write"),
                "table_structure": convert_and_respect_annotation_metadata(
                    object_=table_structure, annotation=TableStructureOptions, direction="write"
                ),
                "generate_page_images": generate_page_images,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if _response is None or not _response.text.strip():
                return AsyncHttpResponse(response=_response, data=None)
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.Optional[ProjectDataIndexConversionSettingsOutput],
                    parse_obj_as(
                        type_=typing.Optional[ProjectDataIndexConversionSettingsOutput],
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
