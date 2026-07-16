# Reference
<details><summary><code>client.<a href="src/fern/client.py">get_activate_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Activates a public third-party extension, making it available for use in stack templates. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html">Using public extensions</a> in the <i>CloudFormation User Guide</i>.</p> <p>Once you have activated a public third-party extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetActivateTypeRequestAction, GetActivateTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_activate_type(
    action=GetActivateTypeRequestAction.ACTIVATE_TYPE,
    version=GetActivateTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetActivateTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetActivateTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetActivateTypeRequestType]` — <p>The extension type.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**public_type_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the public extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**publisher_id:** `typing.Optional[str]` — <p>The ID of the extension publisher.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The name of the extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name_alias:** `typing.Optional[str]` — <p>An alias to assign to the public extension, in this account and region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.</p> <p>An extension alias must be unique within a given account and region. You can activate the same public resource multiple times in the same account and region, using different type name aliases.</p>
    
</dd>
</dl>

<dl>
<dd>

**auto_update:** `typing.Optional[bool]` — <p>Whether to automatically update the extension in this account and region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated.</p> <p>The default is <code>true</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**logging_config:** `typing.Optional[GetActivateTypeRequestLoggingConfig]` — 
    
</dd>
</dl>

<dl>
<dd>

**execution_role_arn:** `typing.Optional[str]` — The name of the IAM execution role to use to activate the extension.
    
</dd>
</dl>

<dl>
<dd>

**version_bump:** `typing.Optional[GetActivateTypeRequestVersionBump]` — <p>Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of <code>AutoUpdate</code>.</p> <ul> <li> <p> <code>MAJOR</code>: CloudFormation updates the extension to the newest major version, if one is available.</p> </li> <li> <p> <code>MINOR</code>: CloudFormation updates the extension to the newest minor version, if one is available.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**major_version:** `typing.Optional[int]` — <p>The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available <i>minor</i> version of the major version selected.</p> <p>You can specify <code>MajorVersion</code> or <code>VersionBump</code>, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_activate_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Activates a public third-party extension, making it available for use in stack templates. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html">Using public extensions</a> in the <i>CloudFormation User Guide</i>.</p> <p>Once you have activated a public third-party extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostActivateTypeRequestAction, PostActivateTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_activate_type(
    action=PostActivateTypeRequestAction.ACTIVATE_TYPE,
    version=PostActivateTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostActivateTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostActivateTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_batch_describe_type_configurations</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry for the account and region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetBatchDescribeTypeConfigurationsRequestAction, GetBatchDescribeTypeConfigurationsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_batch_describe_type_configurations(
    action=GetBatchDescribeTypeConfigurationsRequestAction.BATCH_DESCRIBE_TYPE_CONFIGURATIONS,
    version=GetBatchDescribeTypeConfigurationsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetBatchDescribeTypeConfigurationsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetBatchDescribeTypeConfigurationsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**type_configuration_identifiers:** `typing.Optional[typing.Union[TypeConfigurationIdentifier, typing.Sequence[TypeConfigurationIdentifier]]]` — The list of identifiers for the desired extension configurations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_batch_describe_type_configurations</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry for the account and region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostBatchDescribeTypeConfigurationsRequestAction, PostBatchDescribeTypeConfigurationsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_batch_describe_type_configurations(
    action=PostBatchDescribeTypeConfigurationsRequestAction.BATCH_DESCRIBE_TYPE_CONFIGURATIONS,
    version=PostBatchDescribeTypeConfigurationsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostBatchDescribeTypeConfigurationsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostBatchDescribeTypeConfigurationsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_cancel_update_stack</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.</p> <note> <p>You can cancel only stacks that are in the <code>UPDATE_IN_PROGRESS</code> state.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetCancelUpdateStackRequestAction, GetCancelUpdateStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_cancel_update_stack(
    stack_name="StackName",
    action=GetCancelUpdateStackRequestAction.CANCEL_UPDATE_STACK,
    version=GetCancelUpdateStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name or the unique stack ID that's associated with the stack.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetCancelUpdateStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetCancelUpdateStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — A unique identifier for this <code>CancelUpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to cancel an update on a stack with the same name. You might retry <code>CancelUpdateStack</code> requests to ensure that CloudFormation successfully received them.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_cancel_update_stack</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.</p> <note> <p>You can cancel only stacks that are in the <code>UPDATE_IN_PROGRESS</code> state.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostCancelUpdateStackRequestAction, PostCancelUpdateStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_cancel_update_stack(
    action=PostCancelUpdateStackRequestAction.CANCEL_UPDATE_STACK,
    version=PostCancelUpdateStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostCancelUpdateStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostCancelUpdateStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_continue_update_rollback</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>For a specified stack that's in the <code>UPDATE_ROLLBACK_FAILED</code> state, continues rolling it back to the <code>UPDATE_ROLLBACK_COMPLETE</code> state. Depending on the cause of the failure, you can manually <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> fix the error</a> and continue the rollback. By continuing the rollback, you can return your stack to a working state (the <code>UPDATE_ROLLBACK_COMPLETE</code> state), and then try to update the stack again.</p> <p>A stack goes into the <code>UPDATE_ROLLBACK_FAILED</code> state when CloudFormation can't roll back all changes after a failed stack update. For example, you might have a stack that's rolling back to an old database instance that was deleted outside of CloudFormation. Because CloudFormation doesn't know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetContinueUpdateRollbackRequestAction, GetContinueUpdateRollbackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_continue_update_rollback(
    stack_name="x",
    action=GetContinueUpdateRollbackRequestAction.CONTINUE_UPDATE_ROLLBACK,
    version=GetContinueUpdateRollbackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — <p>The name or the unique ID of the stack that you want to continue rolling back.</p> <note> <p>Don't specify the name of a nested stack (a stack that was created by using the <code>AWS::CloudFormation::Stack</code> resource). Instead, use this operation on the parent stack (the stack that contains the <code>AWS::CloudFormation::Stack</code> resource).</p> </note>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetContinueUpdateRollbackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetContinueUpdateRollbackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**role_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to roll back the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>
    
</dd>
</dl>

<dl>
<dd>

**resources_to_skip:** `typing.Optional[typing.Union[ResourceToSkip, typing.Sequence[ResourceToSkip]]]` — <p>A list of the logical IDs of the resources that CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the <code>UPDATE_FAILED</code> state because a rollback failed. You can't specify resources that are in the <code>UPDATE_FAILED</code> state for other reasons, for example, because an update was canceled. To check why a resource update failed, use the <a>DescribeStackResources</a> action, and view the resource status reason.</p> <important> <p>Specify this property to skip rolling back resources that CloudFormation can't successfully roll back. We recommend that you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> troubleshoot</a> resources before skipping them. CloudFormation sets the status of the specified resources to <code>UPDATE_COMPLETE</code> and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don't, subsequent stack updates might fail, and the stack will become unrecoverable.</p> </important> <p>Specify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources.</p> <p>To skip resources that are part of nested stacks, use the following format: <code>NestedStackName.ResourceLogicalID</code>. If you want to specify the logical ID of a stack resource (<code>Type: AWS::CloudFormation::Stack</code>) in the <code>ResourcesToSkip</code> list, then its corresponding embedded stack must be in one of the following states: <code>DELETE_IN_PROGRESS</code>, <code>DELETE_COMPLETE</code>, or <code>DELETE_FAILED</code>.</p> <note> <p>Don't confuse a child stack's name with its corresponding logical ID defined in the parent stack. For an example of a continue update rollback operation with nested stacks, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html#nested-stacks">Using ResourcesToSkip to recover a nested stacks hierarchy</a>.</p> </note>
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — A unique identifier for this <code>ContinueUpdateRollback</code> request. Specify this token if you plan to retry requests so that CloudFormationknows that you're not attempting to continue the rollback to a stack with the same name. You might retry <code>ContinueUpdateRollback</code> requests to ensure that CloudFormation successfully received them.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_continue_update_rollback</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>For a specified stack that's in the <code>UPDATE_ROLLBACK_FAILED</code> state, continues rolling it back to the <code>UPDATE_ROLLBACK_COMPLETE</code> state. Depending on the cause of the failure, you can manually <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> fix the error</a> and continue the rollback. By continuing the rollback, you can return your stack to a working state (the <code>UPDATE_ROLLBACK_COMPLETE</code> state), and then try to update the stack again.</p> <p>A stack goes into the <code>UPDATE_ROLLBACK_FAILED</code> state when CloudFormation can't roll back all changes after a failed stack update. For example, you might have a stack that's rolling back to an old database instance that was deleted outside of CloudFormation. Because CloudFormation doesn't know the database was deleted, it assumes that the database instance still exists and attempts to roll back to it, causing the update rollback to fail.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostContinueUpdateRollbackRequestAction, PostContinueUpdateRollbackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_continue_update_rollback(
    action=PostContinueUpdateRollbackRequestAction.CONTINUE_UPDATE_ROLLBACK,
    version=PostContinueUpdateRollbackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostContinueUpdateRollbackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostContinueUpdateRollbackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_create_change_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.</p> <p>To create a change set for a stack that doesn't exist, for the <code>ChangeSetType</code> parameter, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code> for the <code>ChangeSetType</code> parameter. To create a change set for an import operation, specify <code>IMPORT</code> for the <code>ChangeSetType</code> parameter. After the <code>CreateChangeSet</code> call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the <a>DescribeChangeSet</a> action.</p> <p>When you are satisfied with the changes the change set will make, execute the change set by using the <a>ExecuteChangeSet</a> action. CloudFormation doesn't make changes until you execute the change set.</p> <p>To create a change set for the entire stack hierarchy, set <code>IncludeNestedStacks</code> to <code>True</code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetCreateChangeSetRequestAction, GetCreateChangeSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_create_change_set(
    stack_name="x",
    change_set_name="x",
    action=GetCreateChangeSetRequestAction.CREATE_CHANGE_SET,
    version=GetCreateChangeSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name or the unique ID of the stack for which you are creating a change set. CloudFormation generates the change set by comparing this stack's information with the information that you submit, such as a modified template or different parameter input values.
    
</dd>
</dl>

<dl>
<dd>

**change_set_name:** `str` — <p>The name of the change set. The name must be unique among all change sets that are associated with the specified stack.</p> <p>A change set name can contain only alphanumeric, case sensitive characters, and hyphens. It must start with an alphabetical character and can't exceed 128 characters.</p>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetCreateChangeSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetCreateChangeSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**template_body:** `typing.Optional[str]` — <p>A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. CloudFormation generates the change set by comparing this template with the template of the stack that you specified.</p> <p>Conditional: You must specify only <code>TemplateBody</code> or <code>TemplateURL</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**template_url:** `typing.Optional[str]` — <p>The location of the file that contains the revised template. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. CloudFormation generates the change set by comparing this template with the stack that you specified.</p> <p>Conditional: You must specify only <code>TemplateBody</code> or <code>TemplateURL</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**use_previous_template:** `typing.Optional[bool]` — Whether to reuse the template that's associated with the stack to create the change set.
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]` — A list of <code>Parameter</code> structures that specify input parameters for the change set. For more information, see the <a>Parameter</a> data type.
    
</dd>
</dl>

<dl>
<dd>

**capabilities:** `typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]` — <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <note> <p>This capacity doesn't apply to creating change sets, and specifying it when creating change sets has no effect.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create or update the stack directly from the template using the <a>CreateStack</a> or <a>UpdateStack</a> action, and specifying this capability.</p> </note> <p>For more information about macros, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation macros to perform custom processing on templates</a>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**resource_types:** `typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]]` — <p>The template resource types that you have permissions to work with if you execute this change set, such as <code>AWS::EC2::Instance</code>, <code>AWS::EC2::*</code>, or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource type that you're updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for condition keys in IAM policies for CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">Controlling access with Identity and Access Management</a> in the CloudFormation User Guide.</p>
    
</dd>
</dl>

<dl>
<dd>

**role_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes when executing the change set. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.</p>
    
</dd>
</dl>

<dl>
<dd>

**rollback_configuration:** `typing.Optional[GetCreateChangeSetRequestRollbackConfiguration]` — The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
    
</dd>
</dl>

<dl>
<dd>

**notification_ar_ns:** `typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]]` — The Amazon Resource Names (ARNs) of Amazon Simple Notification Service (Amazon SNS) topics that CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]` — Key-value pairs to associate with this stack. CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.
    
</dd>
</dl>

<dl>
<dd>

**client_token:** `typing.Optional[str]` — A unique identifier for this <code>CreateChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another change set with the same name. You might retry <code>CreateChangeSet</code> requests to ensure that CloudFormation successfully received them.
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description to help you identify this change set.
    
</dd>
</dl>

<dl>
<dd>

**change_set_type:** `typing.Optional[GetCreateChangeSetRequestChangeSetType]` — <p>The type of change set operation. To create a change set for a new stack, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code>. To create a change set for an import operation, specify <code>IMPORT</code>.</p> <p>If you create a change set for a new stack, CloudFormation creates a stack with a unique stack ID, but no template or resources. The stack will be in the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-describing-stacks.html#d0e11995"> <code>REVIEW_IN_PROGRESS</code> </a> state until you execute the change set.</p> <p>By default, CloudFormation specifies <code>UPDATE</code>. You can't use the <code>UPDATE</code> type to create a change set for a new stack or the <code>CREATE</code> type to create a change set for an existing stack.</p>
    
</dd>
</dl>

<dl>
<dd>

**resources_to_import:** `typing.Optional[typing.Union[ResourceToImport, typing.Sequence[ResourceToImport]]]` — The resources to import into your stack.
    
</dd>
</dl>

<dl>
<dd>

**include_nested_stacks:** `typing.Optional[bool]` — Creates a change set for the all nested stacks specified in the template. The default behavior of this action is set to <code>False</code>. To include nested sets in a change set, specify <code>True</code>.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_create_change_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.</p> <p>To create a change set for a stack that doesn't exist, for the <code>ChangeSetType</code> parameter, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code> for the <code>ChangeSetType</code> parameter. To create a change set for an import operation, specify <code>IMPORT</code> for the <code>ChangeSetType</code> parameter. After the <code>CreateChangeSet</code> call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the <a>DescribeChangeSet</a> action.</p> <p>When you are satisfied with the changes the change set will make, execute the change set by using the <a>ExecuteChangeSet</a> action. CloudFormation doesn't make changes until you execute the change set.</p> <p>To create a change set for the entire stack hierarchy, set <code>IncludeNestedStacks</code> to <code>True</code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostCreateChangeSetRequestAction, PostCreateChangeSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_create_change_set(
    action=PostCreateChangeSetRequestAction.CREATE_CHANGE_SET,
    version=PostCreateChangeSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostCreateChangeSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostCreateChangeSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_create_stack</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the <a>DescribeStacks</a>operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetCreateStackRequestAction, GetCreateStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_create_stack(
    stack_name="StackName",
    action=GetCreateStackRequestAction.CREATE_STACK,
    version=GetCreateStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — <p>The name that's associated with the stack. The name must be unique in the Region in which you are creating the stack.</p> <note> <p>A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetical character and can't be longer than 128 characters.</p> </note>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetCreateStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetCreateStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**template_body:** `typing.Optional[str]` — <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**template_url:** `typing.Optional[str]` — <p>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]` — A list of <code>Parameter</code> structures that specify input parameters for the stack. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.
    
