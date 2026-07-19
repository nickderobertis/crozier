



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .alpine import Alpine
    from .alpine_package_schema import AlpinePackageSchema
    from .alpine_package_schema_package import AlpinePackageSchemaPackage
    from .alpine_package_schema_package_hash import AlpinePackageSchemaPackageHash
    from .alpine_package_schema_package_hash_algorithm import AlpinePackageSchemaPackageHashAlgorithm
    from .alpine_package_schema_public_key import AlpinePackageSchemaPublicKey
    from .consistency_proof import ConsistencyProof
    from .cose import Cose
    from .cose_schema import CoseSchema
    from .cose_schema_data import CoseSchemaData
    from .cose_schema_data_envelope_hash import CoseSchemaDataEnvelopeHash
    from .cose_schema_data_envelope_hash_algorithm import CoseSchemaDataEnvelopeHashAlgorithm
    from .cose_schema_data_payload_hash import CoseSchemaDataPayloadHash
    from .cose_schema_data_payload_hash_algorithm import CoseSchemaDataPayloadHashAlgorithm
    from .dsse import Dsse
    from .dsse_schema import DsseSchema
    from .dsse_schema_envelope_hash import DsseSchemaEnvelopeHash
    from .dsse_schema_envelope_hash_algorithm import DsseSchemaEnvelopeHashAlgorithm
    from .dsse_schema_payload_hash import DsseSchemaPayloadHash
    from .dsse_schema_payload_hash_algorithm import DsseSchemaPayloadHashAlgorithm
    from .dsse_schema_proposed_content import DsseSchemaProposedContent
    from .dsse_schema_signatures_item import DsseSchemaSignaturesItem
    from .error import Error
    from .hashedrekord import Hashedrekord
    from .hashedrekord_schema import HashedrekordSchema
    from .hashedrekord_schema_data import HashedrekordSchemaData
    from .hashedrekord_schema_data_hash import HashedrekordSchemaDataHash
    from .hashedrekord_schema_data_hash_algorithm import HashedrekordSchemaDataHashAlgorithm
    from .hashedrekord_schema_signature import HashedrekordSchemaSignature
    from .hashedrekord_schema_signature_public_key import HashedrekordSchemaSignaturePublicKey
    from .helm import Helm
    from .helm_schema import HelmSchema
    from .helm_schema_chart import HelmSchemaChart
    from .helm_schema_chart_hash import HelmSchemaChartHash
    from .helm_schema_chart_hash_algorithm import HelmSchemaChartHashAlgorithm
    from .helm_schema_chart_provenance import HelmSchemaChartProvenance
    from .helm_schema_chart_provenance_signature import HelmSchemaChartProvenanceSignature
    from .helm_schema_public_key import HelmSchemaPublicKey
    from .inactive_shard_log_info import InactiveShardLogInfo
    from .inclusion_proof import InclusionProof
    from .intoto import Intoto
    from .intoto_schema import IntotoSchema
    from .intoto_schema_one import IntotoSchemaOne
    from .intoto_schema_one_content import IntotoSchemaOneContent
    from .intoto_schema_one_content_envelope import IntotoSchemaOneContentEnvelope
    from .intoto_schema_one_content_envelope_signatures_item import IntotoSchemaOneContentEnvelopeSignaturesItem
    from .intoto_schema_one_content_hash import IntotoSchemaOneContentHash
    from .intoto_schema_one_content_hash_algorithm import IntotoSchemaOneContentHashAlgorithm
    from .intoto_schema_one_content_payload_hash import IntotoSchemaOneContentPayloadHash
    from .intoto_schema_one_content_payload_hash_algorithm import IntotoSchemaOneContentPayloadHashAlgorithm
    from .intoto_schema_public_key import IntotoSchemaPublicKey
    from .intoto_schema_public_key_content import IntotoSchemaPublicKeyContent
    from .intoto_schema_public_key_content_hash import IntotoSchemaPublicKeyContentHash
    from .intoto_schema_public_key_content_hash_algorithm import IntotoSchemaPublicKeyContentHashAlgorithm
    from .intoto_schema_public_key_content_payload_hash import IntotoSchemaPublicKeyContentPayloadHash
    from .intoto_schema_public_key_content_payload_hash_algorithm import (
        IntotoSchemaPublicKeyContentPayloadHashAlgorithm,
    )
    from .jar import Jar
    from .jar_schema import JarSchema
    from .jar_schema_archive import JarSchemaArchive
    from .jar_schema_archive_hash import JarSchemaArchiveHash
    from .jar_schema_archive_hash_algorithm import JarSchemaArchiveHashAlgorithm
    from .jar_schema_signature import JarSchemaSignature
    from .jar_schema_signature_public_key import JarSchemaSignaturePublicKey
    from .log_entry import LogEntry
    from .log_entry_value import LogEntryValue
    from .log_entry_value_attestation import LogEntryValueAttestation
    from .log_entry_value_verification import LogEntryValueVerification
    from .log_info import LogInfo
    from .proposed_entry import ProposedEntry
    from .rekor_schema import RekorSchema
    from .rekor_schema_data import RekorSchemaData
    from .rekor_schema_data_hash import RekorSchemaDataHash
    from .rekor_schema_data_hash_algorithm import RekorSchemaDataHashAlgorithm
    from .rekor_schema_signature import RekorSchemaSignature
    from .rekor_schema_signature_format import RekorSchemaSignatureFormat
    from .rekor_schema_signature_public_key import RekorSchemaSignaturePublicKey
    from .rekord import Rekord
    from .rfc3161 import Rfc3161
    from .rpm import Rpm
    from .rpm_schema import RpmSchema
    from .rpm_schema_package import RpmSchemaPackage
    from .rpm_schema_package_hash import RpmSchemaPackageHash
    from .rpm_schema_package_hash_algorithm import RpmSchemaPackageHashAlgorithm
    from .rpm_schema_public_key import RpmSchemaPublicKey
    from .timestamp_schema import TimestampSchema
    from .timestamp_schema_tsr import TimestampSchemaTsr
    from .tuf import Tuf
    from .tuf_schema import TufSchema
    from .tuf_schema_metadata import TufSchemaMetadata
    from .tuf_schema_root import TufSchemaRoot
