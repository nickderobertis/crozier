

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
from ..types.edit_accepted import EditAccepted
from ..types.edit_result_out import EditResultOut
from ..types.editor_project_response import EditorProjectResponse
from ..types.http_validation_error import HttpValidationError
from ..types.ocr_response import OcrResponse
from ..types.save_image_response import SaveImageResponse
from .types.save_image_request_mode import SaveImageRequestMode
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEditorClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_image_bytes(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/bytes",
            method="GET",
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

    def start_edit(
        self,
        image_id: str,
        *,
        mask_box: typing.Dict[str, int],
        new_text: str,
        kit_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EditAccepted]:
        """
        Parameters
        ----------
        image_id : str

        mask_box : typing.Dict[str, int]
            x,y,w,h

        new_text : str

        kit_id : typing.Optional[str]
            Optional kit id for local edit context; safe-character allowlist keeps sidecar references portable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EditAccepted]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/edit",
            method="POST",
            json={
                "kit_id": kit_id,
                "mask_box": mask_box,
                "new_text": new_text,
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
                    EditAccepted,
                    parse_obj_as(
                        type_=EditAccepted,
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

    def create_edit_result(
        self,
        image_id: str,
        *,
        result_data_url: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EditResultOut]:
        """
        Parameters
        ----------
        image_id : str

        result_data_url : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        source_image_ref : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EditResultOut]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/edit-results",
            method="POST",
            json={
                "metadata": metadata,
                "result_data_url": result_data_url,
                "source_image_ref": source_image_ref,
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
                    EditResultOut,
                    parse_obj_as(
                        type_=EditResultOut,
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

    def get_edit_result_image(
        self, image_id: str, edit_result_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        image_id : str

        edit_result_ref : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/edit-results/{encode_path_param(edit_result_ref)}/image",
            method="GET",
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

    def edit_events(
        self, image_id: str, *, job_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Parameters
        ----------
        image_id : str

        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/edit/events",
            method="GET",
            params={
                "job_id": job_id,
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

    def ocr_image(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OcrResponse]:
        """
        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OcrResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/ocr",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcrResponse,
                    parse_obj_as(
                        type_=OcrResponse,
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

    def get_editor_project(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EditorProjectResponse]:
        """
        Return the saved Viskit editor project JSON for a canonical image id.

        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EditorProjectResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/project",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EditorProjectResponse,
                    parse_obj_as(
                        type_=EditorProjectResponse,
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

    def put_editor_project(
        self,
        image_id: str,
        *,
        document: typing.Dict[str, typing.Any],
        expected_revision: typing.Optional[int] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EditorProjectResponse]:
        """
        Create or replace the persisted project JSON for a canonical image id.

        Parameters
        ----------
        image_id : str

        document : typing.Dict[str, typing.Any]
            Versioned ViskitEditorDocument JSON object

        expected_revision : typing.Optional[int]
            Optimistic concurrency guard; 409 when it differs from stored revision.

        source_image_ref : typing.Optional[str]
            Optional source_images.id backing this project import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EditorProjectResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/project",
            method="PUT",
            json={
                "document": document,
                "expected_revision": expected_revision,
                "source_image_ref": source_image_ref,
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
                    EditorProjectResponse,
                    parse_obj_as(
                        type_=EditorProjectResponse,
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

    def export_editor_project(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.Any]:
        """
        Download the saved editor project as project JSON.

        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.Any]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/project/export",
            method="GET",
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

    def import_editor_project(
        self,
        image_id: str,
        *,
        document: typing.Dict[str, typing.Any],
        expected_revision: typing.Optional[int] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EditorProjectResponse]:
        """
        Import project JSON into the persisted editor state for this image.

        Parameters
        ----------
        image_id : str

        document : typing.Dict[str, typing.Any]
            Versioned ViskitEditorDocument JSON object

        expected_revision : typing.Optional[int]
            Optimistic concurrency guard; 409 when it differs from stored revision.

        source_image_ref : typing.Optional[str]
            Optional source_images.id backing this project import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EditorProjectResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/project/import",
            method="POST",
            json={
                "document": document,
                "expected_revision": expected_revision,
                "source_image_ref": source_image_ref,
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
                    EditorProjectResponse,
                    parse_obj_as(
                        type_=EditorProjectResponse,
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

    def save_edited_image(
        self,
        image_id: str,
        *,
        edit_result_ref: str,
        mode: SaveImageRequestMode,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SaveImageResponse]:
        """
        Persist an edit result via an explicit replace-or-copy choice.

        Parameters
        ----------
        image_id : str

        edit_result_ref : str

        mode : SaveImageRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SaveImageResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/save",
            method="POST",
            json={
                "edit_result_ref": edit_result_ref,
                "mode": mode,
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
                    SaveImageResponse,
                    parse_obj_as(
                        type_=SaveImageResponse,
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


class AsyncRawEditorClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_image_bytes(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/bytes",
            method="GET",
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

    async def start_edit(
        self,
        image_id: str,
        *,
        mask_box: typing.Dict[str, int],
        new_text: str,
        kit_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EditAccepted]:
        """
        Parameters
        ----------
        image_id : str

        mask_box : typing.Dict[str, int]
            x,y,w,h

        new_text : str

        kit_id : typing.Optional[str]
            Optional kit id for local edit context; safe-character allowlist keeps sidecar references portable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EditAccepted]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/edit",
            method="POST",
            json={
                "kit_id": kit_id,
                "mask_box": mask_box,
                "new_text": new_text,
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
                    EditAccepted,
                    parse_obj_as(
                        type_=EditAccepted,
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

    async def create_edit_result(
        self,
        image_id: str,
        *,
        result_data_url: str,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EditResultOut]:
        """
        Parameters
        ----------
        image_id : str

        result_data_url : str

        metadata : typing.Optional[typing.Dict[str, typing.Any]]

        source_image_ref : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EditResultOut]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/edit-results",
            method="POST",
            json={
                "metadata": metadata,
                "result_data_url": result_data_url,
                "source_image_ref": source_image_ref,
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
                    EditResultOut,
                    parse_obj_as(
                        type_=EditResultOut,
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

    async def get_edit_result_image(
        self, image_id: str, edit_result_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        image_id : str

        edit_result_ref : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/edit-results/{encode_path_param(edit_result_ref)}/image",
            method="GET",
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

    async def edit_events(
        self, image_id: str, *, job_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Parameters
        ----------
        image_id : str

        job_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/edit/events",
            method="GET",
            params={
                "job_id": job_id,
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

    async def ocr_image(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OcrResponse]:
        """
        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OcrResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/ocr",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OcrResponse,
                    parse_obj_as(
                        type_=OcrResponse,
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

    async def get_editor_project(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EditorProjectResponse]:
        """
        Return the saved Viskit editor project JSON for a canonical image id.

        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EditorProjectResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/project",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EditorProjectResponse,
                    parse_obj_as(
                        type_=EditorProjectResponse,
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

    async def put_editor_project(
        self,
        image_id: str,
        *,
        document: typing.Dict[str, typing.Any],
        expected_revision: typing.Optional[int] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EditorProjectResponse]:
        """
        Create or replace the persisted project JSON for a canonical image id.

        Parameters
        ----------
        image_id : str

        document : typing.Dict[str, typing.Any]
            Versioned ViskitEditorDocument JSON object

        expected_revision : typing.Optional[int]
            Optimistic concurrency guard; 409 when it differs from stored revision.

        source_image_ref : typing.Optional[str]
            Optional source_images.id backing this project import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EditorProjectResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/project",
            method="PUT",
            json={
                "document": document,
                "expected_revision": expected_revision,
                "source_image_ref": source_image_ref,
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
                    EditorProjectResponse,
                    parse_obj_as(
                        type_=EditorProjectResponse,
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

    async def export_editor_project(
        self, image_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.Any]:
        """
        Download the saved editor project as project JSON.

        Parameters
        ----------
        image_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.Any]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/project/export",
            method="GET",
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

    async def import_editor_project(
        self,
        image_id: str,
        *,
        document: typing.Dict[str, typing.Any],
        expected_revision: typing.Optional[int] = OMIT,
        source_image_ref: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EditorProjectResponse]:
        """
        Import project JSON into the persisted editor state for this image.

        Parameters
        ----------
        image_id : str

        document : typing.Dict[str, typing.Any]
            Versioned ViskitEditorDocument JSON object

        expected_revision : typing.Optional[int]
            Optimistic concurrency guard; 409 when it differs from stored revision.

        source_image_ref : typing.Optional[str]
            Optional source_images.id backing this project import.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EditorProjectResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/project/import",
            method="POST",
            json={
                "document": document,
                "expected_revision": expected_revision,
                "source_image_ref": source_image_ref,
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
                    EditorProjectResponse,
                    parse_obj_as(
                        type_=EditorProjectResponse,
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

    async def save_edited_image(
        self,
        image_id: str,
        *,
        edit_result_ref: str,
        mode: SaveImageRequestMode,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SaveImageResponse]:
        """
        Persist an edit result via an explicit replace-or-copy choice.

        Parameters
        ----------
        image_id : str

        edit_result_ref : str

        mode : SaveImageRequestMode

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SaveImageResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/images/{encode_path_param(image_id)}/save",
            method="POST",
            json={
                "edit_result_ref": edit_result_ref,
                "mode": mode,
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
                    SaveImageResponse,
                    parse_obj_as(
                        type_=SaveImageResponse,
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
