

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocRenderResponseCode(enum.StrEnum):
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
        if self is DocRenderResponseCode.UNKNOWN:
            return unknown()
        if self is DocRenderResponseCode.INVALID_ARG:
            return invalid_arg()
        if self is DocRenderResponseCode.DOC_NOT_OPEN:
            return doc_not_open()
        if self is DocRenderResponseCode.DOC_OPEN_FAILED:
            return doc_open_failed()
        if self is DocRenderResponseCode.DOC_PASSWORD_REQUIRED:
            return doc_password_required()
        if self is DocRenderResponseCode.DOC_PASSWORD_INCORRECT:
            return doc_password_incorrect()
        if self is DocRenderResponseCode.SHARE_PASSWORD_REQUIRED:
            return share_password_required()
        if self is DocRenderResponseCode.ABORTED:
            return aborted()
        if self is DocRenderResponseCode.NETWORK:
            return network()
        if self is DocRenderResponseCode.UNAUTHENTICATED:
            return unauthenticated()
        if self is DocRenderResponseCode.FORBIDDEN:
            return forbidden()
        if self is DocRenderResponseCode.NOT_FOUND:
            return not_found()
        if self is DocRenderResponseCode.WIRE_FORMAT:
            return wire_format()
        if self is DocRenderResponseCode.RUNTIME_UNAVAILABLE:
            return runtime_unavailable()
        if self is DocRenderResponseCode.INVALID_REFERENCE:
            return invalid_reference()
        if self is DocRenderResponseCode.WEAK_ANNOTATION_SESSION_CONFLICT:
            return weak_annotation_session_conflict()
        if self is DocRenderResponseCode.LAYER_VERSION_CONFLICT:
            return layer_version_conflict()
        if self is DocRenderResponseCode.NOT_IMPLEMENTED:
            return not_implemented()
        if self is DocRenderResponseCode.MALFORMED_PDF:
            return malformed_pdf()
        if self is DocRenderResponseCode.SIGNING_PENDING:
            return signing_pending()
        if self is DocRenderResponseCode.SIGNING_EXPIRED:
            return signing_expired()
        if self is DocRenderResponseCode.SIGNING_VERSION_MISMATCH:
            return signing_version_mismatch()
        if self is DocRenderResponseCode.SIGNATURE_REFUSED:
            return signature_refused()
        if self is DocRenderResponseCode.PROTECTED_DOCUMENT:
            return protected_document()
        if self is DocRenderResponseCode.STALE_BASE:
            return stale_base()
