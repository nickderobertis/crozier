

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.agco_power_services_models_ecu import AgcoPowerServicesModelsEcu
from ..types.agco_power_services_models_ecu_state import AgcoPowerServicesModelsEcuState
from ..types.agco_power_services_models_production_data import AgcoPowerServicesModelsProductionData
from ..types.agco_power_services_models_user_status import AgcoPowerServicesModelsUserStatus
from ..types.agco_power_services_models_user_status_state import AgcoPowerServicesModelsUserStatusState
from ..types.system_object import SystemObject
from .raw_client import AsyncRawAftermarketservicesClient, RawAftermarketservicesClient


OMIT = typing.cast(typing.Any, ...)


class AftermarketservicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAftermarketservicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAftermarketservicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAftermarketservicesClient
        """
        return self._raw_client

    def getcerts(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemObject:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemObject
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.aftermarketservices.getcerts()
        """
        _response = self._raw_client.getcerts(request_options=request_options)
        return _response.data

    def putecu(
        self,
        serial_number_: str,
        *,
        edt_instance_id: str,
        engine_serial_number: str,
        serial_number: str,
        state: AgcoPowerServicesModelsEcuState,
        activation_code: typing.Optional[str] = OMIT,
        damaged_description: typing.Optional[str] = OMIT,
        replaces_ecu_serial_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgcoPowerServicesModelsEcu:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number_ : str
            The serial number of the ECU.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        engine_serial_number : str
            The serial number of the ECU’s engine

        serial_number : str
            The serial number of the ECU

        state : AgcoPowerServicesModelsEcuState
            The state of the ECU

        activation_code : typing.Optional[str]
            The code used to activate the ECU. May not be modified. Returned only on activation.

        damaged_description : typing.Optional[str]
            A description why the ECU cannot be deactivated.

        replaces_ecu_serial_number : typing.Optional[str]
            The serial number of the ECU that this ECU replaces. Required if activating an ECU..

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgcoPowerServicesModelsEcu
            OK

        Examples
        --------
        from fern import AgcoPowerServicesModelsEcuState, FernApi

        client = FernApi()
        client.aftermarketservices.putecu(
            serial_number_="serialNumber",
            edt_instance_id="EDTInstanceId",
            engine_serial_number="EngineSerialNumber",
            serial_number="SerialNumber",
            state=AgcoPowerServicesModelsEcuState.ACTIVE,
        )
        """
        _response = self._raw_client.putecu(
            serial_number_,
            edt_instance_id=edt_instance_id,
            engine_serial_number=engine_serial_number,
            serial_number=serial_number,
            state=state,
            activation_code=activation_code,
            damaged_description=damaged_description,
            replaces_ecu_serial_number=replaces_ecu_serial_number,
            request_options=request_options,
        )
        return _response.data

    def getengineiqacodes(
        self, serial_number: str, *, edt_instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the engine.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.aftermarketservices.getengineiqacodes(
            serial_number="serialNumber",
            edt_instance_id="EDTInstanceId",
        )
        """
        _response = self._raw_client.getengineiqacodes(
            serial_number, edt_instance_id=edt_instance_id, request_options=request_options
        )
        return _response.data

    def putiqacodes(
        self,
        serial_number: str,
        *,
        edt_instance_id: str,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the Engine

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.aftermarketservices.putiqacodes(
            serial_number="serialNumber",
            edt_instance_id="EDTInstanceId",
            request=["string"],
        )
        """
        _response = self._raw_client.putiqacodes(
            serial_number, edt_instance_id=edt_instance_id, request=request, request_options=request_options
        )
        return _response.data

    def getproductiondata(
        self, serial_number: str, *, edt_instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgcoPowerServicesModelsProductionData]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the engine.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgcoPowerServicesModelsProductionData]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.aftermarketservices.getproductiondata(
            serial_number="serialNumber",
            edt_instance_id="EDTInstanceId",
        )
        """
        _response = self._raw_client.getproductiondata(
            serial_number, edt_instance_id=edt_instance_id, request_options=request_options
        )
        return _response.data

    def getconnectionstatus(self, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.aftermarketservices.getconnectionstatus()
        """
        _response = self._raw_client.getconnectionstatus(request_options=request_options)
        return _response.data

    def getuserstatus(
        self, *, voucher_code: str, dealer_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AgcoPowerServicesModelsUserStatus:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str

        dealer_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgcoPowerServicesModelsUserStatus
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.aftermarketservices.getuserstatus(
            voucher_code="voucherCode",
            dealer_code="dealerCode",
        )
        """
        _response = self._raw_client.getuserstatus(
            voucher_code=voucher_code, dealer_code=dealer_code, request_options=request_options
        )
        return _response.data

    def updateuserstatus(
        self,
        *,
        dealer_code: str,
        voucher_code: str,
        state: typing.Optional[AgcoPowerServicesModelsUserStatusState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The dealer code of the voucher

        voucher_code : str
            The voucher code

        state : typing.Optional[AgcoPowerServicesModelsUserStatusState]
            The state of the voucher

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.aftermarketservices.updateuserstatus(
            dealer_code="DealerCode",
            voucher_code="VoucherCode",
        )
        """
        _response = self._raw_client.updateuserstatus(
            dealer_code=dealer_code, voucher_code=voucher_code, state=state, request_options=request_options
        )
        return _response.data


class AsyncAftermarketservicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAftermarketservicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAftermarketservicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAftermarketservicesClient
        """
        return self._raw_client

    async def getcerts(self, *, request_options: typing.Optional[RequestOptions] = None) -> SystemObject:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SystemObject
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.aftermarketservices.getcerts()


        asyncio.run(main())
        """
        _response = await self._raw_client.getcerts(request_options=request_options)
        return _response.data

    async def putecu(
        self,
        serial_number_: str,
        *,
        edt_instance_id: str,
        engine_serial_number: str,
        serial_number: str,
        state: AgcoPowerServicesModelsEcuState,
        activation_code: typing.Optional[str] = OMIT,
        damaged_description: typing.Optional[str] = OMIT,
        replaces_ecu_serial_number: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AgcoPowerServicesModelsEcu:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number_ : str
            The serial number of the ECU.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        engine_serial_number : str
            The serial number of the ECU’s engine

        serial_number : str
            The serial number of the ECU

        state : AgcoPowerServicesModelsEcuState
            The state of the ECU

        activation_code : typing.Optional[str]
            The code used to activate the ECU. May not be modified. Returned only on activation.

        damaged_description : typing.Optional[str]
            A description why the ECU cannot be deactivated.

        replaces_ecu_serial_number : typing.Optional[str]
            The serial number of the ECU that this ECU replaces. Required if activating an ECU..

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgcoPowerServicesModelsEcu
            OK

        Examples
        --------
        import asyncio

        from fern import AgcoPowerServicesModelsEcuState, AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.aftermarketservices.putecu(
                serial_number_="serialNumber",
                edt_instance_id="EDTInstanceId",
                engine_serial_number="EngineSerialNumber",
                serial_number="SerialNumber",
                state=AgcoPowerServicesModelsEcuState.ACTIVE,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putecu(
            serial_number_,
            edt_instance_id=edt_instance_id,
            engine_serial_number=engine_serial_number,
            serial_number=serial_number,
            state=state,
            activation_code=activation_code,
            damaged_description=damaged_description,
            replaces_ecu_serial_number=replaces_ecu_serial_number,
            request_options=request_options,
        )
        return _response.data

    async def getengineiqacodes(
        self, serial_number: str, *, edt_instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the engine.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.aftermarketservices.getengineiqacodes(
                serial_number="serialNumber",
                edt_instance_id="EDTInstanceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getengineiqacodes(
            serial_number, edt_instance_id=edt_instance_id, request_options=request_options
        )
        return _response.data

    async def putiqacodes(
        self,
        serial_number: str,
        *,
        edt_instance_id: str,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the Engine

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.aftermarketservices.putiqacodes(
                serial_number="serialNumber",
                edt_instance_id="EDTInstanceId",
                request=["string"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.putiqacodes(
            serial_number, edt_instance_id=edt_instance_id, request=request, request_options=request_options
        )
        return _response.data

    async def getproductiondata(
        self, serial_number: str, *, edt_instance_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AgcoPowerServicesModelsProductionData]:
        """
        No Documentation Found.

        Parameters
        ----------
        serial_number : str
            The serial number of the engine.

        edt_instance_id : str
            The EDT Instance Id of the kit calling this method.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AgcoPowerServicesModelsProductionData]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.aftermarketservices.getproductiondata(
                serial_number="serialNumber",
                edt_instance_id="EDTInstanceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getproductiondata(
            serial_number, edt_instance_id=edt_instance_id, request_options=request_options
        )
        return _response.data

    async def getconnectionstatus(self, *, request_options: typing.Optional[RequestOptions] = None) -> bool:
        """
        No Documentation Found.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.aftermarketservices.getconnectionstatus()


        asyncio.run(main())
        """
        _response = await self._raw_client.getconnectionstatus(request_options=request_options)
        return _response.data

    async def getuserstatus(
        self, *, voucher_code: str, dealer_code: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AgcoPowerServicesModelsUserStatus:
        """
        No Documentation Found.

        Parameters
        ----------
        voucher_code : str

        dealer_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AgcoPowerServicesModelsUserStatus
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.aftermarketservices.getuserstatus(
                voucher_code="voucherCode",
                dealer_code="dealerCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getuserstatus(
            voucher_code=voucher_code, dealer_code=dealer_code, request_options=request_options
        )
        return _response.data

    async def updateuserstatus(
        self,
        *,
        dealer_code: str,
        voucher_code: str,
        state: typing.Optional[AgcoPowerServicesModelsUserStatusState] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> bool:
        """
        No Documentation Found.

        Parameters
        ----------
        dealer_code : str
            The dealer code of the voucher

        voucher_code : str
            The voucher code

        state : typing.Optional[AgcoPowerServicesModelsUserStatusState]
            The state of the voucher

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.aftermarketservices.updateuserstatus(
                dealer_code="DealerCode",
                voucher_code="VoucherCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updateuserstatus(
            dealer_code=dealer_code, voucher_code=voucher_code, state=state, request_options=request_options
        )
        return _response.data
