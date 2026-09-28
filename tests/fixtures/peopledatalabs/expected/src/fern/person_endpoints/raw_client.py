

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
from ..errors.method_not_allowed_error import MethodNotAllowedError
from ..errors.not_found_error import NotFoundError
from ..errors.payment_required_error import PaymentRequiredError
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.person import Person
from ..types.person_retrieve import PersonRetrieve
from ..types.person_retrieve_bulk import PersonRetrieveBulk
from .types.post_v5person_search_request import PostV5PersonSearchRequest
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPersonEndpointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def person_enrich(
        self,
        *,
        pdl_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        street_address: typing.Optional[str] = None,
        locality: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        school: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        email_hash: typing.Optional[str] = None,
        profile: typing.Optional[str] = None,
        lid: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        data_include: typing.Optional[str] = None,
        pretty: typing.Optional[bool] = None,
        min_likelihood: typing.Optional[int] = None,
        include_if_matched: typing.Optional[bool] = None,
        required: typing.Optional[str] = None,
        titlecase: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Person]:
        """
        Parameters
        ----------
        pdl_id : typing.Optional[str]
            The PDL ID of the person to enrich

        name : typing.Optional[str]
            The person's full name, at least first and last

        first_name : typing.Optional[str]
            The person's first name

        last_name : typing.Optional[str]
            The person's last name

        middle_name : typing.Optional[str]
            The person's middle name

        location : typing.Optional[str]
            A location in which a person lives

        street_address : typing.Optional[str]
            A street address in which the person lives

        locality : typing.Optional[str]
            A locality in which the person lives

        region : typing.Optional[str]
            A state or region in which the person lives

        country : typing.Optional[str]
            A country in which the person lives

        postal_code : typing.Optional[str]
            The postal code where the person lives. If there is no value for country, the postal code is assumed to be US

        company : typing.Optional[str]
            A name, website, or social url of a company where the person has worked

        school : typing.Optional[str]
            A name, website, or social url of a university or college the person has attended

        phone : typing.Optional[str]
            A phone number the person has used

        email : typing.Optional[str]
            An email the person has used

        email_hash : typing.Optional[str]
            A SHA-256 or MD5 email hash

        profile : typing.Optional[str]
            A social profile the person has used. https://docs.peopledatalabs.com/docs/social-networks

        lid : typing.Optional[str]
            The person's LinkedIn ID

        birth_date : typing.Optional[str]
            The person's birth date: either the year or a full birth date in the format YYYY-MM-DD

        data_include : typing.Optional[str]
            A comma-separated string of fields that you would like the response to include. Begin the string with a - if you would instead like to exclude the specified fields. If you would like to exclude all data from being returned, use data_include=""

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        min_likelihood : typing.Optional[int]
            The minimum likelihood score that a response must have in order to count as a match

        include_if_matched : typing.Optional[bool]
            If set to true, includes a top-level (alongside "data", "status", etc) field "matched" which includes a value for each queried field parameter that was "matched-on" during our internal query.

        required : typing.Optional[str]
            The fields a response must have in order to count as a match

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase the person data in 200 responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Person]
            Person Found
        """
        _response = self._client_wrapper.httpx_client.request(
            "v5/person/enrich",
            method="GET",
            params={
                "pdl_id": pdl_id,
                "name": name,
                "first_name": first_name,
                "last_name": last_name,
                "middle_name": middle_name,
                "location": location,
                "street_address": street_address,
                "locality": locality,
                "region": region,
                "country": country,
                "postal_code": postal_code,
                "company": company,
                "school": school,
                "phone": phone,
                "email": email,
                "email_hash": email_hash,
                "profile": profile,
                "lid": lid,
                "birth_date": birth_date,
                "data_include": data_include,
                "pretty": pretty,
                "min_likelihood": min_likelihood,
                "include_if_matched": include_if_matched,
                "required": required,
                "titlecase": titlecase,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Person,
                    parse_obj_as(
                        type_=Person,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def person_identify(
        self,
        *,
        name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        street_address: typing.Optional[str] = None,
        locality: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        school: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        email_hash: typing.Optional[str] = None,
        profile: typing.Optional[str] = None,
        lid: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        pretty: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        data_include: typing.Optional[str] = None,
        include_if_matched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Person]:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            The person's full name, at least first and last

        first_name : typing.Optional[str]
            The person's first name

        last_name : typing.Optional[str]
            The person's last name

        middle_name : typing.Optional[str]
            The person's middle name

        location : typing.Optional[str]
            A location in which a person lives

        street_address : typing.Optional[str]
            A street address in which the person lives

        locality : typing.Optional[str]
            A locality in which the person lives

        region : typing.Optional[str]
            A state or region in which the person lives

        country : typing.Optional[str]
            A country in which the person lives

        postal_code : typing.Optional[str]
            The postal code where the person lives. If there is no value for country, the postal code is assumed to be US

        company : typing.Optional[str]
            A name, website, or social url of a company where the person has worked

        school : typing.Optional[str]
            A name, website, or social url of a university or college the person has attended

        phone : typing.Optional[str]
            A phone number the person has used

        email : typing.Optional[str]
            An email the person has used

        email_hash : typing.Optional[str]
            A sha256 email hash

        profile : typing.Optional[str]
            A social profile the person has used. https://docs.peopledatalabs.com/docs/social-networks

        lid : typing.Optional[str]
            The person's LinkedIn ID

        birth_date : typing.Optional[str]
            The person's birth date: either the year or a full birth date in the format YYYY-MM-DD

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase the person data in 200 responses.

        data_include : typing.Optional[str]
            A comma-separated string of fields that you would like the response to include. Begin the string with a - if you would instead like to exclude the specified fields. If you would like to exclude all data from being returned, use data_include=""

        include_if_matched : typing.Optional[bool]
            If true, the response will include the field matches.matched_on that contains a list of every query input that matched this profile

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Person]
            Profiles Found
        """
        _response = self._client_wrapper.httpx_client.request(
            "v5/person/identify",
            method="GET",
            params={
                "name": name,
                "first_name": first_name,
                "last_name": last_name,
                "middle_name": middle_name,
                "location": location,
                "street_address": street_address,
                "locality": locality,
                "region": region,
                "country": country,
                "postal_code": postal_code,
                "company": company,
                "school": school,
                "phone": phone,
                "email": email,
                "email_hash": email_hash,
                "profile": profile,
                "lid": lid,
                "birth_date": birth_date,
                "pretty": pretty,
                "titlecase": titlecase,
                "data_include": data_include,
                "include_if_matched": include_if_matched,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Person,
                    parse_obj_as(
                        type_=Person,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def person_search(
        self, *, request: PostV5PersonSearchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Person]:
        """
        Parameters
        ----------
        request : PostV5PersonSearchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Person]
            Person Found
        """
        _response = self._client_wrapper.httpx_client.request(
            "v5/person/search",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostV5PersonSearchRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Person,
                    parse_obj_as(
                        type_=Person,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def person_retrieve(
        self,
        person_id: str,
        *,
        titlecase: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PersonRetrieve]:
        """
        Parameters
        ----------
        person_id : str
            The ID of a person

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase the person data in 200 responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PersonRetrieve]
            Person Found
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v5/person/retrieve/{encode_path_param(person_id)}",
            method="GET",
            params={
                "titlecase": titlecase,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonRetrieve,
                    parse_obj_as(
                        type_=PersonRetrieve,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    def person_retrieve_bulk(
        self,
        *,
        titlecase: typing.Optional[bool] = None,
        requests: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PersonRetrieveBulk]:
        """
        Parameters
        ----------
        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase the person data in 200 responses.

        requests : typing.Optional[typing.Sequence[typing.Any]]
            requests contains a list of objects that have a Person ID and optional metadata object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PersonRetrieveBulk]
            Person Found
        """
        _response = self._client_wrapper.httpx_client.request(
            "v5/person/retrieve/bulk",
            method="POST",
            params={
                "titlecase": titlecase,
            },
            json={
                "requests": requests,
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
                    PersonRetrieveBulk,
                    parse_obj_as(
                        type_=PersonRetrieveBulk,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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


class AsyncRawPersonEndpointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def person_enrich(
        self,
        *,
        pdl_id: typing.Optional[str] = None,
        name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        street_address: typing.Optional[str] = None,
        locality: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        school: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        email_hash: typing.Optional[str] = None,
        profile: typing.Optional[str] = None,
        lid: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        data_include: typing.Optional[str] = None,
        pretty: typing.Optional[bool] = None,
        min_likelihood: typing.Optional[int] = None,
        include_if_matched: typing.Optional[bool] = None,
        required: typing.Optional[str] = None,
        titlecase: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Person]:
        """
        Parameters
        ----------
        pdl_id : typing.Optional[str]
            The PDL ID of the person to enrich

        name : typing.Optional[str]
            The person's full name, at least first and last

        first_name : typing.Optional[str]
            The person's first name

        last_name : typing.Optional[str]
            The person's last name

        middle_name : typing.Optional[str]
            The person's middle name

        location : typing.Optional[str]
            A location in which a person lives

        street_address : typing.Optional[str]
            A street address in which the person lives

        locality : typing.Optional[str]
            A locality in which the person lives

        region : typing.Optional[str]
            A state or region in which the person lives

        country : typing.Optional[str]
            A country in which the person lives

        postal_code : typing.Optional[str]
            The postal code where the person lives. If there is no value for country, the postal code is assumed to be US

        company : typing.Optional[str]
            A name, website, or social url of a company where the person has worked

        school : typing.Optional[str]
            A name, website, or social url of a university or college the person has attended

        phone : typing.Optional[str]
            A phone number the person has used

        email : typing.Optional[str]
            An email the person has used

        email_hash : typing.Optional[str]
            A SHA-256 or MD5 email hash

        profile : typing.Optional[str]
            A social profile the person has used. https://docs.peopledatalabs.com/docs/social-networks

        lid : typing.Optional[str]
            The person's LinkedIn ID

        birth_date : typing.Optional[str]
            The person's birth date: either the year or a full birth date in the format YYYY-MM-DD

        data_include : typing.Optional[str]
            A comma-separated string of fields that you would like the response to include. Begin the string with a - if you would instead like to exclude the specified fields. If you would like to exclude all data from being returned, use data_include=""

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        min_likelihood : typing.Optional[int]
            The minimum likelihood score that a response must have in order to count as a match

        include_if_matched : typing.Optional[bool]
            If set to true, includes a top-level (alongside "data", "status", etc) field "matched" which includes a value for each queried field parameter that was "matched-on" during our internal query.

        required : typing.Optional[str]
            The fields a response must have in order to count as a match

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase the person data in 200 responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Person]
            Person Found
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v5/person/enrich",
            method="GET",
            params={
                "pdl_id": pdl_id,
                "name": name,
                "first_name": first_name,
                "last_name": last_name,
                "middle_name": middle_name,
                "location": location,
                "street_address": street_address,
                "locality": locality,
                "region": region,
                "country": country,
                "postal_code": postal_code,
                "company": company,
                "school": school,
                "phone": phone,
                "email": email,
                "email_hash": email_hash,
                "profile": profile,
                "lid": lid,
                "birth_date": birth_date,
                "data_include": data_include,
                "pretty": pretty,
                "min_likelihood": min_likelihood,
                "include_if_matched": include_if_matched,
                "required": required,
                "titlecase": titlecase,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Person,
                    parse_obj_as(
                        type_=Person,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def person_identify(
        self,
        *,
        name: typing.Optional[str] = None,
        first_name: typing.Optional[str] = None,
        last_name: typing.Optional[str] = None,
        middle_name: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        street_address: typing.Optional[str] = None,
        locality: typing.Optional[str] = None,
        region: typing.Optional[str] = None,
        country: typing.Optional[str] = None,
        postal_code: typing.Optional[str] = None,
        company: typing.Optional[str] = None,
        school: typing.Optional[str] = None,
        phone: typing.Optional[str] = None,
        email: typing.Optional[str] = None,
        email_hash: typing.Optional[str] = None,
        profile: typing.Optional[str] = None,
        lid: typing.Optional[str] = None,
        birth_date: typing.Optional[str] = None,
        pretty: typing.Optional[bool] = None,
        titlecase: typing.Optional[bool] = None,
        data_include: typing.Optional[str] = None,
        include_if_matched: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Person]:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            The person's full name, at least first and last

        first_name : typing.Optional[str]
            The person's first name

        last_name : typing.Optional[str]
            The person's last name

        middle_name : typing.Optional[str]
            The person's middle name

        location : typing.Optional[str]
            A location in which a person lives

        street_address : typing.Optional[str]
            A street address in which the person lives

        locality : typing.Optional[str]
            A locality in which the person lives

        region : typing.Optional[str]
            A state or region in which the person lives

        country : typing.Optional[str]
            A country in which the person lives

        postal_code : typing.Optional[str]
            The postal code where the person lives. If there is no value for country, the postal code is assumed to be US

        company : typing.Optional[str]
            A name, website, or social url of a company where the person has worked

        school : typing.Optional[str]
            A name, website, or social url of a university or college the person has attended

        phone : typing.Optional[str]
            A phone number the person has used

        email : typing.Optional[str]
            An email the person has used

        email_hash : typing.Optional[str]
            A sha256 email hash

        profile : typing.Optional[str]
            A social profile the person has used. https://docs.peopledatalabs.com/docs/social-networks

        lid : typing.Optional[str]
            The person's LinkedIn ID

        birth_date : typing.Optional[str]
            The person's birth date: either the year or a full birth date in the format YYYY-MM-DD

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase the person data in 200 responses.

        data_include : typing.Optional[str]
            A comma-separated string of fields that you would like the response to include. Begin the string with a - if you would instead like to exclude the specified fields. If you would like to exclude all data from being returned, use data_include=""

        include_if_matched : typing.Optional[bool]
            If true, the response will include the field matches.matched_on that contains a list of every query input that matched this profile

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Person]
            Profiles Found
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v5/person/identify",
            method="GET",
            params={
                "name": name,
                "first_name": first_name,
                "last_name": last_name,
                "middle_name": middle_name,
                "location": location,
                "street_address": street_address,
                "locality": locality,
                "region": region,
                "country": country,
                "postal_code": postal_code,
                "company": company,
                "school": school,
                "phone": phone,
                "email": email,
                "email_hash": email_hash,
                "profile": profile,
                "lid": lid,
                "birth_date": birth_date,
                "pretty": pretty,
                "titlecase": titlecase,
                "data_include": data_include,
                "include_if_matched": include_if_matched,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Person,
                    parse_obj_as(
                        type_=Person,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def person_search(
        self, *, request: PostV5PersonSearchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Person]:
        """
        Parameters
        ----------
        request : PostV5PersonSearchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Person]
            Person Found
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v5/person/search",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostV5PersonSearchRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Person,
                    parse_obj_as(
                        type_=Person,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def person_retrieve(
        self,
        person_id: str,
        *,
        titlecase: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PersonRetrieve]:
        """
        Parameters
        ----------
        person_id : str
            The ID of a person

        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase the person data in 200 responses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PersonRetrieve]
            Person Found
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v5/person/retrieve/{encode_path_param(person_id)}",
            method="GET",
            params={
                "titlecase": titlecase,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PersonRetrieve,
                    parse_obj_as(
                        type_=PersonRetrieve,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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

    async def person_retrieve_bulk(
        self,
        *,
        titlecase: typing.Optional[bool] = None,
        requests: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PersonRetrieveBulk]:
        """
        Parameters
        ----------
        titlecase : typing.Optional[bool]
            Setting titlecase to true will titlecase the person data in 200 responses.

        requests : typing.Optional[typing.Sequence[typing.Any]]
            requests contains a list of objects that have a Person ID and optional metadata object.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PersonRetrieveBulk]
            Person Found
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v5/person/retrieve/bulk",
            method="POST",
            params={
                "titlecase": titlecase,
            },
            json={
                "requests": requests,
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
                    PersonRetrieveBulk,
                    parse_obj_as(
                        type_=PersonRetrieveBulk,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 402:
                raise PaymentRequiredError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 405:
                raise MethodNotAllowedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
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
