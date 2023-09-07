from explorer2go.apps.tenant.models import Domain, Tenant

TENANTS = [
    ('clubesaber.com', 'explorer2go', 'Clube Saber'),
]

for domain_url, schema, name in TENANTS:
    tenant = Tenant(schema_name=schema, name=name)
    tenant.save()

    domain = Domain(
        domain=domain_url,
        tenant=tenant,
        is_primary=schema == 'default',
    )

    domain.save()