</dd>
</dl>

<dl>
<dd>

**disable_rollback:** `typing.Optional[bool]` — <p>Set to <code>true</code> to disable rollback of the stack if stack creation failed. You can specify either <code>DisableRollback</code> or <code>OnFailure</code>, but not both.</p> <p>Default: <code>false</code> </p>
    
</dd>
</dl>

<dl>
<dd>

**rollback_configuration:** `typing.Optional[GetCreateStackRequestRollbackConfiguration]` — The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
    
</dd>
</dl>

<dl>
<dd>

**timeout_in_minutes:** `typing.Optional[int]` — The amount of time that can pass before the stack status becomes CREATE_FAILED; if <code>DisableRollback</code> is not set or is set to <code>false</code>, the stack will be rolled back.
    
</dd>
</dl>

<dl>
<dd>

**notification_ar_ns:** `typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]]` — The Amazon Simple Notification Service (Amazon SNS) topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).
    
</dd>
</dl>

<dl>
<dd>

**capabilities:** `typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]` — <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create the stack directly from the template using this capability.</p> <important> <p>You should only create stacks directly from a stack template that contains macros if you know what processing the macro performs.</p> <p>Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.</p> </important> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation macros to perform custom processing on templates</a>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**resource_types:** `typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]]` — <p>The template resource types that you have permissions to work with for this create stack action, such as <code>AWS::EC2::Instance</code>, <code>AWS::EC2::*</code>, or <code>Custom::MyCustomInstance</code>. Use the following syntax to describe template resource types: <code>AWS::*</code> (for all Amazon Web Services resources), <code>Custom::*</code> (for all custom resources), <code>Custom::<i>logical_ID</i> </code> (for a specific custom resource), <code>AWS::<i>service_name</i>::*</code> (for all resources of a particular Amazon Web Services service), and <code>AWS::<i>service_name</i>::<i>resource_logical_ID</i> </code> (for a specific Amazon Web Services resource).</p> <p>If the list of resource types doesn't include a resource that you're creating, the stack creation fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">Controlling Access with Identity and Access Management</a>.</p>
    
</dd>
</dl>

<dl>
<dd>

**role_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to create the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>
    
</dd>
</dl>

<dl>
<dd>

**on_failure:** `typing.Optional[GetCreateStackRequestOnFailure]` — <p>Determines what action will be taken if stack creation fails. This must be one of: <code>DO_NOTHING</code>, <code>ROLLBACK</code>, or <code>DELETE</code>. You can specify either <code>OnFailure</code> or <code>DisableRollback</code>, but not both.</p> <p>Default: <code>ROLLBACK</code> </p>
    
</dd>
</dl>

<dl>
<dd>

**stack_policy_body:** `typing.Optional[str]` — Structure containing the stack policy body. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html"> Prevent Updates to Stack Resources</a> in the <i>CloudFormation User Guide</i>. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.
    
</dd>
</dl>

<dl>
<dd>

**stack_policy_url:** `typing.Optional[str]` — Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]` — Key-value pairs to associate with this stack. CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — <p>A unique identifier for this <code>CreateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create a stack with the same name. You might retry <code>CreateStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**enable_termination_protection:** `typing.Optional[bool]` — <p>Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>. Termination protection is deactivated on stacks by default.</p> <p>For <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_create_stack</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the <a>DescribeStacks</a>operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostCreateStackRequestAction, PostCreateStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_create_stack(
    action=PostCreateStackRequestAction.CREATE_STACK,
    version=PostCreateStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostCreateStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostCreateStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_create_stack_instances</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either <code>Accounts</code> or <code>DeploymentTargets</code>, and you must specify at least one value for <code>Regions</code>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetCreateStackInstancesRequestAction, GetCreateStackInstancesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_create_stack_instances(
    stack_set_name="StackSetName",
    action=GetCreateStackInstancesRequestAction.CREATE_STACK_INSTANCES,
    version=GetCreateStackInstancesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set that you want to create stack instances from.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetCreateStackInstancesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetCreateStackInstancesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**accounts:** `typing.Optional[typing.Union[Account, typing.Sequence[Account]]]` — <p>[Self-managed permissions] The names of one or more Amazon Web Services accounts that you want to create stack instances in the specified Region(s) for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**deployment_targets:** `typing.Optional[GetCreateStackInstancesRequestDeploymentTargets]` — <p>[Service-managed permissions] The Organizations accounts for which to create stack instances in the specified Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[typing.Union[Region, typing.Sequence[Region]]]` — The names of one or more Amazon Web Services Regions where you want to create stack instances using the specified Amazon Web Services accounts.
    
</dd>
</dl>

<dl>
<dd>

**parameter_overrides:** `typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]` — <p>A list of stack set parameters whose values you want to override in the selected stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During stack set updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template.</p>
    
</dd>
</dl>

<dl>
<dd>

**operation_preferences:** `typing.Optional[GetCreateStackInstancesRequestOperationPreferences]` — Preferences for how CloudFormation performs this stack set operation.
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `typing.Optional[str]` — <p>The unique identifier for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetCreateStackInstancesRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_create_stack_instances</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either <code>Accounts</code> or <code>DeploymentTargets</code>, and you must specify at least one value for <code>Regions</code>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostCreateStackInstancesRequestAction, PostCreateStackInstancesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_create_stack_instances(
    action=PostCreateStackInstancesRequestAction.CREATE_STACK_INSTANCES,
    version=PostCreateStackInstancesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostCreateStackInstancesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostCreateStackInstancesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_create_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a stack set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetCreateStackSetRequestAction, GetCreateStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_create_stack_set(
    stack_set_name="StackSetName",
    action=GetCreateStackSetRequestAction.CREATE_STACK_SET,
    version=GetCreateStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — <p>The name to associate with the stack set. The name must be unique in the Region where you create your stack set.</p> <note> <p>A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.</p> </note>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetCreateStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetCreateStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A description of the stack set. You can use the description to identify the stack set's purpose or other important information.
    
</dd>
</dl>

<dl>
<dd>

**template_body:** `typing.Optional[str]` — <p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**template_url:** `typing.Optional[str]` — <p>The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify either the TemplateBody or the TemplateURL parameter, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**stack_id:** `typing.Optional[str]` — The stack ID you are importing into a new stack set. Specify the Amazon Resource Name (ARN) of the stack.
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]` — The input parameters for the stack set template.
    
</dd>
</dl>

<dl>
<dd>

**capabilities:** `typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]` — <p>In some cases, you must explicitly acknowledge that your stack set template contains certain capabilities in order for CloudFormation to create the stack set and related stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stack sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your stack set template references one or more macros, you must create the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To create the stack set directly, you must acknowledge this capability. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> <important> <p>Stack sets with service-managed permissions don't currently support the use of macros in templates. (This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.</p> </important> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]` — <p>The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.</p> <p>If you specify tags as part of a <code>CreateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you don't, the entire <code>CreateStackSet</code> action fails with an <code>access denied</code> error, and the stack set is not created.</p>
    
</dd>
</dl>

<dl>
<dd>

**administration_role_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the IAM role to use to create this stack set.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Prerequisites: Granting Permissions for Stack Set Operations</a> in the <i>CloudFormation User Guide</i>.</p>
    
</dd>
</dl>

<dl>
<dd>

**execution_role_name:** `typing.Optional[str]` — <p>The name of the IAM execution role to use to create the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the stack set operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.</p>
    
</dd>
</dl>

<dl>
<dd>

**permission_model:** `typing.Optional[GetCreateStackSetRequestPermissionModel]` — <p>Describes how the IAM roles required for stack set operations are created. By default, <code>SELF-MANAGED</code> is specified.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**auto_deployment:** `typing.Optional[GetCreateStackSetRequestAutoDeployment]` — Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or organizational unit (OU). Specify only if <code>PermissionModel</code> is <code>SERVICE_MANAGED</code>.
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetCreateStackSetRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>To create a stack set with service-managed permissions while signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>To create a stack set with service-managed permissions while signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated admin in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul> <p>Stack sets with service-managed permissions are created in the management account, including stack sets that are created by delegated administrators.</p>
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — <p>A unique identifier for this <code>CreateStackSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another stack set with the same name. You might retry <code>CreateStackSet</code> requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>
    
</dd>
</dl>

<dl>
<dd>

**managed_execution:** `typing.Optional[GetCreateStackSetRequestManagedExecution]` — Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_create_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a stack set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostCreateStackSetRequestAction, PostCreateStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_create_stack_set(
    action=PostCreateStackSetRequestAction.CREATE_STACK_SET,
    version=PostCreateStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostCreateStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostCreateStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_deactivate_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Deactivates a public extension that was previously activated in this account and region.</p> <p>Once deactivated, an extension can't be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren't automatically updated if a new version of the extension is released.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDeactivateTypeRequestAction, GetDeactivateTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_deactivate_type(
    action=GetDeactivateTypeRequestAction.DEACTIVATE_TYPE,
    version=GetDeactivateTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetDeactivateTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDeactivateTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The type name of the extension, in this account and region. If you specified a type name alias when enabling the extension, use the type name alias.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetDeactivateTypeRequestType]` — <p>The extension type.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_deactivate_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Deactivates a public extension that was previously activated in this account and region.</p> <p>Once deactivated, an extension can't be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren't automatically updated if a new version of the extension is released.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDeactivateTypeRequestAction, PostDeactivateTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_deactivate_type(
    action=PostDeactivateTypeRequestAction.DEACTIVATE_TYPE,
    version=PostDeactivateTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDeactivateTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDeactivateTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_delete_change_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.</p> <p>If the call successfully completes, CloudFormation successfully deleted the change set.</p> <p>If <code>IncludeNestedStacks</code> specifies <code>True</code> during the creation of the nested change set, then <code>DeleteChangeSet</code> will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of <code>REVIEW_IN_PROGRESS</code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDeleteChangeSetRequestAction, GetDeleteChangeSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_delete_change_set(
    change_set_name="x",
    action=GetDeleteChangeSetRequestAction.DELETE_CHANGE_SET,
    version=GetDeleteChangeSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**change_set_name:** `str` — The name or Amazon Resource Name (ARN) of the change set that you want to delete.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDeleteChangeSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDeleteChangeSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `typing.Optional[str]` — If you specified the name of a change set to delete, specify the stack name or Amazon Resource Name (ARN) that's associated with it.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_delete_change_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.</p> <p>If the call successfully completes, CloudFormation successfully deleted the change set.</p> <p>If <code>IncludeNestedStacks</code> specifies <code>True</code> during the creation of the nested change set, then <code>DeleteChangeSet</code> will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of <code>REVIEW_IN_PROGRESS</code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDeleteChangeSetRequestAction, PostDeleteChangeSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_delete_change_set(
    action=PostDeleteChangeSetRequestAction.DELETE_CHANGE_SET,
    version=PostDeleteChangeSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDeleteChangeSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDeleteChangeSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_delete_stack</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don't show up in the <a>DescribeStacks</a> operation if the deletion has been completed successfully.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDeleteStackRequestAction, GetDeleteStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_delete_stack(
    stack_name="StackName",
    action=GetDeleteStackRequestAction.DELETE_STACK,
    version=GetDeleteStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name or the unique stack ID that's associated with the stack.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDeleteStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDeleteStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**retain_resources:** `typing.Optional[typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]]` — <p>For stacks in the <code>DELETE_FAILED</code> state, a list of resource logical IDs that are associated with the resources you want to retain. During deletion, CloudFormation deletes the stack but doesn't delete the retained resources.</p> <p>Retaining resources is useful when you can't delete a resource, such as a non-empty S3 bucket, but you want to delete the stack.</p>
    
</dd>
</dl>

<dl>
<dd>

**role_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to delete the stack. CloudFormation uses the role's credentials to make calls on your behalf.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — <p>A unique identifier for this <code>DeleteStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to delete a stack with the same name. You might retry <code>DeleteStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_delete_stack</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don't show up in the <a>DescribeStacks</a> operation if the deletion has been completed successfully.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDeleteStackRequestAction, PostDeleteStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_delete_stack(
    action=PostDeleteStackRequestAction.DELETE_STACK,
    version=PostDeleteStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDeleteStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDeleteStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_delete_stack_instances</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDeleteStackInstancesRequestAction, GetDeleteStackInstancesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_delete_stack_instances(
    stack_set_name="StackSetName",
    retain_stacks=True,
    action=GetDeleteStackInstancesRequestAction.DELETE_STACK_INSTANCES,
    version=GetDeleteStackInstancesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set that you want to delete stack instances for.
    
</dd>
</dl>

<dl>
<dd>

**retain_stacks:** `bool` — <p>Removes the stack instances from the specified stack set, but doesn't delete the stacks. You can't reassociate a retained stack or add an existing, saved stack to a new stack set.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">Stack set operation options</a>.</p>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDeleteStackInstancesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDeleteStackInstancesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**accounts:** `typing.Optional[typing.Union[Account, typing.Sequence[Account]]]` — <p>[Self-managed permissions] The names of the Amazon Web Services accounts that you want to delete stack instances for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**deployment_targets:** `typing.Optional[GetDeleteStackInstancesRequestDeploymentTargets]` — <p>[Service-managed permissions] The Organizations accounts from which to delete stack instances.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[typing.Union[Region, typing.Sequence[Region]]]` — The Amazon Web Services Regions where you want to delete stack set instances.
    
