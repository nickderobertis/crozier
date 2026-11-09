

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.admin_license_acknowledgement import AdminLicenseAcknowledgement
from ..types.get_suggested_license import GetSuggestedLicense
from ..types.info import Info
from ..types.license_candidate import LicenseCandidate
from ..types.mutate_admin_acknowledgement import MutateAdminAcknowledgement
from ..types.mutate_std_comment import MutateStdComment
from ..types.standard_comment import StandardComment
from .raw_client import AsyncRawLicenseClient, RawLicenseClient
from .types.get_license_by_shortname_response import GetLicenseByShortnameResponse
from .types.get_licenses_request_kind import GetLicensesRequestKind
from .types.get_licenses_response_item import GetLicensesResponseItem


OMIT = typing.cast(typing.Any, ...)


class LicenseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLicenseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLicenseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLicenseClient
        """
        return self._raw_client

    def import_obligation_csv(
        self,
        *,
        file_input: core.File,
        enclosure: typing.Optional[str] = OMIT,
        delimiter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Import an obligation csv file

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        enclosure : typing.Optional[str]
            Enclosure for string in CSV

        delimiter : typing.Optional[str]
            Delimiters for fields in CSV

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Successfully imported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.import_obligation_csv()
        """
        _response = self._raw_client.import_obligation_csv(
            file_input=file_input, enclosure=enclosure, delimiter=delimiter, request_options=request_options
        )
        return _response.data

    def export_license_obligations(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Export a csv license obligation list

        Parameters
        ----------
        id : typing.Optional[int]
            Obligation id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successfully exported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.export_license_obligations()
        """
        with self._raw_client.export_license_obligations(id=id, request_options=request_options) as r:
            yield from r.data

    def import_obligations_from_json(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Import an obligation json file

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Successfully imported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.import_obligations_from_json()
        """
        _response = self._raw_client.import_obligations_from_json(
            file_input=file_input, request_options=request_options
        )
        return _response.data

    def export_obligations_to_json(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Export a json license obligation list

        Parameters
        ----------
        id : typing.Optional[int]
            Obligation id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successfully exported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.export_obligations_to_json()
        """
        with self._raw_client.export_obligations_to_json(id=id, request_options=request_options) as r:
            yield from r.data

    def get_licenses(
        self,
        *,
        kind: typing.Optional[GetLicensesRequestKind] = None,
        group_name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetLicensesResponseItem]:
        """
        Get a list of available licenses (filtered by kind or status)

        Parameters
        ----------
        kind : typing.Optional[GetLicensesRequestKind]
            Which kind of licenses to get.

        group_name : typing.Optional[str]
            The group name to chose

        page : typing.Optional[int]
            Page number to fetch

        limit : typing.Optional[int]
            Limits of responses per request

        active : typing.Optional[bool]
            Get only active licenses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetLicensesResponseItem]
            All licenses from database

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.get_licenses()
        """
        _response = self._raw_client.get_licenses(
            kind=kind, group_name=group_name, page=page, limit=limit, active=active, request_options=request_options
        )
        return _response.data

    def create_license(
        self,
        *,
        short_name: str,
        group_name: typing.Optional[str] = None,
        merge_request: typing.Optional[bool] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        risk: typing.Optional[int] = OMIT,
        is_candidate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Add a new license to the database

        Parameters
        ----------
        short_name : str
            Short name

        group_name : typing.Optional[str]
            The group name to chose

        merge_request : typing.Optional[bool]
            Open a merge request for candidate license?

        full_name : typing.Optional[str]
            Full name

        text : typing.Optional[str]
            License text

        url : typing.Optional[str]
            URL of the license text

        risk : typing.Optional[int]
            Risk level

        is_candidate : typing.Optional[bool]
            Is the license a candidate?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License added successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.create_license(
            short_name="MIT",
        )
        """
        _response = self._raw_client.create_license(
            short_name=short_name,
            group_name=group_name,
            merge_request=merge_request,
            full_name=full_name,
            text=text,
            url=url,
            risk=risk,
            is_candidate=is_candidate,
            request_options=request_options,
        )
        return _response.data

    def import_license(
        self,
        *,
        file_input: core.File,
        enclosure: typing.Optional[str] = OMIT,
        delimiter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Import a csv license to the database

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        enclosure : typing.Optional[str]
            Enclosure for string in CSV

        delimiter : typing.Optional[str]
            Delimiters for fields in CSV

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Successfully imported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.import_license()
        """
        _response = self._raw_client.import_license(
            file_input=file_input, enclosure=enclosure, delimiter=delimiter, request_options=request_options
        )
        return _response.data

    def export_license(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Export a csv license

        Parameters
        ----------
        id : typing.Optional[int]
            License id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successfully exported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.export_license()
        """
        with self._raw_client.export_license(id=id, request_options=request_options) as r:
            yield from r.data

    def handle_import_license(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Import a json license to the database

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Successfully imported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.handle_import_license()
        """
        _response = self._raw_client.handle_import_license(file_input=file_input, request_options=request_options)
        return _response.data

    def export_admin_license_to_json(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Export a json license

        Parameters
        ----------
        id : typing.Optional[int]
            License id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            Successfully exported

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.export_admin_license_to_json()
        """
        with self._raw_client.export_admin_license_to_json(id=id, request_options=request_options) as r:
            yield from r.data

    def get_license_by_shortname(
        self,
        shortname: str,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLicenseByShortnameResponse:
        """
        Get information about a specific license

        Parameters
        ----------
        shortname : str
            Shortname of the license

        group_name : typing.Optional[str]
            The group name to chose

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLicenseByShortnameResponse
            License

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.get_license_by_shortname(
            shortname="shortname",
        )
        """
        _response = self._raw_client.get_license_by_shortname(
            shortname, group_name=group_name, request_options=request_options
        )
        return _response.data

    def update_license_by_shortname(
        self,
        shortname: str,
        *,
        group_name: typing.Optional[str] = None,
        full_name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        risk: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Update information about a given license

        Parameters
        ----------
        shortname : str
            Shortname of the license

        group_name : typing.Optional[str]
            The group name to chose

        full_name : typing.Optional[str]
            New fullname

        text : typing.Optional[str]
            New license text

        url : typing.Optional[str]
            New URL for license

        risk : typing.Optional[int]
            New risk value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License added successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.update_license_by_shortname(
            shortname="shortname",
        )
        """
        _response = self._raw_client.update_license_by_shortname(
            shortname,
            group_name=group_name,
            full_name=full_name,
            text=text,
            url=url,
            risk=risk,
            request_options=request_options,
        )
        return _response.data

    def get_admin_license_candidates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LicenseCandidate]:
        """
        Get a list of license candidates from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LicenseCandidate]
            Request is successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.get_admin_license_candidates()
        """
        _response = self._raw_client.get_admin_license_candidates(request_options=request_options)
        return _response.data

    def delete_by_license_candidate_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Delete a single admin-license-candidate by the given id.

        Parameters
        ----------
        id : int
            Id of the license-candidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License candidate will be deleted.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.delete_by_license_candidate_id(
            id=1,
        )
        """
        _response = self._raw_client.delete_by_license_candidate_id(id, request_options=request_options)
        return _response.data

    def get_admin_license_acknowledgements(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AdminLicenseAcknowledgement]:
        """
        Get a list of the admin license acknowledgements

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AdminLicenseAcknowledgement]
            Request is successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.get_admin_license_acknowledgements()
        """
        _response = self._raw_client.get_admin_license_acknowledgements(request_options=request_options)
        return _response.data

    def mutate_admin_license_acknowledgement(
        self,
        *,
        request: typing.Sequence[MutateAdminAcknowledgement],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Info]:
        """
        Add, edit and toggle admin-license acknowledgement

        Parameters
        ----------
        request : typing.Sequence[MutateAdminAcknowledgement]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Request is successful

        Examples
        --------
        from fern import FernApi, MutateAdminAcknowledgement

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.mutate_admin_license_acknowledgement(
            request=[MutateAdminAcknowledgement()],
        )
        """
        _response = self._raw_client.mutate_admin_license_acknowledgement(
            request=request, request_options=request_options
        )
        return _response.data

    def get_all_standard_license_comments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[StandardComment]:
        """
        Get a list of all standard license comments.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[StandardComment]
            Request is successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.get_all_standard_license_comments()
        """
        _response = self._raw_client.get_all_standard_license_comments(request_options=request_options)
        return _response.data

    def mutate_std_comments(
        self, *, request: typing.Sequence[MutateStdComment], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Info]:
        """
        Add, edit and toggle standard comments

        Parameters
        ----------
        request : typing.Sequence[MutateStdComment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Request is successful

        Examples
        --------
        from fern import FernApi, MutateStdComment

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.mutate_std_comments(
            request=[MutateStdComment()],
        )
        """
        _response = self._raw_client.mutate_std_comments(request=request, request_options=request_options)
        return _response.data

    def verify_license(
        self,
        shortname: str,
        *,
        parent_shortname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Verify a license as new or variant of another license

        Parameters
        ----------
        shortname : str
            Shortname of the license to be verified

        parent_shortname : typing.Optional[str]
            Shortname of the parent license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License verified successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.verify_license(
            shortname="shortname",
        )
        """
        _response = self._raw_client.verify_license(
            shortname, parent_shortname=parent_shortname, request_options=request_options
        )
        return _response.data

    def merge_license(
        self,
        shortname: str,
        *,
        parent_shortname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Merge a license to another existing license

        Parameters
        ----------
        shortname : str
            Shortname of the license to be merged

        parent_shortname : typing.Optional[str]
            Shortname of the parent license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License merged successfully

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.merge_license(
            shortname="shortname",
        )
        """
        _response = self._raw_client.merge_license(
            shortname, parent_shortname=parent_shortname, request_options=request_options
        )
        return _response.data

    def get_suggested_license(
        self, *, reference_text: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSuggestedLicense:
        """
        Get a single suggested license by the given reference text.

        Parameters
        ----------
        reference_text : typing.Optional[str]
            Reference text to get suggested license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSuggestedLicense
            Request is successful

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.license.get_suggested_license()
        """
        _response = self._raw_client.get_suggested_license(
            reference_text=reference_text, request_options=request_options
        )
        return _response.data


class AsyncLicenseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLicenseClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLicenseClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLicenseClient
        """
        return self._raw_client

    async def import_obligation_csv(
        self,
        *,
        file_input: core.File,
        enclosure: typing.Optional[str] = OMIT,
        delimiter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Import an obligation csv file

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        enclosure : typing.Optional[str]
            Enclosure for string in CSV

        delimiter : typing.Optional[str]
            Delimiters for fields in CSV

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Successfully imported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.import_obligation_csv()


        asyncio.run(main())
        """
        _response = await self._raw_client.import_obligation_csv(
            file_input=file_input, enclosure=enclosure, delimiter=delimiter, request_options=request_options
        )
        return _response.data

    async def export_license_obligations(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Export a csv license obligation list

        Parameters
        ----------
        id : typing.Optional[int]
            Obligation id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successfully exported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.export_license_obligations()


        asyncio.run(main())
        """
        async with self._raw_client.export_license_obligations(id=id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def import_obligations_from_json(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Import an obligation json file

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Successfully imported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.import_obligations_from_json()


        asyncio.run(main())
        """
        _response = await self._raw_client.import_obligations_from_json(
            file_input=file_input, request_options=request_options
        )
        return _response.data

    async def export_obligations_to_json(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Export a json license obligation list

        Parameters
        ----------
        id : typing.Optional[int]
            Obligation id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successfully exported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.export_obligations_to_json()


        asyncio.run(main())
        """
        async with self._raw_client.export_obligations_to_json(id=id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_licenses(
        self,
        *,
        kind: typing.Optional[GetLicensesRequestKind] = None,
        group_name: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        active: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[GetLicensesResponseItem]:
        """
        Get a list of available licenses (filtered by kind or status)

        Parameters
        ----------
        kind : typing.Optional[GetLicensesRequestKind]
            Which kind of licenses to get.

        group_name : typing.Optional[str]
            The group name to chose

        page : typing.Optional[int]
            Page number to fetch

        limit : typing.Optional[int]
            Limits of responses per request

        active : typing.Optional[bool]
            Get only active licenses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[GetLicensesResponseItem]
            All licenses from database

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.get_licenses()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_licenses(
            kind=kind, group_name=group_name, page=page, limit=limit, active=active, request_options=request_options
        )
        return _response.data

    async def create_license(
        self,
        *,
        short_name: str,
        group_name: typing.Optional[str] = None,
        merge_request: typing.Optional[bool] = OMIT,
        full_name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        risk: typing.Optional[int] = OMIT,
        is_candidate: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Add a new license to the database

        Parameters
        ----------
        short_name : str
            Short name

        group_name : typing.Optional[str]
            The group name to chose

        merge_request : typing.Optional[bool]
            Open a merge request for candidate license?

        full_name : typing.Optional[str]
            Full name

        text : typing.Optional[str]
            License text

        url : typing.Optional[str]
            URL of the license text

        risk : typing.Optional[int]
            Risk level

        is_candidate : typing.Optional[bool]
            Is the license a candidate?

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License added successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.create_license(
                short_name="MIT",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_license(
            short_name=short_name,
            group_name=group_name,
            merge_request=merge_request,
            full_name=full_name,
            text=text,
            url=url,
            risk=risk,
            is_candidate=is_candidate,
            request_options=request_options,
        )
        return _response.data

    async def import_license(
        self,
        *,
        file_input: core.File,
        enclosure: typing.Optional[str] = OMIT,
        delimiter: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Import a csv license to the database

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        enclosure : typing.Optional[str]
            Enclosure for string in CSV

        delimiter : typing.Optional[str]
            Delimiters for fields in CSV

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Successfully imported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.import_license()


        asyncio.run(main())
        """
        _response = await self._raw_client.import_license(
            file_input=file_input, enclosure=enclosure, delimiter=delimiter, request_options=request_options
        )
        return _response.data

    async def export_license(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Export a csv license

        Parameters
        ----------
        id : typing.Optional[int]
            License id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successfully exported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.export_license()


        asyncio.run(main())
        """
        async with self._raw_client.export_license(id=id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def handle_import_license(
        self, *, file_input: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Import a json license to the database

        Parameters
        ----------
        file_input : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            Successfully imported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.handle_import_license()


        asyncio.run(main())
        """
        _response = await self._raw_client.handle_import_license(file_input=file_input, request_options=request_options)
        return _response.data

    async def export_admin_license_to_json(
        self, *, id: typing.Optional[int] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Export a json license

        Parameters
        ----------
        id : typing.Optional[int]
            License id to export, 0 for all

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            Successfully exported

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.export_admin_license_to_json()


        asyncio.run(main())
        """
        async with self._raw_client.export_admin_license_to_json(id=id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk

    async def get_license_by_shortname(
        self,
        shortname: str,
        *,
        group_name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetLicenseByShortnameResponse:
        """
        Get information about a specific license

        Parameters
        ----------
        shortname : str
            Shortname of the license

        group_name : typing.Optional[str]
            The group name to chose

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetLicenseByShortnameResponse
            License

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.get_license_by_shortname(
                shortname="shortname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_license_by_shortname(
            shortname, group_name=group_name, request_options=request_options
        )
        return _response.data

    async def update_license_by_shortname(
        self,
        shortname: str,
        *,
        group_name: typing.Optional[str] = None,
        full_name: typing.Optional[str] = OMIT,
        text: typing.Optional[str] = OMIT,
        url: typing.Optional[str] = OMIT,
        risk: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Update information about a given license

        Parameters
        ----------
        shortname : str
            Shortname of the license

        group_name : typing.Optional[str]
            The group name to chose

        full_name : typing.Optional[str]
            New fullname

        text : typing.Optional[str]
            New license text

        url : typing.Optional[str]
            New URL for license

        risk : typing.Optional[int]
            New risk value

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License added successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.update_license_by_shortname(
                shortname="shortname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_license_by_shortname(
            shortname,
            group_name=group_name,
            full_name=full_name,
            text=text,
            url=url,
            risk=risk,
            request_options=request_options,
        )
        return _response.data

    async def get_admin_license_candidates(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[LicenseCandidate]:
        """
        Get a list of license candidates from the database.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[LicenseCandidate]
            Request is successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.get_admin_license_candidates()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_license_candidates(request_options=request_options)
        return _response.data

    async def delete_by_license_candidate_id(
        self, id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Info:
        """
        Delete a single admin-license-candidate by the given id.

        Parameters
        ----------
        id : int
            Id of the license-candidate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License candidate will be deleted.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.delete_by_license_candidate_id(
                id=1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_by_license_candidate_id(id, request_options=request_options)
        return _response.data

    async def get_admin_license_acknowledgements(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[AdminLicenseAcknowledgement]:
        """
        Get a list of the admin license acknowledgements

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[AdminLicenseAcknowledgement]
            Request is successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.get_admin_license_acknowledgements()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_admin_license_acknowledgements(request_options=request_options)
        return _response.data

    async def mutate_admin_license_acknowledgement(
        self,
        *,
        request: typing.Sequence[MutateAdminAcknowledgement],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Info]:
        """
        Add, edit and toggle admin-license acknowledgement

        Parameters
        ----------
        request : typing.Sequence[MutateAdminAcknowledgement]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Request is successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MutateAdminAcknowledgement

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.mutate_admin_license_acknowledgement(
                request=[MutateAdminAcknowledgement()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mutate_admin_license_acknowledgement(
            request=request, request_options=request_options
        )
        return _response.data

    async def get_all_standard_license_comments(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[StandardComment]:
        """
        Get a list of all standard license comments.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[StandardComment]
            Request is successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.get_all_standard_license_comments()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_all_standard_license_comments(request_options=request_options)
        return _response.data

    async def mutate_std_comments(
        self, *, request: typing.Sequence[MutateStdComment], request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[Info]:
        """
        Add, edit and toggle standard comments

        Parameters
        ----------
        request : typing.Sequence[MutateStdComment]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Info]
            Request is successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, MutateStdComment

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.mutate_std_comments(
                request=[MutateStdComment()],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mutate_std_comments(request=request, request_options=request_options)
        return _response.data

    async def verify_license(
        self,
        shortname: str,
        *,
        parent_shortname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Verify a license as new or variant of another license

        Parameters
        ----------
        shortname : str
            Shortname of the license to be verified

        parent_shortname : typing.Optional[str]
            Shortname of the parent license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License verified successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.verify_license(
                shortname="shortname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.verify_license(
            shortname, parent_shortname=parent_shortname, request_options=request_options
        )
        return _response.data

    async def merge_license(
        self,
        shortname: str,
        *,
        parent_shortname: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Info:
        """
        Merge a license to another existing license

        Parameters
        ----------
        shortname : str
            Shortname of the license to be merged

        parent_shortname : typing.Optional[str]
            Shortname of the parent license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Info
            License merged successfully

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.merge_license(
                shortname="shortname",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.merge_license(
            shortname, parent_shortname=parent_shortname, request_options=request_options
        )
        return _response.data

    async def get_suggested_license(
        self, *, reference_text: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> GetSuggestedLicense:
        """
        Get a single suggested license by the given reference text.

        Parameters
        ----------
        reference_text : typing.Optional[str]
            Reference text to get suggested license

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetSuggestedLicense
            Request is successful

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.license.get_suggested_license()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_suggested_license(
            reference_text=reference_text, request_options=request_options
        )
        return _response.data
