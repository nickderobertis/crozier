

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.skill_card_response import SkillCardResponse
from .raw_client import AsyncRawSkillsClient, RawSkillsClient


class SkillsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSkillsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSkillsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSkillsClient
        """
        return self._raw_client

    def list_skills(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SkillCardResponse]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Optional ranking query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SkillCardResponse]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.skills.list_skills()
        """
        _response = self._raw_client.list_skills(q=q, request_options=request_options)
        return _response.data

    def get_skill(self, skill_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> SkillCardResponse:
        """
        Parameters
        ----------
        skill_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SkillCardResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.skills.get_skill(
            skill_id="skill_id",
        )
        """
        _response = self._raw_client.get_skill(skill_id, request_options=request_options)
        return _response.data


class AsyncSkillsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSkillsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSkillsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSkillsClient
        """
        return self._raw_client

    async def list_skills(
        self, *, q: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SkillCardResponse]:
        """
        Parameters
        ----------
        q : typing.Optional[str]
            Optional ranking query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SkillCardResponse]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.skills.list_skills()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_skills(q=q, request_options=request_options)
        return _response.data

    async def get_skill(
        self, skill_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SkillCardResponse:
        """
        Parameters
        ----------
        skill_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SkillCardResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.skills.get_skill(
                skill_id="skill_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_skill(skill_id, request_options=request_options)
        return _response.data
