

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from .types.other_slurp_request_parts_item import OtherSlurpRequestPartsItem
from .types.other_slurp_request_source import OtherSlurpRequestSource
from .types.other_slurp_response import OtherSlurpResponse
from pydantic import ValidationError


class RawOtherClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def slurp(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        parts: typing.Optional[
            typing.Union[OtherSlurpRequestPartsItem, typing.Sequence[OtherSlurpRequestPartsItem]]
        ] = None,
        appearances: typing.Optional[bool] = None,
        articulate: typing.Optional[bool] = None,
        source: typing.Optional[OtherSlurpRequestSource] = None,
        count: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        page_id: typing.Optional[str] = None,
        per_page: typing.Optional[int] = None,
        sleep: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[OtherSlurpResponse]:
        """
        Fetch data from Etherscan and other APIs for any address. Corresponds to the <a href="/chifra/other/#chifra-slurp">chifra slurp</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses to slurp from Etherscan

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional range of blocks to slurp

        parts : typing.Optional[typing.Union[OtherSlurpRequestPartsItem, typing.Sequence[OtherSlurpRequestPartsItem]]]
            which types of transactions to request

        appearances : typing.Optional[bool]
            show only the blocknumber.tx_id appearances of the exported transactions

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        source : typing.Optional[OtherSlurpRequestSource]
            the source of the slurped data

        count : typing.Optional[bool]
            for --appearances mode only, display only the count of records

        page : typing.Optional[int]
            the page to retrieve (page number)

        page_id : typing.Optional[str]
            the page to retrieve (page ID)

        per_page : typing.Optional[int]
            the number of records to request on each page

        sleep : typing.Optional[float]
            seconds to sleep between requests

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        ether : typing.Optional[bool]
            export values in ether

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OtherSlurpResponse]
            returns the requested data
        """
        _response = self._client_wrapper.httpx_client.request(
            "slurp",
            method="GET",
            params={
                "addrs": addrs,
                "blocks": blocks,
                "parts": parts,
                "appearances": appearances,
                "articulate": articulate,
                "source": source,
                "count": count,
                "page": page,
                "pageId": page_id,
                "perPage": per_page,
                "sleep": sleep,
                "chain": chain,
                "noHeader": no_header,
                "cache": cache,
                "decache": decache,
                "ether": ether,
                "fmt": fmt,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtherSlurpResponse,
                    parse_obj_as(
                        type_=OtherSlurpResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawOtherClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def slurp(
        self,
        *,
        addrs: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        blocks: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        parts: typing.Optional[
            typing.Union[OtherSlurpRequestPartsItem, typing.Sequence[OtherSlurpRequestPartsItem]]
        ] = None,
        appearances: typing.Optional[bool] = None,
        articulate: typing.Optional[bool] = None,
        source: typing.Optional[OtherSlurpRequestSource] = None,
        count: typing.Optional[bool] = None,
        page: typing.Optional[int] = None,
        page_id: typing.Optional[str] = None,
        per_page: typing.Optional[int] = None,
        sleep: typing.Optional[float] = None,
        chain: typing.Optional[str] = None,
        no_header: typing.Optional[bool] = None,
        cache: typing.Optional[bool] = None,
        decache: typing.Optional[bool] = None,
        ether: typing.Optional[bool] = None,
        fmt: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[OtherSlurpResponse]:
        """
        Fetch data from Etherscan and other APIs for any address. Corresponds to the <a href="/chifra/other/#chifra-slurp">chifra slurp</a> command line.

        Parameters
        ----------
        addrs : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            one or more addresses to slurp from Etherscan

        blocks : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            an optional range of blocks to slurp

        parts : typing.Optional[typing.Union[OtherSlurpRequestPartsItem, typing.Sequence[OtherSlurpRequestPartsItem]]]
            which types of transactions to request

        appearances : typing.Optional[bool]
            show only the blocknumber.tx_id appearances of the exported transactions

        articulate : typing.Optional[bool]
            articulate the retrieved data if ABIs can be found

        source : typing.Optional[OtherSlurpRequestSource]
            the source of the slurped data

        count : typing.Optional[bool]
            for --appearances mode only, display only the count of records

        page : typing.Optional[int]
            the page to retrieve (page number)

        page_id : typing.Optional[str]
            the page to retrieve (page ID)

        per_page : typing.Optional[int]
            the number of records to request on each page

        sleep : typing.Optional[float]
            seconds to sleep between requests

        chain : typing.Optional[str]
            the chain to use

        no_header : typing.Optional[bool]
            suppress the header in the output

        cache : typing.Optional[bool]
            force the results of the query into the cache

        decache : typing.Optional[bool]
            removes related items from the cache

        ether : typing.Optional[bool]
            export values in ether

        fmt : typing.Optional[str]
            export format, one of [ txt | csv | json ]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OtherSlurpResponse]
            returns the requested data
        """
        _response = await self._client_wrapper.httpx_client.request(
            "slurp",
            method="GET",
            params={
                "addrs": addrs,
                "blocks": blocks,
                "parts": parts,
                "appearances": appearances,
                "articulate": articulate,
                "source": source,
                "count": count,
                "page": page,
                "pageId": page_id,
                "perPage": per_page,
                "sleep": sleep,
                "chain": chain,
                "noHeader": no_header,
                "cache": cache,
                "decache": decache,
                "ether": ether,
                "fmt": fmt,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OtherSlurpResponse,
                    parse_obj_as(
                        type_=OtherSlurpResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
