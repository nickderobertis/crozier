

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WizardConfigTrustChainItem(UniversalBaseModel):
    role: typing.Optional[str] = None
    mint_schema_iri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mintSchemaIri"), pydantic.Field(alias="mintSchemaIri")
    ] = None
    view_only_own_documents: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="viewOnlyOwnDocuments"), pydantic.Field(alias="viewOnlyOwnDocuments")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
