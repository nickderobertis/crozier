

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.person import Person
from ..types.person_retrieve import PersonRetrieve
from ..types.person_retrieve_bulk import PersonRetrieveBulk
from .raw_client import AsyncRawPersonEndpointsClient, RawPersonEndpointsClient
from .types.post_v5person_search_request import PostV5PersonSearchRequest


OMIT = typing.cast(typing.Any, ...)


class PersonEndpointsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPersonEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPersonEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPersonEndpointsClient
        """
        return self._raw_client

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
    ) -> Person:
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
        Person
            Person Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.person_endpoints.person_enrich(
            pdl_id="qEnOZ5Oh0poWnQ1luFBfVw_0000",
            name="Jennifer C. Jackson",
            first_name="Jennifer",
            last_name="Jackson",
            middle_name="Cassandra",
            location="Medford, OR USA",
            street_address="1234 Main Street",
            locality="Boise",
            region="Idaho",
            country="United States",
            postal_code="83701",
            company="Amazon",
            school="University of Iowa",
            phone="+1 555-234-1234",
            email="renee.c.paulsen1959@yahoo.com",
            email_hash="e206e6cd7fa5f9499fd6d2d943dcf7d9c1469bad351061483f5ce7181663b8d4",
            profile="https://linkedin.com/in/seanthorne",
            lid="145991517",
            birth_date="1996-10-01",
            data_include="full_name,emails.address",
            required="education AND (emails OR phone_numbers)",
        )
        """
        _response = self._raw_client.person_enrich(
            pdl_id=pdl_id,
            name=name,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            location=location,
            street_address=street_address,
            locality=locality,
            region=region,
            country=country,
            postal_code=postal_code,
            company=company,
            school=school,
            phone=phone,
            email=email,
            email_hash=email_hash,
            profile=profile,
            lid=lid,
            birth_date=birth_date,
            data_include=data_include,
            pretty=pretty,
            min_likelihood=min_likelihood,
            include_if_matched=include_if_matched,
            required=required,
            titlecase=titlecase,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Person:
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
        Person
            Profiles Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.person_endpoints.person_identify(
            name="Jennifer C. Jackson",
            first_name="Jennifer",
            last_name="Jackson",
            middle_name="Cassandra",
            location="Medford, OR USA",
            street_address="1234 Main Street",
            locality="Boise",
            region="Idaho",
            country="United States",
            postal_code="83701",
            company="Amazon",
            school="University of Iowa",
            phone="+1 555-234-1234",
            email="renee.c.paulsen1959@yahoo.com",
            email_hash="e206e6cd7fa5f9499fd6d2d943dcf7d9c1469bad351061483f5ce7181663b8d4",
            profile="https://linkedin.com/in/seanthorne",
            lid="145991517",
            birth_date="1996-10-01",
            data_include="full_name,emails.address",
        )
        """
        _response = self._raw_client.person_identify(
            name=name,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            location=location,
            street_address=street_address,
            locality=locality,
            region=region,
            country=country,
            postal_code=postal_code,
            company=company,
            school=school,
            phone=phone,
            email=email,
            email_hash=email_hash,
            profile=profile,
            lid=lid,
            birth_date=birth_date,
            pretty=pretty,
            titlecase=titlecase,
            data_include=data_include,
            include_if_matched=include_if_matched,
            request_options=request_options,
        )
        return _response.data

    def person_search(
        self, *, request: PostV5PersonSearchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> Person:
        """
        Parameters
        ----------
        request : PostV5PersonSearchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Person
            Person Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.person_endpoints.person_search(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.person_search(request=request, request_options=request_options)
        return _response.data

    def person_retrieve(
        self,
        person_id: str,
        *,
        titlecase: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonRetrieve:
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
        PersonRetrieve
            Person Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.person_endpoints.person_retrieve(
            person_id="person_id",
        )
        """
        _response = self._raw_client.person_retrieve(person_id, titlecase=titlecase, request_options=request_options)
        return _response.data

    def person_retrieve_bulk(
        self,
        *,
        titlecase: typing.Optional[bool] = None,
        requests: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonRetrieveBulk:
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
        PersonRetrieveBulk
            Person Found

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.person_endpoints.person_retrieve_bulk()
        """
        _response = self._raw_client.person_retrieve_bulk(
            titlecase=titlecase, requests=requests, request_options=request_options
        )
        return _response.data


class AsyncPersonEndpointsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPersonEndpointsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPersonEndpointsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPersonEndpointsClient
        """
        return self._raw_client

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
    ) -> Person:
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
        Person
            Person Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.person_endpoints.person_enrich(
                pdl_id="qEnOZ5Oh0poWnQ1luFBfVw_0000",
                name="Jennifer C. Jackson",
                first_name="Jennifer",
                last_name="Jackson",
                middle_name="Cassandra",
                location="Medford, OR USA",
                street_address="1234 Main Street",
                locality="Boise",
                region="Idaho",
                country="United States",
                postal_code="83701",
                company="Amazon",
                school="University of Iowa",
                phone="+1 555-234-1234",
                email="renee.c.paulsen1959@yahoo.com",
                email_hash="e206e6cd7fa5f9499fd6d2d943dcf7d9c1469bad351061483f5ce7181663b8d4",
                profile="https://linkedin.com/in/seanthorne",
                lid="145991517",
                birth_date="1996-10-01",
                data_include="full_name,emails.address",
                required="education AND (emails OR phone_numbers)",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.person_enrich(
            pdl_id=pdl_id,
            name=name,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            location=location,
            street_address=street_address,
            locality=locality,
            region=region,
            country=country,
            postal_code=postal_code,
            company=company,
            school=school,
            phone=phone,
            email=email,
            email_hash=email_hash,
            profile=profile,
            lid=lid,
            birth_date=birth_date,
            data_include=data_include,
            pretty=pretty,
            min_likelihood=min_likelihood,
            include_if_matched=include_if_matched,
            required=required,
            titlecase=titlecase,
            request_options=request_options,
        )
        return _response.data

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
    ) -> Person:
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
        Person
            Profiles Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.person_endpoints.person_identify(
                name="Jennifer C. Jackson",
                first_name="Jennifer",
                last_name="Jackson",
                middle_name="Cassandra",
                location="Medford, OR USA",
                street_address="1234 Main Street",
                locality="Boise",
                region="Idaho",
                country="United States",
                postal_code="83701",
                company="Amazon",
                school="University of Iowa",
                phone="+1 555-234-1234",
                email="renee.c.paulsen1959@yahoo.com",
                email_hash="e206e6cd7fa5f9499fd6d2d943dcf7d9c1469bad351061483f5ce7181663b8d4",
                profile="https://linkedin.com/in/seanthorne",
                lid="145991517",
                birth_date="1996-10-01",
                data_include="full_name,emails.address",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.person_identify(
            name=name,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            location=location,
            street_address=street_address,
            locality=locality,
            region=region,
            country=country,
            postal_code=postal_code,
            company=company,
            school=school,
            phone=phone,
            email=email,
            email_hash=email_hash,
            profile=profile,
            lid=lid,
            birth_date=birth_date,
            pretty=pretty,
            titlecase=titlecase,
            data_include=data_include,
            include_if_matched=include_if_matched,
            request_options=request_options,
        )
        return _response.data

    async def person_search(
        self, *, request: PostV5PersonSearchRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> Person:
        """
        Parameters
        ----------
        request : PostV5PersonSearchRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Person
            Person Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.person_endpoints.person_search(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.person_search(request=request, request_options=request_options)
        return _response.data

    async def person_retrieve(
        self,
        person_id: str,
        *,
        titlecase: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonRetrieve:
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
        PersonRetrieve
            Person Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.person_endpoints.person_retrieve(
                person_id="person_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.person_retrieve(
            person_id, titlecase=titlecase, request_options=request_options
        )
        return _response.data

    async def person_retrieve_bulk(
        self,
        *,
        titlecase: typing.Optional[bool] = None,
        requests: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PersonRetrieveBulk:
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
        PersonRetrieveBulk
            Person Found

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.person_endpoints.person_retrieve_bulk()


        asyncio.run(main())
        """
        _response = await self._raw_client.person_retrieve_bulk(
            titlecase=titlecase, requests=requests, request_options=request_options
        )
        return _response.data
