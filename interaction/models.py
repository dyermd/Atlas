from django.db import models
from protein.models import Protein
from compound.models import Compound
from article.models import Article
from annotation.models import Annotation
from compound.models import Side_Effect
from source.models import Source
from analysis.models import Analysis

# Create your models here.
class Protein_Protein(models.Model):
    protein1 = models.ForeignKey(Protein, related_name='protein1')
    protein2 = models.ForeignKey(Protein, related_name='protein2')
    source = models.ForeignKey(Source)
    article = models.ForeignKey(Article)
    detection_method = models.ForeignKey(Annotation, related_name='pmi_detection')
    interaction_type = models.ForeignKey(Annotation, related_name='pmi_interaction')
    analysis = models.ForeignKey(Analysis, null=True, blank=True)

    def __unicode__(self):
        return (self.protein1.uniprot_id + '-' + self.protein2.uniprot_id)

    class Meta:
        verbose_name = "Protein-Protein Interaction"
        verbose_name_plural = "Protein-Protein Interactions"

class Protein_Compound(models.Model):
    compound = models.ForeignKey(Compound)
    protein = models.ForeignKey(Protein)
    source = models.ForeignKey(Source)
    article = models.ForeignKey(Article)
    analysis = models.ForeignKey(Analysis, null=True, blank=True)

    def __unicode__(self):
        return (self.compound.drug_name + '-' + self.protein.uniprot_id)

    class Meta:
        verbose_name = "Protein-Compound Interaction"
        verbose_name_plural = "Protein-Compound Interactions"

class Compound_Compound(models.Model):
    compound1 = models.ForeignKey(Compound, related_name='compound1')
    compound2 = models.ForeignKey(Compound, related_name='compound2')
    side_effect = models.ForeignKey(Side_Effect)
    source = models.ForeignKey(Source)
    article = models.ForeignKey(Article)
    analysis = models.ForeignKey(Analysis, null=True, blank=True)

    def __unicode__(self):
        return (self.compound1.compound_name + '-' + self.compound2.compound_name)

    class Meta:
        verbose_name = "Compound-Compound Interaction"
        verbose_name_plural = "Compound-Compound Interactions"
