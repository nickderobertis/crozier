

import json
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param, jsonable_encoder
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.endpoint_get_messages_id import EndpointGetMessagesId
from ..types.endpoint_get_messages_id_metadata import EndpointGetMessagesIdMetadata
from ..types.endpoint_get_messages_id_metadata_collections import EndpointGetMessagesIdMetadataCollections
from ..types.endpoint_post_messages_id_metadata import EndpointPostMessagesIdMetadata
from ..types.endpoint_post_messages_metadata_filters import EndpointPostMessagesMetadataFilters
from .types.post_messages_id_metadata_request_metadata0privacy import PostMessagesIdMetadataRequestMetadata0Privacy
from .types.post_messages_id_metadata_request_metadata1privacy import PostMessagesIdMetadataRequestMetadata1Privacy
from .types.post_messages_id_metadata_request_metadata2privacy import PostMessagesIdMetadataRequestMetadata2Privacy
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawMessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def post_messages_metadata_filters(
        self,
        *,
        limit: typing.Optional[int] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostMessagesMetadataFilters]:
        """
        Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

        Parameters
        ----------
        limit : typing.Optional[int]

        metadata0key : typing.Optional[str]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2values : typing.Optional[typing.List[str]]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostMessagesMetadataFilters]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "messages/metadata/filters",
            method="POST",
            data={
                "limit": limit,
                "metadata_0_key": metadata0key,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
                "offset": offset,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostMessagesMetadataFilters,
                    parse_obj_as(
                        type_=EndpointPostMessagesMetadataFilters,
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

    def get_messages_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointGetMessagesId]:
        """
        Fetch an array of messages. You can only retrieve messages authored by you or by users who exist within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetMessagesId]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetMessagesId,
                    parse_obj_as(
                        type_=EndpointGetMessagesId,
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

    def get_messages_id_metadata(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointGetMessagesIdMetadata]:
        """
        Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

        Parameters
        ----------
        id : int

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetMessagesIdMetadata]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(id)}/metadata",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetMessagesIdMetadata,
                    parse_obj_as(
                        type_=EndpointGetMessagesIdMetadata,
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

    def post_messages_id_metadata(
        self,
        id: int,
        *,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostMessagesIdMetadataRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostMessagesIdMetadataRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostMessagesIdMetadataRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EndpointPostMessagesIdMetadata]:
        """
        Attach one-to-many key/value pairs of metadata to a message, so long as the user who authored the message exists within the current access token's bubble. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by you or the other user in the message's conversation, using an access token which grants you access to the user who authored the message, if it wasn't you; Bubbled metadata by you or the other user in the message's conversation, using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message, if it wasn't you; Private metadata by you, so long as you are using an access token existing within the current bubble.

        Parameters
        ----------
        id : int

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostMessagesIdMetadataRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostMessagesIdMetadataRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostMessagesIdMetadataRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointPostMessagesIdMetadata]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(id)}/metadata",
            method="POST",
            data={
                "metadata_0_key": metadata0key,
                "metadata_0_privacy": metadata0privacy,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_privacy": metadata1privacy,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_privacy": metadata2privacy,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostMessagesIdMetadata,
                    parse_obj_as(
                        type_=EndpointPostMessagesIdMetadata,
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

    def get_messages_id_metadata_collections(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EndpointGetMessagesIdMetadataCollections]:
        """
        Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EndpointGetMessagesIdMetadataCollections]
            Valid Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(id)}/metadata/collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetMessagesIdMetadataCollections,
                    parse_obj_as(
                        type_=EndpointGetMessagesIdMetadataCollections,
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


class AsyncRawMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def post_messages_metadata_filters(
        self,
        *,
        limit: typing.Optional[int] = OMIT,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        offset: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostMessagesMetadataFilters]:
        """
        Paginated listing of messages filtered by arbitrary metadata criteria. Messages must match on all key/value pairs passed in. Messages may only match on one value of an array passed in. However, messages are sorted based on how many distinct values they match on (most matches first).

        Parameters
        ----------
        limit : typing.Optional[int]

        metadata0key : typing.Optional[str]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2values : typing.Optional[typing.List[str]]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostMessagesMetadataFilters]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "messages/metadata/filters",
            method="POST",
            data={
                "limit": limit,
                "metadata_0_key": metadata0key,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
                "offset": offset,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostMessagesMetadataFilters,
                    parse_obj_as(
                        type_=EndpointPostMessagesMetadataFilters,
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

    async def get_messages_id(
        self, id: typing.Sequence[int], *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointGetMessagesId]:
        """
        Fetch an array of messages. You can only retrieve messages authored by you or by users who exist within the current access token's bubble.

        Parameters
        ----------
        id : typing.Sequence[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetMessagesId]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetMessagesId,
                    parse_obj_as(
                        type_=EndpointGetMessagesId,
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

    async def get_messages_id_metadata(
        self,
        id: int,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointGetMessagesIdMetadata]:
        """
        Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble.

        Parameters
        ----------
        id : int

        offset : typing.Optional[int]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetMessagesIdMetadata]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(id)}/metadata",
            method="GET",
            params={
                "offset": offset,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetMessagesIdMetadata,
                    parse_obj_as(
                        type_=EndpointGetMessagesIdMetadata,
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

    async def post_messages_id_metadata(
        self,
        id: int,
        *,
        metadata0key: typing.Optional[str] = OMIT,
        metadata0privacy: typing.Optional[PostMessagesIdMetadataRequestMetadata0Privacy] = OMIT,
        metadata0values: typing.Optional[typing.List[str]] = OMIT,
        metadata1key: typing.Optional[str] = OMIT,
        metadata1privacy: typing.Optional[PostMessagesIdMetadataRequestMetadata1Privacy] = OMIT,
        metadata1values: typing.Optional[typing.List[str]] = OMIT,
        metadata2key: typing.Optional[str] = OMIT,
        metadata2privacy: typing.Optional[PostMessagesIdMetadataRequestMetadata2Privacy] = OMIT,
        metadata2values: typing.Optional[typing.List[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EndpointPostMessagesIdMetadata]:
        """
        Attach one-to-many key/value pairs of metadata to a message, so long as the user who authored the message exists within the current access token's bubble. A key is unique for each author/bubble combination. Attaching metadata with an existing key that was previously created by you, from within the same bubble, overwrites the key with the new value or set of values. The privacy setting allows you to specify who will have access to the metadata: Public metadata by you or the other user in the message's conversation, using an access token which grants you access to the user who authored the message, if it wasn't you; Bubbled metadata by you or the other user in the message's conversation, using an access token existing within the current bubble; User metadata by you, so long as you are using an access token which grants you access to the user who authored the message, if it wasn't you; Private metadata by you, so long as you are using an access token existing within the current bubble.

        Parameters
        ----------
        id : int

        metadata0key : typing.Optional[str]

        metadata0privacy : typing.Optional[PostMessagesIdMetadataRequestMetadata0Privacy]

        metadata0values : typing.Optional[typing.List[str]]

        metadata1key : typing.Optional[str]

        metadata1privacy : typing.Optional[PostMessagesIdMetadataRequestMetadata1Privacy]

        metadata1values : typing.Optional[typing.List[str]]

        metadata2key : typing.Optional[str]

        metadata2privacy : typing.Optional[PostMessagesIdMetadataRequestMetadata2Privacy]

        metadata2values : typing.Optional[typing.List[str]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointPostMessagesIdMetadata]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(id)}/metadata",
            method="POST",
            data={
                "metadata_0_key": metadata0key,
                "metadata_0_privacy": metadata0privacy,
                "metadata_0_values[]": json.dumps(jsonable_encoder(metadata0values))
                if metadata0values is not OMIT
                else OMIT,
                "metadata_1_key": metadata1key,
                "metadata_1_privacy": metadata1privacy,
                "metadata_1_values[]": json.dumps(jsonable_encoder(metadata1values))
                if metadata1values is not OMIT
                else OMIT,
                "metadata_2_key": metadata2key,
                "metadata_2_privacy": metadata2privacy,
                "metadata_2_values[]": json.dumps(jsonable_encoder(metadata2values))
                if metadata2values is not OMIT
                else OMIT,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointPostMessagesIdMetadata,
                    parse_obj_as(
                        type_=EndpointPostMessagesIdMetadata,
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

    async def get_messages_id_metadata_collections(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EndpointGetMessagesIdMetadataCollections]:
        """
        Retrieve all key/value pairs attached to the current message that you have access to, so long as the user who authored the message exists within the current access token's bubble. This includes all public metadata, bubbled metadata that was created by an access token existing within the current bubble, user metadata that was created by you, or private metadata created by you from an access token existing within the current bubble. Metadata will be grouped by key.

        Parameters
        ----------
        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EndpointGetMessagesIdMetadataCollections]
            Valid Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{encode_path_param(id)}/metadata/collections",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EndpointGetMessagesIdMetadataCollections,
                    parse_obj_as(
                        type_=EndpointGetMessagesIdMetadataCollections,
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
