

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
from ..types.content_update_param import ContentUpdateParam
from ..types.content_wrapper import ContentWrapper
from ..types.listed_single_page_list import ListedSinglePageList
from ..types.listed_snapshot_dto import ListedSnapshotDto
from ..types.single_page import SinglePage
from .types.list_single_pages_request_publish_phase import ListSinglePagesRequestPublishPhase
from .types.list_single_pages_request_visible import ListSinglePagesRequestVisible
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSinglePageV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_single_pages(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contributor: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListSinglePagesRequestPublishPhase] = None,
        visible: typing.Optional[ListSinglePagesRequestVisible] = None,
        keyword: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListedSinglePageList]:
        """
        List single pages with pagination, sorting, keyword, publish phase, visibility, and contributor filters.

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

        contributor : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Contributor user names used to filter single pages. A page matches when any listed contributor appears in status.contributors.

        publish_phase : typing.Optional[ListSinglePagesRequestPublishPhase]
            Filter single pages by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.

        visible : typing.Optional[ListSinglePagesRequestVisible]
            Filter single pages by visibility, such as PUBLIC, INTERNAL, or PRIVATE.

        keyword : typing.Optional[str]
            Keyword used to match single page title, slug, or excerpt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListedSinglePageList]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/singlepages",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "contributor": contributor,
                "publishPhase": publish_phase,
                "visible": visible,
                "keyword": keyword,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListedSinglePageList,
                    parse_obj_as(
                        type_=ListedSinglePageList,
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

    def draft_single_page(
        self, *, content: ContentUpdateParam, page: SinglePage, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SinglePage]:
        """
        Create a draft single page together with its initial content.

        Parameters
        ----------
        content : ContentUpdateParam

        page : SinglePage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SinglePage]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/singlepages",
            method="POST",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=ContentUpdateParam, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(object_=page, annotation=SinglePage, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    def update_draft_single_page(
        self,
        name: str,
        *,
        content: ContentUpdateParam,
        page: SinglePage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SinglePage]:
        """
        Update single page metadata, spec, and content in one request.

        Parameters
        ----------
        name : str
            metadata.name of the single page to update.

        content : ContentUpdateParam

        page : SinglePage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SinglePage]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}",
            method="PUT",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=ContentUpdateParam, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(object_=page, annotation=SinglePage, direction="write"),
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
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    def fetch_single_page_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentWrapper]:
        """
        Fetch a single page content snapshot reconstructed from its base snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        snapshot_name : str
            Content snapshot metadata.name to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentWrapper]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/content",
            method="GET",
            params={
                "snapshotName": snapshot_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentWrapper,
                    parse_obj_as(
                        type_=ContentWrapper,
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

    def update_single_page_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        raw_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SinglePage]:
        """
        Update only the content of an existing single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page whose content will be updated.

        content : str
            Rendered HTML or normalized content derived from raw.

        raw : str
            Source text stored by the editor.

        raw_type : str
            Editor/source format of the raw content, for example HTML or Markdown.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SinglePage]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/content",
            method="PUT",
            json={
                "content": content,
                "raw": raw,
                "rawType": raw_type,
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
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    def delete_single_page_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentWrapper]:
        """
        Delete a content snapshot from a single page and return the deleted content.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        snapshot_name : str
            Content snapshot metadata.name to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentWrapper]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/content",
            method="DELETE",
            params={
                "snapshotName": snapshot_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentWrapper,
                    parse_obj_as(
                        type_=ContentWrapper,
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

    def fetch_single_page_head_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentWrapper]:
        """
        Fetch the editable head content of a single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentWrapper]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/head-content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentWrapper,
                    parse_obj_as(
                        type_=ContentWrapper,
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

    def publish_single_page(
        self,
        name: str,
        *,
        async_: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SinglePage]:
        """
        Publish a single page. By default, the request waits until the release snapshot is available.

        Parameters
        ----------
        name : str
            metadata.name of the single page to publish.

        async_ : typing.Optional[bool]
            Whether to return immediately after marking the single page for publishing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SinglePage]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/publish",
            method="PUT",
            params={
                "async": async_,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    def fetch_single_page_release_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentWrapper]:
        """
        Fetch the released content currently served for a published single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentWrapper]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/release-content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentWrapper,
                    parse_obj_as(
                        type_=ContentWrapper,
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

    def revert_to_specified_snapshot_for_single_page(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SinglePage]:
        """
        Restore the single page content from a specified snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the single page whose content will be restored.

        snapshot_name : str
            snapshot <code>metadata.name</code> to restore as the single page's head content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SinglePage]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/revert-content",
            method="PUT",
            json={
                "snapshotName": snapshot_name,
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
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    def list_single_page_snapshots(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ListedSnapshotDto]]:
        """
        List content snapshots for a single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ListedSnapshotDto]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/snapshot",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListedSnapshotDto],
                    parse_obj_as(
                        type_=typing.List[ListedSnapshotDto],
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


class AsyncRawSinglePageV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_single_pages(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        contributor: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListSinglePagesRequestPublishPhase] = None,
        visible: typing.Optional[ListSinglePagesRequestVisible] = None,
        keyword: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListedSinglePageList]:
        """
        List single pages with pagination, sorting, keyword, publish phase, visibility, and contributor filters.

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

        contributor : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            Contributor user names used to filter single pages. A page matches when any listed contributor appears in status.contributors.

        publish_phase : typing.Optional[ListSinglePagesRequestPublishPhase]
            Filter single pages by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.

        visible : typing.Optional[ListSinglePagesRequestVisible]
            Filter single pages by visibility, such as PUBLIC, INTERNAL, or PRIVATE.

        keyword : typing.Optional[str]
            Keyword used to match single page title, slug, or excerpt.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListedSinglePageList]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/singlepages",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "contributor": contributor,
                "publishPhase": publish_phase,
                "visible": visible,
                "keyword": keyword,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListedSinglePageList,
                    parse_obj_as(
                        type_=ListedSinglePageList,
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

    async def draft_single_page(
        self, *, content: ContentUpdateParam, page: SinglePage, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SinglePage]:
        """
        Create a draft single page together with its initial content.

        Parameters
        ----------
        content : ContentUpdateParam

        page : SinglePage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SinglePage]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/singlepages",
            method="POST",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=ContentUpdateParam, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(object_=page, annotation=SinglePage, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    async def update_draft_single_page(
        self,
        name: str,
        *,
        content: ContentUpdateParam,
        page: SinglePage,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SinglePage]:
        """
        Update single page metadata, spec, and content in one request.

        Parameters
        ----------
        name : str
            metadata.name of the single page to update.

        content : ContentUpdateParam

        page : SinglePage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SinglePage]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}",
            method="PUT",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=ContentUpdateParam, direction="write"
                ),
                "page": convert_and_respect_annotation_metadata(object_=page, annotation=SinglePage, direction="write"),
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
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    async def fetch_single_page_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentWrapper]:
        """
        Fetch a single page content snapshot reconstructed from its base snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        snapshot_name : str
            Content snapshot metadata.name to fetch.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentWrapper]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/content",
            method="GET",
            params={
                "snapshotName": snapshot_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentWrapper,
                    parse_obj_as(
                        type_=ContentWrapper,
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

    async def update_single_page_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        raw_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SinglePage]:
        """
        Update only the content of an existing single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page whose content will be updated.

        content : str
            Rendered HTML or normalized content derived from raw.

        raw : str
            Source text stored by the editor.

        raw_type : str
            Editor/source format of the raw content, for example HTML or Markdown.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SinglePage]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/content",
            method="PUT",
            json={
                "content": content,
                "raw": raw,
                "rawType": raw_type,
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
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    async def delete_single_page_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentWrapper]:
        """
        Delete a content snapshot from a single page and return the deleted content.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        snapshot_name : str
            Content snapshot metadata.name to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentWrapper]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/content",
            method="DELETE",
            params={
                "snapshotName": snapshot_name,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentWrapper,
                    parse_obj_as(
                        type_=ContentWrapper,
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

    async def fetch_single_page_head_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentWrapper]:
        """
        Fetch the editable head content of a single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentWrapper]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/head-content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentWrapper,
                    parse_obj_as(
                        type_=ContentWrapper,
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

    async def publish_single_page(
        self,
        name: str,
        *,
        async_: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SinglePage]:
        """
        Publish a single page. By default, the request waits until the release snapshot is available.

        Parameters
        ----------
        name : str
            metadata.name of the single page to publish.

        async_ : typing.Optional[bool]
            Whether to return immediately after marking the single page for publishing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SinglePage]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/publish",
            method="PUT",
            params={
                "async": async_,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    async def fetch_single_page_release_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentWrapper]:
        """
        Fetch the released content currently served for a published single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentWrapper]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/release-content",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ContentWrapper,
                    parse_obj_as(
                        type_=ContentWrapper,
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

    async def revert_to_specified_snapshot_for_single_page(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SinglePage]:
        """
        Restore the single page content from a specified snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the single page whose content will be restored.

        snapshot_name : str
            snapshot <code>metadata.name</code> to restore as the single page's head content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SinglePage]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/revert-content",
            method="PUT",
            json={
                "snapshotName": snapshot_name,
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
                    SinglePage,
                    parse_obj_as(
                        type_=SinglePage,
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

    async def list_single_page_snapshots(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ListedSnapshotDto]]:
        """
        List content snapshots for a single page.

        Parameters
        ----------
        name : str
            metadata.name of the single page.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ListedSnapshotDto]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/singlepages/{encode_path_param(name)}/snapshot",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListedSnapshotDto],
                    parse_obj_as(
                        type_=typing.List[ListedSnapshotDto],
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
