

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.v1project_advisors_response_output import V1ProjectAdvisorsResponseOutput
from .raw_client import AsyncRawAdvisorsClient, RawAdvisorsClient
from .types.v1get_security_advisors_request_lint_type import V1GetSecurityAdvisorsRequestLintType


class AdvisorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdvisorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdvisorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdvisorsClient
        """
        return self._raw_client

    def v1get_performance_advisors(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ProjectAdvisorsResponseOutput:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectAdvisorsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.advisors.v1get_performance_advisors(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_performance_advisors(ref, request_options=request_options)
        return _response.data

    def v1get_security_advisors(
        self,
        ref: str,
        *,
        lint_type: typing.Optional[V1GetSecurityAdvisorsRequestLintType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1ProjectAdvisorsResponseOutput:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        lint_type : typing.Optional[V1GetSecurityAdvisorsRequestLintType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectAdvisorsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.advisors.v1get_security_advisors(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_security_advisors(ref, lint_type=lint_type, request_options=request_options)
        return _response.data


class AsyncAdvisorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdvisorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdvisorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdvisorsClient
        """
        return self._raw_client

    async def v1get_performance_advisors(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ProjectAdvisorsResponseOutput:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectAdvisorsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.advisors.v1get_performance_advisors(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_performance_advisors(ref, request_options=request_options)
        return _response.data

    async def v1get_security_advisors(
        self,
        ref: str,
        *,
        lint_type: typing.Optional[V1GetSecurityAdvisorsRequestLintType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> V1ProjectAdvisorsResponseOutput:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        lint_type : typing.Optional[V1GetSecurityAdvisorsRequestLintType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ProjectAdvisorsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.advisors.v1get_security_advisors(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_security_advisors(
            ref, lint_type=lint_type, request_options=request_options
        )
        return _response.data
