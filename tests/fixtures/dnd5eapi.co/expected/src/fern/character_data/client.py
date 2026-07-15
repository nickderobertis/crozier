

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ability_score import AbilityScore
from ..types.alignment import Alignment
from ..types.background import Background
from ..types.language import Language
from ..types.proficiency import Proficiency
from ..types.skill import Skill
from .raw_client import AsyncRawCharacterDataClient, RawCharacterDataClient
from .types.get_api_ability_scores_index_request_index import GetApiAbilityScoresIndexRequestIndex
from .types.get_api_alignments_index_request_index import GetApiAlignmentsIndexRequestIndex
from .types.get_api_backgrounds_index_request_index import GetApiBackgroundsIndexRequestIndex
from .types.get_api_languages_index_request_index import GetApiLanguagesIndexRequestIndex
from .types.get_api_skills_index_request_index import GetApiSkillsIndexRequestIndex


class CharacterDataClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCharacterDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCharacterDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCharacterDataClient
        """
        return self._raw_client

    def get_an_ability_score_by_index(
        self, index: GetApiAbilityScoresIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AbilityScore:
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
        AbilityScore
            OK

        Examples
        --------
        from fern.character_data import GetApiAbilityScoresIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.character_data.get_an_ability_score_by_index(
            index=GetApiAbilityScoresIndexRequestIndex.CHA,
        )
        """
        _response = self._raw_client.get_an_ability_score_by_index(index, request_options=request_options)
        return _response.data

    def get_an_alignment_by_index(
        self, index: GetApiAlignmentsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Alignment:
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
        Alignment
            OK

        Examples
        --------
        from fern.character_data import GetApiAlignmentsIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.character_data.get_an_alignment_by_index(
            index=GetApiAlignmentsIndexRequestIndex.CHAOTIC_NEUTRAL,
        )
        """
        _response = self._raw_client.get_an_alignment_by_index(index, request_options=request_options)
        return _response.data

    def get_a_background_by_index(
        self, index: GetApiBackgroundsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Background:
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
        Background
            OK

        Examples
        --------
        from fern.character_data import GetApiBackgroundsIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.character_data.get_a_background_by_index(
            index=GetApiBackgroundsIndexRequestIndex.ACOLYTE,
        )
        """
        _response = self._raw_client.get_a_background_by_index(index, request_options=request_options)
        return _response.data

    def get_a_language_by_index(
        self, index: GetApiLanguagesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Language:
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
        Language
            OK

        Examples
        --------
        from fern.character_data import GetApiLanguagesIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.character_data.get_a_language_by_index(
            index=GetApiLanguagesIndexRequestIndex.ABYSSAL,
        )
        """
        _response = self._raw_client.get_a_language_by_index(index, request_options=request_options)
        return _response.data

    def get_a_proficiency_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Proficiency:
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
        Proficiency
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.character_data.get_a_proficiency_by_index(
            index="medium-armor",
        )
        """
        _response = self._raw_client.get_a_proficiency_by_index(index, request_options=request_options)
        return _response.data

    def get_a_skill_by_index(
        self, index: GetApiSkillsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Skill:
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
        Skill
            OK

        Examples
        --------
        from fern.character_data import GetApiSkillsIndexRequestIndex

        from fern import FernApi

        client = FernApi()
        client.character_data.get_a_skill_by_index(
            index=GetApiSkillsIndexRequestIndex.ACROBATICS,
        )
        """
        _response = self._raw_client.get_a_skill_by_index(index, request_options=request_options)
        return _response.data


class AsyncCharacterDataClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCharacterDataClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCharacterDataClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCharacterDataClient
        """
        return self._raw_client

    async def get_an_ability_score_by_index(
        self, index: GetApiAbilityScoresIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AbilityScore:
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
        AbilityScore
            OK

        Examples
        --------
        import asyncio

        from fern.character_data import GetApiAbilityScoresIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.character_data.get_an_ability_score_by_index(
                index=GetApiAbilityScoresIndexRequestIndex.CHA,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_ability_score_by_index(index, request_options=request_options)
        return _response.data

    async def get_an_alignment_by_index(
        self, index: GetApiAlignmentsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Alignment:
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
        Alignment
            OK

        Examples
        --------
        import asyncio

        from fern.character_data import GetApiAlignmentsIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.character_data.get_an_alignment_by_index(
                index=GetApiAlignmentsIndexRequestIndex.CHAOTIC_NEUTRAL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_an_alignment_by_index(index, request_options=request_options)
        return _response.data

    async def get_a_background_by_index(
        self, index: GetApiBackgroundsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Background:
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
        Background
            OK

        Examples
        --------
        import asyncio

        from fern.character_data import GetApiBackgroundsIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.character_data.get_a_background_by_index(
                index=GetApiBackgroundsIndexRequestIndex.ACOLYTE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_background_by_index(index, request_options=request_options)
        return _response.data

    async def get_a_language_by_index(
        self, index: GetApiLanguagesIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Language:
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
        Language
            OK

        Examples
        --------
        import asyncio

        from fern.character_data import GetApiLanguagesIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.character_data.get_a_language_by_index(
                index=GetApiLanguagesIndexRequestIndex.ABYSSAL,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_language_by_index(index, request_options=request_options)
        return _response.data

    async def get_a_proficiency_by_index(
        self, index: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Proficiency:
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
        Proficiency
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.character_data.get_a_proficiency_by_index(
                index="medium-armor",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_proficiency_by_index(index, request_options=request_options)
        return _response.data

    async def get_a_skill_by_index(
        self, index: GetApiSkillsIndexRequestIndex, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Skill:
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
        Skill
            OK

        Examples
        --------
        import asyncio

        from fern.character_data import GetApiSkillsIndexRequestIndex

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.character_data.get_a_skill_by_index(
                index=GetApiSkillsIndexRequestIndex.ACROBATICS,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_a_skill_by_index(index, request_options=request_options)
        return _response.data
