from django.test.runner import DiscoverRunner


class TestRunner(DiscoverRunner):

    def __init__(self, pattern = None, top_level = None, verbosity = 1, interactive = True, failfast = False, keepdb = True, reverse = False, debug_mode = False, debug_sql = False, parallel = 0, tags = None, exclude_tags = None,
                 test_name_patterns = None, pdb = False, buffer = False, enable_faulthandler = True, timing = False, **kwargs):
        super().__init__(pattern, top_level, verbosity, interactive, failfast, keepdb, reverse, debug_mode, debug_sql, parallel, tags, exclude_tags, test_name_patterns, pdb, buffer, enable_faulthandler, timing, **kwargs)

    def setup_databases(self, **kwargs):
        return super().setup_databases(**kwargs)



