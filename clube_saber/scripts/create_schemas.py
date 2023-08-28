from clube_saber.apps.tenant.models import Tenant, Domain

TENANTS = [
    ('clubesaber.com', 'clube_saber', 'Clube Saber'),
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
