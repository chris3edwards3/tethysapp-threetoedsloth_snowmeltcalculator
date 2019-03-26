from tethys_sdk.base import TethysAppBase, url_map_maker


class ThreetoedslothSnowmeltcalculator(TethysAppBase):
    """
    Tethys app class for Three Toed Sloth Snowmelt Calculator.
    """

    name = 'Three-Toed Sloth: Snowmelt Calculator'
    index = 'threetoedsloth_snowmeltcalculator:home'
    icon = 'threetoedsloth_snowmeltcalculator/images/snowicon.png'
    package = 'threetoedsloth_snowmeltcalculator'
    root_url = 'threetoedsloth-snowmeltcalculator'
    color = '#35acf2'
    description = 'Calculate Snowmelt in a user-defined watershed.'
    tags = 'Snowmelt'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='threetoedsloth-snowmeltcalculator',
                controller='threetoedsloth_snowmeltcalculator.controllers.home'
            ),
            UrlMap(
                name='proposal',
                url='threetoedsloth-snowmeltcalculator/proposal',
                controller='threetoedsloth_snowmeltcalculator.controllers.proposal'
            ),
            UrlMap(
                name='mockup',
                url='threetoedsloth-snowmeltcalculator/mockup',
                controller='threetoedsloth_snowmeltcalculator.controllers.mockup'
            ),
            UrlMap(
                name='map',
                url='threetoedsloth-snowmeltcalculator/map',
                controller='threetoedsloth_snowmeltcalculator.controllers.map'
            )
        )

        return url_maps
