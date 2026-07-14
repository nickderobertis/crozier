

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.ability_score import AbilityScore
from ..types.alignment import Alignment
from ..types.background import Background
from ..types.language import Language
from ..types.proficiency import Proficiency
from ..types.skill import Skill
from .types.get_api_ability_scores_index_request_index import GetApiAbilityScoresIndexRequestIndex
from .types.get_api_alignments_index_request_index import GetApiAlignmentsIndexRequestIndex
from .types.get_api_backgrounds_index_request_index import GetApiBackgroundsIndexRequestIndex
from .types.get_api_languages_index_request_index import GetApiLanguagesIndexRequestIndex
from .types.get_api_skills_index_request_index import GetApiSkillsIndexRequestIndex


class RawCharacterDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_an_ability_score_by_index(
        self, index: GetApiAbilityScoresIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AbilityScore]:
        """
        # Ability Score

        Represents one of the six abilities that describes a creature's physical and mental characteristics. The three main rolls of the game - the ability check, the saving throw, and the attack roll - rely on the ability scores. [[SRD p76](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=76)]

        Parameters
        ----------
        index : GetApiAbilityScoresIndexRequestIndex
            The `index` of the ability score to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AbilityScore]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/ability-scores/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AbilityScore,
                    parse_obj_as(
                        type_=AbilityScore,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_an_alignment_by_index(
        self, index: GetApiAlignmentsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Alignment]:
        """
        # Alignment

        A typical creature in the game world has an alignment, which broadly describes its moral and personal attitudes. Alignment is a combination of two factors: one identifies morality (good, evil, or neutral), and the other describes attitudes toward society and order (lawful, chaotic, or neutral). Thus, nine distinct alignments define the possible combinations.[[SRD p58](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=58)]

        Parameters
        ----------
        index : GetApiAlignmentsIndexRequestIndex
            The `index` of the alignment to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Alignment]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/alignments/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Alignment,
                    parse_obj_as(
                        type_=Alignment,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_background_by_index(
        self, index: GetApiBackgroundsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Background]:
        """
        # Background

        Every story has a beginning. Your character's background reveals where you came from, how you became an adventurer, and your place in the world. Choosing a background provides you with important story cues about your character's identity. [[SRD p60](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=60)]

        _Note:_ acolyte is the only background included in the SRD.

        Parameters
        ----------
        index : GetApiBackgroundsIndexRequestIndex
            The `index` of the background to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Background]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/backgrounds/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Background,
                    parse_obj_as(
                        type_=Background,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_language_by_index(
        self, index: GetApiLanguagesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Language]:
        """
        # Language

        Your race indicates the languages your character can speak by default, and your background might give you access to one or more additional languages of your choice. [[SRD p59](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=59)]

        Parameters
        ----------
        index : GetApiLanguagesIndexRequestIndex
            The `index` of the language to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Language]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/languages/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Language,
                    parse_obj_as(
                        type_=Language,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_proficiency_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Proficiency]:
        """
        # Proficiency

        By virtue of race, class, and background a character is proficient at using certain skills, weapons, and equipment. Characters can also gain additional proficiencies at higher levels or by multiclassing. A characters starting proficiencies are determined during character creation.

        Parameters
        ----------
        index : str
            The `index` of the proficiency to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `proficiencies`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Proficiency]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/proficiencies/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Proficiency,
                    parse_obj_as(
                        type_=Proficiency,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_a_skill_by_index(
        self, index: GetApiSkillsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[Skill]:
        """
        # Skill

        Each ability covers a broad range of capabilities, including skills that a character or a monster can be proficient in. A skill represents a specific aspect of an ability score, and an individual's proficiency in a skill demonstrates a focus on that aspect. [[SRD p77](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=77)]

        Parameters
        ----------
        index : GetApiSkillsIndexRequestIndex
            The `index` of the skill to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Skill]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/skills/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Skill,
                    parse_obj_as(
                        type_=Skill,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawCharacterDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_an_ability_score_by_index(
        self, index: GetApiAbilityScoresIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AbilityScore]:
        """
        # Ability Score

        Represents one of the six abilities that describes a creature's physical and mental characteristics. The three main rolls of the game - the ability check, the saving throw, and the attack roll - rely on the ability scores. [[SRD p76](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=76)]

        Parameters
        ----------
        index : GetApiAbilityScoresIndexRequestIndex
            The `index` of the ability score to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AbilityScore]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/ability-scores/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AbilityScore,
                    parse_obj_as(
                        type_=AbilityScore,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_an_alignment_by_index(
        self, index: GetApiAlignmentsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Alignment]:
        """
        # Alignment

        A typical creature in the game world has an alignment, which broadly describes its moral and personal attitudes. Alignment is a combination of two factors: one identifies morality (good, evil, or neutral), and the other describes attitudes toward society and order (lawful, chaotic, or neutral). Thus, nine distinct alignments define the possible combinations.[[SRD p58](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=58)]

        Parameters
        ----------
        index : GetApiAlignmentsIndexRequestIndex
            The `index` of the alignment to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Alignment]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/alignments/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Alignment,
                    parse_obj_as(
                        type_=Alignment,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_background_by_index(
        self, index: GetApiBackgroundsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Background]:
        """
        # Background

        Every story has a beginning. Your character's background reveals where you came from, how you became an adventurer, and your place in the world. Choosing a background provides you with important story cues about your character's identity. [[SRD p60](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=60)]

        _Note:_ acolyte is the only background included in the SRD.

        Parameters
        ----------
        index : GetApiBackgroundsIndexRequestIndex
            The `index` of the background to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Background]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/backgrounds/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Background,
                    parse_obj_as(
                        type_=Background,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_language_by_index(
        self, index: GetApiLanguagesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Language]:
        """
        # Language

        Your race indicates the languages your character can speak by default, and your background might give you access to one or more additional languages of your choice. [[SRD p59](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=59)]

        Parameters
        ----------
        index : GetApiLanguagesIndexRequestIndex
            The `index` of the language to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Language]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/languages/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Language,
                    parse_obj_as(
                        type_=Language,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_proficiency_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Proficiency]:
        """
        # Proficiency

        By virtue of race, class, and background a character is proficient at using certain skills, weapons, and equipment. Characters can also gain additional proficiencies at higher levels or by multiclassing. A characters starting proficiencies are determined during character creation.

        Parameters
        ----------
        index : str
            The `index` of the proficiency to get.

            Available values can be found in the [`ResourceList`](#get-/api/-endpoint-) for `proficiencies`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Proficiency]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/proficiencies/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Proficiency,
                    parse_obj_as(
                        type_=Proficiency,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_a_skill_by_index(
        self, index: GetApiSkillsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Skill]:
        """
        # Skill

        Each ability covers a broad range of capabilities, including skills that a character or a monster can be proficient in. A skill represents a specific aspect of an ability score, and an individual's proficiency in a skill demonstrates a focus on that aspect. [[SRD p77](https://media.wizards.com/2016/downloads/DND/SRD-OGL_V5.1.pdf#page=77)]

        Parameters
        ----------
        index : GetApiSkillsIndexRequestIndex
            The `index` of the skill to get.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Skill]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/skills/{jsonable_encoder(index)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Skill,
                    parse_obj_as(
                        type_=Skill,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
