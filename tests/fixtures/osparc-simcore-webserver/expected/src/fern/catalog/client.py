

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.envelope_catalog_service_get import EnvelopeCatalogServiceGet
from ..types.envelope_dict_annotated_str_string_constraints_image_resources import (
    EnvelopeDictAnnotatedStrStringConstraintsImageResources,
)
from ..types.envelope_list_annotated_str_string_constraints import EnvelopeListAnnotatedStrStringConstraints
from ..types.envelope_list_service_input_get import EnvelopeListServiceInputGet
from ..types.envelope_list_service_output_get import EnvelopeListServiceOutputGet
from ..types.envelope_list_tag_get import EnvelopeListTagGet
from ..types.envelope_service_input_get import EnvelopeServiceInputGet
from ..types.envelope_service_pricing_plan_get import EnvelopeServicePricingPlanGet
from ..types.page_catalog_latest_service_get import PageCatalogLatestServiceGet
from ..types.service_group_access_rights_v2 import ServiceGroupAccessRightsV2
from .raw_client import AsyncRawCatalogClient, RawCatalogClient


OMIT = typing.cast(typing.Any, ...)


class CatalogClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCatalogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCatalogClient
        """
        return self._raw_client

    def list_services_latest(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageCatalogLatestServiceGet:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageCatalogLatestServiceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.list_services_latest()
        """
        _response = self._raw_client.list_services_latest(limit=limit, offset=offset, request_options=request_options)
        return _response.data

    def get_service(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeCatalogServiceGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCatalogServiceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.get_service(
            service_key="service_key",
            service_version="service_version",
        )
        """
        _response = self._raw_client.get_service(service_key, service_version, request_options=request_options)
        return _response.data

    def update_service(
        self,
        service_key: str,
        service_version: str,
        *,
        name: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_ui: typing.Optional[bool] = OMIT,
        version_display: typing.Optional[str] = OMIT,
        deprecated: typing.Optional[dt.datetime] = OMIT,
        classifiers: typing.Optional[typing.Sequence[str]] = OMIT,
        quality: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        access_rights: typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]] = OMIT,
        release_notes_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeCatalogServiceGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        name : typing.Optional[str]

        thumbnail : typing.Optional[str]

        icon : typing.Optional[str]

        description : typing.Optional[str]

        description_ui : typing.Optional[bool]

        version_display : typing.Optional[str]

        deprecated : typing.Optional[dt.datetime]

        classifiers : typing.Optional[typing.Sequence[str]]

        quality : typing.Optional[typing.Dict[str, typing.Any]]

        access_rights : typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]]

        release_notes_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCatalogServiceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.update_service(
            service_key="service_key",
            service_version="service_version",
        )
        """
        _response = self._raw_client.update_service(
            service_key,
            service_version,
            name=name,
            thumbnail=thumbnail,
            icon=icon,
            description=description,
            description_ui=description_ui,
            version_display=version_display,
            deprecated=deprecated,
            classifiers=classifiers,
            quality=quality,
            access_rights=access_rights,
            release_notes_url=release_notes_url,
            request_options=request_options,
        )
        return _response.data

    def list_service_inputs(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListServiceInputGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListServiceInputGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.list_service_inputs(
            service_key="service_key",
            service_version="service_version",
        )
        """
        _response = self._raw_client.list_service_inputs(service_key, service_version, request_options=request_options)
        return _response.data

    def get_service_input(
        self,
        service_key: str,
        service_version: str,
        input_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeServiceInputGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        input_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeServiceInputGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.get_service_input(
            service_key="service_key",
            service_version="service_version",
            input_key="input_key",
        )
        """
        _response = self._raw_client.get_service_input(
            service_key, service_version, input_key, request_options=request_options
        )
        return _response.data

    def get_compatible_inputs_given_source_output(
        self,
        service_key: str,
        service_version: str,
        *,
        from_service: str,
        from_version: str,
        from_output: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListAnnotatedStrStringConstraints:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        from_service : str

        from_version : str

        from_output : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnotatedStrStringConstraints
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.get_compatible_inputs_given_source_output(
            service_key="service_key",
            service_version="service_version",
            from_service="fromService",
            from_version="fromVersion",
            from_output="fromOutput",
        )
        """
        _response = self._raw_client.get_compatible_inputs_given_source_output(
            service_key,
            service_version,
            from_service=from_service,
            from_version=from_version,
            from_output=from_output,
            request_options=request_options,
        )
        return _response.data

    def list_service_outputs(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListAnnotatedStrStringConstraints:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnotatedStrStringConstraints
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.list_service_outputs(
            service_key="service_key",
            service_version="service_version",
        )
        """
        _response = self._raw_client.list_service_outputs(service_key, service_version, request_options=request_options)
        return _response.data

    def get_service_output(
        self,
        service_key: str,
        service_version: str,
        output_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListServiceOutputGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        output_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListServiceOutputGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.get_service_output(
            service_key="service_key",
            service_version="service_version",
            output_key="output_key",
        )
        """
        _response = self._raw_client.get_service_output(
            service_key, service_version, output_key, request_options=request_options
        )
        return _response.data

    def get_compatible_outputs_given_target_input(
        self,
        service_key: str,
        service_version: str,
        *,
        to_service: str,
        to_version: str,
        to_input: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListAnnotatedStrStringConstraints:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        to_service : str

        to_version : str

        to_input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnotatedStrStringConstraints
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.get_compatible_outputs_given_target_input(
            service_key="service_key",
            service_version="service_version",
            to_service="toService",
            to_version="toVersion",
            to_input="toInput",
        )
        """
        _response = self._raw_client.get_compatible_outputs_given_target_input(
            service_key,
            service_version,
            to_service=to_service,
            to_version=to_version,
            to_input=to_input,
            request_options=request_options,
        )
        return _response.data

    def get_service_resources(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictAnnotatedStrStringConstraintsImageResources:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictAnnotatedStrStringConstraintsImageResources
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.get_service_resources(
            service_key="service_key",
            service_version="service_version",
        )
        """
        _response = self._raw_client.get_service_resources(
            service_key, service_version, request_options=request_options
        )
        return _response.data

    def get_service_pricing_plan(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeServicePricingPlanGet:
        """
        Retrieve default pricing plan for provided service

        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeServicePricingPlanGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.get_service_pricing_plan(
            service_key="service_key",
            service_version="service_version",
        )
        """
        _response = self._raw_client.get_service_pricing_plan(
            service_key, service_version, request_options=request_options
        )
        return _response.data

    def list_service_tags(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListTagGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTagGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.list_service_tags(
            service_key="service_key",
            service_version="service_version",
        )
        """
        _response = self._raw_client.list_service_tags(service_key, service_version, request_options=request_options)
        return _response.data

    def add_service_tag(
        self,
        service_key: str,
        service_version: str,
        tag_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeCatalogServiceGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCatalogServiceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.add_service_tag(
            service_key="service_key",
            service_version="service_version",
            tag_id=1,
        )
        """
        _response = self._raw_client.add_service_tag(
            service_key, service_version, tag_id, request_options=request_options
        )
        return _response.data

    def remove_service_tag(
        self,
        service_key: str,
        service_version: str,
        tag_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeCatalogServiceGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCatalogServiceGet
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.catalog.remove_service_tag(
            service_key="service_key",
            service_version="service_version",
            tag_id=1,
        )
        """
        _response = self._raw_client.remove_service_tag(
            service_key, service_version, tag_id, request_options=request_options
        )
        return _response.data


class AsyncCatalogClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCatalogClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCatalogClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCatalogClient
        """
        return self._raw_client

    async def list_services_latest(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PageCatalogLatestServiceGet:
        """
        Parameters
        ----------
        limit : typing.Optional[int]

        offset : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PageCatalogLatestServiceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.list_services_latest()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_services_latest(
            limit=limit, offset=offset, request_options=request_options
        )
        return _response.data

    async def get_service(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeCatalogServiceGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCatalogServiceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.get_service(
                service_key="service_key",
                service_version="service_version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service(service_key, service_version, request_options=request_options)
        return _response.data

    async def update_service(
        self,
        service_key: str,
        service_version: str,
        *,
        name: typing.Optional[str] = OMIT,
        thumbnail: typing.Optional[str] = OMIT,
        icon: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        description_ui: typing.Optional[bool] = OMIT,
        version_display: typing.Optional[str] = OMIT,
        deprecated: typing.Optional[dt.datetime] = OMIT,
        classifiers: typing.Optional[typing.Sequence[str]] = OMIT,
        quality: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        access_rights: typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]] = OMIT,
        release_notes_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeCatalogServiceGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        name : typing.Optional[str]

        thumbnail : typing.Optional[str]

        icon : typing.Optional[str]

        description : typing.Optional[str]

        description_ui : typing.Optional[bool]

        version_display : typing.Optional[str]

        deprecated : typing.Optional[dt.datetime]

        classifiers : typing.Optional[typing.Sequence[str]]

        quality : typing.Optional[typing.Dict[str, typing.Any]]

        access_rights : typing.Optional[typing.Dict[str, typing.Optional[ServiceGroupAccessRightsV2]]]

        release_notes_url : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCatalogServiceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.update_service(
                service_key="service_key",
                service_version="service_version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_service(
            service_key,
            service_version,
            name=name,
            thumbnail=thumbnail,
            icon=icon,
            description=description,
            description_ui=description_ui,
            version_display=version_display,
            deprecated=deprecated,
            classifiers=classifiers,
            quality=quality,
            access_rights=access_rights,
            release_notes_url=release_notes_url,
            request_options=request_options,
        )
        return _response.data

    async def list_service_inputs(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListServiceInputGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListServiceInputGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.list_service_inputs(
                service_key="service_key",
                service_version="service_version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_inputs(
            service_key, service_version, request_options=request_options
        )
        return _response.data

    async def get_service_input(
        self,
        service_key: str,
        service_version: str,
        input_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeServiceInputGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        input_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeServiceInputGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.get_service_input(
                service_key="service_key",
                service_version="service_version",
                input_key="input_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_input(
            service_key, service_version, input_key, request_options=request_options
        )
        return _response.data

    async def get_compatible_inputs_given_source_output(
        self,
        service_key: str,
        service_version: str,
        *,
        from_service: str,
        from_version: str,
        from_output: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListAnnotatedStrStringConstraints:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        from_service : str

        from_version : str

        from_output : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnotatedStrStringConstraints
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.get_compatible_inputs_given_source_output(
                service_key="service_key",
                service_version="service_version",
                from_service="fromService",
                from_version="fromVersion",
                from_output="fromOutput",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_compatible_inputs_given_source_output(
            service_key,
            service_version,
            from_service=from_service,
            from_version=from_version,
            from_output=from_output,
            request_options=request_options,
        )
        return _response.data

    async def list_service_outputs(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListAnnotatedStrStringConstraints:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnotatedStrStringConstraints
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.list_service_outputs(
                service_key="service_key",
                service_version="service_version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_outputs(
            service_key, service_version, request_options=request_options
        )
        return _response.data

    async def get_service_output(
        self,
        service_key: str,
        service_version: str,
        output_key: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListServiceOutputGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        output_key : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListServiceOutputGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.get_service_output(
                service_key="service_key",
                service_version="service_version",
                output_key="output_key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_output(
            service_key, service_version, output_key, request_options=request_options
        )
        return _response.data

    async def get_compatible_outputs_given_target_input(
        self,
        service_key: str,
        service_version: str,
        *,
        to_service: str,
        to_version: str,
        to_input: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeListAnnotatedStrStringConstraints:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        to_service : str

        to_version : str

        to_input : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListAnnotatedStrStringConstraints
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.get_compatible_outputs_given_target_input(
                service_key="service_key",
                service_version="service_version",
                to_service="toService",
                to_version="toVersion",
                to_input="toInput",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_compatible_outputs_given_target_input(
            service_key,
            service_version,
            to_service=to_service,
            to_version=to_version,
            to_input=to_input,
            request_options=request_options,
        )
        return _response.data

    async def get_service_resources(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeDictAnnotatedStrStringConstraintsImageResources:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeDictAnnotatedStrStringConstraintsImageResources
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.get_service_resources(
                service_key="service_key",
                service_version="service_version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_resources(
            service_key, service_version, request_options=request_options
        )
        return _response.data

    async def get_service_pricing_plan(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeServicePricingPlanGet:
        """
        Retrieve default pricing plan for provided service

        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeServicePricingPlanGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.get_service_pricing_plan(
                service_key="service_key",
                service_version="service_version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_service_pricing_plan(
            service_key, service_version, request_options=request_options
        )
        return _response.data

    async def list_service_tags(
        self, service_key: str, service_version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EnvelopeListTagGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeListTagGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.list_service_tags(
                service_key="service_key",
                service_version="service_version",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_service_tags(
            service_key, service_version, request_options=request_options
        )
        return _response.data

    async def add_service_tag(
        self,
        service_key: str,
        service_version: str,
        tag_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeCatalogServiceGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCatalogServiceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.add_service_tag(
                service_key="service_key",
                service_version="service_version",
                tag_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_service_tag(
            service_key, service_version, tag_id, request_options=request_options
        )
        return _response.data

    async def remove_service_tag(
        self,
        service_key: str,
        service_version: str,
        tag_id: int,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EnvelopeCatalogServiceGet:
        """
        Parameters
        ----------
        service_key : str

        service_version : str

        tag_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EnvelopeCatalogServiceGet
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.catalog.remove_service_tag(
                service_key="service_key",
                service_version="service_version",
                tag_id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_service_tag(
            service_key, service_version, tag_id, request_options=request_options
        )
        return _response.data
