

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_list import AccessList
from .address import Address
from .authorization_list import AuthorizationList
from .byte import Byte
from .bytes import Bytes
from .hash32 import Hash32
from .uint import Uint


class GenericTransaction(UniversalBaseModel):
    type: typing.Optional[Byte] = None
    nonce: typing.Optional[Uint] = None
    to: typing.Optional[Address] = None
    from_: typing_extensions.Annotated[
        typing.Optional[Address], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    gas: typing.Optional[Uint] = None
    value: typing.Optional[Uint] = None
    input: typing.Optional[Bytes] = None
    gas_price: typing_extensions.Annotated[
        typing.Optional[Uint],
        FieldMetadata(alias="gasPrice"),
        pydantic.Field(alias="gasPrice", description="The gas price willing to be paid by the sender in wei"),
    ] = None
    """
    The gas price willing to be paid by the sender in wei
    """

    max_priority_fee_per_gas: typing_extensions.Annotated[
        typing.Optional[Uint],
        FieldMetadata(alias="maxPriorityFeePerGas"),
        pydantic.Field(
            alias="maxPriorityFeePerGas",
            description="Maximum fee per gas the sender is willing to pay to miners in wei",
        ),
    ] = None
    """
    Maximum fee per gas the sender is willing to pay to miners in wei
    """

    max_fee_per_gas: typing_extensions.Annotated[
        typing.Optional[Uint],
        FieldMetadata(alias="maxFeePerGas"),
        pydantic.Field(
            alias="maxFeePerGas",
            description="The maximum total fee per gas the sender is willing to pay (includes the network / base fee and miner / priority fee) in wei",
        ),
    ] = None
    """
    The maximum total fee per gas the sender is willing to pay (includes the network / base fee and miner / priority fee) in wei
    """

    max_fee_per_blob_gas: typing_extensions.Annotated[
        typing.Optional[Uint],
        FieldMetadata(alias="maxFeePerBlobGas"),
        pydantic.Field(
            alias="maxFeePerBlobGas",
            description="The maximum total fee per gas the sender is willing to pay for blob gas in wei",
        ),
    ] = None
    """
    The maximum total fee per gas the sender is willing to pay for blob gas in wei
    """

    access_list: typing_extensions.Annotated[
        typing.Optional[AccessList],
        FieldMetadata(alias="accessList"),
        pydantic.Field(alias="accessList", description="EIP-2930 access list"),
    ] = None
    """
    EIP-2930 access list
    """

    blob_versioned_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[Hash32]],
        FieldMetadata(alias="blobVersionedHashes"),
        pydantic.Field(
            alias="blobVersionedHashes",
            description="List of versioned blob hashes associated with the transaction's EIP-4844 data blobs.",
        ),
    ] = None
    """
    List of versioned blob hashes associated with the transaction's EIP-4844 data blobs.
    """

    blobs: typing.Optional[typing.List[Bytes]] = pydantic.Field(default=None)
    """
    Raw blob data.
    """

    commitments: typing.Optional[typing.List[Bytes]] = pydantic.Field(default=None)
    """
    List of blob commitments as per EIP-4844.
    """

    proofs: typing.Optional[typing.List[Bytes]] = pydantic.Field(default=None)
    """
    List of blob proofs. Pre-PeerDAS this contains one KZG proof per blob (length == len(blobs)). Post-PeerDAS this contains cell proofs with length == 128 * len(blobs).
    """

    chain_id: typing_extensions.Annotated[
        typing.Optional[Uint],
        FieldMetadata(alias="chainId"),
        pydantic.Field(alias="chainId", description="Chain ID that this transaction is valid on."),
    ] = None
    """
    Chain ID that this transaction is valid on.
    """

    authorization_list: typing_extensions.Annotated[
        typing.Optional[AuthorizationList],
        FieldMetadata(alias="authorizationList"),
        pydantic.Field(alias="authorizationList", description="EIP-7702 authorization list"),
    ] = None
    """
    EIP-7702 authorization list
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
