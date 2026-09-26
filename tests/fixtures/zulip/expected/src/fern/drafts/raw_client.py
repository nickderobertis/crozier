

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
from ..errors.bad_request_error import BadRequestError
from ..errors.not_found_error import NotFoundError
from ..types.draft import Draft
from ..types.json_success import JsonSuccess
from .types.create_drafts_response import CreateDraftsResponse
from .types.create_saved_snippet_response import CreateSavedSnippetResponse
from .types.edit_draft_request_draft import EditDraftRequestDraft
from .types.get_drafts_response import GetDraftsResponse
from .types.get_saved_snippets_response import GetSavedSnippetsResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDraftsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_drafts(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[GetDraftsResponse]:
        """
        Fetch all drafts for the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetDraftsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "drafts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDraftsResponse,
                    parse_obj_as(
                        type_=GetDraftsResponse,
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

    def create_drafts(
        self,
        *,
        drafts: typing.Optional[typing.Sequence[Draft]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateDraftsResponse]:
        """
        Create one or more drafts on the server. These drafts will be automatically
        synchronized to other clients via `drafts` events.

        Parameters
        ----------
        drafts : typing.Optional[typing.Sequence[Draft]]
            A JSON-encoded list of containing new draft objects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateDraftsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "drafts",
            method="POST",
            data={
                "drafts": convert_and_respect_annotation_metadata(
                    object_=drafts, annotation=typing.Sequence[Draft], direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDraftsResponse,
                    parse_obj_as(
                        type_=CreateDraftsResponse,
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

    def delete_draft(
        self, draft_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Delete a single draft from the server. The deletion will be automatically
        synchronized to other clients via a `drafts` event.

        Parameters
        ----------
        draft_id : int
            The ID of the draft you want to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"drafts/{encode_path_param(draft_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def edit_draft(
        self, draft_id: int, *, draft: EditDraftRequestDraft, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Edit a draft on the server. The edit will be automatically
        synchronized to other clients via `drafts` events.

        Parameters
        ----------
        draft_id : int
            The ID of the draft to be edited.

        draft : EditDraftRequestDraft
            A JSON-encoded object containing a replacement draft object for this ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"drafts/{encode_path_param(draft_id)}",
            method="PATCH",
            data={
                "draft": convert_and_respect_annotation_metadata(
                    object_=draft, annotation=EditDraftRequestDraft, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def get_saved_snippets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetSavedSnippetsResponse]:
        """
        Fetch all the saved snippets for the current user.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetSavedSnippetsResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "saved_snippets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSavedSnippetsResponse,
                    parse_obj_as(
                        type_=GetSavedSnippetsResponse,
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

    def create_saved_snippet(
        self, *, title: str, content: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CreateSavedSnippetResponse]:
        """
        Create a new saved snippet for the current user.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        title : str
            The title of the saved snippet.

        content : str
            The content of the saved snippet in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should insert this content into a message when using
            a saved snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateSavedSnippetResponse]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            "saved_snippets",
            method="POST",
            data={
                "title": title,
                "content": content,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateSavedSnippetResponse,
                    parse_obj_as(
                        type_=CreateSavedSnippetResponse,
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

    def delete_saved_snippet(
        self, saved_snippet_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[JsonSuccess]:
        """
        Delete a saved snippet.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        saved_snippet_id : int
            The ID of the saved snippet to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"saved_snippets/{encode_path_param(saved_snippet_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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

    def edit_saved_snippet(
        self,
        saved_snippet_id: int,
        *,
        title: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[JsonSuccess]:
        """
        Edit a saved snippet for the current user.

        **Changes**: New in Zulip 10.0 (feature level 368).

        Parameters
        ----------
        saved_snippet_id : int
            The ID of the saved snippet to edit.

        title : typing.Optional[str]
            The title of the saved snippet.

        content : typing.Optional[str]
            The content of the saved snippet in the original [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should insert this content into a message when using
            a saved snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[JsonSuccess]
            Success.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"saved_snippets/{encode_path_param(saved_snippet_id)}",
            method="PATCH",
            data={
                "title": title,
                "content": content,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
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


class AsyncRawDraftsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_drafts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetDraftsResponse]:
        """
        Fetch all drafts for the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetDraftsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "drafts",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetDraftsResponse,
                    parse_obj_as(
                        type_=GetDraftsResponse,
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

    async def create_drafts(
        self,
        *,
        drafts: typing.Optional[typing.Sequence[Draft]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateDraftsResponse]:
        """
        Create one or more drafts on the server. These drafts will be automatically
        synchronized to other clients via `drafts` events.

        Parameters
        ----------
        drafts : typing.Optional[typing.Sequence[Draft]]
            A JSON-encoded list of containing new draft objects.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateDraftsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "drafts",
            method="POST",
            data={
                "drafts": convert_and_respect_annotation_metadata(
                    object_=drafts, annotation=typing.Sequence[Draft], direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateDraftsResponse,
                    parse_obj_as(
                        type_=CreateDraftsResponse,
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

    async def delete_draft(
        self, draft_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Delete a single draft from the server. The deletion will be automatically
        synchronized to other clients via a `drafts` event.

        Parameters
        ----------
        draft_id : int
            The ID of the draft you want to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"drafts/{encode_path_param(draft_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def edit_draft(
        self, draft_id: int, *, draft: EditDraftRequestDraft, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Edit a draft on the server. The edit will be automatically
        synchronized to other clients via `drafts` events.

        Parameters
        ----------
        draft_id : int
            The ID of the draft to be edited.

        draft : EditDraftRequestDraft
            A JSON-encoded object containing a replacement draft object for this ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"drafts/{encode_path_param(draft_id)}",
            method="PATCH",
            data={
                "draft": convert_and_respect_annotation_metadata(
                    object_=draft, annotation=EditDraftRequestDraft, direction="write"
                ),
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def get_saved_snippets(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetSavedSnippetsResponse]:
        """
        Fetch all the saved snippets for the current user.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetSavedSnippetsResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "saved_snippets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetSavedSnippetsResponse,
                    parse_obj_as(
                        type_=GetSavedSnippetsResponse,
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

    async def create_saved_snippet(
        self, *, title: str, content: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CreateSavedSnippetResponse]:
        """
        Create a new saved snippet for the current user.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        title : str
            The title of the saved snippet.

        content : str
            The content of the saved snippet in [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should insert this content into a message when using
            a saved snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateSavedSnippetResponse]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "saved_snippets",
            method="POST",
            data={
                "title": title,
                "content": content,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateSavedSnippetResponse,
                    parse_obj_as(
                        type_=CreateSavedSnippetResponse,
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

    async def delete_saved_snippet(
        self, saved_snippet_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Delete a saved snippet.

        **Changes**: New in Zulip 10.0 (feature level 297).

        Parameters
        ----------
        saved_snippet_id : int
            The ID of the saved snippet to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"saved_snippets/{encode_path_param(saved_snippet_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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

    async def edit_saved_snippet(
        self,
        saved_snippet_id: int,
        *,
        title: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[JsonSuccess]:
        """
        Edit a saved snippet for the current user.

        **Changes**: New in Zulip 10.0 (feature level 368).

        Parameters
        ----------
        saved_snippet_id : int
            The ID of the saved snippet to edit.

        title : typing.Optional[str]
            The title of the saved snippet.

        content : typing.Optional[str]
            The content of the saved snippet in the original [Zulip-flavored Markdown](/help/format-your-message-using-markdown) format.

            Clients should insert this content into a message when using
            a saved snippet.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[JsonSuccess]
            Success.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"saved_snippets/{encode_path_param(saved_snippet_id)}",
            method="PATCH",
            data={
                "title": title,
                "content": content,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    JsonSuccess,
                    parse_obj_as(
                        type_=JsonSuccess,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
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