</dd>
</dl>

<dl>
<dd>

**operation_preferences:** `typing.Optional[GetDeleteStackInstancesRequestOperationPreferences]` — Preferences for how CloudFormation performs this stack set operation.
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `typing.Optional[str]` — <p>The unique identifier for this stack set operation.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You can retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetDeleteStackInstancesRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_delete_stack_instances</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDeleteStackInstancesRequestAction, PostDeleteStackInstancesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_delete_stack_instances(
    action=PostDeleteStackInstancesRequestAction.DELETE_STACK_INSTANCES,
    version=PostDeleteStackInstancesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDeleteStackInstancesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDeleteStackInstancesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_delete_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a stack set. Before you can delete a stack set, all its member stack instances must be deleted. For more information about how to complete this, see <a>DeleteStackInstances</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDeleteStackSetRequestAction, GetDeleteStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_delete_stack_set(
    stack_set_name="StackSetName",
    action=GetDeleteStackSetRequestAction.DELETE_STACK_SET,
    version=GetDeleteStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set that you're deleting. You can obtain this value by running <a>ListStackSets</a>.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDeleteStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDeleteStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetDeleteStackSetRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_delete_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a stack set. Before you can delete a stack set, all its member stack instances must be deleted. For more information about how to complete this, see <a>DeleteStackInstances</a>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDeleteStackSetRequestAction, PostDeleteStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_delete_stack_set(
    action=PostDeleteStackSetRequestAction.DELETE_STACK_SET,
    version=PostDeleteStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDeleteStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDeleteStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_deregister_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Marks an extension or extension version as <code>DEPRECATED</code> in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.</p> <p>To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.</p> <p>You can't deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.</p> <p>To view the deprecation status of an extension or extension version, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDeregisterTypeRequestAction, GetDeregisterTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_deregister_type(
    action=GetDeregisterTypeRequestAction.DEREGISTER_TYPE,
    version=GetDeregisterTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetDeregisterTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDeregisterTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetDeregisterTypeRequestType]` — <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `typing.Optional[str]` — The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_deregister_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Marks an extension or extension version as <code>DEPRECATED</code> in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.</p> <p>To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.</p> <p>You can't deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.</p> <p>To view the deprecation status of an extension or extension version, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDeregisterTypeRequestAction, PostDeregisterTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_deregister_type(
    action=PostDeregisterTypeRequestAction.DEREGISTER_TYPE,
    version=PostDeregisterTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDeregisterTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDeregisterTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_account_limits</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation Quotas</a> in the <i>CloudFormation User Guide</i>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeAccountLimitsRequestAction, GetDescribeAccountLimitsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_account_limits(
    action=GetDescribeAccountLimitsRequestAction.DESCRIBE_ACCOUNT_LIMITS,
    version=GetDescribeAccountLimitsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetDescribeAccountLimitsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeAccountLimitsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string that identifies the next page of limits that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_account_limits</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation Quotas</a> in the <i>CloudFormation User Guide</i>.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeAccountLimitsRequestAction, PostDescribeAccountLimitsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_account_limits(
    action=PostDescribeAccountLimitsRequestAction.DESCRIBE_ACCOUNT_LIMITS,
    version=PostDescribeAccountLimitsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeAccountLimitsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeAccountLimitsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_change_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html">Updating Stacks Using Change Sets</a> in the CloudFormation User Guide.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeChangeSetRequestAction, GetDescribeChangeSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_change_set(
    change_set_name="x",
    action=GetDescribeChangeSetRequestAction.DESCRIBE_CHANGE_SET,
    version=GetDescribeChangeSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**change_set_name:** `str` — The name or Amazon Resource Name (ARN) of the change set that you want to describe.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDescribeChangeSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeChangeSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `typing.Optional[str]` — If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string (provided by the <a>DescribeChangeSet</a> response output) that identifies the next page of information that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_change_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html">Updating Stacks Using Change Sets</a> in the CloudFormation User Guide.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeChangeSetRequestAction, PostDescribeChangeSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_change_set(
    action=PostDescribeChangeSetRequestAction.DESCRIBE_CHANGE_SET,
    version=PostDescribeChangeSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeChangeSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeChangeSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_change_set_hooks</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeChangeSetHooksRequestAction, GetDescribeChangeSetHooksRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_change_set_hooks(
    change_set_name="x",
    action=GetDescribeChangeSetHooksRequestAction.DESCRIBE_CHANGE_SET_HOOKS,
    version=GetDescribeChangeSetHooksRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**change_set_name:** `str` — The name or Amazon Resource Name (ARN) of the change set that you want to describe.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDescribeChangeSetHooksRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeChangeSetHooksRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `typing.Optional[str]` — If you specified the name of a change set, specify the stack name or stack ID (ARN) of the change set you want to describe.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string, provided by the <code>DescribeChangeSetHooks</code> response output, that identifies the next page of information that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**logical_resource_id:** `typing.Optional[str]` — If specified, lists only the hooks related to the specified <code>LogicalResourceId</code>.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_change_set_hooks</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeChangeSetHooksRequestAction, PostDescribeChangeSetHooksRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_change_set_hooks(
    action=PostDescribeChangeSetHooksRequestAction.DESCRIBE_CHANGE_SET_HOOKS,
    version=PostDescribeChangeSetHooksRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeChangeSetHooksRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeChangeSetHooksRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_publisher</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about a CloudFormation extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p> <p>For more information about registering as a publisher, see:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i> </p> </li> </ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribePublisherRequestAction, GetDescribePublisherRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_publisher(
    action=GetDescribePublisherRequestAction.DESCRIBE_PUBLISHER,
    version=GetDescribePublisherRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetDescribePublisherRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribePublisherRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**publisher_id:** `typing.Optional[str]` — <p>The ID of the extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_publisher</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about a CloudFormation extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p> <p>For more information about registering as a publisher, see:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i> </p> </li> </ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribePublisherRequestAction, PostDescribePublisherRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_publisher(
    action=PostDescribePublisherRequestAction.DESCRIBE_PUBLISHER,
    version=PostDescribePublisherRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribePublisherRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribePublisherRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_stack_drift_detection_status</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <a>DetectStackDrift</a> to initiate a stack drift detection operation. <code>DetectStackDrift</code> returns a <code>StackDriftDetectionId</code> you can use to monitor the progress of the operation using <code>DescribeStackDriftDetectionStatus</code>. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeStackDriftDetectionStatusRequestAction, GetDescribeStackDriftDetectionStatusRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_stack_drift_detection_status(
    stack_drift_detection_id="x",
    action=GetDescribeStackDriftDetectionStatusRequestAction.DESCRIBE_STACK_DRIFT_DETECTION_STATUS,
    version=GetDescribeStackDriftDetectionStatusRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_drift_detection_id:** `str` — <p>The ID of the drift detection results of this operation.</p> <p>CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results CloudFormation retains for any given stack, and for how long, may vary.</p>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDescribeStackDriftDetectionStatusRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeStackDriftDetectionStatusRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_stack_drift_detection_status</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <a>DetectStackDrift</a> to initiate a stack drift detection operation. <code>DetectStackDrift</code> returns a <code>StackDriftDetectionId</code> you can use to monitor the progress of the operation using <code>DescribeStackDriftDetectionStatus</code>. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeStackDriftDetectionStatusRequestAction, PostDescribeStackDriftDetectionStatusRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_stack_drift_detection_status(
    action=PostDescribeStackDriftDetectionStatusRequestAction.DESCRIBE_STACK_DRIFT_DETECTION_STATUS,
    version=PostDescribeStackDriftDetectionStatusRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeStackDriftDetectionStatusRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeStackDriftDetectionStatusRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_stack_events</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html">Stacks</a> in the CloudFormation User Guide.</p> <note> <p>You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeStackEventsRequestAction, GetDescribeStackEventsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_stack_events(
    action=GetDescribeStackEventsRequestAction.DESCRIBE_STACK_EVENTS,
    version=GetDescribeStackEventsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetDescribeStackEventsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeStackEventsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `typing.Optional[str]` — <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string that identifies the next page of events that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_stack_events</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/concept-stack.html">Stacks</a> in the CloudFormation User Guide.</p> <note> <p>You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeStackEventsRequestAction, PostDescribeStackEventsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_stack_events(
    action=PostDescribeStackEventsRequestAction.DESCRIBE_STACK_EVENTS,
    version=PostDescribeStackEventsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeStackEventsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeStackEventsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_stack_instance</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns the stack instance that's associated with the specified stack set, Amazon Web Services account, and Region.</p> <p>For a list of stack instances that are associated with a specific stack set, use <a>ListStackInstances</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeStackInstanceRequestAction, GetDescribeStackInstanceRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_stack_instance(
    stack_set_name="StackSetName",
    stack_instance_account="StackInstanceAccount",
    stack_instance_region="StackInstanceRegion",
    action=GetDescribeStackInstanceRequestAction.DESCRIBE_STACK_INSTANCE,
    version=GetDescribeStackInstanceRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or the unique stack ID of the stack set that you want to get stack instance information for.
    
</dd>
</dl>

<dl>
<dd>

**stack_instance_account:** `str` — The ID of an Amazon Web Services account that's associated with this stack instance.
    
</dd>
</dl>

<dl>
<dd>

**stack_instance_region:** `str` — The name of a Region that's associated with this stack instance.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDescribeStackInstanceRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeStackInstanceRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetDescribeStackInstanceRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_stack_instance</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns the stack instance that's associated with the specified stack set, Amazon Web Services account, and Region.</p> <p>For a list of stack instances that are associated with a specific stack set, use <a>ListStackInstances</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeStackInstanceRequestAction, PostDescribeStackInstanceRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_stack_instance(
    action=PostDescribeStackInstanceRequestAction.DESCRIBE_STACK_INSTANCE,
    version=PostDescribeStackInstanceRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeStackInstanceRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeStackInstanceRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_stack_resource</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns a description of the specified resource in the specified stack.</p> <p>For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeStackResourceRequestAction, GetDescribeStackResourceRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_stack_resource(
    stack_name="StackName",
    logical_resource_id="LogicalResourceId",
    action=GetDescribeStackResourceRequestAction.DESCRIBE_STACK_RESOURCE,
    version=GetDescribeStackResourceRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>
    
</dd>
</dl>

<dl>
<dd>

**logical_resource_id:** `str` — <p>The logical name of the resource as specified in the template.</p> <p>Default: There is no default value.</p>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDescribeStackResourceRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeStackResourceRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_stack_resource</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns a description of the specified resource in the specified stack.</p> <p>For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeStackResourceRequestAction, PostDescribeStackResourceRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_stack_resource(
    action=PostDescribeStackResourceRequestAction.DESCRIBE_STACK_RESOURCE,
    version=PostDescribeStackResourceRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeStackResourceRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeStackResourceRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_stack_resource_drifts</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.</p> <p>For a given stack, there will be one <code>StackResourceDrift</code> for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that don't currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p>Use <a>DetectStackResourceDrift</a> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all supported resources for a given stack.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeStackResourceDriftsRequestAction, GetDescribeStackResourceDriftsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_stack_resource_drifts(
    stack_name="x",
    action=GetDescribeStackResourceDriftsRequestAction.DESCRIBE_STACK_RESOURCE_DRIFTS,
    version=GetDescribeStackResourceDriftsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name of the stack for which you want drift information.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDescribeStackResourceDriftsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeStackResourceDriftsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_resource_drift_status_filters:** `typing.Optional[typing.Union[StackResourceDriftStatus, typing.Sequence[StackResourceDriftStatus]]]` — <p>The resource drift status values to use as filters for the resource drift results returned.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration in that the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected template values.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation doesn't currently return this value.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string that identifies the next page of stack resource drift results.
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` — The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_stack_resource_drifts</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.</p> <p>For a given stack, there will be one <code>StackResourceDrift</code> for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that don't currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p>Use <a>DetectStackResourceDrift</a> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all supported resources for a given stack.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeStackResourceDriftsRequestAction, PostDescribeStackResourceDriftsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_stack_resource_drifts(
    action=PostDescribeStackResourceDriftsRequestAction.DESCRIBE_STACK_RESOURCE_DRIFTS,
    version=PostDescribeStackResourceDriftsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeStackResourceDriftsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeStackResourceDriftsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[str]` — Pagination limit
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_stack_resources</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns Amazon Web Services resource descriptions for running and deleted stacks. If <code>StackName</code> is specified, all the associated resources that are part of the stack are returned. If <code>PhysicalResourceId</code> is specified, the associated resources of the stack that the resource belongs to are returned.</p> <note> <p>Only the first 100 resources will be returned. If your stack has more resources than this, you should use <code>ListStackResources</code> instead.</p> </note> <p>For deleted stacks, <code>DescribeStackResources</code> returns resource information for up to 90 days after the stack has been deleted.</p> <p>You must specify either <code>StackName</code> or <code>PhysicalResourceId</code>, but not both. In addition, you can specify <code>LogicalResourceId</code> to filter the returned result. For more information about resources, the <code>LogicalResourceId</code> and <code>PhysicalResourceId</code>, go to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/">CloudFormation User Guide</a>.</p> <note> <p>A <code>ValidationError</code> is returned if you specify both <code>StackName</code> and <code>PhysicalResourceId</code> in the same request.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeStackResourcesRequestAction, GetDescribeStackResourcesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_stack_resources(
    action=GetDescribeStackResourcesRequestAction.DESCRIBE_STACK_RESOURCES,
    version=GetDescribeStackResourcesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetDescribeStackResourcesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeStackResourcesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `typing.Optional[str]` — <p>The name or the unique stack ID that is associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p> <p>Required: Conditional. If you don't specify <code>StackName</code>, you must specify <code>PhysicalResourceId</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**logical_resource_id:** `typing.Optional[str]` — <p>The logical name of the resource as specified in the template.</p> <p>Default: There is no default value.</p>
    
</dd>
</dl>

<dl>
<dd>

**physical_resource_id:** `typing.Optional[str]` — <p>The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.</p> <p>For example, for an Amazon Elastic Compute Cloud (EC2) instance, <code>PhysicalResourceId</code> corresponds to the <code>InstanceId</code>. You can pass the EC2 <code>InstanceId</code> to <code>DescribeStackResources</code> to find which stack the instance belongs to and what other resources are part of the stack.</p> <p>Required: Conditional. If you don't specify <code>PhysicalResourceId</code>, you must specify <code>StackName</code>.</p> <p>Default: There is no default value.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_stack_resources</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns Amazon Web Services resource descriptions for running and deleted stacks. If <code>StackName</code> is specified, all the associated resources that are part of the stack are returned. If <code>PhysicalResourceId</code> is specified, the associated resources of the stack that the resource belongs to are returned.</p> <note> <p>Only the first 100 resources will be returned. If your stack has more resources than this, you should use <code>ListStackResources</code> instead.</p> </note> <p>For deleted stacks, <code>DescribeStackResources</code> returns resource information for up to 90 days after the stack has been deleted.</p> <p>You must specify either <code>StackName</code> or <code>PhysicalResourceId</code>, but not both. In addition, you can specify <code>LogicalResourceId</code> to filter the returned result. For more information about resources, the <code>LogicalResourceId</code> and <code>PhysicalResourceId</code>, go to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/">CloudFormation User Guide</a>.</p> <note> <p>A <code>ValidationError</code> is returned if you specify both <code>StackName</code> and <code>PhysicalResourceId</code> in the same request.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeStackResourcesRequestAction, PostDescribeStackResourcesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_stack_resources(
    action=PostDescribeStackResourcesRequestAction.DESCRIBE_STACK_RESOURCES,
    version=PostDescribeStackResourcesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeStackResourcesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeStackResourcesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the description of the specified stack set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeStackSetRequestAction, GetDescribeStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_stack_set(
    stack_set_name="StackSetName",
    action=GetDescribeStackSetRequestAction.DESCRIBE_STACK_SET,
    version=GetDescribeStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set whose description you want.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDescribeStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetDescribeStackSetRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the description of the specified stack set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeStackSetRequestAction, PostDescribeStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_stack_set(
    action=PostDescribeStackSetRequestAction.DESCRIBE_STACK_SET,
    version=PostDescribeStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_stack_set_operation</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the description of the specified stack set operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeStackSetOperationRequestAction, GetDescribeStackSetOperationRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_stack_set_operation(
    stack_set_name="StackSetName",
    operation_id="x",
    action=GetDescribeStackSetOperationRequestAction.DESCRIBE_STACK_SET_OPERATION,
    version=GetDescribeStackSetOperationRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or the unique stack ID of the stack set for the stack operation.
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `str` — The unique ID of the stack set operation.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDescribeStackSetOperationRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeStackSetOperationRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetDescribeStackSetOperationRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_stack_set_operation</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the description of the specified stack set operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeStackSetOperationRequestAction, PostDescribeStackSetOperationRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_stack_set_operation(
    action=PostDescribeStackSetOperationRequestAction.DESCRIBE_STACK_SET_OPERATION,
    version=PostDescribeStackSetOperationRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeStackSetOperationRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeStackSetOperationRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_stacks</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.</p> <note> <p>If the stack doesn't exist, an <code>ValidationError</code> is returned.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeStacksRequestAction, GetDescribeStacksRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_stacks(
    action=GetDescribeStacksRequestAction.DESCRIBE_STACKS,
    version=GetDescribeStacksRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetDescribeStacksRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeStacksRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `typing.Optional[str]` — <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string that identifies the next page of stacks that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_stacks</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created.</p> <note> <p>If the stack doesn't exist, an <code>ValidationError</code> is returned.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeStacksRequestAction, PostDescribeStacksRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_stacks(
    action=PostDescribeStacksRequestAction.DESCRIBE_STACKS,
    version=PostDescribeStacksRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeStacksRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeStacksRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns detailed information about an extension that has been registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeTypeRequestAction, GetDescribeTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_type(
    action=GetDescribeTypeRequestAction.DESCRIBE_TYPE,
    version=GetDescribeTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetDescribeTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetDescribeTypeRequestType]` — <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `typing.Optional[str]` — <p>The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>
    
</dd>
</dl>

<dl>
<dd>

**publisher_id:** `typing.Optional[str]` — <p>The publisher ID of the extension publisher.</p> <p>Extensions provided by Amazon Web Services are not assigned a publisher ID.</p>
    
</dd>
</dl>

<dl>
<dd>

**public_version_number:** `typing.Optional[str]` — The version number of a public third-party extension.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns detailed information about an extension that has been registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeTypeRequestAction, PostDescribeTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_type(
    action=PostDescribeTypeRequestAction.DESCRIBE_TYPE,
    version=PostDescribeTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_describe_type_registration</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about an extension's registration, including its current status and type and version identifiers.</p> <p>When you initiate a registration request using <code> <a>RegisterType</a> </code>, you can then use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of that registration request.</p> <p>Once the registration request has completed, use <code> <a>DescribeType</a> </code> to return detailed information about an extension.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDescribeTypeRegistrationRequestAction, GetDescribeTypeRegistrationRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_describe_type_registration(
    registration_token="x",
    action=GetDescribeTypeRegistrationRequestAction.DESCRIBE_TYPE_REGISTRATION,
    version=GetDescribeTypeRegistrationRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**registration_token:** `str` — <p>The identifier for this registration request.</p> <p>This registration token is generated by CloudFormation when you initiate a registration request using <code> <a>RegisterType</a> </code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDescribeTypeRegistrationRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDescribeTypeRegistrationRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_describe_type_registration</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about an extension's registration, including its current status and type and version identifiers.</p> <p>When you initiate a registration request using <code> <a>RegisterType</a> </code>, you can then use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of that registration request.</p> <p>Once the registration request has completed, use <code> <a>DescribeType</a> </code> to return detailed information about an extension.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDescribeTypeRegistrationRequestAction, PostDescribeTypeRegistrationRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_describe_type_registration(
    action=PostDescribeTypeRegistrationRequestAction.DESCRIBE_TYPE_REGISTRATION,
    version=PostDescribeTypeRegistrationRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDescribeTypeRegistrationRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDescribeTypeRegistrationRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_detect_stack_drift</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackDrift</code> to detect drift on all supported resources for a given stack, or <a>DetectStackResourceDrift</a> to detect drift on individual resources.</p> <p>For a list of stack resources that currently support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p> <code>DetectStackDrift</code> can take up to several minutes, depending on the number of resources contained within the stack. Use <a>DescribeStackDriftDetectionStatus</a> to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p> <p>When detecting drift on a stack, CloudFormation doesn't detect drift on any nested stacks belonging to that stack. Perform <code>DetectStackDrift</code> directly on the nested stack itself.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDetectStackDriftRequestAction, GetDetectStackDriftRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_detect_stack_drift(
    stack_name="x",
    action=GetDetectStackDriftRequestAction.DETECT_STACK_DRIFT,
    version=GetDetectStackDriftRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name of the stack for which you want to detect drift.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDetectStackDriftRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDetectStackDriftRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**logical_resource_ids:** `typing.Optional[typing.Union[LogicalResourceId, typing.Sequence[LogicalResourceId]]]` — The logical names of any resources you want to use as filters.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_detect_stack_drift</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Detects whether a stack's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackDrift</code> to detect drift on all supported resources for a given stack, or <a>DetectStackResourceDrift</a> to detect drift on individual resources.</p> <p>For a list of stack resources that currently support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p> <p> <code>DetectStackDrift</code> can take up to several minutes, depending on the number of resources contained within the stack. Use <a>DescribeStackDriftDetectionStatus</a> to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p> <p>When detecting drift on a stack, CloudFormation doesn't detect drift on any nested stacks belonging to that stack. Perform <code>DetectStackDrift</code> directly on the nested stack itself.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDetectStackDriftRequestAction, PostDetectStackDriftRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_detect_stack_drift(
    action=PostDetectStackDriftRequestAction.DETECT_STACK_DRIFT,
    version=PostDetectStackDriftRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDetectStackDriftRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDetectStackDriftRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_detect_stack_resource_drift</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about whether a resource's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackResourceDrift</code> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all resources in a given stack that support drift detection.</p> <p>Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDetectStackResourceDriftRequestAction, GetDetectStackResourceDriftRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_detect_stack_resource_drift(
    stack_name="x",
    logical_resource_id="LogicalResourceId",
    action=GetDetectStackResourceDriftRequestAction.DETECT_STACK_RESOURCE_DRIFT,
    version=GetDetectStackResourceDriftRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name of the stack to which the resource belongs.
    
</dd>
</dl>

<dl>
<dd>

**logical_resource_id:** `str` — The logical name of the resource for which to return drift information.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDetectStackResourceDriftRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDetectStackResourceDriftRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_detect_stack_resource_drift</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about whether a resource's actual configuration differs, or has <i>drifted</i>, from it's expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detecting Unregulated Configuration Changes to Stacks and Resources</a>.</p> <p>Use <code>DetectStackResourceDrift</code> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all resources in a given stack that support drift detection.</p> <p>Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift-resource-list.html">Resources that Support Drift Detection</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDetectStackResourceDriftRequestAction, PostDetectStackResourceDriftRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_detect_stack_resource_drift(
    action=PostDetectStackResourceDriftRequestAction.DETECT_STACK_RESOURCE_DRIFT,
    version=PostDetectStackResourceDriftRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDetectStackResourceDriftRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDetectStackResourceDriftRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_detect_stack_set_drift</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">How CloudFormation performs drift detection on a stack set</a>.</p> <p> <code>DetectStackSetDrift</code> returns the <code>OperationId</code> of the stack set drift detection operation. Use this operation id with <code> <a>DescribeStackSetOperation</a> </code> to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the stack set, in addition to the number of resources included in each stack.</p> <p>Once the operation has completed, use the following actions to return drift information:</p> <ul> <li> <p>Use <code> <a>DescribeStackSet</a> </code> to return detailed information about the stack set, including detailed information about the last <i>completed</i> drift operation performed on the stack set. (Information about drift operations that are in progress isn't included.)</p> </li> <li> <p>Use <code> <a>ListStackInstances</a> </code> to return a list of stack instances belonging to the stack set, including the drift status and last drift time checked of each instance.</p> </li> <li> <p>Use <code> <a>DescribeStackInstance</a> </code> to return detailed information about a specific stack instance, including its drift status and last drift time checked.</p> </li> </ul> <p>For more information about performing a drift detection operation on a stack set, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Detecting unmanaged changes in stack sets</a>.</p> <p>You can only run a single drift detection operation on a given stack set at one time.</p> <p>To stop a drift detection stack set operation, use <code> <a>StopStackSetOperation</a> </code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetDetectStackSetDriftRequestAction, GetDetectStackSetDriftRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_detect_stack_set_drift(
    stack_set_name="StackSetName",
    action=GetDetectStackSetDriftRequestAction.DETECT_STACK_SET_DRIFT,
    version=GetDetectStackSetDriftRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name of the stack set on which to perform the drift detection operation.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetDetectStackSetDriftRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetDetectStackSetDriftRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**operation_preferences:** `typing.Optional[GetDetectStackSetDriftRequestOperationPreferences]` — 
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `typing.Optional[str]` —  <i>The ID of the stack set operation.</i> 
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetDetectStackSetDriftRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_detect_stack_set_drift</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Detect drift on a stack set. When CloudFormation performs drift detection on a stack set, it performs drift detection on the stack associated with each stack instance in the stack set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">How CloudFormation performs drift detection on a stack set</a>.</p> <p> <code>DetectStackSetDrift</code> returns the <code>OperationId</code> of the stack set drift detection operation. Use this operation id with <code> <a>DescribeStackSetOperation</a> </code> to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the stack set, in addition to the number of resources included in each stack.</p> <p>Once the operation has completed, use the following actions to return drift information:</p> <ul> <li> <p>Use <code> <a>DescribeStackSet</a> </code> to return detailed information about the stack set, including detailed information about the last <i>completed</i> drift operation performed on the stack set. (Information about drift operations that are in progress isn't included.)</p> </li> <li> <p>Use <code> <a>ListStackInstances</a> </code> to return a list of stack instances belonging to the stack set, including the drift status and last drift time checked of each instance.</p> </li> <li> <p>Use <code> <a>DescribeStackInstance</a> </code> to return detailed information about a specific stack instance, including its drift status and last drift time checked.</p> </li> </ul> <p>For more information about performing a drift detection operation on a stack set, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Detecting unmanaged changes in stack sets</a>.</p> <p>You can only run a single drift detection operation on a given stack set at one time.</p> <p>To stop a drift detection stack set operation, use <code> <a>StopStackSetOperation</a> </code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostDetectStackSetDriftRequestAction, PostDetectStackSetDriftRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_detect_stack_set_drift(
    action=PostDetectStackSetDriftRequestAction.DETECT_STACK_SET_DRIFT,
    version=PostDetectStackSetDriftRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostDetectStackSetDriftRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostDetectStackSetDriftRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_estimate_template_cost</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetEstimateTemplateCostRequestAction, GetEstimateTemplateCostRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_estimate_template_cost(
    action=GetEstimateTemplateCostRequestAction.ESTIMATE_TEMPLATE_COST,
    version=GetEstimateTemplateCostRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetEstimateTemplateCostRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetEstimateTemplateCostRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**template_body:** `typing.Optional[str]` — <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.)</p> <p>Conditional: You must pass <code>TemplateBody</code> or <code>TemplateURL</code>. If both are passed, only <code>TemplateBody</code> is used.</p>
    
</dd>
</dl>

<dl>
<dd>

**template_url:** `typing.Optional[str]` — <p>Location of file containing the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]` — A list of <code>Parameter</code> structures that specify input parameters.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_estimate_template_cost</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostEstimateTemplateCostRequestAction, PostEstimateTemplateCostRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_estimate_template_cost(
    action=PostEstimateTemplateCostRequestAction.ESTIMATE_TEMPLATE_COST,
    version=PostEstimateTemplateCostRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostEstimateTemplateCostRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostEstimateTemplateCostRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_execute_change_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the <a>DescribeStacks</a> action to view the status of the update.</p> <p>When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack.</p> <p>If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy.</p> <p>To create a change set for the entire stack hierarchy, <code>IncludeNestedStacks</code> must have been set to <code>True</code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetExecuteChangeSetRequestAction, GetExecuteChangeSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_execute_change_set(
    change_set_name="x",
    action=GetExecuteChangeSetRequestAction.EXECUTE_CHANGE_SET,
    version=GetExecuteChangeSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**change_set_name:** `str` — The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetExecuteChangeSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetExecuteChangeSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `typing.Optional[str]` — If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that's associated with the change set you want to execute.
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — A unique identifier for this <code>ExecuteChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to execute a change set to update a stack with the same name. You might retry <code>ExecuteChangeSet</code> requests to ensure that CloudFormation successfully received them.
    
</dd>
</dl>

<dl>
<dd>

**disable_rollback:** `typing.Optional[bool]` — <p>Preserves the state of previously provisioned resources when an operation fails.</p> <p>Default: <code>True</code> </p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_execute_change_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the <a>DescribeStacks</a> action to view the status of the update.</p> <p>When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack.</p> <p>If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy.</p> <p>To create a change set for the entire stack hierarchy, <code>IncludeNestedStacks</code> must have been set to <code>True</code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostExecuteChangeSetRequestAction, PostExecuteChangeSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_execute_change_set(
    action=PostExecuteChangeSetRequestAction.EXECUTE_CHANGE_SET,
    version=PostExecuteChangeSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostExecuteChangeSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostExecuteChangeSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_get_stack_policy</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetGetStackPolicyRequestAction, GetGetStackPolicyRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_get_stack_policy(
    stack_name="StackName",
    action=GetGetStackPolicyRequestAction.GET_STACK_POLICY,
    version=GetGetStackPolicyRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name or unique stack ID that's associated with the stack whose policy you want to get.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetGetStackPolicyRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetGetStackPolicyRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_get_stack_policy</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostGetStackPolicyRequestAction, PostGetStackPolicyRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_get_stack_policy(
    action=PostGetStackPolicyRequestAction.GET_STACK_POLICY,
    version=PostGetStackPolicyRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostGetStackPolicyRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostGetStackPolicyRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_get_template</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns the template body for a specified stack. You can get the template for running or deleted stacks.</p> <p>For deleted stacks, <code>GetTemplate</code> returns the template for up to 90 days after the stack has been deleted.</p> <note> <p>If the template doesn't exist, a <code>ValidationError</code> is returned.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetGetTemplateRequestAction, GetGetTemplateRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_get_template(
    action=GetGetTemplateRequestAction.GET_TEMPLATE,
    version=GetGetTemplateRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetGetTemplateRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetGetTemplateRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `typing.Optional[str]` — <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>
    
</dd>
</dl>

<dl>
<dd>

**change_set_name:** `typing.Optional[str]` — The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you specify a name, you must also specify the <code>StackName</code>.
    
</dd>
</dl>

<dl>
<dd>

**template_stage:** `typing.Optional[GetGetTemplateRequestTemplateStage]` — <p>For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify <code>Original</code>. To get the template after CloudFormation has processed all transforms, specify <code>Processed</code>.</p> <p>If the template doesn't include transforms, <code>Original</code> and <code>Processed</code> return the same template. By default, CloudFormation specifies <code>Processed</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_get_template</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns the template body for a specified stack. You can get the template for running or deleted stacks.</p> <p>For deleted stacks, <code>GetTemplate</code> returns the template for up to 90 days after the stack has been deleted.</p> <note> <p>If the template doesn't exist, a <code>ValidationError</code> is returned.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostGetTemplateRequestAction, PostGetTemplateRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_get_template(
    action=PostGetTemplateRequestAction.GET_TEMPLATE,
    version=PostGetTemplateRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostGetTemplateRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostGetTemplateRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_get_template_summary</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about a new or existing template. The <code>GetTemplateSummary</code> action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.</p> <p>You can use the <code>GetTemplateSummary</code> action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.</p> <p>For deleted stacks, <code>GetTemplateSummary</code> returns the template information for up to 90 days after the stack has been deleted. If the template doesn't exist, a <code>ValidationError</code> is returned.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetGetTemplateSummaryRequestAction, GetGetTemplateSummaryRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_get_template_summary(
    action=GetGetTemplateSummaryRequestAction.GET_TEMPLATE_SUMMARY,
    version=GetGetTemplateSummaryRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetGetTemplateSummaryRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetGetTemplateSummaryRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**template_body:** `typing.Optional[str]` — <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information about templates, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**template_url:** `typing.Optional[str]` — <p>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that's located in an Amazon S3 bucket or a Systems Manager document. For more information about templates, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `typing.Optional[str]` — <p>The name or the stack ID that's associated with the stack, which aren't always interchangeable. For running stacks, you can specify either the stack's name or its unique stack ID. For deleted stack, you must specify the unique stack ID.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**stack_set_name:** `typing.Optional[str]` — <p>The name or unique ID of the stack set from which the stack was created.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetGetTemplateSummaryRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_get_template_summary</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns information about a new or existing template. The <code>GetTemplateSummary</code> action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.</p> <p>You can use the <code>GetTemplateSummary</code> action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.</p> <p>For deleted stacks, <code>GetTemplateSummary</code> returns the template information for up to 90 days after the stack has been deleted. If the template doesn't exist, a <code>ValidationError</code> is returned.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostGetTemplateSummaryRequestAction, PostGetTemplateSummaryRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_get_template_summary(
    action=PostGetTemplateSummaryRequestAction.GET_TEMPLATE_SUMMARY,
    version=PostGetTemplateSummaryRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostGetTemplateSummaryRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostGetTemplateSummaryRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_import_stacks_to_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Import existing stacks into a new stack sets. Use the stack import operation to import up to 10 stacks into a new stack set in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.</p> <note> <p> <code>ImportStacksToStackSet</code> is only supported by self-managed permissions.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetImportStacksToStackSetRequestAction, GetImportStacksToStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_import_stacks_to_stack_set(
    stack_set_name="StackSetName",
    action=GetImportStacksToStackSetRequestAction.IMPORT_STACKS_TO_STACK_SET,
    version=GetImportStacksToStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name of the stack set. The name must be unique in the Region where you create your stack set.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetImportStacksToStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetImportStacksToStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_ids:** `typing.Optional[typing.Union[StackId, typing.Sequence[StackId]]]` — <p>The IDs of the stacks you are importing into a stack set. You import up to 10 stacks per stack set at a time.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**stack_ids_url:** `typing.Optional[str]` — <p>The Amazon S3 URL which contains list of stack ids to be inputted.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**organizational_unit_ids:** `typing.Optional[typing.Union[OrganizationalUnitId, typing.Sequence[OrganizationalUnitId]]]` — The list of OU ID's to which the stacks being imported has to be mapped as deployment target.
    
</dd>
</dl>

<dl>
<dd>

**operation_preferences:** `typing.Optional[GetImportStacksToStackSetRequestOperationPreferences]` — 
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `typing.Optional[str]` — A unique, user defined, identifier for the stack set operation.
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetImportStacksToStackSetRequestCallAs]` — <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>For service managed stack sets, specify <code>DELEGATED_ADMIN</code>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_import_stacks_to_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Import existing stacks into a new stack sets. Use the stack import operation to import up to 10 stacks into a new stack set in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.</p> <note> <p> <code>ImportStacksToStackSet</code> is only supported by self-managed permissions.</p> </note>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostImportStacksToStackSetRequestAction, PostImportStacksToStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_import_stacks_to_stack_set(
    action=PostImportStacksToStackSetRequestAction.IMPORT_STACKS_TO_STACK_SET,
    version=PostImportStacksToStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostImportStacksToStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostImportStacksToStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_change_sets</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the <code>CREATE_IN_PROGRESS</code> or <code>CREATE_PENDING</code> state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListChangeSetsRequestAction, GetListChangeSetsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_change_sets(
    stack_name="x",
    action=GetListChangeSetsRequestAction.LIST_CHANGE_SETS,
    version=GetListChangeSetsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetListChangeSetsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListChangeSetsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string (provided by the <a>ListChangeSets</a> response output) that identifies the next page of change sets that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_change_sets</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the <code>CREATE_IN_PROGRESS</code> or <code>CREATE_PENDING</code> state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListChangeSetsRequestAction, PostListChangeSetsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_change_sets(
    action=PostListChangeSetsRequestAction.LIST_CHANGE_SETS,
    version=PostListChangeSetsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListChangeSetsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListChangeSetsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_exports</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html"> CloudFormation export stack output values</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListExportsRequestAction, GetListExportsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_exports(
    action=GetListExportsRequestAction.LIST_EXPORTS,
    version=GetListExportsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetListExportsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListExportsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string (provided by the <a>ListExports</a> response output) that identifies the next page of exported output values that you asked to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_exports</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html"> CloudFormation export stack output values</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListExportsRequestAction, PostListExportsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_exports(
    action=PostListExportsRequestAction.LIST_EXPORTS,
    version=PostListExportsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListExportsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListExportsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_imports</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see <a>ListExports</a>.</p> <p>For more information about importing an exported output value, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListImportsRequestAction, GetListImportsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_imports(
    export_name="ExportName",
    action=GetListImportsRequestAction.LIST_IMPORTS,
    version=GetListImportsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**export_name:** `str` — The name of the exported output value. CloudFormation returns the stack names that are importing this value.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetListImportsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListImportsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string (provided by the <a>ListImports</a> response output) that identifies the next page of stacks that are importing the specified exported output value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_imports</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see <a>ListExports</a>.</p> <p>For more information about importing an exported output value, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-importvalue.html"> <code>Fn::ImportValue</code> </a> function.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListImportsRequestAction, PostListImportsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_imports(
    action=PostListImportsRequestAction.LIST_IMPORTS,
    version=PostListImportsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListImportsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListImportsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_stack_instances</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListStackInstancesRequestAction, GetListStackInstancesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_stack_instances(
    stack_set_name="StackSetName",
    action=GetListStackInstancesRequestAction.LIST_STACK_INSTANCES,
    version=GetListStackInstancesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set that you want to list stack instances for.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetListStackInstancesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListStackInstancesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — If the previous request didn't return all the remaining results, the response's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackInstances</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` — The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Union[StackInstanceFilter, typing.Sequence[StackInstanceFilter]]]` — The filter to apply to stack instances
    
</dd>
</dl>

<dl>
<dd>

**stack_instance_account:** `typing.Optional[str]` — The name of the Amazon Web Services account that you want to list stack instances for.
    
</dd>
</dl>

<dl>
<dd>

**stack_instance_region:** `typing.Optional[str]` — The name of the Region where you want to list stack instances.
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetListStackInstancesRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_stack_instances</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about stack instances that are associated with the specified stack set. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListStackInstancesRequestAction, PostListStackInstancesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_stack_instances(
    action=PostListStackInstancesRequestAction.LIST_STACK_INSTANCES,
    version=PostListStackInstancesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListStackInstancesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListStackInstancesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[str]` — Pagination limit
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_stack_resources</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns descriptions of all resources of the specified stack.</p> <p>For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListStackResourcesRequestAction, GetListStackResourcesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_stack_resources(
    stack_name="StackName",
    action=GetListStackResourcesRequestAction.LIST_STACK_RESOURCES,
    version=GetListStackResourcesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — <p>The name or the unique stack ID that is associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Default: There is no default value.</p>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetListStackResourcesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListStackResourcesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string that identifies the next page of stack resources that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_stack_resources</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns descriptions of all resources of the specified stack.</p> <p>For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListStackResourcesRequestAction, PostListStackResourcesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_stack_resources(
    action=PostListStackResourcesRequestAction.LIST_STACK_RESOURCES,
    version=PostListStackResourcesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListStackResourcesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListStackResourcesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_stack_set_operation_results</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about the results of a stack set operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListStackSetOperationResultsRequestAction, GetListStackSetOperationResultsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_stack_set_operation_results(
    stack_set_name="StackSetName",
    operation_id="x",
    action=GetListStackSetOperationResultsRequestAction.LIST_STACK_SET_OPERATION_RESULTS,
    version=GetListStackSetOperationResultsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set that you want to get operation results for.
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `str` — The ID of the stack set operation.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetListStackSetOperationResultsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListStackSetOperationResultsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — If the previous request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSetOperationResults</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` — The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetListStackSetOperationResultsRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[typing.Union[OperationResultFilter, typing.Sequence[OperationResultFilter]]]` — The filter to apply to operation results.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_stack_set_operation_results</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about the results of a stack set operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListStackSetOperationResultsRequestAction, PostListStackSetOperationResultsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_stack_set_operation_results(
    action=PostListStackSetOperationResultsRequestAction.LIST_STACK_SET_OPERATION_RESULTS,
    version=PostListStackSetOperationResultsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListStackSetOperationResultsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListStackSetOperationResultsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[str]` — Pagination limit
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_stack_set_operations</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about operations performed on a stack set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListStackSetOperationsRequestAction, GetListStackSetOperationsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_stack_set_operations(
    stack_set_name="StackSetName",
    action=GetListStackSetOperationsRequestAction.LIST_STACK_SET_OPERATIONS,
    version=GetListStackSetOperationsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set that you want to get operation summaries for.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetListStackSetOperationsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListStackSetOperationsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSetOperations</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` — The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetListStackSetOperationsRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_stack_set_operations</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about operations performed on a stack set.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListStackSetOperationsRequestAction, PostListStackSetOperationsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_stack_set_operations(
    action=PostListStackSetOperationsRequestAction.LIST_STACK_SET_OPERATIONS,
    version=PostListStackSetOperationsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListStackSetOperationsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListStackSetOperationsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[str]` — Pagination limit
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_stack_sets</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns summary information about stack sets that are associated with the user.</p> <ul> <li> <p>[Self-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to your Amazon Web Services account, <code>ListStackSets</code> returns all self-managed stack sets in your Amazon Web Services account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to the organization's management account, <code>ListStackSets</code> returns all stack sets in the management account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>DELEGATED_ADMIN</code> while signed in to your member account, <code>ListStackSets</code> returns all stack sets with service-managed permissions in the management account.</p> </li> </ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListStackSetsRequestAction, GetListStackSetsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_stack_sets(
    action=GetListStackSetsRequestAction.LIST_STACK_SETS,
    version=GetListStackSetsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetListStackSetsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListStackSetsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call <code>ListStackSets</code> again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` — The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[GetListStackSetsRequestStatus]` — The status of the stack sets that you want to get summary information about.
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetListStackSetsRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_stack_sets</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Returns summary information about stack sets that are associated with the user.</p> <ul> <li> <p>[Self-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to your Amazon Web Services account, <code>ListStackSets</code> returns all self-managed stack sets in your Amazon Web Services account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to the organization's management account, <code>ListStackSets</code> returns all stack sets in the management account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>DELEGATED_ADMIN</code> while signed in to your member account, <code>ListStackSets</code> returns all stack sets with service-managed permissions in the management account.</p> </li> </ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListStackSetsRequestAction, PostListStackSetsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_stack_sets(
    action=PostListStackSetsRequestAction.LIST_STACK_SETS,
    version=PostListStackSetsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListStackSetsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListStackSetsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[str]` — Pagination limit
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_stacks</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListStacksRequestAction, GetListStacksRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_stacks(
    action=GetListStacksRequestAction.LIST_STACKS,
    version=GetListStacksRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetListStacksRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListStacksRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — A string that identifies the next page of stacks that you want to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**stack_status_filter:** `typing.Optional[typing.Union[StackStatus, typing.Sequence[StackStatus]]]` — Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the <code>StackStatus</code> parameter of the <a>Stack</a> data type.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_stacks</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the summary information for stacks whose status matches the specified StackStatusFilter. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no StackStatusFilter is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListStacksRequestAction, PostListStacksRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_stacks(
    action=PostListStacksRequestAction.LIST_STACKS,
    version=PostListStacksRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListStacksRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListStacksRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_type_registrations</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of registration tokens for the specified extension(s).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListTypeRegistrationsRequestAction, GetListTypeRegistrationsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_type_registrations(
    action=GetListTypeRegistrationsRequestAction.LIST_TYPE_REGISTRATIONS,
    version=GetListTypeRegistrationsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetListTypeRegistrationsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListTypeRegistrationsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetListTypeRegistrationsRequestType]` — <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**registration_status_filter:** `typing.Optional[GetListTypeRegistrationsRequestRegistrationStatusFilter]` — <p>The current status of the extension registration request.</p> <p>The default is <code>IN_PROGRESS</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` — The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_type_registrations</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a list of registration tokens for the specified extension(s).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListTypeRegistrationsRequestAction, PostListTypeRegistrationsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_type_registrations(
    action=PostListTypeRegistrationsRequestAction.LIST_TYPE_REGISTRATIONS,
    version=PostListTypeRegistrationsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListTypeRegistrationsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListTypeRegistrationsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[str]` — Pagination limit
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_type_versions</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about the versions of an extension.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListTypeVersionsRequestAction, GetListTypeVersionsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_type_versions(
    action=GetListTypeVersionsRequestAction.LIST_TYPE_VERSIONS,
    version=GetListTypeVersionsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetListTypeVersionsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListTypeVersionsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetListTypeVersionsRequestType]` — <p>The kind of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The name of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` — The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — If the previous paginated request didn't return all of the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    
</dd>
</dl>

<dl>
<dd>

**deprecated_status:** `typing.Optional[GetListTypeVersionsRequestDeprecatedStatus]` — <p>The deprecation status of the extension versions that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension version has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>The default is <code>LIVE</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**publisher_id:** `typing.Optional[str]` — <p>The publisher ID of the extension publisher.</p> <p>Extensions published by Amazon aren't assigned a publisher ID.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_type_versions</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about the versions of an extension.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListTypeVersionsRequestAction, PostListTypeVersionsRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_type_versions(
    action=PostListTypeVersionsRequestAction.LIST_TYPE_VERSIONS,
    version=PostListTypeVersionsRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListTypeVersionsRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListTypeVersionsRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[str]` — Pagination limit
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_list_types</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about extension that have been registered with CloudFormation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetListTypesRequestAction, GetListTypesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_list_types(
    action=GetListTypesRequestAction.LIST_TYPES,
    version=GetListTypesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetListTypesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetListTypesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**visibility:** `typing.Optional[GetListTypesRequestVisibility]` — <p>The scope at which the extensions are visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: Extensions that are visible and usable within this account and region. This includes:</p> <ul> <li> <p>Private extensions you have registered in this account and region.</p> </li> <li> <p>Public extensions that you have activated in this account and region.</p> </li> </ul> </li> <li> <p> <code>PUBLIC</code>: Extensions that are publicly visible and available to be activated within any Amazon Web Services account. This includes extensions from Amazon Web Services, in addition to third-party publishers.</p> </li> </ul> <p>The default is <code>PRIVATE</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**provisioning_type:** `typing.Optional[GetListTypesRequestProvisioningType]` — <p>For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include create, read, and delete handlers, and therefore can't actually be provisioned.</p> </li> </ul> <p>The default is <code>FULLY_MUTABLE</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**deprecated_status:** `typing.Optional[GetListTypesRequestDeprecatedStatus]` — <p>The deprecation status of the extension that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is registered for use in CloudFormation operations.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetListTypesRequestType]` — The type of extension.
    
</dd>
</dl>

<dl>
<dd>

**filters:** `typing.Optional[GetListTypesRequestFilters]` — <p>Filter criteria to use in determining which extensions to return.</p> <p>Filters must be compatible with <code>Visibility</code> to return valid results. For example, specifying <code>AWS_TYPES</code> for <code>Category</code> and <code>PRIVATE</code> for <code>Visibility</code> returns an empty list of types, but specifying <code>PUBLIC</code> for <code>Visibility</code> returns the desired list.</p>
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[int]` — The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — If the previous paginated request didn't return all the remaining results, the response object's <code>NextToken</code> parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request object's <code>NextToken</code> parameter. If there are no remaining results, the previous response object's <code>NextToken</code> parameter is set to <code>null</code>.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_list_types</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns summary information about extension that have been registered with CloudFormation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostListTypesRequestAction, PostListTypesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_list_types(
    action=PostListTypesRequestAction.LIST_TYPES,
    version=PostListTypesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostListTypesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostListTypesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**max_results:** `typing.Optional[str]` — Pagination limit
    
</dd>
</dl>

<dl>
<dd>

**next_token:** `typing.Optional[str]` — Pagination token
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_publish_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Publishes the specified extension to the CloudFormation registry as a public extension in this region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetPublishTypeRequestAction, GetPublishTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_publish_type(
    action=GetPublishTypeRequestAction.PUBLISH_TYPE,
    version=GetPublishTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetPublishTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetPublishTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetPublishTypeRequestType]` — <p>The type of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The name of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**public_version_number:** `typing.Optional[str]` — <p>The version number to assign to this version of the extension.</p> <p>Use the following format, and adhere to semantic versioning when assigning a version number to your extension:</p> <p> <code>MAJOR.MINOR.PATCH</code> </p> <p>For more information, see <a href="https://semver.org/">Semantic Versioning 2.0.0</a>.</p> <p>If you don't specify a version number, CloudFormation increments the version number by one minor version release.</p> <p>You cannot specify a version number the first time you publish a type. CloudFormation automatically sets the first version number to be <code>1.0.0</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_publish_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Publishes the specified extension to the CloudFormation registry as a public extension in this region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostPublishTypeRequestAction, PostPublishTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_publish_type(
    action=PostPublishTypeRequestAction.PUBLISH_TYPE,
    version=PostPublishTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostPublishTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostPublishTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_record_handler_progress</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Reports progress of a resource handler to CloudFormation.</p> <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>. Don't use this API in your code.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetRecordHandlerProgressRequestOperationStatus, GetRecordHandlerProgressRequestAction, GetRecordHandlerProgressRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_record_handler_progress(
    bearer_token="x",
    operation_status=GetRecordHandlerProgressRequestOperationStatus.PENDING,
    action=GetRecordHandlerProgressRequestAction.RECORD_HANDLER_PROGRESS,
    version=GetRecordHandlerProgressRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**bearer_token:** `str` — Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    
</dd>
</dl>

<dl>
<dd>

**operation_status:** `GetRecordHandlerProgressRequestOperationStatus` — Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetRecordHandlerProgressRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetRecordHandlerProgressRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**current_operation_status:** `typing.Optional[GetRecordHandlerProgressRequestCurrentOperationStatus]` — Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    
</dd>
</dl>

<dl>
<dd>

**status_message:** `typing.Optional[str]` — Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    
</dd>
</dl>

<dl>
<dd>

**error_code:** `typing.Optional[GetRecordHandlerProgressRequestErrorCode]` — Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    
</dd>
</dl>

<dl>
<dd>

**resource_model:** `typing.Optional[str]` — Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_record_handler_progress</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Reports progress of a resource handler to CloudFormation.</p> <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>. Don't use this API in your code.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostRecordHandlerProgressRequestAction, PostRecordHandlerProgressRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_record_handler_progress(
    action=PostRecordHandlerProgressRequestAction.RECORD_HANDLER_PROGRESS,
    version=PostRecordHandlerProgressRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostRecordHandlerProgressRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostRecordHandlerProgressRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_register_publisher</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions.</p> <p>For information about requirements for registering as a public extension publisher, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p/>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetRegisterPublisherRequestAction, GetRegisterPublisherRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_register_publisher(
    action=GetRegisterPublisherRequestAction.REGISTER_PUBLISHER,
    version=GetRegisterPublisherRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetRegisterPublisherRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetRegisterPublisherRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**accept_terms_and_conditions:** `typing.Optional[bool]` — <p>Whether you accept the <a href="https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf">Terms and Conditions</a> for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry.</p> <p>The default is <code>false</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**connection_arn:** `typing.Optional[str]` — <p>If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation CLI User Guide</i>.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_register_publisher</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions.</p> <p>For information about requirements for registering as a public extension publisher, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p/>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostRegisterPublisherRequestAction, PostRegisterPublisherRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_register_publisher(
    action=PostRegisterPublisherRequestAction.REGISTER_PUBLISHER,
    version=PostRegisterPublisherRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostRegisterPublisherRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostRegisterPublisherRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_register_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:</p> <ul> <li> <p>Validating the extension schema.</p> </li> <li> <p>Determining which handlers, if any, have been specified for the extension.</p> </li> <li> <p>Making the extension available for use in your account.</p> </li> </ul> <p>For more information about how to develop extensions and ready them for registration, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html">Creating Resource Providers</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per region. Use <a href="AWSCloudFormation/latest/APIReference/API_DeregisterType.html">DeregisterType</a> to deregister specific extension versions if necessary.</p> <p>Once you have initiated a registration request using <code> <a>RegisterType</a> </code>, you can use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of the registration request.</p> <p>Once you have registered a private extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetRegisterTypeRequestAction, GetRegisterTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_register_type(
    type_name="strawberry",
    schema_handler_package="x",
    action=GetRegisterTypeRequestAction.REGISTER_TYPE,
    version=GetRegisterTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type_name:** `str` — <p>The name of the extension being registered.</p> <p>We suggest that extension names adhere to the following patterns:</p> <ul> <li> <p>For resource types, <i>company_or_organization</i>::<i>service</i>::<i>type</i>.</p> </li> <li> <p>For modules, <i>company_or_organization</i>::<i>service</i>::<i>type</i>::MODULE.</p> </li> <li> <p>For hooks, <i>MyCompany</i>::<i>Testing</i>::<i>MyTestHook</i>.</p> </li> </ul> <note> <p>The following organization namespaces are reserved and can't be used in your extension names:</p> <ul> <li> <p> <code>Alexa</code> </p> </li> <li> <p> <code>AMZN</code> </p> </li> <li> <p> <code>Amazon</code> </p> </li> <li> <p> <code>AWS</code> </p> </li> <li> <p> <code>Custom</code> </p> </li> <li> <p> <code>Dev</code> </p> </li> </ul> </note>
    
</dd>
</dl>

<dl>
<dd>

**schema_handler_package:** `str` — <p>A URL to the S3 bucket containing the extension project package that contains the necessary files for the extension you want to register.</p> <p>For information about generating a schema handler package for the extension you want to register, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html">submit</a> in the <i>CloudFormation CLI User Guide</i>.</p> <note> <p>The user registering the extension must be able to access the package in the S3 bucket. That's, the user needs to have <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html">GetObject</a> permissions for the schema handler package. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Identity and Access Management User Guide</i>.</p> </note>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetRegisterTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetRegisterTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetRegisterTypeRequestType]` — The kind of extension.
    
</dd>
</dl>

<dl>
<dd>

**logging_config:** `typing.Optional[GetRegisterTypeRequestLoggingConfig]` — Specifies logging configuration information for an extension.
    
</dd>
</dl>

<dl>
<dd>

**execution_role_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension.</p> <p>For CloudFormation to assume the specified execution role, the role must contain a trust relationship with the CloudFormation service principle (<code>resources.cloudformation.amazonaws.com</code>). For more information about adding trust relationships, see <a href="IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy">Modifying a role trust policy</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>If your extension calls Amazon Web Services APIs in any of its handlers, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.</p>
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of an extension from the same registration request, even if the request is submitted multiple times.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_register_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:</p> <ul> <li> <p>Validating the extension schema.</p> </li> <li> <p>Determining which handlers, if any, have been specified for the extension.</p> </li> <li> <p>Making the extension available for use in your account.</p> </li> </ul> <p>For more information about how to develop extensions and ready them for registration, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html">Creating Resource Providers</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per region. Use <a href="AWSCloudFormation/latest/APIReference/API_DeregisterType.html">DeregisterType</a> to deregister specific extension versions if necessary.</p> <p>Once you have initiated a registration request using <code> <a>RegisterType</a> </code>, you can use <code> <a>DescribeTypeRegistration</a> </code> to monitor the progress of the registration request.</p> <p>Once you have registered a private extension in your account and region, use <a href="AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostRegisterTypeRequestAction, PostRegisterTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_register_type(
    action=PostRegisterTypeRequestAction.REGISTER_TYPE,
    version=PostRegisterTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostRegisterTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostRegisterTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_rollback_stack</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>When specifying <code>RollbackStack</code>, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the <a>DescribeStacks</a> operation.</p> <p>Rolls back the specified stack to the last known stable state from <code>CREATE_FAILED</code> or <code>UPDATE_FAILED</code> stack statuses.</p> <p>This operation will delete a stack if it doesn't contain a last known stable state. A last known stable state includes any status in a <code>*_COMPLETE</code>. This includes the following stack statuses.</p> <ul> <li> <p> <code>CREATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_ROLLBACK_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_ROLLBACK_COMPLETE</code> </p> </li> </ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetRollbackStackRequestAction, GetRollbackStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_rollback_stack(
    stack_name="x",
    action=GetRollbackStackRequestAction.ROLLBACK_STACK,
    version=GetRollbackStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name that's associated with the stack.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetRollbackStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetRollbackStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**role_arn:** `typing.Optional[str]` — The Amazon Resource Name (ARN) of an Identity and Access Management role that CloudFormation assumes to rollback the stack.
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — A unique identifier for this <code>RollbackStack</code> request.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_rollback_stack</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>When specifying <code>RollbackStack</code>, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the <a>DescribeStacks</a> operation.</p> <p>Rolls back the specified stack to the last known stable state from <code>CREATE_FAILED</code> or <code>UPDATE_FAILED</code> stack statuses.</p> <p>This operation will delete a stack if it doesn't contain a last known stable state. A last known stable state includes any status in a <code>*_COMPLETE</code>. This includes the following stack statuses.</p> <ul> <li> <p> <code>CREATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_ROLLBACK_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_ROLLBACK_COMPLETE</code> </p> </li> </ul>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostRollbackStackRequestAction, PostRollbackStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_rollback_stack(
    action=PostRollbackStackRequestAction.ROLLBACK_STACK,
    version=PostRollbackStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostRollbackStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostRollbackStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_set_stack_policy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets a stack policy for a specified stack.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetSetStackPolicyRequestAction, GetSetStackPolicyRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_set_stack_policy(
    stack_name="StackName",
    action=GetSetStackPolicyRequestAction.SET_STACK_POLICY,
    version=GetSetStackPolicyRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name or unique stack ID that you want to associate a policy with.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetSetStackPolicyRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetSetStackPolicyRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**stack_policy_body:** `typing.Optional[str]` — Structure containing the stack policy body. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html"> Prevent updates to stack resources</a> in the CloudFormation User Guide. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.
    
</dd>
</dl>

<dl>
<dd>

**stack_policy_url:** `typing.Optional[str]` — Location of a file containing the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an Amazon S3 bucket in the same Amazon Web Services Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_set_stack_policy</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets a stack policy for a specified stack.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostSetStackPolicyRequestAction, PostSetStackPolicyRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_set_stack_policy(
    action=PostSetStackPolicyRequestAction.SET_STACK_POLICY,
    version=PostSetStackPolicyRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostSetStackPolicyRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostSetStackPolicyRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_set_type_configuration</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Specifies the configuration data for a registered CloudFormation extension, in the given account and region.</p> <p>To view the current configuration data for an extension, refer to the <code>ConfigurationSchema</code> element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p> <important> <p>It's strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more details on dynamic references, see <a href="https://docs.aws.amazon.com/">Using dynamic references to specify template values</a> in the <i>CloudFormation User Guide</i>.</p> </important>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetSetTypeConfigurationRequestAction, GetSetTypeConfigurationRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_set_type_configuration(
    configuration="x",
    action=GetSetTypeConfigurationRequestAction.SET_TYPE_CONFIGURATION,
    version=GetSetTypeConfigurationRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**configuration:** `str` — <p>The configuration data for the extension, in this account and region.</p> <p>The configuration data must be formatted as JSON, and validate against the schema returned in the <code>ConfigurationSchema</code> response element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">API_DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration">Defining account-level configuration data for an extension</a> in the <i>CloudFormation CLI User Guide</i>.</p>
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetSetTypeConfigurationRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetSetTypeConfigurationRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**type_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>For public extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">activate the type</a> in this account and region. For private extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">register the type</a> in this account and region.</p> <p>Do not include the extension versions suffix at the end of the ARN. You can set the configuration for an extension, but not for a specific extension version.</p>
    
</dd>
</dl>

<dl>
<dd>

**configuration_alias:** `typing.Optional[str]` — <p>An alias by which to refer to this extension configuration data.</p> <p>Conditional: Specifying a configuration alias is required when setting a configuration for a resource type extension.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The name of the extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetSetTypeConfigurationRequestType]` — <p>The type of extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_set_type_configuration</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Specifies the configuration data for a registered CloudFormation extension, in the given account and region.</p> <p>To view the current configuration data for an extension, refer to the <code>ConfigurationSchema</code> element of <a href="AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p> <important> <p>It's strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more details on dynamic references, see <a href="https://docs.aws.amazon.com/">Using dynamic references to specify template values</a> in the <i>CloudFormation User Guide</i>.</p> </important>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostSetTypeConfigurationRequestAction, PostSetTypeConfigurationRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_set_type_configuration(
    action=PostSetTypeConfigurationRequestAction.SET_TYPE_CONFIGURATION,
    version=PostSetTypeConfigurationRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostSetTypeConfigurationRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostSetTypeConfigurationRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_set_type_default_version</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetSetTypeDefaultVersionRequestAction, GetSetTypeDefaultVersionRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_set_type_default_version(
    action=GetSetTypeDefaultVersionRequestAction.SET_TYPE_DEFAULT_VERSION,
    version=GetSetTypeDefaultVersionRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetSetTypeDefaultVersionRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetSetTypeDefaultVersionRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetSetTypeDefaultVersionRequestType]` — <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `typing.Optional[str]` — The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_set_type_default_version</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostSetTypeDefaultVersionRequestAction, PostSetTypeDefaultVersionRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_set_type_default_version(
    action=PostSetTypeDefaultVersionRequestAction.SET_TYPE_DEFAULT_VERSION,
    version=PostSetTypeDefaultVersionRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostSetTypeDefaultVersionRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostSetTypeDefaultVersionRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_signal_resource</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends a signal to the specified resource with a success or failure status. You can use the <code>SignalResource</code> operation in conjunction with a creation policy or update policy. CloudFormation doesn't proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The <code>SignalResource</code> operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetSignalResourceRequestStatus, GetSignalResourceRequestAction, GetSignalResourceRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_signal_resource(
    stack_name="StackName",
    logical_resource_id="LogicalResourceId",
    unique_id="UniqueId",
    status=GetSignalResourceRequestStatus.SUCCESS,
    action=GetSignalResourceRequestAction.SIGNAL_RESOURCE,
    version=GetSignalResourceRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The stack name or unique stack ID that includes the resource that you want to signal.
    
</dd>
</dl>

<dl>
<dd>

**logical_resource_id:** `str` — The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.
    
</dd>
</dl>

<dl>
<dd>

**unique_id:** `str` — A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `GetSignalResourceRequestStatus` — The status of the signal, which is either success or failure. A failure signal causes CloudFormation to immediately fail the stack creation or update.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetSignalResourceRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetSignalResourceRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_signal_resource</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sends a signal to the specified resource with a success or failure status. You can use the <code>SignalResource</code> operation in conjunction with a creation policy or update policy. CloudFormation doesn't proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The <code>SignalResource</code> operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostSignalResourceRequestAction, PostSignalResourceRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_signal_resource(
    action=PostSignalResourceRequestAction.SIGNAL_RESOURCE,
    version=PostSignalResourceRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostSignalResourceRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostSignalResourceRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_stop_stack_set_operation</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops an in-progress operation on a stack set and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetStopStackSetOperationRequestAction, GetStopStackSetOperationRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_stop_stack_set_operation(
    stack_set_name="StackSetName",
    operation_id="x",
    action=GetStopStackSetOperationRequestAction.STOP_STACK_SET_OPERATION,
    version=GetStopStackSetOperationRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set that you want to stop the operation for.
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `str` — The ID of the stack operation.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetStopStackSetOperationRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetStopStackSetOperationRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetStopStackSetOperationRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_stop_stack_set_operation</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stops an in-progress operation on a stack set and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostStopStackSetOperationRequestAction, PostStopStackSetOperationRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_stop_stack_set_operation(
    action=PostStopStackSetOperationRequestAction.STOP_STACK_SET_OPERATION,
    version=PostStopStackSetOperationRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostStopStackSetOperationRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostStopStackSetOperationRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_test_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.</p> <ul> <li> <p>For resource types, this includes passing all contracts tests defined for the type.</p> </li> <li> <p>For modules, this includes determining if the module's model meets all necessary requirements.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing">Testing your public extension prior to publishing</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in your account and region for testing.</p> <p>To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see <a href="AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>Once you've initiated testing on an extension using <code>TestType</code>, you can pass the returned <code>TypeVersionArn</code> into <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a> to monitor the current test status and test status description for the extension.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetTestTypeRequestAction, GetTestTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_test_type(
    action=GetTestTypeRequestAction.TEST_TYPE,
    version=GetTestTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetTestTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetTestTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[GetTestTypeRequestType]` — <p>The type of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**type_name:** `typing.Optional[str]` — <p>The name of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**version_id:** `typing.Optional[str]` — <p>The version of the extension to test.</p> <p>You can specify the version id with either <code>Arn</code>, or with <code>TypeName</code> and <code>Type</code>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in this account and region for testing.</p>
    
</dd>
</dl>

<dl>
<dd>

**log_delivery_bucket:** `typing.Optional[str]` — <p>The S3 bucket to which CloudFormation delivers the contract test execution logs.</p> <p>CloudFormation delivers the logs by the time contract testing has completed and the extension has been assigned a test type status of <code>PASSED</code> or <code>FAILED</code>.</p> <p>The user calling <code>TestType</code> must be able to access items in the specified S3 bucket. Specifically, the user needs the following permissions:</p> <ul> <li> <p> <code>GetObject</code> </p> </li> <li> <p> <code>PutObject</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Amazon Web Services Identity and Access Management User Guide</i>.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_test_type</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.</p> <ul> <li> <p>For resource types, this includes passing all contracts tests defined for the type.</p> </li> <li> <p>For modules, this includes determining if the module's model meets all necessary requirements.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing">Testing your public extension prior to publishing</a> in the <i>CloudFormation CLI User Guide</i>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in your account and region for testing.</p> <p>To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see <a href="AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>Once you've initiated testing on an extension using <code>TestType</code>, you can pass the returned <code>TypeVersionArn</code> into <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a> to monitor the current test status and test status description for the extension.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation CLI User Guide</i>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostTestTypeRequestAction, PostTestTypeRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_test_type(
    action=PostTestTypeRequestAction.TEST_TYPE,
    version=PostTestTypeRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostTestTypeRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostTestTypeRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_update_stack</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the <a>DescribeStacks</a> action.</p> <p>To get a copy of the template for an existing stack, you can use the <a>GetTemplate</a> action.</p> <p>For more information about creating an update template, updating a stack, and monitoring the progress of the update, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html">Updating a Stack</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetUpdateStackRequestAction, GetUpdateStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_update_stack(
    stack_name="StackName",
    action=GetUpdateStackRequestAction.UPDATE_STACK,
    version=GetUpdateStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_name:** `str` — The name or unique stack ID of the stack to update.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetUpdateStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetUpdateStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**template_body:** `typing.Optional[str]` — <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. (For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.)</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**template_url:** `typing.Optional[str]` — <p>Location of file containing the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**use_previous_template:** `typing.Optional[bool]` — <p>Reuse the existing template that is associated with the stack that you are updating.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**stack_policy_during_update_body:** `typing.Optional[str]` — <p>Structure containing the temporary overriding stack policy body. You can specify either the <code>StackPolicyDuringUpdateBody</code> or the <code>StackPolicyDuringUpdateURL</code> parameter, but not both.</p> <p>If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don't specify a stack policy, the current policy that is associated with the stack will be used.</p>
    
</dd>
</dl>

<dl>
<dd>

**stack_policy_during_update_url:** `typing.Optional[str]` — <p>Location of a file containing the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the <code>StackPolicyDuringUpdateBody</code> or the <code>StackPolicyDuringUpdateURL</code> parameter, but not both.</p> <p>If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don't specify a stack policy, the current policy that is associated with the stack will be used.</p>
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]` — A list of <code>Parameter</code> structures that specify input parameters for the stack. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.
    
</dd>
</dl>

<dl>
<dd>

**capabilities:** `typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]` — <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually updating the stack. If your stack template contains one or more macros, and you choose to update a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <p>If you want to update a stack from a stack template that contains macros <i>and</i> nested stacks, you must update the stack directly from the template using this capability.</p> <important> <p>You should only update stacks directly from a stack template that contains macros if you know what processing the macro performs.</p> <p>Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.</p> </important> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**resource_types:** `typing.Optional[typing.Union[ResourceType, typing.Sequence[ResourceType]]]` — <p>The template resource types that you have permissions to work with for this update stack action, such as <code>AWS::EC2::Instance</code>, <code>AWS::EC2::*</code>, or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource that you're updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. Identity and Access Management (IAM) uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html">Controlling Access with Identity and Access Management</a>.</p>
    
</dd>
</dl>

<dl>
<dd>

**role_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of an Identity and Access Management (IAM) role that CloudFormation assumes to update the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.</p>
    
</dd>
</dl>

<dl>
<dd>

**rollback_configuration:** `typing.Optional[GetUpdateStackRequestRollbackConfiguration]` — The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.
    
</dd>
</dl>

<dl>
<dd>

**stack_policy_body:** `typing.Optional[str]` — <p>Structure containing a new stack policy body. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p> <p>You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don't specify a stack policy, the current policy that is associated with the stack is unchanged.</p>
    
</dd>
</dl>

<dl>
<dd>

**stack_policy_url:** `typing.Optional[str]` — <p>Location of a file containing the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p> <p>You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don't specify a stack policy, the current policy that is associated with the stack is unchanged.</p>
    
</dd>
</dl>

<dl>
<dd>

**notification_ar_ns:** `typing.Optional[typing.Union[NotificationArn, typing.Sequence[NotificationArn]]]` — Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that CloudFormation associates with the stack. Specify an empty list to remove all notification topics.
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]` — <p>Key-value pairs to associate with this stack. CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.</p> <p>If you don't specify this parameter, CloudFormation doesn't modify the stack's tags. If you specify an empty value, CloudFormation removes all associated tags.</p>
    
</dd>
</dl>

<dl>
<dd>

**disable_rollback:** `typing.Optional[bool]` — <p>Preserve the state of previously provisioned resources when an operation fails.</p> <p>Default: <code>False</code> </p>
    
</dd>
</dl>

<dl>
<dd>

**client_request_token:** `typing.Optional[str]` — <p>A unique identifier for this <code>UpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to update a stack with the same name. You might retry <code>UpdateStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_update_stack</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the <a>DescribeStacks</a> action.</p> <p>To get a copy of the template for an existing stack, you can use the <a>GetTemplate</a> action.</p> <p>For more information about creating an update template, updating a stack, and monitoring the progress of the update, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks.html">Updating a Stack</a>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostUpdateStackRequestAction, PostUpdateStackRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_update_stack(
    action=PostUpdateStackRequestAction.UPDATE_STACK,
    version=PostUpdateStackRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostUpdateStackRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostUpdateStackRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_update_stack_instances</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region.</p> <p>You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html">CreateStackInstances</a>.</p> <p>During stack set updates, any parameters overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only update the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetUpdateStackInstancesRequestAction, GetUpdateStackInstancesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_update_stack_instances(
    stack_set_name="StackSetName",
    action=GetUpdateStackInstancesRequestAction.UPDATE_STACK_INSTANCES,
    version=GetUpdateStackInstancesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set associated with the stack instances.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetUpdateStackInstancesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetUpdateStackInstancesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**accounts:** `typing.Optional[typing.Union[Account, typing.Sequence[Account]]]` — <p>[Self-managed permissions] The names of one or more Amazon Web Services accounts for which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**deployment_targets:** `typing.Optional[GetUpdateStackInstancesRequestDeploymentTargets]` — <p>[Service-managed permissions] The Organizations accounts for which you want to update parameter values for stack instances. If your update targets OUs, the overridden parameter values only apply to the accounts that are currently in the target OUs and their child OUs. Accounts added to the target OUs and their child OUs in the future won't use the overridden values.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[typing.Union[Region, typing.Sequence[Region]]]` — The names of one or more Amazon Web Services Regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.
    
</dd>
</dl>

<dl>
<dd>

**parameter_overrides:** `typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]` — <p>A list of input parameters whose values you want to update for the specified stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance update operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the stack set, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During stack set updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <code>UpdateStackSet</code> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**operation_preferences:** `typing.Optional[GetUpdateStackInstancesRequestOperationPreferences]` — Preferences for how CloudFormation performs this stack set operation.
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `typing.Optional[str]` — <p>The unique identifier for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetUpdateStackInstancesRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_update_stack_instances</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region.</p> <p>You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html">CreateStackInstances</a>.</p> <p>During stack set updates, any parameters overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only update the parameter <i>values</i> that are specified in the stack set; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the stack set template. If you add a parameter to a template, before you can override the parameter value specified in the stack set you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the stack set. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostUpdateStackInstancesRequestAction, PostUpdateStackInstancesRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_update_stack_instances(
    action=PostUpdateStackInstancesRequestAction.UPDATE_STACK_INSTANCES,
    version=PostUpdateStackInstancesRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostUpdateStackInstancesRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostUpdateStackInstancesRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_update_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates the stack set, and associated stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent <a>CreateStackInstances</a> calls on the specified stack set use the updated stack set.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetUpdateStackSetRequestAction, GetUpdateStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_update_stack_set(
    stack_set_name="StackSetName",
    action=GetUpdateStackSetRequestAction.UPDATE_STACK_SET,
    version=GetUpdateStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**stack_set_name:** `str` — The name or unique ID of the stack set that you want to update.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetUpdateStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetUpdateStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — A brief description of updates that you are making.
    
</dd>
</dl>

<dl>
<dd>

**template_body:** `typing.Optional[str]` — <p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>
    
</dd>
</dl>

<dl>
<dd>

**template_url:** `typing.Optional[str]` — <p>The location of the file that contains the template body. The URL must point to a template (maximum size: 460,800 bytes) that is located in an Amazon S3 bucket or a Systems Manager document. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>
    
</dd>
</dl>

<dl>
<dd>

**use_previous_template:** `typing.Optional[bool]` — <p>Use the existing template that's associated with the stack set that you're updating.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Union[Parameter, typing.Sequence[Parameter]]]` — A list of input parameters for the stack set template.
    
</dd>
</dl>

<dl>
<dd>

**capabilities:** `typing.Optional[typing.Union[Capability, typing.Sequence[Capability]]]` — <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack set and its associated stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new Identity and Access Management (IAM) users. For those stacks sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html"> AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-addusertogroup.html"> AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your stack set template references one or more macros, you must update the stack set directly from the processed template, without first reviewing the resulting changes in a change set. To update the stack set directly, you must acknowledge this capability. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Using CloudFormation Macros to Perform Custom Processing on Templates</a>.</p> <important> <p>Stack sets with service-managed permissions do not currently support the use of macros in templates. (This includes the <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/create-reusable-transform-function-snippets-and-add-to-your-template-with-aws-include-transform.html">AWS::Include</a> and <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a stack set with service-managed permissions, if you reference a macro in your template the stack set operation will fail.</p> </important> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Union[Tag, typing.Sequence[Tag]]]` — <p>The key-value pairs to associate with this stack set and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.</p> <p>If you specify tags for this parameter, those tags replace any list of tags that are currently associated with this stack set. This means:</p> <ul> <li> <p>If you don't specify this parameter, CloudFormation doesn't modify the stack's tags.</p> </li> <li> <p>If you specify <i>any</i> tags using this parameter, you must specify <i>all</i> the tags that you want associated with this stack set, even tags you've specified before (for example, when creating the stack set or during a previous update of the stack set.). Any tags that you don't include in the updated list of tags are removed from the stack set, and therefore from the stacks and resources as well.</p> </li> <li> <p>If you specify an empty value, CloudFormation removes all currently associated tags.</p> </li> </ul> <p>If you specify new tags as part of an <code>UpdateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the stack set from the list of tags you specify, CloudFormation assumes that you want to remove those tags from the stack set, and checks to see if you have permission to untag resources. If you don't have the necessary permission(s), the entire <code>UpdateStackSet</code> action fails with an <code>access denied</code> error, and the stack set is not updated.</p>
    
</dd>
</dl>

<dl>
<dd>

**operation_preferences:** `typing.Optional[GetUpdateStackSetRequestOperationPreferences]` — Preferences for how CloudFormation performs this stack set operation.
    
</dd>
</dl>

<dl>
<dd>

**administration_role_arn:** `typing.Optional[str]` — <p>The Amazon Resource Name (ARN) of the IAM role to use to update this stack set.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific stack sets within the same administrator account. For more information, see <a href="http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs.html">Granting Permissions for Stack Set Operations</a> in the <i>CloudFormation User Guide</i>.</p> <p>If you specified a customized administrator role when you created the stack set, you must specify a customized administrator role, even if it is the same customized administrator role used with this stack set previously.</p>
    
</dd>
</dl>

<dl>
<dd>

**execution_role_name:** `typing.Optional[str]` — <p>The name of the IAM execution role to use to update the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the stack set operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their stack sets.</p> <p>If you specify a customized execution role, CloudFormation uses that role to update the stack. If you do not specify a customized execution role, CloudFormation performs the update using the role previously associated with the stack set, so long as you have permissions to perform operations on the stack set.</p>
    
</dd>
</dl>

<dl>
<dd>

**deployment_targets:** `typing.Optional[GetUpdateStackSetRequestDeploymentTargets]` — <p>[Service-managed permissions] The Organizations accounts in which to update associated stack instances.</p> <p>To update all the stack instances associated with this stack set, do not specify <code>DeploymentTargets</code> or <code>Regions</code>.</p> <p>If the stack set update includes changes to the template (that is, if <code>TemplateBody</code> or <code>TemplateURL</code> is specified), or the <code>Parameters</code>, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update doesn't include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>
    
</dd>
</dl>

<dl>
<dd>

**permission_model:** `typing.Optional[GetUpdateStackSetRequestPermissionModel]` — <p>Describes how the IAM roles required for stack set operations are created. You cannot modify <code>PermissionModel</code> if there are stack instances associated with your stack set.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant Self-Managed Stack Set Permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-service-managed.html">Grant Service-Managed Stack Set Permissions</a>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**auto_deployment:** `typing.Optional[GetUpdateStackSetRequestAutoDeployment]` — <p>[Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU).</p> <p>If you specify <code>AutoDeployment</code>, don't specify <code>DeploymentTargets</code> or <code>Regions</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**operation_id:** `typing.Optional[str]` — <p>The unique ID for this stack set operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the stack set operation only once, even if you retry the request multiple times. You might retry stack set operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, CloudFormation generates one automatically.</p> <p>Repeating this stack set operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>
    
</dd>
</dl>

<dl>
<dd>

**accounts:** `typing.Optional[typing.Union[Account, typing.Sequence[Account]]]` — <p>[Self-managed permissions] The accounts in which to update associated stack instances. If you specify accounts, you must also specify the Amazon Web Services Regions in which to update stack set instances.</p> <p>To update <i>all</i> the stack instances associated with this stack set, don't specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the stack set update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Amazon Web Services Regions, while leaving all other stack instances with their existing stack instance status.</p>
    
</dd>
</dl>

<dl>
<dd>

**regions:** `typing.Optional[typing.Union[Region, typing.Sequence[Region]]]` — <p>The Amazon Web Services Regions in which to update associated stack instances. If you specify Regions, you must also specify accounts in which to update stack set instances.</p> <p>To update <i>all</i> the stack instances associated with this stack set, do not specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the stack set update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Regions. If the stack set update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>
    
</dd>
</dl>

<dl>
<dd>

**call_as:** `typing.Optional[GetUpdateStackSetRequestCallAs]` — <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for stack sets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
    
</dd>
</dl>

<dl>
<dd>

**managed_execution:** `typing.Optional[GetUpdateStackSetRequestManagedExecution]` — Describes whether StackSets performs non-conflicting operations concurrently and queues conflicting operations.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_update_stack_set</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates the stack set, and associated stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>Even if the stack set operation created by updating the stack set fails (completely or partially, below or above a specified failure tolerance), the stack set is updated with your changes. Subsequent <a>CreateStackInstances</a> calls on the specified stack set use the updated stack set.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostUpdateStackSetRequestAction, PostUpdateStackSetRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_update_stack_set(
    action=PostUpdateStackSetRequestAction.UPDATE_STACK_SET,
    version=PostUpdateStackSetRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostUpdateStackSetRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostUpdateStackSetRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_update_termination_protection</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetUpdateTerminationProtectionRequestAction, GetUpdateTerminationProtectionRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_update_termination_protection(
    enable_termination_protection=True,
    stack_name="x",
    action=GetUpdateTerminationProtectionRequestAction.UPDATE_TERMINATION_PROTECTION,
    version=GetUpdateTerminationProtectionRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**enable_termination_protection:** `bool` — Whether to enable termination protection on the specified stack.
    
</dd>
</dl>

<dl>
<dd>

**stack_name:** `str` — The name or unique ID of the stack for which you want to set termination protection.
    
</dd>
</dl>

<dl>
<dd>

**action:** `GetUpdateTerminationProtectionRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetUpdateTerminationProtectionRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_update_termination_protection</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

<p>Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protecting a Stack From Being Deleted</a> in the <i>CloudFormation User Guide</i>.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostUpdateTerminationProtectionRequestAction, PostUpdateTerminationProtectionRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_update_termination_protection(
    action=PostUpdateTerminationProtectionRequestAction.UPDATE_TERMINATION_PROTECTION,
    version=PostUpdateTerminationProtectionRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostUpdateTerminationProtectionRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostUpdateTerminationProtectionRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">get_validate_template</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, GetValidateTemplateRequestAction, GetValidateTemplateRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.get_validate_template(
    action=GetValidateTemplateRequestAction.VALIDATE_TEMPLATE,
    version=GetValidateTemplateRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `GetValidateTemplateRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `GetValidateTemplateRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**template_body:** `typing.Optional[str]` — <p>Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>
    
</dd>
</dl>

<dl>
<dd>

**template_url:** `typing.Optional[str]` — <p>Location of file containing the template body. The URL must point to a template (max size: 460,800 bytes) that is located in an Amazon S3 bucket or a Systems Manager document. For more information, go to <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-anatomy.html">Template Anatomy</a> in the CloudFormation User Guide.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/fern/client.py">post_validate_template</a>(...) -> str</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi, PostValidateTemplateRequestAction, PostValidateTemplateRequestVersion
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.post_validate_template(
    action=PostValidateTemplateRequestAction.VALIDATE_TEMPLATE,
    version=PostValidateTemplateRequestVersion.TWO_THOUSAND_TEN0515,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**action:** `PostValidateTemplateRequestAction` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `PostValidateTemplateRequestVersion` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

