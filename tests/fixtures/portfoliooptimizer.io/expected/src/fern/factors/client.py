

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawFactorsClient, RawFactorsClient
from .types.post_factors_residualization_request_factors_item import PostFactorsResidualizationRequestFactorsItem
from .types.post_factors_residualization_response import PostFactorsResidualizationResponse


OMIT = typing.cast(typing.Any, ...)


class FactorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFactorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFactorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFactorsClient
        """
        return self._raw_client

    def residualization(
        self,
        *,
        factors: typing.Sequence[PostFactorsResidualizationRequestFactorsItem],
        residualized_factor: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostFactorsResidualizationResponse:
        """
        Compute the residuals of a factor against a set of factors, using a returns-based linear regression analysis.

        References
        * [Factor Research, Factor Exposure Analysis: Exploring Residualization](https://insights.factorresearch.com/research-factor-exposure-analysis-exploring-residualization/)
        * [Catalina B. Garcia, Román Salmeron, Claudia Garcia & Jose Garcia (2019): Residualization: justification, properties and application, Journal of Applied Statistics](https://doi.org/10.1080/02664763.2019.1701638)

        Parameters
        ----------
        factors : typing.Sequence[PostFactorsResidualizationRequestFactorsItem]

        residualized_factor : int
            The index of the factor to residualize

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostFactorsResidualizationResponse
            OK

        Examples
        --------
        from fern.factors import PostFactorsResidualizationRequestFactorsItem

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.factors.residualization(
            factors=[
                PostFactorsResidualizationRequestFactorsItem(
                    factor_returns=[0.01, 0.02, -0.01],
                ),
                PostFactorsResidualizationRequestFactorsItem(
                    factor_returns=[0.025, 0.005, -0.02],
                ),
            ],
            residualized_factor=1,
        )
        """
        _response = self._raw_client.residualization(
            factors=factors, residualized_factor=residualized_factor, request_options=request_options
        )
        return _response.data


class AsyncFactorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFactorsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFactorsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFactorsClient
        """
        return self._raw_client

    async def residualization(
        self,
        *,
        factors: typing.Sequence[PostFactorsResidualizationRequestFactorsItem],
        residualized_factor: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostFactorsResidualizationResponse:
        """
        Compute the residuals of a factor against a set of factors, using a returns-based linear regression analysis.

        References
        * [Factor Research, Factor Exposure Analysis: Exploring Residualization](https://insights.factorresearch.com/research-factor-exposure-analysis-exploring-residualization/)
        * [Catalina B. Garcia, Román Salmeron, Claudia Garcia & Jose Garcia (2019): Residualization: justification, properties and application, Journal of Applied Statistics](https://doi.org/10.1080/02664763.2019.1701638)

        Parameters
        ----------
        factors : typing.Sequence[PostFactorsResidualizationRequestFactorsItem]

        residualized_factor : int
            The index of the factor to residualize

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostFactorsResidualizationResponse
            OK

        Examples
        --------
        import asyncio

        from fern.factors import PostFactorsResidualizationRequestFactorsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.factors.residualization(
                factors=[
                    PostFactorsResidualizationRequestFactorsItem(
                        factor_returns=[0.01, 0.02, -0.01],
                    ),
                    PostFactorsResidualizationRequestFactorsItem(
                        factor_returns=[0.025, 0.005, -0.02],
                    ),
                ],
                residualized_factor=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.residualization(
            factors=factors, residualized_factor=residualized_factor, request_options=request_options
        )
        return _response.data
