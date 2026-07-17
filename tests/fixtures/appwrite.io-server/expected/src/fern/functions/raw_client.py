

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.execution import Execution
from ..types.execution_list import ExecutionList
from ..types.function import Function
from ..types.function_list import FunctionList
from ..types.tag import Tag
from ..types.tag_list import TagList
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFunctionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[FunctionList]:
        """
        Get a list of all the project's functions. You can use the query params to filter your results.

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FunctionList]
            Functions List
        """
        _response = self._client_wrapper.httpx_client.request(
            "functions",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FunctionList,
                    parse_obj_as(
                        type_=FunctionList,
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

    def create(
        self,
        *,
        execute: typing.Sequence[str],
        name: str,
        runtime: str,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Function]:
        """
        Create a new function. You can pass a list of [permissions](/docs/permissions) to allow different project users or team with access to execute the function using the client API.

        Parameters
        ----------
        execute : typing.Sequence[str]
            An array of strings with execution permissions. By default no user is granted with any execute permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        name : str
            Function name. Max length: 128 chars.

        runtime : str
            Execution runtime.

        events : typing.Optional[typing.Sequence[str]]
            Events list.

        schedule : typing.Optional[str]
            Schedule CRON syntax.

        timeout : typing.Optional[int]
            Function maximum execution time in seconds.

        vars : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Function]
            Function
        """
        _response = self._client_wrapper.httpx_client.request(
            "functions",
            method="POST",
            json={
                "events": events,
                "execute": execute,
                "name": name,
                "runtime": runtime,
                "schedule": schedule,
                "timeout": timeout,
                "vars": vars,
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    def get(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Function]:
        """
        Get a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Function]
            Function
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    def update(
        self,
        function_id: str,
        *,
        execute: typing.Sequence[str],
        name: str,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Function]:
        """
        Update function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        execute : typing.Sequence[str]
            An array of strings with execution permissions. By default no user is granted with any execute permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        name : str
            Function name. Max length: 128 chars.

        events : typing.Optional[typing.Sequence[str]]
            Events list.

        schedule : typing.Optional[str]
            Schedule CRON syntax.

        timeout : typing.Optional[int]
            Function maximum execution time in seconds.

        vars : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Function]
            Function
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}",
            method="PUT",
            json={
                "events": events,
                "execute": execute,
                "name": name,
                "schedule": schedule,
                "timeout": timeout,
                "vars": vars,
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    def delete(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_executions(
        self,
        function_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ExecutionList]:
        """
        Get a list of all the current user function execution logs. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's executions. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        function_id : str
            Function unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ExecutionList]
            Executions List
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/executions",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExecutionList,
                    parse_obj_as(
                        type_=ExecutionList,
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

    def create_execution(
        self,
        function_id: str,
        *,
        data: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Execution]:
        """
        Trigger a function execution. The returned object will return you the current execution status. You can ping the `Get Execution` endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        data : typing.Optional[str]
            String of custom data to send to function.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Execution]
            Execution
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/executions",
            method="POST",
            json={
                "data": data,
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
                    Execution,
                    parse_obj_as(
                        type_=Execution,
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

    def get_execution(
        self, function_id: str, execution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Execution]:
        """
        Get a function execution log by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        execution_id : str
            Execution unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Execution]
            Execution
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/executions/{encode_path_param(execution_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Execution,
                    parse_obj_as(
                        type_=Execution,
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

    def update_tag(
        self, function_id: str, *, tag: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Function]:
        """
        Update the function code tag ID using the unique function ID. Use this endpoint to switch the code tag that should be executed by the execution endpoint.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Function]
            Function
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tag",
            method="PATCH",
            json={
                "tag": tag,
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    def list_tags(
        self,
        function_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[TagList]:
        """
        Get a list of all the project's code tags. You can use the query params to filter your results.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[TagList]
            Tags List
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tags",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TagList,
                    parse_obj_as(
                        type_=TagList,
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

    def create_tag(
        self, function_id: str, *, code: str, command: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Tag]:
        """
        Create a new function code tag. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you'll need to update the function's tag to use your new tag UID.

        This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](/docs/functions).

        Use the "command" param to set the entry point used to execute your code.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        code : str
            Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.

        command : str
            Code execution command.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]
            Tag
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tags",
            method="POST",
            data={
                "code": code,
                "command": command,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    def get_tag(
        self, function_id: str, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Tag]:
        """
        Get a code tag by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag_id : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Tag]
            Tag
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tags/{encode_path_param(tag_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    def delete_tag(
        self, function_id: str, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Delete a code tag by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag_id : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tags/{encode_path_param(tag_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFunctionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[FunctionList]:
        """
        Get a list of all the project's functions. You can use the query params to filter your results.

        Parameters
        ----------
        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FunctionList]
            Functions List
        """
        _response = await self._client_wrapper.httpx_client.request(
            "functions",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FunctionList,
                    parse_obj_as(
                        type_=FunctionList,
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

    async def create(
        self,
        *,
        execute: typing.Sequence[str],
        name: str,
        runtime: str,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Function]:
        """
        Create a new function. You can pass a list of [permissions](/docs/permissions) to allow different project users or team with access to execute the function using the client API.

        Parameters
        ----------
        execute : typing.Sequence[str]
            An array of strings with execution permissions. By default no user is granted with any execute permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        name : str
            Function name. Max length: 128 chars.

        runtime : str
            Execution runtime.

        events : typing.Optional[typing.Sequence[str]]
            Events list.

        schedule : typing.Optional[str]
            Schedule CRON syntax.

        timeout : typing.Optional[int]
            Function maximum execution time in seconds.

        vars : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Function]
            Function
        """
        _response = await self._client_wrapper.httpx_client.request(
            "functions",
            method="POST",
            json={
                "events": events,
                "execute": execute,
                "name": name,
                "runtime": runtime,
                "schedule": schedule,
                "timeout": timeout,
                "vars": vars,
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    async def get(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Function]:
        """
        Get a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Function]
            Function
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    async def update(
        self,
        function_id: str,
        *,
        execute: typing.Sequence[str],
        name: str,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        schedule: typing.Optional[str] = OMIT,
        timeout: typing.Optional[int] = OMIT,
        vars: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Function]:
        """
        Update function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        execute : typing.Sequence[str]
            An array of strings with execution permissions. By default no user is granted with any execute permissions. [learn more about permissions](/docs/permissions) and get a full list of available permissions.

        name : str
            Function name. Max length: 128 chars.

        events : typing.Optional[typing.Sequence[str]]
            Events list.

        schedule : typing.Optional[str]
            Schedule CRON syntax.

        timeout : typing.Optional[int]
            Function maximum execution time in seconds.

        vars : typing.Optional[typing.Dict[str, typing.Any]]
            Key-value JSON object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Function]
            Function
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}",
            method="PUT",
            json={
                "events": events,
                "execute": execute,
                "name": name,
                "schedule": schedule,
                "timeout": timeout,
                "vars": vars,
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    async def delete(
        self, function_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a function by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_executions(
        self,
        function_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ExecutionList]:
        """
        Get a list of all the current user function execution logs. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project's executions. [Learn more about different API modes](/docs/admin).

        Parameters
        ----------
        function_id : str
            Function unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ExecutionList]
            Executions List
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/executions",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ExecutionList,
                    parse_obj_as(
                        type_=ExecutionList,
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

    async def create_execution(
        self,
        function_id: str,
        *,
        data: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Execution]:
        """
        Trigger a function execution. The returned object will return you the current execution status. You can ping the `Get Execution` endpoint to get updates on the current execution status. Once this endpoint is called, your function execution process will start asynchronously.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        data : typing.Optional[str]
            String of custom data to send to function.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Execution]
            Execution
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/executions",
            method="POST",
            json={
                "data": data,
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
                    Execution,
                    parse_obj_as(
                        type_=Execution,
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

    async def get_execution(
        self, function_id: str, execution_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Execution]:
        """
        Get a function execution log by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        execution_id : str
            Execution unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Execution]
            Execution
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/executions/{encode_path_param(execution_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Execution,
                    parse_obj_as(
                        type_=Execution,
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

    async def update_tag(
        self, function_id: str, *, tag: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Function]:
        """
        Update the function code tag ID using the unique function ID. Use this endpoint to switch the code tag that should be executed by the execution endpoint.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Function]
            Function
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tag",
            method="PATCH",
            json={
                "tag": tag,
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
                    Function,
                    parse_obj_as(
                        type_=Function,
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

    async def list_tags(
        self,
        function_id: str,
        *,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        order_type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[TagList]:
        """
        Get a list of all the project's code tags. You can use the query params to filter your results.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        search : typing.Optional[str]
            Search term to filter your list results. Max length: 256 chars.

        limit : typing.Optional[int]
            Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.

        offset : typing.Optional[int]
            Results offset. The default value is 0. Use this param to manage pagination.

        order_type : typing.Optional[str]
            Order result by ASC or DESC order.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[TagList]
            Tags List
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tags",
            method="GET",
            params={
                "search": search,
                "limit": limit,
                "offset": offset,
                "orderType": order_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    TagList,
                    parse_obj_as(
                        type_=TagList,
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

    async def create_tag(
        self, function_id: str, *, code: str, command: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Tag]:
        """
        Create a new function code tag. Use this endpoint to upload a new version of your code function. To execute your newly uploaded code, you'll need to update the function's tag to use your new tag UID.

        This endpoint accepts a tar.gz file compressed with your code. Make sure to include any dependencies your code has within the compressed file. You can learn more about code packaging in the [Appwrite Cloud Functions tutorial](/docs/functions).

        Use the "command" param to set the entry point used to execute your code.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        code : str
            Gzip file with your code package. When used with the Appwrite CLI, pass the path to your code directory, and the CLI will automatically package your code. Use a path that is within the current directory.

        command : str
            Code execution command.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]
            Tag
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tags",
            method="POST",
            data={
                "code": code,
                "command": command,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    async def get_tag(
        self, function_id: str, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Tag]:
        """
        Get a code tag by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag_id : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Tag]
            Tag
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tags/{encode_path_param(tag_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Tag,
                    parse_obj_as(
                        type_=Tag,
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

    async def delete_tag(
        self, function_id: str, tag_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Delete a code tag by its unique ID.

        Parameters
        ----------
        function_id : str
            Function unique ID.

        tag_id : str
            Tag unique ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"functions/{encode_path_param(function_id)}/tags/{encode_path_param(tag_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