_dynamic_imports: typing.Dict[str, str] = {
    "Alpine": ".alpine",
    "AlpinePackageSchema": ".alpine_package_schema",
    "AlpinePackageSchemaPackage": ".alpine_package_schema_package",
    "AlpinePackageSchemaPackageHash": ".alpine_package_schema_package_hash",
    "AlpinePackageSchemaPackageHashAlgorithm": ".alpine_package_schema_package_hash_algorithm",
    "AlpinePackageSchemaPublicKey": ".alpine_package_schema_public_key",
    "ConsistencyProof": ".consistency_proof",
    "Cose": ".cose",
    "CoseSchema": ".cose_schema",
    "CoseSchemaData": ".cose_schema_data",
    "CoseSchemaDataEnvelopeHash": ".cose_schema_data_envelope_hash",
    "CoseSchemaDataEnvelopeHashAlgorithm": ".cose_schema_data_envelope_hash_algorithm",
    "CoseSchemaDataPayloadHash": ".cose_schema_data_payload_hash",
    "CoseSchemaDataPayloadHashAlgorithm": ".cose_schema_data_payload_hash_algorithm",
    "Dsse": ".dsse",
    "DsseSchema": ".dsse_schema",
    "DsseSchemaEnvelopeHash": ".dsse_schema_envelope_hash",
    "DsseSchemaEnvelopeHashAlgorithm": ".dsse_schema_envelope_hash_algorithm",
    "DsseSchemaPayloadHash": ".dsse_schema_payload_hash",
    "DsseSchemaPayloadHashAlgorithm": ".dsse_schema_payload_hash_algorithm",
    "DsseSchemaProposedContent": ".dsse_schema_proposed_content",
    "DsseSchemaSignaturesItem": ".dsse_schema_signatures_item",
    "Error": ".error",
    "Hashedrekord": ".hashedrekord",
    "HashedrekordSchema": ".hashedrekord_schema",
    "HashedrekordSchemaData": ".hashedrekord_schema_data",
    "HashedrekordSchemaDataHash": ".hashedrekord_schema_data_hash",
    "HashedrekordSchemaDataHashAlgorithm": ".hashedrekord_schema_data_hash_algorithm",
    "HashedrekordSchemaSignature": ".hashedrekord_schema_signature",
    "HashedrekordSchemaSignaturePublicKey": ".hashedrekord_schema_signature_public_key",
    "Helm": ".helm",
    "HelmSchema": ".helm_schema",
    "HelmSchemaChart": ".helm_schema_chart",
    "HelmSchemaChartHash": ".helm_schema_chart_hash",
    "HelmSchemaChartHashAlgorithm": ".helm_schema_chart_hash_algorithm",
    "HelmSchemaChartProvenance": ".helm_schema_chart_provenance",
    "HelmSchemaChartProvenanceSignature": ".helm_schema_chart_provenance_signature",
    "HelmSchemaPublicKey": ".helm_schema_public_key",
    "InactiveShardLogInfo": ".inactive_shard_log_info",
    "InclusionProof": ".inclusion_proof",
    "Intoto": ".intoto",
    "IntotoSchema": ".intoto_schema",
    "IntotoSchemaOne": ".intoto_schema_one",
    "IntotoSchemaOneContent": ".intoto_schema_one_content",
    "IntotoSchemaOneContentEnvelope": ".intoto_schema_one_content_envelope",
    "IntotoSchemaOneContentEnvelopeSignaturesItem": ".intoto_schema_one_content_envelope_signatures_item",
    "IntotoSchemaOneContentHash": ".intoto_schema_one_content_hash",
    "IntotoSchemaOneContentHashAlgorithm": ".intoto_schema_one_content_hash_algorithm",
    "IntotoSchemaOneContentPayloadHash": ".intoto_schema_one_content_payload_hash",
    "IntotoSchemaOneContentPayloadHashAlgorithm": ".intoto_schema_one_content_payload_hash_algorithm",
    "IntotoSchemaPublicKey": ".intoto_schema_public_key",
    "IntotoSchemaPublicKeyContent": ".intoto_schema_public_key_content",
    "IntotoSchemaPublicKeyContentHash": ".intoto_schema_public_key_content_hash",
    "IntotoSchemaPublicKeyContentHashAlgorithm": ".intoto_schema_public_key_content_hash_algorithm",
    "IntotoSchemaPublicKeyContentPayloadHash": ".intoto_schema_public_key_content_payload_hash",
    "IntotoSchemaPublicKeyContentPayloadHashAlgorithm": ".intoto_schema_public_key_content_payload_hash_algorithm",
    "Jar": ".jar",
    "JarSchema": ".jar_schema",
    "JarSchemaArchive": ".jar_schema_archive",
    "JarSchemaArchiveHash": ".jar_schema_archive_hash",
    "JarSchemaArchiveHashAlgorithm": ".jar_schema_archive_hash_algorithm",
    "JarSchemaSignature": ".jar_schema_signature",
    "JarSchemaSignaturePublicKey": ".jar_schema_signature_public_key",
    "LogEntry": ".log_entry",
    "LogEntryValue": ".log_entry_value",
    "LogEntryValueAttestation": ".log_entry_value_attestation",
    "LogEntryValueVerification": ".log_entry_value_verification",
    "LogInfo": ".log_info",
    "ProposedEntry": ".proposed_entry",
    "RekorSchema": ".rekor_schema",
    "RekorSchemaData": ".rekor_schema_data",
    "RekorSchemaDataHash": ".rekor_schema_data_hash",
    "RekorSchemaDataHashAlgorithm": ".rekor_schema_data_hash_algorithm",
    "RekorSchemaSignature": ".rekor_schema_signature",
    "RekorSchemaSignatureFormat": ".rekor_schema_signature_format",
    "RekorSchemaSignaturePublicKey": ".rekor_schema_signature_public_key",
    "Rekord": ".rekord",
    "Rfc3161": ".rfc3161",
    "Rpm": ".rpm",
    "RpmSchema": ".rpm_schema",
    "RpmSchemaPackage": ".rpm_schema_package",
    "RpmSchemaPackageHash": ".rpm_schema_package_hash",
    "RpmSchemaPackageHashAlgorithm": ".rpm_schema_package_hash_algorithm",
    "RpmSchemaPublicKey": ".rpm_schema_public_key",
    "TimestampSchema": ".timestamp_schema",
    "TimestampSchemaTsr": ".timestamp_schema_tsr",
    "Tuf": ".tuf",
    "TufSchema": ".tuf_schema",
    "TufSchemaMetadata": ".tuf_schema_metadata",
    "TufSchemaRoot": ".tuf_schema_root",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "Alpine",
    "AlpinePackageSchema",
    "AlpinePackageSchemaPackage",
    "AlpinePackageSchemaPackageHash",
    "AlpinePackageSchemaPackageHashAlgorithm",
    "AlpinePackageSchemaPublicKey",
    "ConsistencyProof",
    "Cose",
    "CoseSchema",
    "CoseSchemaData",
    "CoseSchemaDataEnvelopeHash",
    "CoseSchemaDataEnvelopeHashAlgorithm",
    "CoseSchemaDataPayloadHash",
    "CoseSchemaDataPayloadHashAlgorithm",
    "Dsse",
    "DsseSchema",
    "DsseSchemaEnvelopeHash",
    "DsseSchemaEnvelopeHashAlgorithm",
    "DsseSchemaPayloadHash",
    "DsseSchemaPayloadHashAlgorithm",
    "DsseSchemaProposedContent",
    "DsseSchemaSignaturesItem",
    "Error",
    "Hashedrekord",
    "HashedrekordSchema",
    "HashedrekordSchemaData",
    "HashedrekordSchemaDataHash",
    "HashedrekordSchemaDataHashAlgorithm",
    "HashedrekordSchemaSignature",
    "HashedrekordSchemaSignaturePublicKey",
    "Helm",
    "HelmSchema",
    "HelmSchemaChart",
    "HelmSchemaChartHash",
    "HelmSchemaChartHashAlgorithm",
    "HelmSchemaChartProvenance",
    "HelmSchemaChartProvenanceSignature",
    "HelmSchemaPublicKey",
    "InactiveShardLogInfo",
    "InclusionProof",
    "Intoto",
    "IntotoSchema",
    "IntotoSchemaOne",
    "IntotoSchemaOneContent",
    "IntotoSchemaOneContentEnvelope",
    "IntotoSchemaOneContentEnvelopeSignaturesItem",
    "IntotoSchemaOneContentHash",
    "IntotoSchemaOneContentHashAlgorithm",
    "IntotoSchemaOneContentPayloadHash",
    "IntotoSchemaOneContentPayloadHashAlgorithm",
    "IntotoSchemaPublicKey",
    "IntotoSchemaPublicKeyContent",
    "IntotoSchemaPublicKeyContentHash",
    "IntotoSchemaPublicKeyContentHashAlgorithm",
    "IntotoSchemaPublicKeyContentPayloadHash",
    "IntotoSchemaPublicKeyContentPayloadHashAlgorithm",
    "Jar",
    "JarSchema",
    "JarSchemaArchive",
    "JarSchemaArchiveHash",
    "JarSchemaArchiveHashAlgorithm",
    "JarSchemaSignature",
    "JarSchemaSignaturePublicKey",
    "LogEntry",
    "LogEntryValue",
    "LogEntryValueAttestation",
    "LogEntryValueVerification",
    "LogInfo",
    "ProposedEntry",
    "RekorSchema",
    "RekorSchemaData",
    "RekorSchemaDataHash",
    "RekorSchemaDataHashAlgorithm",
    "RekorSchemaSignature",
    "RekorSchemaSignatureFormat",
    "RekorSchemaSignaturePublicKey",
    "Rekord",
    "Rfc3161",
    "Rpm",
    "RpmSchema",
    "RpmSchemaPackage",
    "RpmSchemaPackageHash",
    "RpmSchemaPackageHashAlgorithm",
    "RpmSchemaPublicKey",
    "TimestampSchema",
    "TimestampSchemaTsr",
    "Tuf",
    "TufSchema",
    "TufSchemaMetadata",
    "TufSchemaRoot",
]
