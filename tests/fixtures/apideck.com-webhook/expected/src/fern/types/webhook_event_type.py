

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class WebhookEventType(str, enum.Enum):
    ALL = "*"
    CRM_ACTIVITY_CREATED = "crm.activity.created"
    CRM_ACTIVITY_UPDATED = "crm.activity.updated"
    CRM_ACTIVITY_DELETED = "crm.activity.deleted"
    CRM_COMPANY_CREATED = "crm.company.created"
    CRM_COMPANY_UPDATED = "crm.company.updated"
    CRM_COMPANY_DELETED = "crm.company.deleted"
    CRM_CONTACT_CREATED = "crm.contact.created"
    CRM_CONTACT_UPDATED = "crm.contact.updated"
    CRM_CONTACT_DELETED = "crm.contact.deleted"
    CRM_LEAD_CREATED = "crm.lead.created"
    CRM_LEAD_UPDATED = "crm.lead.updated"
    CRM_LEAD_DELETED = "crm.lead.deleted"
    CRM_NOTE_CREATED = "crm.note.created"
    CRM_NOTES_UPDATED = "crm.notes.updated"
    CRM_NOTES_DELETED = "crm.notes.deleted"
    CRM_OPPORTUNITY_CREATED = "crm.opportunity.created"
    CRM_OPPORTUNITY_UPDATED = "crm.opportunity.updated"
    CRM_OPPORTUNITY_DELETED = "crm.opportunity.deleted"
    LEAD_LEAD_CREATED = "lead.lead.created"
    LEAD_LEAD_UPDATED = "lead.lead.updated"
    LEAD_LEAD_DELETED = "lead.lead.deleted"
    VAULT_CONNECTION_CREATED = "vault.connection.created"
    VAULT_CONNECTION_UPDATED = "vault.connection.updated"
    VAULT_CONNECTION_DISABLED = "vault.connection.disabled"
    VAULT_CONNECTION_DELETED = "vault.connection.deleted"
    VAULT_CONNECTION_CALLABLE = "vault.connection.callable"
    VAULT_CONNECTION_TOKEN_REFRESH_FAILED = "vault.connection.token_refresh.failed"
    ATS_JOB_CREATED = "ats.job.created"
    ATS_JOB_UPDATED = "ats.job.updated"
    ATS_JOB_DELETED = "ats.job.deleted"
    ATS_APPLICANT_CREATED = "ats.applicant.created"
    ATS_APPLICANT_UPDATED = "ats.applicant.updated"
    ATS_APPLICANT_DELETED = "ats.applicant.deleted"
    ACCOUNTING_CUSTOMER_CREATED = "accounting.customer.created"
    ACCOUNTING_CUSTOMER_UPDATED = "accounting.customer.updated"
    ACCOUNTING_CUSTOMER_DELETED = "accounting.customer.deleted"
    ACCOUNTING_INVOICE_CREATED = "accounting.invoice.created"
    ACCOUNTING_INVOICE_UPDATED = "accounting.invoice.updated"
    ACCOUNTING_INVOICE_DELETED = "accounting.invoice.deleted"
    ACCOUNTING_INVOICE_ITEM_CREATED = "accounting.invoice_item.created"
    ACCOUNTING_INVOICE_ITEM_UPDATED = "accounting.invoice_item.updated"
    ACCOUNTING_INVOICE_ITEM_DELETED = "accounting.invoice_item.deleted"
    ACCOUNTING_LEDGER_ACCOUNT_CREATED = "accounting.ledger_account.created"
    ACCOUNTING_LEDGER_ACCOUNT_UPDATED = "accounting.ledger_account.updated"
    ACCOUNTING_LEDGER_ACCOUNT_DELETED = "accounting.ledger_account.deleted"
    ACCOUNTING_TAX_RATE_CREATED = "accounting.tax_rate.created"
    ACCOUNTING_TAX_RATE_UPDATED = "accounting.tax_rate.updated"
    ACCOUNTING_TAX_RATE_DELETED = "accounting.tax_rate.deleted"
    ACCOUNTING_BILL_CREATED = "accounting.bill.created"
    ACCOUNTING_BILL_UPDATED = "accounting.bill.updated"
    ACCOUNTING_BILL_DELETED = "accounting.bill.deleted"
    ACCOUNTING_PAYMENT_CREATED = "accounting.payment.created"
    ACCOUNTING_PAYMENT_UPDATED = "accounting.payment.updated"
    ACCOUNTING_PAYMENT_DELETED = "accounting.payment.deleted"
    ACCOUNTING_SUPPLIER_CREATED = "accounting.supplier.created"
    ACCOUNTING_SUPPLIER_UPDATED = "accounting.supplier.updated"
    ACCOUNTING_SUPPLIER_DELETED = "accounting.supplier.deleted"
    POS_ORDER_CREATED = "pos.order.created"
    POS_ORDER_UPDATED = "pos.order.updated"
    POS_ORDER_DELETED = "pos.order.deleted"
    POS_PRODUCT_CREATED = "pos.product.created"
    POS_PRODUCT_UPDATED = "pos.product.updated"
    POS_PRODUCT_DELETED = "pos.product.deleted"
    POS_PAYMENT_CREATED = "pos.payment.created"
    POS_PAYMENT_UPDATED = "pos.payment.updated"
    POS_PAYMENT_DELETED = "pos.payment.deleted"
    POS_MERCHANT_CREATED = "pos.merchant.created"
    POS_MERCHANT_UPDATED = "pos.merchant.updated"
    POS_MERCHANT_DELETED = "pos.merchant.deleted"
    POS_LOCATION_CREATED = "pos.location.created"
    POS_LOCATION_UPDATED = "pos.location.updated"
    POS_LOCATION_DELETED = "pos.location.deleted"
    POS_ITEM_CREATED = "pos.item.created"
    POS_ITEM_UPDATED = "pos.item.updated"
    POS_ITEM_DELETED = "pos.item.deleted"
    POS_MODIFIER_CREATED = "pos.modifier.created"
    POS_MODIFIER_UPDATED = "pos.modifier.updated"
    POS_MODIFIER_DELETED = "pos.modifier.deleted"
    POS_MODIFIER_GROUP_CREATED = "pos.modifier-group.created"
    POS_MODIFIER_GROUP_UPDATED = "pos.modifier-group.updated"
    POS_MODIFIER_GROUP_DELETED = "pos.modifier-group.deleted"
    HRIS_EMPLOYEE_CREATED = "hris.employee.created"
    HRIS_EMPLOYEE_UPDATED = "hris.employee.updated"
    HRIS_EMPLOYEE_DELETED = "hris.employee.deleted"
    HRIS_COMPANY_CREATED = "hris.company.created"
    HRIS_COMPANY_UPDATED = "hris.company.updated"
    HRIS_COMPANY_DELETED = "hris.company.deleted"
    FILE_STORAGE_FILE_CREATED = "file-storage.file.created"
    FILE_STORAGE_FILE_UPDATED = "file-storage.file.updated"
    FILE_STORAGE_FILE_DELETED = "file-storage.file.deleted"
    ISSUE_TRACKING_TICKET_CREATED = "issue-tracking.ticket.created"
    ISSUE_TRACKING_TICKET_UPDATED = "issue-tracking.ticket.updated"
    ISSUE_TRACKING_TICKET_DELETED = "issue-tracking.ticket.deleted"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        crm_activity_created: typing.Callable[[], T_Result],
        crm_activity_updated: typing.Callable[[], T_Result],
        crm_activity_deleted: typing.Callable[[], T_Result],
        crm_company_created: typing.Callable[[], T_Result],
        crm_company_updated: typing.Callable[[], T_Result],
        crm_company_deleted: typing.Callable[[], T_Result],
        crm_contact_created: typing.Callable[[], T_Result],
        crm_contact_updated: typing.Callable[[], T_Result],
        crm_contact_deleted: typing.Callable[[], T_Result],
        crm_lead_created: typing.Callable[[], T_Result],
        crm_lead_updated: typing.Callable[[], T_Result],
        crm_lead_deleted: typing.Callable[[], T_Result],
        crm_note_created: typing.Callable[[], T_Result],
        crm_notes_updated: typing.Callable[[], T_Result],
        crm_notes_deleted: typing.Callable[[], T_Result],
        crm_opportunity_created: typing.Callable[[], T_Result],
        crm_opportunity_updated: typing.Callable[[], T_Result],
        crm_opportunity_deleted: typing.Callable[[], T_Result],
        lead_lead_created: typing.Callable[[], T_Result],
        lead_lead_updated: typing.Callable[[], T_Result],
        lead_lead_deleted: typing.Callable[[], T_Result],
        vault_connection_created: typing.Callable[[], T_Result],
        vault_connection_updated: typing.Callable[[], T_Result],
        vault_connection_disabled: typing.Callable[[], T_Result],
        vault_connection_deleted: typing.Callable[[], T_Result],
        vault_connection_callable: typing.Callable[[], T_Result],
        vault_connection_token_refresh_failed: typing.Callable[[], T_Result],
        ats_job_created: typing.Callable[[], T_Result],
        ats_job_updated: typing.Callable[[], T_Result],
        ats_job_deleted: typing.Callable[[], T_Result],
        ats_applicant_created: typing.Callable[[], T_Result],
        ats_applicant_updated: typing.Callable[[], T_Result],
        ats_applicant_deleted: typing.Callable[[], T_Result],
        accounting_customer_created: typing.Callable[[], T_Result],
        accounting_customer_updated: typing.Callable[[], T_Result],
        accounting_customer_deleted: typing.Callable[[], T_Result],
        accounting_invoice_created: typing.Callable[[], T_Result],
        accounting_invoice_updated: typing.Callable[[], T_Result],
        accounting_invoice_deleted: typing.Callable[[], T_Result],
        accounting_invoice_item_created: typing.Callable[[], T_Result],
        accounting_invoice_item_updated: typing.Callable[[], T_Result],
        accounting_invoice_item_deleted: typing.Callable[[], T_Result],
        accounting_ledger_account_created: typing.Callable[[], T_Result],
        accounting_ledger_account_updated: typing.Callable[[], T_Result],
        accounting_ledger_account_deleted: typing.Callable[[], T_Result],
        accounting_tax_rate_created: typing.Callable[[], T_Result],
        accounting_tax_rate_updated: typing.Callable[[], T_Result],
        accounting_tax_rate_deleted: typing.Callable[[], T_Result],
        accounting_bill_created: typing.Callable[[], T_Result],
        accounting_bill_updated: typing.Callable[[], T_Result],
        accounting_bill_deleted: typing.Callable[[], T_Result],
        accounting_payment_created: typing.Callable[[], T_Result],
        accounting_payment_updated: typing.Callable[[], T_Result],
        accounting_payment_deleted: typing.Callable[[], T_Result],
        accounting_supplier_created: typing.Callable[[], T_Result],
        accounting_supplier_updated: typing.Callable[[], T_Result],
        accounting_supplier_deleted: typing.Callable[[], T_Result],
        pos_order_created: typing.Callable[[], T_Result],
        pos_order_updated: typing.Callable[[], T_Result],
        pos_order_deleted: typing.Callable[[], T_Result],
        pos_product_created: typing.Callable[[], T_Result],
        pos_product_updated: typing.Callable[[], T_Result],
        pos_product_deleted: typing.Callable[[], T_Result],
        pos_payment_created: typing.Callable[[], T_Result],
        pos_payment_updated: typing.Callable[[], T_Result],
        pos_payment_deleted: typing.Callable[[], T_Result],
        pos_merchant_created: typing.Callable[[], T_Result],
        pos_merchant_updated: typing.Callable[[], T_Result],
        pos_merchant_deleted: typing.Callable[[], T_Result],
        pos_location_created: typing.Callable[[], T_Result],
        pos_location_updated: typing.Callable[[], T_Result],
        pos_location_deleted: typing.Callable[[], T_Result],
        pos_item_created: typing.Callable[[], T_Result],
        pos_item_updated: typing.Callable[[], T_Result],
        pos_item_deleted: typing.Callable[[], T_Result],
        pos_modifier_created: typing.Callable[[], T_Result],
        pos_modifier_updated: typing.Callable[[], T_Result],
        pos_modifier_deleted: typing.Callable[[], T_Result],
        pos_modifier_group_created: typing.Callable[[], T_Result],
        pos_modifier_group_updated: typing.Callable[[], T_Result],
        pos_modifier_group_deleted: typing.Callable[[], T_Result],
        hris_employee_created: typing.Callable[[], T_Result],
        hris_employee_updated: typing.Callable[[], T_Result],
        hris_employee_deleted: typing.Callable[[], T_Result],
        hris_company_created: typing.Callable[[], T_Result],
        hris_company_updated: typing.Callable[[], T_Result],
        hris_company_deleted: typing.Callable[[], T_Result],
        file_storage_file_created: typing.Callable[[], T_Result],
        file_storage_file_updated: typing.Callable[[], T_Result],
        file_storage_file_deleted: typing.Callable[[], T_Result],
        issue_tracking_ticket_created: typing.Callable[[], T_Result],
        issue_tracking_ticket_updated: typing.Callable[[], T_Result],
        issue_tracking_ticket_deleted: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WebhookEventType.ALL:
            return all_()
        if self is WebhookEventType.CRM_ACTIVITY_CREATED:
            return crm_activity_created()
        if self is WebhookEventType.CRM_ACTIVITY_UPDATED:
            return crm_activity_updated()
        if self is WebhookEventType.CRM_ACTIVITY_DELETED:
            return crm_activity_deleted()
        if self is WebhookEventType.CRM_COMPANY_CREATED:
            return crm_company_created()
        if self is WebhookEventType.CRM_COMPANY_UPDATED:
            return crm_company_updated()
        if self is WebhookEventType.CRM_COMPANY_DELETED:
            return crm_company_deleted()
        if self is WebhookEventType.CRM_CONTACT_CREATED:
            return crm_contact_created()
        if self is WebhookEventType.CRM_CONTACT_UPDATED:
            return crm_contact_updated()
        if self is WebhookEventType.CRM_CONTACT_DELETED:
            return crm_contact_deleted()
        if self is WebhookEventType.CRM_LEAD_CREATED:
            return crm_lead_created()
        if self is WebhookEventType.CRM_LEAD_UPDATED:
            return crm_lead_updated()
        if self is WebhookEventType.CRM_LEAD_DELETED:
            return crm_lead_deleted()
        if self is WebhookEventType.CRM_NOTE_CREATED:
            return crm_note_created()
        if self is WebhookEventType.CRM_NOTES_UPDATED:
            return crm_notes_updated()
        if self is WebhookEventType.CRM_NOTES_DELETED:
            return crm_notes_deleted()
        if self is WebhookEventType.CRM_OPPORTUNITY_CREATED:
            return crm_opportunity_created()
        if self is WebhookEventType.CRM_OPPORTUNITY_UPDATED:
            return crm_opportunity_updated()
        if self is WebhookEventType.CRM_OPPORTUNITY_DELETED:
            return crm_opportunity_deleted()
        if self is WebhookEventType.LEAD_LEAD_CREATED:
            return lead_lead_created()
        if self is WebhookEventType.LEAD_LEAD_UPDATED:
            return lead_lead_updated()
        if self is WebhookEventType.LEAD_LEAD_DELETED:
            return lead_lead_deleted()
        if self is WebhookEventType.VAULT_CONNECTION_CREATED:
            return vault_connection_created()
        if self is WebhookEventType.VAULT_CONNECTION_UPDATED:
            return vault_connection_updated()
        if self is WebhookEventType.VAULT_CONNECTION_DISABLED:
            return vault_connection_disabled()
        if self is WebhookEventType.VAULT_CONNECTION_DELETED:
            return vault_connection_deleted()
        if self is WebhookEventType.VAULT_CONNECTION_CALLABLE:
            return vault_connection_callable()
        if self is WebhookEventType.VAULT_CONNECTION_TOKEN_REFRESH_FAILED:
            return vault_connection_token_refresh_failed()
        if self is WebhookEventType.ATS_JOB_CREATED:
            return ats_job_created()
        if self is WebhookEventType.ATS_JOB_UPDATED:
            return ats_job_updated()
        if self is WebhookEventType.ATS_JOB_DELETED:
            return ats_job_deleted()
        if self is WebhookEventType.ATS_APPLICANT_CREATED:
            return ats_applicant_created()
        if self is WebhookEventType.ATS_APPLICANT_UPDATED:
            return ats_applicant_updated()
        if self is WebhookEventType.ATS_APPLICANT_DELETED:
            return ats_applicant_deleted()
        if self is WebhookEventType.ACCOUNTING_CUSTOMER_CREATED:
            return accounting_customer_created()
        if self is WebhookEventType.ACCOUNTING_CUSTOMER_UPDATED:
            return accounting_customer_updated()
        if self is WebhookEventType.ACCOUNTING_CUSTOMER_DELETED:
            return accounting_customer_deleted()
        if self is WebhookEventType.ACCOUNTING_INVOICE_CREATED:
            return accounting_invoice_created()
        if self is WebhookEventType.ACCOUNTING_INVOICE_UPDATED:
            return accounting_invoice_updated()
        if self is WebhookEventType.ACCOUNTING_INVOICE_DELETED:
            return accounting_invoice_deleted()
        if self is WebhookEventType.ACCOUNTING_INVOICE_ITEM_CREATED:
            return accounting_invoice_item_created()
        if self is WebhookEventType.ACCOUNTING_INVOICE_ITEM_UPDATED:
            return accounting_invoice_item_updated()
        if self is WebhookEventType.ACCOUNTING_INVOICE_ITEM_DELETED:
            return accounting_invoice_item_deleted()
        if self is WebhookEventType.ACCOUNTING_LEDGER_ACCOUNT_CREATED:
            return accounting_ledger_account_created()
        if self is WebhookEventType.ACCOUNTING_LEDGER_ACCOUNT_UPDATED:
            return accounting_ledger_account_updated()
        if self is WebhookEventType.ACCOUNTING_LEDGER_ACCOUNT_DELETED:
            return accounting_ledger_account_deleted()
        if self is WebhookEventType.ACCOUNTING_TAX_RATE_CREATED:
            return accounting_tax_rate_created()
        if self is WebhookEventType.ACCOUNTING_TAX_RATE_UPDATED:
            return accounting_tax_rate_updated()
        if self is WebhookEventType.ACCOUNTING_TAX_RATE_DELETED:
            return accounting_tax_rate_deleted()
        if self is WebhookEventType.ACCOUNTING_BILL_CREATED:
            return accounting_bill_created()
        if self is WebhookEventType.ACCOUNTING_BILL_UPDATED:
            return accounting_bill_updated()
        if self is WebhookEventType.ACCOUNTING_BILL_DELETED:
            return accounting_bill_deleted()
        if self is WebhookEventType.ACCOUNTING_PAYMENT_CREATED:
            return accounting_payment_created()
        if self is WebhookEventType.ACCOUNTING_PAYMENT_UPDATED:
            return accounting_payment_updated()
        if self is WebhookEventType.ACCOUNTING_PAYMENT_DELETED:
            return accounting_payment_deleted()
        if self is WebhookEventType.ACCOUNTING_SUPPLIER_CREATED:
            return accounting_supplier_created()
        if self is WebhookEventType.ACCOUNTING_SUPPLIER_UPDATED:
            return accounting_supplier_updated()
        if self is WebhookEventType.ACCOUNTING_SUPPLIER_DELETED:
            return accounting_supplier_deleted()
        if self is WebhookEventType.POS_ORDER_CREATED:
            return pos_order_created()
        if self is WebhookEventType.POS_ORDER_UPDATED:
            return pos_order_updated()
        if self is WebhookEventType.POS_ORDER_DELETED:
            return pos_order_deleted()
        if self is WebhookEventType.POS_PRODUCT_CREATED:
            return pos_product_created()
        if self is WebhookEventType.POS_PRODUCT_UPDATED:
            return pos_product_updated()
        if self is WebhookEventType.POS_PRODUCT_DELETED:
            return pos_product_deleted()
        if self is WebhookEventType.POS_PAYMENT_CREATED:
            return pos_payment_created()
        if self is WebhookEventType.POS_PAYMENT_UPDATED:
            return pos_payment_updated()
        if self is WebhookEventType.POS_PAYMENT_DELETED:
            return pos_payment_deleted()
        if self is WebhookEventType.POS_MERCHANT_CREATED:
            return pos_merchant_created()
        if self is WebhookEventType.POS_MERCHANT_UPDATED:
            return pos_merchant_updated()
        if self is WebhookEventType.POS_MERCHANT_DELETED:
            return pos_merchant_deleted()
        if self is WebhookEventType.POS_LOCATION_CREATED:
            return pos_location_created()
        if self is WebhookEventType.POS_LOCATION_UPDATED:
            return pos_location_updated()
        if self is WebhookEventType.POS_LOCATION_DELETED:
            return pos_location_deleted()
        if self is WebhookEventType.POS_ITEM_CREATED:
            return pos_item_created()
        if self is WebhookEventType.POS_ITEM_UPDATED:
            return pos_item_updated()
        if self is WebhookEventType.POS_ITEM_DELETED:
            return pos_item_deleted()
        if self is WebhookEventType.POS_MODIFIER_CREATED:
            return pos_modifier_created()
        if self is WebhookEventType.POS_MODIFIER_UPDATED:
            return pos_modifier_updated()
        if self is WebhookEventType.POS_MODIFIER_DELETED:
            return pos_modifier_deleted()
        if self is WebhookEventType.POS_MODIFIER_GROUP_CREATED:
            return pos_modifier_group_created()
        if self is WebhookEventType.POS_MODIFIER_GROUP_UPDATED:
            return pos_modifier_group_updated()
        if self is WebhookEventType.POS_MODIFIER_GROUP_DELETED:
            return pos_modifier_group_deleted()
        if self is WebhookEventType.HRIS_EMPLOYEE_CREATED:
            return hris_employee_created()
        if self is WebhookEventType.HRIS_EMPLOYEE_UPDATED:
            return hris_employee_updated()
        if self is WebhookEventType.HRIS_EMPLOYEE_DELETED:
            return hris_employee_deleted()
        if self is WebhookEventType.HRIS_COMPANY_CREATED:
            return hris_company_created()
        if self is WebhookEventType.HRIS_COMPANY_UPDATED:
            return hris_company_updated()
        if self is WebhookEventType.HRIS_COMPANY_DELETED:
            return hris_company_deleted()
        if self is WebhookEventType.FILE_STORAGE_FILE_CREATED:
            return file_storage_file_created()
        if self is WebhookEventType.FILE_STORAGE_FILE_UPDATED:
            return file_storage_file_updated()
        if self is WebhookEventType.FILE_STORAGE_FILE_DELETED:
            return file_storage_file_deleted()
        if self is WebhookEventType.ISSUE_TRACKING_TICKET_CREATED:
            return issue_tracking_ticket_created()
        if self is WebhookEventType.ISSUE_TRACKING_TICKET_UPDATED:
            return issue_tracking_ticket_updated()
        if self is WebhookEventType.ISSUE_TRACKING_TICKET_DELETED:
            return issue_tracking_ticket_deleted()
