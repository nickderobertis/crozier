

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
from ..types.files_sharing_shareapi_create_share200response import FilesSharingShareapiCreateShare200Response
from ..types.files_sharing_shareapi_get_shares200response import FilesSharingShareapiGetShares200Response
from pydantic import ValidationError


class RawFilesSharingShareapiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_shares(
        self,
        *,
        shared_with_me: typing.Optional[str] = None,
        reshares: typing.Optional[str] = None,
        subfiles: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        include_tags: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FilesSharingShareapiGetShares200Response]:
        """
        Parameters
        ----------
        shared_with_me : typing.Optional[str]
            Only get shares with the current user

        reshares : typing.Optional[str]
            Only get shares by the current user and reshares

        subfiles : typing.Optional[str]
            Only get all shares in a folder

        path : typing.Optional[str]
            Get shares for a specific path

        include_tags : typing.Optional[str]
            Include tags in the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilesSharingShareapiGetShares200Response]
            Shares returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/shares",
            method="GET",
            params={
                "shared_with_me": shared_with_me,
                "reshares": reshares,
                "subfiles": subfiles,
                "path": path,
                "include_tags": include_tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiGetShares200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiGetShares200Response,
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

    def create_share(
        self,
        *,
        path: typing.Optional[str] = None,
        permissions: typing.Optional[int] = None,
        share_type: typing.Optional[int] = None,
        share_with: typing.Optional[str] = None,
        public_upload: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        send_password_by_talk: typing.Optional[str] = None,
        expire_date: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FilesSharingShareapiCreateShare200Response]:
        """
        Parameters
        ----------
        path : typing.Optional[str]
            Path of the share

        permissions : typing.Optional[int]
            Permissions for the share

        share_type : typing.Optional[int]
            Type of the share

        share_with : typing.Optional[str]
            The entity this should be shared with

        public_upload : typing.Optional[str]
            If public uploading is allowed

        password : typing.Optional[str]
            Password for the share

        send_password_by_talk : typing.Optional[str]
            Send the password for the share over Talk

        expire_date : typing.Optional[str]
            Expiry date of the share

        note : typing.Optional[str]
            Note for the share

        label : typing.Optional[str]
            Label for the share (only used in link and email)

        attributes : typing.Optional[str]
            Additional attributes for the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilesSharingShareapiCreateShare200Response]
            Share created
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/shares",
            method="POST",
            params={
                "path": path,
                "permissions": permissions,
                "shareType": share_type,
                "shareWith": share_with,
                "publicUpload": public_upload,
                "password": password,
                "sendPasswordByTalk": send_password_by_talk,
                "expireDate": expire_date,
                "note": note,
                "label": label,
                "attributes": attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiCreateShare200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiCreateShare200Response,
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

    def get_inherited_shares(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FilesSharingShareapiGetShares200Response]:
        """
        Parameters
        ----------
        path : str
            Path all shares will be relative to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilesSharingShareapiGetShares200Response]
            Shares returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/shares/inherited",
            method="GET",
            params={
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiGetShares200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiGetShares200Response,
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

    def pending_shares(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FilesSharingShareapiGetShares200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilesSharingShareapiGetShares200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/shares/pending",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiGetShares200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiGetShares200Response,
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

    def get_share(
        self,
        id: str,
        *,
        include_tags: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FilesSharingShareapiCreateShare200Response]:
        """
        Parameters
        ----------
        id : str
            ID of the share

        include_tags : typing.Optional[int]
            Include tags in the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilesSharingShareapiCreateShare200Response]
            Share returned
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/shares/{encode_path_param(id)}",
            method="GET",
            params={
                "include_tags": include_tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiCreateShare200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiCreateShare200Response,
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

    def update_share(
        self,
        id: str,
        *,
        permissions: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        send_password_by_talk: typing.Optional[str] = None,
        public_upload: typing.Optional[str] = None,
        expire_date: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        hide_download: typing.Optional[str] = None,
        attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FilesSharingShareapiCreateShare200Response]:
        """
        Parameters
        ----------
        id : str
            ID of the share

        permissions : typing.Optional[int]
            New permissions

        password : typing.Optional[str]
            New password

        send_password_by_talk : typing.Optional[str]
            New condition if the password should be send over Talk

        public_upload : typing.Optional[str]
            New condition if public uploading is allowed

        expire_date : typing.Optional[str]
            New expiry date

        note : typing.Optional[str]
            New note

        label : typing.Optional[str]
            New label

        hide_download : typing.Optional[str]
            New condition if the download should be hidden

        attributes : typing.Optional[str]
            New additional attributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FilesSharingShareapiCreateShare200Response]
            Share updated successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/shares/{encode_path_param(id)}",
            method="PUT",
            params={
                "permissions": permissions,
                "password": password,
                "sendPasswordByTalk": send_password_by_talk,
                "publicUpload": public_upload,
                "expireDate": expire_date,
                "note": note,
                "label": label,
                "hideDownload": hide_download,
                "attributes": attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiCreateShare200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiCreateShare200Response,
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

    def delete_share(
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
            Share deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/shares/{encode_path_param(id)}",
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

    def accept_share(
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
            Share accepted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/shares/pending/{encode_path_param(id)}",
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


class AsyncRawFilesSharingShareapiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_shares(
        self,
        *,
        shared_with_me: typing.Optional[str] = None,
        reshares: typing.Optional[str] = None,
        subfiles: typing.Optional[str] = None,
        path: typing.Optional[str] = None,
        include_tags: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FilesSharingShareapiGetShares200Response]:
        """
        Parameters
        ----------
        shared_with_me : typing.Optional[str]
            Only get shares with the current user

        reshares : typing.Optional[str]
            Only get shares by the current user and reshares

        subfiles : typing.Optional[str]
            Only get all shares in a folder

        path : typing.Optional[str]
            Get shares for a specific path

        include_tags : typing.Optional[str]
            Include tags in the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilesSharingShareapiGetShares200Response]
            Shares returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/shares",
            method="GET",
            params={
                "shared_with_me": shared_with_me,
                "reshares": reshares,
                "subfiles": subfiles,
                "path": path,
                "include_tags": include_tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiGetShares200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiGetShares200Response,
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

    async def create_share(
        self,
        *,
        path: typing.Optional[str] = None,
        permissions: typing.Optional[int] = None,
        share_type: typing.Optional[int] = None,
        share_with: typing.Optional[str] = None,
        public_upload: typing.Optional[str] = None,
        password: typing.Optional[str] = None,
        send_password_by_talk: typing.Optional[str] = None,
        expire_date: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FilesSharingShareapiCreateShare200Response]:
        """
        Parameters
        ----------
        path : typing.Optional[str]
            Path of the share

        permissions : typing.Optional[int]
            Permissions for the share

        share_type : typing.Optional[int]
            Type of the share

        share_with : typing.Optional[str]
            The entity this should be shared with

        public_upload : typing.Optional[str]
            If public uploading is allowed

        password : typing.Optional[str]
            Password for the share

        send_password_by_talk : typing.Optional[str]
            Send the password for the share over Talk

        expire_date : typing.Optional[str]
            Expiry date of the share

        note : typing.Optional[str]
            Note for the share

        label : typing.Optional[str]
            Label for the share (only used in link and email)

        attributes : typing.Optional[str]
            Additional attributes for the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilesSharingShareapiCreateShare200Response]
            Share created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/shares",
            method="POST",
            params={
                "path": path,
                "permissions": permissions,
                "shareType": share_type,
                "shareWith": share_with,
                "publicUpload": public_upload,
                "password": password,
                "sendPasswordByTalk": send_password_by_talk,
                "expireDate": expire_date,
                "note": note,
                "label": label,
                "attributes": attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiCreateShare200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiCreateShare200Response,
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

    async def get_inherited_shares(
        self, *, path: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FilesSharingShareapiGetShares200Response]:
        """
        Parameters
        ----------
        path : str
            Path all shares will be relative to

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilesSharingShareapiGetShares200Response]
            Shares returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/shares/inherited",
            method="GET",
            params={
                "path": path,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiGetShares200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiGetShares200Response,
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

    async def pending_shares(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FilesSharingShareapiGetShares200Response]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilesSharingShareapiGetShares200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/files_sharing/api/v1/shares/pending",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiGetShares200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiGetShares200Response,
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

    async def get_share(
        self,
        id: str,
        *,
        include_tags: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FilesSharingShareapiCreateShare200Response]:
        """
        Parameters
        ----------
        id : str
            ID of the share

        include_tags : typing.Optional[int]
            Include tags in the share

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilesSharingShareapiCreateShare200Response]
            Share returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/shares/{encode_path_param(id)}",
            method="GET",
            params={
                "include_tags": include_tags,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiCreateShare200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiCreateShare200Response,
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

    async def update_share(
        self,
        id: str,
        *,
        permissions: typing.Optional[int] = None,
        password: typing.Optional[str] = None,
        send_password_by_talk: typing.Optional[str] = None,
        public_upload: typing.Optional[str] = None,
        expire_date: typing.Optional[str] = None,
        note: typing.Optional[str] = None,
        label: typing.Optional[str] = None,
        hide_download: typing.Optional[str] = None,
        attributes: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FilesSharingShareapiCreateShare200Response]:
        """
        Parameters
        ----------
        id : str
            ID of the share

        permissions : typing.Optional[int]
            New permissions

        password : typing.Optional[str]
            New password

        send_password_by_talk : typing.Optional[str]
            New condition if the password should be send over Talk

        public_upload : typing.Optional[str]
            New condition if public uploading is allowed

        expire_date : typing.Optional[str]
            New expiry date

        note : typing.Optional[str]
            New note

        label : typing.Optional[str]
            New label

        hide_download : typing.Optional[str]
            New condition if the download should be hidden

        attributes : typing.Optional[str]
            New additional attributes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FilesSharingShareapiCreateShare200Response]
            Share updated successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/shares/{encode_path_param(id)}",
            method="PUT",
            params={
                "permissions": permissions,
                "password": password,
                "sendPasswordByTalk": send_password_by_talk,
                "publicUpload": public_upload,
                "expireDate": expire_date,
                "note": note,
                "label": label,
                "hideDownload": hide_download,
                "attributes": attributes,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FilesSharingShareapiCreateShare200Response,
                    parse_obj_as(
                        type_=FilesSharingShareapiCreateShare200Response,
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

    async def delete_share(
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
            Share deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/shares/{encode_path_param(id)}",
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

    async def accept_share(
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
            Share accepted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/files_sharing/api/v1/shares/pending/{encode_path_param(id)}",
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
