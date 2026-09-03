

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.process_initialization_response import ProcessInitializationResponse
from ..types.process_status import ProcessStatus
from ..types.process_step_response import ProcessStepResponse
from .raw_client import AsyncRawReferenzprozessClient, RawReferenzprozessClient
from .types.process_initialization_request_customer_context import ProcessInitializationRequestCustomerContext
from .types.process_initialization_request_industry import ProcessInitializationRequestIndustry
from .types.process_initialization_request_process_configuration import ProcessInitializationRequestProcessConfiguration
from .types.process_initialization_request_use_case import ProcessInitializationRequestUseCase


OMIT = typing.cast(typing.Any, ...)


class ReferenzprozessClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawReferenzprozessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawReferenzprozessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawReferenzprozessClient
        """
        return self._raw_client

    def initialize_process(
        self,
        *,
        industry: ProcessInitializationRequestIndustry,
        use_case: ProcessInitializationRequestUseCase,
        customer_context: ProcessInitializationRequestCustomerContext,
        process_configuration: typing.Optional[ProcessInitializationRequestProcessConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessInitializationResponse:
        """
        Initiiert den universellen 10-Stufen-Referenzprozess für Customer Onboarding

        Parameters
        ----------
        industry : ProcessInitializationRequestIndustry
            Ziel-Ecosystem für den Prozess

        use_case : ProcessInitializationRequestUseCase
            Spezifischer Use Case

        customer_context : ProcessInitializationRequestCustomerContext

        process_configuration : typing.Optional[ProcessInitializationRequestProcessConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessInitializationResponse
            Referenzprozess erfolgreich initialisiert

        Examples
        --------
        from fern.referenzprozess import (
            ProcessInitializationRequestCustomerContext,
            ProcessInitializationRequestIndustry,
            ProcessInitializationRequestUseCase,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.referenzprozess.initialize_process(
            industry=ProcessInitializationRequestIndustry.BANKING,
            use_case=ProcessInitializationRequestUseCase.KUNDENBEZIEHUNGSEROFFNUNG,
            customer_context=ProcessInitializationRequestCustomerContext(),
        )
        """
        _response = self._raw_client.initialize_process(
            industry=industry,
            use_case=use_case,
            customer_context=customer_context,
            process_configuration=process_configuration,
            request_options=request_options,
        )
        return _response.data

    def execute_process_step(
        self,
        process_id: str,
        step_number: int,
        *,
        step_data: typing.Dict[str, typing.Any],
        skip_to_step: typing.Optional[int] = OMIT,
        customer_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessStepResponse:
        """
        Führt einen spezifischen Schritt (1-10) des Referenzprozesses aus

        Parameters
        ----------
        process_id : str

        step_number : int

        step_data : typing.Dict[str, typing.Any]
            Step-spezifische Daten

        skip_to_step : typing.Optional[int]

        customer_consent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessStepResponse
            Prozessschritt erfolgreich ausgeführt

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.referenzprozess.execute_process_step(
            process_id="processId",
            step_number=1,
            step_data={"key": "value"},
        )
        """
        _response = self._raw_client.execute_process_step(
            process_id,
            step_number,
            step_data=step_data,
            skip_to_step=skip_to_step,
            customer_consent=customer_consent,
            request_options=request_options,
        )
        return _response.data

    def get_process_status(
        self, process_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessStatus:
        """
        Ruft den aktuellen Status und Fortschritt des Referenzprozesses ab

        Parameters
        ----------
        process_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessStatus
            Prozess-Status erfolgreich abgerufen

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.referenzprozess.get_process_status(
            process_id="processId",
        )
        """
        _response = self._raw_client.get_process_status(process_id, request_options=request_options)
        return _response.data


class AsyncReferenzprozessClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawReferenzprozessClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawReferenzprozessClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawReferenzprozessClient
        """
        return self._raw_client

    async def initialize_process(
        self,
        *,
        industry: ProcessInitializationRequestIndustry,
        use_case: ProcessInitializationRequestUseCase,
        customer_context: ProcessInitializationRequestCustomerContext,
        process_configuration: typing.Optional[ProcessInitializationRequestProcessConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessInitializationResponse:
        """
        Initiiert den universellen 10-Stufen-Referenzprozess für Customer Onboarding

        Parameters
        ----------
        industry : ProcessInitializationRequestIndustry
            Ziel-Ecosystem für den Prozess

        use_case : ProcessInitializationRequestUseCase
            Spezifischer Use Case

        customer_context : ProcessInitializationRequestCustomerContext

        process_configuration : typing.Optional[ProcessInitializationRequestProcessConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessInitializationResponse
            Referenzprozess erfolgreich initialisiert

        Examples
        --------
        import asyncio

        from fern.referenzprozess import (
            ProcessInitializationRequestCustomerContext,
            ProcessInitializationRequestIndustry,
            ProcessInitializationRequestUseCase,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.referenzprozess.initialize_process(
                industry=ProcessInitializationRequestIndustry.BANKING,
                use_case=ProcessInitializationRequestUseCase.KUNDENBEZIEHUNGSEROFFNUNG,
                customer_context=ProcessInitializationRequestCustomerContext(),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.initialize_process(
            industry=industry,
            use_case=use_case,
            customer_context=customer_context,
            process_configuration=process_configuration,
            request_options=request_options,
        )
        return _response.data

    async def execute_process_step(
        self,
        process_id: str,
        step_number: int,
        *,
        step_data: typing.Dict[str, typing.Any],
        skip_to_step: typing.Optional[int] = OMIT,
        customer_consent: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProcessStepResponse:
        """
        Führt einen spezifischen Schritt (1-10) des Referenzprozesses aus

        Parameters
        ----------
        process_id : str

        step_number : int

        step_data : typing.Dict[str, typing.Any]
            Step-spezifische Daten

        skip_to_step : typing.Optional[int]

        customer_consent : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessStepResponse
            Prozessschritt erfolgreich ausgeführt

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.referenzprozess.execute_process_step(
                process_id="processId",
                step_number=1,
                step_data={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.execute_process_step(
            process_id,
            step_number,
            step_data=step_data,
            skip_to_step=skip_to_step,
            customer_consent=customer_consent,
            request_options=request_options,
        )
        return _response.data

    async def get_process_status(
        self, process_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessStatus:
        """
        Ruft den aktuellen Status und Fortschritt des Referenzprozesses ab

        Parameters
        ----------
        process_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessStatus
            Prozess-Status erfolgreich abgerufen

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.referenzprozess.get_process_status(
                process_id="processId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_process_status(process_id, request_options=request_options)
        return _response.data
