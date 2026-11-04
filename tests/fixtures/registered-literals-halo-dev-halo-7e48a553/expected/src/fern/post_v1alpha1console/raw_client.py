

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
from ..types.listed_post_list import ListedPostList
from ..types.listed_snapshot_dto import ListedSnapshotDto
from ..types.post import Post
from .types.list_posts_request_publish_phase import ListPostsRequestPublishPhase
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPostV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_posts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListPostsRequestPublishPhase] = None,
        keyword: typing.Optional[str] = None,
        category_with_children: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListedPostList]:
        """
        List posts with pagination, sorting, keyword, publish phase, and category filters.

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

        publish_phase : typing.Optional[ListPostsRequestPublishPhase]
            Filter posts by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.

        keyword : typing.Optional[str]
            Keyword used to match post title, slug, or excerpt.

        category_with_children : typing.Optional[str]
            Category metadata name used to include posts in that category and its child categories.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListedPostList]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/posts",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "publishPhase": publish_phase,
                "keyword": keyword,
                "categoryWithChildren": category_with_children,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListedPostList,
                    parse_obj_as(
                        type_=ListedPostList,
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

    def draft_post(
        self, *, content: ContentUpdateParam, post: Post, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Post]:
        """
        Create a draft post together with its initial content.

        Parameters
        ----------
        content : ContentUpdateParam

        post : Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/posts",
            method="POST",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=ContentUpdateParam, direction="write"
                ),
                "post": convert_and_respect_annotation_metadata(object_=post, annotation=Post, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    def update_draft_post(
        self,
        name: str,
        *,
        content: ContentUpdateParam,
        post: Post,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Post]:
        """
        Update post metadata, spec, and content in one request.

        Parameters
        ----------
        name : str
            metadata.name of the post to update.

        content : ContentUpdateParam

        post : Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}",
            method="PUT",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=ContentUpdateParam, direction="write"
                ),
                "post": convert_and_respect_annotation_metadata(object_=post, annotation=Post, direction="write"),
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
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    def fetch_post_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentWrapper]:
        """
        Fetch a post content snapshot reconstructed from its base snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/content",
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

    def update_post_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        raw_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Post]:
        """
        Update only the content of an existing post.

        Parameters
        ----------
        name : str
            metadata.name of the post whose content will be updated.

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
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/content",
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
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    def delete_post_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentWrapper]:
        """
        Delete a content snapshot from a post and return the deleted content.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/content",
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

    def fetch_post_head_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentWrapper]:
        """
        Fetch the editable head content of a post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentWrapper]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/head-content",
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

    def publish_post(
        self,
        name: str,
        *,
        head_snapshot: typing.Optional[str] = None,
        async_: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Post]:
        """
        Publish a post. By default, the request waits until the release snapshot is available.

        Parameters
        ----------
        name : str
            metadata.name of the post to publish.

        head_snapshot : typing.Optional[str]
            Snapshot metadata.name to publish. Defaults to the current base snapshot when no head snapshot exists.

        async_ : typing.Optional[bool]
            Whether to return immediately after marking the post for publishing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/publish",
            method="PUT",
            params={
                "headSnapshot": head_snapshot,
                "async": async_,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    def recycle_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Post]:
        """
        Move a post to the recycle bin by marking it as deleted.

        Parameters
        ----------
        name : str
            metadata.name of the post to recycle.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/recycle",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    def fetch_post_release_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ContentWrapper]:
        """
        Fetch the released content currently served for a published post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ContentWrapper]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/release-content",
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

    def revert_to_specified_snapshot_for_post(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Post]:
        """
        Restore the post content from a specified snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the post whose content will be restored.

        snapshot_name : str
            snapshot <code>metadata.name</code> to restore as the post's head content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/revert-content",
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
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    def list_post_snapshots(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[ListedSnapshotDto]]:
        """
        List content snapshots for a post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ListedSnapshotDto]]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/snapshot",
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

    def unpublish_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Post]:
        """
        Unpublish a post so it is no longer served as published content.

        Parameters
        ----------
        name : str
            metadata.name of the post to unpublish.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/unpublish",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Post,
                    parse_obj_as(
                        type_=Post,
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


class AsyncRawPostV1Alpha1ConsoleClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_posts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListPostsRequestPublishPhase] = None,
        keyword: typing.Optional[str] = None,
        category_with_children: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListedPostList]:
        """
        List posts with pagination, sorting, keyword, publish phase, and category filters.

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

        publish_phase : typing.Optional[ListPostsRequestPublishPhase]
            Filter posts by publish phase. Supported values follow PostPhase, such as DRAFT, PENDING_APPROVAL, PUBLISHED, or FAILED.

        keyword : typing.Optional[str]
            Keyword used to match post title, slug, or excerpt.

        category_with_children : typing.Optional[str]
            Category metadata name used to include posts in that category and its child categories.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListedPostList]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/posts",
            method="GET",
            params={
                "page": page,
                "size": size,
                "labelSelector": label_selector,
                "fieldSelector": field_selector,
                "sort": sort,
                "publishPhase": publish_phase,
                "keyword": keyword,
                "categoryWithChildren": category_with_children,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListedPostList,
                    parse_obj_as(
                        type_=ListedPostList,
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

    async def draft_post(
        self, *, content: ContentUpdateParam, post: Post, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Post]:
        """
        Create a draft post together with its initial content.

        Parameters
        ----------
        content : ContentUpdateParam

        post : Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/api.console.halo.run/v1alpha1/posts",
            method="POST",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=ContentUpdateParam, direction="write"
                ),
                "post": convert_and_respect_annotation_metadata(object_=post, annotation=Post, direction="write"),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    async def update_draft_post(
        self,
        name: str,
        *,
        content: ContentUpdateParam,
        post: Post,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Post]:
        """
        Update post metadata, spec, and content in one request.

        Parameters
        ----------
        name : str
            metadata.name of the post to update.

        content : ContentUpdateParam

        post : Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}",
            method="PUT",
            json={
                "content": convert_and_respect_annotation_metadata(
                    object_=content, annotation=ContentUpdateParam, direction="write"
                ),
                "post": convert_and_respect_annotation_metadata(object_=post, annotation=Post, direction="write"),
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
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    async def fetch_post_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentWrapper]:
        """
        Fetch a post content snapshot reconstructed from its base snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/content",
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

    async def update_post_content(
        self,
        name: str,
        *,
        content: str,
        raw: str,
        raw_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Post]:
        """
        Update only the content of an existing post.

        Parameters
        ----------
        name : str
            metadata.name of the post whose content will be updated.

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
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/content",
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
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    async def delete_post_content(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentWrapper]:
        """
        Delete a content snapshot from a post and return the deleted content.

        Parameters
        ----------
        name : str
            metadata.name of the post.

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
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/content",
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

    async def fetch_post_head_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentWrapper]:
        """
        Fetch the editable head content of a post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentWrapper]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/head-content",
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

    async def publish_post(
        self,
        name: str,
        *,
        head_snapshot: typing.Optional[str] = None,
        async_: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Post]:
        """
        Publish a post. By default, the request waits until the release snapshot is available.

        Parameters
        ----------
        name : str
            metadata.name of the post to publish.

        head_snapshot : typing.Optional[str]
            Snapshot metadata.name to publish. Defaults to the current base snapshot when no head snapshot exists.

        async_ : typing.Optional[bool]
            Whether to return immediately after marking the post for publishing.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/publish",
            method="PUT",
            params={
                "headSnapshot": head_snapshot,
                "async": async_,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    async def recycle_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Post]:
        """
        Move a post to the recycle bin by marking it as deleted.

        Parameters
        ----------
        name : str
            metadata.name of the post to recycle.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/recycle",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    async def fetch_post_release_content(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ContentWrapper]:
        """
        Fetch the released content currently served for a published post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ContentWrapper]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/release-content",
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

    async def revert_to_specified_snapshot_for_post(
        self, name: str, *, snapshot_name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Post]:
        """
        Restore the post content from a specified snapshot.

        Parameters
        ----------
        name : str
            metadata.name of the post whose content will be restored.

        snapshot_name : str
            snapshot <code>metadata.name</code> to restore as the post's head content

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/revert-content",
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
                    Post,
                    parse_obj_as(
                        type_=Post,
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

    async def list_post_snapshots(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[ListedSnapshotDto]]:
        """
        List content snapshots for a post.

        Parameters
        ----------
        name : str
            metadata.name of the post.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ListedSnapshotDto]]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/snapshot",
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

    async def unpublish_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Post]:
        """
        Unpublish a post so it is no longer served as published content.

        Parameters
        ----------
        name : str
            metadata.name of the post to unpublish.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/api.console.halo.run/v1alpha1/posts/{encode_path_param(name)}/unpublish",
            method="PUT",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Post,
                    parse_obj_as(
                        type_=Post,
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
