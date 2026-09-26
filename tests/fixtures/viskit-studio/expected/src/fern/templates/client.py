

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.preview_response import PreviewResponse
from ..types.scheme_slot import SchemeSlot
from ..types.scheme_summary import SchemeSummary
from ..types.template_summary import TemplateSummary
from .raw_client import AsyncRawTemplatesClient, RawTemplatesClient
from .types.list_schemes_api_templates_schemes_get_request_locale import ListSchemesApiTemplatesSchemesGetRequestLocale
from .types.preview_request_locale import PreviewRequestLocale
from .types.scheme_payload_locale import SchemePayloadLocale
from .types.template_payload_category import TemplatePayloadCategory
from .types.template_payload_locale import TemplatePayloadLocale
from .types.template_update_category import TemplateUpdateCategory


OMIT = typing.cast(typing.Any, ...)


class TemplatesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTemplatesClient
        """
        return self._raw_client

    def get_templates(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[TemplateSummary]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TemplateSummary]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.templates.get_templates()
        """
        _response = self._raw_client.get_templates(request_options=request_options)
        return _response.data

    def create_template(
        self,
        *,
        locale: TemplatePayloadLocale,
        name: str,
        prompt_template: typing.Dict[str, str],
        category: typing.Optional[TemplatePayloadCategory] = OMIT,
        category_tips: typing.Optional[typing.Dict[str, str]] = OMIT,
        defaults: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        examples: typing.Optional[typing.Sequence[str]] = OMIT,
        supports_image_reference: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        variants: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TemplateSummary:
        """
        Parameters
        ----------
        locale : TemplatePayloadLocale

        name : str

        prompt_template : typing.Dict[str, str]

        category : typing.Optional[TemplatePayloadCategory]

        category_tips : typing.Optional[typing.Dict[str, str]]

        defaults : typing.Optional[typing.Dict[str, str]]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        examples : typing.Optional[typing.Sequence[str]]

        supports_image_reference : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        variants : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TemplateSummary
            Successful Response

        Examples
        --------
        from fern.templates import TemplatePayloadLocale

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.templates.create_template(
            locale=TemplatePayloadLocale.ZH,
            name="name",
            prompt_template={"key": "value"},
        )
        """
        _response = self._raw_client.create_template(
            locale=locale,
            name=name,
            prompt_template=prompt_template,
            category=category,
            category_tips=category_tips,
            defaults=defaults,
            description=description,
            enabled=enabled,
            examples=examples,
            supports_image_reference=supports_image_reference,
            tags=tags,
            variants=variants,
            request_options=request_options,
        )
        return _response.data

    def copy_template(
        self,
        *,
        source_ref: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TemplateSummary:
        """
        Parameters
        ----------
        source_ref : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TemplateSummary
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.templates.copy_template(
            source_ref="source_ref",
        )
        """
        _response = self._raw_client.copy_template(source_ref=source_ref, name=name, request_options=request_options)
        return _response.data

    def get_managed_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TemplateSummary]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TemplateSummary]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.templates.get_managed_templates()
        """
        _response = self._raw_client.get_managed_templates(request_options=request_options)
        return _response.data

    def preview_template(
        self,
        *,
        locale: PreviewRequestLocale,
        template_ref: str,
        brand_color_hex: typing.Optional[str] = OMIT,
        copy: typing.Optional[str] = OMIT,
        design_note: typing.Optional[str] = OMIT,
        sample_brand: typing.Optional[str] = OMIT,
        sample_category: typing.Optional[str] = OMIT,
        sample_name: typing.Optional[str] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        visual: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreviewResponse:
        """
        Parameters
        ----------
        locale : PreviewRequestLocale

        template_ref : str

        brand_color_hex : typing.Optional[str]

        copy : typing.Optional[str]

        design_note : typing.Optional[str]

        sample_brand : typing.Optional[str]

        sample_category : typing.Optional[str]

        sample_name : typing.Optional[str]

        style_prompt : typing.Optional[str]

        visual : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewResponse
            Successful Response

        Examples
        --------
        from fern.templates import PreviewRequestLocale

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.templates.preview_template(
            locale=PreviewRequestLocale.ZH,
            template_ref="template_ref",
        )
        """
        _response = self._raw_client.preview_template(
            locale=locale,
            template_ref=template_ref,
            brand_color_hex=brand_color_hex,
            copy=copy,
            design_note=design_note,
            sample_brand=sample_brand,
            sample_category=sample_category,
            sample_name=sample_name,
            style_prompt=style_prompt,
            visual=visual,
            request_options=request_options,
        )
        return _response.data

    def list_schemes(
        self,
        *,
        locale: typing.Optional[ListSchemesApiTemplatesSchemesGetRequestLocale] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SchemeSummary]:
        """
        Parameters
        ----------
        locale : typing.Optional[ListSchemesApiTemplatesSchemesGetRequestLocale]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchemeSummary]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.templates.list_schemes()
        """
        _response = self._raw_client.list_schemes(locale=locale, request_options=request_options)
        return _response.data

    def create_scheme(
        self,
        *,
        locale: SchemePayloadLocale,
        name: str,
        slots: typing.Sequence[SchemeSlot],
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemeSummary:
        """
        Parameters
        ----------
        locale : SchemePayloadLocale

        name : str

        slots : typing.Sequence[SchemeSlot]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemeSummary
            Successful Response

        Examples
        --------
        from fern.templates import SchemePayloadLocale

        from fern import FernApi, SchemeSlot, SchemeSlotSlotId

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.templates.create_scheme(
            locale=SchemePayloadLocale.ZH,
            name="name",
            slots=[
                SchemeSlot(
                    slot_id=SchemeSlotSlotId.H1,
                    template_ref="template_ref",
                )
            ],
        )
        """
        _response = self._raw_client.create_scheme(
            locale=locale,
            name=name,
            slots=slots,
            description=description,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    def delete_template(
        self, template_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, bool]:
        """
        Parameters
        ----------
        template_ref : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, bool]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.templates.delete_template(
            template_ref="template_ref",
        )
        """
        _response = self._raw_client.delete_template(template_ref, request_options=request_options)
        return _response.data

    def update_template(
        self,
        template_ref: str,
        *,
        category: typing.Optional[TemplateUpdateCategory] = OMIT,
        category_tips: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        defaults: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        examples: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        supports_image_reference: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        variants: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TemplateSummary:
        """
        Parameters
        ----------
        template_ref : str

        category : typing.Optional[TemplateUpdateCategory]

        category_tips : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        defaults : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        examples : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        prompt_template : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        supports_image_reference : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        variants : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TemplateSummary
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.templates.update_template(
            template_ref="template_ref",
        )
        """
        _response = self._raw_client.update_template(
            template_ref,
            category=category,
            category_tips=category_tips,
            defaults=defaults,
            description=description,
            enabled=enabled,
            examples=examples,
            name=name,
            prompt_template=prompt_template,
            supports_image_reference=supports_image_reference,
            tags=tags,
            variants=variants,
            request_options=request_options,
        )
        return _response.data


class AsyncTemplatesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTemplatesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTemplatesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTemplatesClient
        """
        return self._raw_client

    async def get_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TemplateSummary]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TemplateSummary]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.templates.get_templates()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_templates(request_options=request_options)
        return _response.data

    async def create_template(
        self,
        *,
        locale: TemplatePayloadLocale,
        name: str,
        prompt_template: typing.Dict[str, str],
        category: typing.Optional[TemplatePayloadCategory] = OMIT,
        category_tips: typing.Optional[typing.Dict[str, str]] = OMIT,
        defaults: typing.Optional[typing.Dict[str, str]] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        examples: typing.Optional[typing.Sequence[str]] = OMIT,
        supports_image_reference: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        variants: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TemplateSummary:
        """
        Parameters
        ----------
        locale : TemplatePayloadLocale

        name : str

        prompt_template : typing.Dict[str, str]

        category : typing.Optional[TemplatePayloadCategory]

        category_tips : typing.Optional[typing.Dict[str, str]]

        defaults : typing.Optional[typing.Dict[str, str]]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        examples : typing.Optional[typing.Sequence[str]]

        supports_image_reference : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        variants : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TemplateSummary
            Successful Response

        Examples
        --------
        import asyncio

        from fern.templates import TemplatePayloadLocale

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.templates.create_template(
                locale=TemplatePayloadLocale.ZH,
                name="name",
                prompt_template={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_template(
            locale=locale,
            name=name,
            prompt_template=prompt_template,
            category=category,
            category_tips=category_tips,
            defaults=defaults,
            description=description,
            enabled=enabled,
            examples=examples,
            supports_image_reference=supports_image_reference,
            tags=tags,
            variants=variants,
            request_options=request_options,
        )
        return _response.data

    async def copy_template(
        self,
        *,
        source_ref: str,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TemplateSummary:
        """
        Parameters
        ----------
        source_ref : str

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TemplateSummary
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.templates.copy_template(
                source_ref="source_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.copy_template(
            source_ref=source_ref, name=name, request_options=request_options
        )
        return _response.data

    async def get_managed_templates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[TemplateSummary]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[TemplateSummary]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.templates.get_managed_templates()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_managed_templates(request_options=request_options)
        return _response.data

    async def preview_template(
        self,
        *,
        locale: PreviewRequestLocale,
        template_ref: str,
        brand_color_hex: typing.Optional[str] = OMIT,
        copy: typing.Optional[str] = OMIT,
        design_note: typing.Optional[str] = OMIT,
        sample_brand: typing.Optional[str] = OMIT,
        sample_category: typing.Optional[str] = OMIT,
        sample_name: typing.Optional[str] = OMIT,
        style_prompt: typing.Optional[str] = OMIT,
        visual: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PreviewResponse:
        """
        Parameters
        ----------
        locale : PreviewRequestLocale

        template_ref : str

        brand_color_hex : typing.Optional[str]

        copy : typing.Optional[str]

        design_note : typing.Optional[str]

        sample_brand : typing.Optional[str]

        sample_category : typing.Optional[str]

        sample_name : typing.Optional[str]

        style_prompt : typing.Optional[str]

        visual : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern.templates import PreviewRequestLocale

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.templates.preview_template(
                locale=PreviewRequestLocale.ZH,
                template_ref="template_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.preview_template(
            locale=locale,
            template_ref=template_ref,
            brand_color_hex=brand_color_hex,
            copy=copy,
            design_note=design_note,
            sample_brand=sample_brand,
            sample_category=sample_category,
            sample_name=sample_name,
            style_prompt=style_prompt,
            visual=visual,
            request_options=request_options,
        )
        return _response.data

    async def list_schemes(
        self,
        *,
        locale: typing.Optional[ListSchemesApiTemplatesSchemesGetRequestLocale] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[SchemeSummary]:
        """
        Parameters
        ----------
        locale : typing.Optional[ListSchemesApiTemplatesSchemesGetRequestLocale]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SchemeSummary]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.templates.list_schemes()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_schemes(locale=locale, request_options=request_options)
        return _response.data

    async def create_scheme(
        self,
        *,
        locale: SchemePayloadLocale,
        name: str,
        slots: typing.Sequence[SchemeSlot],
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SchemeSummary:
        """
        Parameters
        ----------
        locale : SchemePayloadLocale

        name : str

        slots : typing.Sequence[SchemeSlot]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SchemeSummary
            Successful Response

        Examples
        --------
        import asyncio

        from fern.templates import SchemePayloadLocale

        from fern import AsyncFernApi, SchemeSlot, SchemeSlotSlotId

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.templates.create_scheme(
                locale=SchemePayloadLocale.ZH,
                name="name",
                slots=[
                    SchemeSlot(
                        slot_id=SchemeSlotSlotId.H1,
                        template_ref="template_ref",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_scheme(
            locale=locale,
            name=name,
            slots=slots,
            description=description,
            enabled=enabled,
            request_options=request_options,
        )
        return _response.data

    async def delete_template(
        self, template_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, bool]:
        """
        Parameters
        ----------
        template_ref : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, bool]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.templates.delete_template(
                template_ref="template_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_template(template_ref, request_options=request_options)
        return _response.data

    async def update_template(
        self,
        template_ref: str,
        *,
        category: typing.Optional[TemplateUpdateCategory] = OMIT,
        category_tips: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        defaults: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        description: typing.Optional[str] = OMIT,
        enabled: typing.Optional[bool] = OMIT,
        examples: typing.Optional[typing.Sequence[str]] = OMIT,
        name: typing.Optional[str] = OMIT,
        prompt_template: typing.Optional[typing.Dict[str, typing.Optional[str]]] = OMIT,
        supports_image_reference: typing.Optional[bool] = OMIT,
        tags: typing.Optional[typing.Sequence[str]] = OMIT,
        variants: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TemplateSummary:
        """
        Parameters
        ----------
        template_ref : str

        category : typing.Optional[TemplateUpdateCategory]

        category_tips : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        defaults : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        description : typing.Optional[str]

        enabled : typing.Optional[bool]

        examples : typing.Optional[typing.Sequence[str]]

        name : typing.Optional[str]

        prompt_template : typing.Optional[typing.Dict[str, typing.Optional[str]]]

        supports_image_reference : typing.Optional[bool]

        tags : typing.Optional[typing.Sequence[str]]

        variants : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TemplateSummary
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.templates.update_template(
                template_ref="template_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_template(
            template_ref,
            category=category,
            category_tips=category_tips,
            defaults=defaults,
            description=description,
            enabled=enabled,
            examples=examples,
            name=name,
            prompt_template=prompt_template,
            supports_image_reference=supports_image_reference,
            tags=tags,
            variants=variants,
            request_options=request_options,
        )
        return _response.data
