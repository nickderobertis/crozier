

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capabilities_extensions import CapabilitiesExtensions
from .capabilities_tombstone_policy import CapabilitiesTombstonePolicy
from .deposit_capability import DepositCapability
from .search_capability import SearchCapability


class Capabilities(UniversalBaseModel):
    """
    Declares what an implementation supports — the spec version it targets, whether it provides the optional deposit surface, the registered extensions it implements, and the search filters and facets it provides.
    """

    api_version: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="apiVersion"),
        pydantic.Field(
            alias="apiVersion", description="The version of this specification that the implementation targets."
        ),
    ]
    """
    The version of this specification that the implementation targets.
    """

    extensions: CapabilitiesExtensions = pydantic.Field()
    """
    The registered extensions this implementation provides, as a map of extension identifier to a details object describing how the extension is provided. Presence of a key means the extension is implemented; the value is an empty object when the extension has no extra details to communicate.
    
    Unregistered experimental extensions use an `x-` prefixed identifier and are outside the scope of this specification.
    """

    deposit: DepositCapability
    tombstone_policy: typing_extensions.Annotated[
        CapabilitiesTombstonePolicy,
        FieldMetadata(alias="tombstonePolicy"),
        pydantic.Field(
            alias="tombstonePolicy",
            description='What deleted resource URIs return. `"410"` - deleted URIs respond 410 Gone with a `Tombstone` body; `"404"` - deleted resources are indistinguishable from those that never existed. One policy covers RO-Crate, entity and file URIs alike; implementations MUST NOT mix them.\n\nREQUIRED of every implementation, whether or not it provides the deposit surface: entities and files are mandatory core, so any catalog may hold a URI that no longer resolves.',
        ),
    ]
    """
    What deleted resource URIs return. `"410"` - deleted URIs respond 410 Gone with a `Tombstone` body; `"404"` - deleted resources are indistinguishable from those that never existed. One policy covers RO-Crate, entity and file URIs alike; implementations MUST NOT mix them.
    
    REQUIRED of every implementation, whether or not it provides the deposit surface: entities and files are mandatory core, so any catalog may hold a URI that no longer resolves.
    """

    search: SearchCapability

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
