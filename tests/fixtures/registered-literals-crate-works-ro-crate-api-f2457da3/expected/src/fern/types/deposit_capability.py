

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .deposit_capability_file_upload_item import DepositCapabilityFileUploadItem
from .deposit_capability_id_minting import DepositCapabilityIdMinting


class DepositCapability(UniversalBaseModel):
    """
    Declares whether the implementation provides the optional deposit surface, and on what terms. This block is REQUIRED in `/capabilities`: every implementation states its position explicitly, so a client never has to infer read-only-ness from a missing key.

    `supported` is the single flag clients check. When it is `true` the implementation provides the deposit and RO-Crate endpoints, and `idMinting` and `fileUpload` MUST also be present. When it is `false` the implementation is read-only, the deposit and RO-Crate endpoints are not provided, and the remaining fields MUST be omitted.

    Deletion behaviour is declared separately, in the top-level `tombstonePolicy`.
    """

    supported: bool = pydantic.Field()
    """
    Whether the implementation provides the deposit surface. `true` - deposits are accepted and the deposit and RO-Crate endpoints are available; `false` - the implementation is read-only.
    """

    id_minting: typing_extensions.Annotated[
        typing.Optional[DepositCapabilityIdMinting],
        FieldMetadata(alias="idMinting"),
        pydantic.Field(
            alias="idMinting",
            description="How RO-Crate IDs are minted at deposit creation. `client` - the client MUST propose an ID; `server` - the server always mints one; `both` - the client MAY propose an ID and the server mints one when absent.",
        ),
    ] = None
    """
    How RO-Crate IDs are minted at deposit creation. `client` - the client MUST propose an ID; `server` - the server always mints one; `both` - the client MAY propose an ID and the server mints one when absent.
    """

    file_upload: typing_extensions.Annotated[
        typing.Optional[typing.List[DepositCapabilityFileUploadItem]],
        FieldMetadata(alias="fileUpload"),
        pydantic.Field(
            alias="fileUpload",
            description="The file staging modes the implementation supports on `PUT /deposit/{id}/file/{fileId}`. `inline` - the file's bytes in the request body; `presigned` - transport metadata in the request, bytes uploaded directly to a returned target. New modes may be added by revision of this specification; clients MUST ignore values they do not recognise.",
        ),
    ] = None
    """
    The file staging modes the implementation supports on `PUT /deposit/{id}/file/{fileId}`. `inline` - the file's bytes in the request body; `presigned` - transport metadata in the request, bytes uploaded directly to a returned target. New modes may be added by revision of this specification; clients MUST ignore values they do not recognise.
    """

    deposit_ttl_seconds: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="depositTtlSeconds"),
        pydantic.Field(
            alias="depositTtlSeconds",
            description="How long an open deposit lives before expiring. When absent, expiry is implementation-defined and clients should not rely on any particular TTL.",
        ),
    ] = None
    """
    How long an open deposit lives before expiring. When absent, expiry is implementation-defined and clients should not rely on any particular TTL.
    """

    max_file_size_bytes: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="maxFileSizeBytes"),
        pydantic.Field(
            alias="maxFileSizeBytes",
            description="The largest file the implementation accepts in a deposit. When absent, no limit is declared.",
        ),
    ] = None
    """
    The largest file the implementation accepts in a deposit. When absent, no limit is declared.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
