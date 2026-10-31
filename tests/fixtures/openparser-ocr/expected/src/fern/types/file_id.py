

FileId = str
"""
Eigenpal reusable file-pool id from `POST /files`. Resolved with the same
tenant-scoped authorization as `GET /files/{id}/content`. Missing or
cross-tenant ids return `404 file_not_found`.
"""
