

NonRootFolderPathInput = str
"""
Non-root folder path. A missing leading slash is normalized before validation. Segments are percent-encoded, so a folder shown as "New folder" is `/New%20folder`: everything outside `A-Z a-z 0-9 - _ . ~` is escaped as uppercase hex, and only that exact encoding is accepted. A trailing slash, an empty segment, and a literal `.` or `..` segment are rejected. At most 64 segments and 4096 encoded bytes.
"""
