

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.get_file_copyrights import GetFileCopyrights
from ..types.info import Info
from .raw_client import AsyncRawCopyrightsClient, RawCopyrightsClient
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


OMIT = typing.cast(typing.Any, ...)


class CopyrightsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCopyrightsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCopyrightsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCopyrightsClient
        """
        return self._raw_client

    def get_file_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_copyrights(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_copyrights(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_copyrights(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_copyrights(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_copyrights(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_copyrights(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_copyrights(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_copyrights(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_copyrights(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_copyrights(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_copyrights(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_user_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileUserCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_user_copyrights(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_user_copyrights(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_user_copyright(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_user_copyright(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_user_copyright(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_user_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_user_copyright(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_user_copyright(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_user_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_user_copyright(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_user_copyright(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_scan_code_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_scan_code_copyrights(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_scan_code_copyrights(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_scan_code_copyright(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_scan_code_copyright(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_scan_code_copyright(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_scan_code_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_scan_code_copyright(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_scan_code_copyright(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_scan_code_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_scan_code_copyright(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_scan_code_copyright(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    def get_file_emails(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileEmailsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_emails(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_emails(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_email(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_email(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_email(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_emails(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_emails(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_emails(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_email(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_email(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_scan_code_email(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeEmailRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_scan_code_email(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_scan_code_email(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_scan_code_email(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_scan_code_email(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_scan_code_email(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_scan_code_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_scan_code_email(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_scan_code_email(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_scan_code_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_scan_code_email(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_scan_code_email(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_urls(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileUrlsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_urls(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_urls(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_url(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_url(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_url(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_url(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_url(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_url(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_url(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_scan_code_url(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeUrlRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_scan_code_url(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_scan_code_url(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_scan_code_url(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_scan_code_url(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_scan_code_url(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_scan_code_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_scan_code_url(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_scan_code_url(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_scan_code_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_scan_code_url(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_scan_code_url(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_authors(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileAuthorsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_authors(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_authors(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_author(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_author(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_author(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_author(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_author(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_author(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_author(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_scan_code_author(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeAuthorRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_scan_code_author(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_scan_code_author(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_scan_code_author(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_scan_code_author(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_scan_code_author(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_scan_code_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_scan_code_author(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_scan_code_author(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_scan_code_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_scan_code_author(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_scan_code_author(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_eccs(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileEccsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_eccs(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_eccs(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_ecc(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_ecc(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_ecc(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_ecc(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_ecc(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_ecc(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_ecc(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_ecc(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_ecc(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_keywords(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileKeywordsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_keywords(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_keywords(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_keyword(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_keyword(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_keyword(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_keyword(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_keyword(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_keyword(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_keyword(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_keyword(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_keyword(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_file_ipras(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileIprasRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_file_ipras(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_file_ipras(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    def update_file_ipra(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.update_file_ipra(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.update_file_ipra(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    def delete_file_ipra(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.delete_file_ipra(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.delete_file_ipra(id, item_id, hash, request_options=request_options)
        return _response.data

    def restore_file_ipra(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.restore_file_ipra(
            id=1,
            item_id=1,
            hash="hash",
        )
        """
        _response = self._raw_client.restore_file_ipra(id, item_id, hash, request_options=request_options)
        return _response.data

    def get_total_file_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetTotalFileCopyrightsRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetTotalFileCopyrightsResponseItem]:
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
        typing.List[GetTotalFileCopyrightsResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_total_file_copyrights(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_total_file_copyrights(
            id, item_id, status=status, request_options=request_options
        )
        return _response.data

    def get_total_file_user_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetTotalFileUserCopyrightsRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetTotalFileUserCopyrightsResponseItem]:
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
        typing.List[GetTotalFileUserCopyrightsResponseItem]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.copyrights.get_total_file_user_copyrights(
            id=1,
            item_id=1,
            status="active",
        )
        """
        _response = self._raw_client.get_total_file_user_copyrights(
            id, item_id, status=status, request_options=request_options
        )
        return _response.data


class AsyncCopyrightsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCopyrightsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCopyrightsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCopyrightsClient
        """
        return self._raw_client

    async def get_file_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_copyrights(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_copyrights(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_copyrights(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_copyrights(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_copyrights(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_copyrights(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_copyrights(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_copyrights(id, item_id, hash, request_options=request_options)
        return _response.data

    async def restore_file_copyrights(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_copyrights(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_copyrights(id, item_id, hash, request_options=request_options)
        return _response.data

    async def get_file_user_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileUserCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_user_copyrights(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_user_copyrights(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_user_copyright(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_user_copyright(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_user_copyright(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_user_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_user_copyright(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_user_copyright(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    async def restore_file_user_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_user_copyright(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_user_copyright(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    async def get_file_scan_code_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeCopyrightsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_scan_code_copyrights(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_scan_code_copyrights(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_scan_code_copyright(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_scan_code_copyright(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_scan_code_copyright(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_scan_code_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_scan_code_copyright(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_scan_code_copyright(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    async def restore_file_scan_code_copyright(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_scan_code_copyright(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_scan_code_copyright(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    async def get_file_emails(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileEmailsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_emails(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_emails(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_email(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_email(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_email(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_emails(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_emails(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_emails(id, item_id, hash, request_options=request_options)
        return _response.data

    async def restore_file_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_email(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_email(id, item_id, hash, request_options=request_options)
        return _response.data

    async def get_file_scan_code_email(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeEmailRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_scan_code_email(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_scan_code_email(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_scan_code_email(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_scan_code_email(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_scan_code_email(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_scan_code_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_scan_code_email(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_scan_code_email(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    async def restore_file_scan_code_email(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_scan_code_email(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_scan_code_email(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    async def get_file_urls(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileUrlsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_urls(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_urls(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_url(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_url(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_url(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_url(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_url(id, item_id, hash, request_options=request_options)
        return _response.data

    async def restore_file_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_url(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_url(id, item_id, hash, request_options=request_options)
        return _response.data

    async def get_file_scan_code_url(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeUrlRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_scan_code_url(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_scan_code_url(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_scan_code_url(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_scan_code_url(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_scan_code_url(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_scan_code_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_scan_code_url(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_scan_code_url(id, item_id, hash, request_options=request_options)
        return _response.data

    async def restore_file_scan_code_url(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_scan_code_url(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_scan_code_url(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    async def get_file_authors(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileAuthorsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_authors(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_authors(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_author(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_author(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_author(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_author(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_author(id, item_id, hash, request_options=request_options)
        return _response.data

    async def restore_file_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_author(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_author(id, item_id, hash, request_options=request_options)
        return _response.data

    async def get_file_scan_code_author(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileScanCodeAuthorRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_scan_code_author(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_scan_code_author(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_scan_code_author(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_scan_code_author(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_scan_code_author(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_scan_code_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_scan_code_author(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_scan_code_author(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    async def restore_file_scan_code_author(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_scan_code_author(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_scan_code_author(
            id, item_id, hash, request_options=request_options
        )
        return _response.data

    async def get_file_eccs(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileEccsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_eccs(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_eccs(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_ecc(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_ecc(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_ecc(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_ecc(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_ecc(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_ecc(id, item_id, hash, request_options=request_options)
        return _response.data

    async def restore_file_ecc(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_ecc(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_ecc(id, item_id, hash, request_options=request_options)
        return _response.data

    async def get_file_keywords(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileKeywordsRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_keywords(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_keywords(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_keyword(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_keyword(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_keyword(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_keyword(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_keyword(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_keyword(id, item_id, hash, request_options=request_options)
        return _response.data

    async def restore_file_keyword(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_keyword(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_keyword(id, item_id, hash, request_options=request_options)
        return _response.data

    async def get_file_ipras(
        self,
        id: int,
        item_id: int,
        *,
        status: GetFileIprasRequestStatus,
        limit: typing.Optional[int] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetFileCopyrights]:
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
        typing.List[GetFileCopyrights]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_file_ipras(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_file_ipras(
            id, item_id, status=status, limit=limit, page=page, request_options=request_options
        )
        return _response.data

    async def update_file_ipra(
        self,
        id: int,
        item_id: int,
        hash: str,
        *,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.update_file_ipra(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_file_ipra(
            id, item_id, hash, content=content, request_options=request_options
        )
        return _response.data

    async def delete_file_ipra(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.delete_file_ipra(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_file_ipra(id, item_id, hash, request_options=request_options)
        return _response.data

    async def restore_file_ipra(
        self, id: int, item_id: int, hash: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
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
        Info
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.restore_file_ipra(
                id=1,
                item_id=1,
                hash="hash",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restore_file_ipra(id, item_id, hash, request_options=request_options)
        return _response.data

    async def get_total_file_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetTotalFileCopyrightsRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetTotalFileCopyrightsResponseItem]:
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
        typing.List[GetTotalFileCopyrightsResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_total_file_copyrights(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_total_file_copyrights(
            id, item_id, status=status, request_options=request_options
        )
        return _response.data

    async def get_total_file_user_copyrights(
        self,
        id: int,
        item_id: int,
        *,
        status: GetTotalFileUserCopyrightsRequestStatus,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetTotalFileUserCopyrightsResponseItem]:
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
        typing.List[GetTotalFileUserCopyrightsResponseItem]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.copyrights.get_total_file_user_copyrights(
                id=1,
                item_id=1,
                status="active",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_total_file_user_copyrights(
            id, item_id, status=status, request_options=request_options
        )
        return _response.data
