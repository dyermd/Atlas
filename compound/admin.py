from django.contrib import admin
from compound.models import Compound
from compound.models import Compound_Xref
from compound.models import Patent
from compound.models import Manufacturer
from compound.models import Side_Effect
from compound.models import Annotated_With

# Register your models here.
class Compound_Admin(admin.ModelAdmin):
    search_fields = ("lam_id", "name")
    list_display = ("lam_id", "name", "smiles", "structure_2d")
admin.site.register(Compound, Compound_Admin)

class Compound_Xref_Admin(admin.ModelAdmin):
    search_fields = ("compound__lam_id", "compound__name", "source__name", "xref")
    list_display = ("compound", "get_name", "source", "xref")

    def get_name(self, obj):
        return obj.compound.name
    get_name.short_description="Name"
admin.site.register(Compound_Xref, Compound_Xref_Admin)

class Patent_Admin(admin.ModelAdmin):
    search_fields = ("compound__lam_id", "compound__name", "expiration_year")
    list_display = ("compound", "get_name", "patent_id", "expiration_year")

    def get_name(self, obj):
        return obj.compound.name
    get_name.short_description="Name"
admin.site.register(Patent, Patent_Admin)

class Manufacturer_Admin(admin.ModelAdmin):
    search_fields = ("compound__lam_id", "compound__name", "name")
    list_display = ("compound", "get_name", "name", "contact_info")

    def get_name(self, obj):
        return obj.compound.name
    get_name.short_description="Name"
admin.site.register(Manufacturer, Manufacturer_Admin)
    
class Side_Effect_Admin(admin.ModelAdmin):
    search_fields = ("compound1__lam_id", "compound1__name", "compound2__name", "compound2__lam_id", "side_effect", "source__name")
    list_display = ("compound1", "get_name1", "compound2", "get_name2", "side_effect", "source", "probability")

    def get_name1(self, obj):
        return obj.compound1.name
    get_name1.short_description="Name"

    def get_name2(self, obj):
        return obj.compound2.name
    get_name2.short_description="Name"
admin.site.register(Side_Effect, Side_Effect_Admin)

class Annotated_With_Admin(admin.ModelAdmin):
    search_fields = ("compound__lam_id", "compound__name", "annotation__description", "annotation__annotation_id")
    list_display = ("compound", "get_compound", "get_id", "get_description")

    def get_compound(self, obj):
        return obj.compound.name
    get_compound.short_description="Name"

    def get_id(self, obj):
        return obj.annotation_id
    get_id.short_description="Annotation ID"

    def get_description(self, obj):
        return obj.description
    get_description.short_description="Annotation Description"
admin.site.register(Annotated_With, Annotated_With_Admin)
