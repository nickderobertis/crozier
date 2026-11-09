

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.conference_deaf_response import ConferenceDeafResponse
from ..types.conference_hangup_response import ConferenceHangupResponse
from ..types.conference_kick_response import ConferenceKickResponse
from ..types.conference_list_members_response import ConferenceListMembersResponse
from ..types.conference_list_response import ConferenceListResponse
from ..types.conference_mute_response import ConferenceMuteResponse
from ..types.conference_play_response import ConferencePlayResponse
from ..types.conference_record_start_parameters_file_format import ConferenceRecordStartParametersFileFormat
from ..types.conference_record_start_response import ConferenceRecordStartResponse
from ..types.conference_record_stop_response import ConferenceRecordStopResponse
from ..types.conference_speak_response import ConferenceSpeakResponse
from ..types.conference_undeaf_response import ConferenceUndeafResponse
from ..types.conference_unmute_response import ConferenceUnmuteResponse
from .raw_client import AsyncRawConferenceClient, RawConferenceClient


OMIT = typing.cast(typing.Any, ...)


class ConferenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawConferenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawConferenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawConferenceClient
        """
        return self._raw_client

    def v01conference_deaf(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceDeafResponse:
        """
        Blocks audio to one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceDeafResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_deaf(
            conference_name="Room402",
            member_id="13,42",
        )
        """
        _response = self._raw_client.v01conference_deaf(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    def v01conference_hangup(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceHangupResponse:
        """
        Kicks one or more conference members, without playing the kick sound

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceHangupResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_hangup(
            conference_name="Room402",
            member_id="13,42",
        )
        """
        _response = self._raw_client.v01conference_hangup(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    def v01conference_kick(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceKickResponse:
        """
        Kicks one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceKickResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_kick(
            conference_name="Room402",
            member_id="13,42",
        )
        """
        _response = self._raw_client.v01conference_kick(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    def v01conference_list(
        self,
        *,
        call_uuid_filter: typing.Optional[str] = OMIT,
        deaf_filter: typing.Optional[bool] = OMIT,
        member_filter: typing.Optional[str] = OMIT,
        muted_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferenceListResponse:
        """
        Returns a list of all established conferences

        Parameters
        ----------
        call_uuid_filter : typing.Optional[str]
            Restricts listed calls to the provided values (comma separated call UUID list)

        deaf_filter : typing.Optional[bool]
            Restricts listed members to deaf ones

        member_filter : typing.Optional[str]
            Restricts listed members to the provided values (comma separated member ID list)

        muted_filter : typing.Optional[bool]
            Restricts listed members to muted ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceListResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_list()
        """
        _response = self._raw_client.v01conference_list(
            call_uuid_filter=call_uuid_filter,
            deaf_filter=deaf_filter,
            member_filter=member_filter,
            muted_filter=muted_filter,
            request_options=request_options,
        )
        return _response.data

    def v01conference_list_members(
        self,
        *,
        conference_name: str,
        call_uuid_filter: typing.Optional[str] = OMIT,
        deaf_filter: typing.Optional[bool] = OMIT,
        member_filter: typing.Optional[str] = OMIT,
        muted_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferenceListMembersResponse:
        """
        Retrieves the member list for a given conference

        Parameters
        ----------
        conference_name : str
            Name of the conference

        call_uuid_filter : typing.Optional[str]
            Restricts listed calls to the provided values (comma separated call UUID list)

        deaf_filter : typing.Optional[bool]
            Restricts listed members to deaf ones

        member_filter : typing.Optional[str]
            Restricts listed members to the provided values (comma separated member ID list)

        muted_filter : typing.Optional[bool]
            Restricts listed members to muted ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceListMembersResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_list_members(
            conference_name="Room402",
        )
        """
        _response = self._raw_client.v01conference_list_members(
            conference_name=conference_name,
            call_uuid_filter=call_uuid_filter,
            deaf_filter=deaf_filter,
            member_filter=member_filter,
            muted_filter=muted_filter,
            request_options=request_options,
        )
        return _response.data

    def v01conference_mute(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceMuteResponse:
        """
        Blocks audio from one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceMuteResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_mute(
            conference_name="Room402",
            member_id="13,42",
        )
        """
        _response = self._raw_client.v01conference_mute(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    def v01conference_play(
        self,
        *,
        conference_name: str,
        file_path: str,
        member_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferencePlayResponse:
        """
        Plays media to one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        file_path : str
            Path/URI of the media file to be played

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferencePlayResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_play(
            conference_name="Room402",
            file_path="/var/local/media/sample.wav",
            member_id="13,42",
        )
        """
        _response = self._raw_client.v01conference_play(
            conference_name=conference_name, file_path=file_path, member_id=member_id, request_options=request_options
        )
        return _response.data

    def v01conference_record_start(
        self,
        *,
        conference_name: str,
        file_format: typing.Optional[ConferenceRecordStartParametersFileFormat] = OMIT,
        file_name: typing.Optional[str] = OMIT,
        file_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferenceRecordStartResponse:
        """
        Initiates a conference recording

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        file_format : typing.Optional[ConferenceRecordStartParametersFileFormat]
            File format (extension)

        file_name : typing.Optional[str]
            Recording file name (without extension); if empty, a timestamp based file name will be generated

        file_path : typing.Optional[str]
            Directory path/URI where the recording file will be saved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceRecordStartResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_record_start(
            conference_name="Room402",
        )
        """
        _response = self._raw_client.v01conference_record_start(
            conference_name=conference_name,
            file_format=file_format,
            file_name=file_name,
            file_path=file_path,
            request_options=request_options,
        )
        return _response.data

    def v01conference_record_stop(
        self, *, conference_name: str, record_file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceRecordStopResponse:
        """
        Stops a conference recording

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        record_file : str
            Full path to recording file, as returned by ConferenceRecordStart; `all` shorthand is also available

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceRecordStopResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_record_stop(
            conference_name="Room402",
            record_file="/tmp/recording/sample.wav",
        )
        """
        _response = self._raw_client.v01conference_record_stop(
            conference_name=conference_name, record_file=record_file, request_options=request_options
        )
        return _response.data

    def v01conference_speak(
        self,
        *,
        conference_name: str,
        member_id: str,
        text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferenceSpeakResponse:
        """
        Plays synthesized speech into a conference

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        text : str
            Text to be synthesized

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceSpeakResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_speak(
            conference_name="Room402",
            member_id="13,42",
            text="The quick brown fox jumps over the lazy dog",
        )
        """
        _response = self._raw_client.v01conference_speak(
            conference_name=conference_name, member_id=member_id, text=text, request_options=request_options
        )
        return _response.data

    def v01conference_undeaf(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceUndeafResponse:
        """
        Restores audio to one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceUndeafResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_undeaf(
            conference_name="Room402",
            member_id="13,42",
        )
        """
        _response = self._raw_client.v01conference_undeaf(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    def v01conference_unmute(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceUnmuteResponse:
        """
        Restores audio from one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceUnmuteResponse
            Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.conference.v01conference_unmute(
            conference_name="Room402",
            member_id="13,42",
        )
        """
        _response = self._raw_client.v01conference_unmute(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data


class AsyncConferenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawConferenceClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawConferenceClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawConferenceClient
        """
        return self._raw_client

    async def v01conference_deaf(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceDeafResponse:
        """
        Blocks audio to one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceDeafResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_deaf(
                conference_name="Room402",
                member_id="13,42",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_deaf(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    async def v01conference_hangup(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceHangupResponse:
        """
        Kicks one or more conference members, without playing the kick sound

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceHangupResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_hangup(
                conference_name="Room402",
                member_id="13,42",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_hangup(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    async def v01conference_kick(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceKickResponse:
        """
        Kicks one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceKickResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_kick(
                conference_name="Room402",
                member_id="13,42",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_kick(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    async def v01conference_list(
        self,
        *,
        call_uuid_filter: typing.Optional[str] = OMIT,
        deaf_filter: typing.Optional[bool] = OMIT,
        member_filter: typing.Optional[str] = OMIT,
        muted_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferenceListResponse:
        """
        Returns a list of all established conferences

        Parameters
        ----------
        call_uuid_filter : typing.Optional[str]
            Restricts listed calls to the provided values (comma separated call UUID list)

        deaf_filter : typing.Optional[bool]
            Restricts listed members to deaf ones

        member_filter : typing.Optional[str]
            Restricts listed members to the provided values (comma separated member ID list)

        muted_filter : typing.Optional[bool]
            Restricts listed members to muted ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceListResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_list()


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_list(
            call_uuid_filter=call_uuid_filter,
            deaf_filter=deaf_filter,
            member_filter=member_filter,
            muted_filter=muted_filter,
            request_options=request_options,
        )
        return _response.data

    async def v01conference_list_members(
        self,
        *,
        conference_name: str,
        call_uuid_filter: typing.Optional[str] = OMIT,
        deaf_filter: typing.Optional[bool] = OMIT,
        member_filter: typing.Optional[str] = OMIT,
        muted_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferenceListMembersResponse:
        """
        Retrieves the member list for a given conference

        Parameters
        ----------
        conference_name : str
            Name of the conference

        call_uuid_filter : typing.Optional[str]
            Restricts listed calls to the provided values (comma separated call UUID list)

        deaf_filter : typing.Optional[bool]
            Restricts listed members to deaf ones

        member_filter : typing.Optional[str]
            Restricts listed members to the provided values (comma separated member ID list)

        muted_filter : typing.Optional[bool]
            Restricts listed members to muted ones

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceListMembersResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_list_members(
                conference_name="Room402",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_list_members(
            conference_name=conference_name,
            call_uuid_filter=call_uuid_filter,
            deaf_filter=deaf_filter,
            member_filter=member_filter,
            muted_filter=muted_filter,
            request_options=request_options,
        )
        return _response.data

    async def v01conference_mute(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceMuteResponse:
        """
        Blocks audio from one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceMuteResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_mute(
                conference_name="Room402",
                member_id="13,42",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_mute(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    async def v01conference_play(
        self,
        *,
        conference_name: str,
        file_path: str,
        member_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferencePlayResponse:
        """
        Plays media to one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        file_path : str
            Path/URI of the media file to be played

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferencePlayResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_play(
                conference_name="Room402",
                file_path="/var/local/media/sample.wav",
                member_id="13,42",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_play(
            conference_name=conference_name, file_path=file_path, member_id=member_id, request_options=request_options
        )
        return _response.data

    async def v01conference_record_start(
        self,
        *,
        conference_name: str,
        file_format: typing.Optional[ConferenceRecordStartParametersFileFormat] = OMIT,
        file_name: typing.Optional[str] = OMIT,
        file_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferenceRecordStartResponse:
        """
        Initiates a conference recording

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        file_format : typing.Optional[ConferenceRecordStartParametersFileFormat]
            File format (extension)

        file_name : typing.Optional[str]
            Recording file name (without extension); if empty, a timestamp based file name will be generated

        file_path : typing.Optional[str]
            Directory path/URI where the recording file will be saved

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceRecordStartResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_record_start(
                conference_name="Room402",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_record_start(
            conference_name=conference_name,
            file_format=file_format,
            file_name=file_name,
            file_path=file_path,
            request_options=request_options,
        )
        return _response.data

    async def v01conference_record_stop(
        self, *, conference_name: str, record_file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceRecordStopResponse:
        """
        Stops a conference recording

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        record_file : str
            Full path to recording file, as returned by ConferenceRecordStart; `all` shorthand is also available

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceRecordStopResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_record_stop(
                conference_name="Room402",
                record_file="/tmp/recording/sample.wav",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_record_stop(
            conference_name=conference_name, record_file=record_file, request_options=request_options
        )
        return _response.data

    async def v01conference_speak(
        self,
        *,
        conference_name: str,
        member_id: str,
        text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ConferenceSpeakResponse:
        """
        Plays synthesized speech into a conference

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        text : str
            Text to be synthesized

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceSpeakResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_speak(
                conference_name="Room402",
                member_id="13,42",
                text="The quick brown fox jumps over the lazy dog",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_speak(
            conference_name=conference_name, member_id=member_id, text=text, request_options=request_options
        )
        return _response.data

    async def v01conference_undeaf(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceUndeafResponse:
        """
        Restores audio to one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceUndeafResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_undeaf(
                conference_name="Room402",
                member_id="13,42",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_undeaf(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data

    async def v01conference_unmute(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ConferenceUnmuteResponse:
        """
        Restores audio from one or more conference members

        Parameters
        ----------
        conference_name : str
            Name of the conference in question

        member_id : str
            List of comma separated member IDs to be affected; `all` shorthand is available too.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ConferenceUnmuteResponse
            Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.conference.v01conference_unmute(
                conference_name="Room402",
                member_id="13,42",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v01conference_unmute(
            conference_name=conference_name, member_id=member_id, request_options=request_options
        )
        return _response.data
