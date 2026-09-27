

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.skill import Skill
from .raw_client import AsyncRawSkillEnrichmentClient, RawSkillEnrichmentClient


class SkillEnrichmentClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSkillEnrichmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSkillEnrichmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSkillEnrichmentClient
        """
        return self._raw_client

    def skill_enrich(
        self,
        *,
        skill: str,
        titlecase: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Skill:
        """
        Parameters
        ----------
        skill : str
            skill that will be enriched.

        titlecase : typing.Optional[bool]
            Setting to `true` will titlecase any records returned.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Skill
            Skill enrich completed.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.skill_enrichment.skill_enrich(
            skill="skill",
        )
        """
        _response = self._raw_client.skill_enrich(
            skill=skill, titlecase=titlecase, pretty=pretty, request_options=request_options
        )
        return _response.data


class AsyncSkillEnrichmentClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSkillEnrichmentClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSkillEnrichmentClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSkillEnrichmentClient
        """
        return self._raw_client

    async def skill_enrich(
        self,
        *,
        skill: str,
        titlecase: typing.Optional[bool] = None,
        pretty: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Skill:
        """
        Parameters
        ----------
        skill : str
            skill that will be enriched.

        titlecase : typing.Optional[bool]
            Setting to `true` will titlecase any records returned.

        pretty : typing.Optional[bool]
            Whether the output should have human-readable indentation.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Skill
            Skill enrich completed.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.skill_enrichment.skill_enrich(
                skill="skill",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.skill_enrich(
            skill=skill, titlecase=titlecase, pretty=pretty, request_options=request_options
        )
        return _response.data
