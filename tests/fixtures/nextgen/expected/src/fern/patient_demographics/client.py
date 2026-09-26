

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok78 import Ok78
from ..types.ok79 import Ok79
from ..types.ok81 import Ok81
from ..types.ok83 import Ok83
from ..types.ok84 import Ok84
from .raw_client import AsyncRawPatientDemographicsClient, RawPatientDemographicsClient


OMIT = typing.cast(typing.Any, ...)


class PatientDemographicsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPatientDemographicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPatientDemographicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPatientDemographicsClient
        """
        return self._raw_client

    def base_url_persons(
        self,
        *,
        patients_only: str,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok78:
        """
        Gets a list of persons/patients. If OData $filter criteria for createTimestamp and/or /modifyTimestamp are not specified, the default behavior of this route is to return results for persons/patients that have been created or modified in the last 7 days.

        Parameters
        ----------
        patients_only : str

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok78
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.base_url_persons(
            patients_only="patientsOnly",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons(
            patients_only=patients_only,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    def post_base_url_persons(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a new person

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.post_base_url_persons(
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons(request=request, request_options=request_options)
        return _response.data

    def base_url_persons_person_id(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok79:
        """
        Gets the demographics for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose demographics are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok79
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.base_url_persons_person_id(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id(person_id, request_options=request_options)
        return _response.data

    def base_url_persons_person_id1(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a person's demographic information

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id for the person being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.base_url_persons_person_id1(
            person_id="personId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id1(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    def patch_base_url_persons_person_id(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates properties on existing person demographics given in the request.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose demographics are being updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.patch_base_url_persons_person_id(
            person_id="personId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.patch_base_url_persons_person_id(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_address_histories(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok79:
        """
        Gets the address histories for the specified personId.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose demographics are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok79
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.base_url_persons_person_id_address_histories(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_address_histories(
            person_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_ethnicities(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok81:
        """
        Gets the ethnicities for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ethnicities are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok81
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.base_url_persons_person_id_ethnicities(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_ethnicities(person_id, request_options=request_options)
        return _response.data

    def base_url_persons_person_id_gender_identities(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok81:
        """
        Gets the gender identities for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ethnicities are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok81
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.base_url_persons_person_id_gender_identities(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_gender_identities(
            person_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_races(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok83:
        """
        Gets the races for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose races are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok83
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.base_url_persons_person_id_races(
            person_id="personId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_races(person_id, request_options=request_options)
        return _response.data

    def base_url_persons_lookup(
        self,
        *,
        name: str,
        first_name: str,
        last_name: str,
        middle_name: str,
        prior_last_name: str,
        address_line1: str,
        city: str,
        zip: str,
        sex: str,
        current_gender: str,
        date_of_birth: str,
        external_id: str,
        external_system_id: str,
        exclude_expired: str,
        is_next_md_enabled: str,
        search_patients_only: str,
        quick_search_id: str,
        quick_search_input: str,
        expand: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok84:
        """
        Gets a list of persons/patients based on various search criteria.  Since these results are returned from a /persons/ endpoint, the "id" of each result (whose value is a guid) is a personId and can be used as the value of personId in all other routes that require a personId.

        Using the /persons/lookup route:

        -At least one query parameter must be provided as lookup criteria.
        -Use of multiple criteria is allowed, and will results will include person records matching all criteria.
        -The two "quickSearch" parameters are exceptions to the above; see the quickSearchId & quickSearchInput parameter descriptions for details.

        Parameters
        ----------
        name : str

        first_name : str

        last_name : str

        middle_name : str

        prior_last_name : str

        address_line1 : str

        city : str

        zip : str

        sex : str

        current_gender : str

        date_of_birth : str

        external_id : str

        external_system_id : str

        exclude_expired : str

        is_next_md_enabled : str

        search_patients_only : str

        quick_search_id : str

        quick_search_input : str

        expand : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok84
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.base_url_persons_lookup(
            name="name",
            first_name="firstName",
            last_name="lastName",
            middle_name="middleName",
            prior_last_name="priorLastName",
            address_line1="addressLine1",
            city="city",
            zip="zip",
            sex="sex",
            current_gender="currentGender",
            date_of_birth="dateOfBirth",
            external_id="externalId",
            external_system_id="externalSystemId",
            exclude_expired="excludeExpired",
            is_next_md_enabled="isNextMdEnabled",
            search_patients_only="searchPatientsOnly",
            quick_search_id="quickSearchId",
            quick_search_input="quickSearchInput",
            expand="$expand",
        )
        """
        _response = self._raw_client.base_url_persons_lookup(
            name=name,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            prior_last_name=prior_last_name,
            address_line1=address_line1,
            city=city,
            zip=zip,
            sex=sex,
            current_gender=current_gender,
            date_of_birth=date_of_birth,
            external_id=external_id,
            external_system_id=external_system_id,
            exclude_expired=exclude_expired,
            is_next_md_enabled=is_next_md_enabled,
            search_patients_only=search_patients_only,
            quick_search_id=quick_search_id,
            quick_search_input=quick_search_input,
            expand=expand,
            request_options=request_options,
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok78:
        """
        While this route does not directly return USCDI data, knowledge of an encounterId is sometimes necessary to utilize other routes to obtain USCDI data.

        This route returns a list of encounters (each identified by "id", which in all other routes will be an {encounterId} whose value is a guid) for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose encounters are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok78
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.patient_demographics.base_url_persons_person_id_chart_encounters(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data


class AsyncPatientDemographicsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPatientDemographicsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPatientDemographicsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPatientDemographicsClient
        """
        return self._raw_client

    async def base_url_persons(
        self,
        *,
        patients_only: str,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok78:
        """
        Gets a list of persons/patients. If OData $filter criteria for createTimestamp and/or /modifyTimestamp are not specified, the default behavior of this route is to return results for persons/patients that have been created or modified in the last 7 days.

        Parameters
        ----------
        patients_only : str

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok78
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.base_url_persons(
                patients_only="patientsOnly",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons(
            patients_only=patients_only,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data

    async def post_base_url_persons(
        self, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a new person

        Parameters
        ----------
        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.post_base_url_persons(
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons(request=request, request_options=request_options)
        return _response.data

    async def base_url_persons_person_id(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok79:
        """
        Gets the demographics for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose demographics are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok79
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.base_url_persons_person_id(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id(person_id, request_options=request_options)
        return _response.data

    async def base_url_persons_person_id1(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a person's demographic information

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id for the person being updated

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.base_url_persons_person_id1(
                person_id="personId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id1(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    async def patch_base_url_persons_person_id(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates properties on existing person demographics given in the request.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose demographics are being updated.

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.patch_base_url_persons_person_id(
                person_id="personId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch_base_url_persons_person_id(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_address_histories(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok79:
        """
        Gets the address histories for the specified personId.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose demographics are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok79
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.base_url_persons_person_id_address_histories(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_address_histories(
            person_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_ethnicities(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok81:
        """
        Gets the ethnicities for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ethnicities are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok81
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.base_url_persons_person_id_ethnicities(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_ethnicities(
            person_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_gender_identities(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok81:
        """
        Gets the gender identities for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose ethnicities are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok81
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.base_url_persons_person_id_gender_identities(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_gender_identities(
            person_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_races(
        self, person_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok83:
        """
        Gets the races for the specified person id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the person whose races are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok83
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.base_url_persons_person_id_races(
                person_id="personId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_races(person_id, request_options=request_options)
        return _response.data

    async def base_url_persons_lookup(
        self,
        *,
        name: str,
        first_name: str,
        last_name: str,
        middle_name: str,
        prior_last_name: str,
        address_line1: str,
        city: str,
        zip: str,
        sex: str,
        current_gender: str,
        date_of_birth: str,
        external_id: str,
        external_system_id: str,
        exclude_expired: str,
        is_next_md_enabled: str,
        search_patients_only: str,
        quick_search_id: str,
        quick_search_input: str,
        expand: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok84:
        """
        Gets a list of persons/patients based on various search criteria.  Since these results are returned from a /persons/ endpoint, the "id" of each result (whose value is a guid) is a personId and can be used as the value of personId in all other routes that require a personId.

        Using the /persons/lookup route:

        -At least one query parameter must be provided as lookup criteria.
        -Use of multiple criteria is allowed, and will results will include person records matching all criteria.
        -The two "quickSearch" parameters are exceptions to the above; see the quickSearchId & quickSearchInput parameter descriptions for details.

        Parameters
        ----------
        name : str

        first_name : str

        last_name : str

        middle_name : str

        prior_last_name : str

        address_line1 : str

        city : str

        zip : str

        sex : str

        current_gender : str

        date_of_birth : str

        external_id : str

        external_system_id : str

        exclude_expired : str

        is_next_md_enabled : str

        search_patients_only : str

        quick_search_id : str

        quick_search_input : str

        expand : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok84
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.base_url_persons_lookup(
                name="name",
                first_name="firstName",
                last_name="lastName",
                middle_name="middleName",
                prior_last_name="priorLastName",
                address_line1="addressLine1",
                city="city",
                zip="zip",
                sex="sex",
                current_gender="currentGender",
                date_of_birth="dateOfBirth",
                external_id="externalId",
                external_system_id="externalSystemId",
                exclude_expired="excludeExpired",
                is_next_md_enabled="isNextMdEnabled",
                search_patients_only="searchPatientsOnly",
                quick_search_id="quickSearchId",
                quick_search_input="quickSearchInput",
                expand="$expand",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_lookup(
            name=name,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            prior_last_name=prior_last_name,
            address_line1=address_line1,
            city=city,
            zip=zip,
            sex=sex,
            current_gender=current_gender,
            date_of_birth=date_of_birth,
            external_id=external_id,
            external_system_id=external_system_id,
            exclude_expired=exclude_expired,
            is_next_md_enabled=is_next_md_enabled,
            search_patients_only=search_patients_only,
            quick_search_id=quick_search_id,
            quick_search_input=quick_search_input,
            expand=expand,
            request_options=request_options,
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters(
        self,
        person_id: str,
        *,
        top: str,
        filter: str,
        orderby: str,
        skip: str,
        inlinecount: str,
        count: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok78:
        """
        While this route does not directly return USCDI data, knowledge of an encounterId is sometimes necessary to utilize other routes to obtain USCDI data.

        This route returns a list of encounters (each identified by "id", which in all other routes will be an {encounterId} whose value is a guid) for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose encounters are being retrieved

        top : str

        filter : str

        orderby : str

        skip : str

        inlinecount : str

        count : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok78
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.patient_demographics.base_url_persons_person_id_chart_encounters(
                person_id="personId",
                top="$top",
                filter="$filter",
                orderby="$orderby",
                skip="$skip",
                inlinecount="$inlinecount",
                count="$count",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters(
            person_id,
            top=top,
            filter=filter,
            orderby=orderby,
            skip=skip,
            inlinecount=inlinecount,
            count=count,
            request_options=request_options,
        )
        return _response.data
