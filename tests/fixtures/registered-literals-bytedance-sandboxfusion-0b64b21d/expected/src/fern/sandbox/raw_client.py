

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.http_validation_error import HttpValidationError
from ..types.run_code_response_output import RunCodeResponseOutput
from ..types.run_jupyter_response import RunJupyterResponse
from .types.run_code_request_language import RunCodeRequestLanguage
from .types.run_jupyter_request_kernel import RunJupyterRequestKernel
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSandboxClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def run_code(
        self,
        *,
        code: str,
        language: RunCodeRequestLanguage,
        compile_timeout: typing.Optional[float] = OMIT,
        run_timeout: typing.Optional[float] = OMIT,
        stdin: typing.Optional[str] = OMIT,
        files: typing.Optional[typing.Dict[str, str]] = OMIT,
        fetch_files: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunCodeResponseOutput]:
        """
        Parameters
        ----------
        code : str
            the code to run

        language : RunCodeRequestLanguage
            the language or execution mode to run the code

        compile_timeout : typing.Optional[float]
            compile timeout for compiled languages

        run_timeout : typing.Optional[float]
            code run timeout

        stdin : typing.Optional[str]
            optional string to pass into stdin

        files : typing.Optional[typing.Dict[str, str]]
            a dict from file path to base64 encoded file content

        fetch_files : typing.Optional[typing.Sequence[str]]
            a list of file paths to fetch after code execution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunCodeResponseOutput]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "run_code",
            method="POST",
            json={
                "compile_timeout": compile_timeout,
                "run_timeout": run_timeout,
                "code": code,
                "stdin": stdin,
                "language": language,
                "files": files,
                "fetch_files": fetch_files,
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
                    RunCodeResponseOutput,
                    parse_obj_as(
                        type_=RunCodeResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def run_code_in_jupyter(
        self,
        *,
        cells: typing.Sequence[str],
        cell_timeout: typing.Optional[float] = OMIT,
        total_timeout: typing.Optional[float] = OMIT,
        kernel: typing.Optional[RunJupyterRequestKernel] = OMIT,
        files: typing.Optional[typing.Dict[str, str]] = OMIT,
        fetch_files: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[RunJupyterResponse]:
        """
        Parameters
        ----------
        cells : typing.Sequence[str]
            list of code blocks to run in jupyter notebook

        cell_timeout : typing.Optional[float]
            max run time for each of the cells

        total_timeout : typing.Optional[float]
            max run time for all the cells

        kernel : typing.Optional[RunJupyterRequestKernel]

        files : typing.Optional[typing.Dict[str, str]]
            a dict from file path to base64 encoded file content

        fetch_files : typing.Optional[typing.Sequence[str]]
            a list of file paths to fetch after code execution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RunJupyterResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "run_jupyter",
            method="POST",
            json={
                "cells": cells,
                "cell_timeout": cell_timeout,
                "total_timeout": total_timeout,
                "kernel": kernel,
                "files": files,
                "fetch_files": fetch_files,
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
                    RunJupyterResponse,
                    parse_obj_as(
                        type_=RunJupyterResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawSandboxClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def run_code(
        self,
        *,
        code: str,
        language: RunCodeRequestLanguage,
        compile_timeout: typing.Optional[float] = OMIT,
        run_timeout: typing.Optional[float] = OMIT,
        stdin: typing.Optional[str] = OMIT,
        files: typing.Optional[typing.Dict[str, str]] = OMIT,
        fetch_files: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunCodeResponseOutput]:
        """
        Parameters
        ----------
        code : str
            the code to run

        language : RunCodeRequestLanguage
            the language or execution mode to run the code

        compile_timeout : typing.Optional[float]
            compile timeout for compiled languages

        run_timeout : typing.Optional[float]
            code run timeout

        stdin : typing.Optional[str]
            optional string to pass into stdin

        files : typing.Optional[typing.Dict[str, str]]
            a dict from file path to base64 encoded file content

        fetch_files : typing.Optional[typing.Sequence[str]]
            a list of file paths to fetch after code execution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunCodeResponseOutput]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "run_code",
            method="POST",
            json={
                "compile_timeout": compile_timeout,
                "run_timeout": run_timeout,
                "code": code,
                "stdin": stdin,
                "language": language,
                "files": files,
                "fetch_files": fetch_files,
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
                    RunCodeResponseOutput,
                    parse_obj_as(
                        type_=RunCodeResponseOutput,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def run_code_in_jupyter(
        self,
        *,
        cells: typing.Sequence[str],
        cell_timeout: typing.Optional[float] = OMIT,
        total_timeout: typing.Optional[float] = OMIT,
        kernel: typing.Optional[RunJupyterRequestKernel] = OMIT,
        files: typing.Optional[typing.Dict[str, str]] = OMIT,
        fetch_files: typing.Optional[typing.Sequence[str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[RunJupyterResponse]:
        """
        Parameters
        ----------
        cells : typing.Sequence[str]
            list of code blocks to run in jupyter notebook

        cell_timeout : typing.Optional[float]
            max run time for each of the cells

        total_timeout : typing.Optional[float]
            max run time for all the cells

        kernel : typing.Optional[RunJupyterRequestKernel]

        files : typing.Optional[typing.Dict[str, str]]
            a dict from file path to base64 encoded file content

        fetch_files : typing.Optional[typing.Sequence[str]]
            a list of file paths to fetch after code execution

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RunJupyterResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "run_jupyter",
            method="POST",
            json={
                "cells": cells,
                "cell_timeout": cell_timeout,
                "total_timeout": total_timeout,
                "kernel": kernel,
                "files": files,
                "fetch_files": fetch_files,
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
                    RunJupyterResponse,
                    parse_obj_as(
                        type_=RunJupyterResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
