

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.annotation_setting import AnnotationSetting
from .raw_client import AsyncRawAnnotationSettingV1AlphaUcClient, RawAnnotationSettingV1AlphaUcClient


class AnnotationSettingV1AlphaUcClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAnnotationSettingV1AlphaUcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAnnotationSettingV1AlphaUcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAnnotationSettingV1AlphaUcClient
        """
        return self._raw_client

    def list_available_annotation_settings(
        self, *, target_ref: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AnnotationSetting]:
        """
        List available AnnotationSettings for the given targetRef. The available AnnotationSettings are determined by the currently activated theme and started plugins.

        Parameters
        ----------
        target_ref : str
            The targetRef of the AnnotationSetting. e.g.: 'content.halo.run/Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AnnotationSetting]
            default response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.annotation_setting_v1alpha_uc.list_available_annotation_settings(
            target_ref="targetRef",
        )
        """
        _response = self._raw_client.list_available_annotation_settings(
            target_ref=target_ref, request_options=request_options
        )
        return _response.data


class AsyncAnnotationSettingV1AlphaUcClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAnnotationSettingV1AlphaUcClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAnnotationSettingV1AlphaUcClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAnnotationSettingV1AlphaUcClient
        """
        return self._raw_client

    async def list_available_annotation_settings(
        self, *, target_ref: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AnnotationSetting]:
        """
        List available AnnotationSettings for the given targetRef. The available AnnotationSettings are determined by the currently activated theme and started plugins.

        Parameters
        ----------
        target_ref : str
            The targetRef of the AnnotationSetting. e.g.: 'content.halo.run/Post

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AnnotationSetting]
            default response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.annotation_setting_v1alpha_uc.list_available_annotation_settings(
                target_ref="targetRef",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_available_annotation_settings(
            target_ref=target_ref, request_options=request_options
        )
        return _response.data
