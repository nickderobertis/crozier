

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawConferenceClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def v01conference_deaf(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConferenceDeafResponse]:
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
        HttpResponse[ConferenceDeafResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceDeaf/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceDeafResponse,
                    parse_obj_as(
                        type_=ConferenceDeafResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_hangup(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConferenceHangupResponse]:
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
        HttpResponse[ConferenceHangupResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceHangup/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceHangupResponse,
                    parse_obj_as(
                        type_=ConferenceHangupResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_kick(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConferenceKickResponse]:
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
        HttpResponse[ConferenceKickResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceKick/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceKickResponse,
                    parse_obj_as(
                        type_=ConferenceKickResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_list(
        self,
        *,
        call_uuid_filter: typing.Optional[str] = OMIT,
        deaf_filter: typing.Optional[bool] = OMIT,
        member_filter: typing.Optional[str] = OMIT,
        muted_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConferenceListResponse]:
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
        HttpResponse[ConferenceListResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceList/",
            method="POST",
            data={
                "CallUUIDFilter": call_uuid_filter,
                "DeafFilter": deaf_filter,
                "MemberFilter": member_filter,
                "MutedFilter": muted_filter,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceListResponse,
                    parse_obj_as(
                        type_=ConferenceListResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_list_members(
        self,
        *,
        conference_name: str,
        call_uuid_filter: typing.Optional[str] = OMIT,
        deaf_filter: typing.Optional[bool] = OMIT,
        member_filter: typing.Optional[str] = OMIT,
        muted_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConferenceListMembersResponse]:
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
        HttpResponse[ConferenceListMembersResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceListMembers/",
            method="POST",
            data={
                "CallUUIDFilter": call_uuid_filter,
                "ConferenceName": conference_name,
                "DeafFilter": deaf_filter,
                "MemberFilter": member_filter,
                "MutedFilter": muted_filter,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceListMembersResponse,
                    parse_obj_as(
                        type_=ConferenceListMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_mute(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConferenceMuteResponse]:
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
        HttpResponse[ConferenceMuteResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceMute/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceMuteResponse,
                    parse_obj_as(
                        type_=ConferenceMuteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_play(
        self,
        *,
        conference_name: str,
        file_path: str,
        member_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConferencePlayResponse]:
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
        HttpResponse[ConferencePlayResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferencePlay/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "FilePath": file_path,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferencePlayResponse,
                    parse_obj_as(
                        type_=ConferencePlayResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_record_start(
        self,
        *,
        conference_name: str,
        file_format: typing.Optional[ConferenceRecordStartParametersFileFormat] = OMIT,
        file_name: typing.Optional[str] = OMIT,
        file_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConferenceRecordStartResponse]:
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
        HttpResponse[ConferenceRecordStartResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceRecordStart/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "FileFormat": file_format,
                "FileName": file_name,
                "FilePath": file_path,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceRecordStartResponse,
                    parse_obj_as(
                        type_=ConferenceRecordStartResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_record_stop(
        self, *, conference_name: str, record_file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConferenceRecordStopResponse]:
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
        HttpResponse[ConferenceRecordStopResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceRecordStop/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "RecordFile": record_file,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceRecordStopResponse,
                    parse_obj_as(
                        type_=ConferenceRecordStopResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_speak(
        self,
        *,
        conference_name: str,
        member_id: str,
        text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ConferenceSpeakResponse]:
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
        HttpResponse[ConferenceSpeakResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceSpeak/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
                "Text": text,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceSpeakResponse,
                    parse_obj_as(
                        type_=ConferenceSpeakResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_undeaf(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConferenceUndeafResponse]:
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
        HttpResponse[ConferenceUndeafResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceUndeaf/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceUndeafResponse,
                    parse_obj_as(
                        type_=ConferenceUndeafResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def v01conference_unmute(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ConferenceUnmuteResponse]:
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
        HttpResponse[ConferenceUnmuteResponse]
            Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceUnmute/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceUnmuteResponse,
                    parse_obj_as(
                        type_=ConferenceUnmuteResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawConferenceClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def v01conference_deaf(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConferenceDeafResponse]:
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
        AsyncHttpResponse[ConferenceDeafResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceDeaf/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceDeafResponse,
                    parse_obj_as(
                        type_=ConferenceDeafResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_hangup(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConferenceHangupResponse]:
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
        AsyncHttpResponse[ConferenceHangupResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceHangup/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceHangupResponse,
                    parse_obj_as(
                        type_=ConferenceHangupResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_kick(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConferenceKickResponse]:
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
        AsyncHttpResponse[ConferenceKickResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceKick/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceKickResponse,
                    parse_obj_as(
                        type_=ConferenceKickResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_list(
        self,
        *,
        call_uuid_filter: typing.Optional[str] = OMIT,
        deaf_filter: typing.Optional[bool] = OMIT,
        member_filter: typing.Optional[str] = OMIT,
        muted_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConferenceListResponse]:
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
        AsyncHttpResponse[ConferenceListResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceList/",
            method="POST",
            data={
                "CallUUIDFilter": call_uuid_filter,
                "DeafFilter": deaf_filter,
                "MemberFilter": member_filter,
                "MutedFilter": muted_filter,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceListResponse,
                    parse_obj_as(
                        type_=ConferenceListResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_list_members(
        self,
        *,
        conference_name: str,
        call_uuid_filter: typing.Optional[str] = OMIT,
        deaf_filter: typing.Optional[bool] = OMIT,
        member_filter: typing.Optional[str] = OMIT,
        muted_filter: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConferenceListMembersResponse]:
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
        AsyncHttpResponse[ConferenceListMembersResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceListMembers/",
            method="POST",
            data={
                "CallUUIDFilter": call_uuid_filter,
                "ConferenceName": conference_name,
                "DeafFilter": deaf_filter,
                "MemberFilter": member_filter,
                "MutedFilter": muted_filter,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceListMembersResponse,
                    parse_obj_as(
                        type_=ConferenceListMembersResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_mute(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConferenceMuteResponse]:
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
        AsyncHttpResponse[ConferenceMuteResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceMute/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceMuteResponse,
                    parse_obj_as(
                        type_=ConferenceMuteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_play(
        self,
        *,
        conference_name: str,
        file_path: str,
        member_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConferencePlayResponse]:
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
        AsyncHttpResponse[ConferencePlayResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferencePlay/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "FilePath": file_path,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferencePlayResponse,
                    parse_obj_as(
                        type_=ConferencePlayResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_record_start(
        self,
        *,
        conference_name: str,
        file_format: typing.Optional[ConferenceRecordStartParametersFileFormat] = OMIT,
        file_name: typing.Optional[str] = OMIT,
        file_path: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConferenceRecordStartResponse]:
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
        AsyncHttpResponse[ConferenceRecordStartResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceRecordStart/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "FileFormat": file_format,
                "FileName": file_name,
                "FilePath": file_path,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceRecordStartResponse,
                    parse_obj_as(
                        type_=ConferenceRecordStartResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_record_stop(
        self, *, conference_name: str, record_file: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConferenceRecordStopResponse]:
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
        AsyncHttpResponse[ConferenceRecordStopResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceRecordStop/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "RecordFile": record_file,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceRecordStopResponse,
                    parse_obj_as(
                        type_=ConferenceRecordStopResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_speak(
        self,
        *,
        conference_name: str,
        member_id: str,
        text: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ConferenceSpeakResponse]:
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
        AsyncHttpResponse[ConferenceSpeakResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceSpeak/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
                "Text": text,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceSpeakResponse,
                    parse_obj_as(
                        type_=ConferenceSpeakResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_undeaf(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConferenceUndeafResponse]:
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
        AsyncHttpResponse[ConferenceUndeafResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceUndeaf/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceUndeafResponse,
                    parse_obj_as(
                        type_=ConferenceUndeafResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def v01conference_unmute(
        self, *, conference_name: str, member_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ConferenceUnmuteResponse]:
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
        AsyncHttpResponse[ConferenceUnmuteResponse]
            Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0.1/ConferenceUnmute/",
            method="POST",
            data={
                "ConferenceName": conference_name,
                "MemberID": member_id,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ConferenceUnmuteResponse,
                    parse_obj_as(
                        type_=ConferenceUnmuteResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
