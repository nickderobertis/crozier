

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.run_code_response_output import RunCodeResponseOutput
from ..types.run_jupyter_response import RunJupyterResponse
from .raw_client import AsyncRawSandboxClient, RawSandboxClient
from .types.run_code_request_language import RunCodeRequestLanguage
from .types.run_jupyter_request_kernel import RunJupyterRequestKernel


OMIT = typing.cast(typing.Any, ...)


class SandboxClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSandboxClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSandboxClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSandboxClient
        """
        return self._raw_client

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
    ) -> RunCodeResponseOutput:
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
        RunCodeResponseOutput
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sandbox.run_code(
            code='print("hello")',
            language="python",
        )
        """
        _response = self._raw_client.run_code(
            code=code,
            language=language,
            compile_timeout=compile_timeout,
            run_timeout=run_timeout,
            stdin=stdin,
            files=files,
            fetch_files=fetch_files,
            request_options=request_options,
        )
        return _response.data

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
    ) -> RunJupyterResponse:
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
        RunJupyterResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.sandbox.run_code_in_jupyter(
            cells=[
                "a = 123",
                "a",
                "print(a)",
                'import sys; sys.stderr.write("stderr message")',
                'raise RuntimeError("error message")',
            ],
        )
        """
        _response = self._raw_client.run_code_in_jupyter(
            cells=cells,
            cell_timeout=cell_timeout,
            total_timeout=total_timeout,
            kernel=kernel,
            files=files,
            fetch_files=fetch_files,
            request_options=request_options,
        )
        return _response.data


class AsyncSandboxClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSandboxClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSandboxClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSandboxClient
        """
        return self._raw_client

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
    ) -> RunCodeResponseOutput:
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
        RunCodeResponseOutput
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sandbox.run_code(
                code='print("hello")',
                language="python",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_code(
            code=code,
            language=language,
            compile_timeout=compile_timeout,
            run_timeout=run_timeout,
            stdin=stdin,
            files=files,
            fetch_files=fetch_files,
            request_options=request_options,
        )
        return _response.data

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
    ) -> RunJupyterResponse:
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
        RunJupyterResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.sandbox.run_code_in_jupyter(
                cells=[
                    "a = 123",
                    "a",
                    "print(a)",
                    'import sys; sys.stderr.write("stderr message")',
                    'raise RuntimeError("error message")',
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.run_code_in_jupyter(
            cells=cells,
            cell_timeout=cell_timeout,
            total_timeout=total_timeout,
            kernel=kernel,
            files=files,
            fetch_files=fetch_files,
            request_options=request_options,
        )
        return _response.data
