

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.organization import Organization
from ..types.organization_address import OrganizationAddress
from ..types.paginated_response_of_country import PaginatedResponseOfCountry
from ..types.paginated_response_of_partner_organization import PaginatedResponseOfPartnerOrganization
from ..types.public_image_presentation import PublicImagePresentation
from .raw_client import AsyncRawOrganizationsClient, RawOrganizationsClient


OMIT = typing.cast(typing.Any, ...)


class OrganizationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOrganizationsClient
        """
        return self._raw_client

    def list_countries(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfCountry:
        """
        Parameters
        ----------
        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfCountry
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.list_countries()
        """
        _response = self._raw_client.list_countries(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    def create_organization(
        self,
        *,
        name: str,
        namespace: str,
        id: typing.Optional[int] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Creating a new organization.

        Parameters
        ----------
        name : str
            The name of the organization

        namespace : str
            The namespace of the organization

        id : typing.Optional[int]
            The id of the organization ( Deprecated: Use namespace instead. )

        logo_url : typing.Optional[str]
            URL to a logo of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.create_organization(
            name="ACME Inc.",
            namespace="de.acme",
        )
        """
        _response = self._raw_client.create_organization(
            name=name, namespace=namespace, id=id, logo_url=logo_url, request_options=request_options
        )
        return _response.data

    def find_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Organization:
        """
        Returns a single organization.

        Parameters
        ----------
        organization_id : str
            The namespace of the organization to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.find_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.find_organization(organization_id, request_options=request_options)
        return _response.data

    def update_organization(
        self,
        organization_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization to be updated.

        name : typing.Optional[str]
            The name of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.update_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.update_organization(organization_id, name=name, request_options=request_options)
        return _response.data

    def delete_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization to be deleted.

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
        client.organizations.delete_organization(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.delete_organization(organization_id, request_options=request_options)
        return _response.data

    def find_organization_billing_address(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationAddress:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationAddress
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.find_organization_billing_address(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.find_organization_billing_address(organization_id, request_options=request_options)
        return _response.data

    def update_organization_billing_address(
        self,
        organization_id: str,
        *,
        city: str,
        country_code: str,
        firstname: str,
        lastname: str,
        post_code: str,
        street: str,
        company_name: typing.Optional[str] = OMIT,
        country_name: typing.Optional[str] = OMIT,
        telephone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationAddress:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        city : str

        country_code : str
            The ISO 3166 two-letter country code

        firstname : str

        lastname : str

        post_code : str

        street : str

        company_name : typing.Optional[str]

        country_name : typing.Optional[str]
            The country name

        telephone : typing.Optional[str]
            The telephone number e.g.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationAddress
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.update_organization_billing_address(
            organization_id="organizationId",
            city="MyCity",
            country_code="DE",
            firstname="Max",
            lastname="Muster",
            post_code="postCode",
            street="Examplestreet 1",
        )
        """
        _response = self._raw_client.update_organization_billing_address(
            organization_id,
            city=city,
            country_code=country_code,
            firstname=firstname,
            lastname=lastname,
            post_code=post_code,
            street=street,
            company_name=company_name,
            country_name=country_name,
            telephone=telephone,
            request_options=request_options,
        )
        return _response.data

    def delete_organization_billing_address(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

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
        client.organizations.delete_organization_billing_address(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.delete_organization_billing_address(
            organization_id, request_options=request_options
        )
        return _response.data

    def find_organization_address(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationAddress:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationAddress
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.find_organization_address(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.find_organization_address(organization_id, request_options=request_options)
        return _response.data

    def update_organization_address(
        self,
        organization_id: str,
        *,
        city: str,
        country_code: str,
        firstname: str,
        lastname: str,
        post_code: str,
        street: str,
        company_name: typing.Optional[str] = OMIT,
        country_name: typing.Optional[str] = OMIT,
        telephone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationAddress:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        city : str

        country_code : str
            The ISO 3166 two-letter country code

        firstname : str

        lastname : str

        post_code : str

        street : str

        company_name : typing.Optional[str]

        country_name : typing.Optional[str]
            The country name

        telephone : typing.Optional[str]
            The telephone number e.g.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationAddress
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.update_organization_address(
            organization_id="organizationId",
            city="MyCity",
            country_code="DE",
            firstname="Max",
            lastname="Muster",
            post_code="postCode",
            street="Examplestreet 1",
        )
        """
        _response = self._raw_client.update_organization_address(
            organization_id,
            city=city,
            country_code=country_code,
            firstname=firstname,
            lastname=lastname,
            post_code=post_code,
            street=street,
            company_name=company_name,
            country_name=country_name,
            telephone=telephone,
            request_options=request_options,
        )
        return _response.data

    def set_organization_logo(
        self, organization_id: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> PublicImagePresentation:
        """
        Updating an organization logo using a multipart file upload.

        Parameters
        ----------
        organization_id : str
            The namespace of the organization where the logo should be updated.

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicImagePresentation
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.set_organization_logo(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.set_organization_logo(organization_id, file=file, request_options=request_options)
        return _response.data

    def delete_organization_logo(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization where the logo should be deleted.

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
        client.organizations.delete_organization_logo(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.delete_organization_logo(organization_id, request_options=request_options)
        return _response.data

    def get_partner_organizations(
        self,
        organization_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfPartnerOrganization:
        """
        Listing partners in a paginated manner.

        Parameters
        ----------
        organization_id : str
            The namespace of the organization to query partner organizations

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfPartnerOrganization
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.get_partner_organizations(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_partner_organizations(
            organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    def add_partner_organization(
        self,
        organization_id_path_param: str,
        *,
        organization_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adding a partner organization. If the given organization is already a partner the result will be state 200 too.

        Parameters
        ----------
        organization_id_path_param : str
            The namespace of the organization

        organization_id : str
            The namespace of the partner organization to add

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
        client.organizations.add_partner_organization(
            organization_id_path_param="organizationId",
            organization_id="org.acme",
        )
        """
        _response = self._raw_client.add_partner_organization(
            organization_id_path_param, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def remove_partner_organization(
        self,
        organization_id_path_param: str,
        *,
        organization_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Removing a partner organization

        Parameters
        ----------
        organization_id_path_param : str
            The namespace of the organization

        organization_id : str
            The namespace of the partner organization to remove

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
        client.organizations.remove_partner_organization(
            organization_id_path_param="organizationId",
            organization_id="org.acme",
        )
        """
        _response = self._raw_client.remove_partner_organization(
            organization_id_path_param, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    def get_organization_privileges(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Listing all privileges of the current user/APIKey of the specified organization.

        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.organizations.get_organization_privileges(
            organization_id="organizationId",
        )
        """
        _response = self._raw_client.get_organization_privileges(organization_id, request_options=request_options)
        return _response.data


class AsyncOrganizationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOrganizationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOrganizationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOrganizationsClient
        """
        return self._raw_client

    async def list_countries(
        self,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfCountry:
        """
        Parameters
        ----------
        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfCountry
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.list_countries()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_countries(offset=offset, limit=limit, request_options=request_options)
        return _response.data

    async def create_organization(
        self,
        *,
        name: str,
        namespace: str,
        id: typing.Optional[int] = OMIT,
        logo_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Creating a new organization.

        Parameters
        ----------
        name : str
            The name of the organization

        namespace : str
            The namespace of the organization

        id : typing.Optional[int]
            The id of the organization ( Deprecated: Use namespace instead. )

        logo_url : typing.Optional[str]
            URL to a logo of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.create_organization(
                name="ACME Inc.",
                namespace="de.acme",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_organization(
            name=name, namespace=namespace, id=id, logo_url=logo_url, request_options=request_options
        )
        return _response.data

    async def find_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Organization:
        """
        Returns a single organization.

        Parameters
        ----------
        organization_id : str
            The namespace of the organization to be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.find_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_organization(organization_id, request_options=request_options)
        return _response.data

    async def update_organization(
        self,
        organization_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Organization:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization to be updated.

        name : typing.Optional[str]
            The name of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Organization
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.update_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_organization(
            organization_id, name=name, request_options=request_options
        )
        return _response.data

    async def delete_organization(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization to be deleted.

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
            await client.organizations.delete_organization(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_organization(organization_id, request_options=request_options)
        return _response.data

    async def find_organization_billing_address(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationAddress:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationAddress
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.find_organization_billing_address(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_organization_billing_address(
            organization_id, request_options=request_options
        )
        return _response.data

    async def update_organization_billing_address(
        self,
        organization_id: str,
        *,
        city: str,
        country_code: str,
        firstname: str,
        lastname: str,
        post_code: str,
        street: str,
        company_name: typing.Optional[str] = OMIT,
        country_name: typing.Optional[str] = OMIT,
        telephone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationAddress:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        city : str

        country_code : str
            The ISO 3166 two-letter country code

        firstname : str

        lastname : str

        post_code : str

        street : str

        company_name : typing.Optional[str]

        country_name : typing.Optional[str]
            The country name

        telephone : typing.Optional[str]
            The telephone number e.g.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationAddress
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.update_organization_billing_address(
                organization_id="organizationId",
                city="MyCity",
                country_code="DE",
                firstname="Max",
                lastname="Muster",
                post_code="postCode",
                street="Examplestreet 1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_organization_billing_address(
            organization_id,
            city=city,
            country_code=country_code,
            firstname=firstname,
            lastname=lastname,
            post_code=post_code,
            street=street,
            company_name=company_name,
            country_name=country_name,
            telephone=telephone,
            request_options=request_options,
        )
        return _response.data

    async def delete_organization_billing_address(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

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
            await client.organizations.delete_organization_billing_address(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_organization_billing_address(
            organization_id, request_options=request_options
        )
        return _response.data

    async def find_organization_address(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OrganizationAddress:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationAddress
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.find_organization_address(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.find_organization_address(organization_id, request_options=request_options)
        return _response.data

    async def update_organization_address(
        self,
        organization_id: str,
        *,
        city: str,
        country_code: str,
        firstname: str,
        lastname: str,
        post_code: str,
        street: str,
        company_name: typing.Optional[str] = OMIT,
        country_name: typing.Optional[str] = OMIT,
        telephone: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> OrganizationAddress:
        """
        Parameters
        ----------
        organization_id : str
            organizationId

        city : str

        country_code : str
            The ISO 3166 two-letter country code

        firstname : str

        lastname : str

        post_code : str

        street : str

        company_name : typing.Optional[str]

        country_name : typing.Optional[str]
            The country name

        telephone : typing.Optional[str]
            The telephone number e.g.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OrganizationAddress
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.update_organization_address(
                organization_id="organizationId",
                city="MyCity",
                country_code="DE",
                firstname="Max",
                lastname="Muster",
                post_code="postCode",
                street="Examplestreet 1",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_organization_address(
            organization_id,
            city=city,
            country_code=country_code,
            firstname=firstname,
            lastname=lastname,
            post_code=post_code,
            street=street,
            company_name=company_name,
            country_name=country_name,
            telephone=telephone,
            request_options=request_options,
        )
        return _response.data

    async def set_organization_logo(
        self, organization_id: str, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> PublicImagePresentation:
        """
        Updating an organization logo using a multipart file upload.

        Parameters
        ----------
        organization_id : str
            The namespace of the organization where the logo should be updated.

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PublicImagePresentation
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.set_organization_logo(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.set_organization_logo(
            organization_id, file=file, request_options=request_options
        )
        return _response.data

    async def delete_organization_logo(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Parameters
        ----------
        organization_id : str
            The namespace of the organization where the logo should be deleted.

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
            await client.organizations.delete_organization_logo(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_organization_logo(organization_id, request_options=request_options)
        return _response.data

    async def get_partner_organizations(
        self,
        organization_id: str,
        *,
        offset: typing.Optional[int] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PaginatedResponseOfPartnerOrganization:
        """
        Listing partners in a paginated manner.

        Parameters
        ----------
        organization_id : str
            The namespace of the organization to query partner organizations

        offset : typing.Optional[int]
            Start with the n-th element

        limit : typing.Optional[int]
            The maximum count of returned elements

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PaginatedResponseOfPartnerOrganization
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.get_partner_organizations(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_partner_organizations(
            organization_id, offset=offset, limit=limit, request_options=request_options
        )
        return _response.data

    async def add_partner_organization(
        self,
        organization_id_path_param: str,
        *,
        organization_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Adding a partner organization. If the given organization is already a partner the result will be state 200 too.

        Parameters
        ----------
        organization_id_path_param : str
            The namespace of the organization

        organization_id : str
            The namespace of the partner organization to add

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
            await client.organizations.add_partner_organization(
                organization_id_path_param="organizationId",
                organization_id="org.acme",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add_partner_organization(
            organization_id_path_param, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def remove_partner_organization(
        self,
        organization_id_path_param: str,
        *,
        organization_id: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Removing a partner organization

        Parameters
        ----------
        organization_id_path_param : str
            The namespace of the organization

        organization_id : str
            The namespace of the partner organization to remove

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
            await client.organizations.remove_partner_organization(
                organization_id_path_param="organizationId",
                organization_id="org.acme",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.remove_partner_organization(
            organization_id_path_param, organization_id=organization_id, request_options=request_options
        )
        return _response.data

    async def get_organization_privileges(
        self, organization_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.List[str]:
        """
        Listing all privileges of the current user/APIKey of the specified organization.

        Parameters
        ----------
        organization_id : str
            The namespace of the organization

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[str]
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.organizations.get_organization_privileges(
                organization_id="organizationId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_organization_privileges(organization_id, request_options=request_options)
        return _response.data
