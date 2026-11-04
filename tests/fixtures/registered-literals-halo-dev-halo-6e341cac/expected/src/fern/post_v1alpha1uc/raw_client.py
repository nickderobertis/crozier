

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
from ..types.listed_post_list import ListedPostList
from ..types.metadata import Metadata
from ..types.post import Post
from ..types.post_spec import PostSpec
from ..types.post_status import PostStatus
from ..types.snap_shot_spec import SnapShotSpec
from ..types.snapshot import Snapshot
from .types.list_my_posts_request_publish_phase import ListMyPostsRequestPublishPhase
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPostV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_my_posts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListMyPostsRequestPublishPhase] = None,
        keyword: typing.Optional[str] = None,
        category_with_children: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListedPostList]:
        """
        List posts owned by the current user with pagination, sorting, keyword, publish phase, and category filters.

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

        publish_phase : typing.Optional[ListMyPostsRequestPublishPhase]
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
            "apis/uc.api.content.halo.run/v1alpha1/posts",
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

    def create_my_post(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: PostSpec,
        status: typing.Optional[PostStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Post]:
        """
        Create a draft post for the current user. To create it with initial content, put JSON-serialized Content into metadata.annotations['content.halo.run/content-json'].

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : PostSpec

        status : typing.Optional[PostStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            "apis/uc.api.content.halo.run/v1alpha1/posts",
            method="POST",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=PostSpec, direction="write"),
                "status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=PostStatus, direction="write"
                ),
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

    def get_my_post(self, name: str, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Post]:
        """
        Get a post owned by the current user by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}",
            method="GET",
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

    def update_my_post(
        self,
        name: str,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: PostSpec,
        status: typing.Optional[PostStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Post]:
        """
        Update post metadata and editable spec fields for the current user. Content is not updated by this operation.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        api_version : str

        kind : str

        metadata : Metadata

        spec : PostSpec

        status : typing.Optional[PostStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}",
            method="PUT",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=PostSpec, direction="write"),
                "status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=PostStatus, direction="write"
                ),
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

    def get_my_post_draft(
        self,
        name: str,
        *,
        patched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Snapshot]:
        """
        Get the editable draft snapshot of a post owned by the current user.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        patched : typing.Optional[bool]
            Whether to return the head snapshot patched against the base snapshot. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Snapshot]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/draft",
            method="GET",
            params={
                "patched": patched,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Snapshot,
                    parse_obj_as(
                        type_=Snapshot,
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

    def update_my_post_draft(
        self,
        name: str,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: SnapShotSpec,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Snapshot]:
        """
        Update the editable draft snapshot of a post owned by the current user. The snapshot must belong to the post and must be the current head snapshot.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        api_version : str

        kind : str

        metadata : Metadata

        spec : SnapShotSpec

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Snapshot]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/draft",
            method="PUT",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=SnapShotSpec, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Snapshot,
                    parse_obj_as(
                        type_=Snapshot,
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

    def publish_my_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Post]:
        """
        Publish a post owned by the current user from its current head snapshot.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/publish",
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

    def recycle_my_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Post]:
        """
        Move a post owned by the current user to the recycle bin.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/recycle",
            method="DELETE",
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

    def unpublish_my_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Post]:
        """
        Unpublish a post owned by the current user so it is no longer served as published content.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Post]
            default response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/unpublish",
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


class AsyncRawPostV1Alpha1UcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_my_posts(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        label_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        field_selector: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        sort: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        publish_phase: typing.Optional[ListMyPostsRequestPublishPhase] = None,
        keyword: typing.Optional[str] = None,
        category_with_children: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListedPostList]:
        """
        List posts owned by the current user with pagination, sorting, keyword, publish phase, and category filters.

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

        publish_phase : typing.Optional[ListMyPostsRequestPublishPhase]
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
            "apis/uc.api.content.halo.run/v1alpha1/posts",
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

    async def create_my_post(
        self,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: PostSpec,
        status: typing.Optional[PostStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Post]:
        """
        Create a draft post for the current user. To create it with initial content, put JSON-serialized Content into metadata.annotations['content.halo.run/content-json'].

        Parameters
        ----------
        api_version : str

        kind : str

        metadata : Metadata

        spec : PostSpec

        status : typing.Optional[PostStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "apis/uc.api.content.halo.run/v1alpha1/posts",
            method="POST",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=PostSpec, direction="write"),
                "status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=PostStatus, direction="write"
                ),
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

    async def get_my_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Post]:
        """
        Get a post owned by the current user by metadata.name.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}",
            method="GET",
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

    async def update_my_post(
        self,
        name: str,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: PostSpec,
        status: typing.Optional[PostStatus] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Post]:
        """
        Update post metadata and editable spec fields for the current user. Content is not updated by this operation.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        api_version : str

        kind : str

        metadata : Metadata

        spec : PostSpec

        status : typing.Optional[PostStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}",
            method="PUT",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(object_=spec, annotation=PostSpec, direction="write"),
                "status": convert_and_respect_annotation_metadata(
                    object_=status, annotation=PostStatus, direction="write"
                ),
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

    async def get_my_post_draft(
        self,
        name: str,
        *,
        patched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Snapshot]:
        """
        Get the editable draft snapshot of a post owned by the current user.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        patched : typing.Optional[bool]
            Whether to return the head snapshot patched against the base snapshot. Defaults to false.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Snapshot]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/draft",
            method="GET",
            params={
                "patched": patched,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Snapshot,
                    parse_obj_as(
                        type_=Snapshot,
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

    async def update_my_post_draft(
        self,
        name: str,
        *,
        api_version: str,
        kind: str,
        metadata: Metadata,
        spec: SnapShotSpec,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Snapshot]:
        """
        Update the editable draft snapshot of a post owned by the current user. The snapshot must belong to the post and must be the current head snapshot.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        api_version : str

        kind : str

        metadata : Metadata

        spec : SnapShotSpec

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Snapshot]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/draft",
            method="PUT",
            json={
                "apiVersion": api_version,
                "kind": kind,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=Metadata, direction="write"
                ),
                "spec": convert_and_respect_annotation_metadata(
                    object_=spec, annotation=SnapShotSpec, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Snapshot,
                    parse_obj_as(
                        type_=Snapshot,
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

    async def publish_my_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Post]:
        """
        Publish a post owned by the current user from its current head snapshot.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/publish",
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

    async def recycle_my_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Post]:
        """
        Move a post owned by the current user to the recycle bin.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/recycle",
            method="DELETE",
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

    async def unpublish_my_post(
        self, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Post]:
        """
        Unpublish a post owned by the current user so it is no longer served as published content.

        Parameters
        ----------
        name : str
            metadata.name of a post owned by the current user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Post]
            default response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"apis/uc.api.content.halo.run/v1alpha1/posts/{encode_path_param(name)}/unpublish",
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
