

import datetime as dt
import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.counter import Counter
from ..types.import_job import ImportJob
from ..types.metadata import Metadata
from ..types.secret_ref import SecretRef
from ..types.service_ref import ServiceRef
from .raw_client import AsyncRawJobClient, RawJobClient


OMIT = typing.cast(typing.Any, ...)


class JobClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawJobClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawJobClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawJobClient
        """
        return self._raw_client

    def upload_artifact(
        self, *, main_artifact: bool, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Uploads an artifact to be imported by Microcks.

        Parameters
        ----------
        main_artifact : bool
            Flag telling if this should be considered as primary or secondary artifact. Default to 'true'

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Artifact was imported and Service found
        """
        _response = self._raw_client.upload_artifact(
            main_artifact=main_artifact, file=file, request_options=request_options
        )
        return _response.data

    def get_import_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ImportJob]:
        """
        Retrieve a list of ImportJobs

        Parameters
        ----------
        page : typing.Optional[int]
            Page of ImportJobs to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20)

        name : typing.Optional[str]
            Name like criterion for query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ImportJob]
            List of found ImportJobs

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_import_jobs()
        """
        _response = self._raw_client.get_import_jobs(page=page, size=size, name=name, request_options=request_options)
        return _response.data

    def create_import_job(
        self,
        *,
        name: str,
        repository_url: str,
        active: typing.Optional[bool] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        etag: typing.Optional[str] = OMIT,
        frequency: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_import_date: typing.Optional[dt.datetime] = OMIT,
        last_import_error: typing.Optional[str] = OMIT,
        main_artifact: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        repository_disable_ssl_validation: typing.Optional[bool] = OMIT,
        secret_ref: typing.Optional[SecretRef] = OMIT,
        service_refs: typing.Optional[typing.Sequence[ServiceRef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportJob:
        """
        Create a new ImportJob

        Parameters
        ----------
        name : str
            Unique distinct name of this ImportJob

        repository_url : str
            URL of mocks and tests repository artifact

        active : typing.Optional[bool]
            Whether this ImportJob is active (ie. scheduled for execution)

        created_date : typing.Optional[dt.datetime]
            Creation date for this ImportJob

        etag : typing.Optional[str]
            Etag of repository URL during previous import. Is used for not re-importing if no recent changes

        frequency : typing.Optional[str]
            Reserved for future usage

        id : typing.Optional[str]
            Unique identifier of ImportJob

        last_import_date : typing.Optional[dt.datetime]
            Date last import was done

        last_import_error : typing.Optional[str]
            Error message of last import (if any)

        main_artifact : typing.Optional[bool]
            Flag telling if considered as primary or secondary artifact. Default to `true`

        metadata : typing.Optional[Metadata]
            Metadata of ImportJob

        repository_disable_ssl_validation : typing.Optional[bool]
            Whether to disable SSL certificate verification when checking repository

        secret_ref : typing.Optional[SecretRef]
            Reference of a Secret to used when checking repository

        service_refs : typing.Optional[typing.Sequence[ServiceRef]]
            References of Services discovered when checking repository

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Created ImportJob

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.create_import_job(
            name="name",
            repository_url="repositoryUrl",
        )
        """
        _response = self._raw_client.create_import_job(
            name=name,
            repository_url=repository_url,
            active=active,
            created_date=created_date,
            etag=etag,
            frequency=frequency,
            id=id,
            last_import_date=last_import_date,
            last_import_error=last_import_error,
            main_artifact=main_artifact,
            metadata=metadata,
            repository_disable_ssl_validation=repository_disable_ssl_validation,
            secret_ref=secret_ref,
            service_refs=service_refs,
            request_options=request_options,
        )
        return _response.data

    def get_import_job_counter(self, *, request_options: typing.Optional[RequestOptions] = None) -> Counter:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Counter
            Number of ImportJobs in datastore

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_import_job_counter()
        """
        _response = self._raw_client.get_import_job_counter(request_options=request_options)
        return _response.data

    def get_import_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ImportJob:
        """
        Retrieve an ImportJob using its identifier

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Found ImportJob

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.get_import_job(
            id="id",
        )
        """
        _response = self._raw_client.get_import_job(id, request_options=request_options)
        return _response.data

    def update_import_job(
        self,
        id_: str,
        *,
        name: str,
        repository_url: str,
        active: typing.Optional[bool] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        etag: typing.Optional[str] = OMIT,
        frequency: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_import_date: typing.Optional[dt.datetime] = OMIT,
        last_import_error: typing.Optional[str] = OMIT,
        main_artifact: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        repository_disable_ssl_validation: typing.Optional[bool] = OMIT,
        secret_ref: typing.Optional[SecretRef] = OMIT,
        service_refs: typing.Optional[typing.Sequence[ServiceRef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportJob:
        """
        Update an ImportJob

        Parameters
        ----------
        id_ : str
            Unique identifier of ImportJob to manage

        name : str
            Unique distinct name of this ImportJob

        repository_url : str
            URL of mocks and tests repository artifact

        active : typing.Optional[bool]
            Whether this ImportJob is active (ie. scheduled for execution)

        created_date : typing.Optional[dt.datetime]
            Creation date for this ImportJob

        etag : typing.Optional[str]
            Etag of repository URL during previous import. Is used for not re-importing if no recent changes

        frequency : typing.Optional[str]
            Reserved for future usage

        id : typing.Optional[str]
            Unique identifier of ImportJob

        last_import_date : typing.Optional[dt.datetime]
            Date last import was done

        last_import_error : typing.Optional[str]
            Error message of last import (if any)

        main_artifact : typing.Optional[bool]
            Flag telling if considered as primary or secondary artifact. Default to `true`

        metadata : typing.Optional[Metadata]
            Metadata of ImportJob

        repository_disable_ssl_validation : typing.Optional[bool]
            Whether to disable SSL certificate verification when checking repository

        secret_ref : typing.Optional[SecretRef]
            Reference of a Secret to used when checking repository

        service_refs : typing.Optional[typing.Sequence[ServiceRef]]
            References of Services discovered when checking repository

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Updated ImportJob

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.update_import_job(
            id_="id",
            name="name",
            repository_url="repositoryUrl",
        )
        """
        _response = self._raw_client.update_import_job(
            id_,
            name=name,
            repository_url=repository_url,
            active=active,
            created_date=created_date,
            etag=etag,
            frequency=frequency,
            id=id,
            last_import_date=last_import_date,
            last_import_error=last_import_error,
            main_artifact=main_artifact,
            metadata=metadata,
            repository_disable_ssl_validation=repository_disable_ssl_validation,
            secret_ref=secret_ref,
            service_refs=service_refs,
            request_options=request_options,
        )
        return _response.data

    def delete_import_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Delete an ImportJob

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            ImportJob deleted

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.delete_import_job(
            id="id",
        )
        """
        _response = self._raw_client.delete_import_job(id, request_options=request_options)
        return _response.data

    def activate_import_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ImportJob:
        """
        Make an ImportJob active, so that it is executed

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            ImportJob is activated

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.activate_import_job(
            id="id",
        )
        """
        _response = self._raw_client.activate_import_job(id, request_options=request_options)
        return _response.data

    def start_import_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ImportJob:
        """
        Starting an ImportJob forces it to immediatly import mock definitions

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Started ImportJob

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.start_import_job(
            id="id",
        )
        """
        _response = self._raw_client.start_import_job(id, request_options=request_options)
        return _response.data

    def stop_import_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ImportJob:
        """
        Stopping an ImportJob desactivate it, so that it won't execute at next schedule

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Stopped ImportJob

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.job.stop_import_job(
            id="id",
        )
        """
        _response = self._raw_client.stop_import_job(id, request_options=request_options)
        return _response.data


class AsyncJobClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawJobClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawJobClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawJobClient
        """
        return self._raw_client

    async def upload_artifact(
        self, *, main_artifact: bool, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> str:
        """
        Uploads an artifact to be imported by Microcks.

        Parameters
        ----------
        main_artifact : bool
            Flag telling if this should be considered as primary or secondary artifact. Default to 'true'

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Artifact was imported and Service found
        """
        _response = await self._raw_client.upload_artifact(
            main_artifact=main_artifact, file=file, request_options=request_options
        )
        return _response.data

    async def get_import_jobs(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        name: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[ImportJob]:
        """
        Retrieve a list of ImportJobs

        Parameters
        ----------
        page : typing.Optional[int]
            Page of ImportJobs to retrieve (starts at and defaults to 0)

        size : typing.Optional[int]
            Size of a page. Maximum number of ImportJobs to include in a response (defaults to 20)

        name : typing.Optional[str]
            Name like criterion for query

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[ImportJob]
            List of found ImportJobs

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_import_jobs()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_import_jobs(
            page=page, size=size, name=name, request_options=request_options
        )
        return _response.data

    async def create_import_job(
        self,
        *,
        name: str,
        repository_url: str,
        active: typing.Optional[bool] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        etag: typing.Optional[str] = OMIT,
        frequency: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_import_date: typing.Optional[dt.datetime] = OMIT,
        last_import_error: typing.Optional[str] = OMIT,
        main_artifact: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        repository_disable_ssl_validation: typing.Optional[bool] = OMIT,
        secret_ref: typing.Optional[SecretRef] = OMIT,
        service_refs: typing.Optional[typing.Sequence[ServiceRef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportJob:
        """
        Create a new ImportJob

        Parameters
        ----------
        name : str
            Unique distinct name of this ImportJob

        repository_url : str
            URL of mocks and tests repository artifact

        active : typing.Optional[bool]
            Whether this ImportJob is active (ie. scheduled for execution)

        created_date : typing.Optional[dt.datetime]
            Creation date for this ImportJob

        etag : typing.Optional[str]
            Etag of repository URL during previous import. Is used for not re-importing if no recent changes

        frequency : typing.Optional[str]
            Reserved for future usage

        id : typing.Optional[str]
            Unique identifier of ImportJob

        last_import_date : typing.Optional[dt.datetime]
            Date last import was done

        last_import_error : typing.Optional[str]
            Error message of last import (if any)

        main_artifact : typing.Optional[bool]
            Flag telling if considered as primary or secondary artifact. Default to `true`

        metadata : typing.Optional[Metadata]
            Metadata of ImportJob

        repository_disable_ssl_validation : typing.Optional[bool]
            Whether to disable SSL certificate verification when checking repository

        secret_ref : typing.Optional[SecretRef]
            Reference of a Secret to used when checking repository

        service_refs : typing.Optional[typing.Sequence[ServiceRef]]
            References of Services discovered when checking repository

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Created ImportJob

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.create_import_job(
                name="name",
                repository_url="repositoryUrl",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_import_job(
            name=name,
            repository_url=repository_url,
            active=active,
            created_date=created_date,
            etag=etag,
            frequency=frequency,
            id=id,
            last_import_date=last_import_date,
            last_import_error=last_import_error,
            main_artifact=main_artifact,
            metadata=metadata,
            repository_disable_ssl_validation=repository_disable_ssl_validation,
            secret_ref=secret_ref,
            service_refs=service_refs,
            request_options=request_options,
        )
        return _response.data

    async def get_import_job_counter(self, *, request_options: typing.Optional[RequestOptions] = None) -> Counter:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Counter
            Number of ImportJobs in datastore

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_import_job_counter()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_import_job_counter(request_options=request_options)
        return _response.data

    async def get_import_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ImportJob:
        """
        Retrieve an ImportJob using its identifier

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Found ImportJob

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.get_import_job(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_import_job(id, request_options=request_options)
        return _response.data

    async def update_import_job(
        self,
        id_: str,
        *,
        name: str,
        repository_url: str,
        active: typing.Optional[bool] = OMIT,
        created_date: typing.Optional[dt.datetime] = OMIT,
        etag: typing.Optional[str] = OMIT,
        frequency: typing.Optional[str] = OMIT,
        id: typing.Optional[str] = OMIT,
        last_import_date: typing.Optional[dt.datetime] = OMIT,
        last_import_error: typing.Optional[str] = OMIT,
        main_artifact: typing.Optional[bool] = OMIT,
        metadata: typing.Optional[Metadata] = OMIT,
        repository_disable_ssl_validation: typing.Optional[bool] = OMIT,
        secret_ref: typing.Optional[SecretRef] = OMIT,
        service_refs: typing.Optional[typing.Sequence[ServiceRef]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImportJob:
        """
        Update an ImportJob

        Parameters
        ----------
        id_ : str
            Unique identifier of ImportJob to manage

        name : str
            Unique distinct name of this ImportJob

        repository_url : str
            URL of mocks and tests repository artifact

        active : typing.Optional[bool]
            Whether this ImportJob is active (ie. scheduled for execution)

        created_date : typing.Optional[dt.datetime]
            Creation date for this ImportJob

        etag : typing.Optional[str]
            Etag of repository URL during previous import. Is used for not re-importing if no recent changes

        frequency : typing.Optional[str]
            Reserved for future usage

        id : typing.Optional[str]
            Unique identifier of ImportJob

        last_import_date : typing.Optional[dt.datetime]
            Date last import was done

        last_import_error : typing.Optional[str]
            Error message of last import (if any)

        main_artifact : typing.Optional[bool]
            Flag telling if considered as primary or secondary artifact. Default to `true`

        metadata : typing.Optional[Metadata]
            Metadata of ImportJob

        repository_disable_ssl_validation : typing.Optional[bool]
            Whether to disable SSL certificate verification when checking repository

        secret_ref : typing.Optional[SecretRef]
            Reference of a Secret to used when checking repository

        service_refs : typing.Optional[typing.Sequence[ServiceRef]]
            References of Services discovered when checking repository

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Updated ImportJob

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.update_import_job(
                id_="id",
                name="name",
                repository_url="repositoryUrl",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.update_import_job(
            id_,
            name=name,
            repository_url=repository_url,
            active=active,
            created_date=created_date,
            etag=etag,
            frequency=frequency,
            id=id,
            last_import_date=last_import_date,
            last_import_error=last_import_error,
            main_artifact=main_artifact,
            metadata=metadata,
            repository_disable_ssl_validation=repository_disable_ssl_validation,
            secret_ref=secret_ref,
            service_refs=service_refs,
            request_options=request_options,
        )
        return _response.data

    async def delete_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete an ImportJob

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            ImportJob deleted

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.delete_import_job(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_import_job(id, request_options=request_options)
        return _response.data

    async def activate_import_job(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportJob:
        """
        Make an ImportJob active, so that it is executed

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            ImportJob is activated

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.activate_import_job(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.activate_import_job(id, request_options=request_options)
        return _response.data

    async def start_import_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ImportJob:
        """
        Starting an ImportJob forces it to immediatly import mock definitions

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Started ImportJob

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.start_import_job(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.start_import_job(id, request_options=request_options)
        return _response.data

    async def stop_import_job(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ImportJob:
        """
        Stopping an ImportJob desactivate it, so that it won't execute at next schedule

        Parameters
        ----------
        id : str
            Unique identifier of ImportJob to manage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportJob
            Stopped ImportJob

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.job.stop_import_job(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.stop_import_job(id, request_options=request_options)
        return _response.data
