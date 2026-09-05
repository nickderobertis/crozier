

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_list_pricing_plan_to_service_admin_get import EnvelopeListPricingPlanToServiceAdminGet
from ..types.envelope_pricing_plan_admin_get import EnvelopePricingPlanAdminGet
from ..types.envelope_pricing_plan_to_service_admin_get import EnvelopePricingPlanToServiceAdminGet
from ..types.envelope_pricing_unit_admin_get import EnvelopePricingUnitAdminGet
from ..types.page_pricing_plan_admin_get import PagePricingPlanAdminGet
from ..types.pricing_plan_classification import PricingPlanClassification
from ..types.pricing_unit_cost_update import PricingUnitCostUpdate
from ..types.specific_info import SpecificInfo
from .raw_client import AsyncRawAdminClient, RawAdminClient
from .types.create_pricing_unit_body_params_cost_per_unit import CreatePricingUnitBodyParamsCostPerUnit
from .types.create_pricing_unit_body_params_unit_extra_info import CreatePricingUnitBodyParamsUnitExtraInfo
from .types.update_pricing_unit_body_params_unit_extra_info import UpdatePricingUnitBodyParamsUnitExtraInfo


OMIT = typing.cast(typing.Any, ...)


class AdminClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAdminClient
        """
        return self._raw_client

    def list_pricing_plans_for_admin_user(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePricingPlanAdminGet:
        """
        To keep the listing lightweight, the pricingUnits field is None.

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagePricingPlanAdminGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.list_pricing_plans_for_admin_user()
        """
        _response = self._raw_client.list_pricing_plans_for_admin_user(
            limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    def create_pricing_plan(
        self,
        *,
        display_name: str,
        description: str,
        classification: PricingPlanClassification,
        pricing_plan_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingPlanAdminGet:
        """
        Parameters
        ----------
        display_name : str

        description : str

        classification : PricingPlanClassification

        pricing_plan_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanAdminGet
            Successful Response

        Examples
        --------
        from fern import FernApi, PricingPlanClassification

        client = FernApi()
        client.admin.create_pricing_plan(
            display_name="displayName",
            description="description",
            classification=PricingPlanClassification.TIER,
            pricing_plan_key="pricingPlanKey",
        )
        """
        _response = self._raw_client.create_pricing_plan(
            display_name=display_name,
            description=description,
            classification=classification,
            pricing_plan_key=pricing_plan_key,
            request_options=request_options,
        )
        return _response.data

    def get_pricing_plan_for_admin_user(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePricingPlanAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanAdminGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.get_pricing_plan_for_admin_user(
            pricing_plan_id=1,
        )
        """
        _response = self._raw_client.get_pricing_plan_for_admin_user(pricing_plan_id, request_options=request_options)
        return _response.data

    def update_pricing_plan(
        self,
        pricing_plan_id: int,
        *,
        display_name: str,
        description: str,
        is_active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingPlanAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        display_name : str

        description : str

        is_active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanAdminGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.update_pricing_plan(
            pricing_plan_id=1,
            display_name="displayName",
            description="description",
            is_active=True,
        )
        """
        _response = self._raw_client.update_pricing_plan(
            pricing_plan_id,
            display_name=display_name,
            description=description,
            is_active=is_active,
            request_options=request_options,
        )
        return _response.data

    def get_pricing_unit(
        self, pricing_plan_id: int, pricing_unit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePricingUnitAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingUnitAdminGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.get_pricing_unit(
            pricing_plan_id=1,
            pricing_unit_id=1,
        )
        """
        _response = self._raw_client.get_pricing_unit(pricing_plan_id, pricing_unit_id, request_options=request_options)
        return _response.data

    def update_pricing_unit(
        self,
        pricing_plan_id: int,
        pricing_unit_id: int,
        *,
        unit_name: str,
        unit_extra_info: UpdatePricingUnitBodyParamsUnitExtraInfo,
        default: bool,
        specific_info: SpecificInfo,
        pricing_unit_cost_update: typing.Optional[PricingUnitCostUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingUnitAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        unit_name : str

        unit_extra_info : UpdatePricingUnitBodyParamsUnitExtraInfo

        default : bool

        specific_info : SpecificInfo

        pricing_unit_cost_update : typing.Optional[PricingUnitCostUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingUnitAdminGet
            Successful Response

        Examples
        --------
        from fern import FernApi, SpecificInfo, UnitExtraInfoTierInput

        client = FernApi()
        client.admin.update_pricing_unit(
            pricing_plan_id=1,
            pricing_unit_id=1,
            unit_name="unitName",
            unit_extra_info=UnitExtraInfoTierInput(
                cpu=1,
                ram="RAM",
                vram="VRAM",
            ),
            default=True,
            specific_info=SpecificInfo(
                aws_ec2instances=["aws_ec2_instances"],
            ),
        )
        """
        _response = self._raw_client.update_pricing_unit(
            pricing_plan_id,
            pricing_unit_id,
            unit_name=unit_name,
            unit_extra_info=unit_extra_info,
            default=default,
            specific_info=specific_info,
            pricing_unit_cost_update=pricing_unit_cost_update,
            request_options=request_options,
        )
        return _response.data

    def create_pricing_unit(
        self,
        pricing_plan_id: int,
        *,
        unit_name: str,
        unit_extra_info: CreatePricingUnitBodyParamsUnitExtraInfo,
        default: bool,
        specific_info: SpecificInfo,
        cost_per_unit: CreatePricingUnitBodyParamsCostPerUnit,
        comment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingUnitAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        unit_name : str

        unit_extra_info : CreatePricingUnitBodyParamsUnitExtraInfo

        default : bool

        specific_info : SpecificInfo

        cost_per_unit : CreatePricingUnitBodyParamsCostPerUnit

        comment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingUnitAdminGet
            Successful Response

        Examples
        --------
        from fern import FernApi, SpecificInfo, UnitExtraInfoTierInput

        client = FernApi()
        client.admin.create_pricing_unit(
            pricing_plan_id=1,
            unit_name="unitName",
            unit_extra_info=UnitExtraInfoTierInput(
                cpu=1,
                ram="RAM",
                vram="VRAM",
            ),
            default=True,
            specific_info=SpecificInfo(
                aws_ec2instances=["aws_ec2_instances"],
            ),
            cost_per_unit=1.1,
            comment="comment",
        )
        """
        _response = self._raw_client.create_pricing_unit(
            pricing_plan_id,
            unit_name=unit_name,
            unit_extra_info=unit_extra_info,
            default=default,
            specific_info=specific_info,
            cost_per_unit=cost_per_unit,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    def list_connected_services_to_pricing_plan(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListPricingPlanToServiceAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListPricingPlanToServiceAdminGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.list_connected_services_to_pricing_plan(
            pricing_plan_id=1,
        )
        """
        _response = self._raw_client.list_connected_services_to_pricing_plan(
            pricing_plan_id, request_options=request_options
        )
        return _response.data

    def connect_service_to_pricing_plan(
        self,
        pricing_plan_id: int,
        *,
        service_key: str,
        service_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingPlanToServiceAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanToServiceAdminGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.admin.connect_service_to_pricing_plan(
            pricing_plan_id=1,
            service_key="serviceKey",
            service_version="serviceVersion",
        )
        """
        _response = self._raw_client.connect_service_to_pricing_plan(
            pricing_plan_id, service_key=service_key, service_version=service_version, request_options=request_options
        )
        return _response.data


class AsyncAdminClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAdminClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAdminClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAdminClient
        """
        return self._raw_client

    async def list_pricing_plans_for_admin_user(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PagePricingPlanAdminGet:
        """
        To keep the listing lightweight, the pricingUnits field is None.

        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PagePricingPlanAdminGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.list_pricing_plans_for_admin_user()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_pricing_plans_for_admin_user(
            limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def create_pricing_plan(
        self,
        *,
        display_name: str,
        description: str,
        classification: PricingPlanClassification,
        pricing_plan_key: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingPlanAdminGet:
        """
        Parameters
        ----------
        display_name : str

        description : str

        classification : PricingPlanClassification

        pricing_plan_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanAdminGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, PricingPlanClassification

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.create_pricing_plan(
                display_name="displayName",
                description="description",
                classification=PricingPlanClassification.TIER,
                pricing_plan_key="pricingPlanKey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_pricing_plan(
            display_name=display_name,
            description=description,
            classification=classification,
            pricing_plan_key=pricing_plan_key,
            request_options=request_options,
        )
        return _response.data

    async def get_pricing_plan_for_admin_user(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePricingPlanAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanAdminGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.get_pricing_plan_for_admin_user(
                pricing_plan_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricing_plan_for_admin_user(
            pricing_plan_id, request_options=request_options
        )
        return _response.data

    async def update_pricing_plan(
        self,
        pricing_plan_id: int,
        *,
        display_name: str,
        description: str,
        is_active: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingPlanAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        display_name : str

        description : str

        is_active : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanAdminGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.update_pricing_plan(
                pricing_plan_id=1,
                display_name="displayName",
                description="description",
                is_active=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_pricing_plan(
            pricing_plan_id,
            display_name=display_name,
            description=description,
            is_active=is_active,
            request_options=request_options,
        )
        return _response.data

    async def get_pricing_unit(
        self, pricing_plan_id: int, pricing_unit_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopePricingUnitAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingUnitAdminGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.get_pricing_unit(
                pricing_plan_id=1,
                pricing_unit_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_pricing_unit(
            pricing_plan_id, pricing_unit_id, request_options=request_options
        )
        return _response.data

    async def update_pricing_unit(
        self,
        pricing_plan_id: int,
        pricing_unit_id: int,
        *,
        unit_name: str,
        unit_extra_info: UpdatePricingUnitBodyParamsUnitExtraInfo,
        default: bool,
        specific_info: SpecificInfo,
        pricing_unit_cost_update: typing.Optional[PricingUnitCostUpdate] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingUnitAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        pricing_unit_id : int

        unit_name : str

        unit_extra_info : UpdatePricingUnitBodyParamsUnitExtraInfo

        default : bool

        specific_info : SpecificInfo

        pricing_unit_cost_update : typing.Optional[PricingUnitCostUpdate]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingUnitAdminGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SpecificInfo, UnitExtraInfoTierInput

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.update_pricing_unit(
                pricing_plan_id=1,
                pricing_unit_id=1,
                unit_name="unitName",
                unit_extra_info=UnitExtraInfoTierInput(
                    cpu=1,
                    ram="RAM",
                    vram="VRAM",
                ),
                default=True,
                specific_info=SpecificInfo(
                    aws_ec2instances=["aws_ec2_instances"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_pricing_unit(
            pricing_plan_id,
            pricing_unit_id,
            unit_name=unit_name,
            unit_extra_info=unit_extra_info,
            default=default,
            specific_info=specific_info,
            pricing_unit_cost_update=pricing_unit_cost_update,
            request_options=request_options,
        )
        return _response.data

    async def create_pricing_unit(
        self,
        pricing_plan_id: int,
        *,
        unit_name: str,
        unit_extra_info: CreatePricingUnitBodyParamsUnitExtraInfo,
        default: bool,
        specific_info: SpecificInfo,
        cost_per_unit: CreatePricingUnitBodyParamsCostPerUnit,
        comment: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingUnitAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        unit_name : str

        unit_extra_info : CreatePricingUnitBodyParamsUnitExtraInfo

        default : bool

        specific_info : SpecificInfo

        cost_per_unit : CreatePricingUnitBodyParamsCostPerUnit

        comment : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingUnitAdminGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, SpecificInfo, UnitExtraInfoTierInput

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.create_pricing_unit(
                pricing_plan_id=1,
                unit_name="unitName",
                unit_extra_info=UnitExtraInfoTierInput(
                    cpu=1,
                    ram="RAM",
                    vram="VRAM",
                ),
                default=True,
                specific_info=SpecificInfo(
                    aws_ec2instances=["aws_ec2_instances"],
                ),
                cost_per_unit=1.1,
                comment="comment",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_pricing_unit(
            pricing_plan_id,
            unit_name=unit_name,
            unit_extra_info=unit_extra_info,
            default=default,
            specific_info=specific_info,
            cost_per_unit=cost_per_unit,
            comment=comment,
            request_options=request_options,
        )
        return _response.data

    async def list_connected_services_to_pricing_plan(
        self, pricing_plan_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListPricingPlanToServiceAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListPricingPlanToServiceAdminGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.list_connected_services_to_pricing_plan(
                pricing_plan_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_connected_services_to_pricing_plan(
            pricing_plan_id, request_options=request_options
        )
        return _response.data

    async def connect_service_to_pricing_plan(
        self,
        pricing_plan_id: int,
        *,
        service_key: str,
        service_version: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopePricingPlanToServiceAdminGet:
        """
        Parameters
        ----------
        pricing_plan_id : int

        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopePricingPlanToServiceAdminGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.admin.connect_service_to_pricing_plan(
                pricing_plan_id=1,
                service_key="serviceKey",
                service_version="serviceVersion",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.connect_service_to_pricing_plan(
            pricing_plan_id, service_key=service_key, service_version=service_version, request_options=request_options
        )
        return _response.data
