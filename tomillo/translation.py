from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Prensa)
class PrensaTranslationOptions(TranslationOptions):
    fields = ('titulo', 'descripcion')

@register(Alumni)
class AlumniTranslationOptions(TranslationOptions):
    fields = ('acerca_de',)

@register(Aliado)
class AliadoTranslationOptions(TranslationOptions):
    fields = ('testimonio',)

@register(Numero)
class NumeroTranslationOptions(TranslationOptions):
    fields = ('nombre',)

@register(Programa)
class ProgramaTranslationOptions(TranslationOptions):
    fields = ('descripcion','contenido','requisitos','nombrePrograma',)

@register(Promocion)
class PromocionTranslationOptions(TranslationOptions):
    fields = ('nombrePromo',)


@register(Recurso)
class RecursoTranslationOptions(TranslationOptions):
    fields = ('nombreRec',)