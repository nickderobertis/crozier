

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok import Ok
from ..types.ok1 import Ok1
from ..types.ok4 import Ok4
from ..types.ok6 import Ok6
from ..types.ok7 import Ok7
from .raw_client import AsyncRawAllergiesAndIntolerancesClient, RawAllergiesAndIntolerancesClient


OMIT = typing.cast(typing.Any, ...)


class AllergiesAndIntolerancesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAllergiesAndIntolerancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAllergiesAndIntolerancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAllergiesAndIntolerancesClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_allergies(
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
    ) -> Ok:
        """
        Returns a list of allergy summaries for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

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
        Ok
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.allergies_and_intolerances.base_url_persons_person_id_chart_allergies(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_allergies(
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

    def base_url_persons_person_id_chart_allergies_allergy_id(
        self, person_id: str, allergy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok1:
        """
        Gets the allergy details for the given person id and allergy id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        allergy_id : str
            (Required) (Required) The id of the allergy being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok1
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.allergies_and_intolerances.base_url_persons_person_id_chart_allergies_allergy_id(
            person_id="personId",
            allergy_id="allergyId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_allergies_allergy_id(
            person_id, allergy_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_allergies_allergy_id_dur_check(
        self, person_id: str, allergy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok1:
        """
        StartFragmentGets a list of interactions for a given allergyId.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        allergy_id : str
            (Required) (Required) The id of the allergy being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok1
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.allergies_and_intolerances.base_url_persons_person_id_chart_allergies_allergy_id_dur_check(
            person_id="personId",
            allergy_id="allergyId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_allergies_allergy_id_dur_check(
            person_id, allergy_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_deleted_allergies(
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
    ) -> Ok:
        """
        Gets a list of patient deleted allergies after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

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
        Ok
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.allergies_and_intolerances.base_url_persons_person_id_chart_deleted_allergies(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_deleted_allergies(
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

    def base_url_persons_person_id_chart_encounters_encounter_id_allergies(
        self,
        person_id: str,
        encounter_id: str,
        *,
        include_resolved: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok4:
        """
        Gets a list of allergy summaries for the given person id and encounter id, with the option of including resolved allergies.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the allergies were added

        include_resolved : str
            A true or false value that includes or excludes allergies that are resolved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok4
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies(
            person_id="personId",
            encounter_id="encounterId",
            include_resolved="includeResolved",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies(
            person_id, encounter_id, include_resolved=include_resolved, request_options=request_options
        )
        return _response.data

    def post_base_url_persons_person_id_chart_encounters_encounter_id_allergies(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add the allergy to patient's encounter

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy is being added

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

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
        client.allergies_and_intolerances.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies(
            person_id="personId",
            encounter_id="encounterId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id1(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok1:
        """
        Gets the allergy details for the given person id, encounter id, and allergy id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the allergy was added

        allergy_id : str
            (Required) (Required) The id of the allergy being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok1
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id1(
            person_id="personId",
            encounter_id="encounterId",
            allergy_id="allergyId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id1(
            person_id, encounter_id, allergy_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update a patient allergy

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to be updated

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
        client.allergies_and_intolerances.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
            person_id="personId",
            encounter_id="encounterId",
            allergy_id="allergyId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
            person_id, encounter_id, allergy_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a patient's allergy

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy is being deleted

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to be deleted

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
        client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
            person_id="personId",
            encounter_id="encounterId",
            allergy_id="allergyId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
            person_id, encounter_id, allergy_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok6:
        """
        Gets a list of reactions a patient experiences for the given allergy id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the allergy being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok6
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
            person_id="personId",
            encounter_id="encounterId",
            allergy_id="allergyId",
        )
        """
        _response = (
            self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
                person_id, encounter_id, allergy_id, request_options=request_options
            )
        )
        return _response.data

    def post_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a reaction that the patient experiences for the given allergy id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy reaction is being added

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to which the reaction belongs

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
        client.allergies_and_intolerances.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
            person_id="personId",
            encounter_id="encounterId",
            allergy_id="allergyId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
            person_id, encounter_id, allergy_id, request=request, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        reaction_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a reaction that the patient experiences for the given allergy id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy reaction is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to which the reaction belongs

        reaction_id : str
            (Required) (Required) The id of the patient's allergy reaction to be updated

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
        client.allergies_and_intolerances.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
            person_id="personId",
            encounter_id="encounterId",
            allergy_id="allergyId",
            reaction_id="reactionId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
            person_id, encounter_id, allergy_id, reaction_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        reaction_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a reaction that the patient experiences for the given allergy id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy reaction is being deleted

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to which the reaction belongs

        reaction_id : str
            (Required) (Required) The id of the patient's allergy reaction to be deleted

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
        client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
            person_id="personId",
            encounter_id="encounterId",
            allergy_id="allergyId",
            reaction_id="reactionId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
            person_id, encounter_id, allergy_id, reaction_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_health_concerns_allergies(
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
    ) -> Ok7:
        """
        Gets a patient's health concerns allergies.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns allergies are being retrieved.

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
        Ok7
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.allergies_and_intolerances.base_url_persons_person_id_chart_health_concerns_allergies(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_health_concerns_allergies(
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


class AsyncAllergiesAndIntolerancesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAllergiesAndIntolerancesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAllergiesAndIntolerancesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAllergiesAndIntolerancesClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_allergies(
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
    ) -> Ok:
        """
        Returns a list of allergy summaries for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

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
        Ok
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_allergies(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_allergies(
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

    async def base_url_persons_person_id_chart_allergies_allergy_id(
        self, person_id: str, allergy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok1:
        """
        Gets the allergy details for the given person id and allergy id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        allergy_id : str
            (Required) (Required) The id of the allergy being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok1
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_allergies_allergy_id(
                person_id="personId",
                allergy_id="allergyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_allergies_allergy_id(
            person_id, allergy_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_allergies_allergy_id_dur_check(
        self, person_id: str, allergy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Ok1:
        """
        StartFragmentGets a list of interactions for a given allergyId.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        allergy_id : str
            (Required) (Required) The id of the allergy being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok1
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_allergies_allergy_id_dur_check(
                person_id="personId",
                allergy_id="allergyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_allergies_allergy_id_dur_check(
            person_id, allergy_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_deleted_allergies(
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
    ) -> Ok:
        """
        Gets a list of patient deleted allergies after applying additional OData operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

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
        Ok
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_deleted_allergies(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_deleted_allergies(
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

    async def base_url_persons_person_id_chart_encounters_encounter_id_allergies(
        self,
        person_id: str,
        encounter_id: str,
        *,
        include_resolved: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok4:
        """
        Gets a list of allergy summaries for the given person id and encounter id, with the option of including resolved allergies.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the allergies were added

        include_resolved : str
            A true or false value that includes or excludes allergies that are resolved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok4
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies(
                person_id="personId",
                encounter_id="encounterId",
                include_resolved="includeResolved",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies(
            person_id, encounter_id, include_resolved=include_resolved, request_options=request_options
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_encounters_encounter_id_allergies(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add the allergy to patient's encounter

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy is being added

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

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
            await client.allergies_and_intolerances.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies(
                person_id="personId",
                encounter_id="encounterId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id1(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok1:
        """
        Gets the allergy details for the given person id, encounter id, and allergy id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the allergy was added

        allergy_id : str
            (Required) (Required) The id of the allergy being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok1
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id1(
                person_id="personId",
                encounter_id="encounterId",
                allergy_id="allergyId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id1(
                person_id, encounter_id, allergy_id, request_options=request_options
            )
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update a patient allergy

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to be updated

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
            await client.allergies_and_intolerances.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
                person_id="personId",
                encounter_id="encounterId",
                allergy_id="allergyId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
                person_id, encounter_id, allergy_id, request=request, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete a patient's allergy

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy is being deleted

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to be deleted

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
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
                person_id="personId",
                encounter_id="encounterId",
                allergy_id="allergyId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id(
                person_id, encounter_id, allergy_id, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok6:
        """
        Gets a list of reactions a patient experiences for the given allergy id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergies are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the allergy being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok6
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
                person_id="personId",
                encounter_id="encounterId",
                allergy_id="allergyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
            person_id, encounter_id, allergy_id, request_options=request_options
        )
        return _response.data

    async def post_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Adds a reaction that the patient experiences for the given allergy id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy reaction is being added

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to which the reaction belongs

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
            await client.allergies_and_intolerances.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
                person_id="personId",
                encounter_id="encounterId",
                allergy_id="allergyId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions(
            person_id, encounter_id, allergy_id, request=request, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        reaction_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a reaction that the patient experiences for the given allergy id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy reaction is being updated

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to which the reaction belongs

        reaction_id : str
            (Required) (Required) The id of the patient's allergy reaction to be updated

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
            await client.allergies_and_intolerances.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
                person_id="personId",
                encounter_id="encounterId",
                allergy_id="allergyId",
                reaction_id="reactionId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
            person_id, encounter_id, allergy_id, reaction_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
        self,
        person_id: str,
        encounter_id: str,
        allergy_id: str,
        reaction_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a reaction that the patient experiences for the given allergy id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose allergy reaction is being deleted

        encounter_id : str
            (Required) (Required) The id of the encounter to which the patient allergy belongs

        allergy_id : str
            (Required) (Required) The id of the patient's allergy to which the reaction belongs

        reaction_id : str
            (Required) (Required) The id of the patient's allergy reaction to be deleted

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
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
                person_id="personId",
                encounter_id="encounterId",
                allergy_id="allergyId",
                reaction_id="reactionId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_allergies_allergy_id_reactions_reaction_id(
            person_id, encounter_id, allergy_id, reaction_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_health_concerns_allergies(
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
    ) -> Ok7:
        """
        Gets a patient's health concerns allergies.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns allergies are being retrieved.

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
        Ok7
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.allergies_and_intolerances.base_url_persons_person_id_chart_health_concerns_allergies(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_health_concerns_allergies(
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
