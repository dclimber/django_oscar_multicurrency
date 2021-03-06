import oscar.apps.analytics.apps as apps


class AnalyticsConfig(apps.AnalyticsConfig):
    label = 'analytics'
    name = 'apps.analytics'
    verbose_name = 'Analytics'

    def ready(self):
        from . import receivers  # noqa
        super().ready()
