from django.db import models

class Cliente(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Importadora(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, default='')
    phone_number = models.IntegerField()
    site = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200)
    province = models.CharField(choices=(
            (1, "Cidade de Maputo"),
            (2, "Provincia de Maputo"),
            (3, "Inhambane"),
            (4, "Gaza"),
            (5, "Sofala"),
            (6, "Manica"),
            (7, "Tete"),
            (8, "Zambezia"),
            (9, "Nampula"),
            (10, "Niassa"),
            (11, "Cabo Delgado"),
        ),
        max_length=1)

    def __str__(self):
        return self.name
    
    
    # Nome
# Nome_Comercial
# Descricao 
# Validade 
# Categoria(suposta entidade)
# Substância activa
# Composicao quimica
# Apresentação (quantidade)
# Fabricante (suposta entidade)

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique = True)

    def save(self, *args, **kwargs): 
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    class Meta:
        verbose_name_plural = 'Categories'


    def __str__(self): 
        return self.name
        
class Produto(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    comercial_name = models.CharField(max_length=200, null=False, blank=False)
    description = models.CharField(max_length=200)
    expire_date = models.DateTimeField()
    category = models.CharField(max_length=200)
    made_in = models.CharField(max_length=200)
    price = models.FloatField()


    def __str__(self):
        return self.name
