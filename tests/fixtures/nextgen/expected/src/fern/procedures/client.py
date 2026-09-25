

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok92 import Ok92
from ..types.ok93 import Ok93
from .raw_client import AsyncRawProceduresClient, RawProceduresClient


OMIT = typing.cast(typing.Any, ...)


class ProceduresClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProceduresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProceduresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProceduresClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_procedures(
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
    ) -> Ok92:
        """
        Gets a patient's procedures summary.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose procedures summary is being fetched

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
        Ok92
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.procedures.base_url_persons_person_id_chart_procedures(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_procedures(
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

    def base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
        self,
        person_id: str,
        encounter_id: str,
        procedure_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok93:
        """
        Gets a specific patient procedure.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of patient's encounter

        procedure_id : str
            (Required) (Required) The id of patient's procedure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok93
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.procedures.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
            person_id="personId",
            encounter_id="encounterId",
            procedure_id="procedureId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
            person_id, encounter_id, procedure_id, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
        self,
        person_id: str,
        encounter_id: str,
        procedure_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient procedure

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of patient's encounter

        procedure_id : str
            (Required) (Required) The id of patient's procedure

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
        client.procedures.put_base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
            person_id="personId",
            encounter_id="encounterId",
            procedure_id="procedureId",
            request={"key": "value"},
        )
        """
        _response = (
            self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
                person_id, encounter_id, procedure_id, request=request, request_options=request_options
            )
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id1(
        self,
        person_id: str,
        encounter_id: str,
        procedure_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a patient procedure

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of patient's encounter

        procedure_id : str
            (Required) (Required) The id of patient's procedure

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
        client.procedures.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id1(
            person_id="personId",
            encounter_id="encounterId",
            procedure_id="procedureId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id1(
            person_id, encounter_id, procedure_id, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_encounters_encounter_id_procedures(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add a procedure to patient's encounter

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient's encounter

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
        client.procedures.base_url_persons_person_id_chart_encounters_encounter_id_procedures(
            person_id="personId",
            encounter_id="encounterId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_procedures(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncProceduresClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProceduresClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProceduresClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProceduresClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_procedures(
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
    ) -> Ok92:
        """
        Gets a patient's procedures summary.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose procedures summary is being fetched

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
        Ok92
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.procedures.base_url_persons_person_id_chart_procedures(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_procedures(
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

    async def base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
        self,
        person_id: str,
        encounter_id: str,
        procedure_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Ok93:
        """
        Gets a specific patient procedure.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of patient's encounter

        procedure_id : str
            (Required) (Required) The id of patient's procedure

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Ok93
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.procedures.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
                person_id="personId",
                encounter_id="encounterId",
                procedure_id="procedureId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
                person_id, encounter_id, procedure_id, request_options=request_options
            )
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
        self,
        person_id: str,
        encounter_id: str,
        procedure_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient procedure

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of patient's encounter

        procedure_id : str
            (Required) (Required) The id of patient's procedure

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
            await client.procedures.put_base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
                person_id="personId",
                encounter_id="encounterId",
                procedure_id="procedureId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.put_base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id(
                person_id, encounter_id, procedure_id, request=request, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id1(
        self,
        person_id: str,
        encounter_id: str,
        procedure_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a patient procedure

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of patient's encounter

        procedure_id : str
            (Required) (Required) The id of patient's procedure

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
            await client.procedures.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id1(
                person_id="personId",
                encounter_id="encounterId",
                procedure_id="procedureId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_procedures_procedure_id1(
                person_id, encounter_id, procedure_id, request_options=request_options
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_encounters_encounter_id_procedures(
        self,
        person_id: str,
        encounter_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Add a procedure to patient's encounter

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient

        encounter_id : str
            (Required) (Required) The id of the patient's encounter

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
            await client.procedures.base_url_persons_person_id_chart_encounters_encounter_id_procedures(
                person_id="personId",
                encounter_id="encounterId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_encounters_encounter_id_procedures(
            person_id, encounter_id, request=request, request_options=request_options
        )
        return _response.data
