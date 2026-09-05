

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawProbeClient, RawProbeClient
from .types.probe_rules_request_rules_item import ProbeRulesRequestRulesItem


OMIT = typing.cast(typing.Any, ...)


class ProbeClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProbeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProbeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProbeClient
        """
        return self._raw_client

    def rules(
        self,
        id: str,
        *,
        rules: typing.Sequence[ProbeRulesRequestRulesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        rules : typing.Sequence[ProbeRulesRequestRulesItem]
            Array of rules for the price table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.probe import (
            ProbeRulesRequestRulesItem,
            ProbeRulesRequestRulesItemContext,
            ProbeRulesRequestRulesItemContextDateRange,
            ProbeRulesRequestRulesItemContextMarkupRange,
        )

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.probe.rules(
            id="id",
            rules=[
                ProbeRulesRequestRulesItem(
                    context=ProbeRulesRequestRulesItemContext(
                        brands={"Brand ID": "2000002", "Brand Name": "Whiskas"},
                        categories={"Category ID": "1", "Category Name": "Alimentação"},
                        date_range=ProbeRulesRequestRulesItemContextDateRange(
                            from_="2022-01-23T19:00:00.000Z",
                            to="2023-10-26T00:00:00.000Z",
                        ),
                        markup_range=ProbeRulesRequestRulesItemContextMarkupRange(
                            from_=0,
                            to=200,
                        ),
                    ),
                    id=1,
                    percentual_modifier=0.0,
                )
            ],
        )
        """
        _response = self._raw_client.rules(id, rules=rules, request_options=request_options)
        return _response.data


class AsyncProbeClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProbeClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProbeClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProbeClient
        """
        return self._raw_client

    async def rules(
        self,
        id: str,
        *,
        rules: typing.Sequence[ProbeRulesRequestRulesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        id : str

        rules : typing.Sequence[ProbeRulesRequestRulesItem]
            Array of rules for the price table.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.probe import (
            ProbeRulesRequestRulesItem,
            ProbeRulesRequestRulesItemContext,
            ProbeRulesRequestRulesItemContextDateRange,
            ProbeRulesRequestRulesItemContextMarkupRange,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.probe.rules(
                id="id",
                rules=[
                    ProbeRulesRequestRulesItem(
                        context=ProbeRulesRequestRulesItemContext(
                            brands={"Brand ID": "2000002", "Brand Name": "Whiskas"},
                            categories={
                                "Category ID": "1",
                                "Category Name": "Alimentação",
                            },
                            date_range=ProbeRulesRequestRulesItemContextDateRange(
                                from_="2022-01-23T19:00:00.000Z",
                                to="2023-10-26T00:00:00.000Z",
                            ),
                            markup_range=ProbeRulesRequestRulesItemContextMarkupRange(
                                from_=0,
                                to=200,
                            ),
                        ),
                        id=1,
                        percentual_modifier=0.0,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.rules(id, rules=rules, request_options=request_options)
        return _response.data
