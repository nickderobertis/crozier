

import typing

from .v2file_contract_expiration import V2FileContractExpiration
from .v2file_contract_renewal import V2FileContractRenewal
from .v2storage_proof import V2StorageProof

V2FileContractResolutionResolution = typing.Union[V2FileContractRenewal, V2StorageProof, V2FileContractExpiration]
