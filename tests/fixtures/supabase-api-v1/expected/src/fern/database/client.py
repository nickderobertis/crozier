

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_role_response_output import CreateRoleResponseOutput
from ..types.delete_roles_response_output import DeleteRolesResponseOutput
from ..types.get_project_db_metadata_response_output import GetProjectDbMetadataResponseOutput
from ..types.invite_external_user_jit_response_output import InviteExternalUserJitResponseOutput
from ..types.jit_access_response_output import JitAccessResponseOutput
from ..types.jit_authorize_access_response_output import JitAuthorizeAccessResponseOutput
from ..types.jit_list_access_response_output import JitListAccessResponseOutput
from ..types.postgres_config_response_output import PostgresConfigResponseOutput
from ..types.read_only_status_response_output import ReadOnlyStatusResponseOutput
from ..types.snippet_list_output import SnippetListOutput
from ..types.snippet_response_output import SnippetResponseOutput
from ..types.ssl_enforcement_response_output import SslEnforcementResponseOutput
from ..types.supavisor_config_response_output import SupavisorConfigResponseOutput
from ..types.typescript_response_output import TypescriptResponseOutput
from ..types.update_supavisor_config_response_output import UpdateSupavisorConfigResponseOutput
from ..types.v1backup_schedule_response_output import V1BackupScheduleResponseOutput
from ..types.v1backups_response_output import V1BackupsResponseOutput
from ..types.v1get_migration_response_output import V1GetMigrationResponseOutput
from ..types.v1list_migrations_response_output import V1ListMigrationsResponseOutput
from ..types.v1pgbouncer_config_response_output import V1PgbouncerConfigResponseOutput
from ..types.v1restore_point_response import V1RestorePointResponse
from ..types.v1update_password_response_output import V1UpdatePasswordResponseOutput
from .raw_client import AsyncRawDatabaseClient, RawDatabaseClient
from .types.invite_external_user_jit_access_body_roles_item import InviteExternalUserJitAccessBodyRolesItem
from .types.jit_access_request_request_state import JitAccessRequestRequestState
from .types.set_up_read_replica_body_read_replica_region import SetUpReadReplicaBodyReadReplicaRegion
from .types.ssl_enforcement_request_requested_config import SslEnforcementRequestRequestedConfig
from .types.update_jit_access_body_roles_item import UpdateJitAccessBodyRolesItem
from .types.update_postgres_config_body_session_replication_role import UpdatePostgresConfigBodySessionReplicationRole
from .types.update_supavisor_config_body_pool_mode import UpdateSupavisorConfigBodyPoolMode
from .types.v1get_jit_access_config_response import V1GetJitAccessConfigResponse
from .types.v1list_all_snippets_request_sort_by import V1ListAllSnippetsRequestSortBy
from .types.v1list_all_snippets_request_sort_order import V1ListAllSnippetsRequestSortOrder
from .types.v1update_jit_access_config_response import V1UpdateJitAccessConfigResponse


OMIT = typing.cast(typing.Any, ...)


class DatabaseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDatabaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDatabaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDatabaseClient
        """
        return self._raw_client

    def v1list_all_snippets(
        self,
        *,
        project_ref: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        sort_by: typing.Optional[V1ListAllSnippetsRequestSortBy] = None,
        sort_order: typing.Optional[V1ListAllSnippetsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnippetListOutput:
        """
        Parameters
        ----------
        project_ref : typing.Optional[str]
            Project ref

        cursor : typing.Optional[str]

        limit : typing.Optional[str]

        sort_by : typing.Optional[V1ListAllSnippetsRequestSortBy]

        sort_order : typing.Optional[V1ListAllSnippetsRequestSortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnippetListOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1list_all_snippets(
            project_ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_all_snippets(
            project_ref=project_ref,
            cursor=cursor,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    def v1get_a_snippet(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SnippetResponseOutput:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnippetResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_a_snippet(
            id="44444444-4444-4444-8444-444444444444",
        )
        """
        _response = self._raw_client.v1get_a_snippet(id, request_options=request_options)
        return _response.data

    def v1get_jit_access_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1GetJitAccessConfigResponse:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1GetJitAccessConfigResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_jit_access_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_jit_access_config(ref, request_options=request_options)
        return _response.data

    def v1update_jit_access_config(
        self, ref: str, *, state: JitAccessRequestRequestState, request_options: typing.Optional[RequestOptions] = None
    ) -> V1UpdateJitAccessConfigResponse:
        """
        Parameters
        ----------
        ref : str
            Project ref

        state : JitAccessRequestRequestState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1UpdateJitAccessConfigResponse


        Examples
        --------
        from fern.database import JitAccessRequestRequestState

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1update_jit_access_config(
            ref="abcdefghijklmnopqrst",
            state=JitAccessRequestRequestState.ENABLED,
        )
        """
        _response = self._raw_client.v1update_jit_access_config(ref, state=state, request_options=request_options)
        return _response.data

    def v1get_ssl_enforcement_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SslEnforcementResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SslEnforcementResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_ssl_enforcement_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_ssl_enforcement_config(ref, request_options=request_options)
        return _response.data

    def v1update_ssl_enforcement_config(
        self,
        ref: str,
        *,
        requested_config: SslEnforcementRequestRequestedConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SslEnforcementResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        requested_config : SslEnforcementRequestRequestedConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SslEnforcementResponseOutput


        Examples
        --------
        from fern.database import SslEnforcementRequestRequestedConfig

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1update_ssl_enforcement_config(
            ref="abcdefghijklmnopqrst",
            requested_config=SslEnforcementRequestRequestedConfig(
                database=True,
            ),
        )
        """
        _response = self._raw_client.v1update_ssl_enforcement_config(
            ref, requested_config=requested_config, request_options=request_options
        )
        return _response.data

    def v1generate_typescript_types(
        self,
        ref: str,
        *,
        included_schemas: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TypescriptResponseOutput:
        """
        Returns the TypeScript types of your schema for use with supabase-js.

        Parameters
        ----------
        ref : str
            Project ref

        included_schemas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TypescriptResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1generate_typescript_types(
            ref="abcdefghijklmnopqrst",
            included_schemas="public,auth",
        )
        """
        _response = self._raw_client.v1generate_typescript_types(
            ref, included_schemas=included_schemas, request_options=request_options
        )
        return _response.data

    def v1get_readonly_mode_status(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReadOnlyStatusResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadOnlyStatusResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_readonly_mode_status(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_readonly_mode_status(ref, request_options=request_options)
        return _response.data

    def v1disable_readonly_mode_temporarily(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1disable_readonly_mode_temporarily(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1disable_readonly_mode_temporarily(ref, request_options=request_options)
        return _response.data

    def v1setup_a_read_replica(
        self,
        ref: str,
        *,
        read_replica_region: SetUpReadReplicaBodyReadReplicaRegion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        read_replica_region : SetUpReadReplicaBodyReadReplicaRegion
            Region you want your read replica to reside in

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern.database import SetUpReadReplicaBodyReadReplicaRegion

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1setup_a_read_replica(
            ref="abcdefghijklmnopqrst",
            read_replica_region=SetUpReadReplicaBodyReadReplicaRegion.US_WEST1,
        )
        """
        _response = self._raw_client.v1setup_a_read_replica(
            ref, read_replica_region=read_replica_region, request_options=request_options
        )
        return _response.data

    def v1remove_a_read_replica(
        self, ref: str, *, database_identifier: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        database_identifier : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1remove_a_read_replica(
            ref="abcdefghijklmnopqrst",
            database_identifier="abcdefghijklmnopqrst-rr-us-west-1-abcde",
        )
        """
        _response = self._raw_client.v1remove_a_read_replica(
            ref, database_identifier=database_identifier, request_options=request_options
        )
        return _response.data

    def v1create_login_role(
        self, ref: str, *, read_only: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateRoleResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        read_only : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRoleResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1create_login_role(
            ref="abcdefghijklmnopqrst",
            read_only=True,
        )
        """
        _response = self._raw_client.v1create_login_role(ref, read_only=read_only, request_options=request_options)
        return _response.data

    def v1delete_login_roles(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteRolesResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRolesResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1delete_login_roles(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1delete_login_roles(ref, request_options=request_options)
        return _response.data

    def v1list_migration_history(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ListMigrationsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ListMigrationsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1list_migration_history(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_migration_history(ref, request_options=request_options)
        return _response.data

    def v1apply_a_migration(
        self,
        ref: str,
        *,
        query: str,
        idempotency_key: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        rollback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        query : str

        idempotency_key : typing.Optional[str]
            A unique key to ensure the same migration is tracked only once.

        name : typing.Optional[str]

        rollback : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1apply_a_migration(
            ref="abcdefghijklmnopqrst",
            query="create table public.widgets(id bigint primary key);",
            name="create_widgets_table",
            rollback="drop table if exists public.widgets;",
        )
        """
        _response = self._raw_client.v1apply_a_migration(
            ref,
            query=query,
            idempotency_key=idempotency_key,
            name=name,
            rollback=rollback,
            request_options=request_options,
        )
        return _response.data

    def v1upsert_a_migration(
        self,
        ref: str,
        *,
        query: str,
        idempotency_key: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        rollback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        query : str

        idempotency_key : typing.Optional[str]
            A unique key to ensure the same migration is tracked only once.

        name : typing.Optional[str]

        rollback : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1upsert_a_migration(
            ref="abcdefghijklmnopqrst",
            query="create table public.widgets(id bigint primary key);",
            name="create_widgets_table",
            rollback="drop table if exists public.widgets;",
        )
        """
        _response = self._raw_client.v1upsert_a_migration(
            ref,
            query=query,
            idempotency_key=idempotency_key,
            name=name,
            rollback=rollback,
            request_options=request_options,
        )
        return _response.data

    def v1rollback_migrations(
        self, ref: str, *, gte: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        gte : str
            Rollback migrations greater or equal to this version

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1rollback_migrations(
            ref="abcdefghijklmnopqrst",
            gte="20250312000000",
        )
        """
        _response = self._raw_client.v1rollback_migrations(ref, gte=gte, request_options=request_options)
        return _response.data

    def v1get_a_migration(
        self, ref: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1GetMigrationResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1GetMigrationResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_a_migration(
            ref="abcdefghijklmnopqrst",
            version="20250312000000",
        )
        """
        _response = self._raw_client.v1get_a_migration(ref, version, request_options=request_options)
        return _response.data

    def v1patch_a_migration(
        self,
        ref: str,
        version: str,
        *,
        name: typing.Optional[str] = OMIT,
        rollback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        version : str

        name : typing.Optional[str]

        rollback : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1patch_a_migration(
            ref="abcdefghijklmnopqrst",
            version="20250312000000",
            name="create_widgets_table",
            rollback="drop table if exists public.widgets;",
        )
        """
        _response = self._raw_client.v1patch_a_migration(
            ref, version, name=name, rollback=rollback, request_options=request_options
        )
        return _response.data

    def v1run_a_query(
        self,
        ref: str,
        *,
        query: str,
        parameters: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        query : str

        parameters : typing.Optional[typing.Sequence[typing.Any]]

        read_only : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1run_a_query(
            ref="abcdefghijklmnopqrst",
            query="select * from pg_stat_activity limit 1;",
            read_only=True,
        )
        """
        _response = self._raw_client.v1run_a_query(
            ref, query=query, parameters=parameters, read_only=read_only, request_options=request_options
        )
        return _response.data

    def v1read_only_query(
        self,
        ref: str,
        *,
        query: str,
        parameters: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        All entity references must be schema qualified.

        Parameters
        ----------
        ref : str
            Project ref

        query : str

        parameters : typing.Optional[typing.Sequence[typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1read_only_query(
            ref="abcdefghijklmnopqrst",
            query="select * from pg_stat_activity limit 1;",
        )
        """
        _response = self._raw_client.v1read_only_query(
            ref, query=query, parameters=parameters, request_options=request_options
        )
        return _response.data

    def v1enable_database_webhook(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1enable_database_webhook(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1enable_database_webhook(ref, request_options=request_options)
        return _response.data

    def v1get_database_metadata(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectDbMetadataResponseOutput:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectDbMetadataResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_database_metadata(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_database_metadata(ref, request_options=request_options)
        return _response.data

    def v1update_database_password(
        self, ref: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V1UpdatePasswordResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1UpdatePasswordResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1update_database_password(
            ref="abcdefghijklmnopqrst",
            password="correct-horse-battery-staple",
        )
        """
        _response = self._raw_client.v1update_database_password(ref, password=password, request_options=request_options)
        return _response.data

    def v1get_jit_access(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JitAccessResponseOutput:
        """
        Mappings of roles a user can assume in the project database

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitAccessResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_jit_access(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_jit_access(ref, request_options=request_options)
        return _response.data

    def v1authorize_jit_access(
        self, ref: str, *, role: str, rhost: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JitAuthorizeAccessResponseOutput:
        """
        Authorizes the request to assume a role in the project database

        Parameters
        ----------
        ref : str
            Project ref

        role : str

        rhost : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitAuthorizeAccessResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1authorize_jit_access(
            ref="abcdefghijklmnopqrst",
            role="postgres",
            rhost="203.0.113.10",
        )
        """
        _response = self._raw_client.v1authorize_jit_access(
            ref, role=role, rhost=rhost, request_options=request_options
        )
        return _response.data

    def v1update_jit_access(
        self,
        ref: str,
        *,
        user_id: str,
        roles: typing.Sequence[UpdateJitAccessBodyRolesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JitAccessResponseOutput:
        """
        Modifies the roles that can be assumed and for how long

        Parameters
        ----------
        ref : str
            Project ref

        user_id : str

        roles : typing.Sequence[UpdateJitAccessBodyRolesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitAccessResponseOutput


        Examples
        --------
        from fern.database import (
            UpdateJitAccessBodyRolesItem,
            UpdateJitAccessBodyRolesItemAllowedNetworks,
            UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1update_jit_access(
            ref="abcdefghijklmnopqrst",
            user_id="55555555-5555-4555-8555-555555555555",
            roles=[
                UpdateJitAccessBodyRolesItem(
                    role="postgres",
                    expires_at=1740787200.0,
                    allowed_networks=UpdateJitAccessBodyRolesItemAllowedNetworks(
                        allowed_cidrs=[
                            UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem(
                                cidr="203.0.113.0/24",
                            )
                        ],
                    ),
                    branches_only=False,
                )
            ],
        )
        """
        _response = self._raw_client.v1update_jit_access(
            ref, user_id=user_id, roles=roles, request_options=request_options
        )
        return _response.data

    def v1list_jit_access(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JitListAccessResponseOutput:
        """
        Mappings of roles a user can assume in the project database

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitListAccessResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1list_jit_access(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_jit_access(ref, request_options=request_options)
        return _response.data

    def v1invite_external_jit_access(
        self,
        ref: str,
        *,
        email: str,
        roles: typing.Sequence[InviteExternalUserJitAccessBodyRolesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteExternalUserJitResponseOutput:
        """
        Invites the external user and sets initial roles that can be assumed and for how long

        Parameters
        ----------
        ref : str
            Project ref

        email : str

        roles : typing.Sequence[InviteExternalUserJitAccessBodyRolesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteExternalUserJitResponseOutput


        Examples
        --------
        from fern.database import (
            InviteExternalUserJitAccessBodyRolesItem,
            InviteExternalUserJitAccessBodyRolesItemAllowedNetworks,
            InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
        )

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1invite_external_jit_access(
            ref="abcdefghijklmnopqrst",
            email="external-user@somedomain.xyz",
            roles=[
                InviteExternalUserJitAccessBodyRolesItem(
                    role="postgres",
                    expires_at=1740787200.0,
                    allowed_networks=InviteExternalUserJitAccessBodyRolesItemAllowedNetworks(
                        allowed_cidrs=[
                            InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem(
                                cidr="203.0.113.0/24",
                            )
                        ],
                    ),
                    branches_only=False,
                )
            ],
        )
        """
        _response = self._raw_client.v1invite_external_jit_access(
            ref, email=email, roles=roles, request_options=request_options
        )
        return _response.data

    def v1accept_invite_external_jit_access(
        self, ref: str, *, email: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JitAccessResponseOutput:
        """
        Accepts the invitation to JIT database access

        Parameters
        ----------
        ref : str
            Project ref

        email : str

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitAccessResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1accept_invite_external_jit_access(
            ref="abcdefghijklmnopqrst",
            email="external-user@somedomain.xyz",
            token="",
        )
        """
        _response = self._raw_client.v1accept_invite_external_jit_access(
            ref, email=email, token=token, request_options=request_options
        )
        return _response.data

    def v1delete_invite_external_jit_access(
        self, ref: str, invite_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Revokes and deletes the invitation

        Parameters
        ----------
        ref : str
            Project ref

        invite_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1delete_invite_external_jit_access(
            ref="abcdefghijklmnopqrst",
            invite_id="55555555-5555-4555-8555-555555555555",
        )
        """
        _response = self._raw_client.v1delete_invite_external_jit_access(
            ref, invite_id, request_options=request_options
        )
        return _response.data

    def v1delete_jit_access(
        self, ref: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove JIT mappings of a user, revoking all JIT database access

        Parameters
        ----------
        ref : str
            Project ref

        user_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1delete_jit_access(
            ref="abcdefghijklmnopqrst",
            user_id="55555555-5555-4555-8555-555555555555",
        )
        """
        _response = self._raw_client.v1delete_jit_access(ref, user_id, request_options=request_options)
        return _response.data

    def v1get_database_openapi(
        self, ref: str, *, schema: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the PostgREST OpenAPI specification for the project. This is the replacement for querying `/rest/v1/` directly with the anon key.

        Parameters
        ----------
        ref : str
            Project ref

        schema : typing.Optional[str]
            The database schema to generate the OpenAPI spec for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_database_openapi(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_database_openapi(ref, schema=schema, request_options=request_options)
        return _response.data

    def v1get_project_pgbouncer_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1PgbouncerConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1PgbouncerConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_project_pgbouncer_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_project_pgbouncer_config(ref, request_options=request_options)
        return _response.data

    def v1get_pooler_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SupavisorConfigResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SupavisorConfigResponseOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_pooler_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_pooler_config(ref, request_options=request_options)
        return _response.data

    def v1update_pooler_config(
        self,
        ref: str,
        *,
        default_pool_size: typing.Optional[int] = OMIT,
        pool_mode: typing.Optional[UpdateSupavisorConfigBodyPoolMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSupavisorConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        default_pool_size : typing.Optional[int]

        pool_mode : typing.Optional[UpdateSupavisorConfigBodyPoolMode]
            Dedicated pooler mode for the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSupavisorConfigResponseOutput


        Examples
        --------
        from fern.database import UpdateSupavisorConfigBodyPoolMode

        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1update_pooler_config(
            ref="abcdefghijklmnopqrst",
            default_pool_size=25,
            pool_mode=UpdateSupavisorConfigBodyPoolMode.TRANSACTION,
        )
        """
        _response = self._raw_client.v1update_pooler_config(
            ref, default_pool_size=default_pool_size, pool_mode=pool_mode, request_options=request_options
        )
        return _response.data

    def v1get_postgres_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostgresConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostgresConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_postgres_config(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_postgres_config(ref, request_options=request_options)
        return _response.data

    def v1update_postgres_config(
        self,
        ref: str,
        *,
        effective_cache_size: typing.Optional[str] = OMIT,
        logical_decoding_work_mem: typing.Optional[str] = OMIT,
        cron_log_statement: typing.Optional[bool] = OMIT,
        log_autovacuum_min_duration: typing.Optional[str] = OMIT,
        log_checkpoints: typing.Optional[bool] = OMIT,
        log_connections: typing.Optional[bool] = OMIT,
        log_disconnections: typing.Optional[bool] = OMIT,
        log_duration: typing.Optional[bool] = OMIT,
        log_lock_waits: typing.Optional[bool] = OMIT,
        log_recovery_conflict_waits: typing.Optional[bool] = OMIT,
        log_replication_commands: typing.Optional[bool] = OMIT,
        log_startup_progress_interval: typing.Optional[str] = OMIT,
        log_temp_files: typing.Optional[str] = OMIT,
        maintenance_work_mem: typing.Optional[str] = OMIT,
        track_activity_query_size: typing.Optional[str] = OMIT,
        max_connections: typing.Optional[int] = OMIT,
        max_locks_per_transaction: typing.Optional[int] = OMIT,
        max_logical_replication_workers: typing.Optional[int] = OMIT,
        max_parallel_maintenance_workers: typing.Optional[int] = OMIT,
        max_parallel_workers: typing.Optional[int] = OMIT,
        max_parallel_workers_per_gather: typing.Optional[int] = OMIT,
        max_replication_slots: typing.Optional[int] = OMIT,
        max_slot_wal_keep_size: typing.Optional[str] = OMIT,
        max_standby_archive_delay: typing.Optional[str] = OMIT,
        max_standby_streaming_delay: typing.Optional[str] = OMIT,
        max_sync_workers_per_subscription: typing.Optional[int] = OMIT,
        max_wal_size: typing.Optional[str] = OMIT,
        max_wal_senders: typing.Optional[int] = OMIT,
        max_worker_processes: typing.Optional[int] = OMIT,
        session_replication_role: typing.Optional[UpdatePostgresConfigBodySessionReplicationRole] = OMIT,
        shared_buffers: typing.Optional[str] = OMIT,
        statement_timeout: typing.Optional[str] = OMIT,
        track_commit_timestamp: typing.Optional[bool] = OMIT,
        wal_keep_size: typing.Optional[str] = OMIT,
        wal_sender_timeout: typing.Optional[str] = OMIT,
        work_mem: typing.Optional[str] = OMIT,
        checkpoint_timeout: typing.Optional[str] = OMIT,
        hot_standby_feedback: typing.Optional[bool] = OMIT,
        restart_database: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostgresConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        effective_cache_size : typing.Optional[str]

        logical_decoding_work_mem : typing.Optional[str]

        cron_log_statement : typing.Optional[bool]

        log_autovacuum_min_duration : typing.Optional[str]
            Default unit: ms

        log_checkpoints : typing.Optional[bool]

        log_connections : typing.Optional[bool]

        log_disconnections : typing.Optional[bool]

        log_duration : typing.Optional[bool]

        log_lock_waits : typing.Optional[bool]

        log_recovery_conflict_waits : typing.Optional[bool]

        log_replication_commands : typing.Optional[bool]

        log_startup_progress_interval : typing.Optional[str]
            Default unit: ms

        log_temp_files : typing.Optional[str]

        maintenance_work_mem : typing.Optional[str]

        track_activity_query_size : typing.Optional[str]

        max_connections : typing.Optional[int]

        max_locks_per_transaction : typing.Optional[int]

        max_logical_replication_workers : typing.Optional[int]

        max_parallel_maintenance_workers : typing.Optional[int]

        max_parallel_workers : typing.Optional[int]

        max_parallel_workers_per_gather : typing.Optional[int]

        max_replication_slots : typing.Optional[int]

        max_slot_wal_keep_size : typing.Optional[str]

        max_standby_archive_delay : typing.Optional[str]

        max_standby_streaming_delay : typing.Optional[str]

        max_sync_workers_per_subscription : typing.Optional[int]

        max_wal_size : typing.Optional[str]

        max_wal_senders : typing.Optional[int]

        max_worker_processes : typing.Optional[int]

        session_replication_role : typing.Optional[UpdatePostgresConfigBodySessionReplicationRole]

        shared_buffers : typing.Optional[str]

        statement_timeout : typing.Optional[str]
            Default unit: ms

        track_commit_timestamp : typing.Optional[bool]

        wal_keep_size : typing.Optional[str]

        wal_sender_timeout : typing.Optional[str]
            Default unit: ms

        work_mem : typing.Optional[str]

        checkpoint_timeout : typing.Optional[str]
            Default unit: s

        hot_standby_feedback : typing.Optional[bool]

        restart_database : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostgresConfigResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1update_postgres_config(
            ref="abcdefghijklmnopqrst",
            max_connections=120,
            shared_buffers="256MB",
            statement_timeout="60000ms",
            work_mem="4MB",
        )
        """
        _response = self._raw_client.v1update_postgres_config(
            ref,
            effective_cache_size=effective_cache_size,
            logical_decoding_work_mem=logical_decoding_work_mem,
            cron_log_statement=cron_log_statement,
            log_autovacuum_min_duration=log_autovacuum_min_duration,
            log_checkpoints=log_checkpoints,
            log_connections=log_connections,
            log_disconnections=log_disconnections,
            log_duration=log_duration,
            log_lock_waits=log_lock_waits,
            log_recovery_conflict_waits=log_recovery_conflict_waits,
            log_replication_commands=log_replication_commands,
            log_startup_progress_interval=log_startup_progress_interval,
            log_temp_files=log_temp_files,
            maintenance_work_mem=maintenance_work_mem,
            track_activity_query_size=track_activity_query_size,
            max_connections=max_connections,
            max_locks_per_transaction=max_locks_per_transaction,
            max_logical_replication_workers=max_logical_replication_workers,
            max_parallel_maintenance_workers=max_parallel_maintenance_workers,
            max_parallel_workers=max_parallel_workers,
            max_parallel_workers_per_gather=max_parallel_workers_per_gather,
            max_replication_slots=max_replication_slots,
            max_slot_wal_keep_size=max_slot_wal_keep_size,
            max_standby_archive_delay=max_standby_archive_delay,
            max_standby_streaming_delay=max_standby_streaming_delay,
            max_sync_workers_per_subscription=max_sync_workers_per_subscription,
            max_wal_size=max_wal_size,
            max_wal_senders=max_wal_senders,
            max_worker_processes=max_worker_processes,
            session_replication_role=session_replication_role,
            shared_buffers=shared_buffers,
            statement_timeout=statement_timeout,
            track_commit_timestamp=track_commit_timestamp,
            wal_keep_size=wal_keep_size,
            wal_sender_timeout=wal_sender_timeout,
            work_mem=work_mem,
            checkpoint_timeout=checkpoint_timeout,
            hot_standby_feedback=hot_standby_feedback,
            restart_database=restart_database,
            request_options=request_options,
        )
        return _response.data

    def v1list_all_backups(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1BackupsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BackupsResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1list_all_backups(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_all_backups(ref, request_options=request_options)
        return _response.data

    def v1restore_pitr_backup(
        self, ref: str, *, recovery_time_target_unix: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        recovery_time_target_unix : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1restore_pitr_backup(
            ref="abcdefghijklmnopqrst",
            recovery_time_target_unix=1740787200,
        )
        """
        _response = self._raw_client.v1restore_pitr_backup(
            ref, recovery_time_target_unix=recovery_time_target_unix, request_options=request_options
        )
        return _response.data

    def v1get_restore_point(
        self, ref: str, *, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> V1RestorePointResponse:
        """
        Parameters
        ----------
        ref : str
            Project ref

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1RestorePointResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_restore_point(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_restore_point(ref, name=name, request_options=request_options)
        return _response.data

    def v1create_restore_point(
        self, ref: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V1RestorePointResponse:
        """
        Parameters
        ----------
        ref : str
            Project ref

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1RestorePointResponse


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1create_restore_point(
            ref="abcdefghijklmnopqrst",
            name="before-upgrade",
        )
        """
        _response = self._raw_client.v1create_restore_point(ref, name=name, request_options=request_options)
        return _response.data

    def v1restore_physical_backup(
        self, ref: str, *, id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1restore_physical_backup(
            ref="abcdefghijklmnopqrst",
            id=12345,
        )
        """
        _response = self._raw_client.v1restore_physical_backup(ref, id=id, request_options=request_options)
        return _response.data

    def v1get_backup_schedule(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1BackupScheduleResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BackupScheduleResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1get_backup_schedule(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1get_backup_schedule(ref, request_options=request_options)
        return _response.data

    def v1update_backup_schedule(
        self, ref: str, *, schedule_for: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V1BackupScheduleResponseOutput:
        """
        Sets the time at which the daily backup runs. The change takes effect on the next backup window that includes the new time. If the new time has already passed for today, the first backup at the new time will occur the following day. It can only be updated 3 times per 24 hours.

        Parameters
        ----------
        ref : str
            Project ref

        schedule_for : str
            Time of day to schedule daily backups, in UTC. Format: HH:MM:SS.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BackupScheduleResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1update_backup_schedule(
            ref="abcdefghijklmnopqrst",
            schedule_for="04:00:00",
        )
        """
        _response = self._raw_client.v1update_backup_schedule(
            ref, schedule_for=schedule_for, request_options=request_options
        )
        return _response.data

    def v1undo(self, ref: str, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.database.v1undo(
            ref="abcdefghijklmnopqrst",
            name="before-upgrade",
        )
        """
        _response = self._raw_client.v1undo(ref, name=name, request_options=request_options)
        return _response.data


class AsyncDatabaseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDatabaseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDatabaseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDatabaseClient
        """
        return self._raw_client

    async def v1list_all_snippets(
        self,
        *,
        project_ref: typing.Optional[str] = None,
        cursor: typing.Optional[str] = None,
        limit: typing.Optional[str] = None,
        sort_by: typing.Optional[V1ListAllSnippetsRequestSortBy] = None,
        sort_order: typing.Optional[V1ListAllSnippetsRequestSortOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SnippetListOutput:
        """
        Parameters
        ----------
        project_ref : typing.Optional[str]
            Project ref

        cursor : typing.Optional[str]

        limit : typing.Optional[str]

        sort_by : typing.Optional[V1ListAllSnippetsRequestSortBy]

        sort_order : typing.Optional[V1ListAllSnippetsRequestSortOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnippetListOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1list_all_snippets(
                project_ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_snippets(
            project_ref=project_ref,
            cursor=cursor,
            limit=limit,
            sort_by=sort_by,
            sort_order=sort_order,
            request_options=request_options,
        )
        return _response.data

    async def v1get_a_snippet(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SnippetResponseOutput:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SnippetResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_a_snippet(
                id="44444444-4444-4444-8444-444444444444",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_a_snippet(id, request_options=request_options)
        return _response.data

    async def v1get_jit_access_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1GetJitAccessConfigResponse:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1GetJitAccessConfigResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_jit_access_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_jit_access_config(ref, request_options=request_options)
        return _response.data

    async def v1update_jit_access_config(
        self, ref: str, *, state: JitAccessRequestRequestState, request_options: typing.Optional[RequestOptions] = None
    ) -> V1UpdateJitAccessConfigResponse:
        """
        Parameters
        ----------
        ref : str
            Project ref

        state : JitAccessRequestRequestState

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1UpdateJitAccessConfigResponse


        Examples
        --------
        import asyncio

        from fern.database import JitAccessRequestRequestState

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1update_jit_access_config(
                ref="abcdefghijklmnopqrst",
                state=JitAccessRequestRequestState.ENABLED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_jit_access_config(ref, state=state, request_options=request_options)
        return _response.data

    async def v1get_ssl_enforcement_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> SslEnforcementResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SslEnforcementResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_ssl_enforcement_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_ssl_enforcement_config(ref, request_options=request_options)
        return _response.data

    async def v1update_ssl_enforcement_config(
        self,
        ref: str,
        *,
        requested_config: SslEnforcementRequestRequestedConfig,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SslEnforcementResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        requested_config : SslEnforcementRequestRequestedConfig

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SslEnforcementResponseOutput


        Examples
        --------
        import asyncio

        from fern.database import SslEnforcementRequestRequestedConfig

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1update_ssl_enforcement_config(
                ref="abcdefghijklmnopqrst",
                requested_config=SslEnforcementRequestRequestedConfig(
                    database=True,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_ssl_enforcement_config(
            ref, requested_config=requested_config, request_options=request_options
        )
        return _response.data

    async def v1generate_typescript_types(
        self,
        ref: str,
        *,
        included_schemas: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> TypescriptResponseOutput:
        """
        Returns the TypeScript types of your schema for use with supabase-js.

        Parameters
        ----------
        ref : str
            Project ref

        included_schemas : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TypescriptResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1generate_typescript_types(
                ref="abcdefghijklmnopqrst",
                included_schemas="public,auth",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1generate_typescript_types(
            ref, included_schemas=included_schemas, request_options=request_options
        )
        return _response.data

    async def v1get_readonly_mode_status(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ReadOnlyStatusResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReadOnlyStatusResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_readonly_mode_status(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_readonly_mode_status(ref, request_options=request_options)
        return _response.data

    async def v1disable_readonly_mode_temporarily(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1disable_readonly_mode_temporarily(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1disable_readonly_mode_temporarily(ref, request_options=request_options)
        return _response.data

    async def v1setup_a_read_replica(
        self,
        ref: str,
        *,
        read_replica_region: SetUpReadReplicaBodyReadReplicaRegion,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        read_replica_region : SetUpReadReplicaBodyReadReplicaRegion
            Region you want your read replica to reside in

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern.database import SetUpReadReplicaBodyReadReplicaRegion

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1setup_a_read_replica(
                ref="abcdefghijklmnopqrst",
                read_replica_region=SetUpReadReplicaBodyReadReplicaRegion.US_WEST1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1setup_a_read_replica(
            ref, read_replica_region=read_replica_region, request_options=request_options
        )
        return _response.data

    async def v1remove_a_read_replica(
        self, ref: str, *, database_identifier: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        database_identifier : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1remove_a_read_replica(
                ref="abcdefghijklmnopqrst",
                database_identifier="abcdefghijklmnopqrst-rr-us-west-1-abcde",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1remove_a_read_replica(
            ref, database_identifier=database_identifier, request_options=request_options
        )
        return _response.data

    async def v1create_login_role(
        self, ref: str, *, read_only: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> CreateRoleResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        read_only : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateRoleResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1create_login_role(
                ref="abcdefghijklmnopqrst",
                read_only=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_login_role(
            ref, read_only=read_only, request_options=request_options
        )
        return _response.data

    async def v1delete_login_roles(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteRolesResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteRolesResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1delete_login_roles(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_login_roles(ref, request_options=request_options)
        return _response.data

    async def v1list_migration_history(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1ListMigrationsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1ListMigrationsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1list_migration_history(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_migration_history(ref, request_options=request_options)
        return _response.data

    async def v1apply_a_migration(
        self,
        ref: str,
        *,
        query: str,
        idempotency_key: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        rollback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        query : str

        idempotency_key : typing.Optional[str]
            A unique key to ensure the same migration is tracked only once.

        name : typing.Optional[str]

        rollback : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1apply_a_migration(
                ref="abcdefghijklmnopqrst",
                query="create table public.widgets(id bigint primary key);",
                name="create_widgets_table",
                rollback="drop table if exists public.widgets;",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1apply_a_migration(
            ref,
            query=query,
            idempotency_key=idempotency_key,
            name=name,
            rollback=rollback,
            request_options=request_options,
        )
        return _response.data

    async def v1upsert_a_migration(
        self,
        ref: str,
        *,
        query: str,
        idempotency_key: typing.Optional[str] = None,
        name: typing.Optional[str] = OMIT,
        rollback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        query : str

        idempotency_key : typing.Optional[str]
            A unique key to ensure the same migration is tracked only once.

        name : typing.Optional[str]

        rollback : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1upsert_a_migration(
                ref="abcdefghijklmnopqrst",
                query="create table public.widgets(id bigint primary key);",
                name="create_widgets_table",
                rollback="drop table if exists public.widgets;",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1upsert_a_migration(
            ref,
            query=query,
            idempotency_key=idempotency_key,
            name=name,
            rollback=rollback,
            request_options=request_options,
        )
        return _response.data

    async def v1rollback_migrations(
        self, ref: str, *, gte: str, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        gte : str
            Rollback migrations greater or equal to this version

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1rollback_migrations(
                ref="abcdefghijklmnopqrst",
                gte="20250312000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1rollback_migrations(ref, gte=gte, request_options=request_options)
        return _response.data

    async def v1get_a_migration(
        self, ref: str, version: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1GetMigrationResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        version : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1GetMigrationResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_a_migration(
                ref="abcdefghijklmnopqrst",
                version="20250312000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_a_migration(ref, version, request_options=request_options)
        return _response.data

    async def v1patch_a_migration(
        self,
        ref: str,
        version: str,
        *,
        name: typing.Optional[str] = OMIT,
        rollback: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        version : str

        name : typing.Optional[str]

        rollback : typing.Optional[str]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1patch_a_migration(
                ref="abcdefghijklmnopqrst",
                version="20250312000000",
                name="create_widgets_table",
                rollback="drop table if exists public.widgets;",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1patch_a_migration(
            ref, version, name=name, rollback=rollback, request_options=request_options
        )
        return _response.data

    async def v1run_a_query(
        self,
        ref: str,
        *,
        query: str,
        parameters: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        read_only: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        query : str

        parameters : typing.Optional[typing.Sequence[typing.Any]]

        read_only : typing.Optional[bool]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1run_a_query(
                ref="abcdefghijklmnopqrst",
                query="select * from pg_stat_activity limit 1;",
                read_only=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1run_a_query(
            ref, query=query, parameters=parameters, read_only=read_only, request_options=request_options
        )
        return _response.data

    async def v1read_only_query(
        self,
        ref: str,
        *,
        query: str,
        parameters: typing.Optional[typing.Sequence[typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        All entity references must be schema qualified.

        Parameters
        ----------
        ref : str
            Project ref

        query : str

        parameters : typing.Optional[typing.Sequence[typing.Any]]

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1read_only_query(
                ref="abcdefghijklmnopqrst",
                query="select * from pg_stat_activity limit 1;",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1read_only_query(
            ref, query=query, parameters=parameters, request_options=request_options
        )
        return _response.data

    async def v1enable_database_webhook(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1enable_database_webhook(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1enable_database_webhook(ref, request_options=request_options)
        return _response.data

    async def v1get_database_metadata(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetProjectDbMetadataResponseOutput:
        """
        This is an **experimental** endpoint. It is subject to change or removal in future versions. Use it with caution, as it may not remain supported or stable.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetProjectDbMetadataResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_database_metadata(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_database_metadata(ref, request_options=request_options)
        return _response.data

    async def v1update_database_password(
        self, ref: str, *, password: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V1UpdatePasswordResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        password : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1UpdatePasswordResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1update_database_password(
                ref="abcdefghijklmnopqrst",
                password="correct-horse-battery-staple",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_database_password(
            ref, password=password, request_options=request_options
        )
        return _response.data

    async def v1get_jit_access(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JitAccessResponseOutput:
        """
        Mappings of roles a user can assume in the project database

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitAccessResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_jit_access(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_jit_access(ref, request_options=request_options)
        return _response.data

    async def v1authorize_jit_access(
        self, ref: str, *, role: str, rhost: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JitAuthorizeAccessResponseOutput:
        """
        Authorizes the request to assume a role in the project database

        Parameters
        ----------
        ref : str
            Project ref

        role : str

        rhost : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitAuthorizeAccessResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1authorize_jit_access(
                ref="abcdefghijklmnopqrst",
                role="postgres",
                rhost="203.0.113.10",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1authorize_jit_access(
            ref, role=role, rhost=rhost, request_options=request_options
        )
        return _response.data

    async def v1update_jit_access(
        self,
        ref: str,
        *,
        user_id: str,
        roles: typing.Sequence[UpdateJitAccessBodyRolesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> JitAccessResponseOutput:
        """
        Modifies the roles that can be assumed and for how long

        Parameters
        ----------
        ref : str
            Project ref

        user_id : str

        roles : typing.Sequence[UpdateJitAccessBodyRolesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitAccessResponseOutput


        Examples
        --------
        import asyncio

        from fern.database import (
            UpdateJitAccessBodyRolesItem,
            UpdateJitAccessBodyRolesItemAllowedNetworks,
            UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1update_jit_access(
                ref="abcdefghijklmnopqrst",
                user_id="55555555-5555-4555-8555-555555555555",
                roles=[
                    UpdateJitAccessBodyRolesItem(
                        role="postgres",
                        expires_at=1740787200.0,
                        allowed_networks=UpdateJitAccessBodyRolesItemAllowedNetworks(
                            allowed_cidrs=[
                                UpdateJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem(
                                    cidr="203.0.113.0/24",
                                )
                            ],
                        ),
                        branches_only=False,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_jit_access(
            ref, user_id=user_id, roles=roles, request_options=request_options
        )
        return _response.data

    async def v1list_jit_access(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> JitListAccessResponseOutput:
        """
        Mappings of roles a user can assume in the project database

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitListAccessResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1list_jit_access(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_jit_access(ref, request_options=request_options)
        return _response.data

    async def v1invite_external_jit_access(
        self,
        ref: str,
        *,
        email: str,
        roles: typing.Sequence[InviteExternalUserJitAccessBodyRolesItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InviteExternalUserJitResponseOutput:
        """
        Invites the external user and sets initial roles that can be assumed and for how long

        Parameters
        ----------
        ref : str
            Project ref

        email : str

        roles : typing.Sequence[InviteExternalUserJitAccessBodyRolesItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        InviteExternalUserJitResponseOutput


        Examples
        --------
        import asyncio

        from fern.database import (
            InviteExternalUserJitAccessBodyRolesItem,
            InviteExternalUserJitAccessBodyRolesItemAllowedNetworks,
            InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1invite_external_jit_access(
                ref="abcdefghijklmnopqrst",
                email="external-user@somedomain.xyz",
                roles=[
                    InviteExternalUserJitAccessBodyRolesItem(
                        role="postgres",
                        expires_at=1740787200.0,
                        allowed_networks=InviteExternalUserJitAccessBodyRolesItemAllowedNetworks(
                            allowed_cidrs=[
                                InviteExternalUserJitAccessBodyRolesItemAllowedNetworksAllowedCidrsItem(
                                    cidr="203.0.113.0/24",
                                )
                            ],
                        ),
                        branches_only=False,
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1invite_external_jit_access(
            ref, email=email, roles=roles, request_options=request_options
        )
        return _response.data

    async def v1accept_invite_external_jit_access(
        self, ref: str, *, email: str, token: str, request_options: typing.Optional[RequestOptions] = None
    ) -> JitAccessResponseOutput:
        """
        Accepts the invitation to JIT database access

        Parameters
        ----------
        ref : str
            Project ref

        email : str

        token : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        JitAccessResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1accept_invite_external_jit_access(
                ref="abcdefghijklmnopqrst",
                email="external-user@somedomain.xyz",
                token="",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1accept_invite_external_jit_access(
            ref, email=email, token=token, request_options=request_options
        )
        return _response.data

    async def v1delete_invite_external_jit_access(
        self, ref: str, invite_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Revokes and deletes the invitation

        Parameters
        ----------
        ref : str
            Project ref

        invite_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1delete_invite_external_jit_access(
                ref="abcdefghijklmnopqrst",
                invite_id="55555555-5555-4555-8555-555555555555",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_invite_external_jit_access(
            ref, invite_id, request_options=request_options
        )
        return _response.data

    async def v1delete_jit_access(
        self, ref: str, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Remove JIT mappings of a user, revoking all JIT database access

        Parameters
        ----------
        ref : str
            Project ref

        user_id : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1delete_jit_access(
                ref="abcdefghijklmnopqrst",
                user_id="55555555-5555-4555-8555-555555555555",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_jit_access(ref, user_id, request_options=request_options)
        return _response.data

    async def v1get_database_openapi(
        self, ref: str, *, schema: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns the PostgREST OpenAPI specification for the project. This is the replacement for querying `/rest/v1/` directly with the anon key.

        Parameters
        ----------
        ref : str
            Project ref

        schema : typing.Optional[str]
            The database schema to generate the OpenAPI spec for

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_database_openapi(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_database_openapi(ref, schema=schema, request_options=request_options)
        return _response.data

    async def v1get_project_pgbouncer_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1PgbouncerConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1PgbouncerConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_project_pgbouncer_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_project_pgbouncer_config(ref, request_options=request_options)
        return _response.data

    async def v1get_pooler_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[SupavisorConfigResponseOutput]:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[SupavisorConfigResponseOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_pooler_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_pooler_config(ref, request_options=request_options)
        return _response.data

    async def v1update_pooler_config(
        self,
        ref: str,
        *,
        default_pool_size: typing.Optional[int] = OMIT,
        pool_mode: typing.Optional[UpdateSupavisorConfigBodyPoolMode] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateSupavisorConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        default_pool_size : typing.Optional[int]

        pool_mode : typing.Optional[UpdateSupavisorConfigBodyPoolMode]
            Dedicated pooler mode for the project

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateSupavisorConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern.database import UpdateSupavisorConfigBodyPoolMode

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1update_pooler_config(
                ref="abcdefghijklmnopqrst",
                default_pool_size=25,
                pool_mode=UpdateSupavisorConfigBodyPoolMode.TRANSACTION,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_pooler_config(
            ref, default_pool_size=default_pool_size, pool_mode=pool_mode, request_options=request_options
        )
        return _response.data

    async def v1get_postgres_config(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PostgresConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostgresConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_postgres_config(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_postgres_config(ref, request_options=request_options)
        return _response.data

    async def v1update_postgres_config(
        self,
        ref: str,
        *,
        effective_cache_size: typing.Optional[str] = OMIT,
        logical_decoding_work_mem: typing.Optional[str] = OMIT,
        cron_log_statement: typing.Optional[bool] = OMIT,
        log_autovacuum_min_duration: typing.Optional[str] = OMIT,
        log_checkpoints: typing.Optional[bool] = OMIT,
        log_connections: typing.Optional[bool] = OMIT,
        log_disconnections: typing.Optional[bool] = OMIT,
        log_duration: typing.Optional[bool] = OMIT,
        log_lock_waits: typing.Optional[bool] = OMIT,
        log_recovery_conflict_waits: typing.Optional[bool] = OMIT,
        log_replication_commands: typing.Optional[bool] = OMIT,
        log_startup_progress_interval: typing.Optional[str] = OMIT,
        log_temp_files: typing.Optional[str] = OMIT,
        maintenance_work_mem: typing.Optional[str] = OMIT,
        track_activity_query_size: typing.Optional[str] = OMIT,
        max_connections: typing.Optional[int] = OMIT,
        max_locks_per_transaction: typing.Optional[int] = OMIT,
        max_logical_replication_workers: typing.Optional[int] = OMIT,
        max_parallel_maintenance_workers: typing.Optional[int] = OMIT,
        max_parallel_workers: typing.Optional[int] = OMIT,
        max_parallel_workers_per_gather: typing.Optional[int] = OMIT,
        max_replication_slots: typing.Optional[int] = OMIT,
        max_slot_wal_keep_size: typing.Optional[str] = OMIT,
        max_standby_archive_delay: typing.Optional[str] = OMIT,
        max_standby_streaming_delay: typing.Optional[str] = OMIT,
        max_sync_workers_per_subscription: typing.Optional[int] = OMIT,
        max_wal_size: typing.Optional[str] = OMIT,
        max_wal_senders: typing.Optional[int] = OMIT,
        max_worker_processes: typing.Optional[int] = OMIT,
        session_replication_role: typing.Optional[UpdatePostgresConfigBodySessionReplicationRole] = OMIT,
        shared_buffers: typing.Optional[str] = OMIT,
        statement_timeout: typing.Optional[str] = OMIT,
        track_commit_timestamp: typing.Optional[bool] = OMIT,
        wal_keep_size: typing.Optional[str] = OMIT,
        wal_sender_timeout: typing.Optional[str] = OMIT,
        work_mem: typing.Optional[str] = OMIT,
        checkpoint_timeout: typing.Optional[str] = OMIT,
        hot_standby_feedback: typing.Optional[bool] = OMIT,
        restart_database: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostgresConfigResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        effective_cache_size : typing.Optional[str]

        logical_decoding_work_mem : typing.Optional[str]

        cron_log_statement : typing.Optional[bool]

        log_autovacuum_min_duration : typing.Optional[str]
            Default unit: ms

        log_checkpoints : typing.Optional[bool]

        log_connections : typing.Optional[bool]

        log_disconnections : typing.Optional[bool]

        log_duration : typing.Optional[bool]

        log_lock_waits : typing.Optional[bool]

        log_recovery_conflict_waits : typing.Optional[bool]

        log_replication_commands : typing.Optional[bool]

        log_startup_progress_interval : typing.Optional[str]
            Default unit: ms

        log_temp_files : typing.Optional[str]

        maintenance_work_mem : typing.Optional[str]

        track_activity_query_size : typing.Optional[str]

        max_connections : typing.Optional[int]

        max_locks_per_transaction : typing.Optional[int]

        max_logical_replication_workers : typing.Optional[int]

        max_parallel_maintenance_workers : typing.Optional[int]

        max_parallel_workers : typing.Optional[int]

        max_parallel_workers_per_gather : typing.Optional[int]

        max_replication_slots : typing.Optional[int]

        max_slot_wal_keep_size : typing.Optional[str]

        max_standby_archive_delay : typing.Optional[str]

        max_standby_streaming_delay : typing.Optional[str]

        max_sync_workers_per_subscription : typing.Optional[int]

        max_wal_size : typing.Optional[str]

        max_wal_senders : typing.Optional[int]

        max_worker_processes : typing.Optional[int]

        session_replication_role : typing.Optional[UpdatePostgresConfigBodySessionReplicationRole]

        shared_buffers : typing.Optional[str]

        statement_timeout : typing.Optional[str]
            Default unit: ms

        track_commit_timestamp : typing.Optional[bool]

        wal_keep_size : typing.Optional[str]

        wal_sender_timeout : typing.Optional[str]
            Default unit: ms

        work_mem : typing.Optional[str]

        checkpoint_timeout : typing.Optional[str]
            Default unit: s

        hot_standby_feedback : typing.Optional[bool]

        restart_database : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostgresConfigResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1update_postgres_config(
                ref="abcdefghijklmnopqrst",
                max_connections=120,
                shared_buffers="256MB",
                statement_timeout="60000ms",
                work_mem="4MB",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_postgres_config(
            ref,
            effective_cache_size=effective_cache_size,
            logical_decoding_work_mem=logical_decoding_work_mem,
            cron_log_statement=cron_log_statement,
            log_autovacuum_min_duration=log_autovacuum_min_duration,
            log_checkpoints=log_checkpoints,
            log_connections=log_connections,
            log_disconnections=log_disconnections,
            log_duration=log_duration,
            log_lock_waits=log_lock_waits,
            log_recovery_conflict_waits=log_recovery_conflict_waits,
            log_replication_commands=log_replication_commands,
            log_startup_progress_interval=log_startup_progress_interval,
            log_temp_files=log_temp_files,
            maintenance_work_mem=maintenance_work_mem,
            track_activity_query_size=track_activity_query_size,
            max_connections=max_connections,
            max_locks_per_transaction=max_locks_per_transaction,
            max_logical_replication_workers=max_logical_replication_workers,
            max_parallel_maintenance_workers=max_parallel_maintenance_workers,
            max_parallel_workers=max_parallel_workers,
            max_parallel_workers_per_gather=max_parallel_workers_per_gather,
            max_replication_slots=max_replication_slots,
            max_slot_wal_keep_size=max_slot_wal_keep_size,
            max_standby_archive_delay=max_standby_archive_delay,
            max_standby_streaming_delay=max_standby_streaming_delay,
            max_sync_workers_per_subscription=max_sync_workers_per_subscription,
            max_wal_size=max_wal_size,
            max_wal_senders=max_wal_senders,
            max_worker_processes=max_worker_processes,
            session_replication_role=session_replication_role,
            shared_buffers=shared_buffers,
            statement_timeout=statement_timeout,
            track_commit_timestamp=track_commit_timestamp,
            wal_keep_size=wal_keep_size,
            wal_sender_timeout=wal_sender_timeout,
            work_mem=work_mem,
            checkpoint_timeout=checkpoint_timeout,
            hot_standby_feedback=hot_standby_feedback,
            restart_database=restart_database,
            request_options=request_options,
        )
        return _response.data

    async def v1list_all_backups(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1BackupsResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BackupsResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1list_all_backups(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_backups(ref, request_options=request_options)
        return _response.data

    async def v1restore_pitr_backup(
        self, ref: str, *, recovery_time_target_unix: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        recovery_time_target_unix : int

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1restore_pitr_backup(
                ref="abcdefghijklmnopqrst",
                recovery_time_target_unix=1740787200,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1restore_pitr_backup(
            ref, recovery_time_target_unix=recovery_time_target_unix, request_options=request_options
        )
        return _response.data

    async def v1get_restore_point(
        self, ref: str, *, name: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> V1RestorePointResponse:
        """
        Parameters
        ----------
        ref : str
            Project ref

        name : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1RestorePointResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_restore_point(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_restore_point(ref, name=name, request_options=request_options)
        return _response.data

    async def v1create_restore_point(
        self, ref: str, *, name: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V1RestorePointResponse:
        """
        Parameters
        ----------
        ref : str
            Project ref

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1RestorePointResponse


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1create_restore_point(
                ref="abcdefghijklmnopqrst",
                name="before-upgrade",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_restore_point(ref, name=name, request_options=request_options)
        return _response.data

    async def v1restore_physical_backup(
        self, ref: str, *, id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        id : int

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1restore_physical_backup(
                ref="abcdefghijklmnopqrst",
                id=12345,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1restore_physical_backup(ref, id=id, request_options=request_options)
        return _response.data

    async def v1get_backup_schedule(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> V1BackupScheduleResponseOutput:
        """
        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BackupScheduleResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1get_backup_schedule(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_backup_schedule(ref, request_options=request_options)
        return _response.data

    async def v1update_backup_schedule(
        self, ref: str, *, schedule_for: str, request_options: typing.Optional[RequestOptions] = None
    ) -> V1BackupScheduleResponseOutput:
        """
        Sets the time at which the daily backup runs. The change takes effect on the next backup window that includes the new time. If the new time has already passed for today, the first backup at the new time will occur the following day. It can only be updated 3 times per 24 hours.

        Parameters
        ----------
        ref : str
            Project ref

        schedule_for : str
            Time of day to schedule daily backups, in UTC. Format: HH:MM:SS.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        V1BackupScheduleResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1update_backup_schedule(
                ref="abcdefghijklmnopqrst",
                schedule_for="04:00:00",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_backup_schedule(
            ref, schedule_for=schedule_for, request_options=request_options
        )
        return _response.data

    async def v1undo(self, ref: str, *, name: str, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        ref : str
            Project ref

        name : str

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
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.database.v1undo(
                ref="abcdefghijklmnopqrst",
                name="before-upgrade",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1undo(ref, name=name, request_options=request_options)
        return _response.data
