

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ok94 import Ok94
from ..types.ok95 import Ok95
from ..types.ok96 import Ok96
from .raw_client import AsyncRawSmokingStatusClient, RawSmokingStatusClient


class SmokingStatusClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSmokingStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSmokingStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSmokingStatusClient
        """
        return self._raw_client

    def base_url_persons_person_id_chart_health_concerns_tobacco_smoking_usage_status(
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
    ) -> Ok94:
        """
        Gets a patient's tobacco uses status for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns tobacco uses status are being retrieved.

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
        Ok94
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.smoking_status.base_url_persons_person_id_chart_health_concerns_tobacco_smoking_usage_status(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_health_concerns_tobacco_smoking_usage_status(
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

    def base_url_persons_person_id_chart_social_history(
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
    ) -> Ok95:
        """
        Gets a list of social history for the given person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose social history is being retrieved

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
        Ok95
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.smoking_status.base_url_persons_person_id_chart_social_history(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_social_history(
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

    def base_url_persons_person_id_chart_tobacco_usage(
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
    ) -> Ok96:
        """
        Gets a list of tobacco usage for the given person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose tobacco usage is being retrieved

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
        Ok96
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            accept="YOUR_ACCEPT",
        )
        client.smoking_status.base_url_persons_person_id_chart_tobacco_usage(
            person_id="personId",
            top="$top",
            filter="$filter",
            orderby="$orderby",
            skip="$skip",
            inlinecount="$inlinecount",
            count="$count",
        )
        """
        _response = self._raw_client.base_url_persons_person_id_chart_tobacco_usage(
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


class AsyncSmokingStatusClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSmokingStatusClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSmokingStatusClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSmokingStatusClient
        """
        return self._raw_client

    async def base_url_persons_person_id_chart_health_concerns_tobacco_smoking_usage_status(
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
    ) -> Ok94:
        """
        Gets a patient's tobacco uses status for health concern.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose health concerns tobacco uses status are being retrieved.

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
        Ok94
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.smoking_status.base_url_persons_person_id_chart_health_concerns_tobacco_smoking_usage_status(
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
        _response = (
            await self._raw_client.base_url_persons_person_id_chart_health_concerns_tobacco_smoking_usage_status(
                person_id,
                top=top,
                filter=filter,
                orderby=orderby,
                skip=skip,
                inlinecount=inlinecount,
                count=count,
                request_options=request_options,
            )
        )
        return _response.data

    async def base_url_persons_person_id_chart_social_history(
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
    ) -> Ok95:
        """
        Gets a list of social history for the given person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose social history is being retrieved

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
        Ok95
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.smoking_status.base_url_persons_person_id_chart_social_history(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_social_history(
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

    async def base_url_persons_person_id_chart_tobacco_usage(
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
    ) -> Ok96:
        """
        Gets a list of tobacco usage for the given person id after applying additional OData query operations.

        Parameters
        ----------
        person_id : str
            (Required) (Required) The id of the patient whose tobacco usage is being retrieved

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
        Ok96
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            accept="YOUR_ACCEPT",
        )


        async def main() -> None:
            await client.smoking_status.base_url_persons_person_id_chart_tobacco_usage(
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
        _response = await self._raw_client.base_url_persons_person_id_chart_tobacco_usage(
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
