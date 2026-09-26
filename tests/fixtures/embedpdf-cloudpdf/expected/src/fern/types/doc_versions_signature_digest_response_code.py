

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocVersionsSignatureDigestResponseCode(enum.StrEnum):
    UNKNOWN = "Unknown"
    INVALID_ARG = "InvalidArg"
    DOC_NOT_OPEN = "DocNotOpen"
    DOC_OPEN_FAILED = "DocOpenFailed"
    DOC_PASSWORD_REQUIRED = "DocPasswordRequired"
    DOC_PASSWORD_INCORRECT = "DocPasswordIncorrect"
    SHARE_PASSWORD_REQUIRED = "SharePasswordRequired"
    ABORTED = "Aborted"
    NETWORK = "Network"
    UNAUTHENTICATED = "Unauthenticated"
    FORBIDDEN = "Forbidden"
    NOT_FOUND = "NotFound"
    WIRE_FORMAT = "WireFormat"
    RUNTIME_UNAVAILABLE = "RuntimeUnavailable"
    INVALID_REFERENCE = "InvalidReference"
    WEAK_ANNOTATION_SESSION_CONFLICT = "WeakAnnotationSessionConflict"
    LAYER_VERSION_CONFLICT = "LayerVersionConflict"
    NOT_IMPLEMENTED = "NotImplemented"
    MALFORMED_PDF = "MalformedPdf"
    SIGNING_PENDING = "SigningPending"
    SIGNING_EXPIRED = "SigningExpired"
    SIGNING_VERSION_MISMATCH = "SigningVersionMismatch"
    SIGNATURE_REFUSED = "SignatureRefused"
    PROTECTED_DOCUMENT = "ProtectedDocument"
    STALE_BASE = "StaleBase"

    def visit(
        self,
        unknown: typing.Callable[[], T_Result],
        invalid_arg: typing.Callable[[], T_Result],
        doc_not_open: typing.Callable[[], T_Result],
        doc_open_failed: typing.Callable[[], T_Result],
        doc_password_required: typing.Callable[[], T_Result],
        doc_password_incorrect: typing.Callable[[], T_Result],
        share_password_required: typing.Callable[[], T_Result],
        aborted: typing.Callable[[], T_Result],
        network: typing.Callable[[], T_Result],
        unauthenticated: typing.Callable[[], T_Result],
        forbidden: typing.Callable[[], T_Result],
        not_found: typing.Callable[[], T_Result],
        wire_format: typing.Callable[[], T_Result],
        runtime_unavailable: typing.Callable[[], T_Result],
        invalid_reference: typing.Callable[[], T_Result],
        weak_annotation_session_conflict: typing.Callable[[], T_Result],
        layer_version_conflict: typing.Callable[[], T_Result],
        not_implemented: typing.Callable[[], T_Result],
        malformed_pdf: typing.Callable[[], T_Result],
        signing_pending: typing.Callable[[], T_Result],
        signing_expired: typing.Callable[[], T_Result],
        signing_version_mismatch: typing.Callable[[], T_Result],
        signature_refused: typing.Callable[[], T_Result],
        protected_document: typing.Callable[[], T_Result],
        stale_base: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocVersionsSignatureDigestResponseCode.UNKNOWN:
            return unknown()
        if self is DocVersionsSignatureDigestResponseCode.INVALID_ARG:
            return invalid_arg()
        if self is DocVersionsSignatureDigestResponseCode.DOC_NOT_OPEN:
            return doc_not_open()
        if self is DocVersionsSignatureDigestResponseCode.DOC_OPEN_FAILED:
            return doc_open_failed()
        if self is DocVersionsSignatureDigestResponseCode.DOC_PASSWORD_REQUIRED:
            return doc_password_required()
        if self is DocVersionsSignatureDigestResponseCode.DOC_PASSWORD_INCORRECT:
            return doc_password_incorrect()
        if self is DocVersionsSignatureDigestResponseCode.SHARE_PASSWORD_REQUIRED:
            return share_password_required()
        if self is DocVersionsSignatureDigestResponseCode.ABORTED:
            return aborted()
        if self is DocVersionsSignatureDigestResponseCode.NETWORK:
            return network()
        if self is DocVersionsSignatureDigestResponseCode.UNAUTHENTICATED:
            return unauthenticated()
        if self is DocVersionsSignatureDigestResponseCode.FORBIDDEN:
            return forbidden()
        if self is DocVersionsSignatureDigestResponseCode.NOT_FOUND:
            return not_found()
        if self is DocVersionsSignatureDigestResponseCode.WIRE_FORMAT:
            return wire_format()
        if self is DocVersionsSignatureDigestResponseCode.RUNTIME_UNAVAILABLE:
            return runtime_unavailable()
        if self is DocVersionsSignatureDigestResponseCode.INVALID_REFERENCE:
            return invalid_reference()
        if self is DocVersionsSignatureDigestResponseCode.WEAK_ANNOTATION_SESSION_CONFLICT:
            return weak_annotation_session_conflict()
        if self is DocVersionsSignatureDigestResponseCode.LAYER_VERSION_CONFLICT:
            return layer_version_conflict()
        if self is DocVersionsSignatureDigestResponseCode.NOT_IMPLEMENTED:
            return not_implemented()
        if self is DocVersionsSignatureDigestResponseCode.MALFORMED_PDF:
            return malformed_pdf()
        if self is DocVersionsSignatureDigestResponseCode.SIGNING_PENDING:
            return signing_pending()
        if self is DocVersionsSignatureDigestResponseCode.SIGNING_EXPIRED:
            return signing_expired()
        if self is DocVersionsSignatureDigestResponseCode.SIGNING_VERSION_MISMATCH:
            return signing_version_mismatch()
        if self is DocVersionsSignatureDigestResponseCode.SIGNATURE_REFUSED:
            return signature_refused()
        if self is DocVersionsSignatureDigestResponseCode.PROTECTED_DOCUMENT:
            return protected_document()
        if self is DocVersionsSignatureDigestResponseCode.STALE_BASE:
            return stale_base()
