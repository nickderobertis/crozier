

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
from ..types.assistant_file_object import AssistantFileObject
from ..types.assistant_object import AssistantObject
from ..types.assistants_api_response_format_option import AssistantsApiResponseFormatOption
from ..types.assistants_api_tool_choice_option import AssistantsApiToolChoiceOption
from ..types.create_message_request import CreateMessageRequest
from ..types.create_message_request_role import CreateMessageRequestRole
from ..types.create_thread_request import CreateThreadRequest
from ..types.delete_assistant_file_response import DeleteAssistantFileResponse
from ..types.delete_assistant_response import DeleteAssistantResponse
from ..types.delete_thread_response import DeleteThreadResponse
from ..types.list_assistant_files_response import ListAssistantFilesResponse
from ..types.list_assistants_response import ListAssistantsResponse
from ..types.list_message_files_response import ListMessageFilesResponse
from ..types.list_messages_response import ListMessagesResponse
from ..types.list_run_steps_response import ListRunStepsResponse
from ..types.list_runs_response import ListRunsResponse
from ..types.message_file_object import MessageFileObject
from ..types.message_object import MessageObject
from ..types.run_object import RunObject
from ..types.run_step_object import RunStepObject
from ..types.thread_object import ThreadObject
from ..types.truncation_object import TruncationObject
from .types.create_assistant_request_model import CreateAssistantRequestModel
from .types.create_assistant_request_tools_item import CreateAssistantRequestToolsItem
from .types.create_run_request_model import CreateRunRequestModel
from .types.create_run_request_tools_item import CreateRunRequestToolsItem
from .types.create_thread_and_run_request_model import CreateThreadAndRunRequestModel
from .types.create_thread_and_run_request_tools_item import CreateThreadAndRunRequestToolsItem
from .types.list_assistant_files_request_order import ListAssistantFilesRequestOrder
from .types.list_assistants_request_order import ListAssistantsRequestOrder
from .types.list_message_files_request_order import ListMessageFilesRequestOrder
from .types.list_messages_request_order import ListMessagesRequestOrder
from .types.list_run_steps_request_order import ListRunStepsRequestOrder
from .types.list_runs_request_order import ListRunsRequestOrder
from .types.modify_assistant_request_tools_item import ModifyAssistantRequestToolsItem
from .types.submit_tool_outputs_run_request_tool_outputs_item import SubmitToolOutputsRunRequestToolOutputsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAssistantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_assistants(
        self,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAssistantsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAssistantsResponse]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListAssistantsRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAssistantsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assistants",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAssistantsResponse,
                    parse_obj_as(
                        type_=ListAssistantsResponse,
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

    def create_assistant(
        self,
        *,
        model: CreateAssistantRequestModel,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        tools: typing.Optional[typing.Sequence[CreateAssistantRequestToolsItem]] = OMIT,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AssistantObject]:
        """
        Parameters
        ----------
        model : CreateAssistantRequestModel
            ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

        name : typing.Optional[str]
            The name of the assistant. The maximum length is 256 characters.

        description : typing.Optional[str]
            The description of the assistant. The maximum length is 512 characters.

        instructions : typing.Optional[str]
            The system instructions that the assistant uses. The maximum length is 256,000 characters.

        tools : typing.Optional[typing.Sequence[CreateAssistantRequestToolsItem]]
            A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

        file_ids : typing.Optional[typing.Sequence[str]]
            A list of [file](/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AssistantObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assistants",
            method="POST",
            json={
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateAssistantRequestModel, direction="write"
                ),
                "name": name,
                "description": description,
                "instructions": instructions,
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Sequence[CreateAssistantRequestToolsItem], direction="write"
                ),
                "file_ids": file_ids,
                "metadata": metadata,
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
                    AssistantObject,
                    parse_obj_as(
                        type_=AssistantObject,
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

    def get_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AssistantObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AssistantObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssistantObject,
                    parse_obj_as(
                        type_=AssistantObject,
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

    def modify_assistant(
        self,
        assistant_id: str,
        *,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        tools: typing.Optional[typing.Sequence[ModifyAssistantRequestToolsItem]] = OMIT,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AssistantObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to modify.

        model : typing.Optional[str]
            ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

        name : typing.Optional[str]
            The name of the assistant. The maximum length is 256 characters.

        description : typing.Optional[str]
            The description of the assistant. The maximum length is 512 characters.

        instructions : typing.Optional[str]
            The system instructions that the assistant uses. The maximum length is 256,000 characters.

        tools : typing.Optional[typing.Sequence[ModifyAssistantRequestToolsItem]]
            A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

        file_ids : typing.Optional[typing.Sequence[str]]
            A list of [File](/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order. If a file was previously attached to the list but does not show up in the list, it will be deleted from the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AssistantObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="POST",
            json={
                "model": model,
                "name": name,
                "description": description,
                "instructions": instructions,
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Sequence[ModifyAssistantRequestToolsItem], direction="write"
                ),
                "file_ids": file_ids,
                "metadata": metadata,
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
                    AssistantObject,
                    parse_obj_as(
                        type_=AssistantObject,
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

    def delete_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteAssistantResponse]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteAssistantResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAssistantResponse,
                    parse_obj_as(
                        type_=DeleteAssistantResponse,
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

    def create_thread(
        self,
        *,
        messages: typing.Optional[typing.Sequence[CreateMessageRequest]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadObject]:
        """
        Parameters
        ----------
        messages : typing.Optional[typing.Sequence[CreateMessageRequest]]
            A list of [messages](/docs/api-reference/messages) to start the thread with.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "threads",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[CreateMessageRequest], direction="write"
                ),
                "metadata": metadata,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadObject,
                    parse_obj_as(
                        type_=ThreadObject,
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

    def get_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ThreadObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadObject,
                    parse_obj_as(
                        type_=ThreadObject,
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

    def modify_thread(
        self,
        thread_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ThreadObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to modify. Only the `metadata` can be modified.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ThreadObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="POST",
            json={
                "metadata": metadata,
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
                    ThreadObject,
                    parse_obj_as(
                        type_=ThreadObject,
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

    def delete_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteThreadResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteThreadResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteThreadResponse,
                    parse_obj_as(
                        type_=DeleteThreadResponse,
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

    def list_messages(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        run_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMessagesResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) the messages belong to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListMessagesRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        run_id : typing.Optional[str]
            Filter messages by the run ID that generated them.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMessagesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
                "run_id": run_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMessagesResponse,
                    parse_obj_as(
                        type_=ListMessagesResponse,
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

    def create_message(
        self,
        thread_id: str,
        *,
        role: CreateMessageRequestRole,
        content: str,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessageObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) to create a message for.

        role : CreateMessageRequestRole
            The role of the entity that is creating the message. Allowed values include:
            - `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
            - `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

        content : str
            The content of the message.

        file_ids : typing.Optional[typing.Sequence[str]]
            A list of [File](/docs/api-reference/files) IDs that the message should use. There can be a maximum of 10 files attached to a message. Useful for tools like `retrieval` and `code_interpreter` that can access and use files.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessageObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages",
            method="POST",
            json={
                "role": role,
                "content": content,
                "file_ids": file_ids,
                "metadata": metadata,
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
                    MessageObject,
                    parse_obj_as(
                        type_=MessageObject,
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

    def get_message(
        self, thread_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessageObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) to which this message belongs.

        message_id : str
            The ID of the message to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessageObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageObject,
                    parse_obj_as(
                        type_=MessageObject,
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

    def modify_message(
        self,
        thread_id: str,
        message_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MessageObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to which this message belongs.

        message_id : str
            The ID of the message to modify.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessageObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages/{encode_path_param(message_id)}",
            method="POST",
            json={
                "metadata": metadata,
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
                    MessageObject,
                    parse_obj_as(
                        type_=MessageObject,
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

    def create_thread_and_run(
        self,
        *,
        assistant_id: str,
        thread: typing.Optional[CreateThreadRequest] = OMIT,
        model: typing.Optional[CreateThreadAndRunRequestModel] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        tools: typing.Optional[typing.Sequence[CreateThreadAndRunRequestToolsItem]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        max_prompt_tokens: typing.Optional[int] = OMIT,
        max_completion_tokens: typing.Optional[int] = OMIT,
        truncation_strategy: typing.Optional[TruncationObject] = OMIT,
        tool_choice: typing.Optional[AssistantsApiToolChoiceOption] = OMIT,
        response_format: typing.Optional[AssistantsApiResponseFormatOption] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.

        thread : typing.Optional[CreateThreadRequest]
            If no thread is provided, an empty thread will be created.

        model : typing.Optional[CreateThreadAndRunRequestModel]
            The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

        instructions : typing.Optional[str]
            Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.

        tools : typing.Optional[typing.Sequence[CreateThreadAndRunRequestToolsItem]]
            Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        temperature : typing.Optional[float]
            What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

        stream : typing.Optional[bool]
            If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

        max_prompt_tokens : typing.Optional[int]
            The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

        max_completion_tokens : typing.Optional[int]
            The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

        truncation_strategy : typing.Optional[TruncationObject]

        tool_choice : typing.Optional[AssistantsApiToolChoiceOption]

        response_format : typing.Optional[AssistantsApiResponseFormatOption]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "threads/runs",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "thread": convert_and_respect_annotation_metadata(
                    object_=thread, annotation=CreateThreadRequest, direction="write"
                ),
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=typing.Optional[CreateThreadAndRunRequestModel], direction="write"
                ),
                "instructions": instructions,
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools,
                    annotation=typing.Optional[typing.Sequence[CreateThreadAndRunRequestToolsItem]],
                    direction="write",
                ),
                "metadata": metadata,
                "temperature": temperature,
                "stream": stream,
                "max_prompt_tokens": max_prompt_tokens,
                "max_completion_tokens": max_completion_tokens,
                "truncation_strategy": convert_and_respect_annotation_metadata(
                    object_=truncation_strategy, annotation=TruncationObject, direction="write"
                ),
                "tool_choice": convert_and_respect_annotation_metadata(
                    object_=tool_choice, annotation=AssistantsApiToolChoiceOption, direction="write"
                ),
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format, annotation=AssistantsApiResponseFormatOption, direction="write"
                ),
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
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    def list_runs(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListRunsResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread the run belongs to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListRunsRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListRunsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRunsResponse,
                    parse_obj_as(
                        type_=ListRunsResponse,
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

    def create_run(
        self,
        thread_id: str,
        *,
        assistant_id: str,
        model: typing.Optional[CreateRunRequestModel] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        additional_instructions: typing.Optional[str] = OMIT,
        additional_messages: typing.Optional[typing.Sequence[CreateMessageRequest]] = OMIT,
        tools: typing.Optional[typing.Sequence[CreateRunRequestToolsItem]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        max_prompt_tokens: typing.Optional[int] = OMIT,
        max_completion_tokens: typing.Optional[int] = OMIT,
        truncation_strategy: typing.Optional[TruncationObject] = OMIT,
        tool_choice: typing.Optional[AssistantsApiToolChoiceOption] = OMIT,
        response_format: typing.Optional[AssistantsApiResponseFormatOption] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to run.

        assistant_id : str
            The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.

        model : typing.Optional[CreateRunRequestModel]
            The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

        instructions : typing.Optional[str]
            Overrides the [instructions](/docs/api-reference/assistants/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis.

        additional_instructions : typing.Optional[str]
            Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.

        additional_messages : typing.Optional[typing.Sequence[CreateMessageRequest]]
            Adds additional messages to the thread before creating the run.

        tools : typing.Optional[typing.Sequence[CreateRunRequestToolsItem]]
            Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        temperature : typing.Optional[float]
            What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

        stream : typing.Optional[bool]
            If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

        max_prompt_tokens : typing.Optional[int]
            The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

        max_completion_tokens : typing.Optional[int]
            The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

        truncation_strategy : typing.Optional[TruncationObject]

        tool_choice : typing.Optional[AssistantsApiToolChoiceOption]

        response_format : typing.Optional[AssistantsApiResponseFormatOption]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=typing.Optional[CreateRunRequestModel], direction="write"
                ),
                "instructions": instructions,
                "additional_instructions": additional_instructions,
                "additional_messages": convert_and_respect_annotation_metadata(
                    object_=additional_messages,
                    annotation=typing.Optional[typing.Sequence[CreateMessageRequest]],
                    direction="write",
                ),
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools,
                    annotation=typing.Optional[typing.Sequence[CreateRunRequestToolsItem]],
                    direction="write",
                ),
                "metadata": metadata,
                "temperature": temperature,
                "stream": stream,
                "max_prompt_tokens": max_prompt_tokens,
                "max_completion_tokens": max_completion_tokens,
                "truncation_strategy": convert_and_respect_annotation_metadata(
                    object_=truncation_strategy, annotation=TruncationObject, direction="write"
                ),
                "tool_choice": convert_and_respect_annotation_metadata(
                    object_=tool_choice, annotation=AssistantsApiToolChoiceOption, direction="write"
                ),
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format, annotation=AssistantsApiResponseFormatOption, direction="write"
                ),
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
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    def get_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) that was run.

        run_id : str
            The ID of the run to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    def modify_run(
        self,
        thread_id: str,
        run_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) that was run.

        run_id : str
            The ID of the run to modify.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}",
            method="POST",
            json={
                "metadata": metadata,
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
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    def submit_tool_ouputs_to_run(
        self,
        thread_id: str,
        run_id: str,
        *,
        tool_outputs: typing.Sequence[SubmitToolOutputsRunRequestToolOutputsItem],
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) to which this run belongs.

        run_id : str
            The ID of the run that requires the tool output submission.

        tool_outputs : typing.Sequence[SubmitToolOutputsRunRequestToolOutputsItem]
            A list of tools for which the outputs are being submitted.

        stream : typing.Optional[bool]
            If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/submit_tool_outputs",
            method="POST",
            json={
                "tool_outputs": convert_and_respect_annotation_metadata(
                    object_=tool_outputs,
                    annotation=typing.Sequence[SubmitToolOutputsRunRequestToolOutputsItem],
                    direction="write",
                ),
                "stream": stream,
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
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    def cancel_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to which this run belongs.

        run_id : str
            The ID of the run to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    def list_run_steps(
        self,
        thread_id: str,
        run_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunStepsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListRunStepsResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread the run and run steps belong to.

        run_id : str
            The ID of the run the run steps belong to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListRunStepsRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListRunStepsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/steps",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRunStepsResponse,
                    parse_obj_as(
                        type_=ListRunStepsResponse,
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

    def get_run_step(
        self, thread_id: str, run_id: str, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RunStepObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to which the run and run step belongs.

        run_id : str
            The ID of the run to which the run step belongs.

        step_id : str
            The ID of the run step to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunStepObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/steps/{encode_path_param(step_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunStepObject,
                    parse_obj_as(
                        type_=RunStepObject,
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

    def list_assistant_files(
        self,
        assistant_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAssistantFilesRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAssistantFilesResponse]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant the file belongs to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListAssistantFilesRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAssistantFilesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/files",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAssistantFilesResponse,
                    parse_obj_as(
                        type_=ListAssistantFilesResponse,
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

    def create_assistant_file(
        self, assistant_id: str, *, file_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AssistantFileObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant for which to create a File.

        file_id : str
            A [File](/docs/api-reference/files) ID (with `purpose="assistants"`) that the assistant should use. Useful for tools like `retrieval` and `code_interpreter` that can access files.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AssistantFileObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/files",
            method="POST",
            json={
                "file_id": file_id,
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
                    AssistantFileObject,
                    parse_obj_as(
                        type_=AssistantFileObject,
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

    def get_assistant_file(
        self, assistant_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AssistantFileObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant who the file belongs to.

        file_id : str
            The ID of the file we're getting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AssistantFileObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/files/{encode_path_param(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssistantFileObject,
                    parse_obj_as(
                        type_=AssistantFileObject,
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

    def delete_assistant_file(
        self, assistant_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteAssistantFileResponse]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant that the file belongs to.

        file_id : str
            The ID of the file to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteAssistantFileResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/files/{encode_path_param(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAssistantFileResponse,
                    parse_obj_as(
                        type_=DeleteAssistantFileResponse,
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

    def list_message_files(
        self,
        thread_id: str,
        message_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessageFilesRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListMessageFilesResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread that the message and files belong to.

        message_id : str
            The ID of the message that the files belongs to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListMessageFilesRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListMessageFilesResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages/{encode_path_param(message_id)}/files",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMessageFilesResponse,
                    parse_obj_as(
                        type_=ListMessageFilesResponse,
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

    def get_message_file(
        self, thread_id: str, message_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[MessageFileObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to which the message and File belong.

        message_id : str
            The ID of the message the file belongs to.

        file_id : str
            The ID of the file being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[MessageFileObject]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages/{encode_path_param(message_id)}/files/{encode_path_param(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageFileObject,
                    parse_obj_as(
                        type_=MessageFileObject,
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


class AsyncRawAssistantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_assistants(
        self,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAssistantsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAssistantsResponse]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListAssistantsRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAssistantsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assistants",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAssistantsResponse,
                    parse_obj_as(
                        type_=ListAssistantsResponse,
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

    async def create_assistant(
        self,
        *,
        model: CreateAssistantRequestModel,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        tools: typing.Optional[typing.Sequence[CreateAssistantRequestToolsItem]] = OMIT,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AssistantObject]:
        """
        Parameters
        ----------
        model : CreateAssistantRequestModel
            ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

        name : typing.Optional[str]
            The name of the assistant. The maximum length is 256 characters.

        description : typing.Optional[str]
            The description of the assistant. The maximum length is 512 characters.

        instructions : typing.Optional[str]
            The system instructions that the assistant uses. The maximum length is 256,000 characters.

        tools : typing.Optional[typing.Sequence[CreateAssistantRequestToolsItem]]
            A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

        file_ids : typing.Optional[typing.Sequence[str]]
            A list of [file](/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AssistantObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assistants",
            method="POST",
            json={
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=CreateAssistantRequestModel, direction="write"
                ),
                "name": name,
                "description": description,
                "instructions": instructions,
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Sequence[CreateAssistantRequestToolsItem], direction="write"
                ),
                "file_ids": file_ids,
                "metadata": metadata,
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
                    AssistantObject,
                    parse_obj_as(
                        type_=AssistantObject,
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

    async def get_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AssistantObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AssistantObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssistantObject,
                    parse_obj_as(
                        type_=AssistantObject,
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

    async def modify_assistant(
        self,
        assistant_id: str,
        *,
        model: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        tools: typing.Optional[typing.Sequence[ModifyAssistantRequestToolsItem]] = OMIT,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AssistantObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to modify.

        model : typing.Optional[str]
            ID of the model to use. You can use the [List models](/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](/docs/models/overview) for descriptions of them.

        name : typing.Optional[str]
            The name of the assistant. The maximum length is 256 characters.

        description : typing.Optional[str]
            The description of the assistant. The maximum length is 512 characters.

        instructions : typing.Optional[str]
            The system instructions that the assistant uses. The maximum length is 256,000 characters.

        tools : typing.Optional[typing.Sequence[ModifyAssistantRequestToolsItem]]
            A list of tool enabled on the assistant. There can be a maximum of 128 tools per assistant. Tools can be of types `code_interpreter`, `retrieval`, or `function`.

        file_ids : typing.Optional[typing.Sequence[str]]
            A list of [File](/docs/api-reference/files) IDs attached to this assistant. There can be a maximum of 20 files attached to the assistant. Files are ordered by their creation date in ascending order. If a file was previously attached to the list but does not show up in the list, it will be deleted from the assistant.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AssistantObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="POST",
            json={
                "model": model,
                "name": name,
                "description": description,
                "instructions": instructions,
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools, annotation=typing.Sequence[ModifyAssistantRequestToolsItem], direction="write"
                ),
                "file_ids": file_ids,
                "metadata": metadata,
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
                    AssistantObject,
                    parse_obj_as(
                        type_=AssistantObject,
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

    async def delete_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteAssistantResponse]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteAssistantResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAssistantResponse,
                    parse_obj_as(
                        type_=DeleteAssistantResponse,
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

    async def create_thread(
        self,
        *,
        messages: typing.Optional[typing.Sequence[CreateMessageRequest]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadObject]:
        """
        Parameters
        ----------
        messages : typing.Optional[typing.Sequence[CreateMessageRequest]]
            A list of [messages](/docs/api-reference/messages) to start the thread with.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "threads",
            method="POST",
            json={
                "messages": convert_and_respect_annotation_metadata(
                    object_=messages, annotation=typing.Sequence[CreateMessageRequest], direction="write"
                ),
                "metadata": metadata,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadObject,
                    parse_obj_as(
                        type_=ThreadObject,
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

    async def get_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ThreadObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ThreadObject,
                    parse_obj_as(
                        type_=ThreadObject,
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

    async def modify_thread(
        self,
        thread_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ThreadObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to modify. Only the `metadata` can be modified.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ThreadObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="POST",
            json={
                "metadata": metadata,
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
                    ThreadObject,
                    parse_obj_as(
                        type_=ThreadObject,
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

    async def delete_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteThreadResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteThreadResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteThreadResponse,
                    parse_obj_as(
                        type_=DeleteThreadResponse,
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

    async def list_messages(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessagesRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        run_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMessagesResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) the messages belong to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListMessagesRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        run_id : typing.Optional[str]
            Filter messages by the run ID that generated them.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMessagesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
                "run_id": run_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMessagesResponse,
                    parse_obj_as(
                        type_=ListMessagesResponse,
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

    async def create_message(
        self,
        thread_id: str,
        *,
        role: CreateMessageRequestRole,
        content: str,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessageObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) to create a message for.

        role : CreateMessageRequestRole
            The role of the entity that is creating the message. Allowed values include:
            - `user`: Indicates the message is sent by an actual user and should be used in most cases to represent user-generated messages.
            - `assistant`: Indicates the message is generated by the assistant. Use this value to insert messages from the assistant into the conversation.

        content : str
            The content of the message.

        file_ids : typing.Optional[typing.Sequence[str]]
            A list of [File](/docs/api-reference/files) IDs that the message should use. There can be a maximum of 10 files attached to a message. Useful for tools like `retrieval` and `code_interpreter` that can access and use files.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessageObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages",
            method="POST",
            json={
                "role": role,
                "content": content,
                "file_ids": file_ids,
                "metadata": metadata,
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
                    MessageObject,
                    parse_obj_as(
                        type_=MessageObject,
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

    async def get_message(
        self, thread_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessageObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) to which this message belongs.

        message_id : str
            The ID of the message to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessageObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages/{encode_path_param(message_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageObject,
                    parse_obj_as(
                        type_=MessageObject,
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

    async def modify_message(
        self,
        thread_id: str,
        message_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MessageObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to which this message belongs.

        message_id : str
            The ID of the message to modify.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessageObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages/{encode_path_param(message_id)}",
            method="POST",
            json={
                "metadata": metadata,
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
                    MessageObject,
                    parse_obj_as(
                        type_=MessageObject,
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

    async def create_thread_and_run(
        self,
        *,
        assistant_id: str,
        thread: typing.Optional[CreateThreadRequest] = OMIT,
        model: typing.Optional[CreateThreadAndRunRequestModel] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        tools: typing.Optional[typing.Sequence[CreateThreadAndRunRequestToolsItem]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        max_prompt_tokens: typing.Optional[int] = OMIT,
        max_completion_tokens: typing.Optional[int] = OMIT,
        truncation_strategy: typing.Optional[TruncationObject] = OMIT,
        tool_choice: typing.Optional[AssistantsApiToolChoiceOption] = OMIT,
        response_format: typing.Optional[AssistantsApiResponseFormatOption] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.

        thread : typing.Optional[CreateThreadRequest]
            If no thread is provided, an empty thread will be created.

        model : typing.Optional[CreateThreadAndRunRequestModel]
            The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

        instructions : typing.Optional[str]
            Override the default system message of the assistant. This is useful for modifying the behavior on a per-run basis.

        tools : typing.Optional[typing.Sequence[CreateThreadAndRunRequestToolsItem]]
            Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        temperature : typing.Optional[float]
            What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

        stream : typing.Optional[bool]
            If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

        max_prompt_tokens : typing.Optional[int]
            The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

        max_completion_tokens : typing.Optional[int]
            The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `incomplete`. See `incomplete_details` for more info.

        truncation_strategy : typing.Optional[TruncationObject]

        tool_choice : typing.Optional[AssistantsApiToolChoiceOption]

        response_format : typing.Optional[AssistantsApiResponseFormatOption]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "threads/runs",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "thread": convert_and_respect_annotation_metadata(
                    object_=thread, annotation=CreateThreadRequest, direction="write"
                ),
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=typing.Optional[CreateThreadAndRunRequestModel], direction="write"
                ),
                "instructions": instructions,
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools,
                    annotation=typing.Optional[typing.Sequence[CreateThreadAndRunRequestToolsItem]],
                    direction="write",
                ),
                "metadata": metadata,
                "temperature": temperature,
                "stream": stream,
                "max_prompt_tokens": max_prompt_tokens,
                "max_completion_tokens": max_completion_tokens,
                "truncation_strategy": convert_and_respect_annotation_metadata(
                    object_=truncation_strategy, annotation=TruncationObject, direction="write"
                ),
                "tool_choice": convert_and_respect_annotation_metadata(
                    object_=tool_choice, annotation=AssistantsApiToolChoiceOption, direction="write"
                ),
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format, annotation=AssistantsApiResponseFormatOption, direction="write"
                ),
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
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    async def list_runs(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListRunsResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread the run belongs to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListRunsRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListRunsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRunsResponse,
                    parse_obj_as(
                        type_=ListRunsResponse,
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

    async def create_run(
        self,
        thread_id: str,
        *,
        assistant_id: str,
        model: typing.Optional[CreateRunRequestModel] = OMIT,
        instructions: typing.Optional[str] = OMIT,
        additional_instructions: typing.Optional[str] = OMIT,
        additional_messages: typing.Optional[typing.Sequence[CreateMessageRequest]] = OMIT,
        tools: typing.Optional[typing.Sequence[CreateRunRequestToolsItem]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        temperature: typing.Optional[float] = OMIT,
        stream: typing.Optional[bool] = OMIT,
        max_prompt_tokens: typing.Optional[int] = OMIT,
        max_completion_tokens: typing.Optional[int] = OMIT,
        truncation_strategy: typing.Optional[TruncationObject] = OMIT,
        tool_choice: typing.Optional[AssistantsApiToolChoiceOption] = OMIT,
        response_format: typing.Optional[AssistantsApiResponseFormatOption] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to run.

        assistant_id : str
            The ID of the [assistant](/docs/api-reference/assistants) to use to execute this run.

        model : typing.Optional[CreateRunRequestModel]
            The ID of the [Model](/docs/api-reference/models) to be used to execute this run. If a value is provided here, it will override the model associated with the assistant. If not, the model associated with the assistant will be used.

        instructions : typing.Optional[str]
            Overrides the [instructions](/docs/api-reference/assistants/createAssistant) of the assistant. This is useful for modifying the behavior on a per-run basis.

        additional_instructions : typing.Optional[str]
            Appends additional instructions at the end of the instructions for the run. This is useful for modifying the behavior on a per-run basis without overriding other instructions.

        additional_messages : typing.Optional[typing.Sequence[CreateMessageRequest]]
            Adds additional messages to the thread before creating the run.

        tools : typing.Optional[typing.Sequence[CreateRunRequestToolsItem]]
            Override the tools the assistant can use for this run. This is useful for modifying the behavior on a per-run basis.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        temperature : typing.Optional[float]
            What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.

        stream : typing.Optional[bool]
            If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

        max_prompt_tokens : typing.Optional[int]
            The maximum number of prompt tokens that may be used over the course of the run. The run will make a best effort to use only the number of prompt tokens specified, across multiple turns of the run. If the run exceeds the number of prompt tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

        max_completion_tokens : typing.Optional[int]
            The maximum number of completion tokens that may be used over the course of the run. The run will make a best effort to use only the number of completion tokens specified, across multiple turns of the run. If the run exceeds the number of completion tokens specified, the run will end with status `complete`. See `incomplete_details` for more info.

        truncation_strategy : typing.Optional[TruncationObject]

        tool_choice : typing.Optional[AssistantsApiToolChoiceOption]

        response_format : typing.Optional[AssistantsApiResponseFormatOption]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs",
            method="POST",
            json={
                "assistant_id": assistant_id,
                "model": convert_and_respect_annotation_metadata(
                    object_=model, annotation=typing.Optional[CreateRunRequestModel], direction="write"
                ),
                "instructions": instructions,
                "additional_instructions": additional_instructions,
                "additional_messages": convert_and_respect_annotation_metadata(
                    object_=additional_messages,
                    annotation=typing.Optional[typing.Sequence[CreateMessageRequest]],
                    direction="write",
                ),
                "tools": convert_and_respect_annotation_metadata(
                    object_=tools,
                    annotation=typing.Optional[typing.Sequence[CreateRunRequestToolsItem]],
                    direction="write",
                ),
                "metadata": metadata,
                "temperature": temperature,
                "stream": stream,
                "max_prompt_tokens": max_prompt_tokens,
                "max_completion_tokens": max_completion_tokens,
                "truncation_strategy": convert_and_respect_annotation_metadata(
                    object_=truncation_strategy, annotation=TruncationObject, direction="write"
                ),
                "tool_choice": convert_and_respect_annotation_metadata(
                    object_=tool_choice, annotation=AssistantsApiToolChoiceOption, direction="write"
                ),
                "response_format": convert_and_respect_annotation_metadata(
                    object_=response_format, annotation=AssistantsApiResponseFormatOption, direction="write"
                ),
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
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    async def get_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) that was run.

        run_id : str
            The ID of the run to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    async def modify_run(
        self,
        thread_id: str,
        run_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) that was run.

        run_id : str
            The ID of the run to modify.

        metadata : typing.Optional[typing.Dict[str, typing.Any]]
            Set of 16 key-value pairs that can be attached to an object. This can be useful for storing additional information about the object in a structured format. Keys can be a maximum of 64 characters long and values can be a maxium of 512 characters long.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}",
            method="POST",
            json={
                "metadata": metadata,
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
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    async def submit_tool_ouputs_to_run(
        self,
        thread_id: str,
        run_id: str,
        *,
        tool_outputs: typing.Sequence[SubmitToolOutputsRunRequestToolOutputsItem],
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the [thread](/docs/api-reference/threads) to which this run belongs.

        run_id : str
            The ID of the run that requires the tool output submission.

        tool_outputs : typing.Sequence[SubmitToolOutputsRunRequestToolOutputsItem]
            A list of tools for which the outputs are being submitted.

        stream : typing.Optional[bool]
            If `true`, returns a stream of events that happen during the Run as server-sent events, terminating when the Run enters a terminal state with a `data: [DONE]` message.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/submit_tool_outputs",
            method="POST",
            json={
                "tool_outputs": convert_and_respect_annotation_metadata(
                    object_=tool_outputs,
                    annotation=typing.Sequence[SubmitToolOutputsRunRequestToolOutputsItem],
                    direction="write",
                ),
                "stream": stream,
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
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    async def cancel_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to which this run belongs.

        run_id : str
            The ID of the run to cancel.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/cancel",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunObject,
                    parse_obj_as(
                        type_=RunObject,
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

    async def list_run_steps(
        self,
        thread_id: str,
        run_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunStepsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListRunStepsResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread the run and run steps belong to.

        run_id : str
            The ID of the run the run steps belong to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListRunStepsRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListRunStepsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/steps",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListRunStepsResponse,
                    parse_obj_as(
                        type_=ListRunStepsResponse,
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

    async def get_run_step(
        self, thread_id: str, run_id: str, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RunStepObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to which the run and run step belongs.

        run_id : str
            The ID of the run to which the run step belongs.

        step_id : str
            The ID of the run step to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunStepObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/runs/{encode_path_param(run_id)}/steps/{encode_path_param(step_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RunStepObject,
                    parse_obj_as(
                        type_=RunStepObject,
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

    async def list_assistant_files(
        self,
        assistant_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAssistantFilesRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAssistantFilesResponse]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant the file belongs to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListAssistantFilesRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAssistantFilesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/files",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAssistantFilesResponse,
                    parse_obj_as(
                        type_=ListAssistantFilesResponse,
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

    async def create_assistant_file(
        self, assistant_id: str, *, file_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AssistantFileObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant for which to create a File.

        file_id : str
            A [File](/docs/api-reference/files) ID (with `purpose="assistants"`) that the assistant should use. Useful for tools like `retrieval` and `code_interpreter` that can access files.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AssistantFileObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/files",
            method="POST",
            json={
                "file_id": file_id,
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
                    AssistantFileObject,
                    parse_obj_as(
                        type_=AssistantFileObject,
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

    async def get_assistant_file(
        self, assistant_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AssistantFileObject]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant who the file belongs to.

        file_id : str
            The ID of the file we're getting.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AssistantFileObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/files/{encode_path_param(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AssistantFileObject,
                    parse_obj_as(
                        type_=AssistantFileObject,
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

    async def delete_assistant_file(
        self, assistant_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteAssistantFileResponse]:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant that the file belongs to.

        file_id : str
            The ID of the file to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteAssistantFileResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"assistants/{encode_path_param(assistant_id)}/files/{encode_path_param(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAssistantFileResponse,
                    parse_obj_as(
                        type_=DeleteAssistantFileResponse,
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

    async def list_message_files(
        self,
        thread_id: str,
        message_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListMessageFilesRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListMessageFilesResponse]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread that the message and files belong to.

        message_id : str
            The ID of the message that the files belongs to.

        limit : typing.Optional[int]
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 20.

        order : typing.Optional[ListMessageFilesRequestOrder]
            Sort order by the `created_at` timestamp of the objects. `asc` for ascending order and `desc` for descending order.

        after : typing.Optional[str]
            A cursor for use in pagination. `after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include after=obj_foo in order to fetch the next page of the list.

        before : typing.Optional[str]
            A cursor for use in pagination. `before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with obj_foo, your subsequent call can include before=obj_foo in order to fetch the previous page of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListMessageFilesResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages/{encode_path_param(message_id)}/files",
            method="GET",
            params={
                "limit": limit,
                "order": order,
                "after": after,
                "before": before,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListMessageFilesResponse,
                    parse_obj_as(
                        type_=ListMessageFilesResponse,
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

    async def get_message_file(
        self, thread_id: str, message_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[MessageFileObject]:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to which the message and File belong.

        message_id : str
            The ID of the message the file belongs to.

        file_id : str
            The ID of the file being retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[MessageFileObject]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"threads/{encode_path_param(thread_id)}/messages/{encode_path_param(message_id)}/files/{encode_path_param(file_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MessageFileObject,
                    parse_obj_as(
                        type_=MessageFileObject,
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
