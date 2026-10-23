

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.sub_project import SubProject
from .raw_client import AsyncRawSubprojectClient, RawSubprojectClient
from .types.sub_project_create_body_access_policy import SubProjectCreateBodyAccessPolicy
from .types.sub_project_create_body_acls import SubProjectCreateBodyAcls
from .types.sub_project_patch_body_acls import SubProjectPatchBodyAcls


OMIT = typing.cast(typing.Any, ...)


class SubprojectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawSubprojectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawSubprojectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawSubprojectClient
        """
        return self._raw_client

    def get(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        translate_user_info: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubProject:
        """
        <ul><li>Return the metadata for a requested sub-project.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubProject
            Retrieved subproject metadata successfully.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.subproject.get(
            tenantid="tenantid",
            subprojectid="subprojectid",
        )
        """
        _response = self._raw_client.get(
            tenantid, subprojectid, translate_user_info=translate_user_info, request_options=request_options
        )
        return _response.data

    def create(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        ltag: typing.Optional[str] = None,
        admin: typing.Optional[str] = OMIT,
        storage_class: typing.Optional[str] = OMIT,
        storage_location: typing.Optional[str] = OMIT,
        access_policy: typing.Optional[SubProjectCreateBodyAccessPolicy] = OMIT,
        acls: typing.Optional[SubProjectCreateBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubProject:
        """
        <ul>
        <li>Creates a new subproject resource in seismic store.</li>
        <li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            The tenant name - In OSDU this match the data-partition-id

        subprojectid : str
            The subproject name. It must match the regex <b>^[a-z][a-z\\d\\-]*[a-z\\d]$</b>

        ltag : typing.Optional[str]
            A valid compliance legal tag. It can be generated and managed via core-compliance-service.

        admin : typing.Optional[str]
            An optional user to set as admin. The user will be added in the first admins acl group

        storage_class : typing.Optional[str]
            Storage class for the bucket (Google Required Only)

        storage_location : typing.Optional[str]
            Storage location for the bucket (Google Required Only)

        access_policy : typing.Optional[SubProjectCreateBodyAccessPolicy]
            The datasets access level mode: "uniform" (uniform data access to all subprojects datasets) or "datasets" (acl can be applied at dataset level)

        acls : typing.Optional[SubProjectCreateBodyAcls]
            The entitlement groups to enable subproject access as admin or viewer. If not specified, default entitlement data groups will be created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubProject
            The registered subproject.

        Examples
        --------
        from fern.subproject import (
            SubProjectCreateBodyAccessPolicy,
            SubProjectCreateBodyAcls,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.subproject.create(
            tenantid="tenantid",
            subprojectid="subprojectid",
            admin="admin@email",
            storage_class="MULTI_REGIONAL",
            storage_location="US",
            access_policy=SubProjectCreateBodyAccessPolicy.UNIFORM,
            acls=SubProjectCreateBodyAcls(
                admins=[
                    "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.admin@slb.p4d.cloud.slb-ds.com"
                ],
                viewers=[
                    "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.viewer@slb.p4d.cloud.slb-ds.com"
                ],
            ),
        )
        """
        _response = self._raw_client.create(
            tenantid,
            subprojectid,
            ltag=ltag,
            admin=admin,
            storage_class=storage_class,
            storage_location=storage_location,
            access_policy=access_policy,
            acls=acls,
            request_options=request_options,
        )
        return _response.data

    def delete(
        self, tenantid: str, subprojectid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        <ul><li>Delete a subproject in seismic store.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.subproject.delete(
            tenantid="tenantid",
            subprojectid="subprojectid",
        )
        """
        _response = self._raw_client.delete(tenantid, subprojectid, request_options=request_options)
        return _response.data

    def patch(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        ltag: str,
        recursive: typing.Optional[bool] = None,
        access_policy: typing.Optional[str] = OMIT,
        acls: typing.Optional[SubProjectPatchBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubProject:
        """
        <ul>
          <li>Patch a subproject metadata in seismic store.</li>
          <li>Required roles: subproject.admin</li>
          <li>Possible actions:</li>
          <ul>
            <li>legal tag and/or ACLs groups can be patched by providing new values</li>
            <li>access policy can be changed from <i>uniform</i> to <i>dataset</i></li>
            <li><b>NOTE:</b> It is not possible to change subproject access policy from <i>dataset</i> to <i>uniform</i></li>
            <li><b>NOTE:</b> This operation is eventual consistent and it can take up to 5s before it gets completely applied</li>
          </ul>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        ltag : str
            Legal tag of the subproject.

        recursive : typing.Optional[bool]
            True if the legal tags of all datasets in a subproject needs to be updated.

        access_policy : typing.Optional[str]
            Access Policy for the subproject.

        acls : typing.Optional[SubProjectPatchBodyAcls]
            ACLs with admin groups and viewer groups. Existing acls will be replaced with the provided acls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubProject
            Updated subproject metadata successfully.

        Examples
        --------
        from fern.subproject import SubProjectPatchBodyAcls

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.subproject.patch(
            tenantid="tenantid",
            subprojectid="subprojectid",
            ltag="ltag",
            access_policy="dataset",
            acls=SubProjectPatchBodyAcls(
                admins=[
                    "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.admin@slb.p4d.cloud.slb-ds.com",
                    "data.sdms.tenant.subproject.1f1tr7fe-fb0e-402a-b725-606723e5356n.admin@slb.p4d.cloud.slb-ds.com",
                ],
                viewers=[
                    "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.viewer@slb.p4d.cloud.slb-ds.com"
                ],
            ),
        )
        """
        _response = self._raw_client.patch(
            tenantid,
            subprojectid,
            ltag=ltag,
            recursive=recursive,
            access_policy=access_policy,
            acls=acls,
            request_options=request_options,
        )
        return _response.data


class AsyncSubprojectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawSubprojectClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawSubprojectClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawSubprojectClient
        """
        return self._raw_client

    async def get(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        translate_user_info: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubProject:
        """
        <ul><li>Return the metadata for a requested sub-project.</li><li>Required roles: subproject.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        translate_user_info : typing.Optional[bool]
            translate the user-id to a more human readable user info

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubProject
            Retrieved subproject metadata successfully.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.subproject.get(
                tenantid="tenantid",
                subprojectid="subprojectid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get(
            tenantid, subprojectid, translate_user_info=translate_user_info, request_options=request_options
        )
        return _response.data

    async def create(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        ltag: typing.Optional[str] = None,
        admin: typing.Optional[str] = OMIT,
        storage_class: typing.Optional[str] = OMIT,
        storage_location: typing.Optional[str] = OMIT,
        access_policy: typing.Optional[SubProjectCreateBodyAccessPolicy] = OMIT,
        acls: typing.Optional[SubProjectCreateBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubProject:
        """
        <ul>
        <li>Creates a new subproject resource in seismic store.</li>
        <li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            The tenant name - In OSDU this match the data-partition-id

        subprojectid : str
            The subproject name. It must match the regex <b>^[a-z][a-z\\d\\-]*[a-z\\d]$</b>

        ltag : typing.Optional[str]
            A valid compliance legal tag. It can be generated and managed via core-compliance-service.

        admin : typing.Optional[str]
            An optional user to set as admin. The user will be added in the first admins acl group

        storage_class : typing.Optional[str]
            Storage class for the bucket (Google Required Only)

        storage_location : typing.Optional[str]
            Storage location for the bucket (Google Required Only)

        access_policy : typing.Optional[SubProjectCreateBodyAccessPolicy]
            The datasets access level mode: "uniform" (uniform data access to all subprojects datasets) or "datasets" (acl can be applied at dataset level)

        acls : typing.Optional[SubProjectCreateBodyAcls]
            The entitlement groups to enable subproject access as admin or viewer. If not specified, default entitlement data groups will be created.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubProject
            The registered subproject.

        Examples
        --------
        import asyncio

        from fern.subproject import (
            SubProjectCreateBodyAccessPolicy,
            SubProjectCreateBodyAcls,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.subproject.create(
                tenantid="tenantid",
                subprojectid="subprojectid",
                admin="admin@email",
                storage_class="MULTI_REGIONAL",
                storage_location="US",
                access_policy=SubProjectCreateBodyAccessPolicy.UNIFORM,
                acls=SubProjectCreateBodyAcls(
                    admins=[
                        "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.admin@slb.p4d.cloud.slb-ds.com"
                    ],
                    viewers=[
                        "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.viewer@slb.p4d.cloud.slb-ds.com"
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create(
            tenantid,
            subprojectid,
            ltag=ltag,
            admin=admin,
            storage_class=storage_class,
            storage_location=storage_location,
            access_policy=access_policy,
            acls=acls,
            request_options=request_options,
        )
        return _response.data

    async def delete(
        self, tenantid: str, subprojectid: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        <ul><li>Delete a subproject in seismic store.</li><li>Required roles: users.datalake.admin</li></ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

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
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.subproject.delete(
                tenantid="tenantid",
                subprojectid="subprojectid",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(tenantid, subprojectid, request_options=request_options)
        return _response.data

    async def patch(
        self,
        tenantid: str,
        subprojectid: str,
        *,
        ltag: str,
        recursive: typing.Optional[bool] = None,
        access_policy: typing.Optional[str] = OMIT,
        acls: typing.Optional[SubProjectPatchBodyAcls] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubProject:
        """
        <ul>
          <li>Patch a subproject metadata in seismic store.</li>
          <li>Required roles: subproject.admin</li>
          <li>Possible actions:</li>
          <ul>
            <li>legal tag and/or ACLs groups can be patched by providing new values</li>
            <li>access policy can be changed from <i>uniform</i> to <i>dataset</i></li>
            <li><b>NOTE:</b> It is not possible to change subproject access policy from <i>dataset</i> to <i>uniform</i></li>
            <li><b>NOTE:</b> This operation is eventual consistent and it can take up to 5s before it gets completely applied</li>
          </ul>
        </ul>

        Parameters
        ----------
        tenantid : str
            Name of the tenant.

        subprojectid : str
            Name of the subproject.

        ltag : str
            Legal tag of the subproject.

        recursive : typing.Optional[bool]
            True if the legal tags of all datasets in a subproject needs to be updated.

        access_policy : typing.Optional[str]
            Access Policy for the subproject.

        acls : typing.Optional[SubProjectPatchBodyAcls]
            ACLs with admin groups and viewer groups. Existing acls will be replaced with the provided acls.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubProject
            Updated subproject metadata successfully.

        Examples
        --------
        import asyncio

        from fern.subproject import SubProjectPatchBodyAcls

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.subproject.patch(
                tenantid="tenantid",
                subprojectid="subprojectid",
                ltag="ltag",
                access_policy="dataset",
                acls=SubProjectPatchBodyAcls(
                    admins=[
                        "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.admin@slb.p4d.cloud.slb-ds.com",
                        "data.sdms.tenant.subproject.1f1tr7fe-fb0e-402a-b725-606723e5356n.admin@slb.p4d.cloud.slb-ds.com",
                    ],
                    viewers=[
                        "data.sdms.tenant.subproject.1b1417e5-fb0e-402a-b725-606723e50b76.viewer@slb.p4d.cloud.slb-ds.com"
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.patch(
            tenantid,
            subprojectid,
            ltag=ltag,
            recursive=recursive,
            access_policy=access_policy,
            acls=acls,
            request_options=request_options,
        )
        return _response.data
