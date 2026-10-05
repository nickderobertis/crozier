

import typing

import httpx
from . import core
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.logging import LogConfig, Logger
from .core.request_options import RequestOptions
from .raw_client import AsyncRawFernApi, RawFernApi
from .types.entry_node import EntryNode
from .types.entry_node_search_result import EntryNodeSearchResult
from .types.error_node import ErrorNode
from .types.project import Project
from .types.project_status import ProjectStatus


OMIT = typing.cast(typing.Any, ...)


class FernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import FernApi

    client = FernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = SyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = RawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> RawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFernApi
        """
        return self._raw_client

    def hello_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.hello_get()
        """
        _response = self._raw_client.hello_get(request_options=request_options)
        return _response.data

    def pong_ping_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Check server health

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.pong_ping_get()
        """
        _response = self._raw_client.pong_ping_get(request_options=request_options)
        return _response.data

    def get_all_projects_projects_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Project]:
        """
        List projects created in the Taxonomy Editor

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Project]
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_all_projects_projects_get()
        """
        _response = self._raw_client.get_all_projects_projects_get(request_options=request_options)
        return _response.data

    def get_project_info_taxonomy_name_branch_project_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Get information about a Taxonomy Editor project

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.get_project_info_taxonomy_name_branch_project_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.get_project_info_taxonomy_name_branch_project_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def set_project_status_taxonomy_name_branch_set_project_status_get(
        self,
        taxonomy_name: str,
        branch: str,
        *,
        status: typing.Optional[ProjectStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Set the status of a Taxonomy Editor project

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        status : typing.Optional[ProjectStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.set_project_status_taxonomy_name_branch_set_project_status_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.set_project_status_taxonomy_name_branch_set_project_status_get(
            taxonomy_name, branch, status=status, request_options=request_options
        )
        return _response.data

    def find_all_nodes_taxonomy_name_branch_nodes_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get all nodes within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_all_nodes_taxonomy_name_branch_nodes_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.find_all_nodes_taxonomy_name_branch_nodes_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def find_all_root_nodes_taxonomy_name_branch_rootentries_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get all root nodes within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_all_root_nodes_taxonomy_name_branch_rootentries_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.find_all_root_nodes_taxonomy_name_branch_rootentries_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def find_one_entry_taxonomy_name_branch_entry_entry_get(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntryNode:
        """
        Get entry corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntryNode
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_one_entry_taxonomy_name_branch_entry_entry_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
            entry="entry",
        )
        """
        _response = self._raw_client.find_one_entry_taxonomy_name_branch_entry_entry_get(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    def edit_entry_taxonomy_name_branch_entry_entry_post(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Editing an entry in a taxonomy.
        New key-value pairs can be added, old key-value pairs can be updated.
        URL will be of format '/entry/<id>'

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.edit_entry_taxonomy_name_branch_entry_entry_post(
            taxonomy_name="taxonomy_name",
            branch="branch",
            entry="entry",
        )
        """
        _response = self._raw_client.edit_entry_taxonomy_name_branch_entry_entry_post(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    def find_one_entry_parents_taxonomy_name_branch_entry_entry_parents_get(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get parents for a entry corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_one_entry_parents_taxonomy_name_branch_entry_entry_parents_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
            entry="entry",
        )
        """
        _response = self._raw_client.find_one_entry_parents_taxonomy_name_branch_entry_entry_parents_get(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    def find_one_entry_children_taxonomy_name_branch_entry_entry_children_get(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get children for a entry corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_one_entry_children_taxonomy_name_branch_entry_entry_children_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
            entry="entry",
        )
        """
        _response = self._raw_client.find_one_entry_children_taxonomy_name_branch_entry_entry_children_get(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    def edit_entry_children_taxonomy_name_branch_entry_entry_children_post(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Editing an entry's children in a taxonomy.
        New children can be added, old children can be removed.
        URL will be of format '/entry/<id>/children'

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.edit_entry_children_taxonomy_name_branch_entry_entry_children_post(
            taxonomy_name="taxonomy_name",
            branch="branch",
            entry="entry",
        )
        """
        _response = self._raw_client.edit_entry_children_taxonomy_name_branch_entry_entry_children_post(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    def find_one_synonym_taxonomy_name_branch_synonym_synonym_get(
        self, taxonomy_name: str, branch: str, synonym: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get synonym corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        synonym : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_one_synonym_taxonomy_name_branch_synonym_synonym_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
            synonym="synonym",
        )
        """
        _response = self._raw_client.find_one_synonym_taxonomy_name_branch_synonym_synonym_get(
            taxonomy_name, branch, synonym, request_options=request_options
        )
        return _response.data

    def find_all_synonyms_taxonomy_name_branch_synonym_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get all synonyms within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_all_synonyms_taxonomy_name_branch_synonym_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.find_all_synonyms_taxonomy_name_branch_synonym_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def find_one_stopword_taxonomy_name_branch_stopword_stopword_get(
        self, taxonomy_name: str, branch: str, stopword: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get stopword corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        stopword : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_one_stopword_taxonomy_name_branch_stopword_stopword_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
            stopword="stopword",
        )
        """
        _response = self._raw_client.find_one_stopword_taxonomy_name_branch_stopword_stopword_get(
            taxonomy_name, branch, stopword, request_options=request_options
        )
        return _response.data

    def find_all_stopwords_taxonomy_name_branch_stopword_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get all stopwords within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_all_stopwords_taxonomy_name_branch_stopword_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.find_all_stopwords_taxonomy_name_branch_stopword_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def find_header_taxonomy_name_branch_header_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get __header__ within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_header_taxonomy_name_branch_header_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.find_header_taxonomy_name_branch_header_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def find_footer_taxonomy_name_branch_footer_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get __footer__ within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_footer_taxonomy_name_branch_footer_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.find_footer_taxonomy_name_branch_footer_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def find_all_errors_taxonomy_name_branch_parsing_errors_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ErrorNode:
        """
        Get all errors within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorNode
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.find_all_errors_taxonomy_name_branch_parsing_errors_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.find_all_errors_taxonomy_name_branch_parsing_errors_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def search_entry_nodes_taxonomy_name_branch_nodes_entry_get(
        self,
        taxonomy_name: str,
        branch: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntryNodeSearchResult:
        """
        Parameters
        ----------
        taxonomy_name : str

        branch : str

        q : typing.Optional[str]
            The search query string to filter down the returned entry nodes.            Example: is:root language:en not(language):fr

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntryNodeSearchResult
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.search_entry_nodes_taxonomy_name_branch_nodes_entry_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.search_entry_nodes_taxonomy_name_branch_nodes_entry_get(
            taxonomy_name, branch, q=q, page=page, request_options=request_options
        )
        return _response.data

    def export_to_text_file_taxonomy_name_branch_downloadexport_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.export_to_text_file_taxonomy_name_branch_downloadexport_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.export_to_text_file_taxonomy_name_branch_downloadexport_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def export_to_github_taxonomy_name_branch_githubexport_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.export_to_github_taxonomy_name_branch_githubexport_get(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.export_to_github_taxonomy_name_branch_githubexport_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def import_from_github_taxonomy_name_branch_import_post(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get taxonomy from Product Opener GitHub repository

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.import_from_github_taxonomy_name_branch_import_post(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.import_from_github_taxonomy_name_branch_import_post(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    def upload_taxonomy_taxonomy_name_branch_upload_post(
        self,
        taxonomy_name: str,
        branch: str,
        *,
        file: core.File,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Upload taxonomy file to be parsed

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        file : core.File
            See core.File for more documentation

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.upload_taxonomy_taxonomy_name_branch_upload_post(
            taxonomy_name="taxonomy_name",
            branch="branch",
            description="description",
        )
        """
        _response = self._raw_client.upload_taxonomy_taxonomy_name_branch_upload_post(
            taxonomy_name, branch, file=file, description=description, request_options=request_options
        )
        return _response.data

    def create_entry_node_taxonomy_name_branch_entry_post(
        self,
        taxonomy_name: str,
        branch: str,
        *,
        name: str,
        main_language_code: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Creating a new entry node in a taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        name : str

        main_language_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.create_entry_node_taxonomy_name_branch_entry_post(
            taxonomy_name="taxonomy_name",
            branch="branch",
            name="name",
            main_language_code="mainLanguageCode",
        )
        """
        _response = self._raw_client.create_entry_node_taxonomy_name_branch_entry_post(
            taxonomy_name, branch, name=name, main_language_code=main_language_code, request_options=request_options
        )
        return _response.data

    def delete_node_taxonomy_name_branch_nodes_id_delete(
        self, taxonomy_name: str, branch: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Deleting given node from a taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_node_taxonomy_name_branch_nodes_id_delete(
            taxonomy_name="taxonomy_name",
            branch="branch",
            id="id",
        )
        """
        _response = self._raw_client.delete_node_taxonomy_name_branch_nodes_id_delete(
            taxonomy_name, branch, id, request_options=request_options
        )
        return _response.data

    def delete_project_taxonomy_name_branch_delete(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a project

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.delete_project_taxonomy_name_branch_delete(
            taxonomy_name="taxonomy_name",
            branch="branch",
        )
        """
        _response = self._raw_client.delete_project_taxonomy_name_branch_delete(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data


def _make_default_async_client(
    timeout: typing.Optional[float],
    follow_redirects: typing.Optional[bool],
) -> httpx.AsyncClient:
    try:
        import httpx_aiohttp
    except ImportError:
        pass
    else:
        if follow_redirects is not None:
            return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout, follow_redirects=follow_redirects)
        return httpx_aiohttp.HttpxAiohttpClient(timeout=timeout)

    if follow_redirects is not None:
        return httpx.AsyncClient(timeout=timeout, follow_redirects=follow_redirects)
    return httpx.AsyncClient(timeout=timeout)


class AsyncFernApi:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : str
        The base url to use for requests from the client.

    headers : typing.Optional[typing.Dict[str, str]]
        Additional headers to send with every request.

    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests. By default the timeout is 60 seconds, unless a custom httpx client is used, in which case this default is not enforced.

    max_retries : typing.Optional[int]
        The default maximum number of retries for failed requests. Defaults to 2. Per-request `max_retries` in `request_options` takes precedence over this value.

    stream_reconnection_enabled : typing.Optional[bool]
        Whether to automatically reconnect on stream disconnection for resumable streaming endpoints. Defaults to True. Per-request `stream_reconnection_enabled` in `request_options` takes precedence over this value.

    max_stream_reconnection_attempts : typing.Optional[int]
        The maximum number of reconnection attempts for resumable streaming endpoints. Defaults to no limit. Per-request `max_stream_reconnection_attempts` in `request_options` takes precedence over this value.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    logging : typing.Optional[typing.Union[LogConfig, Logger]]
        Configure logging for the SDK. Accepts a LogConfig dict with 'level' (debug/info/warn/error), 'logger' (custom logger implementation), and 'silent' (boolean, defaults to True) fields. You can also pass a pre-configured Logger instance.

    Examples
    --------
    from fern import AsyncFernApi

    client = AsyncFernApi(
        base_url="https://yourhost.com/path/to/api",
    )
    """

    def __init__(
        self,
        *,
        base_url: str,
        headers: typing.Optional[typing.Dict[str, str]] = None,
        timeout: typing.Optional[float] = None,
        max_retries: typing.Optional[int] = None,
        stream_reconnection_enabled: typing.Optional[bool] = None,
        max_stream_reconnection_attempts: typing.Optional[int] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
        logging: typing.Optional[typing.Union[LogConfig, Logger]] = None,
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        _defaulted_max_retries = max_retries if max_retries is not None else 2
        self._client_wrapper = AsyncClientWrapper(
            base_url=base_url,
            headers=headers,
            httpx_client=httpx_client
            if httpx_client is not None
            else _make_default_async_client(timeout=_defaulted_timeout, follow_redirects=follow_redirects),
            timeout=_defaulted_timeout,
            max_retries=_defaulted_max_retries,
            stream_reconnection_enabled=stream_reconnection_enabled,
            max_stream_reconnection_attempts=max_stream_reconnection_attempts,
            logging=logging,
        )
        self._raw_client = AsyncRawFernApi(client_wrapper=self._client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFernApi:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFernApi
        """
        return self._raw_client

    async def hello_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.hello_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.hello_get(request_options=request_options)
        return _response.data

    async def pong_ping_get(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Check server health

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.pong_ping_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.pong_ping_get(request_options=request_options)
        return _response.data

    async def get_all_projects_projects_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Project]:
        """
        List projects created in the Taxonomy Editor

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Project]
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_all_projects_projects_get()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_projects_projects_get(request_options=request_options)
        return _response.data

    async def get_project_info_taxonomy_name_branch_project_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Project:
        """
        Get information about a Taxonomy Editor project

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Project
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.get_project_info_taxonomy_name_branch_project_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_project_info_taxonomy_name_branch_project_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def set_project_status_taxonomy_name_branch_set_project_status_get(
        self,
        taxonomy_name: str,
        branch: str,
        *,
        status: typing.Optional[ProjectStatus] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Set the status of a Taxonomy Editor project

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        status : typing.Optional[ProjectStatus]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.set_project_status_taxonomy_name_branch_set_project_status_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_project_status_taxonomy_name_branch_set_project_status_get(
            taxonomy_name, branch, status=status, request_options=request_options
        )
        return _response.data

    async def find_all_nodes_taxonomy_name_branch_nodes_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get all nodes within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_all_nodes_taxonomy_name_branch_nodes_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_nodes_taxonomy_name_branch_nodes_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def find_all_root_nodes_taxonomy_name_branch_rootentries_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get all root nodes within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_all_root_nodes_taxonomy_name_branch_rootentries_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_root_nodes_taxonomy_name_branch_rootentries_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def find_one_entry_taxonomy_name_branch_entry_entry_get(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> EntryNode:
        """
        Get entry corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntryNode
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_one_entry_taxonomy_name_branch_entry_entry_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
                entry="entry",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_one_entry_taxonomy_name_branch_entry_entry_get(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    async def edit_entry_taxonomy_name_branch_entry_entry_post(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Editing an entry in a taxonomy.
        New key-value pairs can be added, old key-value pairs can be updated.
        URL will be of format '/entry/<id>'

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.edit_entry_taxonomy_name_branch_entry_entry_post(
                taxonomy_name="taxonomy_name",
                branch="branch",
                entry="entry",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_entry_taxonomy_name_branch_entry_entry_post(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    async def find_one_entry_parents_taxonomy_name_branch_entry_entry_parents_get(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get parents for a entry corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_one_entry_parents_taxonomy_name_branch_entry_entry_parents_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
                entry="entry",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_one_entry_parents_taxonomy_name_branch_entry_entry_parents_get(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    async def find_one_entry_children_taxonomy_name_branch_entry_entry_children_get(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get children for a entry corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_one_entry_children_taxonomy_name_branch_entry_entry_children_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
                entry="entry",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_one_entry_children_taxonomy_name_branch_entry_entry_children_get(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    async def edit_entry_children_taxonomy_name_branch_entry_entry_children_post(
        self, taxonomy_name: str, branch: str, entry: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Editing an entry's children in a taxonomy.
        New children can be added, old children can be removed.
        URL will be of format '/entry/<id>/children'

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        entry : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.edit_entry_children_taxonomy_name_branch_entry_entry_children_post(
                taxonomy_name="taxonomy_name",
                branch="branch",
                entry="entry",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.edit_entry_children_taxonomy_name_branch_entry_entry_children_post(
            taxonomy_name, branch, entry, request_options=request_options
        )
        return _response.data

    async def find_one_synonym_taxonomy_name_branch_synonym_synonym_get(
        self, taxonomy_name: str, branch: str, synonym: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get synonym corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        synonym : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_one_synonym_taxonomy_name_branch_synonym_synonym_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
                synonym="synonym",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_one_synonym_taxonomy_name_branch_synonym_synonym_get(
            taxonomy_name, branch, synonym, request_options=request_options
        )
        return _response.data

    async def find_all_synonyms_taxonomy_name_branch_synonym_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get all synonyms within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_all_synonyms_taxonomy_name_branch_synonym_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_synonyms_taxonomy_name_branch_synonym_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def find_one_stopword_taxonomy_name_branch_stopword_stopword_get(
        self, taxonomy_name: str, branch: str, stopword: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get stopword corresponding to id within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        stopword : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_one_stopword_taxonomy_name_branch_stopword_stopword_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
                stopword="stopword",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_one_stopword_taxonomy_name_branch_stopword_stopword_get(
            taxonomy_name, branch, stopword, request_options=request_options
        )
        return _response.data

    async def find_all_stopwords_taxonomy_name_branch_stopword_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get all stopwords within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_all_stopwords_taxonomy_name_branch_stopword_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_stopwords_taxonomy_name_branch_stopword_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def find_header_taxonomy_name_branch_header_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get __header__ within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_header_taxonomy_name_branch_header_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_header_taxonomy_name_branch_header_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def find_footer_taxonomy_name_branch_footer_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get __footer__ within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_footer_taxonomy_name_branch_footer_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_footer_taxonomy_name_branch_footer_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def find_all_errors_taxonomy_name_branch_parsing_errors_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ErrorNode:
        """
        Get all errors within taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ErrorNode
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.find_all_errors_taxonomy_name_branch_parsing_errors_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_all_errors_taxonomy_name_branch_parsing_errors_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def search_entry_nodes_taxonomy_name_branch_nodes_entry_get(
        self,
        taxonomy_name: str,
        branch: str,
        *,
        q: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> EntryNodeSearchResult:
        """
        Parameters
        ----------
        taxonomy_name : str

        branch : str

        q : typing.Optional[str]
            The search query string to filter down the returned entry nodes.            Example: is:root language:en not(language):fr

        page : typing.Optional[int]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        EntryNodeSearchResult
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.search_entry_nodes_taxonomy_name_branch_nodes_entry_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.search_entry_nodes_taxonomy_name_branch_nodes_entry_get(
            taxonomy_name, branch, q=q, page=page, request_options=request_options
        )
        return _response.data

    async def export_to_text_file_taxonomy_name_branch_downloadexport_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.export_to_text_file_taxonomy_name_branch_downloadexport_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_to_text_file_taxonomy_name_branch_downloadexport_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def export_to_github_taxonomy_name_branch_githubexport_get(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.export_to_github_taxonomy_name_branch_githubexport_get(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_to_github_taxonomy_name_branch_githubexport_get(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def import_from_github_taxonomy_name_branch_import_post(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Get taxonomy from Product Opener GitHub repository

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.import_from_github_taxonomy_name_branch_import_post(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_from_github_taxonomy_name_branch_import_post(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data

    async def upload_taxonomy_taxonomy_name_branch_upload_post(
        self,
        taxonomy_name: str,
        branch: str,
        *,
        file: core.File,
        description: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Upload taxonomy file to be parsed

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        file : core.File
            See core.File for more documentation

        description : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.upload_taxonomy_taxonomy_name_branch_upload_post(
                taxonomy_name="taxonomy_name",
                branch="branch",
                description="description",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_taxonomy_taxonomy_name_branch_upload_post(
            taxonomy_name, branch, file=file, description=description, request_options=request_options
        )
        return _response.data

    async def create_entry_node_taxonomy_name_branch_entry_post(
        self,
        taxonomy_name: str,
        branch: str,
        *,
        name: str,
        main_language_code: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Any:
        """
        Creating a new entry node in a taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        name : str

        main_language_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.create_entry_node_taxonomy_name_branch_entry_post(
                taxonomy_name="taxonomy_name",
                branch="branch",
                name="name",
                main_language_code="mainLanguageCode",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_entry_node_taxonomy_name_branch_entry_post(
            taxonomy_name, branch, name=name, main_language_code=main_language_code, request_options=request_options
        )
        return _response.data

    async def delete_node_taxonomy_name_branch_nodes_id_delete(
        self, taxonomy_name: str, branch: str, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Deleting given node from a taxonomy

        Parameters
        ----------
        taxonomy_name : str

        branch : str

        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_node_taxonomy_name_branch_nodes_id_delete(
                taxonomy_name="taxonomy_name",
                branch="branch",
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_node_taxonomy_name_branch_nodes_id_delete(
            taxonomy_name, branch, id, request_options=request_options
        )
        return _response.data

    async def delete_project_taxonomy_name_branch_delete(
        self, taxonomy_name: str, branch: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Delete a project

        Parameters
        ----------
        taxonomy_name : str

        branch : str

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
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.delete_project_taxonomy_name_branch_delete(
                taxonomy_name="taxonomy_name",
                branch="branch",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_project_taxonomy_name_branch_delete(
            taxonomy_name, branch, request_options=request_options
        )
        return _response.data
