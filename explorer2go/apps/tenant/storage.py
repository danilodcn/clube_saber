from django_tenants.utils import parse_tenant_config_path
from storages.backends.s3boto3 import S3Boto3Storage


class TenantS3Storage(S3Boto3Storage):
    def get_default_settings(self):
        settings = super().get_default_settings()
        settings['location'] = parse_tenant_config_path('daconnas-%s')
        return settings
