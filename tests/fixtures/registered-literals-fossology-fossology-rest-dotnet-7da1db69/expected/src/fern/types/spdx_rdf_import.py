

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .spdx_rdf_import_add_new_licenses_as import SpdxRdfImportAddNewLicensesAs


class SpdxRdfImport(UniversalBaseModel):
    """
    Information required by SPDX RDF report import agent.
    """

    add_new_licenses_as: typing_extensions.Annotated[
        typing.Optional[SpdxRdfImportAddNewLicensesAs],
        FieldMetadata(alias="addNewLicensesAs"),
        pydantic.Field(alias="addNewLicensesAs", description="Create new licenses as"),
    ] = None
    """
    Create new licenses as
    """

    add_license_info_from_info_in_file: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="addLicenseInfoFromInfoInFile"),
        pydantic.Field(
            alias="addLicenseInfoFromInfoInFile",
            description="Add the License Info as findings from SPDX tag of type licenseInfoInFile",
        ),
    ] = None
    """
    Add the License Info as findings from SPDX tag of type licenseInfoInFile
    """

    add_license_info_from_concluded: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="addLicenseInfoFromConcluded"),
        pydantic.Field(
            alias="addLicenseInfoFromConcluded",
            description="Add the License Info as findings from SPDX tag of type licenseConcluded",
        ),
    ] = None
    """
    Add the License Info as findings from SPDX tag of type licenseConcluded
    """

    add_concluded_as_decisions: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="addConcludedAsDecisions"),
        pydantic.Field(alias="addConcludedAsDecisions", description="Add concluded licenses as decisions"),
    ] = None
    """
    Add concluded licenses as decisions
    """

    add_concluded_as_decisions_tbd: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="addConcludedAsDecisionsTBD"),
        pydantic.Field(
            alias="addConcludedAsDecisionsTBD", description='Add concluded licenses imported as "to be discussed"'
        ),
    ] = None
    """
    Add concluded licenses imported as "to be discussed"
    """

    add_copyrights: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="addCopyrights"),
        pydantic.Field(alias="addCopyrights", description="Add the copyright information as text findings"),
    ] = None
    """
    Add the copyright information as text findings
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
