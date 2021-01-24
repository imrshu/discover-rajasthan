from django.db import models
from django.utils.text import slugify
from django_resized import ResizedImageField


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, null=True, blank=True)
    image = ResizedImageField(size=[800, 533], upload_to='category', null=True, blank=True)
    description = models.TextField()
    display_order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Packages'
        ordering = ('display_order',)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/packages/category/{self.slug}/tours/'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)


class Tour(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = ResizedImageField(size=[800, 533], upload_to='tours', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    price = models.PositiveIntegerField(default=0)
    price_is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/packages/category/{self.category.slug}/tours/{self.slug}/'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tour, self).save(*args, **kwargs)


class TourDetail(models.Model):
    tour = models.OneToOneField(Tour, on_delete=models.CASCADE)
    image1 = ResizedImageField(size=[1000,450], upload_to='tour_detail')
    image2 = ResizedImageField(size=[1000,450], upload_to='tour_detail')
    image3 = ResizedImageField(size=[1000,450], upload_to='tour_detail', null=True, blank=True)
    num_of_days = models.PositiveIntegerField(default=0)
    num_of_nights = models.PositiveIntegerField(default=0)
    description = models.TextField()
    inclusion = models.TextField()
    exclusion = models.TextField()
    highlights = models.TextField()
    flight_included = models.BooleanField(default=False)
    cab_included = models.BooleanField(default=False)
    breakfast_included = models.BooleanField(default=False)
    hotel_included = models.BooleanField(default=False)
    sightseeing_included = models.BooleanField(default=False)
    special_highlight = models.CharField(max_length=100)
    keywords = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class TourItenary(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    rating = models.PositiveIntegerField(default=1)
    review = models.TextField()


    def __str__(self):
        return self.tour.title


class BookNow(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    travel_date = models.DateField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=15)
    no_of_people = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name_plural = 'Customer Booking'

    def __str__(self):
        return self.tour.title + ' ' + self.email
