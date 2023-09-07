from explorer2go.apps.tenant.models import Domain, Tenant
from django.contrib.auth.models import User


User.objects.create_superuser(  # type: ignore
    username='test', password='123', email='test@test.com'
)


TENANTS = [
    ('clubesaber.com', 'clubesaber', 'Clube Saber'),
    ('localhost', 'localhost', 'Clube Saber'),
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
