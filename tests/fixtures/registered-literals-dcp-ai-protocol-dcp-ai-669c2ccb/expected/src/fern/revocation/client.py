

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawRevocationClient, RawRevocationClient
from .types.check_revocation_response import CheckRevocationResponse
from .types.list_revocations_response import ListRevocationsResponse
from .types.publish_revocation_response import PublishRevocationResponse


OMIT = typing.cast(typing.Any, ...)


class RevocationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRevocationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRevocationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRevocationClient
        """
        return self._raw_client

    def list_revocations(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListRevocationsResponse:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRevocationsResponse
            List of revocation records

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.revocation.list_revocations()
        """
        _response = self._raw_client.list_revocations(request_options=request_options)
        return _response.data

    def publish_revocation(
        self,
        *,
        dcp_version: str,
        agent_id: str,
        human_id: str,
        timestamp: dt.datetime,
        reason: str,
        signature: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishRevocationResponse:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        dcp_version : str

        agent_id : str

        human_id : str

        timestamp : dt.datetime

        reason : str

        signature : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishRevocationResponse
            Revocation published

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.revocation.publish_revocation(
            dcp_version="dcp_version",
            agent_id="agent_id",
            human_id="human_id",
            timestamp=datetime.datetime.fromisoformat(
                "2024-01-15 09:30:00+00:00",
            ),
            reason="reason",
            signature="signature",
        )
        """
        _response = self._raw_client.publish_revocation(
            dcp_version=dcp_version,
            agent_id=agent_id,
            human_id=human_id,
            timestamp=timestamp,
            reason=reason,
            signature=signature,
            request_options=request_options,
        )
        return _response.data

    def check_revocation(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckRevocationResponse:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckRevocationResponse
            Revocation status

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )
        client.revocation.check_revocation(
            agent_id="agent_id",
        )
        """
        _response = self._raw_client.check_revocation(agent_id, request_options=request_options)
        return _response.data


class AsyncRevocationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRevocationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRevocationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRevocationClient
        """
        return self._raw_client

    async def list_revocations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListRevocationsResponse:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListRevocationsResponse
            List of revocation records

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.revocation.list_revocations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_revocations(request_options=request_options)
        return _response.data

    async def publish_revocation(
        self,
        *,
        dcp_version: str,
        agent_id: str,
        human_id: str,
        timestamp: dt.datetime,
        reason: str,
        signature: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishRevocationResponse:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        dcp_version : str

        agent_id : str

        human_id : str

        timestamp : dt.datetime

        reason : str

        signature : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishRevocationResponse
            Revocation published

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.revocation.publish_revocation(
                dcp_version="dcp_version",
                agent_id="agent_id",
                human_id="human_id",
                timestamp=datetime.datetime.fromisoformat(
                    "2024-01-15 09:30:00+00:00",
                ),
                reason="reason",
                signature="signature",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publish_revocation(
            dcp_version=dcp_version,
            agent_id=agent_id,
            human_id=human_id,
            timestamp=timestamp,
            reason=reason,
            signature=signature,
            request_options=request_options,
        )
        return _response.data

    async def check_revocation(
        self, agent_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> CheckRevocationResponse:
        """
        Available on the revocation service (port 3003).

        Parameters
        ----------
        agent_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CheckRevocationResponse
            Revocation status

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            dcp_api_key="YOUR_DCP_API_KEY",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.revocation.check_revocation(
                agent_id="agent_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_revocation(agent_id, request_options=request_options)
        return _response.data
