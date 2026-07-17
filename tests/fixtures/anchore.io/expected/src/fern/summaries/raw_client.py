

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.internal_server_error import InternalServerError
from ..types.anchore_image_tag_summary_list import AnchoreImageTagSummaryList
from .types.list_imagetags_request_image_status_item import ListImagetagsRequestImageStatusItem
from pydantic import ValidationError


class RawSummariesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_imagetags(
        self,
        *,
        image_status: typing.Optional[
            typing.Union[ListImagetagsRequestImageStatusItem, typing.Sequence[ListImagetagsRequestImageStatusItem]]
        ] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AnchoreImageTagSummaryList]:
        """
        List all image tags visible to the user

        Parameters
        ----------
        image_status : typing.Optional[typing.Union[ListImagetagsRequestImageStatusItem, typing.Sequence[ListImagetagsRequestImageStatusItem]]]
            Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AnchoreImageTagSummaryList]
            successful operation
        """
        _response = self._client_wrapper.httpx_client.request(
            "summaries/imagetags",
            method="GET",
            params={
                "image_status": ",".join(map(str, image_status))
                if isinstance(image_status, (list, tuple, set))
                else image_status,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageTagSummaryList,
                    parse_obj_as(
                        type_=AnchoreImageTagSummaryList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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


class AsyncRawSummariesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_imagetags(
        self,
        *,
        image_status: typing.Optional[
            typing.Union[ListImagetagsRequestImageStatusItem, typing.Sequence[ListImagetagsRequestImageStatusItem]]
        ] = None,
        anchore_account: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AnchoreImageTagSummaryList]:
        """
        List all image tags visible to the user

        Parameters
        ----------
        image_status : typing.Optional[typing.Union[ListImagetagsRequestImageStatusItem, typing.Sequence[ListImagetagsRequestImageStatusItem]]]
            Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified

        anchore_account : typing.Optional[str]
            An account name to change the resource scope of the request to that account, if permissions allow (admin only)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AnchoreImageTagSummaryList]
            successful operation
        """
        _response = await self._client_wrapper.httpx_client.request(
            "summaries/imagetags",
            method="GET",
            params={
                "image_status": ",".join(map(str, image_status))
                if isinstance(image_status, (list, tuple, set))
                else image_status,
            },
            headers={
                "x-anchore-account": str(anchore_account) if anchore_account is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AnchoreImageTagSummaryList,
                    parse_obj_as(
                        type_=AnchoreImageTagSummaryList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 500:
                raise InternalServerError(
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
