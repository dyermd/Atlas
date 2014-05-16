from django.contrib import admin
from interaction.models import Protein_Protein
from interaction.models import Protein_Compound
from interaction.models import Compound_Compound

# Register your models here.
class Protein_Protein_Admin(admin.ModelAdmin):
    search_fields = ("protein1__uniprot_id", "protein1__gene_name", "protein2__uniprot_id", "protein2__gene_name", "detection_method__description", "interaction_type__description", "source__name")
    list_display = ("protein1", "get_gene1", "protein2", "get_gene2", "article", "source", "get_detection", "get_type")

    def get_gene1(self, obj):
        return obj.protein1.gene_name
    get_gene1.short_description='Gene'

    def get_gene2(self, obj):
        return obj.protein2.gene_name
    get_gene2.short_description='Gene'

    def get_detection(self, obj):
        return obj.detection_method.description
    get_detection.short_description='Detection Method'

    def get_type(self, obj):
        return obj.interaction_type.description
    get_type.short_description='Interaction Type'
admin.site.register(Protein_Protein, Protein_Protein_Admin)

class Compound_Compound_Admin(admin.ModelAdmin):
    search_fields = ("compound1__lam_id", "compound1__name", "compound2__lam_id", "compound2__name", "side_effect__side_effect", "source__name")
    list_display = ("compound1", "get_name1", "compound2", "get_name2", "side_effect", "article", "source")

    def get_name1(self, obj):
        return obj.compound1.name
    get_name1.short_description='Compound'

    def get_name2(self, obj):
        return obj.compound2.name
    get_name2.short_description='Compound'
admin.site.register(Compound_Compound, Compound_Compound_Admin)

class Protein_Compound_Admin(admin.ModelAdmin):
    search_fields = ("protein__uniprot_id", "protein__gene_name", "compound__lam_id", "compound__name", "source")
    list_display = ("protein", "get_gene", "compound", "get_compound", "article", "source")

    def get_gene(self, obj):
        return obj.protein.gene_name
    get_gene.short_description='Gene'

    def get_compound(self, obj):
        return obj.compound.name
    get_compound.short_description='Compound'
admin.site.register(Protein_Compound, Protein_Compound_Admin)
