

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.get_file_copyrights import GetFileCopyrights
from ..types.info import Info
from .types.get_file_authors_request_status import GetFileAuthorsRequestStatus
from .types.get_file_copyrights_request_status import GetFileCopyrightsRequestStatus
from .types.get_file_eccs_request_status import GetFileEccsRequestStatus
from .types.get_file_emails_request_status import GetFileEmailsRequestStatus
from .types.get_file_ipras_request_status import GetFileIprasRequestStatus
from .types.get_file_keywords_request_status import GetFileKeywordsRequestStatus
from .types.get_file_scan_code_author_request_status import GetFileScanCodeAuthorRequestStatus
from .types.get_file_scan_code_copyrights_request_status import GetFileScanCodeCopyrightsRequestStatus
from .types.get_file_scan_code_email_request_status import GetFileScanCodeEmailRequestStatus
from .types.get_file_scan_code_url_request_status import GetFileScanCodeUrlRequestStatus
from .types.get_file_urls_request_status import GetFileUrlsRequestStatus
from .types.get_file_user_copyrights_request_status import GetFileUserCopyrightsRequestStatus
from .types.get_total_file_copyrights_request_status import GetTotalFileCopyrightsRequestStatus
from .types.get_total_file_copyrights_response_item import GetTotalFileCopyrightsResponseItem
from .types.get_total_file_user_copyrights_request_status import GetTotalFileUserCopyrightsRequestStatus
from .types.get_total_file_user_copyrights_response_item import GetTotalFileUserCopyrightsResponseItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawCopyrightsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_file_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of copyrights associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileCopyrightsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/copyrights",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_copyrights(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates a copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/copyrights/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_copyrights(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes a copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/copyrights/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_copyrights(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores a copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/copyrights/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_user_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileUserCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of user copyright findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileUserCopyrightsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/user-copyrights",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_user_copyright(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates user copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/user-copyrights/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_user_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes user copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/user-copyrights/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_user_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores user copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/user-copyrights/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_scan_code_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of scancode copyright findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileScanCodeCopyrightsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-copyrights",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_scan_code_copyright(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates scancode copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-copyrights/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_scan_code_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes scancode copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-copyrights/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_scan_code_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores scancode copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-copyrights/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_emails(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileEmailsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of emails associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileEmailsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/emails",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_email(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates an email statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/emails/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_emails(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes an email statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/emails/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores an email statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/emails/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_scan_code_email(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeEmailRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of scancode email findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileScanCodeEmailRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-emails",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_scan_code_email(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates scancode email finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-emails/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_scan_code_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes scancode email finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-emails/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_scan_code_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores scancode email finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-emails/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_urls(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileUrlsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of URLs associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileUrlsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/urls",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_url(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates an URL statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/urls/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes an URL statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/urls/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores an URL statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/urls/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_scan_code_url(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeUrlRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of scancode url findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileScanCodeUrlRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-urls",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_scan_code_url(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates scancode url finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-urls/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_scan_code_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes scancode url finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-urls/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_scan_code_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores scancode url finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-urls/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_authors(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileAuthorsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of authors associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileAuthorsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/authors",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_author(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates an author statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/authors/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes an author statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/authors/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores an author statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/authors/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_scan_code_author(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeAuthorRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of scancode author findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileScanCodeAuthorRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-authors",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_scan_code_author(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates scancode author finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-authors/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_scan_code_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes scancode author finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-authors/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_scan_code_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores scancode author finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-authors/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_eccs(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileEccsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of ECCs associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileEccsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/eccs",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_ecc(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates an ECC statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/eccs/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_ecc(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes an ECC statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/eccs/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_ecc(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores an ECC statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/eccs/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_keywords(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileKeywordsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of keywords associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileKeywordsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/keywords",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_keyword(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates a keyword statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/keywords/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_keyword(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes a keyword statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/keywords/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_keyword(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores a keyword statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/keywords/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_file_ipras(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileIprasRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of IPRAs associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileIprasRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/ipras",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    def update_file_ipra(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Info]:
        """
        Updates an IPRA statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/ipras/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def delete_file_ipra(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Deletes an IPRA statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/ipras/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def restore_file_ipra(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Info]:
        """
        Restores an IPRA statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Info]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/ipras/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    def get_total_file_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetTotalFileCopyrightsRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetTotalFileCopyrightsResponseItem]]:
        """
        Returns the total number of copyrights associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            Upload Tree ID

        status : GetTotalFileCopyrightsRequestStatus
            status of the copyright

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetTotalFileCopyrightsResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/totalcopyrights",
            method="GET",
            params={
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetTotalFileCopyrightsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetTotalFileCopyrightsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def get_total_file_user_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetTotalFileUserCopyrightsRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[GetTotalFileUserCopyrightsResponseItem]]:
        """
        Returns the total number of user copyright findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            Upload Tree ID

        status : GetTotalFileUserCopyrightsRequestStatus
            status of the copyright

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[GetTotalFileUserCopyrightsResponseItem]]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/totalusercopyrights",
            method="GET",
            params={
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetTotalFileUserCopyrightsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetTotalFileUserCopyrightsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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


class AsyncRawCopyrightsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_file_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of copyrights associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileCopyrightsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/copyrights",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_copyrights(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates a copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/copyrights/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_copyrights(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes a copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/copyrights/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_copyrights(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores a copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/copyrights/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_user_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileUserCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of user copyright findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileUserCopyrightsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/user-copyrights",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_user_copyright(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates user copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/user-copyrights/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_user_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes user copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/user-copyrights/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_user_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores user copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/user-copyrights/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_scan_code_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of scancode copyright findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileScanCodeCopyrightsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-copyrights",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_scan_code_copyright(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates scancode copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-copyrights/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_scan_code_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes scancode copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-copyrights/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_scan_code_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores scancode copyright statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-copyrights/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_emails(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileEmailsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of emails associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileEmailsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/emails",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_email(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates an email statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/emails/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_emails(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes an email statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/emails/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores an email statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/emails/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_scan_code_email(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeEmailRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of scancode email findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileScanCodeEmailRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-emails",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_scan_code_email(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates scancode email finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-emails/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_scan_code_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes scancode email finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-emails/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_scan_code_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores scancode email finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-emails/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_urls(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileUrlsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of URLs associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileUrlsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/urls",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_url(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates an URL statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/urls/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes an URL statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/urls/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores an URL statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/urls/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_scan_code_url(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeUrlRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of scancode url findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileScanCodeUrlRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-urls",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_scan_code_url(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates scancode url finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-urls/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_scan_code_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes scancode url finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-urls/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_scan_code_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores scancode url finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-urls/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_authors(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileAuthorsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of authors associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileAuthorsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/authors",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_author(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates an author statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/authors/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes an author statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/authors/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores an author statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/authors/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_scan_code_author(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeAuthorRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of scancode author findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileScanCodeAuthorRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-authors",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_scan_code_author(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates scancode author finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-authors/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_scan_code_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes scancode author finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-authors/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_scan_code_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores scancode author finding for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/scancode-authors/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_eccs(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileEccsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of ECCs associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileEccsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/eccs",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_ecc(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates an ECC statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/eccs/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_ecc(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes an ECC statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/eccs/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_ecc(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores an ECC statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/eccs/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_keywords(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileKeywordsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of keywords associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileKeywordsRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/keywords",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_keyword(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates a keyword statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/keywords/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_keyword(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes a keyword statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/keywords/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_keyword(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores a keyword statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/keywords/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_file_ipras(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileIprasRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetFileCopyrights]]:
        """
        Returns the list of IPRAs associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            UploadTree ID (available via /uploads/{id}/topitem & /uploads/{id}/item/{itemId}/tree/view)

        status : GetFileIprasRequestStatus
            Status of the CX

        limit : typing.Optional[int]
            Limits of responses per request

        page : typing.Optional[int]
            Page number for responses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetFileCopyrights]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/ipras",
            method="GET",
            params={
                "status": status,
            },
            headers={
                "limit": str(limit) if limit is not None else None,
                "page": str(page) if page is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetFileCopyrights],
                    parse_obj_as(
                        type_=typing.List[GetFileCopyrights],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
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

    async def update_file_ipra(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Info]:
        """
        Updates an IPRA statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        content : typing.Optional[str]
            Copyright text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/ipras/{encode_path_param(hash)}",
            method="PUT",
            json={
                "content": content,
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
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def delete_file_ipra(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Deletes an IPRA statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/ipras/{encode_path_param(hash)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def restore_file_ipra(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Info]:
        """
        Restores an IPRA statement for a particular file

        Parameters
        ----------
        id : int
            Upload ID

        item_id : int
            Upload tree ID

        hash : str
            CX hash

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Info]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/ipras/{encode_path_param(hash)}",
            method="PATCH",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Info,
                    parse_obj_as(
                        type_=Info,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
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

    async def get_total_file_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetTotalFileCopyrightsRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetTotalFileCopyrightsResponseItem]]:
        """
        Returns the total number of copyrights associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            Upload Tree ID

        status : GetTotalFileCopyrightsRequestStatus
            status of the copyright

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetTotalFileCopyrightsResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/totalcopyrights",
            method="GET",
            params={
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetTotalFileCopyrightsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetTotalFileCopyrightsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def get_total_file_user_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetTotalFileUserCopyrightsRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[GetTotalFileUserCopyrightsResponseItem]]:
        """
        Returns the total number of user copyright findings associated with the file

        Parameters
        ----------
        id : int
            Upload Id

        item_id : int
            Upload Tree ID

        status : GetTotalFileUserCopyrightsRequestStatus
            status of the copyright

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[GetTotalFileUserCopyrightsResponseItem]]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"uploads/{encode_path_param(id)}/item/{encode_path_param(item_id)}/totalusercopyrights",
            method="GET",
            params={
                "status": status,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[GetTotalFileUserCopyrightsResponseItem],
                    parse_obj_as(
                        type_=typing.List[GetTotalFileUserCopyrightsResponseItem],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Info,
                        parse_obj_as(
                            type_=Info,
                            object_=_response.json(),
                        ),
                    ),
                )
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
