

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.image_import_content_response import ImageImportContentResponse
from ..types.image_import_operation import ImageImportOperation
from ..types.image_imports import ImageImports
from ..types.import_content_digest_list import ImportContentDigestList
from ..types.import_descriptor import ImportDescriptor
from ..types.import_distribution import ImportDistribution
from ..types.import_package import ImportPackage
from ..types.import_package_relationship import ImportPackageRelationship
from ..types.import_schema import ImportSchema
from ..types.import_source import ImportSource
from .raw_client import AsyncRawImportsClient, RawImportsClient


OMIT = typing.cast(typing.Any, ...)


class ImportsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawImportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawImportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawImportsClient
        """
        return self._raw_client

    def list_operations(self, *, request_options: typing.Optional[RequestOptions] = None) -> ImageImports:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImports
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.list_operations()
        """
        _response = self._raw_client.list_operations(request_options=request_options)
        return _response.data

    def create_operation(self, *, request_options: typing.Optional[RequestOptions] = None) -> ImageImportOperation:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportOperation
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.create_operation()
        """
        _response = self._raw_client.create_operation(request_options=request_options)
        return _response.data

    def get_operation(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImageImportOperation:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportOperation
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.get_operation(
            operation_id="operation_id",
        )
        """
        _response = self._raw_client.get_operation(operation_id, request_options=request_options)
        return _response.data

    def invalidate_operation(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImageImportOperation:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportOperation
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.invalidate_operation(
            operation_id="operation_id",
        )
        """
        _response = self._raw_client.invalidate_operation(operation_id, request_options=request_options)
        return _response.data

    def list_import_dockerfiles(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.list_import_dockerfiles(
            operation_id="operation_id",
        )
        """
        _response = self._raw_client.list_import_dockerfiles(operation_id, request_options=request_options)
        return _response.data

    def import_image_dockerfile(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.import_image_dockerfile(
            operation_id="operation_id",
        )
        """
        _response = self._raw_client.import_image_dockerfile(operation_id, request_options=request_options)
        return _response.data

    def list_import_image_configs(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.list_import_image_configs(
            operation_id="operation_id",
        )
        """
        _response = self._raw_client.list_import_image_configs(operation_id, request_options=request_options)
        return _response.data

    def import_image_config(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.import_image_config(
            operation_id="operation_id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.import_image_config(operation_id, request=request, request_options=request_options)
        return _response.data

    def list_import_image_manifests(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.list_import_image_manifests(
            operation_id="operation_id",
        )
        """
        _response = self._raw_client.list_import_image_manifests(operation_id, request_options=request_options)
        return _response.data

    def import_image_manifest(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.import_image_manifest(
            operation_id="operation_id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.import_image_manifest(
            operation_id, request=request, request_options=request_options
        )
        return _response.data

    def list_import_packages(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.list_import_packages(
            operation_id="operation_id",
        )
        """
        _response = self._raw_client.list_import_packages(operation_id, request_options=request_options)
        return _response.data

    def import_image_packages(
        self,
        operation_id: str,
        *,
        artifacts: typing.Sequence[ImportPackage],
        distro: ImportDistribution,
        source: ImportSource,
        artifact_relationships: typing.Optional[typing.Sequence[ImportPackageRelationship]] = OMIT,
        descriptor: typing.Optional[ImportDescriptor] = OMIT,
        schema: typing.Optional[ImportSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        artifacts : typing.Sequence[ImportPackage]

        distro : ImportDistribution

        source : ImportSource

        artifact_relationships : typing.Optional[typing.Sequence[ImportPackageRelationship]]

        descriptor : typing.Optional[ImportDescriptor]

        schema : typing.Optional[ImportSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        from fern import (
            FernApi,
            ImportDistribution,
            ImportPackage,
            ImportPackageLocation,
            ImportSource,
        )

        client = FernApi()
        client.imports.import_image_packages(
            operation_id="operation_id",
            artifacts=[
                ImportPackage(
                    cpes=["cpes"],
                    language="language",
                    licenses=["licenses"],
                    locations=[
                        ImportPackageLocation(
                            path="path",
                        )
                    ],
                    metadata_type="metadataType",
                    name="name",
                    type="type",
                    version="version",
                )
            ],
            distro=ImportDistribution(
                id_like="idLike",
                name="name",
                version="version",
            ),
            source=ImportSource(
                target={"key": "value"},
                type="type",
            ),
        )
        """
        _response = self._raw_client.import_image_packages(
            operation_id,
            artifacts=artifacts,
            distro=distro,
            source=source,
            artifact_relationships=artifact_relationships,
            descriptor=descriptor,
            schema=schema,
            request_options=request_options,
        )
        return _response.data

    def list_import_parent_manifests(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.list_import_parent_manifests(
            operation_id="operation_id",
        )
        """
        _response = self._raw_client.list_import_parent_manifests(operation_id, request_options=request_options)
        return _response.data

    def import_image_parent_manifest(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.imports.import_image_parent_manifest(
            operation_id="operation_id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.import_image_parent_manifest(
            operation_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncImportsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawImportsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawImportsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawImportsClient
        """
        return self._raw_client

    async def list_operations(self, *, request_options: typing.Optional[RequestOptions] = None) -> ImageImports:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImports
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.list_operations()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_operations(request_options=request_options)
        return _response.data

    async def create_operation(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImageImportOperation:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportOperation
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.create_operation()


        asyncio.run(main())
        """
        _response = await self._raw_client.create_operation(request_options=request_options)
        return _response.data

    async def get_operation(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImageImportOperation:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportOperation
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.get_operation(
                operation_id="operation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_operation(operation_id, request_options=request_options)
        return _response.data

    async def invalidate_operation(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImageImportOperation:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportOperation
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.invalidate_operation(
                operation_id="operation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.invalidate_operation(operation_id, request_options=request_options)
        return _response.data

    async def list_import_dockerfiles(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.list_import_dockerfiles(
                operation_id="operation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_import_dockerfiles(operation_id, request_options=request_options)
        return _response.data

    async def import_image_dockerfile(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.import_image_dockerfile(
                operation_id="operation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_image_dockerfile(operation_id, request_options=request_options)
        return _response.data

    async def list_import_image_configs(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.list_import_image_configs(
                operation_id="operation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_import_image_configs(operation_id, request_options=request_options)
        return _response.data

    async def import_image_config(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.import_image_config(
                operation_id="operation_id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_image_config(
            operation_id, request=request, request_options=request_options
        )
        return _response.data

    async def list_import_image_manifests(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.list_import_image_manifests(
                operation_id="operation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_import_image_manifests(operation_id, request_options=request_options)
        return _response.data

    async def import_image_manifest(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.import_image_manifest(
                operation_id="operation_id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_image_manifest(
            operation_id, request=request, request_options=request_options
        )
        return _response.data

    async def list_import_packages(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.list_import_packages(
                operation_id="operation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_import_packages(operation_id, request_options=request_options)
        return _response.data

    async def import_image_packages(
        self,
        operation_id: str,
        *,
        artifacts: typing.Sequence[ImportPackage],
        distro: ImportDistribution,
        source: ImportSource,
        artifact_relationships: typing.Optional[typing.Sequence[ImportPackageRelationship]] = OMIT,
        descriptor: typing.Optional[ImportDescriptor] = OMIT,
        schema: typing.Optional[ImportSchema] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        artifacts : typing.Sequence[ImportPackage]

        distro : ImportDistribution

        source : ImportSource

        artifact_relationships : typing.Optional[typing.Sequence[ImportPackageRelationship]]

        descriptor : typing.Optional[ImportDescriptor]

        schema : typing.Optional[ImportSchema]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        import asyncio

        from fern import (
            AsyncFernApi,
            ImportDistribution,
            ImportPackage,
            ImportPackageLocation,
            ImportSource,
        )

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.import_image_packages(
                operation_id="operation_id",
                artifacts=[
                    ImportPackage(
                        cpes=["cpes"],
                        language="language",
                        licenses=["licenses"],
                        locations=[
                            ImportPackageLocation(
                                path="path",
                            )
                        ],
                        metadata_type="metadataType",
                        name="name",
                        type="type",
                        version="version",
                    )
                ],
                distro=ImportDistribution(
                    id_like="idLike",
                    name="name",
                    version="version",
                ),
                source=ImportSource(
                    target={"key": "value"},
                    type="type",
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_image_packages(
            operation_id,
            artifacts=artifacts,
            distro=distro,
            source=source,
            artifact_relationships=artifact_relationships,
            descriptor=descriptor,
            schema=schema,
            request_options=request_options,
        )
        return _response.data

    async def list_import_parent_manifests(
        self, operation_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ImportContentDigestList:
        """
        Parameters
        ----------
        operation_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImportContentDigestList
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.list_import_parent_manifests(
                operation_id="operation_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.list_import_parent_manifests(operation_id, request_options=request_options)
        return _response.data

    async def import_image_parent_manifest(
        self,
        operation_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ImageImportContentResponse:
        """
        Parameters
        ----------
        operation_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ImageImportContentResponse
            success

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.imports.import_image_parent_manifest(
                operation_id="operation_id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.import_image_parent_manifest(
            operation_id, request=request, request_options=request_options
        )
        return _response.data
