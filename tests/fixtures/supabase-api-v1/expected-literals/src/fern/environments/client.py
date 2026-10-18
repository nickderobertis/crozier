

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.action_run_response_output import ActionRunResponseOutput
from ..types.branch_delete_response_output import BranchDeleteResponseOutput
from ..types.branch_detail_response_output import BranchDetailResponseOutput
from ..types.branch_response_output import BranchResponseOutput
from ..types.branch_restore_response_output import BranchRestoreResponseOutput
from ..types.branch_update_response_output import BranchUpdateResponseOutput
from ..types.list_action_run_response_output import ListActionRunResponseOutput
from ..types.update_run_status_response_output import UpdateRunStatusResponseOutput
from .raw_client import AsyncRawEnvironmentsClient, RawEnvironmentsClient
from .types.create_branch_body_desired_instance_size import CreateBranchBodyDesiredInstanceSize
from .types.create_branch_body_postgres_engine import CreateBranchBodyPostgresEngine
from .types.create_branch_body_release_channel import CreateBranchBodyReleaseChannel
from .types.update_branch_body_status import UpdateBranchBodyStatus
from .types.update_run_status_body_clone import UpdateRunStatusBodyClone
from .types.update_run_status_body_configure import UpdateRunStatusBodyConfigure
from .types.update_run_status_body_deploy import UpdateRunStatusBodyDeploy
from .types.update_run_status_body_health import UpdateRunStatusBodyHealth
from .types.update_run_status_body_migrate import UpdateRunStatusBodyMigrate
from .types.update_run_status_body_pull import UpdateRunStatusBodyPull
from .types.update_run_status_body_seed import UpdateRunStatusBodySeed


OMIT = typing.cast(typing.Any, ...)


class EnvironmentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawEnvironmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawEnvironmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawEnvironmentsClient
        """
        return self._raw_client

    def v1get_a_branch_config(
        self, branch_id_or_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BranchDetailResponseOutput:
        """
        Fetches configurations of the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchDetailResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1get_a_branch_config(
            branch_id_or_ref="branch_id_or_ref",
        )
        """
        _response = self._raw_client.v1get_a_branch_config(branch_id_or_ref, request_options=request_options)
        return _response.data

    def v1delete_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        force: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchDeleteResponseOutput:
        """
        Deletes the specified database branch. By default, deletes immediately. Use force=false to schedule deletion with 1-hour grace period (only when soft deletion is enabled).

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        force : typing.Optional[str]
            If set to false, schedule deletion with 1-hour grace period (only when soft deletion is enabled).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchDeleteResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1delete_a_branch(
            branch_id_or_ref="branch_id_or_ref",
        )
        """
        _response = self._raw_client.v1delete_a_branch(branch_id_or_ref, force=force, request_options=request_options)
        return _response.data

    def v1update_a_branch_config(
        self,
        branch_id_or_ref: str,
        *,
        branch_name: typing.Optional[str] = OMIT,
        git_branch: typing.Optional[str] = OMIT,
        reset_on_push: typing.Optional[bool] = OMIT,
        persistent: typing.Optional[bool] = OMIT,
        status: typing.Optional[UpdateBranchBodyStatus] = OMIT,
        request_review: typing.Optional[bool] = OMIT,
        notify_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchResponseOutput:
        """
        Updates the configuration of the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        branch_name : typing.Optional[str]

        git_branch : typing.Optional[str]

        reset_on_push : typing.Optional[bool]
            This field is deprecated and will be ignored. Use v1-reset-a-branch endpoint directly instead.

        persistent : typing.Optional[bool]

        status : typing.Optional[UpdateBranchBodyStatus]

        request_review : typing.Optional[bool]

        notify_url : typing.Optional[str]
            HTTP endpoint to receive branch status updates.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1update_a_branch_config(
            branch_id_or_ref="branch_id_or_ref",
            branch_name="preview-login-page",
            git_branch="feature/login-page",
            persistent=True,
            request_review=True,
            notify_url="https://example.com/webhooks/branches",
        )
        """
        _response = self._raw_client.v1update_a_branch_config(
            branch_id_or_ref,
            branch_name=branch_name,
            git_branch=git_branch,
            reset_on_push=reset_on_push,
            persistent=persistent,
            status=status,
            request_review=request_review,
            notify_url=notify_url,
            request_options=request_options,
        )
        return _response.data

    def v1push_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchUpdateResponseOutput:
        """
        Pushes the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchUpdateResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1push_a_branch(
            branch_id_or_ref="branch_id_or_ref",
            migration_version="20250312000000",
        )
        """
        _response = self._raw_client.v1push_a_branch(
            branch_id_or_ref, migration_version=migration_version, request_options=request_options
        )
        return _response.data

    def v1merge_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchUpdateResponseOutput:
        """
        Merges the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchUpdateResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1merge_a_branch(
            branch_id_or_ref="branch_id_or_ref",
            migration_version="20250312000000",
        )
        """
        _response = self._raw_client.v1merge_a_branch(
            branch_id_or_ref, migration_version=migration_version, request_options=request_options
        )
        return _response.data

    def v1reset_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchUpdateResponseOutput:
        """
        Resets the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchUpdateResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1reset_a_branch(
            branch_id_or_ref="branch_id_or_ref",
            migration_version="20250312000000",
        )
        """
        _response = self._raw_client.v1reset_a_branch(
            branch_id_or_ref, migration_version=migration_version, request_options=request_options
        )
        return _response.data

    def v1restore_a_branch(
        self, branch_id_or_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BranchRestoreResponseOutput:
        """
        Cancels scheduled deletion and restores the branch to active state

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchRestoreResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1restore_a_branch(
            branch_id_or_ref="branch_id_or_ref",
        )
        """
        _response = self._raw_client.v1restore_a_branch(branch_id_or_ref, request_options=request_options)
        return _response.data

    def v1diff_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        included_schemas: typing.Optional[str] = None,
        pgdelta: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Diffs the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        included_schemas : typing.Optional[str]

        pgdelta : typing.Optional[str]
            Use pg-delta instead of Migra for diffing when true.
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1diff_a_branch(
            branch_id_or_ref="branch_id_or_ref",
        )
        """
        _response = self._raw_client.v1diff_a_branch(
            branch_id_or_ref, included_schemas=included_schemas, pgdelta=pgdelta, request_options=request_options
        )
        return _response.data

    def v1list_action_runs(
        self,
        ref: str,
        *,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListActionRunResponseOutput:
        """
        Returns a paginated list of action runs of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        offset : typing.Optional[float]

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListActionRunResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1list_action_runs(
            ref="abcdefghijklmnopqrst",
            offset=0.0,
            limit=20.0,
        )
        """
        _response = self._raw_client.v1list_action_runs(
            ref, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def v1count_action_runs(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns the total number of action runs of the specified project.

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
        client.environments.v1count_action_runs(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1count_action_runs(ref, request_options=request_options)
        return _response.headers

    def v1get_action_run(
        self, ref: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionRunResponseOutput:
        """
        Returns the current status of the specified action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRunResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1get_action_run(
            ref="abcdefghijklmnopqrst",
            run_id="run_01hq3q9m7y5q7e4a7x2c8m1p4n",
        )
        """
        _response = self._raw_client.v1get_action_run(ref, run_id, request_options=request_options)
        return _response.data

    def v1update_action_run_status(
        self,
        ref: str,
        run_id: str,
        *,
        clone: typing.Optional[UpdateRunStatusBodyClone] = OMIT,
        pull: typing.Optional[UpdateRunStatusBodyPull] = OMIT,
        health: typing.Optional[UpdateRunStatusBodyHealth] = OMIT,
        configure: typing.Optional[UpdateRunStatusBodyConfigure] = OMIT,
        migrate: typing.Optional[UpdateRunStatusBodyMigrate] = OMIT,
        seed: typing.Optional[UpdateRunStatusBodySeed] = OMIT,
        deploy: typing.Optional[UpdateRunStatusBodyDeploy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateRunStatusResponseOutput:
        """
        Updates the status of an ongoing action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        clone : typing.Optional[UpdateRunStatusBodyClone]

        pull : typing.Optional[UpdateRunStatusBodyPull]

        health : typing.Optional[UpdateRunStatusBodyHealth]

        configure : typing.Optional[UpdateRunStatusBodyConfigure]

        migrate : typing.Optional[UpdateRunStatusBodyMigrate]

        seed : typing.Optional[UpdateRunStatusBodySeed]

        deploy : typing.Optional[UpdateRunStatusBodyDeploy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateRunStatusResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1update_action_run_status(
            ref="abcdefghijklmnopqrst",
            run_id="run_01hq3q9m7y5q7e4a7x2c8m1p4n",
            clone="RUNNING",
            configure="RUNNING",
            migrate="RUNNING",
            deploy="CREATED",
        )
        """
        _response = self._raw_client.v1update_action_run_status(
            ref,
            run_id,
            clone=clone,
            pull=pull,
            health=health,
            configure=configure,
            migrate=migrate,
            seed=seed,
            deploy=deploy,
            request_options=request_options,
        )
        return _response.data

    def v1get_action_run_logs(
        self, ref: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the logs from the specified action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1get_action_run_logs(
            ref="ref",
            run_id="run_id",
        )
        """
        _response = self._raw_client.v1get_action_run_logs(ref, run_id, request_options=request_options)
        return _response.data

    def v1list_all_branches(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BranchResponseOutput]:
        """
        Returns all database branches of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BranchResponseOutput]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1list_all_branches(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1list_all_branches(ref, request_options=request_options)
        return _response.data

    def v1create_a_branch(
        self,
        ref: str,
        *,
        branch_name: str,
        git_branch: typing.Optional[str] = OMIT,
        is_default: typing.Optional[bool] = OMIT,
        persistent: typing.Optional[bool] = OMIT,
        region: typing.Optional[str] = OMIT,
        desired_instance_size: typing.Optional[CreateBranchBodyDesiredInstanceSize] = OMIT,
        release_channel: typing.Optional[CreateBranchBodyReleaseChannel] = OMIT,
        postgres_engine: typing.Optional[CreateBranchBodyPostgresEngine] = OMIT,
        secrets: typing.Optional[typing.Dict[str, str]] = OMIT,
        with_data: typing.Optional[bool] = OMIT,
        notify_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchResponseOutput:
        """
        Creates a database branch from the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        branch_name : str

        git_branch : typing.Optional[str]

        is_default : typing.Optional[bool]

        persistent : typing.Optional[bool]

        region : typing.Optional[str]

        desired_instance_size : typing.Optional[CreateBranchBodyDesiredInstanceSize]

        release_channel : typing.Optional[CreateBranchBodyReleaseChannel]
            Release channel. If not provided, GA will be used.

        postgres_engine : typing.Optional[CreateBranchBodyPostgresEngine]
            Postgres engine version. If not provided, the latest version will be used.

        secrets : typing.Optional[typing.Dict[str, str]]

        with_data : typing.Optional[bool]

        notify_url : typing.Optional[str]
            HTTP endpoint to receive branch status updates.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1create_a_branch(
            ref="abcdefghijklmnopqrst",
            branch_name="preview-login-page",
            git_branch="feature/login-page",
            persistent=True,
            with_data=False,
            notify_url="https://example.com/webhooks/branches",
        )
        """
        _response = self._raw_client.v1create_a_branch(
            ref,
            branch_name=branch_name,
            git_branch=git_branch,
            is_default=is_default,
            persistent=persistent,
            region=region,
            desired_instance_size=desired_instance_size,
            release_channel=release_channel,
            postgres_engine=postgres_engine,
            secrets=secrets,
            with_data=with_data,
            notify_url=notify_url,
            request_options=request_options,
        )
        return _response.data

    def v1disable_preview_branching(self, ref: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Disables preview branching for the specified project

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
        client.environments.v1disable_preview_branching(
            ref="abcdefghijklmnopqrst",
        )
        """
        _response = self._raw_client.v1disable_preview_branching(ref, request_options=request_options)
        return _response.data

    def v1get_a_branch(
        self, ref: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BranchResponseOutput:
        """
        Fetches the specified database branch by its name.

        Parameters
        ----------
        ref : str
            Project ref

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchResponseOutput


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.environments.v1get_a_branch(
            ref="abcdefghijklmnopqrst",
            name="preview-login-page",
        )
        """
        _response = self._raw_client.v1get_a_branch(ref, name, request_options=request_options)
        return _response.data


class AsyncEnvironmentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawEnvironmentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawEnvironmentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawEnvironmentsClient
        """
        return self._raw_client

    async def v1get_a_branch_config(
        self, branch_id_or_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BranchDetailResponseOutput:
        """
        Fetches configurations of the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchDetailResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1get_a_branch_config(
                branch_id_or_ref="branch_id_or_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_a_branch_config(branch_id_or_ref, request_options=request_options)
        return _response.data

    async def v1delete_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        force: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchDeleteResponseOutput:
        """
        Deletes the specified database branch. By default, deletes immediately. Use force=false to schedule deletion with 1-hour grace period (only when soft deletion is enabled).

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        force : typing.Optional[str]
            If set to false, schedule deletion with 1-hour grace period (only when soft deletion is enabled).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchDeleteResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1delete_a_branch(
                branch_id_or_ref="branch_id_or_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1delete_a_branch(
            branch_id_or_ref, force=force, request_options=request_options
        )
        return _response.data

    async def v1update_a_branch_config(
        self,
        branch_id_or_ref: str,
        *,
        branch_name: typing.Optional[str] = OMIT,
        git_branch: typing.Optional[str] = OMIT,
        reset_on_push: typing.Optional[bool] = OMIT,
        persistent: typing.Optional[bool] = OMIT,
        status: typing.Optional[UpdateBranchBodyStatus] = OMIT,
        request_review: typing.Optional[bool] = OMIT,
        notify_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchResponseOutput:
        """
        Updates the configuration of the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        branch_name : typing.Optional[str]

        git_branch : typing.Optional[str]

        reset_on_push : typing.Optional[bool]
            This field is deprecated and will be ignored. Use v1-reset-a-branch endpoint directly instead.

        persistent : typing.Optional[bool]

        status : typing.Optional[UpdateBranchBodyStatus]

        request_review : typing.Optional[bool]

        notify_url : typing.Optional[str]
            HTTP endpoint to receive branch status updates.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1update_a_branch_config(
                branch_id_or_ref="branch_id_or_ref",
                branch_name="preview-login-page",
                git_branch="feature/login-page",
                persistent=True,
                request_review=True,
                notify_url="https://example.com/webhooks/branches",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_a_branch_config(
            branch_id_or_ref,
            branch_name=branch_name,
            git_branch=git_branch,
            reset_on_push=reset_on_push,
            persistent=persistent,
            status=status,
            request_review=request_review,
            notify_url=notify_url,
            request_options=request_options,
        )
        return _response.data

    async def v1push_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchUpdateResponseOutput:
        """
        Pushes the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchUpdateResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1push_a_branch(
                branch_id_or_ref="branch_id_or_ref",
                migration_version="20250312000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1push_a_branch(
            branch_id_or_ref, migration_version=migration_version, request_options=request_options
        )
        return _response.data

    async def v1merge_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchUpdateResponseOutput:
        """
        Merges the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchUpdateResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1merge_a_branch(
                branch_id_or_ref="branch_id_or_ref",
                migration_version="20250312000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1merge_a_branch(
            branch_id_or_ref, migration_version=migration_version, request_options=request_options
        )
        return _response.data

    async def v1reset_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        migration_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchUpdateResponseOutput:
        """
        Resets the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        migration_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchUpdateResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1reset_a_branch(
                branch_id_or_ref="branch_id_or_ref",
                migration_version="20250312000000",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1reset_a_branch(
            branch_id_or_ref, migration_version=migration_version, request_options=request_options
        )
        return _response.data

    async def v1restore_a_branch(
        self, branch_id_or_ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BranchRestoreResponseOutput:
        """
        Cancels scheduled deletion and restores the branch to active state

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchRestoreResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1restore_a_branch(
                branch_id_or_ref="branch_id_or_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1restore_a_branch(branch_id_or_ref, request_options=request_options)
        return _response.data

    async def v1diff_a_branch(
        self,
        branch_id_or_ref: str,
        *,
        included_schemas: typing.Optional[str] = None,
        pgdelta: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Diffs the specified database branch

        Parameters
        ----------
        branch_id_or_ref : str
            Branch ref or deprecated branch ID

        included_schemas : typing.Optional[str]

        pgdelta : typing.Optional[str]
            Use pg-delta instead of Migra for diffing when true.
            Boolean string.

            Truthy values: `true`, `1`, `yes`, `on`, `y`, `enabled`

            Falsy values: `false`, `0`, `no`, `off`, `n`, `disabled`

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1diff_a_branch(
                branch_id_or_ref="branch_id_or_ref",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1diff_a_branch(
            branch_id_or_ref, included_schemas=included_schemas, pgdelta=pgdelta, request_options=request_options
        )
        return _response.data

    async def v1list_action_runs(
        self,
        ref: str,
        *,
        offset: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListActionRunResponseOutput:
        """
        Returns a paginated list of action runs of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        offset : typing.Optional[float]

        limit : typing.Optional[float]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListActionRunResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1list_action_runs(
                ref="abcdefghijklmnopqrst",
                offset=0.0,
                limit=20.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_action_runs(
            ref, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def v1count_action_runs(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Returns the total number of action runs of the specified project.

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
            await client.environments.v1count_action_runs(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1count_action_runs(ref, request_options=request_options)
        return _response.headers

    async def v1get_action_run(
        self, ref: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ActionRunResponseOutput:
        """
        Returns the current status of the specified action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ActionRunResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1get_action_run(
                ref="abcdefghijklmnopqrst",
                run_id="run_01hq3q9m7y5q7e4a7x2c8m1p4n",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_action_run(ref, run_id, request_options=request_options)
        return _response.data

    async def v1update_action_run_status(
        self,
        ref: str,
        run_id: str,
        *,
        clone: typing.Optional[UpdateRunStatusBodyClone] = OMIT,
        pull: typing.Optional[UpdateRunStatusBodyPull] = OMIT,
        health: typing.Optional[UpdateRunStatusBodyHealth] = OMIT,
        configure: typing.Optional[UpdateRunStatusBodyConfigure] = OMIT,
        migrate: typing.Optional[UpdateRunStatusBodyMigrate] = OMIT,
        seed: typing.Optional[UpdateRunStatusBodySeed] = OMIT,
        deploy: typing.Optional[UpdateRunStatusBodyDeploy] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateRunStatusResponseOutput:
        """
        Updates the status of an ongoing action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        clone : typing.Optional[UpdateRunStatusBodyClone]

        pull : typing.Optional[UpdateRunStatusBodyPull]

        health : typing.Optional[UpdateRunStatusBodyHealth]

        configure : typing.Optional[UpdateRunStatusBodyConfigure]

        migrate : typing.Optional[UpdateRunStatusBodyMigrate]

        seed : typing.Optional[UpdateRunStatusBodySeed]

        deploy : typing.Optional[UpdateRunStatusBodyDeploy]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateRunStatusResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1update_action_run_status(
                ref="abcdefghijklmnopqrst",
                run_id="run_01hq3q9m7y5q7e4a7x2c8m1p4n",
                clone="RUNNING",
                configure="RUNNING",
                migrate="RUNNING",
                deploy="CREATED",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1update_action_run_status(
            ref,
            run_id,
            clone=clone,
            pull=pull,
            health=health,
            configure=configure,
            migrate=migrate,
            seed=seed,
            deploy=deploy,
            request_options=request_options,
        )
        return _response.data

    async def v1get_action_run_logs(
        self, ref: str, run_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Returns the logs from the specified action run.

        Parameters
        ----------
        ref : str
            Project ref

        run_id : str
            Action Run ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1get_action_run_logs(
                ref="ref",
                run_id="run_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_action_run_logs(ref, run_id, request_options=request_options)
        return _response.data

    async def v1list_all_branches(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[BranchResponseOutput]:
        """
        Returns all database branches of the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[BranchResponseOutput]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1list_all_branches(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1list_all_branches(ref, request_options=request_options)
        return _response.data

    async def v1create_a_branch(
        self,
        ref: str,
        *,
        branch_name: str,
        git_branch: typing.Optional[str] = OMIT,
        is_default: typing.Optional[bool] = OMIT,
        persistent: typing.Optional[bool] = OMIT,
        region: typing.Optional[str] = OMIT,
        desired_instance_size: typing.Optional[CreateBranchBodyDesiredInstanceSize] = OMIT,
        release_channel: typing.Optional[CreateBranchBodyReleaseChannel] = OMIT,
        postgres_engine: typing.Optional[CreateBranchBodyPostgresEngine] = OMIT,
        secrets: typing.Optional[typing.Dict[str, str]] = OMIT,
        with_data: typing.Optional[bool] = OMIT,
        notify_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BranchResponseOutput:
        """
        Creates a database branch from the specified project.

        Parameters
        ----------
        ref : str
            Project ref

        branch_name : str

        git_branch : typing.Optional[str]

        is_default : typing.Optional[bool]

        persistent : typing.Optional[bool]

        region : typing.Optional[str]

        desired_instance_size : typing.Optional[CreateBranchBodyDesiredInstanceSize]

        release_channel : typing.Optional[CreateBranchBodyReleaseChannel]
            Release channel. If not provided, GA will be used.

        postgres_engine : typing.Optional[CreateBranchBodyPostgresEngine]
            Postgres engine version. If not provided, the latest version will be used.

        secrets : typing.Optional[typing.Dict[str, str]]

        with_data : typing.Optional[bool]

        notify_url : typing.Optional[str]
            HTTP endpoint to receive branch status updates.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1create_a_branch(
                ref="abcdefghijklmnopqrst",
                branch_name="preview-login-page",
                git_branch="feature/login-page",
                persistent=True,
                with_data=False,
                notify_url="https://example.com/webhooks/branches",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1create_a_branch(
            ref,
            branch_name=branch_name,
            git_branch=git_branch,
            is_default=is_default,
            persistent=persistent,
            region=region,
            desired_instance_size=desired_instance_size,
            release_channel=release_channel,
            postgres_engine=postgres_engine,
            secrets=secrets,
            with_data=with_data,
            notify_url=notify_url,
            request_options=request_options,
        )
        return _response.data

    async def v1disable_preview_branching(
        self, ref: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Disables preview branching for the specified project

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
            await client.environments.v1disable_preview_branching(
                ref="abcdefghijklmnopqrst",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1disable_preview_branching(ref, request_options=request_options)
        return _response.data

    async def v1get_a_branch(
        self, ref: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> BranchResponseOutput:
        """
        Fetches the specified database branch by its name.

        Parameters
        ----------
        ref : str
            Project ref

        name : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BranchResponseOutput


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.environments.v1get_a_branch(
                ref="abcdefghijklmnopqrst",
                name="preview-login-page",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.v1get_a_branch(ref, name, request_options=request_options)
        return _response.data
