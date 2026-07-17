

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_factors_residualization_request_factors_item import PostFactorsResidualizationRequestFactorsItem
from .types.post_factors_residualization_response import PostFactorsResidualizationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFactorsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def residualization(
        self,
        *,
        factors: typing.Sequence[PostFactorsResidualizationRequestFactorsItem],
        residualized_factor: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostFactorsResidualizationResponse]:
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
        HttpResponse[PostFactorsResidualizationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "factors/residualization",
            method="POST",
            json={
                "factors": convert_and_respect_annotation_metadata(
                    object_=factors,
                    annotation=typing.Sequence[PostFactorsResidualizationRequestFactorsItem],
                    direction="write",
                ),
                "residualizedFactor": residualized_factor,
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
                    PostFactorsResidualizationResponse,
                    parse_obj_as(
                        type_=PostFactorsResidualizationResponse,
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


class AsyncRawFactorsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def residualization(
        self,
        *,
        factors: typing.Sequence[PostFactorsResidualizationRequestFactorsItem],
        residualized_factor: int,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostFactorsResidualizationResponse]:
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
        AsyncHttpResponse[PostFactorsResidualizationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "factors/residualization",
            method="POST",
            json={
                "factors": convert_and_respect_annotation_metadata(
                    object_=factors,
                    annotation=typing.Sequence[PostFactorsResidualizationRequestFactorsItem],
                    direction="write",
                ),
                "residualizedFactor": residualized_factor,
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
                    PostFactorsResidualizationResponse,
                    parse_obj_as(
                        type_=PostFactorsResidualizationResponse,
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
