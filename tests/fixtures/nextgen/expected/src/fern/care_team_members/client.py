

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok11 import Ok11
from .raw_client import AsyncRawCareTeamMembersClient, RawCareTeamMembersClient


OMIT = typing.cast(typing.Any, ...)


class CareTeamMembersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCareTeamMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCareTeamMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCareTeamMembersClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_care_team_members(
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
    ) -> Ok11:
        """
        Returns a list of care team members for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care team members are being retrieved

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
        Ok11
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.care_team_members.base_url_persons_person_id_chart_care_team_members(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_care_team_members(
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

    def post_base_url_persons_person_id_chart_care_team_members(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Add care team member for the specified person id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care team members are being saved

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.care_team_members.post_base_url_persons_person_id_chart_care_team_members(
            person_id="personId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.post_base_url_persons_person_id_chart_care_team_members(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    def put_base_url_persons_person_id_chart_care_team_members_care_team_member_id(
        self,
        person_id: str,
        care_team_member_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's care team member record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of patient whose care team member record is being updated

        care_team_member_id : str
            (Required) (Required) The id of the care team member being updated

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
        client.care_team_members.put_base_url_persons_person_id_chart_care_team_members_care_team_member_id(
            person_id="personId",
            care_team_member_id="careTeamMemberId",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.put_base_url_persons_person_id_chart_care_team_members_care_team_member_id(
            person_id, care_team_member_id, request=request, request_options=request_options
        )
        return _response.data

    def base_url_persons_person_id_chart_care_team_members_care_team_member_id(
        self, person_id: str, care_team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a patient's care team member

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of patient whose care team member record is being deleted

        care_team_member_id : str
            (Required) (Required) The id of the care team member being deleted

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
        client.care_team_members.base_url_persons_person_id_chart_care_team_members_care_team_member_id(
            person_id="personId",
            care_team_member_id="careTeamMemberId",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_care_team_members_care_team_member_id(
            person_id, care_team_member_id, request_options=request_options
        )
        return _response.data


class AsyncCareTeamMembersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCareTeamMembersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCareTeamMembersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCareTeamMembersClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_care_team_members(
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
    ) -> Ok11:
        """
        Returns a list of care team members for the specified person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care team members are being retrieved

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
        Ok11
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.care_team_members.base_url_persons_person_id_chart_care_team_members(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_care_team_members(
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

    async def post_base_url_persons_person_id_chart_care_team_members(
        self, person_id: str, *, request: typing.Any, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Add care team member for the specified person id

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose care team members are being saved

        request : typing.Any

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.care_team_members.post_base_url_persons_person_id_chart_care_team_members(
                person_id="personId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_base_url_persons_person_id_chart_care_team_members(
            person_id, request=request, request_options=request_options
        )
        return _response.data

    async def put_base_url_persons_person_id_chart_care_team_members_care_team_member_id(
        self,
        person_id: str,
        care_team_member_id: str,
        *,
        request: typing.Any,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Updates a patient's care team member record

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of patient whose care team member record is being updated

        care_team_member_id : str
            (Required) (Required) The id of the care team member being updated

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
            await client.care_team_members.put_base_url_persons_person_id_chart_care_team_members_care_team_member_id(
                person_id="personId",
                care_team_member_id="careTeamMemberId",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_base_url_persons_person_id_chart_care_team_members_care_team_member_id(
            person_id, care_team_member_id, request=request, request_options=request_options
        )
        return _response.data

    async def base_url_persons_person_id_chart_care_team_members_care_team_member_id(
        self, person_id: str, care_team_member_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Deletes a patient's care team member

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of patient whose care team member record is being deleted

        care_team_member_id : str
            (Required) (Required) The id of the care team member being deleted

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
            await client.care_team_members.base_url_persons_person_id_chart_care_team_members_care_team_member_id(
                person_id="personId",
                care_team_member_id="careTeamMemberId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.base_url_persons_person_id_chart_care_team_members_care_team_member_id(
            person_id, care_team_member_id, request_options=request_options
        )
        return _response.data
