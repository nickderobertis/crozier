

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.knot import Knot
from ..types.weave import Weave
from ..types.weave_finish_delivery import WeaveFinishDelivery
from ..types.weave_plan_finish import WeavePlanFinish
from ..types.weave_plan_pattern import WeavePlanPattern
from ..types.weave_plan_threads_item import WeavePlanThreadsItem
from .raw_client import AsyncRawWeavesClient, RawWeavesClient


OMIT = typing.cast(typing.Any, ...)


class WeavesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWeavesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWeavesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWeavesClient
        """
        return self._raw_client

    def get_weave(self, weave_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Weave:
        """
        Parameters
        ----------
        weave_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Weave
            The weave

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.weaves.get_weave(
            weave_id="weave_id",
        )
        """
        _response = self._raw_client.get_weave(weave_id, request_options=request_options)
        return _response.data

    def start_weave(
        self,
        *,
        pattern: WeavePlanPattern,
        threads: typing.Sequence[WeavePlanThreadsItem],
        knots: typing.Sequence[Knot],
        finish: WeavePlanFinish,
        shelf_id: str,
        label: str,
        delivery: WeaveFinishDelivery,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Weave:
        """
        Parameters
        ----------
        pattern : WeavePlanPattern
            The weave's pattern.

        threads : typing.Sequence[WeavePlanThreadsItem]
            The threads, in order.

        knots : typing.Sequence[Knot]
            The knots tied along the selvedge.

        finish : WeavePlanFinish
            How the cloth is finished.

        shelf_id : str
            The shelf the cloth goes to.

        label : str
            The cloth's label.

        delivery : WeaveFinishDelivery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Weave
            Started

        Examples
        --------
        from fern import (
            BeadRef_Glass,
            FernApi,
            Knot,
            WeaveFinishDelivery,
            WeavePlanPattern_Plain,
            WeavePlanThreadsItem_Warp,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.weaves.start_weave(
            shelf_id="shelfId",
            label="label",
            delivery=WeaveFinishDelivery(),
            pattern=WeavePlanPattern_Plain(),
            threads=[WeavePlanThreadsItem_Warp()],
            knots=[
                Knot(
                    bead=BeadRef_Glass(
                        glass_id="glassId",
                    ),
                )
            ],
            finish="MATTE",
        )
        """
        _response = self._raw_client.start_weave(
            pattern=pattern,
            threads=threads,
            knots=knots,
            finish=finish,
            shelf_id=shelf_id,
            label=label,
            delivery=delivery,
            request_options=request_options,
        )
        return _response.data

    def check_weave(
        self,
        *,
        pattern: WeavePlanPattern,
        threads: typing.Sequence[WeavePlanThreadsItem],
        knots: typing.Sequence[Knot],
        finish: WeavePlanFinish,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Weave:
        """
        Parameters
        ----------
        pattern : WeavePlanPattern
            The weave's pattern.

        threads : typing.Sequence[WeavePlanThreadsItem]
            The threads, in order.

        knots : typing.Sequence[Knot]
            The knots tied along the selvedge.

        finish : WeavePlanFinish
            How the cloth is finished.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Weave
            Checked

        Examples
        --------
        from fern import (
            BeadRef_Glass,
            FernApi,
            Knot,
            WeavePlanPattern_Plain,
            WeavePlanThreadsItem_Warp,
        )

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.weaves.check_weave(
            pattern=WeavePlanPattern_Plain(),
            threads=[WeavePlanThreadsItem_Warp()],
            knots=[
                Knot(
                    bead=BeadRef_Glass(
                        glass_id="glassId",
                    ),
                )
            ],
            finish="MATTE",
        )
        """
        _response = self._raw_client.check_weave(
            pattern=pattern, threads=threads, knots=knots, finish=finish, request_options=request_options
        )
        return _response.data

    def blend_weave(
        self,
        *,
        yarn: typing.Optional[str] = OMIT,
        gauge: typing.Optional[int] = OMIT,
        dye: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        yarn : typing.Optional[str]

        gauge : typing.Optional[int]
            The yarn's gauge.

        dye : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.weaves.blend_weave()
        """
        _response = self._raw_client.blend_weave(yarn=yarn, gauge=gauge, dye=dye, request_options=request_options)
        return _response.data


class AsyncWeavesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWeavesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWeavesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWeavesClient
        """
        return self._raw_client

    async def get_weave(self, weave_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Weave:
        """
        Parameters
        ----------
        weave_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Weave
            The weave

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.weaves.get_weave(
                weave_id="weave_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_weave(weave_id, request_options=request_options)
        return _response.data

    async def start_weave(
        self,
        *,
        pattern: WeavePlanPattern,
        threads: typing.Sequence[WeavePlanThreadsItem],
        knots: typing.Sequence[Knot],
        finish: WeavePlanFinish,
        shelf_id: str,
        label: str,
        delivery: WeaveFinishDelivery,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Weave:
        """
        Parameters
        ----------
        pattern : WeavePlanPattern
            The weave's pattern.

        threads : typing.Sequence[WeavePlanThreadsItem]
            The threads, in order.

        knots : typing.Sequence[Knot]
            The knots tied along the selvedge.

        finish : WeavePlanFinish
            How the cloth is finished.

        shelf_id : str
            The shelf the cloth goes to.

        label : str
            The cloth's label.

        delivery : WeaveFinishDelivery

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Weave
            Started

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            BeadRef_Glass,
            Knot,
            WeaveFinishDelivery,
            WeavePlanPattern_Plain,
            WeavePlanThreadsItem_Warp,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.weaves.start_weave(
                shelf_id="shelfId",
                label="label",
                delivery=WeaveFinishDelivery(),
                pattern=WeavePlanPattern_Plain(),
                threads=[WeavePlanThreadsItem_Warp()],
                knots=[
                    Knot(
                        bead=BeadRef_Glass(
                            glass_id="glassId",
                        ),
                    )
                ],
                finish="MATTE",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_weave(
            pattern=pattern,
            threads=threads,
            knots=knots,
            finish=finish,
            shelf_id=shelf_id,
            label=label,
            delivery=delivery,
            request_options=request_options,
        )
        return _response.data

    async def check_weave(
        self,
        *,
        pattern: WeavePlanPattern,
        threads: typing.Sequence[WeavePlanThreadsItem],
        knots: typing.Sequence[Knot],
        finish: WeavePlanFinish,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Weave:
        """
        Parameters
        ----------
        pattern : WeavePlanPattern
            The weave's pattern.

        threads : typing.Sequence[WeavePlanThreadsItem]
            The threads, in order.

        knots : typing.Sequence[Knot]
            The knots tied along the selvedge.

        finish : WeavePlanFinish
            How the cloth is finished.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Weave
            Checked

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            BeadRef_Glass,
            Knot,
            WeavePlanPattern_Plain,
            WeavePlanThreadsItem_Warp,
        )

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.weaves.check_weave(
                pattern=WeavePlanPattern_Plain(),
                threads=[WeavePlanThreadsItem_Warp()],
                knots=[
                    Knot(
                        bead=BeadRef_Glass(
                            glass_id="glassId",
                        ),
                    )
                ],
                finish="MATTE",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.check_weave(
            pattern=pattern, threads=threads, knots=knots, finish=finish, request_options=request_options
        )
        return _response.data

    async def blend_weave(
        self,
        *,
        yarn: typing.Optional[str] = OMIT,
        gauge: typing.Optional[int] = OMIT,
        dye: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        yarn : typing.Optional[str]

        gauge : typing.Optional[int]
            The yarn's gauge.

        dye : typing.Optional[str]

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.weaves.blend_weave()


        asyncio.run(main())
        """
        _response = await self._raw_client.blend_weave(yarn=yarn, gauge=gauge, dye=dye, request_options=request_options)
        return _response.data
