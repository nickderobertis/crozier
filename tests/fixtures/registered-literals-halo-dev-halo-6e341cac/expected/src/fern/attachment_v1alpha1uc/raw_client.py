

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.attachment import Attachment
from ..types.attachment_list import AttachmentList
from ..types.attachment_permalink_match_list import AttachmentPermalinkMatchList
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAttachmentV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_my_attachments(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ungrouped: typing.Optional[bool] = None,
        keyword: typing.Optional[str] = None,
        accepts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AttachmentList]:
        """
        List attachments of the current user uploaded.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        ungrouped : typing.Optional[bool]
            Filter attachments without group. This parameter will ignore group parameter.

        keyword : typing.Optional[str]
            Keyword for searching.

        accepts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Acceptable media types.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AttachmentList]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "ungrouped": ungrouped,
                "keyword": keyword,
                "accepts": accepts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AttachmentList,
                    parse_obj_as(
                        type_=AttachmentList,
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

    def create_attachment_for_post(
        self,
        *,
        file: core.File,
        wait_for_permalink: typing.Optional[bool] = None,
        post_name: typing.Optional[str] = OMIT,
        single_page_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Attachment]:
        """
        Create attachment for the given post. Deprecated in favor of /attachments/-/upload.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        wait_for_permalink : typing.Optional[bool]
            Wait for permalink.

        post_name : typing.Optional[str]
            post <code>metadata.name</code>

        single_page_name : typing.Optional[str]
            single page <code>metadata.name</code>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Attachment]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments",
            method="POST",
            params={
                "waitForPermalink": wait_for_permalink,
            },
            data={
                "postName": post_name,
                "singlePageName": single_page_name,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Attachment,
                    parse_obj_as(
                        type_=Attachment,
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

    def match_attachment_permalinks_for_uc(
        self, *, urls: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AttachmentPermalinkMatchList]:
        """
        Match URL strings against Attachment permalinks for user center.

        Parameters
        ----------
        urls : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AttachmentPermalinkMatchList]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments/-/match-permalinks",
            method="POST",
            json={
                "urls": urls,
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
                    AttachmentPermalinkMatchList,
                    parse_obj_as(
                        type_=AttachmentPermalinkMatchList,
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

    def upload_attachment_for_uc(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Attachment]:
        """
        Upload attachment to user center storage.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        filename : typing.Optional[str]
            The filename to use when uploading from url. If not provided, the filename will be extracted from the url.

        url : typing.Optional[str]
            The url to upload from. If not provided, the file will be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Attachment]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments/-/upload",
            method="POST",
            data={
                "filename": filename,
                "url": url,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Attachment,
                    parse_obj_as(
                        type_=Attachment,
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

    def external_transfer_attachment1(
        self,
        *,
        url: str,
        wait_for_permalink: typing.Optional[bool] = None,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Attachment]:
        """
        Upload attachment from the given URL.
        Deprecated in favor of /attachments/-/upload.

        Parameters
        ----------
        url : str
            remote file URL to transfer into user-center storage

        wait_for_permalink : typing.Optional[bool]
            Wait for permalink.

        filename : typing.Optional[str]
            custom file name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Attachment]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments/-/upload-from-url",
            method="POST",
            params={
                "waitForPermalink": wait_for_permalink,
            },
            json={
                "filename": filename,
                "url": url,
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
                    Attachment,
                    parse_obj_as(
                        type_=Attachment,
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


class AsyncRawAttachmentV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_my_attachments(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        ungrouped: typing.Optional[bool] = None,
        keyword: typing.Optional[str] = None,
        accepts: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AttachmentList]:
        """
        List attachments of the current user uploaded.

        Parameters
        ----------
        page : typing.Optional[int]
            Page number. Default is 0.

        size : typing.Optional[int]
            Size number. Default is 0.

        label_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Label selector. e.g.: hidden!=true

        field_selector : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Field selector. e.g.: metadata.name==halo

        sort : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Sorting criteria in the format: property,(asc|desc). Default sort order is ascending. Multiple sort criteria are supported.

        ungrouped : typing.Optional[bool]
            Filter attachments without group. This parameter will ignore group parameter.

        keyword : typing.Optional[str]
            Keyword for searching.

        accepts : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Acceptable media types.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AttachmentList]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "ungrouped": ungrouped,
                "keyword": keyword,
                "accepts": accepts,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AttachmentList,
                    parse_obj_as(
                        type_=AttachmentList,
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

    async def create_attachment_for_post(
        self,
        *,
        file: core.File,
        wait_for_permalink: typing.Optional[bool] = None,
        post_name: typing.Optional[str] = OMIT,
        single_page_name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Attachment]:
        """
        Create attachment for the given post. Deprecated in favor of /attachments/-/upload.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        wait_for_permalink : typing.Optional[bool]
            Wait for permalink.

        post_name : typing.Optional[str]
            post <code>metadata.name</code>

        single_page_name : typing.Optional[str]
            single page <code>metadata.name</code>

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Attachment]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments",
            method="POST",
            params={
                "waitForPermalink": wait_for_permalink,
            },
            data={
                "postName": post_name,
                "singlePageName": single_page_name,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Attachment,
                    parse_obj_as(
                        type_=Attachment,
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

    async def match_attachment_permalinks_for_uc(
        self, *, urls: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AttachmentPermalinkMatchList]:
        """
        Match URL strings against Attachment permalinks for user center.

        Parameters
        ----------
        urls : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AttachmentPermalinkMatchList]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments/-/match-permalinks",
            method="POST",
            json={
                "urls": urls,
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
                    AttachmentPermalinkMatchList,
                    parse_obj_as(
                        type_=AttachmentPermalinkMatchList,
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

    async def upload_attachment_for_uc(
        self,
        *,
        file: typing.Optional[core.File] = OMIT,
        filename: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Attachment]:
        """
        Upload attachment to user center storage.

        Parameters
        ----------
        file : typing.Optional[core.File]
            See core.File for more documentation

        filename : typing.Optional[str]
            The filename to use when uploading from url. If not provided, the filename will be extracted from the url.

        url : typing.Optional[str]
            The url to upload from. If not provided, the file will be used.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Attachment]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments/-/upload",
            method="POST",
            data={
                "filename": filename,
                "url": url,
            },
            files={
                **({"file": file} if file is not None else {}),
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Attachment,
                    parse_obj_as(
                        type_=Attachment,
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

    async def external_transfer_attachment1(
        self,
        *,
        url: str,
        wait_for_permalink: typing.Optional[bool] = None,
        filename: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Attachment]:
        """
        Upload attachment from the given URL.
        Deprecated in favor of /attachments/-/upload.

        Parameters
        ----------
        url : str
            remote file URL to transfer into user-center storage

        wait_for_permalink : typing.Optional[bool]
            Wait for permalink.

        filename : typing.Optional[str]
            custom file name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Attachment]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.storage.halo.run/v1alpha1/attachments/-/upload-from-url",
            method="POST",
            params={
                "waitForPermalink": wait_for_permalink,
            },
            json={
                "filename": filename,
                "url": url,
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
                    Attachment,
                    parse_obj_as(
                        type_=Attachment,
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
