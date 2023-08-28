from clube_saber.apps.tenant.models import Client, Domain

TENANTS = [
    ('clubesaber.com', 'clube_saber', 'Clube Saber'),
]

for domain_url, schema, name in TENANTS:
    client = Client(schema_name=schema, name=name)
    client.save()

    domain = Domain(
        domain=domain_url,
        tenant=client,
        is_primary=schema == 'default',
    )

    domain.save()
