

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok_response_risk_coverage_pension import OkResponseRiskCoveragePension
from .raw_client import AsyncRawRiskCoveragesClient, RawRiskCoveragesClient


class RiskCoveragesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRiskCoveragesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRiskCoveragesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRiskCoveragesClient
        """
        return self._raw_client

    def get_pension_risk_coverages(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponseRiskCoveragePension:
        """
        Método para obter informações de Previdência de Cobertura de Riscos.

        Parameters
        ----------
        page : typing.Optional[int]
            Número da página que está sendo requisitada (o valor da primeira página é 1).

        page_size : typing.Optional[int]
            Quantidade total de registros por páginas.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponseRiskCoveragePension
            Dados de previdência de risco obtidos com sucesso da instituição.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.risk_coverages.get_pension_risk_coverages()
        """
        _response = self._raw_client.get_pension_risk_coverages(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data


class AsyncRiskCoveragesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRiskCoveragesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRiskCoveragesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRiskCoveragesClient
        """
        return self._raw_client

    async def get_pension_risk_coverages(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponseRiskCoveragePension:
        """
        Método para obter informações de Previdência de Cobertura de Riscos.

        Parameters
        ----------
        page : typing.Optional[int]
            Número da página que está sendo requisitada (o valor da primeira página é 1).

        page_size : typing.Optional[int]
            Quantidade total de registros por páginas.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponseRiskCoveragePension
            Dados de previdência de risco obtidos com sucesso da instituição.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.risk_coverages.get_pension_risk_coverages()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pension_risk_coverages(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data
