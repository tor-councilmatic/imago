from rest_framework.routers import Route, DefaultRouter

class DefaultOCDRouter(DefaultRouter):

    def __init__(self, *args, **kwargs):
        ocd_detail_route = Route(
                url=r'{lookup}{trailing_slash}$',
                mapping={
                    'get': 'retrieve',
                    },
                name='{basename}-detail',
                initkwargs={'suffix': 'Instance'},
                )
        # Strip out the old retrieve route mapping
        self.routes[-2][1].pop('get', None)
        self.routes = self.routes + [ocd_detail_route]
        super(DefaultOCDRouter, self).__init__(*args, **kwargs)

    def get_lookup_regex(self, viewset, lookup_prefix=''):
        """
        Given a viewset, return the portion of URL regex that is used
        to match against a single instance.
        Note that lookup_prefix is not used directly inside REST rest_framework
        itself, but is required in order to nicely support nested router
        implementations, such as drf-nested-routers.
        https://github.com/alanjds/drf-nested-routers
        """
        base_regex = '(?P<{lookup_prefix}{lookup_url_kwarg}>ocd-{lookup_base_name}/{lookup_value})'
        # Use `pk` as default field, unset set.  Default regex should not
        # consume `.json` style suffixes and should break at '/' boundaries.
        lookup_field = getattr(viewset, 'lookup_field', 'pk')
        lookup_url_kwarg = getattr(viewset, 'lookup_url_kwarg', None) or lookup_field
        lookup_base_name = self.get_default_base_name(viewset)
        if lookup_base_name == 'voteevent':
            lookup_base_name = 'vote'
        if lookup_base_name in ['division', 'jurisdiction']:
            lookup_value = '[a-z0-9\-\:\/]+'
        else:
            lookup_value = '[a-f0-9\-]+'

        return base_regex.format(
            lookup_prefix=lookup_prefix,
            lookup_url_kwarg=lookup_url_kwarg,
            lookup_base_name=lookup_base_name,
            lookup_value=lookup_value,
)
