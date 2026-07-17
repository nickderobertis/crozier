

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_assets_returns_simulation_bootstrap_request_assets_item import (
    PostAssetsReturnsSimulationBootstrapRequestAssetsItem,
)
from .types.post_assets_returns_simulation_bootstrap_request_bootstrap_method import (
    PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod,
)
from .types.post_assets_returns_simulation_bootstrap_response import PostAssetsReturnsSimulationBootstrapResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAssetsReturnsSimulationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def bootstrap(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem],
        bootstrap_average_block_length: typing.Optional[float] = OMIT,
        bootstrap_block_length: typing.Optional[int] = OMIT,
        bootstrap_method: typing.Optional[PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod] = OMIT,
        simulations: typing.Optional[int] = OMIT,
        simulations_length: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsReturnsSimulationBootstrapResponse]:
        """
        Simulate the return(s) of one or several asset(s) for one or several time period(s) using a bootstrap method.

        References
        * [Efron, B. (1979), Bootstrap methods: Another look at the jackknife, The Annals of Statistics 7, 1-26](https://projecteuclid.org/journals/annals-of-statistics/volume-7/issue-1/Bootstrap-Methods-Another-Look-at-the-Jackknife/10.1214/aos/1176344552.full)
        * [Politis, D. N. and Romano, J. P., A circular block resampling procedure for stationary data, in R. Lepage and L. Billard, eds, Exploring the Limits of Bootstrap, Wiley, New York, pp. 263-270](https://statistics.stanford.edu/technical-reports/circular-block-resampling-procedure-stationary-data)
        * [Politis, D. N. and Romano, J. P., The stationary bootstrap, Journal of the American Statistical Association 89, 1303-1313](https://www.jstor.org/stable/2290993)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem]

        bootstrap_average_block_length : typing.Optional[float]
            The average length of the blocks to use in case the bootstrap method is 'stationaryBlock', in time periods; if not provided, defaults to the inverse of 3.15 * the common length of the assetReturns arrays^1/3

        bootstrap_block_length : typing.Optional[int]
            The length of the blocks to use in case the bootstrap method is 'circularBlock', in time periods; if not provided, defaults to [3.15 * the common length of the assetReturns arrays^1/3]

        bootstrap_method : typing.Optional[PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod]
            The bootstrap method to use

        simulations : typing.Optional[int]
            The number of simulations to perform

        simulations_length : typing.Optional[int]
            The number of time period(s) to simulate per simulation; if not provided, defaults to the common length of the assetReturns arrays

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsReturnsSimulationBootstrapResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/returns/simulation/bootstrap",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem],
                    direction="write",
                ),
                "bootstrapAverageBlockLength": bootstrap_average_block_length,
                "bootstrapBlockLength": bootstrap_block_length,
                "bootstrapMethod": bootstrap_method,
                "simulations": simulations,
                "simulationsLength": simulations_length,
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
                    PostAssetsReturnsSimulationBootstrapResponse,
                    parse_obj_as(
                        type_=PostAssetsReturnsSimulationBootstrapResponse,
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


class AsyncRawAssetsReturnsSimulationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def bootstrap(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem],
        bootstrap_average_block_length: typing.Optional[float] = OMIT,
        bootstrap_block_length: typing.Optional[int] = OMIT,
        bootstrap_method: typing.Optional[PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod] = OMIT,
        simulations: typing.Optional[int] = OMIT,
        simulations_length: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsReturnsSimulationBootstrapResponse]:
        """
        Simulate the return(s) of one or several asset(s) for one or several time period(s) using a bootstrap method.

        References
        * [Efron, B. (1979), Bootstrap methods: Another look at the jackknife, The Annals of Statistics 7, 1-26](https://projecteuclid.org/journals/annals-of-statistics/volume-7/issue-1/Bootstrap-Methods-Another-Look-at-the-Jackknife/10.1214/aos/1176344552.full)
        * [Politis, D. N. and Romano, J. P., A circular block resampling procedure for stationary data, in R. Lepage and L. Billard, eds, Exploring the Limits of Bootstrap, Wiley, New York, pp. 263-270](https://statistics.stanford.edu/technical-reports/circular-block-resampling-procedure-stationary-data)
        * [Politis, D. N. and Romano, J. P., The stationary bootstrap, Journal of the American Statistical Association 89, 1303-1313](https://www.jstor.org/stable/2290993)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem]

        bootstrap_average_block_length : typing.Optional[float]
            The average length of the blocks to use in case the bootstrap method is 'stationaryBlock', in time periods; if not provided, defaults to the inverse of 3.15 * the common length of the assetReturns arrays^1/3

        bootstrap_block_length : typing.Optional[int]
            The length of the blocks to use in case the bootstrap method is 'circularBlock', in time periods; if not provided, defaults to [3.15 * the common length of the assetReturns arrays^1/3]

        bootstrap_method : typing.Optional[PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod]
            The bootstrap method to use

        simulations : typing.Optional[int]
            The number of simulations to perform

        simulations_length : typing.Optional[int]
            The number of time period(s) to simulate per simulation; if not provided, defaults to the common length of the assetReturns arrays

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsReturnsSimulationBootstrapResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/returns/simulation/bootstrap",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem],
                    direction="write",
                ),
                "bootstrapAverageBlockLength": bootstrap_average_block_length,
                "bootstrapBlockLength": bootstrap_block_length,
                "bootstrapMethod": bootstrap_method,
                "simulations": simulations,
                "simulationsLength": simulations_length,
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
                    PostAssetsReturnsSimulationBootstrapResponse,
                    parse_obj_as(
                        type_=PostAssetsReturnsSimulationBootstrapResponse,
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
