

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.export_policy import ExportPolicy
from ..types.migration_config_policies_dto import MigrationConfigPoliciesDto
from ..types.multi_policy_config import MultiPolicyConfig
from ..types.policy_block import PolicyBlock
from ..types.policy_block_data import PolicyBlockData
from ..types.policy_category_dto import PolicyCategoryDto
from ..types.policy_config import PolicyConfig
from ..types.policy_config_policy_topics_item import PolicyConfigPolicyTopicsItem
from ..types.preview_policy import PreviewPolicy
from ..types.publish_policy import PublishPolicy
from ..types.task import Task
from ..types.validate_policy import ValidatePolicy
from .raw_client import AsyncRawPoliciesClient, RawPoliciesClient
from .types.get_policies_policy_id_dry_run_ipfs_response_item import GetPoliciesPolicyIdDryRunIpfsResponseItem
from .types.get_policies_policy_id_dry_run_transactions_response_item import (
    GetPoliciesPolicyIdDryRunTransactionsResponseItem,
)
from .types.get_policies_policy_id_dry_run_users_response_item import GetPoliciesPolicyIdDryRunUsersResponseItem
from .types.get_policies_policy_id_groups_response_item import GetPoliciesPolicyIdGroupsResponseItem
from .types.get_policies_policy_id_response import GetPoliciesPolicyIdResponse
from .types.get_policies_policy_id_tag_tag_response import GetPoliciesPolicyIdTagTagResponse
from .types.get_policies_response_item import GetPoliciesResponseItem
from .types.policy_api_get_policy_documents_request_type import PolicyApiGetPolicyDocumentsRequestType
from .types.policy_api_migrate_data_response_item import PolicyApiMigrateDataResponseItem
from .types.post_policies_policy_id_dry_run_login_response_item import PostPoliciesPolicyIdDryRunLoginResponseItem
from .types.post_policies_policy_id_dry_run_user_response_item import PostPoliciesPolicyIdDryRunUserResponseItem


OMIT = typing.cast(typing.Any, ...)


class PoliciesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPoliciesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPoliciesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPoliciesClient
        """
        return self._raw_client

    def return_a_list_of_all_policies(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetPoliciesResponseItem]:
        """
        Returns all policies. Only users with the Standard Registry and Installer role are allowed to make the request.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesResponseItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.return_a_list_of_all_policies()
        """
        _response = self._raw_client.return_a_list_of_all_policies(
            page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    def creates_a_new_policy(
        self,
        *,
        name: str,
        version: str,
        description: str,
        topic_description: str,
        config: typing.Dict[str, typing.Any],
        topic_id: str,
        policy_tag: str,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        policy_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        policy_topics: typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Creates a new policy. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        name : str

        version : str

        description : str

        topic_description : str

        config : typing.Dict[str, typing.Any]

        topic_id : str

        policy_tag : str

        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        status : typing.Optional[str]

        owner : typing.Optional[str]

        policy_roles : typing.Optional[typing.Sequence[str]]

        policy_topics : typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.creates_a_new_policy(
            name="name",
            version="version",
            description="description",
            topic_description="topicDescription",
            config={"key": "value"},
            topic_id="topicId",
            policy_tag="policyTag",
        )
        """
        _response = self._raw_client.creates_a_new_policy(
            name=name,
            version=version,
            description=description,
            topic_description=topic_description,
            config=config,
            topic_id=topic_id,
            policy_tag=policy_tag,
            id=id,
            uuid_=uuid_,
            status=status,
            owner=owner,
            policy_roles=policy_roles,
            policy_topics=policy_topics,
            request_options=request_options,
        )
        return _response.data

    def policy_api_migrate_data(
        self,
        *,
        policies: MigrationConfigPoliciesDto,
        vcs: typing.Sequence[str],
        vps: typing.Sequence[str],
        schemas: typing.Dict[str, typing.Any],
        groups: typing.Dict[str, typing.Any],
        roles: typing.Dict[str, typing.Any],
        blocks: typing.Dict[str, typing.Any],
        tokens: typing.Dict[str, typing.Any],
        migrate_state: bool,
        migrate_retire_pools: bool,
        edited_v_cs: typing.Dict[str, typing.Any],
        retire_contract_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PolicyApiMigrateDataResponseItem]:
        """
        Migrate policy data. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policies : MigrationConfigPoliciesDto

        vcs : typing.Sequence[str]

        vps : typing.Sequence[str]

        schemas : typing.Dict[str, typing.Any]

        groups : typing.Dict[str, typing.Any]

        roles : typing.Dict[str, typing.Any]

        blocks : typing.Dict[str, typing.Any]

        tokens : typing.Dict[str, typing.Any]

        migrate_state : bool

        migrate_retire_pools : bool

        edited_v_cs : typing.Dict[str, typing.Any]

        retire_contract_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PolicyApiMigrateDataResponseItem]
            Errors while migration.

        Examples
        --------
        from fern import FernApi, MigrationConfigPoliciesDto

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_migrate_data(
            policies=MigrationConfigPoliciesDto(
                src="src",
                dst="dst",
            ),
            vcs=["vcs"],
            vps=["vps"],
            schemas={"key": "value"},
            groups={"key": "value"},
            roles={"key": "value"},
            blocks={"key": "value"},
            tokens={"key": "value"},
            migrate_state=True,
            migrate_retire_pools=True,
            edited_v_cs={"key": "value"},
            retire_contract_id="retireContractId",
        )
        """
        _response = self._raw_client.policy_api_migrate_data(
            policies=policies,
            vcs=vcs,
            vps=vps,
            schemas=schemas,
            groups=groups,
            roles=roles,
            blocks=blocks,
            tokens=tokens,
            migrate_state=migrate_state,
            migrate_retire_pools=migrate_retire_pools,
            edited_v_cs=edited_v_cs,
            retire_contract_id=retire_contract_id,
            request_options=request_options,
        )
        return _response.data

    def policy_api_migrate_data_async(
        self,
        *,
        policies: MigrationConfigPoliciesDto,
        vcs: typing.Sequence[str],
        vps: typing.Sequence[str],
        schemas: typing.Dict[str, typing.Any],
        groups: typing.Dict[str, typing.Any],
        roles: typing.Dict[str, typing.Any],
        blocks: typing.Dict[str, typing.Any],
        tokens: typing.Dict[str, typing.Any],
        migrate_state: bool,
        migrate_retire_pools: bool,
        edited_v_cs: typing.Dict[str, typing.Any],
        retire_contract_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Migrate policy data asynchronous. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policies : MigrationConfigPoliciesDto

        vcs : typing.Sequence[str]

        vps : typing.Sequence[str]

        schemas : typing.Dict[str, typing.Any]

        groups : typing.Dict[str, typing.Any]

        roles : typing.Dict[str, typing.Any]

        blocks : typing.Dict[str, typing.Any]

        tokens : typing.Dict[str, typing.Any]

        migrate_state : bool

        migrate_retire_pools : bool

        edited_v_cs : typing.Dict[str, typing.Any]

        retire_contract_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Created task.

        Examples
        --------
        from fern import FernApi, MigrationConfigPoliciesDto

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_migrate_data_async(
            policies=MigrationConfigPoliciesDto(
                src="src",
                dst="dst",
            ),
            vcs=["vcs"],
            vps=["vps"],
            schemas={"key": "value"},
            groups={"key": "value"},
            roles={"key": "value"},
            blocks={"key": "value"},
            tokens={"key": "value"},
            migrate_state=True,
            migrate_retire_pools=True,
            edited_v_cs={"key": "value"},
            retire_contract_id="retireContractId",
        )
        """
        _response = self._raw_client.policy_api_migrate_data_async(
            policies=policies,
            vcs=vcs,
            vps=vps,
            schemas=schemas,
            groups=groups,
            roles=roles,
            blocks=blocks,
            tokens=tokens,
            migrate_state=migrate_state,
            migrate_retire_pools=migrate_retire_pools,
            edited_v_cs=edited_v_cs,
            retire_contract_id=retire_contract_id,
            request_options=request_options,
        )
        return _response.data

    def policy_api_update_policy_async(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        policy_id : str
            Policy identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_update_policy_async(
            policy_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.policy_api_update_policy_async(policy_id, request_options=request_options)
        return _response.data

    def policy_api_delete_policy_async(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        policy_id : str
            Policy identifier

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
        client.policies.policy_api_delete_policy_async(
            policy_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.policy_api_delete_policy_async(policy_id, request_options=request_options)
        return _response.data

    def retrieves_policy_configuration(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPoliciesPolicyIdResponse:
        """
        Retrieves policy configuration for the specified policy ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPoliciesPolicyIdResponse
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.retrieves_policy_configuration(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.retrieves_policy_configuration(policy_id, request_options=request_options)
        return _response.data

    def updates_policy_configuration(
        self,
        policy_id: str,
        *,
        name: str,
        version: str,
        description: str,
        topic_description: str,
        config: typing.Dict[str, typing.Any],
        topic_id: str,
        policy_tag: str,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        policy_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        policy_topics: typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyConfig:
        """
        Updates policy configuration for the specified policy ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        name : str

        version : str

        description : str

        topic_description : str

        config : typing.Dict[str, typing.Any]

        topic_id : str

        policy_tag : str

        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        status : typing.Optional[str]

        owner : typing.Optional[str]

        policy_roles : typing.Optional[typing.Sequence[str]]

        policy_topics : typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyConfig
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.updates_policy_configuration(
            policy_id="policyId",
            name="name",
            version="version",
            description="description",
            topic_description="topicDescription",
            config={"key": "value"},
            topic_id="topicId",
            policy_tag="policyTag",
        )
        """
        _response = self._raw_client.updates_policy_configuration(
            policy_id,
            name=name,
            version=version,
            description=description,
            topic_description=topic_description,
            config=config,
            topic_id=topic_id,
            policy_tag=policy_tag,
            id=id,
            uuid_=uuid_,
            status=status,
            owner=owner,
            policy_roles=policy_roles,
            policy_topics=policy_topics,
            request_options=request_options,
        )
        return _response.data

    def publishes_the_policy_onto_ipfs(
        self,
        policy_id: str,
        *,
        policy_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishPolicy:
        """
        Publishes the policy with the specified (internal) policy ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        policy_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishPolicy
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.publishes_the_policy_onto_ipfs(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.publishes_the_policy_onto_ipfs(
            policy_id, policy_version=policy_version, request_options=request_options
        )
        return _response.data

    def publishes_the_policy_with_the_specified_internal_policy_id_onto_ipfs_sends_a_message_featuring_its_ipfs_cid_into_the_corresponding_hedera_topic(
        self,
        policy_id: str,
        *,
        policy_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Publishes the policy with the specified (internal) policy ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        policy_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.publishes_the_policy_with_the_specified_internal_policy_id_onto_ipfs_sends_a_message_featuring_its_ipfs_cid_into_the_corresponding_hedera_topic(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.publishes_the_policy_with_the_specified_internal_policy_id_onto_ipfs_sends_a_message_featuring_its_ipfs_cid_into_the_corresponding_hedera_topic(
            policy_id, policy_version=policy_version, request_options=request_options
        )
        return _response.data

    def dry_run_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishPolicy:
        """
        Run policy without making any persistent changes or executing transaction. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishPolicy
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.dry_run_policy(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.dry_run_policy(policy_id, request_options=request_options)
        return _response.data

    def policy_api_discontinue_policy(
        self,
        policy_id: typing.Any,
        *,
        date: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Discontunue policy. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        date : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Policies.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_discontinue_policy(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.policy_api_discontinue_policy(
            policy_id, date=date, request_options=request_options
        )
        return _response.data

    def return_policy_to_editing(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishPolicy:
        """
        Return policy to editing. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishPolicy
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.return_policy_to_editing(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.return_policy_to_editing(policy_id, request_options=request_options)
        return _response.data

    def validates_policy(
        self,
        *,
        name: str,
        version: str,
        description: str,
        topic_description: str,
        config: typing.Dict[str, typing.Any],
        topic_id: str,
        policy_tag: str,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        policy_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        policy_topics: typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidatePolicy:
        """
        Validates selected policy. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        name : str

        version : str

        description : str

        topic_description : str

        config : typing.Dict[str, typing.Any]

        topic_id : str

        policy_tag : str

        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        status : typing.Optional[str]

        owner : typing.Optional[str]

        policy_roles : typing.Optional[typing.Sequence[str]]

        policy_topics : typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidatePolicy
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.validates_policy(
            name="name",
            version="version",
            description="description",
            topic_description="topicDescription",
            config={"key": "value"},
            topic_id="topicId",
            policy_tag="policyTag",
        )
        """
        _response = self._raw_client.validates_policy(
            name=name,
            version=version,
            description=description,
            topic_description=topic_description,
            config=config,
            topic_id=topic_id,
            policy_tag=policy_tag,
            id=id,
            uuid_=uuid_,
            status=status,
            owner=owner,
            policy_roles=policy_roles,
            policy_topics=policy_topics,
            request_options=request_options,
        )
        return _response.data

    def policy_api_get_policy_navigation(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns a policy navigation.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_get_policy_navigation(
            policy_id="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.policy_api_get_policy_navigation(policy_id, request_options=request_options)
        return _response.data

    def returns_a_list_of_groups_the_user_is_a_member_of(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetPoliciesPolicyIdGroupsResponseItem]:
        """
        Returns a list of groups the user is a member of.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesPolicyIdGroupsResponseItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.returns_a_list_of_groups_the_user_is_a_member_of(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.returns_a_list_of_groups_the_user_is_a_member_of(
            policy_id, request_options=request_options
        )
        return _response.data

    def makes_the_selected_group_active(
        self,
        policy_id: str,
        *,
        uuid_: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Makes the selected group active. if UUID is not set then returns the user to the default state.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        uuid_ : typing.Optional[str]

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
        client.policies.makes_the_selected_group_active(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.makes_the_selected_group_active(
            policy_id, uuid_=uuid_, request_options=request_options
        )
        return _response.data

    def policy_api_get_policy_documents(
        self,
        policy_id: typing.Any,
        *,
        page_size: float,
        page_index: float,
        type: PolicyApiGetPolicyDocumentsRequestType,
        include_document: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Get policy documents. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        page_size : float
            Page size.

        page_index : float
            Page index.

        type : PolicyApiGetPolicyDocumentsRequestType
            Document type.

        include_document : bool
            Include document field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Documents.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_get_policy_documents(
            policy_id="policyId",
            page_size=1.1,
            page_index=1.1,
            type="VC",
            include_document=True,
        )
        """
        _response = self._raw_client.policy_api_get_policy_documents(
            policy_id,
            page_size=page_size,
            page_index=page_index,
            type=type,
            include_document=include_document,
            request_options=request_options,
        )
        return _response.data

    def policy_api_download_policy_data(
        self, policy_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Get policy data. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Policy data.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_download_policy_data(
            policy_id="policyId",
        )
        """
        with self._raw_client.policy_api_download_policy_data(policy_id, request_options=request_options) as r:
            yield from r.data

    def policy_api_upload_policy_data(
        self, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Upload policy data. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Uploaded policy.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_upload_policy_data(
            request="string",
        )
        """
        _response = self._raw_client.policy_api_upload_policy_data(request=request, request_options=request_options)
        return _response.data

    def policy_api_get_tag_block_map(
        self, policy_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get policy tag block map. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Policy tag block map.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_get_tag_block_map(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.policy_api_get_tag_block_map(policy_id, request_options=request_options)
        return _response.data

    def policy_api_download_virtual_keys(
        self, policy_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Get policy virtual keys. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Policy virtual keys.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_download_virtual_keys(
            policy_id="policyId",
        )
        """
        with self._raw_client.policy_api_download_virtual_keys(policy_id, request_options=request_options) as r:
            yield from r.data

    def policy_api_upload_virtual_keys(
        self, policy_id: typing.Any, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Upload policy virtual keys. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        request : bytes

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
        client.policies.policy_api_upload_virtual_keys(
            policy_id="policyId",
            request="string",
        )
        """
        _response = self._raw_client.policy_api_upload_virtual_keys(
            policy_id, request=request, request_options=request_options
        )
        return _response.data

    def retrieves_data_for_the_policy_root_block(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PolicyBlock:
        """
        Returns data from the root policy block. Only users with the Standard Registry and Installer role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBlock
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.retrieves_data_for_the_policy_root_block(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.retrieves_data_for_the_policy_root_block(
            policy_id, request_options=request_options
        )
        return _response.data

    def requests_block_data(
        self, policy_id: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PolicyBlockData:
        """
        Requests block data by tag. Only users with a role that described in block are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        tag : str
            Tag from the selected policy.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBlockData
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.requests_block_data(
            policy_id="policyId",
            tag="tag",
        )
        """
        _response = self._raw_client.requests_block_data(policy_id, tag, request_options=request_options)
        return _response.data

    def sends_data_to_the_specified_block(
        self,
        policy_id: str,
        tag: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBlockData:
        """
        Sends data to the specified block.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        tag : str
            Tag from the selected policy.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBlockData
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.sends_data_to_the_specified_block(
            policy_id="policyId",
            tag="tag",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.sends_data_to_the_specified_block(
            policy_id, tag, request=request, request_options=request_options
        )
        return _response.data

    def policy_api_get_blocks_by_tag_name(
        self, policy_id: str, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Requests block data by tag. Only users with a role that described in block are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        tag_name : str
            Policy block tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_get_blocks_by_tag_name(
            policy_id="652745597a7b53526de37c05",
            tag_name="someTag",
        )
        """
        _response = self._raw_client.policy_api_get_blocks_by_tag_name(
            policy_id, tag_name, request_options=request_options
        )
        return _response.data

    def policy_api_set_blocks_by_tag_name(
        self, policy_id: str, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Sends data to the specified block.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        tag_name : str
            Policy block tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_set_blocks_by_tag_name(
            policy_id="652745597a7b53526de37c05",
            tag_name="someTag",
        )
        """
        _response = self._raw_client.policy_api_set_blocks_by_tag_name(
            policy_id, tag_name, request_options=request_options
        )
        return _response.data

    def policy_api_get_block_by_tag_name(
        self, policy_id: str, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Requests block data by tag. Only users with a role that described in block are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        tag_name : str
            Policy block tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_get_block_by_tag_name(
            policy_id="652745597a7b53526de37c05",
            tag_name="someTag",
        )
        """
        _response = self._raw_client.policy_api_get_block_by_tag_name(
            policy_id, tag_name, request_options=request_options
        )
        return _response.data

    def policy_api_get_block_parents(
        self, policy_id: str, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        policy_id : str
            Policy identifier

        uuid_ : str
            Block identifier

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
        client.policies.policy_api_get_block_parents(
            policy_id="652745597a7b53526de37c05",
            uuid_="652745597a7b53526de37c05",
        )
        """
        _response = self._raw_client.policy_api_get_block_parents(policy_id, uuid_, request_options=request_options)
        return _response.data

    def return_policy_and_its_artifacts_in_a_zip_file_format_for_the_specified_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportPolicy:
        """
        Returns a zip file containing the published policy and all associated artifacts, i.e. schemas and VCs. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportPolicy
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.return_policy_and_its_artifacts_in_a_zip_file_format_for_the_specified_policy(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.return_policy_and_its_artifacts_in_a_zip_file_format_for_the_specified_policy(
            policy_id, request_options=request_options
        )
        return _response.data

    def return_heder_message_id_for_the_specified_published_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportPolicy:
        """
        Returns the Hedera message ID for the specified policy published onto IPFS. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportPolicy
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.return_heder_message_id_for_the_specified_published_policy(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.return_heder_message_id_for_the_specified_published_policy(
            policy_id, request_options=request_options
        )
        return _response.data

    def policy_api_get_policy_export_xlsx(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Returns a xlsx file containing the published policy and all associated artifacts, i.e. schemas and VCs. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_get_policy_export_xlsx(
            policy_id="policyId",
        )
        """
        with self._raw_client.policy_api_get_policy_export_xlsx(policy_id, request_options=request_options) as r:
            yield from r.data

    def imports_new_policy_from_ipfs(
        self,
        *,
        version_of_topic_id: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PolicyConfig]:
        """
        Imports new policy and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        version_of_topic_id : typing.Optional[str]
            The topic ID of policy version.

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PolicyConfig]
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.imports_new_policy_from_ipfs(
            version_of_topic_id="0.0.00000001",
        )
        """
        _response = self._raw_client.imports_new_policy_from_ipfs(
            version_of_topic_id=version_of_topic_id, message_id=message_id, request_options=request_options
        )
        return _response.data

    def imports_new_policy_and_all_associated_artifacts_from_ipfs_into_the_local_db(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Imports new policy and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.imports_new_policy_and_all_associated_artifacts_from_ipfs_into_the_local_db()
        """
        _response = self._raw_client.imports_new_policy_and_all_associated_artifacts_from_ipfs_into_the_local_db(
            message_id=message_id, request_options=request_options
        )
        return _response.data

    def policy_preview_from_ipfs(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PreviewPolicy:
        """
        Previews the policy from IPFS without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewPolicy
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_preview_from_ipfs()
        """
        _response = self._raw_client.policy_preview_from_ipfs(message_id=message_id, request_options=request_options)
        return _response.data

    def previews_the_policy_from_ipfs_without_loading_it_into_the_local_db(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Previews the policy from IPFS without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.previews_the_policy_from_ipfs_without_loading_it_into_the_local_db()
        """
        _response = self._raw_client.previews_the_policy_from_ipfs_without_loading_it_into_the_local_db(
            message_id=message_id, request_options=request_options
        )
        return _response.data

    def imports_new_policy_from_a_zip_file(
        self,
        *,
        version_of_topic_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PolicyConfig]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        version_of_topic_id : typing.Optional[str]
            The topic ID of policy version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PolicyConfig]
            Created.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.imports_new_policy_from_a_zip_file(
            version_of_topic_id="0.0.00000001",
        )
        """
        _response = self._raw_client.imports_new_policy_from_a_zip_file(
            version_of_topic_id=version_of_topic_id, request_options=request_options
        )
        return _response.data

    def policy_api_import_policy_from_file_with_metadata(
        self,
        *,
        version_of_topic_id: typing.Optional[str] = None,
        policy_file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        version_of_topic_id : typing.Optional[str]
            Topic Id

        policy_file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_import_policy_from_file_with_metadata()
        """
        _response = self._raw_client.policy_api_import_policy_from_file_with_metadata(
            version_of_topic_id=version_of_topic_id,
            policy_file=policy_file,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def imports_new_policy_and_all_associated_artifacts_such_as_schemas_and_v_cs_from_the_provided_zip_file_into_the_local_db(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.imports_new_policy_and_all_associated_artifacts_such_as_schemas_and_v_cs_from_the_provided_zip_file_into_the_local_db()
        """
        _response = self._raw_client.imports_new_policy_and_all_associated_artifacts_such_as_schemas_and_v_cs_from_the_provided_zip_file_into_the_local_db(
            request_options=request_options
        )
        return _response.data

    def policy_api_import_policy_from_file_with_metadata_async(
        self,
        *,
        version_of_topic_id: typing.Optional[str] = None,
        policy_file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        version_of_topic_id : typing.Optional[str]
            Topic Id

        policy_file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_import_policy_from_file_with_metadata_async()
        """
        _response = self._raw_client.policy_api_import_policy_from_file_with_metadata_async(
            version_of_topic_id=version_of_topic_id,
            policy_file=policy_file,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def policy_preview_from_a_zip_file(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreviewPolicy:
        """
        Previews the policy from a zip file without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewPolicy
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_preview_from_a_zip_file()
        """
        _response = self._raw_client.policy_preview_from_a_zip_file(request_options=request_options)
        return _response.data

    def policy_api_import_policy_from_xlsx(
        self, *, policy_id: str, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided xlsx file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_import_policy_from_xlsx(
            policy_id="policyId",
            request="string",
        )
        """
        _response = self._raw_client.policy_api_import_policy_from_xlsx(
            policy_id=policy_id, request=request, request_options=request_options
        )
        return _response.data

    def policy_api_import_policy_from_xlsx_async(
        self, *, policy_id: str, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided xlsx file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_import_policy_from_xlsx_async(
            policy_id="policyId",
            request="string",
        )
        """
        _response = self._raw_client.policy_api_import_policy_from_xlsx_async(
            policy_id=policy_id, request=request, request_options=request_options
        )
        return _response.data

    def policy_api_import_policy_from_xlsx_preview(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Previews the policy from a xlsx file without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_import_policy_from_xlsx_preview(
            request="string",
        )
        """
        _response = self._raw_client.policy_api_import_policy_from_xlsx_preview(
            request=request, request_options=request_options
        )
        return _response.data

    def policy_api_get_block_about(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
        client.policies.policy_api_get_block_about()
        """
        _response = self._raw_client.policy_api_get_block_about(request_options=request_options)
        return _response.data

    def returns_all_virtual_users(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetPoliciesPolicyIdDryRunUsersResponseItem]:
        """
        Returns all virtual users. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesPolicyIdDryRunUsersResponseItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.returns_all_virtual_users(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.returns_all_virtual_users(policy_id, request_options=request_options)
        return _response.data

    def create_a_new_virtual_account(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PostPoliciesPolicyIdDryRunUserResponseItem]:
        """
        Create a new virtual account. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PostPoliciesPolicyIdDryRunUserResponseItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.create_a_new_virtual_account(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.create_a_new_virtual_account(policy_id, request_options=request_options)
        return _response.data

    def logs_virtual_user_into_the_system(
        self,
        policy_id: str,
        *,
        did: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PostPoliciesPolicyIdDryRunLoginResponseItem]:
        """
        Logs virtual user into the system. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        did : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PostPoliciesPolicyIdDryRunLoginResponseItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.logs_virtual_user_into_the_system(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.logs_virtual_user_into_the_system(
            policy_id, did=did, request_options=request_options
        )
        return _response.data

    def restarts_the_execution_of_the_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Restarts the execution of the policy. Clear data in database. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

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
        client.policies.restarts_the_execution_of_the_policy(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.restarts_the_execution_of_the_policy(policy_id, request_options=request_options)
        return _response.data

    def returns_lists_of_virtual_transactions(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetPoliciesPolicyIdDryRunTransactionsResponseItem]:
        """
        Returns lists of virtual transactions. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesPolicyIdDryRunTransactionsResponseItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.returns_lists_of_virtual_transactions(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.returns_lists_of_virtual_transactions(policy_id, request_options=request_options)
        return _response.data

    def returns_lists_of_virtual_artifacts(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetPoliciesPolicyIdDryRunIpfsResponseItem]:
        """
        Returns lists of virtual artifacts. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesPolicyIdDryRunIpfsResponseItem]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.returns_lists_of_virtual_artifacts(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.returns_lists_of_virtual_artifacts(policy_id, request_options=request_options)
        return _response.data

    def requests_multi_policy_config(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MultiPolicyConfig:
        """
        Requests Multi policy config.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MultiPolicyConfig
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.requests_multi_policy_config(
            policy_id="policyId",
        )
        """
        _response = self._raw_client.requests_multi_policy_config(policy_id, request_options=request_options)
        return _response.data

    def creates_multi_policy_config(
        self,
        policy_id: str,
        *,
        main_policy_topic_id: str,
        synchronization_topic_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MultiPolicyConfig:
        """
        Creates a link between the current policy and the main policy. Or creates a group making the current policy the main one.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        main_policy_topic_id : str

        synchronization_topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MultiPolicyConfig
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.creates_multi_policy_config(
            policy_id="policyId",
            main_policy_topic_id="mainPolicyTopicId",
            synchronization_topic_id="synchronizationTopicId",
        )
        """
        _response = self._raw_client.creates_multi_policy_config(
            policy_id,
            main_policy_topic_id=main_policy_topic_id,
            synchronization_topic_id=synchronization_topic_id,
            request_options=request_options,
        )
        return _response.data

    def policy_api_get_policy_categories_async(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PolicyCategoryDto]:
        """
        Get all categories

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PolicyCategoryDto]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_get_policy_categories_async()
        """
        _response = self._raw_client.policy_api_get_policy_categories_async(request_options=request_options)
        return _response.data

    def policy_api_get_policies_by_category(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get policies by categories and text

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.policy_api_get_policies_by_category(
            request="string",
        )
        """
        _response = self._raw_client.policy_api_get_policies_by_category(
            request=request, request_options=request_options
        )
        return _response.data

    def requests_block_id_from_a_policy_by_tag(
        self, policy_id: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPoliciesPolicyIdTagTagResponse:
        """
        Requests block ID from a policy by tag. Only users with the Standard Registry and Installer roles are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        tag : str
            Tag from the selected policy.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPoliciesPolicyIdTagTagResponse
            Successful operation.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.policies.requests_block_id_from_a_policy_by_tag(
            policy_id="policyId",
            tag="tag",
        )
        """
        _response = self._raw_client.requests_block_id_from_a_policy_by_tag(
            policy_id, tag, request_options=request_options
        )
        return _response.data


class AsyncPoliciesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPoliciesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPoliciesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPoliciesClient
        """
        return self._raw_client

    async def return_a_list_of_all_policies(
        self,
        *,
        page_index: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetPoliciesResponseItem]:
        """
        Returns all policies. Only users with the Standard Registry and Installer role are allowed to make the request.

        Parameters
        ----------
        page_index : typing.Optional[int]
            The number of pages to skip before starting to collect the result set

        page_size : typing.Optional[int]
            The numbers of items to return

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesResponseItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.return_a_list_of_all_policies()


        asyncio.run(main())
        """
        _response = await self._raw_client.return_a_list_of_all_policies(
            page_index=page_index, page_size=page_size, request_options=request_options
        )
        return _response.data

    async def creates_a_new_policy(
        self,
        *,
        name: str,
        version: str,
        description: str,
        topic_description: str,
        config: typing.Dict[str, typing.Any],
        topic_id: str,
        policy_tag: str,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        policy_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        policy_topics: typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Creates a new policy. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        name : str

        version : str

        description : str

        topic_description : str

        config : typing.Dict[str, typing.Any]

        topic_id : str

        policy_tag : str

        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        status : typing.Optional[str]

        owner : typing.Optional[str]

        policy_roles : typing.Optional[typing.Sequence[str]]

        policy_topics : typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.creates_a_new_policy(
                name="name",
                version="version",
                description="description",
                topic_description="topicDescription",
                config={"key": "value"},
                topic_id="topicId",
                policy_tag="policyTag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_a_new_policy(
            name=name,
            version=version,
            description=description,
            topic_description=topic_description,
            config=config,
            topic_id=topic_id,
            policy_tag=policy_tag,
            id=id,
            uuid_=uuid_,
            status=status,
            owner=owner,
            policy_roles=policy_roles,
            policy_topics=policy_topics,
            request_options=request_options,
        )
        return _response.data

    async def policy_api_migrate_data(
        self,
        *,
        policies: MigrationConfigPoliciesDto,
        vcs: typing.Sequence[str],
        vps: typing.Sequence[str],
        schemas: typing.Dict[str, typing.Any],
        groups: typing.Dict[str, typing.Any],
        roles: typing.Dict[str, typing.Any],
        blocks: typing.Dict[str, typing.Any],
        tokens: typing.Dict[str, typing.Any],
        migrate_state: bool,
        migrate_retire_pools: bool,
        edited_v_cs: typing.Dict[str, typing.Any],
        retire_contract_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PolicyApiMigrateDataResponseItem]:
        """
        Migrate policy data. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policies : MigrationConfigPoliciesDto

        vcs : typing.Sequence[str]

        vps : typing.Sequence[str]

        schemas : typing.Dict[str, typing.Any]

        groups : typing.Dict[str, typing.Any]

        roles : typing.Dict[str, typing.Any]

        blocks : typing.Dict[str, typing.Any]

        tokens : typing.Dict[str, typing.Any]

        migrate_state : bool

        migrate_retire_pools : bool

        edited_v_cs : typing.Dict[str, typing.Any]

        retire_contract_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PolicyApiMigrateDataResponseItem]
            Errors while migration.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MigrationConfigPoliciesDto

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_migrate_data(
                policies=MigrationConfigPoliciesDto(
                    src="src",
                    dst="dst",
                ),
                vcs=["vcs"],
                vps=["vps"],
                schemas={"key": "value"},
                groups={"key": "value"},
                roles={"key": "value"},
                blocks={"key": "value"},
                tokens={"key": "value"},
                migrate_state=True,
                migrate_retire_pools=True,
                edited_v_cs={"key": "value"},
                retire_contract_id="retireContractId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_migrate_data(
            policies=policies,
            vcs=vcs,
            vps=vps,
            schemas=schemas,
            groups=groups,
            roles=roles,
            blocks=blocks,
            tokens=tokens,
            migrate_state=migrate_state,
            migrate_retire_pools=migrate_retire_pools,
            edited_v_cs=edited_v_cs,
            retire_contract_id=retire_contract_id,
            request_options=request_options,
        )
        return _response.data

    async def policy_api_migrate_data_async(
        self,
        *,
        policies: MigrationConfigPoliciesDto,
        vcs: typing.Sequence[str],
        vps: typing.Sequence[str],
        schemas: typing.Dict[str, typing.Any],
        groups: typing.Dict[str, typing.Any],
        roles: typing.Dict[str, typing.Any],
        blocks: typing.Dict[str, typing.Any],
        tokens: typing.Dict[str, typing.Any],
        migrate_state: bool,
        migrate_retire_pools: bool,
        edited_v_cs: typing.Dict[str, typing.Any],
        retire_contract_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Migrate policy data asynchronous. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policies : MigrationConfigPoliciesDto

        vcs : typing.Sequence[str]

        vps : typing.Sequence[str]

        schemas : typing.Dict[str, typing.Any]

        groups : typing.Dict[str, typing.Any]

        roles : typing.Dict[str, typing.Any]

        blocks : typing.Dict[str, typing.Any]

        tokens : typing.Dict[str, typing.Any]

        migrate_state : bool

        migrate_retire_pools : bool

        edited_v_cs : typing.Dict[str, typing.Any]

        retire_contract_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Created task.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MigrationConfigPoliciesDto

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_migrate_data_async(
                policies=MigrationConfigPoliciesDto(
                    src="src",
                    dst="dst",
                ),
                vcs=["vcs"],
                vps=["vps"],
                schemas={"key": "value"},
                groups={"key": "value"},
                roles={"key": "value"},
                blocks={"key": "value"},
                tokens={"key": "value"},
                migrate_state=True,
                migrate_retire_pools=True,
                edited_v_cs={"key": "value"},
                retire_contract_id="retireContractId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_migrate_data_async(
            policies=policies,
            vcs=vcs,
            vps=vps,
            schemas=schemas,
            groups=groups,
            roles=roles,
            blocks=blocks,
            tokens=tokens,
            migrate_state=migrate_state,
            migrate_retire_pools=migrate_retire_pools,
            edited_v_cs=edited_v_cs,
            retire_contract_id=retire_contract_id,
            request_options=request_options,
        )
        return _response.data

    async def policy_api_update_policy_async(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Parameters
        ----------
        policy_id : str
            Policy identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_update_policy_async(
                policy_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_update_policy_async(policy_id, request_options=request_options)
        return _response.data

    async def policy_api_delete_policy_async(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        policy_id : str
            Policy identifier

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
            await client.policies.policy_api_delete_policy_async(
                policy_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_delete_policy_async(policy_id, request_options=request_options)
        return _response.data

    async def retrieves_policy_configuration(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPoliciesPolicyIdResponse:
        """
        Retrieves policy configuration for the specified policy ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPoliciesPolicyIdResponse
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.retrieves_policy_configuration(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieves_policy_configuration(policy_id, request_options=request_options)
        return _response.data

    async def updates_policy_configuration(
        self,
        policy_id: str,
        *,
        name: str,
        version: str,
        description: str,
        topic_description: str,
        config: typing.Dict[str, typing.Any],
        topic_id: str,
        policy_tag: str,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        policy_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        policy_topics: typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyConfig:
        """
        Updates policy configuration for the specified policy ID. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        name : str

        version : str

        description : str

        topic_description : str

        config : typing.Dict[str, typing.Any]

        topic_id : str

        policy_tag : str

        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        status : typing.Optional[str]

        owner : typing.Optional[str]

        policy_roles : typing.Optional[typing.Sequence[str]]

        policy_topics : typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyConfig
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.updates_policy_configuration(
                policy_id="policyId",
                name="name",
                version="version",
                description="description",
                topic_description="topicDescription",
                config={"key": "value"},
                topic_id="topicId",
                policy_tag="policyTag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updates_policy_configuration(
            policy_id,
            name=name,
            version=version,
            description=description,
            topic_description=topic_description,
            config=config,
            topic_id=topic_id,
            policy_tag=policy_tag,
            id=id,
            uuid_=uuid_,
            status=status,
            owner=owner,
            policy_roles=policy_roles,
            policy_topics=policy_topics,
            request_options=request_options,
        )
        return _response.data

    async def publishes_the_policy_onto_ipfs(
        self,
        policy_id: str,
        *,
        policy_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PublishPolicy:
        """
        Publishes the policy with the specified (internal) policy ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        policy_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishPolicy
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.publishes_the_policy_onto_ipfs(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publishes_the_policy_onto_ipfs(
            policy_id, policy_version=policy_version, request_options=request_options
        )
        return _response.data

    async def publishes_the_policy_with_the_specified_internal_policy_id_onto_ipfs_sends_a_message_featuring_its_ipfs_cid_into_the_corresponding_hedera_topic(
        self,
        policy_id: str,
        *,
        policy_version: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Task:
        """
        Publishes the policy with the specified (internal) policy ID onto IPFS, sends a message featuring its IPFS CID into the corresponding Hedera topic. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        policy_version : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.publishes_the_policy_with_the_specified_internal_policy_id_onto_ipfs_sends_a_message_featuring_its_ipfs_cid_into_the_corresponding_hedera_topic(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.publishes_the_policy_with_the_specified_internal_policy_id_onto_ipfs_sends_a_message_featuring_its_ipfs_cid_into_the_corresponding_hedera_topic(
            policy_id, policy_version=policy_version, request_options=request_options
        )
        return _response.data

    async def dry_run_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishPolicy:
        """
        Run policy without making any persistent changes or executing transaction. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishPolicy
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.dry_run_policy(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.dry_run_policy(policy_id, request_options=request_options)
        return _response.data

    async def policy_api_discontinue_policy(
        self,
        policy_id: typing.Any,
        *,
        date: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Discontunue policy. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        date : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Policies.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_discontinue_policy(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_discontinue_policy(
            policy_id, date=date, request_options=request_options
        )
        return _response.data

    async def return_policy_to_editing(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PublishPolicy:
        """
        Return policy to editing. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublishPolicy
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.return_policy_to_editing(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_policy_to_editing(policy_id, request_options=request_options)
        return _response.data

    async def validates_policy(
        self,
        *,
        name: str,
        version: str,
        description: str,
        topic_description: str,
        config: typing.Dict[str, typing.Any],
        topic_id: str,
        policy_tag: str,
        id: typing.Optional[str] = OMIT,
        uuid_: typing.Optional[str] = OMIT,
        status: typing.Optional[str] = OMIT,
        owner: typing.Optional[str] = OMIT,
        policy_roles: typing.Optional[typing.Sequence[str]] = OMIT,
        policy_topics: typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ValidatePolicy:
        """
        Validates selected policy. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        name : str

        version : str

        description : str

        topic_description : str

        config : typing.Dict[str, typing.Any]

        topic_id : str

        policy_tag : str

        id : typing.Optional[str]

        uuid_ : typing.Optional[str]

        status : typing.Optional[str]

        owner : typing.Optional[str]

        policy_roles : typing.Optional[typing.Sequence[str]]

        policy_topics : typing.Optional[typing.Sequence[PolicyConfigPolicyTopicsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ValidatePolicy
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.validates_policy(
                name="name",
                version="version",
                description="description",
                topic_description="topicDescription",
                config={"key": "value"},
                topic_id="topicId",
                policy_tag="policyTag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validates_policy(
            name=name,
            version=version,
            description=description,
            topic_description=topic_description,
            config=config,
            topic_id=topic_id,
            policy_tag=policy_tag,
            id=id,
            uuid_=uuid_,
            status=status,
            owner=owner,
            policy_roles=policy_roles,
            policy_topics=policy_topics,
            request_options=request_options,
        )
        return _response.data

    async def policy_api_get_policy_navigation(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Returns a policy navigation.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_get_policy_navigation(
                policy_id="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_get_policy_navigation(policy_id, request_options=request_options)
        return _response.data

    async def returns_a_list_of_groups_the_user_is_a_member_of(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetPoliciesPolicyIdGroupsResponseItem]:
        """
        Returns a list of groups the user is a member of.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesPolicyIdGroupsResponseItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.returns_a_list_of_groups_the_user_is_a_member_of(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_a_list_of_groups_the_user_is_a_member_of(
            policy_id, request_options=request_options
        )
        return _response.data

    async def makes_the_selected_group_active(
        self,
        policy_id: str,
        *,
        uuid_: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Makes the selected group active. if UUID is not set then returns the user to the default state.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        uuid_ : typing.Optional[str]

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
            await client.policies.makes_the_selected_group_active(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.makes_the_selected_group_active(
            policy_id, uuid_=uuid_, request_options=request_options
        )
        return _response.data

    async def policy_api_get_policy_documents(
        self,
        policy_id: typing.Any,
        *,
        page_size: float,
        page_index: float,
        type: PolicyApiGetPolicyDocumentsRequestType,
        include_document: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[typing.Dict[str, typing.Any]]:
        """
        Get policy documents. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        page_size : float
            Page size.

        page_index : float
            Page index.

        type : PolicyApiGetPolicyDocumentsRequestType
            Document type.

        include_document : bool
            Include document field.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[typing.Dict[str, typing.Any]]
            Documents.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_get_policy_documents(
                policy_id="policyId",
                page_size=1.1,
                page_index=1.1,
                type="VC",
                include_document=True,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_get_policy_documents(
            policy_id,
            page_size=page_size,
            page_index=page_index,
            type=type,
            include_document=include_document,
            request_options=request_options,
        )
        return _response.data

    async def policy_api_download_policy_data(
        self, policy_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Get policy data. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Policy data.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_download_policy_data(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.policy_api_download_policy_data(policy_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def policy_api_upload_policy_data(
        self, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Upload policy data. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request : bytes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Uploaded policy.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_upload_policy_data(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_upload_policy_data(
            request=request, request_options=request_options
        )
        return _response.data

    async def policy_api_get_tag_block_map(
        self, policy_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get policy tag block map. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Policy tag block map.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_get_tag_block_map(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_get_tag_block_map(policy_id, request_options=request_options)
        return _response.data

    async def policy_api_download_virtual_keys(
        self, policy_id: typing.Any, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Get policy virtual keys. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Policy virtual keys.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_download_virtual_keys(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.policy_api_download_virtual_keys(policy_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def policy_api_upload_virtual_keys(
        self, policy_id: typing.Any, *, request: bytes, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Upload policy virtual keys. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : typing.Any
            Policy identifier.

        request : bytes

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
            await client.policies.policy_api_upload_virtual_keys(
                policy_id="policyId",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_upload_virtual_keys(
            policy_id, request=request, request_options=request_options
        )
        return _response.data

    async def retrieves_data_for_the_policy_root_block(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PolicyBlock:
        """
        Returns data from the root policy block. Only users with the Standard Registry and Installer role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBlock
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.retrieves_data_for_the_policy_root_block(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.retrieves_data_for_the_policy_root_block(
            policy_id, request_options=request_options
        )
        return _response.data

    async def requests_block_data(
        self, policy_id: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PolicyBlockData:
        """
        Requests block data by tag. Only users with a role that described in block are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        tag : str
            Tag from the selected policy.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBlockData
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.requests_block_data(
                policy_id="policyId",
                tag="tag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.requests_block_data(policy_id, tag, request_options=request_options)
        return _response.data

    async def sends_data_to_the_specified_block(
        self,
        policy_id: str,
        tag: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PolicyBlockData:
        """
        Sends data to the specified block.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        tag : str
            Tag from the selected policy.

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PolicyBlockData
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.sends_data_to_the_specified_block(
                policy_id="policyId",
                tag="tag",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sends_data_to_the_specified_block(
            policy_id, tag, request=request, request_options=request_options
        )
        return _response.data

    async def policy_api_get_blocks_by_tag_name(
        self, policy_id: str, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Requests block data by tag. Only users with a role that described in block are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        tag_name : str
            Policy block tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_get_blocks_by_tag_name(
                policy_id="652745597a7b53526de37c05",
                tag_name="someTag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_get_blocks_by_tag_name(
            policy_id, tag_name, request_options=request_options
        )
        return _response.data

    async def policy_api_set_blocks_by_tag_name(
        self, policy_id: str, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Sends data to the specified block.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        tag_name : str
            Policy block tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_set_blocks_by_tag_name(
                policy_id="652745597a7b53526de37c05",
                tag_name="someTag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_set_blocks_by_tag_name(
            policy_id, tag_name, request_options=request_options
        )
        return _response.data

    async def policy_api_get_block_by_tag_name(
        self, policy_id: str, tag_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Requests block data by tag. Only users with a role that described in block are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy identifier

        tag_name : str
            Policy block tag

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_get_block_by_tag_name(
                policy_id="652745597a7b53526de37c05",
                tag_name="someTag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_get_block_by_tag_name(
            policy_id, tag_name, request_options=request_options
        )
        return _response.data

    async def policy_api_get_block_parents(
        self, policy_id: str, uuid_: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        policy_id : str
            Policy identifier

        uuid_ : str
            Block identifier

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
            await client.policies.policy_api_get_block_parents(
                policy_id="652745597a7b53526de37c05",
                uuid_="652745597a7b53526de37c05",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_get_block_parents(
            policy_id, uuid_, request_options=request_options
        )
        return _response.data

    async def return_policy_and_its_artifacts_in_a_zip_file_format_for_the_specified_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportPolicy:
        """
        Returns a zip file containing the published policy and all associated artifacts, i.e. schemas and VCs. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportPolicy
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.return_policy_and_its_artifacts_in_a_zip_file_format_for_the_specified_policy(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = (
            await self._raw_client.return_policy_and_its_artifacts_in_a_zip_file_format_for_the_specified_policy(
                policy_id, request_options=request_options
            )
        )
        return _response.data

    async def return_heder_message_id_for_the_specified_published_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ExportPolicy:
        """
        Returns the Hedera message ID for the specified policy published onto IPFS. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ExportPolicy
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.return_heder_message_id_for_the_specified_published_policy(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.return_heder_message_id_for_the_specified_published_policy(
            policy_id, request_options=request_options
        )
        return _response.data

    async def policy_api_get_policy_export_xlsx(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Returns a xlsx file containing the published policy and all associated artifacts, i.e. schemas and VCs. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_get_policy_export_xlsx(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        async with self._raw_client.policy_api_get_policy_export_xlsx(policy_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def imports_new_policy_from_ipfs(
        self,
        *,
        version_of_topic_id: typing.Optional[str] = None,
        message_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PolicyConfig]:
        """
        Imports new policy and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        version_of_topic_id : typing.Optional[str]
            The topic ID of policy version.

        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PolicyConfig]
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.imports_new_policy_from_ipfs(
                version_of_topic_id="0.0.00000001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.imports_new_policy_from_ipfs(
            version_of_topic_id=version_of_topic_id, message_id=message_id, request_options=request_options
        )
        return _response.data

    async def imports_new_policy_and_all_associated_artifacts_from_ipfs_into_the_local_db(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Imports new policy and all associated artifacts from IPFS into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.imports_new_policy_and_all_associated_artifacts_from_ipfs_into_the_local_db()


        asyncio.run(main())
        """
        _response = await self._raw_client.imports_new_policy_and_all_associated_artifacts_from_ipfs_into_the_local_db(
            message_id=message_id, request_options=request_options
        )
        return _response.data

    async def policy_preview_from_ipfs(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> PreviewPolicy:
        """
        Previews the policy from IPFS without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewPolicy
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_preview_from_ipfs()


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_preview_from_ipfs(
            message_id=message_id, request_options=request_options
        )
        return _response.data

    async def previews_the_policy_from_ipfs_without_loading_it_into_the_local_db(
        self, *, message_id: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Previews the policy from IPFS without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        message_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.previews_the_policy_from_ipfs_without_loading_it_into_the_local_db()


        asyncio.run(main())
        """
        _response = await self._raw_client.previews_the_policy_from_ipfs_without_loading_it_into_the_local_db(
            message_id=message_id, request_options=request_options
        )
        return _response.data

    async def imports_new_policy_from_a_zip_file(
        self,
        *,
        version_of_topic_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PolicyConfig]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        version_of_topic_id : typing.Optional[str]
            The topic ID of policy version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PolicyConfig]
            Created.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.imports_new_policy_from_a_zip_file(
                version_of_topic_id="0.0.00000001",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.imports_new_policy_from_a_zip_file(
            version_of_topic_id=version_of_topic_id, request_options=request_options
        )
        return _response.data

    async def policy_api_import_policy_from_file_with_metadata(
        self,
        *,
        version_of_topic_id: typing.Optional[str] = None,
        policy_file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        version_of_topic_id : typing.Optional[str]
            Topic Id

        policy_file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_import_policy_from_file_with_metadata()


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_import_policy_from_file_with_metadata(
            version_of_topic_id=version_of_topic_id,
            policy_file=policy_file,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def imports_new_policy_and_all_associated_artifacts_such_as_schemas_and_v_cs_from_the_provided_zip_file_into_the_local_db(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Task:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Task
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.imports_new_policy_and_all_associated_artifacts_such_as_schemas_and_v_cs_from_the_provided_zip_file_into_the_local_db()


        asyncio.run(main())
        """
        _response = await self._raw_client.imports_new_policy_and_all_associated_artifacts_such_as_schemas_and_v_cs_from_the_provided_zip_file_into_the_local_db(
            request_options=request_options
        )
        return _response.data

    async def policy_api_import_policy_from_file_with_metadata_async(
        self,
        *,
        version_of_topic_id: typing.Optional[str] = None,
        policy_file: typing.Optional[core.File] = OMIT,
        metadata: typing.Optional[core.File] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided zip file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        version_of_topic_id : typing.Optional[str]
            Topic Id

        policy_file : typing.Optional[core.File]
            See core.File for more documentation

        metadata : typing.Optional[core.File]
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_import_policy_from_file_with_metadata_async()


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_import_policy_from_file_with_metadata_async(
            version_of_topic_id=version_of_topic_id,
            policy_file=policy_file,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def policy_preview_from_a_zip_file(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> PreviewPolicy:
        """
        Previews the policy from a zip file without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PreviewPolicy
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_preview_from_a_zip_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_preview_from_a_zip_file(request_options=request_options)
        return _response.data

    async def policy_api_import_policy_from_xlsx(
        self, *, policy_id: str, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided xlsx file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_import_policy_from_xlsx(
                policy_id="policyId",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_import_policy_from_xlsx(
            policy_id=policy_id, request=request, request_options=request_options
        )
        return _response.data

    async def policy_api_import_policy_from_xlsx_async(
        self, *, policy_id: str, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Imports new policy and all associated artifacts, such as schemas and VCs, from the provided xlsx file into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy Id

        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_import_policy_from_xlsx_async(
                policy_id="policyId",
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_import_policy_from_xlsx_async(
            policy_id=policy_id, request=request, request_options=request_options
        )
        return _response.data

    async def policy_api_import_policy_from_xlsx_preview(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Previews the policy from a xlsx file without loading it into the local DB. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_import_policy_from_xlsx_preview(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_import_policy_from_xlsx_preview(
            request=request, request_options=request_options
        )
        return _response.data

    async def policy_api_get_block_about(self, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
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
            await client.policies.policy_api_get_block_about()


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_get_block_about(request_options=request_options)
        return _response.data

    async def returns_all_virtual_users(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetPoliciesPolicyIdDryRunUsersResponseItem]:
        """
        Returns all virtual users. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesPolicyIdDryRunUsersResponseItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.returns_all_virtual_users(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_all_virtual_users(policy_id, request_options=request_options)
        return _response.data

    async def create_a_new_virtual_account(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PostPoliciesPolicyIdDryRunUserResponseItem]:
        """
        Create a new virtual account. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PostPoliciesPolicyIdDryRunUserResponseItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.create_a_new_virtual_account(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_a_new_virtual_account(policy_id, request_options=request_options)
        return _response.data

    async def logs_virtual_user_into_the_system(
        self,
        policy_id: str,
        *,
        did: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[PostPoliciesPolicyIdDryRunLoginResponseItem]:
        """
        Logs virtual user into the system. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        did : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PostPoliciesPolicyIdDryRunLoginResponseItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.logs_virtual_user_into_the_system(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.logs_virtual_user_into_the_system(
            policy_id, did=did, request_options=request_options
        )
        return _response.data

    async def restarts_the_execution_of_the_policy(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Restarts the execution of the policy. Clear data in database. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

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
            await client.policies.restarts_the_execution_of_the_policy(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.restarts_the_execution_of_the_policy(
            policy_id, request_options=request_options
        )
        return _response.data

    async def returns_lists_of_virtual_transactions(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetPoliciesPolicyIdDryRunTransactionsResponseItem]:
        """
        Returns lists of virtual transactions. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesPolicyIdDryRunTransactionsResponseItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.returns_lists_of_virtual_transactions(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_lists_of_virtual_transactions(
            policy_id, request_options=request_options
        )
        return _response.data

    async def returns_lists_of_virtual_artifacts(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[GetPoliciesPolicyIdDryRunIpfsResponseItem]:
        """
        Returns lists of virtual artifacts. Only users with the Standard Registry role are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetPoliciesPolicyIdDryRunIpfsResponseItem]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.returns_lists_of_virtual_artifacts(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.returns_lists_of_virtual_artifacts(
            policy_id, request_options=request_options
        )
        return _response.data

    async def requests_multi_policy_config(
        self, policy_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> MultiPolicyConfig:
        """
        Requests Multi policy config.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MultiPolicyConfig
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.requests_multi_policy_config(
                policy_id="policyId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.requests_multi_policy_config(policy_id, request_options=request_options)
        return _response.data

    async def creates_multi_policy_config(
        self,
        policy_id: str,
        *,
        main_policy_topic_id: str,
        synchronization_topic_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MultiPolicyConfig:
        """
        Creates a link between the current policy and the main policy. Or creates a group making the current policy the main one.

        Parameters
        ----------
        policy_id : str
            Policy ID.

        main_policy_topic_id : str

        synchronization_topic_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MultiPolicyConfig
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.creates_multi_policy_config(
                policy_id="policyId",
                main_policy_topic_id="mainPolicyTopicId",
                synchronization_topic_id="synchronizationTopicId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.creates_multi_policy_config(
            policy_id,
            main_policy_topic_id=main_policy_topic_id,
            synchronization_topic_id=synchronization_topic_id,
            request_options=request_options,
        )
        return _response.data

    async def policy_api_get_policy_categories_async(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[PolicyCategoryDto]:
        """
        Get all categories

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[PolicyCategoryDto]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_get_policy_categories_async()


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_get_policy_categories_async(request_options=request_options)
        return _response.data

    async def policy_api_get_policies_by_category(
        self, *, request: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, typing.Any]:
        """
        Get policies by categories and text

        Parameters
        ----------
        request : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.policy_api_get_policies_by_category(
                request="string",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.policy_api_get_policies_by_category(
            request=request, request_options=request_options
        )
        return _response.data

    async def requests_block_id_from_a_policy_by_tag(
        self, policy_id: str, tag: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetPoliciesPolicyIdTagTagResponse:
        """
        Requests block ID from a policy by tag. Only users with the Standard Registry and Installer roles are allowed to make the request.

        Parameters
        ----------
        policy_id : str
            Selected policy ID.

        tag : str
            Tag from the selected policy.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetPoliciesPolicyIdTagTagResponse
            Successful operation.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.policies.requests_block_id_from_a_policy_by_tag(
                policy_id="policyId",
                tag="tag",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.requests_block_id_from_a_policy_by_tag(
            policy_id, tag, request_options=request_options
        )
        return _response.data
