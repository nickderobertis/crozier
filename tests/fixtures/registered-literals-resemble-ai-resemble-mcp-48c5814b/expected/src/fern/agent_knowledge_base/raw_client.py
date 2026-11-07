

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.error import Error
from .types.attach_knowledge_item_to_agent_response import AttachKnowledgeItemToAgentResponse
from .types.create_knowledge_item_request_source_type import CreateKnowledgeItemRequestSourceType
from .types.create_knowledge_item_response import CreateKnowledgeItemResponse
from .types.delete_knowledge_item_response import DeleteKnowledgeItemResponse
from .types.detach_knowledge_item_from_agent_response import DetachKnowledgeItemFromAgentResponse
from .types.get_knowledge_item_response import GetKnowledgeItemResponse
from .types.list_agent_knowledge_items_response import ListAgentKnowledgeItemsResponse
from .types.list_knowledge_items_request_source_type import ListKnowledgeItemsRequestSourceType
from .types.list_knowledge_items_request_status import ListKnowledgeItemsRequestStatus
from .types.list_knowledge_items_response import ListKnowledgeItemsResponse
from .types.reingest_knowledge_item_response import ReingestKnowledgeItemResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAgentKnowledgeBaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_knowledge_items(
        self,
        *,
        status: typing.Optional[ListKnowledgeItemsRequestStatus] = None,
        source_type: typing.Optional[ListKnowledgeItemsRequestSourceType] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListKnowledgeItemsResponse]:
        """
        List all knowledge items belonging to the authenticated user's team

        Parameters
        ----------
        status : typing.Optional[ListKnowledgeItemsRequestStatus]
            Filter by status

        source_type : typing.Optional[ListKnowledgeItemsRequestSourceType]
            Filter by source type

        page : typing.Optional[int]
            Page number

        per_page : typing.Optional[int]
            Items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListKnowledgeItemsResponse]
            List of knowledge items
        """
        _response = self._client_wrapper.httpx_client.request(
            "knowledge_items",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "status": status,
                "source_type": source_type,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListKnowledgeItemsResponse,
                    parse_obj_as(
                        type_=ListKnowledgeItemsResponse,
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

    def create_knowledge_item(
        self,
        *,
        title: str,
        description: str,
        source_type: CreateKnowledgeItemRequestSourceType,
        url: typing.Optional[str] = OMIT,
        raw_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateKnowledgeItemResponse]:
        """
        Creates a new knowledge item and queues it for ingestion processing

        Parameters
        ----------
        title : str
            Title of the knowledge item

        description : str
            Description of the knowledge item

        source_type : CreateKnowledgeItemRequestSourceType
            Type of knowledge source

        url : typing.Optional[str]
            Required when source_type is url

        raw_text : typing.Optional[str]
            Required when source_type is text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateKnowledgeItemResponse]
            Knowledge item created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "knowledge_items",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "title": title,
                "description": description,
                "source_type": source_type,
                "url": url,
                "raw_text": raw_text,
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
                    CreateKnowledgeItemResponse,
                    parse_obj_as(
                        type_=CreateKnowledgeItemResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def get_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetKnowledgeItemResponse]:
        """
        Retrieves a single knowledge item with detailed information including attached agents

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetKnowledgeItemResponse]
            Knowledge item details
        """
        _response = self._client_wrapper.httpx_client.request(
            f"knowledge_items/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetKnowledgeItemResponse,
                    parse_obj_as(
                        type_=GetKnowledgeItemResponse,
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

    def delete_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteKnowledgeItemResponse]:
        """
        Deletes a knowledge item and cleans up associated data

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteKnowledgeItemResponse]
            Knowledge item deleted successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"knowledge_items/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteKnowledgeItemResponse,
                    parse_obj_as(
                        type_=DeleteKnowledgeItemResponse,
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

    def reingest_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ReingestKnowledgeItemResponse]:
        """
        Re-runs the ingestion pipeline for an existing knowledge item

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ReingestKnowledgeItemResponse]
            Re-ingestion queued successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"knowledge_items/{encode_path_param(uuid_)}/reingest",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReingestKnowledgeItemResponse,
                    parse_obj_as(
                        type_=ReingestKnowledgeItemResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def list_agent_knowledge_items(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListAgentKnowledgeItemsResponse]:
        """
        Lists all knowledge items attached to a specific agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAgentKnowledgeItemsResponse]
            List of knowledge items attached to agent
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/knowledge_items",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAgentKnowledgeItemsResponse,
                    parse_obj_as(
                        type_=ListAgentKnowledgeItemsResponse,
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

    def attach_knowledge_item_to_agent(
        self, agent_uuid: str, *, knowledge_item_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AttachKnowledgeItemToAgentResponse]:
        """
        Attaches an existing knowledge item to an agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        knowledge_item_uuid : str
            The UUID of the knowledge item to attach

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AttachKnowledgeItemToAgentResponse]
            Knowledge item attached successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/knowledge_items",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "knowledge_item_uuid": knowledge_item_uuid,
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
                    AttachKnowledgeItemToAgentResponse,
                    parse_obj_as(
                        type_=AttachKnowledgeItemToAgentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def detach_knowledge_item_from_agent(
        self, agent_uuid: str, knowledge_item_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DetachKnowledgeItemFromAgentResponse]:
        """
        Removes a knowledge item from an agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        knowledge_item_uuid : str
            The UUID of the knowledge item to detach

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DetachKnowledgeItemFromAgentResponse]
            Knowledge item detached successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/knowledge_items/{encode_path_param(knowledge_item_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DetachKnowledgeItemFromAgentResponse,
                    parse_obj_as(
                        type_=DetachKnowledgeItemFromAgentResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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


class AsyncRawAgentKnowledgeBaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_knowledge_items(
        self,
        *,
        status: typing.Optional[ListKnowledgeItemsRequestStatus] = None,
        source_type: typing.Optional[ListKnowledgeItemsRequestSourceType] = None,
        page: typing.Optional[int] = None,
        per_page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListKnowledgeItemsResponse]:
        """
        List all knowledge items belonging to the authenticated user's team

        Parameters
        ----------
        status : typing.Optional[ListKnowledgeItemsRequestStatus]
            Filter by status

        source_type : typing.Optional[ListKnowledgeItemsRequestSourceType]
            Filter by source type

        page : typing.Optional[int]
            Page number

        per_page : typing.Optional[int]
            Items per page

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListKnowledgeItemsResponse]
            List of knowledge items
        """
        _response = await self._client_wrapper.httpx_client.request(
            "knowledge_items",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            params={
                "status": status,
                "source_type": source_type,
                "page": page,
                "per_page": per_page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListKnowledgeItemsResponse,
                    parse_obj_as(
                        type_=ListKnowledgeItemsResponse,
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

    async def create_knowledge_item(
        self,
        *,
        title: str,
        description: str,
        source_type: CreateKnowledgeItemRequestSourceType,
        url: typing.Optional[str] = OMIT,
        raw_text: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateKnowledgeItemResponse]:
        """
        Creates a new knowledge item and queues it for ingestion processing

        Parameters
        ----------
        title : str
            Title of the knowledge item

        description : str
            Description of the knowledge item

        source_type : CreateKnowledgeItemRequestSourceType
            Type of knowledge source

        url : typing.Optional[str]
            Required when source_type is url

        raw_text : typing.Optional[str]
            Required when source_type is text

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateKnowledgeItemResponse]
            Knowledge item created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "knowledge_items",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "title": title,
                "description": description,
                "source_type": source_type,
                "url": url,
                "raw_text": raw_text,
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
                    CreateKnowledgeItemResponse,
                    parse_obj_as(
                        type_=CreateKnowledgeItemResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def get_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetKnowledgeItemResponse]:
        """
        Retrieves a single knowledge item with detailed information including attached agents

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetKnowledgeItemResponse]
            Knowledge item details
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"knowledge_items/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetKnowledgeItemResponse,
                    parse_obj_as(
                        type_=GetKnowledgeItemResponse,
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

    async def delete_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteKnowledgeItemResponse]:
        """
        Deletes a knowledge item and cleans up associated data

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteKnowledgeItemResponse]
            Knowledge item deleted successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"knowledge_items/{encode_path_param(uuid_)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteKnowledgeItemResponse,
                    parse_obj_as(
                        type_=DeleteKnowledgeItemResponse,
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

    async def reingest_knowledge_item(
        self, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ReingestKnowledgeItemResponse]:
        """
        Re-runs the ingestion pipeline for an existing knowledge item

        Parameters
        ----------
        uuid_ : str
            The UUID of the knowledge item

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ReingestKnowledgeItemResponse]
            Re-ingestion queued successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"knowledge_items/{encode_path_param(uuid_)}/reingest",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ReingestKnowledgeItemResponse,
                    parse_obj_as(
                        type_=ReingestKnowledgeItemResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def list_agent_knowledge_items(
        self, agent_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListAgentKnowledgeItemsResponse]:
        """
        Lists all knowledge items attached to a specific agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAgentKnowledgeItemsResponse]
            List of knowledge items attached to agent
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/knowledge_items",
            base_url=self._client_wrapper.get_environment().base,
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAgentKnowledgeItemsResponse,
                    parse_obj_as(
                        type_=ListAgentKnowledgeItemsResponse,
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

    async def attach_knowledge_item_to_agent(
        self, agent_uuid: str, *, knowledge_item_uuid: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AttachKnowledgeItemToAgentResponse]:
        """
        Attaches an existing knowledge item to an agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        knowledge_item_uuid : str
            The UUID of the knowledge item to attach

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AttachKnowledgeItemToAgentResponse]
            Knowledge item attached successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/knowledge_items",
            base_url=self._client_wrapper.get_environment().base,
            method="POST",
            json={
                "knowledge_item_uuid": knowledge_item_uuid,
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
                    AttachKnowledgeItemToAgentResponse,
                    parse_obj_as(
                        type_=AttachKnowledgeItemToAgentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def detach_knowledge_item_from_agent(
        self, agent_uuid: str, knowledge_item_uuid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DetachKnowledgeItemFromAgentResponse]:
        """
        Removes a knowledge item from an agent

        Parameters
        ----------
        agent_uuid : str
            The UUID of the agent

        knowledge_item_uuid : str
            The UUID of the knowledge item to detach

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DetachKnowledgeItemFromAgentResponse]
            Knowledge item detached successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"agents/{encode_path_param(agent_uuid)}/knowledge_items/{encode_path_param(knowledge_item_uuid)}",
            base_url=self._client_wrapper.get_environment().base,
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DetachKnowledgeItemFromAgentResponse,
                    parse_obj_as(
                        type_=DetachKnowledgeItemFromAgentResponse,
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
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
