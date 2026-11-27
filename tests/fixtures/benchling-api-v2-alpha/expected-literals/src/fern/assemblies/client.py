

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.assembly import Assembly
from ..types.assembly_spec_finalized_output_location import AssemblySpecFinalizedOutputLocation
from ..types.assembly_spec_shared_assembly_parameters import AssemblySpecSharedAssemblyParameters
from ..types.assembly_spec_shared_bins_item import AssemblySpecSharedBinsItem
from ..types.assembly_spec_shared_constructs_item import AssemblySpecSharedConstructsItem
from ..types.assembly_spec_shared_fragments_item import AssemblySpecSharedFragmentsItem
from ..types.assembly_spec_shared_topology import AssemblySpecSharedTopology
from ..types.async_task_link import AsyncTaskLink
from .raw_client import AsyncRawAssembliesClient, RawAssembliesClient


OMIT = typing.cast(typing.Any, ...)


class AssembliesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssembliesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssembliesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssembliesClient
        """
        return self._raw_client

    def get_assembly(
        self, bulk_assembly_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Assembly:
        """
        Get a bulk assembly by its API identifier.

        Parameters
        ----------
        bulk_assembly_id : str
            API identifier of bulk assembly

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assembly
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.assemblies.get_assembly(
            bulk_assembly_id="bulk_assembly_id",
        )
        """
        _response = self._raw_client.get_assembly(bulk_assembly_id, request_options=request_options)
        return _response.data

    def create_and_finalize_assembly(
        self,
        *,
        assembly_parameters: AssemblySpecSharedAssemblyParameters,
        bins: typing.Sequence[AssemblySpecSharedBinsItem],
        constructs: typing.Sequence[AssemblySpecSharedConstructsItem],
        fragments: typing.Sequence[AssemblySpecSharedFragmentsItem],
        topology: AssemblySpecSharedTopology,
        folder_id: str,
        name: str,
        output_location: AssemblySpecFinalizedOutputLocation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncTaskLink:
        """
        Create and finalize a new bulk assembly in a single step.

        Parameters
        ----------
        assembly_parameters : AssemblySpecSharedAssemblyParameters
            Assembly-wide parameters to describe requirements and procedures for the assembly.

        bins : typing.Sequence[AssemblySpecSharedBinsItem]
            Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.

        constructs : typing.Sequence[AssemblySpecSharedConstructsItem]
            Output constructs that should be created.

        fragments : typing.Sequence[AssemblySpecSharedFragmentsItem]
            Fragments to be used in the assembly.

        topology : AssemblySpecSharedTopology
            Whether the created constructs should be circular or linear.

        folder_id : str
            API identifier of the folder in which the assembly should be created.

        name : str
            Name of the bulk assembly.

        output_location : AssemblySpecFinalizedOutputLocation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncTaskLink
            This endpoint launches a [long-running task](#/Tasks/getTask) and returns the Task ID of the launched task.
            The task response contains a [finalized bulk assembly](#components/schemas/Assembly).

        Examples
        --------
        from fern import (
            AssemblyConcatenationMethodParameters,
            AssemblyPolymerReference_AaSequence,
            AssemblySpecFinalizedOutputLocation,
            AssemblySpecSharedAssemblyParameters_Concatenation,
            AssemblySpecSharedBinsItem_Constant,
            AssemblySpecSharedConstructsItem,
            AssemblySpecSharedFragmentsItem,
            FernApi,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.assemblies.create_and_finalize_assembly(
            folder_id="folderId",
            name="name",
            output_location=AssemblySpecFinalizedOutputLocation(
                construct_folder_id="constructFolderId",
            ),
            assembly_parameters=AssemblySpecSharedAssemblyParameters_Concatenation(
                parameters=AssemblyConcatenationMethodParameters(
                    fragment_production_method="SLICE",
                    polymer_type="DNA",
                ),
            ),
            bins=[
                AssemblySpecSharedBinsItem_Constant(
                    id="id",
                    name="name",
                    residues="residues",
                )
            ],
            constructs=[
                AssemblySpecSharedConstructsItem(
                    fragments=["fragments"],
                    id="id",
                )
            ],
            fragments=[
                AssemblySpecSharedFragmentsItem(
                    end=1.1,
                    id="id",
                    orientation="FORWARD",
                    polymer=AssemblyPolymerReference_AaSequence(
                        protein_id="proteinId",
                    ),
                    start=1.1,
                    bin_id="bin1",
                )
            ],
            topology="CIRCULAR",
        )
        """
        _response = self._raw_client.create_and_finalize_assembly(
            assembly_parameters=assembly_parameters,
            bins=bins,
            constructs=constructs,
            fragments=fragments,
            topology=topology,
            folder_id=folder_id,
            name=name,
            output_location=output_location,
            request_options=request_options,
        )
        return _response.data

    def validate_assembly(
        self,
        *,
        assembly_parameters: AssemblySpecSharedAssemblyParameters,
        bins: typing.Sequence[AssemblySpecSharedBinsItem],
        constructs: typing.Sequence[AssemblySpecSharedConstructsItem],
        fragments: typing.Sequence[AssemblySpecSharedFragmentsItem],
        topology: AssemblySpecSharedTopology,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncTaskLink:
        """
        Validate an assembly prior to finalization to see if it will succeed.

        Parameters
        ----------
        assembly_parameters : AssemblySpecSharedAssemblyParameters
            Assembly-wide parameters to describe requirements and procedures for the assembly.

        bins : typing.Sequence[AssemblySpecSharedBinsItem]
            Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.

        constructs : typing.Sequence[AssemblySpecSharedConstructsItem]
            Output constructs that should be created.

        fragments : typing.Sequence[AssemblySpecSharedFragmentsItem]
            Fragments to be used in the assembly.

        topology : AssemblySpecSharedTopology
            Whether the created constructs should be circular or linear.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncTaskLink
            This endpoint launched a [long-running task](#/Tasks/getTask) and returns the Task ID of the launched task.
            The task response contains a set of [validation results](#components/schemas/AssemblyValidationResult).

        Examples
        --------
        from fern import (
            AssemblyConcatenationMethodParameters,
            AssemblyPolymerReference_AaSequence,
            AssemblySpecSharedAssemblyParameters_Concatenation,
            AssemblySpecSharedBinsItem_Constant,
            AssemblySpecSharedConstructsItem,
            AssemblySpecSharedFragmentsItem,
            FernApi,
        )

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.assemblies.validate_assembly(
            assembly_parameters=AssemblySpecSharedAssemblyParameters_Concatenation(
                parameters=AssemblyConcatenationMethodParameters(
                    fragment_production_method="SLICE",
                    polymer_type="DNA",
                ),
            ),
            bins=[
                AssemblySpecSharedBinsItem_Constant(
                    id="id",
                    name="name",
                    residues="residues",
                )
            ],
            constructs=[
                AssemblySpecSharedConstructsItem(
                    fragments=["fragments"],
                    id="id",
                )
            ],
            fragments=[
                AssemblySpecSharedFragmentsItem(
                    end=1.1,
                    id="id",
                    orientation="FORWARD",
                    polymer=AssemblyPolymerReference_AaSequence(
                        protein_id="proteinId",
                    ),
                    start=1.1,
                    bin_id="bin1",
                )
            ],
            topology="CIRCULAR",
        )
        """
        _response = self._raw_client.validate_assembly(
            assembly_parameters=assembly_parameters,
            bins=bins,
            constructs=constructs,
            fragments=fragments,
            topology=topology,
            request_options=request_options,
        )
        return _response.data


class AsyncAssembliesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssembliesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssembliesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssembliesClient
        """
        return self._raw_client

    async def get_assembly(
        self, bulk_assembly_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Assembly:
        """
        Get a bulk assembly by its API identifier.

        Parameters
        ----------
        bulk_assembly_id : str
            API identifier of bulk assembly

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Assembly
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.assemblies.get_assembly(
                bulk_assembly_id="bulk_assembly_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_assembly(bulk_assembly_id, request_options=request_options)
        return _response.data

    async def create_and_finalize_assembly(
        self,
        *,
        assembly_parameters: AssemblySpecSharedAssemblyParameters,
        bins: typing.Sequence[AssemblySpecSharedBinsItem],
        constructs: typing.Sequence[AssemblySpecSharedConstructsItem],
        fragments: typing.Sequence[AssemblySpecSharedFragmentsItem],
        topology: AssemblySpecSharedTopology,
        folder_id: str,
        name: str,
        output_location: AssemblySpecFinalizedOutputLocation,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncTaskLink:
        """
        Create and finalize a new bulk assembly in a single step.

        Parameters
        ----------
        assembly_parameters : AssemblySpecSharedAssemblyParameters
            Assembly-wide parameters to describe requirements and procedures for the assembly.

        bins : typing.Sequence[AssemblySpecSharedBinsItem]
            Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.

        constructs : typing.Sequence[AssemblySpecSharedConstructsItem]
            Output constructs that should be created.

        fragments : typing.Sequence[AssemblySpecSharedFragmentsItem]
            Fragments to be used in the assembly.

        topology : AssemblySpecSharedTopology
            Whether the created constructs should be circular or linear.

        folder_id : str
            API identifier of the folder in which the assembly should be created.

        name : str
            Name of the bulk assembly.

        output_location : AssemblySpecFinalizedOutputLocation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncTaskLink
            This endpoint launches a [long-running task](#/Tasks/getTask) and returns the Task ID of the launched task.
            The task response contains a [finalized bulk assembly](#components/schemas/Assembly).

        Examples
        --------
        import asyncio

        from fern import (
            AssemblyConcatenationMethodParameters,
            AssemblyPolymerReference_AaSequence,
            AssemblySpecFinalizedOutputLocation,
            AssemblySpecSharedAssemblyParameters_Concatenation,
            AssemblySpecSharedBinsItem_Constant,
            AssemblySpecSharedConstructsItem,
            AssemblySpecSharedFragmentsItem,
            AsyncFernApi,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.assemblies.create_and_finalize_assembly(
                folder_id="folderId",
                name="name",
                output_location=AssemblySpecFinalizedOutputLocation(
                    construct_folder_id="constructFolderId",
                ),
                assembly_parameters=AssemblySpecSharedAssemblyParameters_Concatenation(
                    parameters=AssemblyConcatenationMethodParameters(
                        fragment_production_method="SLICE",
                        polymer_type="DNA",
                    ),
                ),
                bins=[
                    AssemblySpecSharedBinsItem_Constant(
                        id="id",
                        name="name",
                        residues="residues",
                    )
                ],
                constructs=[
                    AssemblySpecSharedConstructsItem(
                        fragments=["fragments"],
                        id="id",
                    )
                ],
                fragments=[
                    AssemblySpecSharedFragmentsItem(
                        end=1.1,
                        id="id",
                        orientation="FORWARD",
                        polymer=AssemblyPolymerReference_AaSequence(
                            protein_id="proteinId",
                        ),
                        start=1.1,
                        bin_id="bin1",
                    )
                ],
                topology="CIRCULAR",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_and_finalize_assembly(
            assembly_parameters=assembly_parameters,
            bins=bins,
            constructs=constructs,
            fragments=fragments,
            topology=topology,
            folder_id=folder_id,
            name=name,
            output_location=output_location,
            request_options=request_options,
        )
        return _response.data

    async def validate_assembly(
        self,
        *,
        assembly_parameters: AssemblySpecSharedAssemblyParameters,
        bins: typing.Sequence[AssemblySpecSharedBinsItem],
        constructs: typing.Sequence[AssemblySpecSharedConstructsItem],
        fragments: typing.Sequence[AssemblySpecSharedFragmentsItem],
        topology: AssemblySpecSharedTopology,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncTaskLink:
        """
        Validate an assembly prior to finalization to see if it will succeed.

        Parameters
        ----------
        assembly_parameters : AssemblySpecSharedAssemblyParameters
            Assembly-wide parameters to describe requirements and procedures for the assembly.

        bins : typing.Sequence[AssemblySpecSharedBinsItem]
            Bins are used to group fragments according to their position in the output construct or add a spacer (i.e. constant) region.

        constructs : typing.Sequence[AssemblySpecSharedConstructsItem]
            Output constructs that should be created.

        fragments : typing.Sequence[AssemblySpecSharedFragmentsItem]
            Fragments to be used in the assembly.

        topology : AssemblySpecSharedTopology
            Whether the created constructs should be circular or linear.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncTaskLink
            This endpoint launched a [long-running task](#/Tasks/getTask) and returns the Task ID of the launched task.
            The task response contains a set of [validation results](#components/schemas/AssemblyValidationResult).

        Examples
        --------
        import asyncio

        from fern import (
            AssemblyConcatenationMethodParameters,
            AssemblyPolymerReference_AaSequence,
            AssemblySpecSharedAssemblyParameters_Concatenation,
            AssemblySpecSharedBinsItem_Constant,
            AssemblySpecSharedConstructsItem,
            AssemblySpecSharedFragmentsItem,
            AsyncFernApi,
        )

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.assemblies.validate_assembly(
                assembly_parameters=AssemblySpecSharedAssemblyParameters_Concatenation(
                    parameters=AssemblyConcatenationMethodParameters(
                        fragment_production_method="SLICE",
                        polymer_type="DNA",
                    ),
                ),
                bins=[
                    AssemblySpecSharedBinsItem_Constant(
                        id="id",
                        name="name",
                        residues="residues",
                    )
                ],
                constructs=[
                    AssemblySpecSharedConstructsItem(
                        fragments=["fragments"],
                        id="id",
                    )
                ],
                fragments=[
                    AssemblySpecSharedFragmentsItem(
                        end=1.1,
                        id="id",
                        orientation="FORWARD",
                        polymer=AssemblyPolymerReference_AaSequence(
                            protein_id="proteinId",
                        ),
                        start=1.1,
                        bin_id="bin1",
                    )
                ],
                topology="CIRCULAR",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.validate_assembly(
            assembly_parameters=assembly_parameters,
            bins=bins,
            constructs=constructs,
            fragments=fragments,
            topology=topology,
            request_options=request_options,
        )
        return _response.data
