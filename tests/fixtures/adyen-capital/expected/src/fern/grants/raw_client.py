

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.default_error_response_entity import DefaultErrorResponseEntity
from ..types.disbursement import Disbursement
from ..types.disbursement_repayment_info_update import DisbursementRepaymentInfoUpdate
from ..types.disbursements import Disbursements
from ..types.grant import Grant
from ..types.grant_info_counterparty import GrantInfoCounterparty
from ..types.grants import Grants
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawGrantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_grants(
        self, *, counterparty_account_holder_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Grants]:
        """
        Returns a list of all the grants of a specific account holder.

        Parameters
        ----------
        counterparty_account_holder_id : str
            The unique identifier of the account holder that received the grants.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Grants]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "grants",
            method="GET",
            params={
                "counterpartyAccountHolderId": counterparty_account_holder_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Grants,
                    parse_obj_as(
                        type_=Grants,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    def post_grants(
        self,
        *,
        grant_account_id: str,
        grant_offer_id: str,
        counterparty: typing.Optional[GrantInfoCounterparty] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Grant]:
        """
        Make a request for a grant on behalf of an account holder.

        Parameters
        ----------
        grant_account_id : str
            The unique identifier of the grant account that tracks this grant.

        grant_offer_id : str
            The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.

        counterparty : typing.Optional[GrantInfoCounterparty]
            Contains the details of the party that receives the grant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Grant]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "grants",
            method="POST",
            json={
                "counterparty": convert_and_respect_annotation_metadata(
                    object_=counterparty, annotation=GrantInfoCounterparty, direction="write"
                ),
                "grantAccountId": grant_account_id,
                "grantOfferId": grant_offer_id,
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
                    Grant,
                    parse_obj_as(
                        type_=Grant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    def get_grants_grant_id(
        self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Grant]:
        """
        Returns the details of the specified grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Grant]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"grants/{encode_path_param(grant_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Grant,
                    parse_obj_as(
                        type_=Grant,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    def get_grants_grant_id_disbursements(
        self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Disbursements]:
        """
        Returns the disbursements of a specified grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Disbursements]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"grants/{encode_path_param(grant_id)}/disbursements",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Disbursements,
                    parse_obj_as(
                        type_=Disbursements,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    def get_grants_grant_id_disbursements_disbursement_id(
        self, grant_id: str, disbursement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Disbursement]:
        """
        Returns the details of a disbursement specified in the path.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        disbursement_id : str
            The unique identifier of the disbursement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Disbursement]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"grants/{encode_path_param(grant_id)}/disbursements/{encode_path_param(disbursement_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Disbursement,
                    parse_obj_as(
                        type_=Disbursement,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    def patch_grants_grant_id_disbursements_disbursement_id(
        self,
        grant_id: str,
        disbursement_id: str,
        *,
        repayment: typing.Optional[DisbursementRepaymentInfoUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Disbursement]:
        """
        Update the percentage of your user's net income that is deducted for repaying the grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        disbursement_id : str
            The unique identifier of the disbursement.

        repayment : typing.Optional[DisbursementRepaymentInfoUpdate]
            Contains information about the basis points configured for repaying the disbursement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Disbursement]
            OK - The request has succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"grants/{encode_path_param(grant_id)}/disbursements/{encode_path_param(disbursement_id)}",
            method="PATCH",
            json={
                "repayment": convert_and_respect_annotation_metadata(
                    object_=repayment, annotation=DisbursementRepaymentInfoUpdate, direction="write"
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
                    Disbursement,
                    parse_obj_as(
                        type_=Disbursement,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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


class AsyncRawGrantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_grants(
        self, *, counterparty_account_holder_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Grants]:
        """
        Returns a list of all the grants of a specific account holder.

        Parameters
        ----------
        counterparty_account_holder_id : str
            The unique identifier of the account holder that received the grants.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Grants]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "grants",
            method="GET",
            params={
                "counterpartyAccountHolderId": counterparty_account_holder_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Grants,
                    parse_obj_as(
                        type_=Grants,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    async def post_grants(
        self,
        *,
        grant_account_id: str,
        grant_offer_id: str,
        counterparty: typing.Optional[GrantInfoCounterparty] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Grant]:
        """
        Make a request for a grant on behalf of an account holder.

        Parameters
        ----------
        grant_account_id : str
            The unique identifier of the grant account that tracks this grant.

        grant_offer_id : str
            The unique identifier of the selected offer. Adyen uses the details of the selected offer to create a grant.

        counterparty : typing.Optional[GrantInfoCounterparty]
            Contains the details of the party that receives the grant.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Grant]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "grants",
            method="POST",
            json={
                "counterparty": convert_and_respect_annotation_metadata(
                    object_=counterparty, annotation=GrantInfoCounterparty, direction="write"
                ),
                "grantAccountId": grant_account_id,
                "grantOfferId": grant_offer_id,
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
                    Grant,
                    parse_obj_as(
                        type_=Grant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    async def get_grants_grant_id(
        self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Grant]:
        """
        Returns the details of the specified grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Grant]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"grants/{encode_path_param(grant_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Grant,
                    parse_obj_as(
                        type_=Grant,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    async def get_grants_grant_id_disbursements(
        self, grant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Disbursements]:
        """
        Returns the disbursements of a specified grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Disbursements]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"grants/{encode_path_param(grant_id)}/disbursements",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Disbursements,
                    parse_obj_as(
                        type_=Disbursements,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    async def get_grants_grant_id_disbursements_disbursement_id(
        self, grant_id: str, disbursement_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Disbursement]:
        """
        Returns the details of a disbursement specified in the path.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        disbursement_id : str
            The unique identifier of the disbursement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Disbursement]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"grants/{encode_path_param(grant_id)}/disbursements/{encode_path_param(disbursement_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Disbursement,
                    parse_obj_as(
                        type_=Disbursement,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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

    async def patch_grants_grant_id_disbursements_disbursement_id(
        self,
        grant_id: str,
        disbursement_id: str,
        *,
        repayment: typing.Optional[DisbursementRepaymentInfoUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Disbursement]:
        """
        Update the percentage of your user's net income that is deducted for repaying the grant.

        Parameters
        ----------
        grant_id : str
            The unique identifier of the grant reference.

        disbursement_id : str
            The unique identifier of the disbursement.

        repayment : typing.Optional[DisbursementRepaymentInfoUpdate]
            Contains information about the basis points configured for repaying the disbursement.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Disbursement]
            OK - The request has succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"grants/{encode_path_param(grant_id)}/disbursements/{encode_path_param(disbursement_id)}",
            method="PATCH",
            json={
                "repayment": convert_and_respect_annotation_metadata(
                    object_=repayment, annotation=DisbursementRepaymentInfoUpdate, direction="write"
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
                    Disbursement,
                    parse_obj_as(
                        type_=Disbursement,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        DefaultErrorResponseEntity,
                        parse_obj_as(
                            type_=DefaultErrorResponseEntity,
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
