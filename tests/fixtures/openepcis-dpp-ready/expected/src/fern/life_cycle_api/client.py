

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_dpp_result import CreateDppResult
from ..types.digital_product_passport import DigitalProductPassport
from ..types.dpp_id_page import DppIdPage
from ..types.identifier import Identifier
from ..types.timestamp import Timestamp
from .raw_client import AsyncRawLifeCycleApiClient, RawLifeCycleApiClient
from .types.create_dpp_request_representation import CreateDppRequestRepresentation
from .types.read_dpp_by_id_request_representation import ReadDppByIdRequestRepresentation
from .types.read_dpp_by_product_id_request_representation import ReadDppByProductIdRequestRepresentation
from .types.read_dpp_version_by_id_and_date_request_representation import ReadDppVersionByIdAndDateRequestRepresentation
from .types.update_dpp_by_id_request_representation import UpdateDppByIdRequestRepresentation


OMIT = typing.cast(typing.Any, ...)


class LifeCycleApiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLifeCycleApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLifeCycleApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLifeCycleApiClient
        """
        return self._raw_client

    def read_dpp_by_id(
        self,
        dpp_id: Identifier,
        *,
        representation: typing.Optional[ReadDppByIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DigitalProductPassport:
        """
        Returns the DPP with the specified DPP ID. Conformance: shall.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        representation : typing.Optional[ReadDppByIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DigitalProductPassport
            The requested DPP.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.life_cycle_api.read_dpp_by_id(
            dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
        )
        """
        _response = self._raw_client.read_dpp_by_id(
            dpp_id, representation=representation, request_options=request_options
        )
        return _response.data

    def delete_dpp_by_id(self, dpp_id: Identifier, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Removes the DPP with the specified DPP ID (end of life). Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.life_cycle_api.delete_dpp_by_id(
            dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
        )
        """
        _response = self._raw_client.delete_dpp_by_id(dpp_id, request_options=request_options)
        return _response.data

    def update_dpp_by_id(
        self,
        dpp_id: Identifier,
        *,
        request: DigitalProductPassport,
        representation: typing.Optional[UpdateDppByIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DigitalProductPassport:
        """
        Partial update of a DPP. The body carries only the parts to update or extend
        (RFC 7396 JSON Merge Patch may be used). If any part fails, the whole update
        fails and no change is adopted. All changes are archived per EN 18221.
        Conformance: shall where authorized third parties hold write access.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        request : DigitalProductPassport

        representation : typing.Optional[UpdateDppByIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DigitalProductPassport
            The updated DPP.

        Examples
        --------
        import datetime

        from fern import DigitalProductPassportCompressed, FernApi, Granularity

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.life_cycle_api.update_dpp_by_id(
            dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
            request=DigitalProductPassportCompressed(
                digital_product_passport_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                unique_product_identifier="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                granularity=Granularity.MODEL,
                dpp_schema_version="EN 18223:2026",
                dpp_status="active",
                last_updated=datetime.datetime.fromisoformat(
                    "2026-06-08 15:30:00+00:00",
                ),
                economic_operator_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
            ),
        )
        """
        _response = self._raw_client.update_dpp_by_id(
            dpp_id, request=request, representation=representation, request_options=request_options
        )
        return _response.data

    def read_dpp_by_product_id(
        self,
        product_id: Identifier,
        *,
        representation: typing.Optional[ReadDppByProductIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DigitalProductPassport:
        """
        Returns the current active DPP (latest version) for the unique product identifier (EN 18219 GS1 Digital Link). Conformance: shall.

        Parameters
        ----------
        product_id : Identifier
            Unique product identifier (EN 18219 GS1 Digital Link), percent-encoded.

        representation : typing.Optional[ReadDppByProductIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DigitalProductPassport
            The latest active DPP for the product.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.life_cycle_api.read_dpp_by_product_id(
            product_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
        )
        """
        _response = self._raw_client.read_dpp_by_product_id(
            product_id, representation=representation, request_options=request_options
        )
        return _response.data

    def read_dpp_version_by_id_and_date(
        self,
        dpp_id: Identifier,
        *,
        date: Timestamp,
        representation: typing.Optional[ReadDppVersionByIdAndDateRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DigitalProductPassport:
        """
        Returns the DPP version current at the given date (archived versions per EN 18221). Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        date : Timestamp
            UTC-based timestamp (ISO 8601-1) for which the version is requested.

        representation : typing.Optional[ReadDppVersionByIdAndDateRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DigitalProductPassport
            The DPP version at the given date.

        Examples
        --------
        import datetime

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.life_cycle_api.read_dpp_version_by_id_and_date(
            dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
            date=datetime.datetime.fromisoformat(
                "2026-06-08 15:30:00+00:00",
            ),
        )
        """
        _response = self._raw_client.read_dpp_version_by_id_and_date(
            dpp_id, date=date, representation=representation, request_options=request_options
        )
        return _response.data

    def read_dpp_ids_by_product_ids(
        self,
        *,
        product_ids: typing.Sequence[Identifier],
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DppIdPage:
        """
        Returns the DPP identifiers matching a set of product identifiers (discovery). Paginated by `limit` and `cursor` (the cursor shall not be empty). Conformance: shall.

        Parameters
        ----------
        product_ids : typing.Sequence[Identifier]

        limit : typing.Optional[int]
            Maximum number of identifiers to return in this page.

        cursor : typing.Optional[str]
            Opaque, non-empty pagination token from a prior response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DppIdPage
            The matching DPP identifiers, with an optional next-page cursor.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.life_cycle_api.read_dpp_ids_by_product_ids(
            product_ids=["https://id.gs1.org/01/09521002005004/21/BAT2024-001"],
        )
        """
        _response = self._raw_client.read_dpp_ids_by_product_ids(
            product_ids=product_ids, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    def create_dpp(
        self,
        *,
        request: DigitalProductPassport,
        representation: typing.Optional[CreateDppRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDppResult:
        """
        Creates a new DPP and returns its DPP ID. Conformance: should.

        Parameters
        ----------
        request : DigitalProductPassport

        representation : typing.Optional[CreateDppRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDppResult
            DPP created.

        Examples
        --------
        import datetime

        from fern import DigitalProductPassportCompressed, FernApi, Granularity

        client = FernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )
        client.life_cycle_api.create_dpp(
            request=DigitalProductPassportCompressed(
                digital_product_passport_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                unique_product_identifier="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                granularity=Granularity.MODEL,
                dpp_schema_version="EN 18223:2026",
                dpp_status="active",
                last_updated=datetime.datetime.fromisoformat(
                    "2026-06-08 15:30:00+00:00",
                ),
                economic_operator_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
            ),
        )
        """
        _response = self._raw_client.create_dpp(
            request=request, representation=representation, request_options=request_options
        )
        return _response.data


class AsyncLifeCycleApiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLifeCycleApiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLifeCycleApiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLifeCycleApiClient
        """
        return self._raw_client

    async def read_dpp_by_id(
        self,
        dpp_id: Identifier,
        *,
        representation: typing.Optional[ReadDppByIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DigitalProductPassport:
        """
        Returns the DPP with the specified DPP ID. Conformance: shall.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        representation : typing.Optional[ReadDppByIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DigitalProductPassport
            The requested DPP.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.life_cycle_api.read_dpp_by_id(
                dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_dpp_by_id(
            dpp_id, representation=representation, request_options=request_options
        )
        return _response.data

    async def delete_dpp_by_id(
        self, dpp_id: Identifier, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes the DPP with the specified DPP ID (end of life). Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

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
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.life_cycle_api.delete_dpp_by_id(
                dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_dpp_by_id(dpp_id, request_options=request_options)
        return _response.data

    async def update_dpp_by_id(
        self,
        dpp_id: Identifier,
        *,
        request: DigitalProductPassport,
        representation: typing.Optional[UpdateDppByIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DigitalProductPassport:
        """
        Partial update of a DPP. The body carries only the parts to update or extend
        (RFC 7396 JSON Merge Patch may be used). If any part fails, the whole update
        fails and no change is adopted. All changes are archived per EN 18221.
        Conformance: shall where authorized third parties hold write access.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        request : DigitalProductPassport

        representation : typing.Optional[UpdateDppByIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DigitalProductPassport
            The updated DPP.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, DigitalProductPassportCompressed, Granularity

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.life_cycle_api.update_dpp_by_id(
                dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                request=DigitalProductPassportCompressed(
                    digital_product_passport_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                    unique_product_identifier="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                    granularity=Granularity.MODEL,
                    dpp_schema_version="EN 18223:2026",
                    dpp_status="active",
                    last_updated=datetime.datetime.fromisoformat(
                        "2026-06-08 15:30:00+00:00",
                    ),
                    economic_operator_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_dpp_by_id(
            dpp_id, request=request, representation=representation, request_options=request_options
        )
        return _response.data

    async def read_dpp_by_product_id(
        self,
        product_id: Identifier,
        *,
        representation: typing.Optional[ReadDppByProductIdRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DigitalProductPassport:
        """
        Returns the current active DPP (latest version) for the unique product identifier (EN 18219 GS1 Digital Link). Conformance: shall.

        Parameters
        ----------
        product_id : Identifier
            Unique product identifier (EN 18219 GS1 Digital Link), percent-encoded.

        representation : typing.Optional[ReadDppByProductIdRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DigitalProductPassport
            The latest active DPP for the product.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.life_cycle_api.read_dpp_by_product_id(
                product_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_dpp_by_product_id(
            product_id, representation=representation, request_options=request_options
        )
        return _response.data

    async def read_dpp_version_by_id_and_date(
        self,
        dpp_id: Identifier,
        *,
        date: Timestamp,
        representation: typing.Optional[ReadDppVersionByIdAndDateRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DigitalProductPassport:
        """
        Returns the DPP version current at the given date (archived versions per EN 18221). Conformance: should.

        Parameters
        ----------
        dpp_id : Identifier
            The DPP's unique identifier (EN 18223), percent-encoded in the path.

        date : Timestamp
            UTC-based timestamp (ISO 8601-1) for which the version is requested.

        representation : typing.Optional[ReadDppVersionByIdAndDateRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DigitalProductPassport
            The DPP version at the given date.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.life_cycle_api.read_dpp_version_by_id_and_date(
                dpp_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                date=datetime.datetime.fromisoformat(
                    "2026-06-08 15:30:00+00:00",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_dpp_version_by_id_and_date(
            dpp_id, date=date, representation=representation, request_options=request_options
        )
        return _response.data

    async def read_dpp_ids_by_product_ids(
        self,
        *,
        product_ids: typing.Sequence[Identifier],
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> DppIdPage:
        """
        Returns the DPP identifiers matching a set of product identifiers (discovery). Paginated by `limit` and `cursor` (the cursor shall not be empty). Conformance: shall.

        Parameters
        ----------
        product_ids : typing.Sequence[Identifier]

        limit : typing.Optional[int]
            Maximum number of identifiers to return in this page.

        cursor : typing.Optional[str]
            Opaque, non-empty pagination token from a prior response.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DppIdPage
            The matching DPP identifiers, with an optional next-page cursor.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.life_cycle_api.read_dpp_ids_by_product_ids(
                product_ids=["https://id.gs1.org/01/09521002005004/21/BAT2024-001"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read_dpp_ids_by_product_ids(
            product_ids=product_ids, limit=limit, cursor=cursor, request_options=request_options
        )
        return _response.data

    async def create_dpp(
        self,
        *,
        request: DigitalProductPassport,
        representation: typing.Optional[CreateDppRequestRepresentation] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateDppResult:
        """
        Creates a new DPP and returns its DPP ID. Conformance: should.

        Parameters
        ----------
        request : DigitalProductPassport

        representation : typing.Optional[CreateDppRequestRepresentation]
            Payload form per EN 18222 clause 8.1. Absent implies `compressed`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateDppResult
            DPP created.

        Examples
        --------
        import asyncio
        import datetime

        from fern import AsyncFernApi, DigitalProductPassportCompressed, Granularity

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
            api_key="YOUR_API_KEY",
            api_key_secret="YOUR_API_KEY_SECRET",
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.life_cycle_api.create_dpp(
                request=DigitalProductPassportCompressed(
                    digital_product_passport_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                    unique_product_identifier="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                    granularity=Granularity.MODEL,
                    dpp_schema_version="EN 18223:2026",
                    dpp_status="active",
                    last_updated=datetime.datetime.fromisoformat(
                        "2026-06-08 15:30:00+00:00",
                    ),
                    economic_operator_id="https://id.gs1.org/01/09521002005004/21/BAT2024-001",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_dpp(
            request=request, representation=representation, request_options=request_options
        )
        return _response.data
