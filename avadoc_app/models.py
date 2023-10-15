from django.db import models


# Create your models here.
class Docente(models.Model):
    id_docente = models.AutoField(primary_key=True)
    cod_docente = models.CharField(max_length=200, blank=True, null=True)
    nome_docente = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table= 'Docente'


class Curso(models.Model):
    id_curso = models.AutoField(primary_key=True)
    cod_curso = models.CharField(max_length=200, blank=True, null=True)
    turma_curso = models.CharField(max_length=200, blank=True, null=True)
    nome_curso = models.CharField(max_length=200, blank=True, null=True)
    turno_curso = models.CharField(max_length=200, blank=True, null=True)
    periodo_curso = models.CharField(max_length=200, blank=True, null=True)


class Campi(models.Model):
    id_campi = models.AutoField(primary_key=True)
    cod_campi = models.CharField(max_length=200, blank=True, null=True)
    nome_campi = models.CharField(max_length=200, blank=True, null=True)

class Componente(models.Model):
    id_comp= models.AutoField(primary_key=True)
    nome_comp = models.CharField(max_length=200, blank=True, null=True)
    sigla_comp = models.CharField(max_length=200, blank=True, null=True)

class Nivel(models.Model):
    id_nivel= models.AutoField(primary_key=True)
    nome_nivel = models.CharField(max_length=200, blank=True, null=True)


class Discente(models.Model):
    id_discente= models.AutoField(primary_key=True)
    mat_discente= models.CharField(max_length=200, blank=True, null=True)
    nome_discente = models.CharField(max_length=200, blank=True, null=True)
    ingresso_discente = models.CharField(max_length=200, blank=True, null=True)
    campus_discente = models.CharField(max_length=200, blank=True, null=True)
    cidade_discente = models.CharField(max_length=200, blank=True, null=True)
    curso_discente = models.CharField(max_length=200, blank=True, null=True)
    nascimento_discente = models.CharField(max_length=200, blank=True, null=True)
    desc_curso_discente = models.CharField(max_length=200, blank=True, null=True)
    email_discente = models.CharField(max_length=200, blank=True, null=True)
    endereco_discente = models.CharField(max_length=200, blank=True, null=True)
    estado_discente = models.CharField(max_length=200, blank=True, null=True)
    fomr_ing_discente = models.CharField(max_length=200, blank=True, null=True)
    mun_res_discente = models.CharField(max_length=200, blank=True, null=True)
    naturalidade_discente = models.CharField(max_length=200, blank=True, null=True)
    resp_discente = models.CharField(max_length=200, blank=True, null=True)
    sexo_discente = models.CharField(max_length=200, blank=True, null=True)
    status_discente = models.CharField(max_length=200, blank=True, null=True)
    tel_discente = models.CharField(max_length=200, blank=True, null=True)

class Diario(models.Model):
    id_diario= models.AutoField(primary_key=True)
    id_curso= models.ForeignKey(Curso, models.DO_NOTHING, db_column='id_curso', blank=True, null=True)
    id_comp = models.ForeignKey(Componente, models.DO_NOTHING, db_column='id_comp', blank=True, null=True)
    id_nivel= models.ForeignKey(Nivel, models.DO_NOTHING, db_column='id_nivel', blank=True, null=True)
    id_docente = models.ForeignKey(Docente, models.DO_NOTHING, db_column='id_docente', blank=True, null=True)
    id_discente = models.ForeignKey(Discente, models.DO_NOTHING, db_column='id_discente', blank=True, null=True)
    id_campi = models.ForeignKey(Campi, models.DO_NOTHING, db_column='id_campi', blank=True, null=True)