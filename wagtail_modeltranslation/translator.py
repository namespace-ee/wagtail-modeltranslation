from modeltranslation.translator import TranslationOptions


class WagtailTranslationOptions(TranslationOptions):
    def __init__(self, model):
        from wagtail.wagtailcore.models import Page
        if Page in model.__bases__:
            self.fields += (
                'title',
                'slug',
                'seo_title',
                'search_description',
                'url_path',)

        super(WagtailTranslationOptions, self).__init__(model)
