

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAiClient, RawAiClient
from .types.ai_classify_survey_request_language_strategy import AiClassifySurveyRequestLanguageStrategy
from .types.ai_classify_survey_request_run_strategy import AiClassifySurveyRequestRunStrategy
from .types.ai_classify_survey_response import AiClassifySurveyResponse
from .types.ai_gateway_delete_response import AiGatewayDeleteResponse
from .types.ai_gateway_info_response import AiGatewayInfoResponse
from .types.ai_gateway_logs_response import AiGatewayLogsResponse
from .types.ai_gateway_model_pricing_response import AiGatewayModelPricingResponse
from .types.ai_gateway_quota_alert_get_response import AiGatewayQuotaAlertGetResponse
from .types.ai_gateway_quota_alert_upsert_response import AiGatewayQuotaAlertUpsertResponse
from .types.ai_gateway_update_response import AiGatewayUpdateResponse
from .types.ai_translate_survey_request_language_strategy import AiTranslateSurveyRequestLanguageStrategy
from .types.ai_translate_survey_request_run_strategy import AiTranslateSurveyRequestRunStrategy
from .types.ai_translate_survey_response import AiTranslateSurveyResponse


OMIT = typing.cast(typing.Any, ...)


class AiClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAiClient
        """
        return self._raw_client

    def classifysurvey(
        self,
        *,
        workspace_id: str,
        survey_id: str,
        start_at: float,
        end_at: float,
        run_strategy: AiClassifySurveyRequestRunStrategy,
        payload_content_field: str,
        suggestion_category: typing.Sequence[str],
        language_strategy: typing.Optional[AiClassifySurveyRequestLanguageStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiClassifySurveyResponse:
        """
        classify survey

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : float

        end_at : float

        run_strategy : AiClassifySurveyRequestRunStrategy

        payload_content_field : str

        suggestion_category : typing.Sequence[str]

        language_strategy : typing.Optional[AiClassifySurveyRequestLanguageStrategy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiClassifySurveyResponse
            Successful response

        Examples
        --------
        from fern.ai import AiClassifySurveyRequestRunStrategy

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.classifysurvey(
            workspace_id="workspaceId",
            survey_id="surveyId",
            start_at=1.1,
            end_at=1.1,
            run_strategy=AiClassifySurveyRequestRunStrategy.SKIP_EXIST,
            payload_content_field="payloadContentField",
            suggestion_category=["suggestionCategory"],
        )
        """
        _response = self._raw_client.classifysurvey(
            workspace_id=workspace_id,
            survey_id=survey_id,
            start_at=start_at,
            end_at=end_at,
            run_strategy=run_strategy,
            payload_content_field=payload_content_field,
            suggestion_category=suggestion_category,
            language_strategy=language_strategy,
            request_options=request_options,
        )
        return _response.data

    def translatesurvey(
        self,
        *,
        workspace_id: str,
        survey_id: str,
        start_at: float,
        end_at: float,
        run_strategy: AiTranslateSurveyRequestRunStrategy,
        payload_content_field: str,
        language_strategy: typing.Optional[AiTranslateSurveyRequestLanguageStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiTranslateSurveyResponse:
        """
        translate survey

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : float

        end_at : float

        run_strategy : AiTranslateSurveyRequestRunStrategy

        payload_content_field : str

        language_strategy : typing.Optional[AiTranslateSurveyRequestLanguageStrategy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiTranslateSurveyResponse
            Successful response

        Examples
        --------
        from fern.ai import AiTranslateSurveyRequestRunStrategy

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.translatesurvey(
            workspace_id="workspaceId",
            survey_id="surveyId",
            start_at=1.1,
            end_at=1.1,
            run_strategy=AiTranslateSurveyRequestRunStrategy.SKIP_EXIST,
            payload_content_field="payloadContentField",
        )
        """
        _response = self._raw_client.translatesurvey(
            workspace_id=workspace_id,
            survey_id=survey_id,
            start_at=start_at,
            end_at=end_at,
            run_strategy=run_strategy,
            payload_content_field=payload_content_field,
            language_strategy=language_strategy,
            request_options=request_options,
        )
        return _response.data

    def ai_gateway_info(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AiGatewayInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AiGatewayInfoResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.ai_gateway_info(
            workspace_id="workspaceId",
            gateway_id="gatewayId",
        )
        """
        _response = self._raw_client.ai_gateway_info(
            workspace_id=workspace_id, gateway_id=gateway_id, request_options=request_options
        )
        return _response.data

    def ai_gateway_update(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        name: str,
        model_api_key: typing.Optional[str] = OMIT,
        custom_model_base_url: typing.Optional[str] = OMIT,
        custom_model_name: typing.Optional[str] = OMIT,
        custom_model_input_price: typing.Optional[float] = OMIT,
        custom_model_output_price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayUpdateResponse:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        name : str

        model_api_key : typing.Optional[str]

        custom_model_base_url : typing.Optional[str]

        custom_model_name : typing.Optional[str]

        custom_model_input_price : typing.Optional[float]

        custom_model_output_price : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayUpdateResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.ai_gateway_update(
            workspace_id="workspaceId",
            gateway_id="gatewayId",
            name="name",
        )
        """
        _response = self._raw_client.ai_gateway_update(
            workspace_id=workspace_id,
            gateway_id=gateway_id,
            name=name,
            model_api_key=model_api_key,
            custom_model_base_url=custom_model_base_url,
            custom_model_name=custom_model_name,
            custom_model_input_price=custom_model_input_price,
            custom_model_output_price=custom_model_output_price,
            request_options=request_options,
        )
        return _response.data

    def ai_gateway_delete(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AiGatewayDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayDeleteResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.ai_gateway_delete(
            workspace_id="workspaceId",
            gateway_id="gatewayId",
        )
        """
        _response = self._raw_client.ai_gateway_delete(
            workspace_id=workspace_id, gateway_id=gateway_id, request_options=request_options
        )
        return _response.data

    def ai_gateway_logs(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        log_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayLogsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        log_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayLogsResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.ai_gateway_logs(
            workspace_id="workspaceId",
            gateway_id="gatewayId",
        )
        """
        _response = self._raw_client.ai_gateway_logs(
            workspace_id=workspace_id,
            gateway_id=gateway_id,
            cursor=cursor,
            limit=limit,
            log_id=log_id,
            request_options=request_options,
        )
        return _response.data

    def ai_gateway_model_pricing(
        self,
        *,
        workspace_id: str,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayModelPricingResponse:
        """
        Parameters
        ----------
        workspace_id : str

        search : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayModelPricingResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.ai_gateway_model_pricing(
            workspace_id="workspaceId",
        )
        """
        _response = self._raw_client.ai_gateway_model_pricing(
            workspace_id=workspace_id, search=search, limit=limit, request_options=request_options
        )
        return _response.data

    def ai_gateway_quota_alert_get(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AiGatewayQuotaAlertGetResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AiGatewayQuotaAlertGetResponse]
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.ai_gateway_quota_alert_get(
            workspace_id="workspaceId",
            gateway_id="gatewayId",
        )
        """
        _response = self._raw_client.ai_gateway_quota_alert_get(
            workspace_id=workspace_id, gateway_id=gateway_id, request_options=request_options
        )
        return _response.data

    def ai_gateway_quota_alert_upsert(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        daily_quota: float,
        enabled: bool,
        notification_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayQuotaAlertUpsertResponse:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        daily_quota : float

        enabled : bool

        notification_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayQuotaAlertUpsertResponse
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.ai_gateway_quota_alert_upsert(
            workspace_id="workspaceId",
            gateway_id="gatewayId",
            daily_quota=1.1,
            enabled=True,
        )
        """
        _response = self._raw_client.ai_gateway_quota_alert_upsert(
            workspace_id=workspace_id,
            gateway_id=gateway_id,
            daily_quota=daily_quota,
            enabled=enabled,
            notification_id=notification_id,
            request_options=request_options,
        )
        return _response.data

    def ai_gateway_quota_alert_delete(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.ai.ai_gateway_quota_alert_delete(
            workspace_id="workspaceId",
            gateway_id="gatewayId",
        )
        """
        _response = self._raw_client.ai_gateway_quota_alert_delete(
            workspace_id=workspace_id, gateway_id=gateway_id, request_options=request_options
        )
        return _response.data


class AsyncAiClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAiClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAiClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAiClient
        """
        return self._raw_client

    async def classifysurvey(
        self,
        *,
        workspace_id: str,
        survey_id: str,
        start_at: float,
        end_at: float,
        run_strategy: AiClassifySurveyRequestRunStrategy,
        payload_content_field: str,
        suggestion_category: typing.Sequence[str],
        language_strategy: typing.Optional[AiClassifySurveyRequestLanguageStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiClassifySurveyResponse:
        """
        classify survey

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : float

        end_at : float

        run_strategy : AiClassifySurveyRequestRunStrategy

        payload_content_field : str

        suggestion_category : typing.Sequence[str]

        language_strategy : typing.Optional[AiClassifySurveyRequestLanguageStrategy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiClassifySurveyResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.ai import AiClassifySurveyRequestRunStrategy

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.classifysurvey(
                workspace_id="workspaceId",
                survey_id="surveyId",
                start_at=1.1,
                end_at=1.1,
                run_strategy=AiClassifySurveyRequestRunStrategy.SKIP_EXIST,
                payload_content_field="payloadContentField",
                suggestion_category=["suggestionCategory"],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.classifysurvey(
            workspace_id=workspace_id,
            survey_id=survey_id,
            start_at=start_at,
            end_at=end_at,
            run_strategy=run_strategy,
            payload_content_field=payload_content_field,
            suggestion_category=suggestion_category,
            language_strategy=language_strategy,
            request_options=request_options,
        )
        return _response.data

    async def translatesurvey(
        self,
        *,
        workspace_id: str,
        survey_id: str,
        start_at: float,
        end_at: float,
        run_strategy: AiTranslateSurveyRequestRunStrategy,
        payload_content_field: str,
        language_strategy: typing.Optional[AiTranslateSurveyRequestLanguageStrategy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiTranslateSurveyResponse:
        """
        translate survey

        Parameters
        ----------
        workspace_id : str

        survey_id : str

        start_at : float

        end_at : float

        run_strategy : AiTranslateSurveyRequestRunStrategy

        payload_content_field : str

        language_strategy : typing.Optional[AiTranslateSurveyRequestLanguageStrategy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiTranslateSurveyResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern.ai import AiTranslateSurveyRequestRunStrategy

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.translatesurvey(
                workspace_id="workspaceId",
                survey_id="surveyId",
                start_at=1.1,
                end_at=1.1,
                run_strategy=AiTranslateSurveyRequestRunStrategy.SKIP_EXIST,
                payload_content_field="payloadContentField",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.translatesurvey(
            workspace_id=workspace_id,
            survey_id=survey_id,
            start_at=start_at,
            end_at=end_at,
            run_strategy=run_strategy,
            payload_content_field=payload_content_field,
            language_strategy=language_strategy,
            request_options=request_options,
        )
        return _response.data

    async def ai_gateway_info(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AiGatewayInfoResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AiGatewayInfoResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.ai_gateway_info(
                workspace_id="workspaceId",
                gateway_id="gatewayId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_gateway_info(
            workspace_id=workspace_id, gateway_id=gateway_id, request_options=request_options
        )
        return _response.data

    async def ai_gateway_update(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        name: str,
        model_api_key: typing.Optional[str] = OMIT,
        custom_model_base_url: typing.Optional[str] = OMIT,
        custom_model_name: typing.Optional[str] = OMIT,
        custom_model_input_price: typing.Optional[float] = OMIT,
        custom_model_output_price: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayUpdateResponse:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        name : str

        model_api_key : typing.Optional[str]

        custom_model_base_url : typing.Optional[str]

        custom_model_name : typing.Optional[str]

        custom_model_input_price : typing.Optional[float]

        custom_model_output_price : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayUpdateResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.ai_gateway_update(
                workspace_id="workspaceId",
                gateway_id="gatewayId",
                name="name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_gateway_update(
            workspace_id=workspace_id,
            gateway_id=gateway_id,
            name=name,
            model_api_key=model_api_key,
            custom_model_base_url=custom_model_base_url,
            custom_model_name=custom_model_name,
            custom_model_input_price=custom_model_input_price,
            custom_model_output_price=custom_model_output_price,
            request_options=request_options,
        )
        return _response.data

    async def ai_gateway_delete(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AiGatewayDeleteResponse:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayDeleteResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.ai_gateway_delete(
                workspace_id="workspaceId",
                gateway_id="gatewayId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_gateway_delete(
            workspace_id=workspace_id, gateway_id=gateway_id, request_options=request_options
        )
        return _response.data

    async def ai_gateway_logs(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        log_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayLogsResponse:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        cursor : typing.Optional[str]

        limit : typing.Optional[int]

        log_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayLogsResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.ai_gateway_logs(
                workspace_id="workspaceId",
                gateway_id="gatewayId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_gateway_logs(
            workspace_id=workspace_id,
            gateway_id=gateway_id,
            cursor=cursor,
            limit=limit,
            log_id=log_id,
            request_options=request_options,
        )
        return _response.data

    async def ai_gateway_model_pricing(
        self,
        *,
        workspace_id: str,
        search: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayModelPricingResponse:
        """
        Parameters
        ----------
        workspace_id : str

        search : typing.Optional[str]

        limit : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayModelPricingResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.ai_gateway_model_pricing(
                workspace_id="workspaceId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_gateway_model_pricing(
            workspace_id=workspace_id, search=search, limit=limit, request_options=request_options
        )
        return _response.data

    async def ai_gateway_quota_alert_get(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Optional[AiGatewayQuotaAlertGetResponse]:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Optional[AiGatewayQuotaAlertGetResponse]
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.ai_gateway_quota_alert_get(
                workspace_id="workspaceId",
                gateway_id="gatewayId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_gateway_quota_alert_get(
            workspace_id=workspace_id, gateway_id=gateway_id, request_options=request_options
        )
        return _response.data

    async def ai_gateway_quota_alert_upsert(
        self,
        *,
        workspace_id: str,
        gateway_id: str,
        daily_quota: float,
        enabled: bool,
        notification_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AiGatewayQuotaAlertUpsertResponse:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        daily_quota : float

        enabled : bool

        notification_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AiGatewayQuotaAlertUpsertResponse
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.ai_gateway_quota_alert_upsert(
                workspace_id="workspaceId",
                gateway_id="gatewayId",
                daily_quota=1.1,
                enabled=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_gateway_quota_alert_upsert(
            workspace_id=workspace_id,
            gateway_id=gateway_id,
            daily_quota=daily_quota,
            enabled=enabled,
            notification_id=notification_id,
            request_options=request_options,
        )
        return _response.data

    async def ai_gateway_quota_alert_delete(
        self, *, workspace_id: str, gateway_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> bool:
        """
        Parameters
        ----------
        workspace_id : str

        gateway_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        bool
            Successful response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.ai.ai_gateway_quota_alert_delete(
                workspace_id="workspaceId",
                gateway_id="gatewayId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ai_gateway_quota_alert_delete(
            workspace_id=workspace_id, gateway_id=gateway_id, request_options=request_options
        )
        return _response.data
