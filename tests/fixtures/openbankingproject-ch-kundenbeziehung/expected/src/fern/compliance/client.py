

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.mi_fid_assessment_response import MiFidAssessmentResponse
from .raw_client import AsyncRawComplianceClient, RawComplianceClient
from .types.mi_fid_assessment_request_financial_situation import MiFidAssessmentRequestFinancialSituation
from .types.mi_fid_assessment_request_investment_experience import MiFidAssessmentRequestInvestmentExperience


OMIT = typing.cast(typing.Any, ...)


class ComplianceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawComplianceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawComplianceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawComplianceClient
        """
        return self._raw_client

    def perform_mi_fid_assessment(
        self,
        *,
        customer_id: str,
        investment_objectives: typing.Sequence[str],
        existing_assessments: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        investment_experience: typing.Optional[MiFidAssessmentRequestInvestmentExperience] = OMIT,
        financial_situation: typing.Optional[MiFidAssessmentRequestFinancialSituation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MiFidAssessmentResponse:
        """
        Führt MiFID II konforme Anlageeignungsprüfung durch

        Parameters
        ----------
        customer_id : str

        investment_objectives : typing.Sequence[str]

        existing_assessments : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        investment_experience : typing.Optional[MiFidAssessmentRequestInvestmentExperience]

        financial_situation : typing.Optional[MiFidAssessmentRequestFinancialSituation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MiFidAssessmentResponse
            MiFID II Assessment erfolgreich

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.compliance.perform_mi_fid_assessment(
            customer_id="customerId",
            investment_objectives=["investmentObjectives"],
        )
        """
        _response = self._raw_client.perform_mi_fid_assessment(
            customer_id=customer_id,
            investment_objectives=investment_objectives,
            existing_assessments=existing_assessments,
            investment_experience=investment_experience,
            financial_situation=financial_situation,
            request_options=request_options,
        )
        return _response.data


class AsyncComplianceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawComplianceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawComplianceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawComplianceClient
        """
        return self._raw_client

    async def perform_mi_fid_assessment(
        self,
        *,
        customer_id: str,
        investment_objectives: typing.Sequence[str],
        existing_assessments: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        investment_experience: typing.Optional[MiFidAssessmentRequestInvestmentExperience] = OMIT,
        financial_situation: typing.Optional[MiFidAssessmentRequestFinancialSituation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MiFidAssessmentResponse:
        """
        Führt MiFID II konforme Anlageeignungsprüfung durch

        Parameters
        ----------
        customer_id : str

        investment_objectives : typing.Sequence[str]

        existing_assessments : typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]]

        investment_experience : typing.Optional[MiFidAssessmentRequestInvestmentExperience]

        financial_situation : typing.Optional[MiFidAssessmentRequestFinancialSituation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MiFidAssessmentResponse
            MiFID II Assessment erfolgreich

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.compliance.perform_mi_fid_assessment(
                customer_id="customerId",
                investment_objectives=["investmentObjectives"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.perform_mi_fid_assessment(
            customer_id=customer_id,
            investment_objectives=investment_objectives,
            existing_assessments=existing_assessments,
            investment_experience=investment_experience,
            financial_situation=financial_situation,
            request_options=request_options,
        )
        return _response.data
