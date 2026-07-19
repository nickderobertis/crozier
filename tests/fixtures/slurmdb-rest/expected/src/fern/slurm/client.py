

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dbv0037account_info import Dbv0037AccountInfo
from ..types.dbv0037account_response import Dbv0037AccountResponse
from ..types.dbv0037associations_info import Dbv0037AssociationsInfo
from ..types.dbv0037cluster_info import Dbv0037ClusterInfo
from ..types.dbv0037config_info import Dbv0037ConfigInfo
from ..types.dbv0037config_response import Dbv0037ConfigResponse
from ..types.dbv0037diag import Dbv0037Diag
from ..types.dbv0037job_info import Dbv0037JobInfo
from ..types.dbv0037qos_info import Dbv0037QosInfo
from ..types.dbv0037response_account_delete import Dbv0037ResponseAccountDelete
from ..types.dbv0037response_association_delete import Dbv0037ResponseAssociationDelete
from ..types.dbv0037response_cluster_add import Dbv0037ResponseClusterAdd
from ..types.dbv0037response_cluster_delete import Dbv0037ResponseClusterDelete
from ..types.dbv0037response_qos_delete import Dbv0037ResponseQosDelete
from ..types.dbv0037response_tres import Dbv0037ResponseTres
from ..types.dbv0037response_user_delete import Dbv0037ResponseUserDelete
from ..types.dbv0037response_user_update import Dbv0037ResponseUserUpdate
from ..types.dbv0037response_wckey_add import Dbv0037ResponseWckeyAdd
from ..types.dbv0037response_wckey_delete import Dbv0037ResponseWckeyDelete
from ..types.dbv0037tres_info import Dbv0037TresInfo
from ..types.dbv0037user_info import Dbv0037UserInfo
from ..types.dbv0037wckey_info import Dbv0037WckeyInfo
from .raw_client import AsyncRawSlurmClient, RawSlurmClient


class SlurmClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSlurmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSlurmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSlurmClient
        """
        return self._raw_client

    def slurmdbd_get_job(
        self, job_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037JobInfo:
        """
        This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

        Parameters
        ----------
        job_id : int
            Slurm Job ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037JobInfo
            Job description

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_job(
            job_id=1000000,
        )
        """
        _response = self._raw_client.slurmdbd_get_job(job_id, request_options=request_options)
        return _response.data

    def slurmdbd_get_db_config(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037ConfigInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ConfigInfo
            slurmdbd configuration

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_db_config()
        """
        _response = self._raw_client.slurmdbd_get_db_config(request_options=request_options)
        return _response.data

    def slurmdbd_set_db_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ConfigResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ConfigResponse
            Load config

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_set_db_config()
        """
        _response = self._raw_client.slurmdbd_set_db_config(request_options=request_options)
        return _response.data

    def slurmdbd_get_tres(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037TresInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037TresInfo
            List of TRES

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_tres()
        """
        _response = self._raw_client.slurmdbd_get_tres(request_options=request_options)
        return _response.data

    def slurmdbd_update_tres(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037ResponseTres:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseTres
            List of TRES

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_update_tres()
        """
        _response = self._raw_client.slurmdbd_update_tres(request_options=request_options)
        return _response.data

    def slurmdbd_get_single_qos(
        self, qos_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037QosInfo:
        """
        Parameters
        ----------
        qos_name : str
            Slurm QOS Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037QosInfo
            QOS information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_single_qos(
            qos_name="qos_name",
        )
        """
        _response = self._raw_client.slurmdbd_get_single_qos(qos_name, request_options=request_options)
        return _response.data

    def slurmdbd_delete_qos(
        self, qos_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseQosDelete:
        """
        Parameters
        ----------
        qos_name : str
            Slurm QOS Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseQosDelete
            Delete qos

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_delete_qos(
            qos_name="qos_name",
        )
        """
        _response = self._raw_client.slurmdbd_delete_qos(qos_name, request_options=request_options)
        return _response.data

    def slurmdbd_get_qos(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037QosInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037QosInfo
            List of QOS'

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_qos()
        """
        _response = self._raw_client.slurmdbd_get_qos(request_options=request_options)
        return _response.data

    def slurmdbd_get_associations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037AssociationsInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AssociationsInfo
            List of associations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_associations()
        """
        _response = self._raw_client.slurmdbd_get_associations(request_options=request_options)
        return _response.data

    def slurmdbd_get_association(
        self,
        *,
        cluster: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dbv0037AssociationsInfo:
        """
        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster name

        account : typing.Optional[str]
            Account name

        user : typing.Optional[str]
            User name

        partition : typing.Optional[str]
            Partition Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AssociationsInfo
            List of associations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_association()
        """
        _response = self._raw_client.slurmdbd_get_association(
            cluster=cluster, account=account, user=user, partition=partition, request_options=request_options
        )
        return _response.data

    def slurmdbd_delete_association(
        self,
        *,
        account: str,
        user: str,
        cluster: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dbv0037ResponseAssociationDelete:
        """
        Parameters
        ----------
        account : str
            Account name

        user : str
            User name

        cluster : typing.Optional[str]
            Cluster name

        partition : typing.Optional[str]
            Partition Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseAssociationDelete
            Delete associations

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_delete_association(
            account="account",
            user="user",
        )
        """
        _response = self._raw_client.slurmdbd_delete_association(
            account=account, user=user, cluster=cluster, partition=partition, request_options=request_options
        )
        return _response.data

    def slurmdbd_get_user(
        self, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037UserInfo:
        """
        Parameters
        ----------
        user_name : str
            Slurm User Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037UserInfo
            List of users

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_user(
            user_name="user_name",
        )
        """
        _response = self._raw_client.slurmdbd_get_user(user_name, request_options=request_options)
        return _response.data

    def slurmdbd_delete_user(
        self, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseUserDelete:
        """
        Parameters
        ----------
        user_name : str
            Slurm User Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseUserDelete
            Delete user

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_delete_user(
            user_name="user_name",
        )
        """
        _response = self._raw_client.slurmdbd_delete_user(user_name, request_options=request_options)
        return _response.data

    def slurmdbd_get_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037UserInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037UserInfo
            List of users

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_users()
        """
        _response = self._raw_client.slurmdbd_get_users(request_options=request_options)
        return _response.data

    def slurmdbd_update_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseUserUpdate:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseUserUpdate
            Update users

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_update_users()
        """
        _response = self._raw_client.slurmdbd_update_users(request_options=request_options)
        return _response.data

    def slurmdbd_get_cluster(
        self, cluster_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ClusterInfo:
        """
        Parameters
        ----------
        cluster_name : str
            Slurm cluster name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ClusterInfo
            Cluster information

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_cluster(
            cluster_name="cluster_name",
        )
        """
        _response = self._raw_client.slurmdbd_get_cluster(cluster_name, request_options=request_options)
        return _response.data

    def slurmdbd_delete_cluster(
        self, cluster_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseClusterDelete:
        """
        Parameters
        ----------
        cluster_name : str
            Slurm cluster name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseClusterDelete
            Delete cluster

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_delete_cluster(
            cluster_name="cluster_name",
        )
        """
        _response = self._raw_client.slurmdbd_delete_cluster(cluster_name, request_options=request_options)
        return _response.data

    def slurmdbd_get_clusters(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037ClusterInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ClusterInfo
            List of clusters

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_clusters()
        """
        _response = self._raw_client.slurmdbd_get_clusters(request_options=request_options)
        return _response.data

    def slurmdbd_add_clusters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseClusterAdd:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseClusterAdd
            List of clusters

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_add_clusters()
        """
        _response = self._raw_client.slurmdbd_add_clusters(request_options=request_options)
        return _response.data

    def slurmdbd_get_wckey(
        self, wckey: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037WckeyInfo:
        """
        Parameters
        ----------
        wckey : str
            Slurm wckey name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037WckeyInfo
            List of wckey

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_wckey(
            wckey="wckey",
        )
        """
        _response = self._raw_client.slurmdbd_get_wckey(wckey, request_options=request_options)
        return _response.data

    def slurmdbd_delete_wckey(
        self, wckey: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseWckeyDelete:
        """
        Parameters
        ----------
        wckey : str
            Slurm wckey name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseWckeyDelete
            Delete wckey

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_delete_wckey(
            wckey="wckey",
        )
        """
        _response = self._raw_client.slurmdbd_delete_wckey(wckey, request_options=request_options)
        return _response.data

    def slurmdbd_get_wckeys(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037WckeyInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037WckeyInfo
            List of wckeys

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_wckeys()
        """
        _response = self._raw_client.slurmdbd_get_wckeys(request_options=request_options)
        return _response.data

    def slurmdbd_add_wckeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseWckeyAdd:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseWckeyAdd
            List of wckeys

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_add_wckeys()
        """
        _response = self._raw_client.slurmdbd_add_wckeys(request_options=request_options)
        return _response.data

    def slurmdbd_get_account(
        self, account_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037AccountInfo:
        """
        Parameters
        ----------
        account_name : str
            Slurm Account Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AccountInfo
            List of accounts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_account(
            account_name="account_name",
        )
        """
        _response = self._raw_client.slurmdbd_get_account(account_name, request_options=request_options)
        return _response.data

    def slurmdbd_delete_account(
        self, account_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseAccountDelete:
        """
        Parameters
        ----------
        account_name : str
            Slurm Account Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseAccountDelete
            Delete account

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_delete_account(
            account_name="account_name",
        )
        """
        _response = self._raw_client.slurmdbd_delete_account(account_name, request_options=request_options)
        return _response.data

    def slurmdbd_get_accounts(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037AccountInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AccountInfo
            List of accounts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_accounts()
        """
        _response = self._raw_client.slurmdbd_get_accounts(request_options=request_options)
        return _response.data

    def slurmdbd_update_account(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037AccountResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AccountResponse
            Add/update list of accounts

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_update_account()
        """
        _response = self._raw_client.slurmdbd_update_account(request_options=request_options)
        return _response.data

    def slurmdbd_get_jobs(
        self,
        *,
        submit_time: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        association: typing.Optional[str] = None,
        cluster: typing.Optional[str] = None,
        constraints: typing.Optional[str] = None,
        cpus_max: typing.Optional[str] = None,
        cpus_min: typing.Optional[str] = None,
        skip_steps: typing.Optional[bool] = None,
        disable_wait_for_result: typing.Optional[bool] = None,
        exit_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        job_name: typing.Optional[str] = None,
        nodes_max: typing.Optional[str] = None,
        nodes_min: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        qos: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        reservation: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        step: typing.Optional[str] = None,
        node: typing.Optional[str] = None,
        wckey: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dbv0037JobInfo:
        """
        Parameters
        ----------
        submit_time : typing.Optional[str]
            Filter by submission time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        start_time : typing.Optional[str]
            Filter by start time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        end_time : typing.Optional[str]
            Filter by end time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        account : typing.Optional[str]
            Comma delimited list of accounts to match

        association : typing.Optional[str]
            Comma delimited list of associations to match

        cluster : typing.Optional[str]
            Comma delimited list of cluster to match

        constraints : typing.Optional[str]
            Comma delimited list of constraints to match

        cpus_max : typing.Optional[str]
            Number of CPUs high range

        cpus_min : typing.Optional[str]
            Number of CPUs low range

        skip_steps : typing.Optional[bool]
            Report job step information

        disable_wait_for_result : typing.Optional[bool]
            Disable waiting for result from slurmdbd

        exit_code : typing.Optional[str]
            Exit code of job

        format : typing.Optional[str]
            Comma delimited list of formats to match

        group : typing.Optional[str]
            Comma delimited list of groups to match

        job_name : typing.Optional[str]
            Comma delimited list of job names to match

        nodes_max : typing.Optional[str]
            Number of nodes high range

        nodes_min : typing.Optional[str]
            Number of nodes low range

        partition : typing.Optional[str]
            Comma delimited list of partitions to match

        qos : typing.Optional[str]
            Comma delimited list of QOS to match

        reason : typing.Optional[str]
            Comma delimited list of job reasons to match

        reservation : typing.Optional[str]
            Comma delimited list of reservations to match

        state : typing.Optional[str]
            Comma delimited list of states to match

        step : typing.Optional[str]
            Comma delimited list of job steps to match

        node : typing.Optional[str]
            Comma delimited list of used nodes to match

        wckey : typing.Optional[str]
            Comma delimited list of wckeys to match

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037JobInfo
            List of jobs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_get_jobs()
        """
        _response = self._raw_client.slurmdbd_get_jobs(
            submit_time=submit_time,
            start_time=start_time,
            end_time=end_time,
            account=account,
            association=association,
            cluster=cluster,
            constraints=constraints,
            cpus_max=cpus_max,
            cpus_min=cpus_min,
            skip_steps=skip_steps,
            disable_wait_for_result=disable_wait_for_result,
            exit_code=exit_code,
            format=format,
            group=group,
            job_name=job_name,
            nodes_max=nodes_max,
            nodes_min=nodes_min,
            partition=partition,
            qos=qos,
            reason=reason,
            reservation=reservation,
            state=state,
            step=step,
            node=node,
            wckey=wckey,
            request_options=request_options,
        )
        return _response.data

    def slurmdbd_diag(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037Diag:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037Diag
            Dictionary of statistics

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )
        client.slurm.slurmdbd_diag()
        """
        _response = self._raw_client.slurmdbd_diag(request_options=request_options)
        return _response.data


class AsyncSlurmClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSlurmClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSlurmClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSlurmClient
        """
        return self._raw_client

    async def slurmdbd_get_job(
        self, job_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037JobInfo:
        """
        This endpoint may return multiple job entries since job_id is not a unique key - only the tuple (cluster, job_id, start_time) is unique. If the requested job_id is a component of a heterogeneous job all components are returned.

        Parameters
        ----------
        job_id : int
            Slurm Job ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037JobInfo
            Job description

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_job(
                job_id=1000000,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_job(job_id, request_options=request_options)
        return _response.data

    async def slurmdbd_get_db_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ConfigInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ConfigInfo
            slurmdbd configuration

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_db_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_db_config(request_options=request_options)
        return _response.data

    async def slurmdbd_set_db_config(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ConfigResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ConfigResponse
            Load config

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_set_db_config()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_set_db_config(request_options=request_options)
        return _response.data

    async def slurmdbd_get_tres(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037TresInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037TresInfo
            List of TRES

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_tres()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_tres(request_options=request_options)
        return _response.data

    async def slurmdbd_update_tres(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseTres:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseTres
            List of TRES

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_update_tres()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_update_tres(request_options=request_options)
        return _response.data

    async def slurmdbd_get_single_qos(
        self, qos_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037QosInfo:
        """
        Parameters
        ----------
        qos_name : str
            Slurm QOS Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037QosInfo
            QOS information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_single_qos(
                qos_name="qos_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_single_qos(qos_name, request_options=request_options)
        return _response.data

    async def slurmdbd_delete_qos(
        self, qos_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseQosDelete:
        """
        Parameters
        ----------
        qos_name : str
            Slurm QOS Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseQosDelete
            Delete qos

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_delete_qos(
                qos_name="qos_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_delete_qos(qos_name, request_options=request_options)
        return _response.data

    async def slurmdbd_get_qos(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037QosInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037QosInfo
            List of QOS'

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_qos()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_qos(request_options=request_options)
        return _response.data

    async def slurmdbd_get_associations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037AssociationsInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AssociationsInfo
            List of associations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_associations()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_associations(request_options=request_options)
        return _response.data

    async def slurmdbd_get_association(
        self,
        *,
        cluster: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        user: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dbv0037AssociationsInfo:
        """
        Parameters
        ----------
        cluster : typing.Optional[str]
            Cluster name

        account : typing.Optional[str]
            Account name

        user : typing.Optional[str]
            User name

        partition : typing.Optional[str]
            Partition Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AssociationsInfo
            List of associations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_association()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_association(
            cluster=cluster, account=account, user=user, partition=partition, request_options=request_options
        )
        return _response.data

    async def slurmdbd_delete_association(
        self,
        *,
        account: str,
        user: str,
        cluster: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dbv0037ResponseAssociationDelete:
        """
        Parameters
        ----------
        account : str
            Account name

        user : str
            User name

        cluster : typing.Optional[str]
            Cluster name

        partition : typing.Optional[str]
            Partition Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseAssociationDelete
            Delete associations

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_delete_association(
                account="account",
                user="user",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_delete_association(
            account=account, user=user, cluster=cluster, partition=partition, request_options=request_options
        )
        return _response.data

    async def slurmdbd_get_user(
        self, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037UserInfo:
        """
        Parameters
        ----------
        user_name : str
            Slurm User Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037UserInfo
            List of users

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_user(
                user_name="user_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_user(user_name, request_options=request_options)
        return _response.data

    async def slurmdbd_delete_user(
        self, user_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseUserDelete:
        """
        Parameters
        ----------
        user_name : str
            Slurm User Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseUserDelete
            Delete user

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_delete_user(
                user_name="user_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_delete_user(user_name, request_options=request_options)
        return _response.data

    async def slurmdbd_get_users(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037UserInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037UserInfo
            List of users

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_users(request_options=request_options)
        return _response.data

    async def slurmdbd_update_users(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseUserUpdate:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseUserUpdate
            Update users

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_update_users()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_update_users(request_options=request_options)
        return _response.data

    async def slurmdbd_get_cluster(
        self, cluster_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ClusterInfo:
        """
        Parameters
        ----------
        cluster_name : str
            Slurm cluster name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ClusterInfo
            Cluster information

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_cluster(
                cluster_name="cluster_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_cluster(cluster_name, request_options=request_options)
        return _response.data

    async def slurmdbd_delete_cluster(
        self, cluster_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseClusterDelete:
        """
        Parameters
        ----------
        cluster_name : str
            Slurm cluster name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseClusterDelete
            Delete cluster

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_delete_cluster(
                cluster_name="cluster_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_delete_cluster(cluster_name, request_options=request_options)
        return _response.data

    async def slurmdbd_get_clusters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ClusterInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ClusterInfo
            List of clusters

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_clusters()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_clusters(request_options=request_options)
        return _response.data

    async def slurmdbd_add_clusters(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseClusterAdd:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseClusterAdd
            List of clusters

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_add_clusters()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_add_clusters(request_options=request_options)
        return _response.data

    async def slurmdbd_get_wckey(
        self, wckey: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037WckeyInfo:
        """
        Parameters
        ----------
        wckey : str
            Slurm wckey name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037WckeyInfo
            List of wckey

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_wckey(
                wckey="wckey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_wckey(wckey, request_options=request_options)
        return _response.data

    async def slurmdbd_delete_wckey(
        self, wckey: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseWckeyDelete:
        """
        Parameters
        ----------
        wckey : str
            Slurm wckey name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseWckeyDelete
            Delete wckey

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_delete_wckey(
                wckey="wckey",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_delete_wckey(wckey, request_options=request_options)
        return _response.data

    async def slurmdbd_get_wckeys(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037WckeyInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037WckeyInfo
            List of wckeys

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_wckeys()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_wckeys(request_options=request_options)
        return _response.data

    async def slurmdbd_add_wckeys(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseWckeyAdd:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseWckeyAdd
            List of wckeys

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_add_wckeys()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_add_wckeys(request_options=request_options)
        return _response.data

    async def slurmdbd_get_account(
        self, account_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037AccountInfo:
        """
        Parameters
        ----------
        account_name : str
            Slurm Account Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AccountInfo
            List of accounts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_account(
                account_name="account_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_account(account_name, request_options=request_options)
        return _response.data

    async def slurmdbd_delete_account(
        self, account_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037ResponseAccountDelete:
        """
        Parameters
        ----------
        account_name : str
            Slurm Account Name

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037ResponseAccountDelete
            Delete account

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_delete_account(
                account_name="account_name",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_delete_account(account_name, request_options=request_options)
        return _response.data

    async def slurmdbd_get_accounts(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037AccountInfo:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AccountInfo
            List of accounts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_accounts()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_accounts(request_options=request_options)
        return _response.data

    async def slurmdbd_update_account(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Dbv0037AccountResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037AccountResponse
            Add/update list of accounts

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_update_account()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_update_account(request_options=request_options)
        return _response.data

    async def slurmdbd_get_jobs(
        self,
        *,
        submit_time: typing.Optional[str] = None,
        start_time: typing.Optional[str] = None,
        end_time: typing.Optional[str] = None,
        account: typing.Optional[str] = None,
        association: typing.Optional[str] = None,
        cluster: typing.Optional[str] = None,
        constraints: typing.Optional[str] = None,
        cpus_max: typing.Optional[str] = None,
        cpus_min: typing.Optional[str] = None,
        skip_steps: typing.Optional[bool] = None,
        disable_wait_for_result: typing.Optional[bool] = None,
        exit_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        group: typing.Optional[str] = None,
        job_name: typing.Optional[str] = None,
        nodes_max: typing.Optional[str] = None,
        nodes_min: typing.Optional[str] = None,
        partition: typing.Optional[str] = None,
        qos: typing.Optional[str] = None,
        reason: typing.Optional[str] = None,
        reservation: typing.Optional[str] = None,
        state: typing.Optional[str] = None,
        step: typing.Optional[str] = None,
        node: typing.Optional[str] = None,
        wckey: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Dbv0037JobInfo:
        """
        Parameters
        ----------
        submit_time : typing.Optional[str]
            Filter by submission time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        start_time : typing.Optional[str]
            Filter by start time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        end_time : typing.Optional[str]
            Filter by end time
             Accepted formats:
             HH:MM[:SS] [AM|PM]
            MMDD[YY] or MM/DD[/YY] or MM.DD[.YY]
            MM/DD[/YY]-HH:MM[:SS]
            YYYY-MM-DD[THH:MM[:SS]]

        account : typing.Optional[str]
            Comma delimited list of accounts to match

        association : typing.Optional[str]
            Comma delimited list of associations to match

        cluster : typing.Optional[str]
            Comma delimited list of cluster to match

        constraints : typing.Optional[str]
            Comma delimited list of constraints to match

        cpus_max : typing.Optional[str]
            Number of CPUs high range

        cpus_min : typing.Optional[str]
            Number of CPUs low range

        skip_steps : typing.Optional[bool]
            Report job step information

        disable_wait_for_result : typing.Optional[bool]
            Disable waiting for result from slurmdbd

        exit_code : typing.Optional[str]
            Exit code of job

        format : typing.Optional[str]
            Comma delimited list of formats to match

        group : typing.Optional[str]
            Comma delimited list of groups to match

        job_name : typing.Optional[str]
            Comma delimited list of job names to match

        nodes_max : typing.Optional[str]
            Number of nodes high range

        nodes_min : typing.Optional[str]
            Number of nodes low range

        partition : typing.Optional[str]
            Comma delimited list of partitions to match

        qos : typing.Optional[str]
            Comma delimited list of QOS to match

        reason : typing.Optional[str]
            Comma delimited list of job reasons to match

        reservation : typing.Optional[str]
            Comma delimited list of reservations to match

        state : typing.Optional[str]
            Comma delimited list of states to match

        step : typing.Optional[str]
            Comma delimited list of job steps to match

        node : typing.Optional[str]
            Comma delimited list of used nodes to match

        wckey : typing.Optional[str]
            Comma delimited list of wckeys to match

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037JobInfo
            List of jobs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_get_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_get_jobs(
            submit_time=submit_time,
            start_time=start_time,
            end_time=end_time,
            account=account,
            association=association,
            cluster=cluster,
            constraints=constraints,
            cpus_max=cpus_max,
            cpus_min=cpus_min,
            skip_steps=skip_steps,
            disable_wait_for_result=disable_wait_for_result,
            exit_code=exit_code,
            format=format,
            group=group,
            job_name=job_name,
            nodes_max=nodes_max,
            nodes_min=nodes_min,
            partition=partition,
            qos=qos,
            reason=reason,
            reservation=reservation,
            state=state,
            step=step,
            node=node,
            wckey=wckey,
            request_options=request_options,
        )
        return _response.data

    async def slurmdbd_diag(self, *, request_options: typing.Optional[RequestOptions] = None) -> Dbv0037Diag:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Dbv0037Diag
            Dictionary of statistics

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            slurm_user_token="YOUR_SLURM_USER_TOKEN",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.slurm.slurmdbd_diag()


        asyncio.run(main())
        """
        _response = await self._raw_client.slurmdbd_diag(request_options=request_options)
        return _response.data
