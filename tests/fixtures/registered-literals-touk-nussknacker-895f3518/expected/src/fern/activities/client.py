

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.process_activity import ProcessActivity
from ..types.scenario_activities import ScenarioActivities
from ..types.scenario_activities_metadata import ScenarioActivitiesMetadata
from ..types.scenario_attachments import ScenarioAttachments
from .raw_client import AsyncRawActivitiesClient, RawActivitiesClient


OMIT = typing.cast(typing.Any, ...)


class ActivitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawActivitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawActivitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawActivitiesClient
        """
        return self._raw_client

    def post_api_processes_scenarioname_versionid_activity_attachments(
        self,
        scenario_name: str,
        version_id: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        version_id : int

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = self._raw_client.post_api_processes_scenarioname_versionid_activity_attachments(
            scenario_name, version_id, request=request, request_options=request_options
        )
        return _response.data

    def post_api_processes_scenarioname_versionid_activity_comment(
        self, scenario_name: str, version_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        version_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.post_api_processes_scenarioname_versionid_activity_comment(
            scenario_name="scenarioName",
            version_id=1000000,
        )
        """
        _response = self._raw_client.post_api_processes_scenarioname_versionid_activity_comment(
            scenario_name, version_id, request_options=request_options
        )
        return _response.data

    def get_api_processes_scenarioname_activity_attachments(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScenarioAttachments:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioAttachments


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.get_api_processes_scenarioname_activity_attachments(
            scenario_name="scenarioName",
        )
        """
        _response = self._raw_client.get_api_processes_scenarioname_activity_attachments(
            scenario_name, request_options=request_options
        )
        return _response.data

    def get_api_processes_scenarioname_activity_attachments_attachmentid(
        self, scenario_name: str, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Parameters
        ----------
        scenario_name : str

        attachment_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.get_api_processes_scenarioname_activity_attachments_attachmentid(
            scenario_name="scenarioName",
            attachment_id=1000000,
        )
        """
        with self._raw_client.get_api_processes_scenarioname_activity_attachments_attachmentid(
            scenario_name, attachment_id, request_options=request_options
        ) as r:
            yield from r.data

    def delete_api_processes_scenarioname_activity_attachments_attachmentid(
        self, scenario_name: str, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        attachment_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.delete_api_processes_scenarioname_activity_attachments_attachmentid(
            scenario_name="scenarioName",
            attachment_id=1000000,
        )
        """
        _response = self._raw_client.delete_api_processes_scenarioname_activity_attachments_attachmentid(
            scenario_name, attachment_id, request_options=request_options
        )
        return _response.data

    def put_api_processes_scenarioname_activity_comment_scenarioactivityid(
        self, scenario_name: str, scenario_activity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_activity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.put_api_processes_scenarioname_activity_comment_scenarioactivityid(
            scenario_name="scenarioName",
            scenario_activity_id="scenarioActivityId",
        )
        """
        _response = self._raw_client.put_api_processes_scenarioname_activity_comment_scenarioactivityid(
            scenario_name, scenario_activity_id, request_options=request_options
        )
        return _response.data

    def delete_api_processes_scenarioname_activity_comment_scenarioactivityid(
        self, scenario_name: str, scenario_activity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_activity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.delete_api_processes_scenarioname_activity_comment_scenarioactivityid(
            scenario_name="scenarioName",
            scenario_activity_id="scenarioActivityId",
        )
        """
        _response = self._raw_client.delete_api_processes_scenarioname_activity_comment_scenarioactivityid(
            scenario_name, scenario_activity_id, request_options=request_options
        )
        return _response.data

    def post_api_processes_scenarioname_versionid_activity_comments(
        self, scenario_name: str, version_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        version_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.post_api_processes_scenarioname_versionid_activity_comments(
            scenario_name="scenarioName",
            version_id=1000000,
        )
        """
        _response = self._raw_client.post_api_processes_scenarioname_versionid_activity_comments(
            scenario_name, version_id, request_options=request_options
        )
        return _response.data

    def delete_api_processes_scenarioname_activity_comments_commentid(
        self, scenario_name: str, comment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        comment_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.delete_api_processes_scenarioname_activity_comments_commentid(
            scenario_name="scenarioName",
            comment_id=1000000,
        )
        """
        _response = self._raw_client.delete_api_processes_scenarioname_activity_comments_commentid(
            scenario_name, comment_id, request_options=request_options
        )
        return _response.data

    def get_api_processes_scenarioname_activity(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessActivity:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessActivity


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.get_api_processes_scenarioname_activity(
            scenario_name="scenarioName",
        )
        """
        _response = self._raw_client.get_api_processes_scenarioname_activity(
            scenario_name, request_options=request_options
        )
        return _response.data

    def get_api_processes_scenarioname_activity_activities(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScenarioActivities:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioActivities


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.get_api_processes_scenarioname_activity_activities(
            scenario_name="scenarioName",
        )
        """
        _response = self._raw_client.get_api_processes_scenarioname_activity_activities(
            scenario_name, request_options=request_options
        )
        return _response.data

    def get_api_processes_scenarioname_activity_activities_metadata(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScenarioActivitiesMetadata:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioActivitiesMetadata


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )
        client.activities.get_api_processes_scenarioname_activity_activities_metadata(
            scenario_name="scenarioName",
        )
        """
        _response = self._raw_client.get_api_processes_scenarioname_activity_activities_metadata(
            scenario_name, request_options=request_options
        )
        return _response.data


class AsyncActivitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawActivitiesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawActivitiesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawActivitiesClient
        """
        return self._raw_client

    async def post_api_processes_scenarioname_versionid_activity_attachments(
        self,
        scenario_name: str,
        version_id: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        version_id : int

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None
        """
        _response = await self._raw_client.post_api_processes_scenarioname_versionid_activity_attachments(
            scenario_name, version_id, request=request, request_options=request_options
        )
        return _response.data

    async def post_api_processes_scenarioname_versionid_activity_comment(
        self, scenario_name: str, version_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        version_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.post_api_processes_scenarioname_versionid_activity_comment(
                scenario_name="scenarioName",
                version_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_processes_scenarioname_versionid_activity_comment(
            scenario_name, version_id, request_options=request_options
        )
        return _response.data

    async def get_api_processes_scenarioname_activity_attachments(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScenarioAttachments:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioAttachments


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.get_api_processes_scenarioname_activity_attachments(
                scenario_name="scenarioName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_processes_scenarioname_activity_attachments(
            scenario_name, request_options=request_options
        )
        return _response.data

    async def get_api_processes_scenarioname_activity_attachments_attachmentid(
        self, scenario_name: str, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Parameters
        ----------
        scenario_name : str

        attachment_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.get_api_processes_scenarioname_activity_attachments_attachmentid(
                scenario_name="scenarioName",
                attachment_id=1000000,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_api_processes_scenarioname_activity_attachments_attachmentid(
            scenario_name, attachment_id, request_options=request_options
        ) as r:
            async for _chunk in r.data:
                yield _chunk

    async def delete_api_processes_scenarioname_activity_attachments_attachmentid(
        self, scenario_name: str, attachment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        attachment_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.delete_api_processes_scenarioname_activity_attachments_attachmentid(
                scenario_name="scenarioName",
                attachment_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_processes_scenarioname_activity_attachments_attachmentid(
            scenario_name, attachment_id, request_options=request_options
        )
        return _response.data

    async def put_api_processes_scenarioname_activity_comment_scenarioactivityid(
        self, scenario_name: str, scenario_activity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_activity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.put_api_processes_scenarioname_activity_comment_scenarioactivityid(
                scenario_name="scenarioName",
                scenario_activity_id="scenarioActivityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_api_processes_scenarioname_activity_comment_scenarioactivityid(
            scenario_name, scenario_activity_id, request_options=request_options
        )
        return _response.data

    async def delete_api_processes_scenarioname_activity_comment_scenarioactivityid(
        self, scenario_name: str, scenario_activity_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        scenario_activity_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.delete_api_processes_scenarioname_activity_comment_scenarioactivityid(
                scenario_name="scenarioName",
                scenario_activity_id="scenarioActivityId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_processes_scenarioname_activity_comment_scenarioactivityid(
            scenario_name, scenario_activity_id, request_options=request_options
        )
        return _response.data

    async def post_api_processes_scenarioname_versionid_activity_comments(
        self, scenario_name: str, version_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        version_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.post_api_processes_scenarioname_versionid_activity_comments(
                scenario_name="scenarioName",
                version_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_api_processes_scenarioname_versionid_activity_comments(
            scenario_name, version_id, request_options=request_options
        )
        return _response.data

    async def delete_api_processes_scenarioname_activity_comments_commentid(
        self, scenario_name: str, comment_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        scenario_name : str

        comment_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.delete_api_processes_scenarioname_activity_comments_commentid(
                scenario_name="scenarioName",
                comment_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_api_processes_scenarioname_activity_comments_commentid(
            scenario_name, comment_id, request_options=request_options
        )
        return _response.data

    async def get_api_processes_scenarioname_activity(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProcessActivity:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProcessActivity


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.get_api_processes_scenarioname_activity(
                scenario_name="scenarioName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_processes_scenarioname_activity(
            scenario_name, request_options=request_options
        )
        return _response.data

    async def get_api_processes_scenarioname_activity_activities(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScenarioActivities:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioActivities


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.get_api_processes_scenarioname_activity_activities(
                scenario_name="scenarioName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_processes_scenarioname_activity_activities(
            scenario_name, request_options=request_options
        )
        return _response.data

    async def get_api_processes_scenarioname_activity_activities_metadata(
        self, scenario_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ScenarioActivitiesMetadata:
        """
        Parameters
        ----------
        scenario_name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ScenarioActivitiesMetadata


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            nu_impersonate_user_identity="YOUR_NU_IMPERSONATE_USER_IDENTITY",
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.activities.get_api_processes_scenarioname_activity_activities_metadata(
                scenario_name="scenarioName",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_api_processes_scenarioname_activity_activities_metadata(
            scenario_name, request_options=request_options
        )
        return _response.data
