

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.algorithm_advisory import AlgorithmAdvisory
from .raw_client import AsyncRawAdvisoryClient, RawAdvisoryClient
from .types.auto_apply_advisories_response import AutoApplyAdvisoriesResponse
from .types.check_advisories_response import CheckAdvisoriesResponse
from .types.get_algorithm_advisories_response import GetAlgorithmAdvisoriesResponse
from .types.publish_advisory_response import PublishAdvisoryResponse


OMIT = typing.cast(typing.Any, ...)


class AdvisoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdvisoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdvisoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdvisoryClient
        """
        return self._raw_client

    def get_algorithm_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAlgorithmAdvisoriesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAlgorithmAdvisoriesResponse
            Published algorithm advisories

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.advisory.get_algorithm_advisories()
        """
        _response = self._raw_client.get_algorithm_advisories(request_options=request_options)
        return _response.data

    def publish_advisory(
        self, *, advisory: AlgorithmAdvisory, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishAdvisoryResponse:
        """
        Publishes a governance-signed algorithm advisory (deprecate/warn/revoke).

        Parameters
        ----------
        advisory : AlgorithmAdvisory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishAdvisoryResponse
            Advisory published

        Examples
        --------
        from fern import (
            AlgorithmAdvisory,
            AlgorithmAdvisoryAction,
            AlgorithmAdvisoryType,
            FernApi,
        )

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.advisory.publish_advisory(
            advisory=AlgorithmAdvisory(
                type=AlgorithmAdvisoryType.ALGORITHM_ADVISORY,
                advisory_id="advisory_id",
                affected_algorithms=["affected_algorithms"],
                action=AlgorithmAdvisoryAction.DEPRECATE,
            ),
        )
        """
        _response = self._raw_client.publish_advisory(advisory=advisory, request_options=request_options)
        return _response.data

    def check_advisories(self, *, request_options: typing.Optional[RequestOptions] = None) -> CheckAdvisoriesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckAdvisoriesResponse
            Active advisory status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.advisory.check_advisories()
        """
        _response = self._raw_client.check_advisories(request_options=request_options)
        return _response.data

    def auto_apply_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AutoApplyAdvisoriesResponse:
        """
        Scans active advisories and automatically updates the verifier policy
        by removing deprecated/revoked algorithms and adding replacements.
        May auto-switch to pq_only mode if all classical algorithms are removed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutoApplyAdvisoriesResponse
            Advisory auto-apply result

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.advisory.auto_apply_advisories()
        """
        _response = self._raw_client.auto_apply_advisories(request_options=request_options)
        return _response.data


class AsyncAdvisoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdvisoryClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdvisoryClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdvisoryClient
        """
        return self._raw_client

    async def get_algorithm_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAlgorithmAdvisoriesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetAlgorithmAdvisoriesResponse
            Published algorithm advisories

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.advisory.get_algorithm_advisories()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_algorithm_advisories(request_options=request_options)
        return _response.data

    async def publish_advisory(
        self, *, advisory: AlgorithmAdvisory, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishAdvisoryResponse:
        """
        Publishes a governance-signed algorithm advisory (deprecate/warn/revoke).

        Parameters
        ----------
        advisory : AlgorithmAdvisory

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishAdvisoryResponse
            Advisory published

        Examples
        --------
        import asyncio

        from fern import (
            AlgorithmAdvisory,
            AlgorithmAdvisoryAction,
            AlgorithmAdvisoryType,
            AsyncFernApi,
        )

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.advisory.publish_advisory(
                advisory=AlgorithmAdvisory(
                    type=AlgorithmAdvisoryType.ALGORITHM_ADVISORY,
                    advisory_id="advisory_id",
                    affected_algorithms=["affected_algorithms"],
                    action=AlgorithmAdvisoryAction.DEPRECATE,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_advisory(advisory=advisory, request_options=request_options)
        return _response.data

    async def check_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckAdvisoriesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckAdvisoriesResponse
            Active advisory status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.advisory.check_advisories()


        asyncio.run(main())
        """
        _response = await self._raw_client.check_advisories(request_options=request_options)
        return _response.data

    async def auto_apply_advisories(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AutoApplyAdvisoriesResponse:
        """
        Scans active advisories and automatically updates the verifier policy
        by removing deprecated/revoked algorithms and adding replacements.
        May auto-switch to pq_only mode if all classical algorithms are removed.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AutoApplyAdvisoriesResponse
            Advisory auto-apply result

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.advisory.auto_apply_advisories()


        asyncio.run(main())
        """
        _response = await self._raw_client.auto_apply_advisories(request_options=request_options)
        return _response.data
