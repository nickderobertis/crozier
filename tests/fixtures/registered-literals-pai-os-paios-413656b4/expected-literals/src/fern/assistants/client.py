

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
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
from .raw_client import AsyncRawAssistantsClient, RawAssistantsClient
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


OMIT = typing.cast(typing.Any, ...)


class AssistantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssistantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssistantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssistantsClient
        """
        return self._raw_client

    def list_assistants(
        self,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAssistantsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAssistantsResponse:
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
        ListAssistantsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.list_assistants()
        """
        _response = self._raw_client.list_assistants(
            limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

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
    ) -> AssistantObject:
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
        AssistantObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.create_assistant(
            model="gpt-4-turbo",
        )
        """
        _response = self._raw_client.create_assistant(
            model=model,
            name=name,
            description=description,
            instructions=instructions,
            tools=tools,
            file_ids=file_ids,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def get_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssistantObject:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssistantObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.get_assistant(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.get_assistant(assistant_id, request_options=request_options)
        return _response.data

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
    ) -> AssistantObject:
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
        AssistantObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.modify_assistant(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.modify_assistant(
            assistant_id,
            model=model,
            name=name,
            description=description,
            instructions=instructions,
            tools=tools,
            file_ids=file_ids,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def delete_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAssistantResponse:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAssistantResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.delete_assistant(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.delete_assistant(assistant_id, request_options=request_options)
        return _response.data

    def create_thread(
        self,
        *,
        messages: typing.Optional[typing.Sequence[CreateMessageRequest]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadObject:
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
        ThreadObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.create_thread()
        """
        _response = self._raw_client.create_thread(
            messages=messages, metadata=metadata, request_options=request_options
        )
        return _response.data

    def get_thread(self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ThreadObject:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.get_thread(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.get_thread(thread_id, request_options=request_options)
        return _response.data

    def modify_thread(
        self,
        thread_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadObject:
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
        ThreadObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.modify_thread(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.modify_thread(thread_id, metadata=metadata, request_options=request_options)
        return _response.data

    def delete_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteThreadResponse:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteThreadResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.delete_thread(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.delete_thread(thread_id, request_options=request_options)
        return _response.data

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
    ) -> ListMessagesResponse:
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
        ListMessagesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.list_messages(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.list_messages(
            thread_id,
            limit=limit,
            order=order,
            after=after,
            before=before,
            run_id=run_id,
            request_options=request_options,
        )
        return _response.data

    def create_message(
        self,
        thread_id: str,
        *,
        role: CreateMessageRequestRole,
        content: str,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageObject:
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
        MessageObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.create_message(
            thread_id="thread_id",
            role="user",
            content="content",
        )
        """
        _response = self._raw_client.create_message(
            thread_id, role=role, content=content, file_ids=file_ids, metadata=metadata, request_options=request_options
        )
        return _response.data

    def get_message(
        self, thread_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageObject:
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
        MessageObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.get_message(
            thread_id="thread_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.get_message(thread_id, message_id, request_options=request_options)
        return _response.data

    def modify_message(
        self,
        thread_id: str,
        message_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageObject:
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
        MessageObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.modify_message(
            thread_id="thread_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.modify_message(
            thread_id, message_id, metadata=metadata, request_options=request_options
        )
        return _response.data

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
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.create_thread_and_run(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.create_thread_and_run(
            assistant_id=assistant_id,
            thread=thread,
            model=model,
            instructions=instructions,
            tools=tools,
            metadata=metadata,
            temperature=temperature,
            stream=stream,
            max_prompt_tokens=max_prompt_tokens,
            max_completion_tokens=max_completion_tokens,
            truncation_strategy=truncation_strategy,
            tool_choice=tool_choice,
            response_format=response_format,
            request_options=request_options,
        )
        return _response.data

    def list_runs(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRunsResponse:
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
        ListRunsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.list_runs(
            thread_id="thread_id",
        )
        """
        _response = self._raw_client.list_runs(
            thread_id, limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

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
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.create_run(
            thread_id="thread_id",
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.create_run(
            thread_id,
            assistant_id=assistant_id,
            model=model,
            instructions=instructions,
            additional_instructions=additional_instructions,
            additional_messages=additional_messages,
            tools=tools,
            metadata=metadata,
            temperature=temperature,
            stream=stream,
            max_prompt_tokens=max_prompt_tokens,
            max_completion_tokens=max_completion_tokens,
            truncation_strategy=truncation_strategy,
            tool_choice=tool_choice,
            response_format=response_format,
            request_options=request_options,
        )
        return _response.data

    def get_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.get_run(
            thread_id="thread_id",
            run_id="run_id",
        )
        """
        _response = self._raw_client.get_run(thread_id, run_id, request_options=request_options)
        return _response.data

    def modify_run(
        self,
        thread_id: str,
        run_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.modify_run(
            thread_id="thread_id",
            run_id="run_id",
        )
        """
        _response = self._raw_client.modify_run(thread_id, run_id, metadata=metadata, request_options=request_options)
        return _response.data

    def submit_tool_ouputs_to_run(
        self,
        thread_id: str,
        run_id: str,
        *,
        tool_outputs: typing.Sequence[SubmitToolOutputsRunRequestToolOutputsItem],
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        from fern.assistants import SubmitToolOutputsRunRequestToolOutputsItem

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.submit_tool_ouputs_to_run(
            thread_id="thread_id",
            run_id="run_id",
            tool_outputs=[SubmitToolOutputsRunRequestToolOutputsItem()],
        )
        """
        _response = self._raw_client.submit_tool_ouputs_to_run(
            thread_id, run_id, tool_outputs=tool_outputs, stream=stream, request_options=request_options
        )
        return _response.data

    def cancel_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.cancel_run(
            thread_id="thread_id",
            run_id="run_id",
        )
        """
        _response = self._raw_client.cancel_run(thread_id, run_id, request_options=request_options)
        return _response.data

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
    ) -> ListRunStepsResponse:
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
        ListRunStepsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.list_run_steps(
            thread_id="thread_id",
            run_id="run_id",
        )
        """
        _response = self._raw_client.list_run_steps(
            thread_id, run_id, limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

    def get_run_step(
        self, thread_id: str, run_id: str, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunStepObject:
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
        RunStepObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.get_run_step(
            thread_id="thread_id",
            run_id="run_id",
            step_id="step_id",
        )
        """
        _response = self._raw_client.get_run_step(thread_id, run_id, step_id, request_options=request_options)
        return _response.data

    def list_assistant_files(
        self,
        assistant_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAssistantFilesRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAssistantFilesResponse:
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
        ListAssistantFilesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.list_assistant_files(
            assistant_id="assistant_id",
        )
        """
        _response = self._raw_client.list_assistant_files(
            assistant_id, limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

    def create_assistant_file(
        self, assistant_id: str, *, file_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AssistantFileObject:
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
        AssistantFileObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.create_assistant_file(
            assistant_id="file-abc123",
            file_id="file_id",
        )
        """
        _response = self._raw_client.create_assistant_file(
            assistant_id, file_id=file_id, request_options=request_options
        )
        return _response.data

    def get_assistant_file(
        self, assistant_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssistantFileObject:
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
        AssistantFileObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.get_assistant_file(
            assistant_id="assistant_id",
            file_id="file_id",
        )
        """
        _response = self._raw_client.get_assistant_file(assistant_id, file_id, request_options=request_options)
        return _response.data

    def delete_assistant_file(
        self, assistant_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAssistantFileResponse:
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
        DeleteAssistantFileResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.delete_assistant_file(
            assistant_id="assistant_id",
            file_id="file_id",
        )
        """
        _response = self._raw_client.delete_assistant_file(assistant_id, file_id, request_options=request_options)
        return _response.data

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
    ) -> ListMessageFilesResponse:
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
        ListMessageFilesResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.list_message_files(
            thread_id="thread_id",
            message_id="message_id",
        )
        """
        _response = self._raw_client.list_message_files(
            thread_id, message_id, limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

    def get_message_file(
        self, thread_id: str, message_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageFileObject:
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
        MessageFileObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.assistants.get_message_file(
            thread_id="thread_abc123",
            message_id="msg_abc123",
            file_id="file-abc123",
        )
        """
        _response = self._raw_client.get_message_file(thread_id, message_id, file_id, request_options=request_options)
        return _response.data


class AsyncAssistantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssistantsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssistantsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssistantsClient
        """
        return self._raw_client

    async def list_assistants(
        self,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAssistantsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAssistantsResponse:
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
        ListAssistantsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.list_assistants()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_assistants(
            limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

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
    ) -> AssistantObject:
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
        AssistantObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.create_assistant(
                model="gpt-4-turbo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_assistant(
            model=model,
            name=name,
            description=description,
            instructions=instructions,
            tools=tools,
            file_ids=file_ids,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def get_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssistantObject:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AssistantObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.get_assistant(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_assistant(assistant_id, request_options=request_options)
        return _response.data

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
    ) -> AssistantObject:
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
        AssistantObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.modify_assistant(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_assistant(
            assistant_id,
            model=model,
            name=name,
            description=description,
            instructions=instructions,
            tools=tools,
            file_ids=file_ids,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def delete_assistant(
        self, assistant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAssistantResponse:
        """
        Parameters
        ----------
        assistant_id : str
            The ID of the assistant to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteAssistantResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.delete_assistant(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_assistant(assistant_id, request_options=request_options)
        return _response.data

    async def create_thread(
        self,
        *,
        messages: typing.Optional[typing.Sequence[CreateMessageRequest]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadObject:
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
        ThreadObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.create_thread()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_thread(
            messages=messages, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def get_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ThreadObject:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to retrieve.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ThreadObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.get_thread(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_thread(thread_id, request_options=request_options)
        return _response.data

    async def modify_thread(
        self,
        thread_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ThreadObject:
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
        ThreadObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.modify_thread(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_thread(thread_id, metadata=metadata, request_options=request_options)
        return _response.data

    async def delete_thread(
        self, thread_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteThreadResponse:
        """
        Parameters
        ----------
        thread_id : str
            The ID of the thread to delete.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteThreadResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.delete_thread(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_thread(thread_id, request_options=request_options)
        return _response.data

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
    ) -> ListMessagesResponse:
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
        ListMessagesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.list_messages(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_messages(
            thread_id,
            limit=limit,
            order=order,
            after=after,
            before=before,
            run_id=run_id,
            request_options=request_options,
        )
        return _response.data

    async def create_message(
        self,
        thread_id: str,
        *,
        role: CreateMessageRequestRole,
        content: str,
        file_ids: typing.Optional[typing.Sequence[str]] = OMIT,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageObject:
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
        MessageObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.create_message(
                thread_id="thread_id",
                role="user",
                content="content",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_message(
            thread_id, role=role, content=content, file_ids=file_ids, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def get_message(
        self, thread_id: str, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageObject:
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
        MessageObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.get_message(
                thread_id="thread_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_message(thread_id, message_id, request_options=request_options)
        return _response.data

    async def modify_message(
        self,
        thread_id: str,
        message_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageObject:
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
        MessageObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.modify_message(
                thread_id="thread_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_message(
            thread_id, message_id, metadata=metadata, request_options=request_options
        )
        return _response.data

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
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.create_thread_and_run(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_thread_and_run(
            assistant_id=assistant_id,
            thread=thread,
            model=model,
            instructions=instructions,
            tools=tools,
            metadata=metadata,
            temperature=temperature,
            stream=stream,
            max_prompt_tokens=max_prompt_tokens,
            max_completion_tokens=max_completion_tokens,
            truncation_strategy=truncation_strategy,
            tool_choice=tool_choice,
            response_format=response_format,
            request_options=request_options,
        )
        return _response.data

    async def list_runs(
        self,
        thread_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListRunsRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListRunsResponse:
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
        ListRunsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.list_runs(
                thread_id="thread_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_runs(
            thread_id, limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

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
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.create_run(
                thread_id="thread_id",
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_run(
            thread_id,
            assistant_id=assistant_id,
            model=model,
            instructions=instructions,
            additional_instructions=additional_instructions,
            additional_messages=additional_messages,
            tools=tools,
            metadata=metadata,
            temperature=temperature,
            stream=stream,
            max_prompt_tokens=max_prompt_tokens,
            max_completion_tokens=max_completion_tokens,
            truncation_strategy=truncation_strategy,
            tool_choice=tool_choice,
            response_format=response_format,
            request_options=request_options,
        )
        return _response.data

    async def get_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.get_run(
                thread_id="thread_id",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run(thread_id, run_id, request_options=request_options)
        return _response.data

    async def modify_run(
        self,
        thread_id: str,
        run_id: str,
        *,
        metadata: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.modify_run(
                thread_id="thread_id",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.modify_run(
            thread_id, run_id, metadata=metadata, request_options=request_options
        )
        return _response.data

    async def submit_tool_ouputs_to_run(
        self,
        thread_id: str,
        run_id: str,
        *,
        tool_outputs: typing.Sequence[SubmitToolOutputsRunRequestToolOutputsItem],
        stream: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        import asyncio

        from fern.assistants import SubmitToolOutputsRunRequestToolOutputsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.submit_tool_ouputs_to_run(
                thread_id="thread_id",
                run_id="run_id",
                tool_outputs=[SubmitToolOutputsRunRequestToolOutputsItem()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.submit_tool_ouputs_to_run(
            thread_id, run_id, tool_outputs=tool_outputs, stream=stream, request_options=request_options
        )
        return _response.data

    async def cancel_run(
        self, thread_id: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunObject:
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
        RunObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.cancel_run(
                thread_id="thread_id",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.cancel_run(thread_id, run_id, request_options=request_options)
        return _response.data

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
    ) -> ListRunStepsResponse:
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
        ListRunStepsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.list_run_steps(
                thread_id="thread_id",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_run_steps(
            thread_id, run_id, limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

    async def get_run_step(
        self, thread_id: str, run_id: str, step_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RunStepObject:
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
        RunStepObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.get_run_step(
                thread_id="thread_id",
                run_id="run_id",
                step_id="step_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_run_step(thread_id, run_id, step_id, request_options=request_options)
        return _response.data

    async def list_assistant_files(
        self,
        assistant_id: str,
        *,
        limit: typing.Optional[int] = None,
        order: typing.Optional[ListAssistantFilesRequestOrder] = None,
        after: typing.Optional[str] = None,
        before: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListAssistantFilesResponse:
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
        ListAssistantFilesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.list_assistant_files(
                assistant_id="assistant_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_assistant_files(
            assistant_id, limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

    async def create_assistant_file(
        self, assistant_id: str, *, file_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AssistantFileObject:
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
        AssistantFileObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.create_assistant_file(
                assistant_id="file-abc123",
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_assistant_file(
            assistant_id, file_id=file_id, request_options=request_options
        )
        return _response.data

    async def get_assistant_file(
        self, assistant_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AssistantFileObject:
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
        AssistantFileObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.get_assistant_file(
                assistant_id="assistant_id",
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_assistant_file(assistant_id, file_id, request_options=request_options)
        return _response.data

    async def delete_assistant_file(
        self, assistant_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteAssistantFileResponse:
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
        DeleteAssistantFileResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.delete_assistant_file(
                assistant_id="assistant_id",
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_assistant_file(assistant_id, file_id, request_options=request_options)
        return _response.data

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
    ) -> ListMessageFilesResponse:
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
        ListMessageFilesResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.list_message_files(
                thread_id="thread_id",
                message_id="message_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_message_files(
            thread_id, message_id, limit=limit, order=order, after=after, before=before, request_options=request_options
        )
        return _response.data

    async def get_message_file(
        self, thread_id: str, message_id: str, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MessageFileObject:
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
        MessageFileObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.assistants.get_message_file(
                thread_id="thread_abc123",
                message_id="msg_abc123",
                file_id="file-abc123",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_message_file(
            thread_id, message_id, file_id, request_options=request_options
        )
        return _response.data
