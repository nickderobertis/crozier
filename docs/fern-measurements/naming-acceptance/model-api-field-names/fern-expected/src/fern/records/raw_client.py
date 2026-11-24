

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.record import Record
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawRecordsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_record(
        self,
        *,
        kwargs_: typing.Optional[str] = OMIT,
        self_: typing.Optional[str] = OMIT,
        args: typing.Optional[str] = OMIT,
        json: typing.Optional[str] = OMIT,
        data: typing.Optional[str] = OMIT,
        files: typing.Optional[str] = OMIT,
        headers: typing.Optional[str] = OMIT,
        params: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        timeout: typing.Optional[str] = OMIT,
        cls: typing.Optional[str] = OMIT,
        client: typing.Optional[str] = OMIT,
        dict: typing.Optional[str] = OMIT,
        model_config: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        copy: typing.Optional[str] = OMIT,
        schema: typing.Optional[str] = OMIT,
        validate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Record]:
        """
        Parameters
        ----------
        kwargs_ : typing.Optional[str]

        self_ : typing.Optional[str]

        args : typing.Optional[str]

        json : typing.Optional[str]

        data : typing.Optional[str]

        files : typing.Optional[str]

        headers : typing.Optional[str]

        params : typing.Optional[str]

        content : typing.Optional[str]

        timeout : typing.Optional[str]

        cls : typing.Optional[str]

        client : typing.Optional[str]

        dict : typing.Optional[str]

        model_config : typing.Optional[str]

        type : typing.Optional[str]

        id : typing.Optional[str]

        copy : typing.Optional[str]

        schema : typing.Optional[str]

        validate : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Record]
            ok
        """
        _response = self._client_wrapper.httpx_client.request(
            "records",
            method="POST",
            json={
                "kwargs": kwargs_,
                "self": self_,
                "args": args,
                "json": json,
                "data": data,
                "files": files,
                "headers": headers,
                "params": params,
                "content": content,
                "timeout": timeout,
                "cls": cls,
                "client": client,
                "dict": dict,
                "model_config": model_config,
                "type": type,
                "id": id,
                "copy": copy,
                "schema": schema,
                "validate": validate,
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
                    Record,
                    parse_obj_as(
                        type_=Record,
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


class AsyncRawRecordsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_record(
        self,
        *,
        kwargs_: typing.Optional[str] = OMIT,
        self_: typing.Optional[str] = OMIT,
        args: typing.Optional[str] = OMIT,
        json: typing.Optional[str] = OMIT,
        data: typing.Optional[str] = OMIT,
        files: typing.Optional[str] = OMIT,
        headers: typing.Optional[str] = OMIT,
        params: typing.Optional[str] = OMIT,
        content: typing.Optional[str] = OMIT,
        timeout: typing.Optional[str] = OMIT,
        cls: typing.Optional[str] = OMIT,
        client: typing.Optional[str] = OMIT,
        dict: typing.Optional[str] = OMIT,
        model_config: typing.Optional[str] = OMIT,
        type: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        copy: typing.Optional[str] = OMIT,
        schema: typing.Optional[str] = OMIT,
        validate: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Record]:
        """
        Parameters
        ----------
        kwargs_ : typing.Optional[str]

        self_ : typing.Optional[str]

        args : typing.Optional[str]

        json : typing.Optional[str]

        data : typing.Optional[str]

        files : typing.Optional[str]

        headers : typing.Optional[str]

        params : typing.Optional[str]

        content : typing.Optional[str]

        timeout : typing.Optional[str]

        cls : typing.Optional[str]

        client : typing.Optional[str]

        dict : typing.Optional[str]

        model_config : typing.Optional[str]

        type : typing.Optional[str]

        id : typing.Optional[str]

        copy : typing.Optional[str]

        schema : typing.Optional[str]

        validate : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Record]
            ok
        """
        _response = await self._client_wrapper.httpx_client.request(
            "records",
            method="POST",
            json={
                "kwargs": kwargs_,
                "self": self_,
                "args": args,
                "json": json,
                "data": data,
                "files": files,
                "headers": headers,
                "params": params,
                "content": content,
                "timeout": timeout,
                "cls": cls,
                "client": client,
                "dict": dict,
                "model_config": model_config,
                "type": type,
                "id": id,
                "copy": copy,
                "schema": schema,
                "validate": validate,
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
                    Record,
                    parse_obj_as(
                        type_=Record,
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
