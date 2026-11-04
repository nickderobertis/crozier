

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok_response_survival_coverage_pension import OkResponseSurvivalCoveragePension
from .raw_client import AsyncRawSurvivalCoveragesClient, RawSurvivalCoveragesClient


class SurvivalCoveragesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSurvivalCoveragesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSurvivalCoveragesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSurvivalCoveragesClient
        """
        return self._raw_client

    def get_pension_survival_coverages(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponseSurvivalCoveragePension:
        """
        Método para obter informações de Previdência de Cobertura de Sobrevivência.

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
        OkResponseSurvivalCoveragePension
            Dados de previdência de sobrevivência obtidos com sucesso da instituição.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.survival_coverages.get_pension_survival_coverages()
        """
        _response = self._raw_client.get_pension_survival_coverages(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data


class AsyncSurvivalCoveragesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSurvivalCoveragesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSurvivalCoveragesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSurvivalCoveragesClient
        """
        return self._raw_client

    async def get_pension_survival_coverages(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OkResponseSurvivalCoveragePension:
        """
        Método para obter informações de Previdência de Cobertura de Sobrevivência.

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
        OkResponseSurvivalCoveragePension
            Dados de previdência de sobrevivência obtidos com sucesso da instituição.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.survival_coverages.get_pension_survival_coverages()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pension_survival_coverages(
            page=page, page_size=page_size, request_options=request_options
        )
        return _response.data
