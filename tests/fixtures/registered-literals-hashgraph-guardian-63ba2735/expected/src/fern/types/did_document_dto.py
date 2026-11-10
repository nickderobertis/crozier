

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DidDocumentDto(UniversalBaseModel):
    id: str
    context: typing.Optional[typing.List[str]] = None
    also_known_as: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="alsoKnownAs"), pydantic.Field(alias="alsoKnownAs")
    ] = None
    controller: typing.Optional[typing.List[str]] = None
    verification_method: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="verificationMethod"),
        pydantic.Field(alias="verificationMethod"),
    ] = None
    authentication: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    assertion_method: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="assertionMethod"),
        pydantic.Field(alias="assertionMethod"),
    ] = None
    key_agreement: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="keyAgreement"),
        pydantic.Field(alias="keyAgreement"),
    ] = None
    capability_invocation: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="capabilityInvocation"),
        pydantic.Field(alias="capabilityInvocation"),
    ] = None
    capability_delegation: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Any]]],
        FieldMetadata(alias="capabilityDelegation"),
        pydantic.Field(alias="capabilityDelegation"),
    ] = None
    service: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
