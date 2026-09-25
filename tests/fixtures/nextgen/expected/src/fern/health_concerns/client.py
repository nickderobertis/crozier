

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok24 import Ok24
from ..types.ok25 import Ok25
from ..types.ok26 import Ok26
from ..types.ok28 import Ok28
from ..types.ok29 import Ok29
from ..types.ok30 import Ok30
from ..types.ok31 import Ok31
from .raw_client import AsyncRawHealthConcernsClient, RawHealthConcernsClient


OMIT = typing.cast(typing.Any, ...)


class HealthConcernsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawHealthConcernsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawHealthConcernsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawHealthConcernsClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_care_plan_health_concerns(
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
    ) -> Ok24:
        """
        Returns a list of health concerns for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok24
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.health_concerns.base_url_persons_person_id_chart_care_plan_health_concerns(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_care_plan_health_concerns(
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

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates patient's careplan health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) Encounter id for healthconcern

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
        client.health_concerns.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns(
            person_id="personId",
            encounter_id="encounterId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data

    def get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        expand: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok25:
        """
        Returns specific health concern details for a patient.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concern are being fetched

        encounter_id : str
            (Required) (Required) The id of the patient encounter whose health concern are being fetched

        health_concern_id : str
            (Required) (Required) The id of the health concern whose health concern are being fetched

        expand : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok25
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.health_concerns.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            expand="$expand",
        )
        """
        _response = self._raw_client.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
            person_id, encounter_id, health_concern_id, expand=expand, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update patient's careplan health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) Encounter id for healthconcern

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

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
        client.health_concerns.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
            person_id, encounter_id, health_concern_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete health concern details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

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
        client.health_concerns.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
            person_id="personId",
            encounter_id="encounterId",
            health_concern_id="healthConcernId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
            person_id, encounter_id, health_concern_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_health_concerns_encounter_diagnosis(
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
    ) -> Ok26:
        """
        Gets a patient's health concerns encounter diagnosis for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns encounter diagnosis are being retrieved.

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok26
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.health_concerns.base_url_persons_person_id_chart_health_concerns_encounter_diagnosis(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_health_concerns_encounter_diagnosis(
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

    def base_url_persons_person_id_chart_health_concerns_family_histories_organizer(
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
    ) -> Ok28:
        """
        Gets a patient's family histories for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns family histories are being retrieved.

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok28
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.health_concerns.base_url_persons_person_id_chart_health_concerns_family_histories_organizer(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_health_concerns_family_histories_organizer(
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

    def base_url_persons_person_id_chart_health_concerns_problem_observations(
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
    ) -> Ok29:
        """
        Gets a patient's health concerns problem observation.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns problem observation are being retrieved.

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok29
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.health_concerns.base_url_persons_person_id_chart_health_concerns_problem_observations(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_health_concerns_problem_observations(
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

    def base_url_persons_person_id_chart_health_concerns_social_history(
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
    ) -> Ok30:
        """
        Gets a patient's social history for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns social history are being retrieved.

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok30
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.health_concerns.base_url_persons_person_id_chart_health_concerns_social_history(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_health_concerns_social_history(
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

    def base_url_persons_person_id_chart_health_concerns_vitals(
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
    ) -> Ok31:
        """
        Gets a patient's vitals for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concern vitals are being fetched

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok31
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.health_concerns.base_url_persons_person_id_chart_health_concerns_vitals(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_health_concerns_vitals(
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


class AsyncHealthConcernsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawHealthConcernsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawHealthConcernsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawHealthConcernsClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_care_plan_health_concerns(
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
    ) -> Ok24:
        """
        Returns a list of health concerns for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns are being retrieved

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok24
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.health_concerns.base_url_persons_person_id_chart_care_plan_health_concerns(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_care_plan_health_concerns(
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

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Creates patient's careplan health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) Encounter id for healthconcern

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
            await client.health_concerns.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns(
                person_id="personId",
                encounter_id="encounterId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns(
                person_id, encounter_id, request=request, request_options=request_options
            )
        )
        return _response.data

    async def get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        expand: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok25:
        """
        Returns specific health concern details for a patient.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concern are being fetched

        encounter_id : str
            (Required) (Required) The id of the patient encounter whose health concern are being fetched

        health_concern_id : str
            (Required) (Required) The id of the health concern whose health concern are being fetched

        expand : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok25
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.health_concerns.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                expand="$expand",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
            person_id, encounter_id, health_concern_id, expand=expand, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Update patient's careplan health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient.

        encounter_id : str
            (Required) (Required) Encounter id for healthconcern

        health_concern_id : str
            (Required) (Required) Care plan health concern id of patient

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
            await client.health_concerns.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
            person_id, encounter_id, health_concern_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
        self,
        person_id: str,
        encounter_id: str,
        health_concern_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Delete health concern details

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient encounter

        health_concern_id : str
            (Required) (Required) The id of the health concern

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
            await client.health_concerns.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
                person_id="personId",
                encounter_id="encounterId",
                health_concern_id="healthConcernId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_care_plan_health_concerns_health_concern_id(
            person_id, encounter_id, health_concern_id, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_health_concerns_encounter_diagnosis(
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
    ) -> Ok26:
        """
        Gets a patient's health concerns encounter diagnosis for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns encounter diagnosis are being retrieved.

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok26
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.health_concerns.base_url_persons_person_id_chart_health_concerns_encounter_diagnosis(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_health_concerns_encounter_diagnosis(
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

    async def base_url_persons_person_id_chart_health_concerns_family_histories_organizer(
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
    ) -> Ok28:
        """
        Gets a patient's family histories for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns family histories are being retrieved.

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok28
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.health_concerns.base_url_persons_person_id_chart_health_concerns_family_histories_organizer(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_health_concerns_family_histories_organizer(
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

    async def base_url_persons_person_id_chart_health_concerns_problem_observations(
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
    ) -> Ok29:
        """
        Gets a patient's health concerns problem observation.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns problem observation are being retrieved.

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok29
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.health_concerns.base_url_persons_person_id_chart_health_concerns_problem_observations(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_health_concerns_problem_observations(
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

    async def base_url_persons_person_id_chart_health_concerns_social_history(
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
    ) -> Ok30:
        """
        Gets a patient's social history for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns social history are being retrieved.

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok30
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.health_concerns.base_url_persons_person_id_chart_health_concerns_social_history(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_health_concerns_social_history(
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

    async def base_url_persons_person_id_chart_health_concerns_vitals(
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
    ) -> Ok31:
        """
        Gets a patient's vitals for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concern vitals are being fetched

        top : str
            (Required)

        filter : str
            (Required)

        orderby : str
            (Required)

        skip : str
            (Required)

        inlinecount : str
            (Required)

        count : str
            (Required)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok31
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.health_concerns.base_url_persons_person_id_chart_health_concerns_vitals(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_health_concerns_vitals(
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
