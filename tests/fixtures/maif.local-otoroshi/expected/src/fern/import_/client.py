

import datetime as dt
import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.done import Done
from ..types.global_config import GlobalConfig
from ..types.import_export import ImportExport
from ..types.import_export_admins_item import ImportExportAdminsItem
from ..types.import_export_api_keys_item import ImportExportApiKeysItem
from ..types.import_export_error_templates_item import ImportExportErrorTemplatesItem
from ..types.import_export_service_descriptors_item import ImportExportServiceDescriptorsItem
from ..types.import_export_service_groups_item import ImportExportServiceGroupsItem
from ..types.import_export_simple_admins_item import ImportExportSimpleAdminsItem
from ..types.import_export_stats import ImportExportStats
from .raw_client import AsyncRawImportClient, RawImportClient


OMIT = typing.cast(typing.Any, ...)


class ImportClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImportClient
        """
        return self._raw_client

    def full_import_from_file(
        self,
        *,
        admins: typing.Sequence[ImportExportAdminsItem],
        api_keys: typing.Sequence[ImportExportApiKeysItem],
        config: GlobalConfig,
        date: dt.datetime,
        date_raw: int,
        error_templates: typing.Sequence[ImportExportErrorTemplatesItem],
        label: str,
        service_descriptors: typing.Sequence[ImportExportServiceDescriptorsItem],
        service_groups: typing.Sequence[ImportExportServiceGroupsItem],
        simple_admins: typing.Sequence[ImportExportSimpleAdminsItem],
        stats: ImportExportStats,
        app_config: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Done:
        """
        Import the full state of Otoroshi as a file

        Parameters
        ----------
        admins : typing.Sequence[ImportExportAdminsItem]
            Current U2F admin at the time of export

        api_keys : typing.Sequence[ImportExportApiKeysItem]
            Current apik keys at the time of export

        config : GlobalConfig
            Current global config at the time of export

        date : dt.datetime

        date_raw : int

        error_templates : typing.Sequence[ImportExportErrorTemplatesItem]
            Current error templates at the time of export

        label : str

        service_descriptors : typing.Sequence[ImportExportServiceDescriptorsItem]
            Current service descriptors at the time of export

        service_groups : typing.Sequence[ImportExportServiceGroupsItem]
            Current service groups at the time of export

        simple_admins : typing.Sequence[ImportExportSimpleAdminsItem]
            Current simple admins at the time of export

        stats : ImportExportStats
            Current global stats at the time of export

        app_config : typing.Optional[typing.Dict[str, str]]
            Current env variables at the time of export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import datetime

        from fern import (
            FernApi,
            GlobalConfig,
            ImportExportAdminsItem,
            ImportExportApiKeysItem,
            ImportExportErrorTemplatesItem,
            ImportExportServiceDescriptorsItem,
            ImportExportServiceGroupsItem,
            ImportExportSimpleAdminsItem,
            ImportExportStats,
            IpFiltering,
            Target,
            Webhook,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.import_.full_import_from_file(
            admins=[
                ImportExportAdminsItem(
                    created_at=123,
                    label="a string value",
                    password="a string value",
                    registration={"key": "value"},
                    username="a string value",
                )
            ],
            api_keys=[
                ImportExportApiKeysItem(
                    authorized_entities=["a string value"],
                    client_id="a string value",
                    client_name="a string value",
                    client_secret="a string value",
                    enabled=True,
                )
            ],
            config=GlobalConfig(
                alerts_emails=["admin@otoroshi.io"],
                alerts_webhooks=[
                    Webhook(
                        headers={"key": "value"},
                        url="http://www.google.com",
                    )
                ],
                analytics_webhooks=[
                    Webhook(
                        headers={"key": "value"},
                        url="http://www.google.com",
                    )
                ],
                api_read_only=True,
                auto_link_to_default_group=True,
                endless_ip_addresses=["192.192.192.192"],
                ip_filtering=IpFiltering(
                    blacklist=["192.192.192.192"],
                    whitelist=["192.192.192.192"],
                ),
                limit_concurrent_requests=True,
                max_concurrent_requests=123,
                per_ip_throttling_quota=123,
                stream_entity_only=True,
                throttling_quota=123,
                u2f_login_only=True,
                use_circuit_breakers=True,
            ),
            date=datetime.datetime.fromisoformat(
                "2017-07-21 17:32:28+00:00",
            ),
            date_raw=123,
            error_templates=[
                ImportExportErrorTemplatesItem(
                    messages={"key": "value"},
                    service_id="a string value",
                    template40x="a string value",
                    template50x="a string value",
                    template_build="a string value",
                    template_maintenance="a string value",
                )
            ],
            label="a string value",
            service_descriptors=[
                ImportExportServiceDescriptorsItem(
                    build_mode=True,
                    domain="a string value",
                    enabled=True,
                    enforce_secure_communication=True,
                    env="a string value",
                    force_https=True,
                    groups=["a string value"],
                    id="110e8400-e29b-11d4-a716-446655440000",
                    maintenance_mode=True,
                    name="a string value",
                    private_app=True,
                    root="a string value",
                    subdomain="a string value",
                    targets=[
                        Target(
                            host="www.google.com",
                            scheme="a string value",
                        )
                    ],
                )
            ],
            service_groups=[
                ImportExportServiceGroupsItem(
                    id="a string value",
                    name="a string value",
                )
            ],
            simple_admins=[
                ImportExportSimpleAdminsItem(
                    created_at=123,
                    label="a string value",
                    password="a string value",
                    username="a string value",
                )
            ],
            stats=ImportExportStats(
                calls=123,
                data_in=123,
                data_out=123,
            ),
        )
        """
        _response = self._raw_client.full_import_from_file(
            admins=admins,
            api_keys=api_keys,
            config=config,
            date=date,
            date_raw=date_raw,
            error_templates=error_templates,
            label=label,
            service_descriptors=service_descriptors,
            service_groups=service_groups,
            simple_admins=simple_admins,
            stats=stats,
            app_config=app_config,
            request_options=request_options,
        )
        return _response.data

    def full_export(self, *, request_options: typing.Optional[RequestOptions] = None) -> ImportExport:
        """
        Export the full state of Otoroshi

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportExport
            Successful operation

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.import_.full_export()
        """
        _response = self._raw_client.full_export(request_options=request_options)
        return _response.data

    def full_import(
        self,
        *,
        admins: typing.Sequence[ImportExportAdminsItem],
        api_keys: typing.Sequence[ImportExportApiKeysItem],
        config: GlobalConfig,
        date: dt.datetime,
        date_raw: int,
        error_templates: typing.Sequence[ImportExportErrorTemplatesItem],
        label: str,
        service_descriptors: typing.Sequence[ImportExportServiceDescriptorsItem],
        service_groups: typing.Sequence[ImportExportServiceGroupsItem],
        simple_admins: typing.Sequence[ImportExportSimpleAdminsItem],
        stats: ImportExportStats,
        app_config: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Done:
        """
        Import the full state of Otoroshi

        Parameters
        ----------
        admins : typing.Sequence[ImportExportAdminsItem]
            Current U2F admin at the time of export

        api_keys : typing.Sequence[ImportExportApiKeysItem]
            Current apik keys at the time of export

        config : GlobalConfig
            Current global config at the time of export

        date : dt.datetime

        date_raw : int

        error_templates : typing.Sequence[ImportExportErrorTemplatesItem]
            Current error templates at the time of export

        label : str

        service_descriptors : typing.Sequence[ImportExportServiceDescriptorsItem]
            Current service descriptors at the time of export

        service_groups : typing.Sequence[ImportExportServiceGroupsItem]
            Current service groups at the time of export

        simple_admins : typing.Sequence[ImportExportSimpleAdminsItem]
            Current simple admins at the time of export

        stats : ImportExportStats
            Current global stats at the time of export

        app_config : typing.Optional[typing.Dict[str, str]]
            Current env variables at the time of export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import datetime

        from fern import (
            FernApi,
            GlobalConfig,
            ImportExportAdminsItem,
            ImportExportApiKeysItem,
            ImportExportErrorTemplatesItem,
            ImportExportServiceDescriptorsItem,
            ImportExportServiceGroupsItem,
            ImportExportSimpleAdminsItem,
            ImportExportStats,
            IpFiltering,
            Target,
            Webhook,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.import_.full_import(
            admins=[
                ImportExportAdminsItem(
                    created_at=123,
                    label="a string value",
                    password="a string value",
                    registration={"key": "value"},
                    username="a string value",
                )
            ],
            api_keys=[
                ImportExportApiKeysItem(
                    authorized_entities=["a string value"],
                    client_id="a string value",
                    client_name="a string value",
                    client_secret="a string value",
                    enabled=True,
                )
            ],
            config=GlobalConfig(
                alerts_emails=["admin@otoroshi.io"],
                alerts_webhooks=[
                    Webhook(
                        headers={"key": "value"},
                        url="http://www.google.com",
                    )
                ],
                analytics_webhooks=[
                    Webhook(
                        headers={"key": "value"},
                        url="http://www.google.com",
                    )
                ],
                api_read_only=True,
                auto_link_to_default_group=True,
                endless_ip_addresses=["192.192.192.192"],
                ip_filtering=IpFiltering(
                    blacklist=["192.192.192.192"],
                    whitelist=["192.192.192.192"],
                ),
                limit_concurrent_requests=True,
                max_concurrent_requests=123,
                per_ip_throttling_quota=123,
                stream_entity_only=True,
                throttling_quota=123,
                u2f_login_only=True,
                use_circuit_breakers=True,
            ),
            date=datetime.datetime.fromisoformat(
                "2017-07-21 17:32:28+00:00",
            ),
            date_raw=123,
            error_templates=[
                ImportExportErrorTemplatesItem(
                    messages={"key": "value"},
                    service_id="a string value",
                    template40x="a string value",
                    template50x="a string value",
                    template_build="a string value",
                    template_maintenance="a string value",
                )
            ],
            label="a string value",
            service_descriptors=[
                ImportExportServiceDescriptorsItem(
                    build_mode=True,
                    domain="a string value",
                    enabled=True,
                    enforce_secure_communication=True,
                    env="a string value",
                    force_https=True,
                    groups=["a string value"],
                    id="110e8400-e29b-11d4-a716-446655440000",
                    maintenance_mode=True,
                    name="a string value",
                    private_app=True,
                    root="a string value",
                    subdomain="a string value",
                    targets=[
                        Target(
                            host="www.google.com",
                            scheme="a string value",
                        )
                    ],
                )
            ],
            service_groups=[
                ImportExportServiceGroupsItem(
                    id="a string value",
                    name="a string value",
                )
            ],
            simple_admins=[
                ImportExportSimpleAdminsItem(
                    created_at=123,
                    label="a string value",
                    password="a string value",
                    username="a string value",
                )
            ],
            stats=ImportExportStats(
                calls=123,
                data_in=123,
                data_out=123,
            ),
        )
        """
        _response = self._raw_client.full_import(
            admins=admins,
            api_keys=api_keys,
            config=config,
            date=date,
            date_raw=date_raw,
            error_templates=error_templates,
            label=label,
            service_descriptors=service_descriptors,
            service_groups=service_groups,
            simple_admins=simple_admins,
            stats=stats,
            app_config=app_config,
            request_options=request_options,
        )
        return _response.data


class AsyncImportClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImportClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImportClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImportClient
        """
        return self._raw_client

    async def full_import_from_file(
        self,
        *,
        admins: typing.Sequence[ImportExportAdminsItem],
        api_keys: typing.Sequence[ImportExportApiKeysItem],
        config: GlobalConfig,
        date: dt.datetime,
        date_raw: int,
        error_templates: typing.Sequence[ImportExportErrorTemplatesItem],
        label: str,
        service_descriptors: typing.Sequence[ImportExportServiceDescriptorsItem],
        service_groups: typing.Sequence[ImportExportServiceGroupsItem],
        simple_admins: typing.Sequence[ImportExportSimpleAdminsItem],
        stats: ImportExportStats,
        app_config: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Done:
        """
        Import the full state of Otoroshi as a file

        Parameters
        ----------
        admins : typing.Sequence[ImportExportAdminsItem]
            Current U2F admin at the time of export

        api_keys : typing.Sequence[ImportExportApiKeysItem]
            Current apik keys at the time of export

        config : GlobalConfig
            Current global config at the time of export

        date : dt.datetime

        date_raw : int

        error_templates : typing.Sequence[ImportExportErrorTemplatesItem]
            Current error templates at the time of export

        label : str

        service_descriptors : typing.Sequence[ImportExportServiceDescriptorsItem]
            Current service descriptors at the time of export

        service_groups : typing.Sequence[ImportExportServiceGroupsItem]
            Current service groups at the time of export

        simple_admins : typing.Sequence[ImportExportSimpleAdminsItem]
            Current simple admins at the time of export

        stats : ImportExportStats
            Current global stats at the time of export

        app_config : typing.Optional[typing.Dict[str, str]]
            Current env variables at the time of export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            GlobalConfig,
            ImportExportAdminsItem,
            ImportExportApiKeysItem,
            ImportExportErrorTemplatesItem,
            ImportExportServiceDescriptorsItem,
            ImportExportServiceGroupsItem,
            ImportExportSimpleAdminsItem,
            ImportExportStats,
            IpFiltering,
            Target,
            Webhook,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.import_.full_import_from_file(
                admins=[
                    ImportExportAdminsItem(
                        created_at=123,
                        label="a string value",
                        password="a string value",
                        registration={"key": "value"},
                        username="a string value",
                    )
                ],
                api_keys=[
                    ImportExportApiKeysItem(
                        authorized_entities=["a string value"],
                        client_id="a string value",
                        client_name="a string value",
                        client_secret="a string value",
                        enabled=True,
                    )
                ],
                config=GlobalConfig(
                    alerts_emails=["admin@otoroshi.io"],
                    alerts_webhooks=[
                        Webhook(
                            headers={"key": "value"},
                            url="http://www.google.com",
                        )
                    ],
                    analytics_webhooks=[
                        Webhook(
                            headers={"key": "value"},
                            url="http://www.google.com",
                        )
                    ],
                    api_read_only=True,
                    auto_link_to_default_group=True,
                    endless_ip_addresses=["192.192.192.192"],
                    ip_filtering=IpFiltering(
                        blacklist=["192.192.192.192"],
                        whitelist=["192.192.192.192"],
                    ),
                    limit_concurrent_requests=True,
                    max_concurrent_requests=123,
                    per_ip_throttling_quota=123,
                    stream_entity_only=True,
                    throttling_quota=123,
                    u2f_login_only=True,
                    use_circuit_breakers=True,
                ),
                date=datetime.datetime.fromisoformat(
                    "2017-07-21 17:32:28+00:00",
                ),
                date_raw=123,
                error_templates=[
                    ImportExportErrorTemplatesItem(
                        messages={"key": "value"},
                        service_id="a string value",
                        template40x="a string value",
                        template50x="a string value",
                        template_build="a string value",
                        template_maintenance="a string value",
                    )
                ],
                label="a string value",
                service_descriptors=[
                    ImportExportServiceDescriptorsItem(
                        build_mode=True,
                        domain="a string value",
                        enabled=True,
                        enforce_secure_communication=True,
                        env="a string value",
                        force_https=True,
                        groups=["a string value"],
                        id="110e8400-e29b-11d4-a716-446655440000",
                        maintenance_mode=True,
                        name="a string value",
                        private_app=True,
                        root="a string value",
                        subdomain="a string value",
                        targets=[
                            Target(
                                host="www.google.com",
                                scheme="a string value",
                            )
                        ],
                    )
                ],
                service_groups=[
                    ImportExportServiceGroupsItem(
                        id="a string value",
                        name="a string value",
                    )
                ],
                simple_admins=[
                    ImportExportSimpleAdminsItem(
                        created_at=123,
                        label="a string value",
                        password="a string value",
                        username="a string value",
                    )
                ],
                stats=ImportExportStats(
                    calls=123,
                    data_in=123,
                    data_out=123,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.full_import_from_file(
            admins=admins,
            api_keys=api_keys,
            config=config,
            date=date,
            date_raw=date_raw,
            error_templates=error_templates,
            label=label,
            service_descriptors=service_descriptors,
            service_groups=service_groups,
            simple_admins=simple_admins,
            stats=stats,
            app_config=app_config,
            request_options=request_options,
        )
        return _response.data

    async def full_export(self, *, request_options: typing.Optional[RequestOptions] = None) -> ImportExport:
        """
        Export the full state of Otoroshi

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportExport
            Successful operation

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.import_.full_export()


        asyncio.run(main())
        """
        _response = await self._raw_client.full_export(request_options=request_options)
        return _response.data

    async def full_import(
        self,
        *,
        admins: typing.Sequence[ImportExportAdminsItem],
        api_keys: typing.Sequence[ImportExportApiKeysItem],
        config: GlobalConfig,
        date: dt.datetime,
        date_raw: int,
        error_templates: typing.Sequence[ImportExportErrorTemplatesItem],
        label: str,
        service_descriptors: typing.Sequence[ImportExportServiceDescriptorsItem],
        service_groups: typing.Sequence[ImportExportServiceGroupsItem],
        simple_admins: typing.Sequence[ImportExportSimpleAdminsItem],
        stats: ImportExportStats,
        app_config: typing.Optional[typing.Dict[str, str]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Done:
        """
        Import the full state of Otoroshi

        Parameters
        ----------
        admins : typing.Sequence[ImportExportAdminsItem]
            Current U2F admin at the time of export

        api_keys : typing.Sequence[ImportExportApiKeysItem]
            Current apik keys at the time of export

        config : GlobalConfig
            Current global config at the time of export

        date : dt.datetime

        date_raw : int

        error_templates : typing.Sequence[ImportExportErrorTemplatesItem]
            Current error templates at the time of export

        label : str

        service_descriptors : typing.Sequence[ImportExportServiceDescriptorsItem]
            Current service descriptors at the time of export

        service_groups : typing.Sequence[ImportExportServiceGroupsItem]
            Current service groups at the time of export

        simple_admins : typing.Sequence[ImportExportSimpleAdminsItem]
            Current simple admins at the time of export

        stats : ImportExportStats
            Current global stats at the time of export

        app_config : typing.Optional[typing.Dict[str, str]]
            Current env variables at the time of export

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Done
            Successful operation

        Examples
        --------
        import asyncio
        import datetime

        from fern import (
            AsyncFernApi,
            GlobalConfig,
            ImportExportAdminsItem,
            ImportExportApiKeysItem,
            ImportExportErrorTemplatesItem,
            ImportExportServiceDescriptorsItem,
            ImportExportServiceGroupsItem,
            ImportExportSimpleAdminsItem,
            ImportExportStats,
            IpFiltering,
            Target,
            Webhook,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.import_.full_import(
                admins=[
                    ImportExportAdminsItem(
                        created_at=123,
                        label="a string value",
                        password="a string value",
                        registration={"key": "value"},
                        username="a string value",
                    )
                ],
                api_keys=[
                    ImportExportApiKeysItem(
                        authorized_entities=["a string value"],
                        client_id="a string value",
                        client_name="a string value",
                        client_secret="a string value",
                        enabled=True,
                    )
                ],
                config=GlobalConfig(
                    alerts_emails=["admin@otoroshi.io"],
                    alerts_webhooks=[
                        Webhook(
                            headers={"key": "value"},
                            url="http://www.google.com",
                        )
                    ],
                    analytics_webhooks=[
                        Webhook(
                            headers={"key": "value"},
                            url="http://www.google.com",
                        )
                    ],
                    api_read_only=True,
                    auto_link_to_default_group=True,
                    endless_ip_addresses=["192.192.192.192"],
                    ip_filtering=IpFiltering(
                        blacklist=["192.192.192.192"],
                        whitelist=["192.192.192.192"],
                    ),
                    limit_concurrent_requests=True,
                    max_concurrent_requests=123,
                    per_ip_throttling_quota=123,
                    stream_entity_only=True,
                    throttling_quota=123,
                    u2f_login_only=True,
                    use_circuit_breakers=True,
                ),
                date=datetime.datetime.fromisoformat(
                    "2017-07-21 17:32:28+00:00",
                ),
                date_raw=123,
                error_templates=[
                    ImportExportErrorTemplatesItem(
                        messages={"key": "value"},
                        service_id="a string value",
                        template40x="a string value",
                        template50x="a string value",
                        template_build="a string value",
                        template_maintenance="a string value",
                    )
                ],
                label="a string value",
                service_descriptors=[
                    ImportExportServiceDescriptorsItem(
                        build_mode=True,
                        domain="a string value",
                        enabled=True,
                        enforce_secure_communication=True,
                        env="a string value",
                        force_https=True,
                        groups=["a string value"],
                        id="110e8400-e29b-11d4-a716-446655440000",
                        maintenance_mode=True,
                        name="a string value",
                        private_app=True,
                        root="a string value",
                        subdomain="a string value",
                        targets=[
                            Target(
                                host="www.google.com",
                                scheme="a string value",
                            )
                        ],
                    )
                ],
                service_groups=[
                    ImportExportServiceGroupsItem(
                        id="a string value",
                        name="a string value",
                    )
                ],
                simple_admins=[
                    ImportExportSimpleAdminsItem(
                        created_at=123,
                        label="a string value",
                        password="a string value",
                        username="a string value",
                    )
                ],
                stats=ImportExportStats(
                    calls=123,
                    data_in=123,
                    data_out=123,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.full_import(
            admins=admins,
            api_keys=api_keys,
            config=config,
            date=date,
            date_raw=date_raw,
            error_templates=error_templates,
            label=label,
            service_descriptors=service_descriptors,
            service_groups=service_groups,
            simple_admins=simple_admins,
            stats=stats,
            app_config=app_config,
            request_options=request_options,
        )
        return _response.data
