from django.contrib import admin
from analysis.models import Analysis
from analysis.models import Compound_Interaction_Result
from analysis.models import Compound_Sensitivity_Result
from analysis.models import Transposon_Result
from analysis.models import Mutation_Result
from analysis.models import Array_Result
from analysis.models import Coverage_Stat_Result

# Register your models here.

class Analysis_Admin(admin.ModelAdmin):
    search_fields = ("name", "description", "type", "parameters", "status")
    list_fields = ("name", "description", "type", "parameters", "status", "date")
admin.site.register(Analysis, Analysis_Admin)

class Compound_Interaction_Result_Admin(admin.ModelAdmin):
    search_fields = ("analysis__name", "analysis__source__name", "sample__name", "compound__name", "compound__lam_id", "protein__uniprot_id", "protein__gene_name")
    list_fields = ("analysis", "get_source", "sample", "compound", "get_name", "protein", "get_gene", "p-value")

    def get_source(self, obj):
        return obj.source.name
    get_source.short_description='Source'

    def get_name(self, obj):
        return obj.compound.name
    get_name.short_description='Name'

    def get_gene(self, obj):
        return obj.protein.gene_name
    get_gene.short_description='Gene'
admin.site.register(Compound_Interaction_Result, Compound_Interaction_Result_Admin)

class Compound_Sensitivity_Result_Admin(admin.ModelAdmin):
    search_fields = ("analysis__name", "analysis__source__name", "sample__name", "compound__name", "compound__lam_id")
    list_fields = ("analysis", "get_source", "sample", "compound", "get_name", "ic50")

    def get_source(self, obj):
        return obj.source.name
    get_source.short_description='Source'

    def get_name(self, obj):
        return obj.compound.name
    get_name.short_description='Name'
admin.site.register(Compound_Sensitivity_Result, Compound_Sensitivity_Result_Admin)

class Transposon_Result_Admin(admin.ModelAdmin):
    search_fields = ("analysis__name", "analysis__source__name", "sample__name", "protein__uniprot_id", "protein__gene_name")
    list_fields = ("analysis", "get_source", "sample", "compound", "get_name", "position", "coverage", "frequency", "sequence", "strand", "location", "distance")

    def get_source(self, obj):
        return obj.source.name
    get_source.short_description='Source'

    def get_name(self, obj):
        return obj.compound.name
    get_name.short_description='Name'
admin.site.register(Transposon_Result, Transposon_Result_Admin)

class Mutation_Result_Admin(admin.ModelAdmin):
    search_fields = ("analysis__name", "analysis__source__name", "sample__name", "protein__uniprot_id", "protein__gene_name", "category", "type")
    list_fields = ("analysis", "get_source", "sample", "protein", "get_gene", "position", "category", "type", "total_coverage", "reference_coverage", "variant_coverage", "reference_call", "variant_call", "frequency")

    def get_source(self, obj):
        return obj.source.name
    get_source.short_description='Source'

    def get_gene(self, obj):
        return obj.protein.gene_name
    get_gene.short_description='Gene'
admin.site.register(Mutation_Result, Mutation_Result_Admin)

class Array_Result_Admin(admin.ModelAdmin):
    search_fields = ("analysis__name", "analysis__source__name", "sample__name", "protein__uniprot_id", "protein__gene_name")
    list_fields = ("analysis", "get_source", "sample", "protein", "get_gene", "normalized_value")

    def get_source(self, obj):
        return obj.source.name
    get_source.short_description='Source'

    def get_gene(self, obj):
        return obj.protein.gene_name
    get_gene.short_description='Gene'
admin.site.register(Array_Result, Array_Result_Admin)

class Coverage_Stat_Result_Admin(admin.ModelAdmin):
    search_fields = ("analysis__name", "analysis__source__name", "sample__name")
    list_fields = ("analysis", "get_source", "sample", "mapped_read", "percent_on_target", "average_coverage", "uniformity_of_coverage", "percent_1x", "percent_20x", "percent_100x")

    def get_source(self, obj):
        return obj.source.name
    get_source.short_description='Source'
admin.site.register(Coverage_Stat_Result, Coverage_Stat_Result_Admin)

