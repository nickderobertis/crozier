

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.project_create_checkout_key_response import ProjectCreateCheckoutKeyResponse
from ..types.project_create_env_var_response import ProjectCreateEnvVarResponse
from ..types.project_delete_checkout_key_by_fingerprint_response import ProjectDeleteCheckoutKeyByFingerprintResponse
from ..types.project_delete_environment_variable_response import ProjectDeleteEnvironmentVariableResponse
from ..types.project_get_by_slug_response import ProjectGetBySlugResponse
from ..types.project_get_checkout_key_by_fingerprint_response import ProjectGetCheckoutKeyByFingerprintResponse
from ..types.project_get_masked_env_var_response import ProjectGetMaskedEnvVarResponse
from ..types.project_list_checkout_keys_response import ProjectListCheckoutKeysResponse
from ..types.project_list_env_var_values_response import ProjectListEnvVarValuesResponse
from ..types.project_settings import ProjectSettings
from ..types.project_settings_advanced import ProjectSettingsAdvanced
from .raw_client import AsyncRawProjectClient, RawProjectClient
from .types.project_create_checkout_key_request_type import ProjectCreateCheckoutKeyRequestType
from .types.project_list_checkout_keys_request_digest import ProjectListCheckoutKeysRequestDigest


OMIT = typing.cast(typing.Any, ...)


class ProjectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawProjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawProjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawProjectClient
        """
        return self._raw_client

    def getbyslug(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectGetBySlugResponse:
        """
        Retrieves a project by project slug.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGetBySlugResponse
            A project object

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.getbyslug(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.getbyslug(project_slug, request_options=request_options)
        return _response.data

    def listcheckoutkeys(
        self,
        project_slug: str,
        *,
        digest: typing.Optional[ProjectListCheckoutKeysRequestDigest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectListCheckoutKeysResponse:
        """
        Returns a sequence of checkout keys for `:project`.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        digest : typing.Optional[ProjectListCheckoutKeysRequestDigest]
            The fingerprint digest type to return. This may be either `md5` or `sha256`. If not passed, defaults to `md5`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectListCheckoutKeysResponse
            A sequence of checkout keys.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.listcheckoutkeys(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.listcheckoutkeys(project_slug, digest=digest, request_options=request_options)
        return _response.data

    def createcheckoutkey(
        self,
        project_slug: str,
        *,
        type: ProjectCreateCheckoutKeyRequestType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectCreateCheckoutKeyResponse:
        """
        Not available to projects that use GitLab or GitHub App. Creates a new checkout key. This API request is only usable with a user API token.
                                   Please ensure that you have authorized your account with GitHub before creating user keys.
                                   This is necessary to give CircleCI the permission to create a user key associated with
                                   your GitHub user account. You can find this page by visiting Project Settings > Checkout SSH Keys

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        type : ProjectCreateCheckoutKeyRequestType
            The type of checkout key to create. This may be either `deploy-key` or `user-key`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectCreateCheckoutKeyResponse
            The checkout key.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.createcheckoutkey(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            type="user-key",
        )
        """
        _response = self._raw_client.createcheckoutkey(project_slug, type=type, request_options=request_options)
        return _response.data

    def getcheckoutkeybyfingerprint(
        self, project_slug: str, fingerprint: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectGetCheckoutKeyByFingerprintResponse:
        """
        Returns an individual checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        fingerprint : str
            An SSH key fingerprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGetCheckoutKeyByFingerprintResponse
            The checkout key.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.getcheckoutkeybyfingerprint(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            fingerprint="c9:0b:1c:4f:d5:65:56:b9:ad:88:f9:81:2b:37:74:2f",
        )
        """
        _response = self._raw_client.getcheckoutkeybyfingerprint(
            project_slug, fingerprint, request_options=request_options
        )
        return _response.data

    def deletecheckoutkeybyfingerprint(
        self, project_slug: str, fingerprint: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectDeleteCheckoutKeyByFingerprintResponse:
        """
        Deletes the checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        fingerprint : str
            An SSH key fingerprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDeleteCheckoutKeyByFingerprintResponse
            A confirmation message.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.deletecheckoutkeybyfingerprint(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            fingerprint="c9:0b:1c:4f:d5:65:56:b9:ad:88:f9:81:2b:37:74:2f",
        )
        """
        _response = self._raw_client.deletecheckoutkeybyfingerprint(
            project_slug, fingerprint, request_options=request_options
        )
        return _response.data

    def listenvvarvalues(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectListEnvVarValuesResponse:
        """
        Returns four 'x' characters, in addition to the last four ASCII characters of the value, consistent with the display of environment variable values on the CircleCI website.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectListEnvVarValuesResponse
            A sequence of environment variables.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.listenvvarvalues(
            project_slug="gh/CircleCI-Public/api-preview-docs",
        )
        """
        _response = self._raw_client.listenvvarvalues(project_slug, request_options=request_options)
        return _response.data

    def createenvvar(
        self, project_slug: str, *, name: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectCreateEnvVarResponse:
        """
        Creates a new environment variable.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        value : str
            The value of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectCreateEnvVarResponse
            The environment variable.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.createenvvar(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            name="foo",
            value="xxxx1234",
        )
        """
        _response = self._raw_client.createenvvar(project_slug, name=name, value=value, request_options=request_options)
        return _response.data

    def getmaskedenvvar(
        self, project_slug: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectGetMaskedEnvVarResponse:
        """
        Returns the masked value of environment variable :name.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGetMaskedEnvVarResponse
            The environment variable.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.getmaskedenvvar(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            name="foo",
        )
        """
        _response = self._raw_client.getmaskedenvvar(project_slug, name, request_options=request_options)
        return _response.data

    def deleteenvironmentvariable(
        self, project_slug: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectDeleteEnvironmentVariableResponse:
        """
        Deletes the environment variable named :name.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDeleteEnvironmentVariableResponse
            A confirmation message.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.deleteenvironmentvariable(
            project_slug="gh/CircleCI-Public/api-preview-docs",
            name="foo",
        )
        """
        _response = self._raw_client.deleteenvironmentvariable(project_slug, name, request_options=request_options)
        return _response.data

    def createprojectdefaultsettings(
        self, provider: str, organization: str, project: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectSettings:
        """
        [__EXPERIMENTAL__]  Creates a new CircleCI project, and returns a list of the default advanced settings. Can only be called on a repo with a main branch and an existing config.yml file. Not yet available to projects that use GitLab or GitHub App.

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSettings
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.createprojectdefaultsettings(
            provider="gh",
            organization="CircleCI-Public",
            project="api-preview-docs",
        )
        """
        _response = self._raw_client.createprojectdefaultsettings(
            provider, organization, project, request_options=request_options
        )
        return _response.data

    def getsettings(
        self, provider: str, organization: str, project: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectSettings:
        """
        [__EXPERIMENTAL__] Returns a list of the advanced settings for a CircleCI project, whether enabled (true) or not (false).

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSettings
            Successful response.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.getsettings(
            provider="gh",
            organization="CircleCI-Public",
            project="api-preview-docs",
        )
        """
        _response = self._raw_client.getsettings(provider, organization, project, request_options=request_options)
        return _response.data

    def updatesettings(
        self,
        provider: str,
        organization: str,
        project: str,
        *,
        advanced: typing.Optional[ProjectSettingsAdvanced] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectSettings:
        """
        [__EXPERIMENTAL__] Updates one or more of the advanced settings for a CircleCI project.

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        advanced : typing.Optional[ProjectSettingsAdvanced]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSettings
            Successful response. Always includes the full advanced settings object. Returned even when the provided updates match the existing settings, but can also be returned when `oss: true` fails to set.

        Examples
        --------
        from fern import FernApi, ProjectSettingsAdvanced

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.project.updatesettings(
            provider="gh",
            organization="CircleCI-Public",
            project="api-preview-docs",
            advanced=ProjectSettingsAdvanced(
                autocancel_builds=False,
                build_prs_only=True,
                pr_only_branch_overrides=["main"],
            ),
        )
        """
        _response = self._raw_client.updatesettings(
            provider, organization, project, advanced=advanced, request_options=request_options
        )
        return _response.data


class AsyncProjectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawProjectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawProjectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawProjectClient
        """
        return self._raw_client

    async def getbyslug(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectGetBySlugResponse:
        """
        Retrieves a project by project slug.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGetBySlugResponse
            A project object

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.getbyslug(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getbyslug(project_slug, request_options=request_options)
        return _response.data

    async def listcheckoutkeys(
        self,
        project_slug: str,
        *,
        digest: typing.Optional[ProjectListCheckoutKeysRequestDigest] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectListCheckoutKeysResponse:
        """
        Returns a sequence of checkout keys for `:project`.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        digest : typing.Optional[ProjectListCheckoutKeysRequestDigest]
            The fingerprint digest type to return. This may be either `md5` or `sha256`. If not passed, defaults to `md5`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectListCheckoutKeysResponse
            A sequence of checkout keys.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.listcheckoutkeys(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listcheckoutkeys(
            project_slug, digest=digest, request_options=request_options
        )
        return _response.data

    async def createcheckoutkey(
        self,
        project_slug: str,
        *,
        type: ProjectCreateCheckoutKeyRequestType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectCreateCheckoutKeyResponse:
        """
        Not available to projects that use GitLab or GitHub App. Creates a new checkout key. This API request is only usable with a user API token.
                                   Please ensure that you have authorized your account with GitHub before creating user keys.
                                   This is necessary to give CircleCI the permission to create a user key associated with
                                   your GitHub user account. You can find this page by visiting Project Settings > Checkout SSH Keys

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        type : ProjectCreateCheckoutKeyRequestType
            The type of checkout key to create. This may be either `deploy-key` or `user-key`.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectCreateCheckoutKeyResponse
            The checkout key.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.createcheckoutkey(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                type="user-key",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createcheckoutkey(project_slug, type=type, request_options=request_options)
        return _response.data

    async def getcheckoutkeybyfingerprint(
        self, project_slug: str, fingerprint: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectGetCheckoutKeyByFingerprintResponse:
        """
        Returns an individual checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        fingerprint : str
            An SSH key fingerprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGetCheckoutKeyByFingerprintResponse
            The checkout key.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.getcheckoutkeybyfingerprint(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                fingerprint="c9:0b:1c:4f:d5:65:56:b9:ad:88:f9:81:2b:37:74:2f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getcheckoutkeybyfingerprint(
            project_slug, fingerprint, request_options=request_options
        )
        return _response.data

    async def deletecheckoutkeybyfingerprint(
        self, project_slug: str, fingerprint: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectDeleteCheckoutKeyByFingerprintResponse:
        """
        Deletes the checkout key via md5 or sha256 fingerprint. sha256 keys should be url-encoded.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        fingerprint : str
            An SSH key fingerprint.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDeleteCheckoutKeyByFingerprintResponse
            A confirmation message.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.deletecheckoutkeybyfingerprint(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                fingerprint="c9:0b:1c:4f:d5:65:56:b9:ad:88:f9:81:2b:37:74:2f",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deletecheckoutkeybyfingerprint(
            project_slug, fingerprint, request_options=request_options
        )
        return _response.data

    async def listenvvarvalues(
        self, project_slug: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectListEnvVarValuesResponse:
        """
        Returns four 'x' characters, in addition to the last four ASCII characters of the value, consistent with the display of environment variable values on the CircleCI website.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectListEnvVarValuesResponse
            A sequence of environment variables.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.listenvvarvalues(
                project_slug="gh/CircleCI-Public/api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.listenvvarvalues(project_slug, request_options=request_options)
        return _response.data

    async def createenvvar(
        self, project_slug: str, *, name: str, value: str, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectCreateEnvVarResponse:
        """
        Creates a new environment variable.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        value : str
            The value of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectCreateEnvVarResponse
            The environment variable.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.createenvvar(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                name="foo",
                value="xxxx1234",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createenvvar(
            project_slug, name=name, value=value, request_options=request_options
        )
        return _response.data

    async def getmaskedenvvar(
        self, project_slug: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectGetMaskedEnvVarResponse:
        """
        Returns the masked value of environment variable :name.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectGetMaskedEnvVarResponse
            The environment variable.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.getmaskedenvvar(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                name="foo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getmaskedenvvar(project_slug, name, request_options=request_options)
        return _response.data

    async def deleteenvironmentvariable(
        self, project_slug: str, name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectDeleteEnvironmentVariableResponse:
        """
        Deletes the environment variable named :name.

        Parameters
        ----------
        project_slug : str
            Project slug in the form `vcs-slug/org-name/repo-name`. The `/` characters may be URL-escaped. For projects that use GitLab or GitHub App, use `circleci` as the `vcs-slug`, replace `org-name` with the organization ID (found in Organization Settings), and replace `repo-name` with the project ID (found in Project Settings).

        name : str
            The name of the environment variable.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectDeleteEnvironmentVariableResponse
            A confirmation message.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.deleteenvironmentvariable(
                project_slug="gh/CircleCI-Public/api-preview-docs",
                name="foo",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.deleteenvironmentvariable(
            project_slug, name, request_options=request_options
        )
        return _response.data

    async def createprojectdefaultsettings(
        self, provider: str, organization: str, project: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectSettings:
        """
        [__EXPERIMENTAL__]  Creates a new CircleCI project, and returns a list of the default advanced settings. Can only be called on a repo with a main branch and an existing config.yml file. Not yet available to projects that use GitLab or GitHub App.

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSettings
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.createprojectdefaultsettings(
                provider="gh",
                organization="CircleCI-Public",
                project="api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.createprojectdefaultsettings(
            provider, organization, project, request_options=request_options
        )
        return _response.data

    async def getsettings(
        self, provider: str, organization: str, project: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ProjectSettings:
        """
        [__EXPERIMENTAL__] Returns a list of the advanced settings for a CircleCI project, whether enabled (true) or not (false).

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSettings
            Successful response.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.getsettings(
                provider="gh",
                organization="CircleCI-Public",
                project="api-preview-docs",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.getsettings(provider, organization, project, request_options=request_options)
        return _response.data

    async def updatesettings(
        self,
        provider: str,
        organization: str,
        project: str,
        *,
        advanced: typing.Optional[ProjectSettingsAdvanced] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ProjectSettings:
        """
        [__EXPERIMENTAL__] Updates one or more of the advanced settings for a CircleCI project.

        Parameters
        ----------
        provider : str
            The `provider` segment of a project or org slug, the first of the three. This may be a VCS. For projects that use GitLab or GitHub App, use `circleci`.

        organization : str
            The `organization` segment of a project or org slug, the second of the three. For GitHub OAuth or Bitbucket projects, this is the organization name. For projects that use GitLab or GitHub App, use the organization ID (found in Organization Settings).

        project : str
            The `project` segment of a project slug, the third of the three. For GitHub OAuth or Bitbucket projects, this is the repository name. For projects that use GitLab or GitHub App, use the project ID (found in Project Settings).

        advanced : typing.Optional[ProjectSettingsAdvanced]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProjectSettings
            Successful response. Always includes the full advanced settings object. Returned even when the provided updates match the existing settings, but can also be returned when `oss: true` fails to set.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, ProjectSettingsAdvanced

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.project.updatesettings(
                provider="gh",
                organization="CircleCI-Public",
                project="api-preview-docs",
                advanced=ProjectSettingsAdvanced(
                    autocancel_builds=False,
                    build_prs_only=True,
                    pr_only_branch_overrides=["main"],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.updatesettings(
            provider, organization, project, advanced=advanced, request_options=request_options
        )
        return _response.data
