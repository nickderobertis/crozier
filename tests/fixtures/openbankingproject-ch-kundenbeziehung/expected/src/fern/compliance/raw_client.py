

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..types.mi_fid_assessment_response import MiFidAssessmentResponse
from .types.mi_fid_assessment_request_financial_situation import MiFidAssessmentRequestFinancialSituation
from .types.mi_fid_assessment_request_investment_experience import MiFidAssessmentRequestInvestmentExperience
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawComplianceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def perform_mi_fid_assessment(
        self,
        *,
        customer_id: str,
        investment_objectives: typing.Sequence[str],
        existing_assessments: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        investment_experience: typing.Optional[MiFidAssessmentRequestInvestmentExperience] = OMIT,
        financial_situation: typing.Optional[MiFidAssessmentRequestFinancialSituation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[MiFidAssessmentResponse]:
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
        HttpResponse[MiFidAssessmentResponse]
            MiFID II Assessment erfolgreich
        """
        _response = self._client_wrapper.httpx_client.request(
            "mifid/assessment",
            method="POST",
            json={
                "customerId": customer_id,
                "existingAssessments": existing_assessments,
                "investmentObjectives": investment_objectives,
                "investmentExperience": investment_experience,
                "financialSituation": convert_and_respect_annotation_metadata(
                    object_=financial_situation, annotation=MiFidAssessmentRequestFinancialSituation, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MiFidAssessmentResponse,
                    parse_obj_as(
                        type_=MiFidAssessmentResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawComplianceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def perform_mi_fid_assessment(
        self,
        *,
        customer_id: str,
        investment_objectives: typing.Sequence[str],
        existing_assessments: typing.Optional[typing.Sequence[typing.Dict[str, typing.Any]]] = OMIT,
        investment_experience: typing.Optional[MiFidAssessmentRequestInvestmentExperience] = OMIT,
        financial_situation: typing.Optional[MiFidAssessmentRequestFinancialSituation] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[MiFidAssessmentResponse]:
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
        AsyncHttpResponse[MiFidAssessmentResponse]
            MiFID II Assessment erfolgreich
        """
        _response = await self._client_wrapper.httpx_client.request(
            "mifid/assessment",
            method="POST",
            json={
                "customerId": customer_id,
                "existingAssessments": existing_assessments,
                "investmentObjectives": investment_objectives,
                "investmentExperience": investment_experience,
                "financialSituation": convert_and_respect_annotation_metadata(
                    object_=financial_situation, annotation=MiFidAssessmentRequestFinancialSituation, direction="write"
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    MiFidAssessmentResponse,
                    parse_obj_as(
                        type_=MiFidAssessmentResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
