

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok97 import Ok97
from ..types.ok98 import Ok98
from .raw_client import AsyncRawVitalSignsClient, RawVitalSignsClient


OMIT = typing.cast(typing.Any, ...)


class VitalSignsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVitalSignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVitalSignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVitalSignsClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_vitals(
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
    ) -> Ok97:
        """
        Gets a list of vital sign summaries for the given person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose vital signs are being retrieved

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
        Ok97
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.vital_signs.base_url_persons_person_id_chart_vitals(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_vitals(
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

    def base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
        self,
        person_id: str,
        encounter_id: str,
        vitals_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok98:
        """
        Gets the vital sign details for the given person id, encounter id, and vital signs id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose vital signs are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the vital signs were taken

        vitals_id : str
            (Required) (Required) The id of the vital signs that are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok98
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.vital_signs.base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
            person_id="personId",
            encounter_id="encounterId",
            vitals_id="vitalsId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
            person_id, encounter_id, vitals_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
        self,
        person_id: str,
        encounter_id: str,
        vitals_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok98:
        """
        Updates Vital Signs for the given person id, encounter id and vital signs Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose vital signs are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the vital signs were taken

        vitals_id : str
            (Required) (Required) The id of the vital signs that are being retrieved

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok98
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.vital_signs.put_base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
            person_id="personId",
            encounter_id="encounterId",
            vitals_id="vitalsId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
            person_id, encounter_id, vitals_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_vitals(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok98:
        """
        Updates Vital Signs for the given person id, encounter id and vital signs Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose vital signs are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the vital signs were taken

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok98
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.vital_signs.base_url_persons_person_id_chart_encounters_encounter_id_vitals(
            person_id="personId",
            encounter_id="encounterId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_vitals(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncVitalSignsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVitalSignsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVitalSignsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVitalSignsClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_vitals(
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
    ) -> Ok97:
        """
        Gets a list of vital sign summaries for the given person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose vital signs are being retrieved

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
        Ok97
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.vital_signs.base_url_persons_person_id_chart_vitals(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_vitals(
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

    async def base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
        self,
        person_id: str,
        encounter_id: str,
        vitals_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok98:
        """
        Gets the vital sign details for the given person id, encounter id, and vital signs id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose vital signs are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the vital signs were taken

        vitals_id : str
            (Required) (Required) The id of the vital signs that are being retrieved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok98
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.vital_signs.base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
                person_id="personId",
                encounter_id="encounterId",
                vitals_id="vitalsId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
            person_id, encounter_id, vitals_id, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
        self,
        person_id: str,
        encounter_id: str,
        vitals_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok98:
        """
        Updates Vital Signs for the given person id, encounter id and vital signs Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose vital signs are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the vital signs were taken

        vitals_id : str
            (Required) (Required) The id of the vital signs that are being retrieved

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok98
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.vital_signs.put_base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
                person_id="personId",
                encounter_id="encounterId",
                vitals_id="vitalsId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_vitals_vitals_id(
                person_id, encounter_id, vitals_id, request=request, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_vitals(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok98:
        """
        Updates Vital Signs for the given person id, encounter id and vital signs Id.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose vital signs are being retrieved

        encounter_id : str
            (Required) (Required) The id of the encounter in which the vital signs were taken

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok98
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.vital_signs.base_url_persons_person_id_chart_encounters_encounter_id_vitals(
                person_id="personId",
                encounter_id="encounterId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_vitals(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data
