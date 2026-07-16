

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
from ..errors.bad_request_error import BadRequestError
from ..types.address import Address
from ..types.amount import Amount
from ..types.avatar import Avatar
from ..types.billing_contract_subscription import BillingContractSubscription
from ..types.customer import Customer
from ..types.customer_limit import CustomerLimit
from ..types.label_user import LabelUser
from ..types.notification_filter import NotificationFilter
from ..types.pointer import Pointer
from ..types.relation_user import RelationUser
from ..types.tax_resident import TaxResident
from ..types.ubo import Ubo
from ..types.user_company_read import UserCompanyRead
from ..types.user_company_update import UserCompanyUpdate
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawUserCompanyClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def read_user_company(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserCompanyRead]:
        """
        Get a specific company.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserCompanyRead]
            With UserCompany you can retrieve information regarding the authenticated UserCompany and update specific fields.<br/><br/>Notification filters can be set on a UserCompany level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user-company/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserCompanyRead,
                    parse_obj_as(
                        type_=UserCompanyRead,
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

    def update_user_company(
        self,
        item_id: int,
        *,
        address_main: typing.Optional[Address] = OMIT,
        address_postal: typing.Optional[Address] = OMIT,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar: typing.Optional[Avatar] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        billing_contract: typing.Optional[typing.Sequence[BillingContractSubscription]] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        counter_bank_iban: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        created: typing.Optional[str] = OMIT,
        customer: typing.Optional[Customer] = OMIT,
        customer_limit: typing.Optional[CustomerLimit] = OMIT,
        daily_limit_without_confirmation_login: typing.Optional[Amount] = OMIT,
        deny_reason: typing.Optional[str] = OMIT,
        directors: typing.Optional[typing.Sequence[LabelUser]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        language: typing.Optional[str] = OMIT,
        legal_form: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilter]] = OMIT,
        public_nick_name: typing.Optional[str] = OMIT,
        public_uuid: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        relations: typing.Optional[typing.Sequence[RelationUser]] = OMIT,
        sector_of_industry: typing.Optional[str] = OMIT,
        session_timeout: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        tax_resident: typing.Optional[typing.Sequence[TaxResident]] = OMIT,
        type_of_business_entity: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        updated: typing.Optional[str] = OMIT,
        version_terms_of_service: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserCompanyUpdate]:
        """
        Modify a specific company's data.

        Parameters
        ----------
        item_id : int


        address_main : typing.Optional[Address]
            The company's main address.

        address_postal : typing.Optional[Address]
            The company's postal address.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The aliases of the account.

        avatar : typing.Optional[Avatar]
            The company's avatar.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        billing_contract : typing.Optional[typing.Sequence[BillingContractSubscription]]
            The subscription of the company.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        counter_bank_iban : typing.Optional[str]
            The company's other bank account IBAN, through which we verify it.

        country : typing.Optional[str]
            The country as an ISO 3166-1 alpha-2 country code.

        created : typing.Optional[str]
            The timestamp of the company object's creation.

        customer : typing.Optional[Customer]
            The customer profile of the company.

        customer_limit : typing.Optional[CustomerLimit]
            The customer limits of the company.

        daily_limit_without_confirmation_login : typing.Optional[Amount]
            The amount the company can pay in the session without asking for credentials.

        deny_reason : typing.Optional[str]
            The user deny reason.

        directors : typing.Optional[typing.Sequence[LabelUser]]
            The existing bunq aliases for the company's directors.

        display_name : typing.Optional[str]
            The company's display name.

        id : typing.Optional[int]
            The id of the modified company.

        language : typing.Optional[str]
            The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        legal_form : typing.Optional[str]
            The company's legal form.

        name : typing.Optional[str]
            The company name.

        notification_filters : typing.Optional[typing.Sequence[NotificationFilter]]
            The types of notifications that will result in a push notification or URL callback for this UserCompany.

        public_nick_name : typing.Optional[str]
            The company's public nick name.

        public_uuid : typing.Optional[str]
            The company's public UUID.

        region : typing.Optional[str]
            The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        relations : typing.Optional[typing.Sequence[RelationUser]]
            The relations for this user.

        sector_of_industry : typing.Optional[str]
            The sector of industry.

        session_timeout : typing.Optional[int]
            The setting for the session timeout of the company in seconds.

        status : typing.Optional[str]
            The user status. Can be: ACTIVE, SIGNUP, RECOVERY.

        sub_status : typing.Optional[str]
            The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.

        tax_resident : typing.Optional[typing.Sequence[TaxResident]]
            The user's tax residence numbers for different countries.

        type_of_business_entity : typing.Optional[str]
            The type of business entity.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        updated : typing.Optional[str]
            The timestamp of the company object's last update.

        version_terms_of_service : typing.Optional[str]
            The version of the terms of service accepted by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserCompanyUpdate]
            With UserCompany you can retrieve information regarding the authenticated UserCompany and update specific fields.<br/><br/>Notification filters can be set on a UserCompany level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"user-company/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "address_main": convert_and_respect_annotation_metadata(
                    object_=address_main, annotation=Address, direction="write"
                ),
                "address_postal": convert_and_respect_annotation_metadata(
                    object_=address_postal, annotation=Address, direction="write"
                ),
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=typing.Sequence[Pointer], direction="write"
                ),
                "avatar": convert_and_respect_annotation_metadata(object_=avatar, annotation=Avatar, direction="write"),
                "avatar_uuid": avatar_uuid,
                "billing_contract": convert_and_respect_annotation_metadata(
                    object_=billing_contract, annotation=typing.Sequence[BillingContractSubscription], direction="write"
                ),
                "chamber_of_commerce_number": chamber_of_commerce_number,
                "counter_bank_iban": counter_bank_iban,
                "country": country,
                "created": created,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=Customer, direction="write"
                ),
                "customer_limit": convert_and_respect_annotation_metadata(
                    object_=customer_limit, annotation=CustomerLimit, direction="write"
                ),
                "daily_limit_without_confirmation_login": convert_and_respect_annotation_metadata(
                    object_=daily_limit_without_confirmation_login, annotation=Amount, direction="write"
                ),
                "deny_reason": deny_reason,
                "directors": convert_and_respect_annotation_metadata(
                    object_=directors, annotation=typing.Sequence[LabelUser], direction="write"
                ),
                "display_name": display_name,
                "id": id,
                "language": language,
                "legal_form": legal_form,
                "name": name,
                "notification_filters": convert_and_respect_annotation_metadata(
                    object_=notification_filters, annotation=typing.Sequence[NotificationFilter], direction="write"
                ),
                "public_nick_name": public_nick_name,
                "public_uuid": public_uuid,
                "region": region,
                "relations": convert_and_respect_annotation_metadata(
                    object_=relations, annotation=typing.Sequence[RelationUser], direction="write"
                ),
                "sector_of_industry": sector_of_industry,
                "session_timeout": session_timeout,
                "status": status,
                "sub_status": sub_status,
                "tax_resident": convert_and_respect_annotation_metadata(
                    object_=tax_resident, annotation=typing.Sequence[TaxResident], direction="write"
                ),
                "type_of_business_entity": type_of_business_entity,
                "ubo": convert_and_respect_annotation_metadata(
                    object_=ubo, annotation=typing.Sequence[Ubo], direction="write"
                ),
                "updated": updated,
                "version_terms_of_service": version_terms_of_service,
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
                    UserCompanyUpdate,
                    parse_obj_as(
                        type_=UserCompanyUpdate,
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


class AsyncRawUserCompanyClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def read_user_company(
        self, item_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserCompanyRead]:
        """
        Get a specific company.

        Parameters
        ----------
        item_id : int


        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserCompanyRead]
            With UserCompany you can retrieve information regarding the authenticated UserCompany and update specific fields.<br/><br/>Notification filters can be set on a UserCompany level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user-company/{encode_path_param(item_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserCompanyRead,
                    parse_obj_as(
                        type_=UserCompanyRead,
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

    async def update_user_company(
        self,
        item_id: int,
        *,
        address_main: typing.Optional[Address] = OMIT,
        address_postal: typing.Optional[Address] = OMIT,
        alias: typing.Optional[typing.Sequence[Pointer]] = OMIT,
        avatar: typing.Optional[Avatar] = OMIT,
        avatar_uuid: typing.Optional[str] = OMIT,
        billing_contract: typing.Optional[typing.Sequence[BillingContractSubscription]] = OMIT,
        chamber_of_commerce_number: typing.Optional[str] = OMIT,
        counter_bank_iban: typing.Optional[str] = OMIT,
        country: typing.Optional[str] = OMIT,
        created: typing.Optional[str] = OMIT,
        customer: typing.Optional[Customer] = OMIT,
        customer_limit: typing.Optional[CustomerLimit] = OMIT,
        daily_limit_without_confirmation_login: typing.Optional[Amount] = OMIT,
        deny_reason: typing.Optional[str] = OMIT,
        directors: typing.Optional[typing.Sequence[LabelUser]] = OMIT,
        display_name: typing.Optional[str] = OMIT,
        id: typing.Optional[int] = OMIT,
        language: typing.Optional[str] = OMIT,
        legal_form: typing.Optional[str] = OMIT,
        name: typing.Optional[str] = OMIT,
        notification_filters: typing.Optional[typing.Sequence[NotificationFilter]] = OMIT,
        public_nick_name: typing.Optional[str] = OMIT,
        public_uuid: typing.Optional[str] = OMIT,
        region: typing.Optional[str] = OMIT,
        relations: typing.Optional[typing.Sequence[RelationUser]] = OMIT,
        sector_of_industry: typing.Optional[str] = OMIT,
        session_timeout: typing.Optional[int] = OMIT,
        status: typing.Optional[str] = OMIT,
        sub_status: typing.Optional[str] = OMIT,
        tax_resident: typing.Optional[typing.Sequence[TaxResident]] = OMIT,
        type_of_business_entity: typing.Optional[str] = OMIT,
        ubo: typing.Optional[typing.Sequence[Ubo]] = OMIT,
        updated: typing.Optional[str] = OMIT,
        version_terms_of_service: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserCompanyUpdate]:
        """
        Modify a specific company's data.

        Parameters
        ----------
        item_id : int


        address_main : typing.Optional[Address]
            The company's main address.

        address_postal : typing.Optional[Address]
            The company's postal address.

        alias : typing.Optional[typing.Sequence[Pointer]]
            The aliases of the account.

        avatar : typing.Optional[Avatar]
            The company's avatar.

        avatar_uuid : typing.Optional[str]
            The public UUID of the company's avatar.

        billing_contract : typing.Optional[typing.Sequence[BillingContractSubscription]]
            The subscription of the company.

        chamber_of_commerce_number : typing.Optional[str]
            The company's chamber of commerce number.

        counter_bank_iban : typing.Optional[str]
            The company's other bank account IBAN, through which we verify it.

        country : typing.Optional[str]
            The country as an ISO 3166-1 alpha-2 country code.

        created : typing.Optional[str]
            The timestamp of the company object's creation.

        customer : typing.Optional[Customer]
            The customer profile of the company.

        customer_limit : typing.Optional[CustomerLimit]
            The customer limits of the company.

        daily_limit_without_confirmation_login : typing.Optional[Amount]
            The amount the company can pay in the session without asking for credentials.

        deny_reason : typing.Optional[str]
            The user deny reason.

        directors : typing.Optional[typing.Sequence[LabelUser]]
            The existing bunq aliases for the company's directors.

        display_name : typing.Optional[str]
            The company's display name.

        id : typing.Optional[int]
            The id of the modified company.

        language : typing.Optional[str]
            The person's preferred language. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        legal_form : typing.Optional[str]
            The company's legal form.

        name : typing.Optional[str]
            The company name.

        notification_filters : typing.Optional[typing.Sequence[NotificationFilter]]
            The types of notifications that will result in a push notification or URL callback for this UserCompany.

        public_nick_name : typing.Optional[str]
            The company's public nick name.

        public_uuid : typing.Optional[str]
            The company's public UUID.

        region : typing.Optional[str]
            The person's preferred region. Formatted as a ISO 639-1 language code plus a ISO 3166-1 alpha-2 country code, seperated by an underscore.

        relations : typing.Optional[typing.Sequence[RelationUser]]
            The relations for this user.

        sector_of_industry : typing.Optional[str]
            The sector of industry.

        session_timeout : typing.Optional[int]
            The setting for the session timeout of the company in seconds.

        status : typing.Optional[str]
            The user status. Can be: ACTIVE, SIGNUP, RECOVERY.

        sub_status : typing.Optional[str]
            The user sub-status. Can be: NONE, FACE_RESET, APPROVAL, APPROVAL_DIRECTOR, APPROVAL_PARENT, APPROVAL_SUPPORT, COUNTER_IBAN, IDEAL or SUBMIT.

        tax_resident : typing.Optional[typing.Sequence[TaxResident]]
            The user's tax residence numbers for different countries.

        type_of_business_entity : typing.Optional[str]
            The type of business entity.

        ubo : typing.Optional[typing.Sequence[Ubo]]
            The names of the company's ultimate beneficiary owners. Minimum zero, maximum four.

        updated : typing.Optional[str]
            The timestamp of the company object's last update.

        version_terms_of_service : typing.Optional[str]
            The version of the terms of service accepted by the user.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserCompanyUpdate]
            With UserCompany you can retrieve information regarding the authenticated UserCompany and update specific fields.<br/><br/>Notification filters can be set on a UserCompany level to receive callbacks. For more information check the <a href="/api/1/page/callbacks">dedicated callbacks page</a>.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"user-company/{encode_path_param(item_id)}",
            method="PUT",
            json={
                "address_main": convert_and_respect_annotation_metadata(
                    object_=address_main, annotation=Address, direction="write"
                ),
                "address_postal": convert_and_respect_annotation_metadata(
                    object_=address_postal, annotation=Address, direction="write"
                ),
                "alias": convert_and_respect_annotation_metadata(
                    object_=alias, annotation=typing.Sequence[Pointer], direction="write"
                ),
                "avatar": convert_and_respect_annotation_metadata(object_=avatar, annotation=Avatar, direction="write"),
                "avatar_uuid": avatar_uuid,
                "billing_contract": convert_and_respect_annotation_metadata(
                    object_=billing_contract, annotation=typing.Sequence[BillingContractSubscription], direction="write"
                ),
                "chamber_of_commerce_number": chamber_of_commerce_number,
                "counter_bank_iban": counter_bank_iban,
                "country": country,
                "created": created,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=Customer, direction="write"
                ),
                "customer_limit": convert_and_respect_annotation_metadata(
                    object_=customer_limit, annotation=CustomerLimit, direction="write"
                ),
                "daily_limit_without_confirmation_login": convert_and_respect_annotation_metadata(
                    object_=daily_limit_without_confirmation_login, annotation=Amount, direction="write"
                ),
                "deny_reason": deny_reason,
                "directors": convert_and_respect_annotation_metadata(
                    object_=directors, annotation=typing.Sequence[LabelUser], direction="write"
                ),
                "display_name": display_name,
                "id": id,
                "language": language,
                "legal_form": legal_form,
                "name": name,
                "notification_filters": convert_and_respect_annotation_metadata(
                    object_=notification_filters, annotation=typing.Sequence[NotificationFilter], direction="write"
                ),
                "public_nick_name": public_nick_name,
                "public_uuid": public_uuid,
                "region": region,
                "relations": convert_and_respect_annotation_metadata(
                    object_=relations, annotation=typing.Sequence[RelationUser], direction="write"
                ),
                "sector_of_industry": sector_of_industry,
                "session_timeout": session_timeout,
                "status": status,
                "sub_status": sub_status,
                "tax_resident": convert_and_respect_annotation_metadata(
                    object_=tax_resident, annotation=typing.Sequence[TaxResident], direction="write"
                ),
                "type_of_business_entity": type_of_business_entity,
                "ubo": convert_and_respect_annotation_metadata(
                    object_=ubo, annotation=typing.Sequence[Ubo], direction="write"
                ),
                "updated": updated,
                "version_terms_of_service": version_terms_of_service,
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
                    UserCompanyUpdate,
                    parse_obj_as(
                        type_=UserCompanyUpdate,
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
