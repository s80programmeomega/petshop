from django.contrib import admin
from django.utils.html import format_html
from .models import Specie, Breed, Pet, PetPhoto, Owner, OwnerPhoto


class BaseAdmin(admin.ModelAdmin):
    readonly_fields = ('created_by',)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


class BreedInline(admin.TabularInline):
    model = Breed
    extra = 0


class PetInline(admin.TabularInline):
    model = Pet
    extra = 0


class OwnerPhotoInline(admin.TabularInline):
    model = OwnerPhoto
    extra = 0


@admin.register(Specie)
class SpecieAdmin(BaseAdmin):
    list_display = ('id', 'name', 'description',
                    'created_by', 'created_at', 'updated_at')
    list_filter = ('created_by',)
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    ordering = ('id',)
    inlines = [BreedInline]


@admin.register(Breed)
class BreedAdmin(BaseAdmin):
    list_display = ('id', 'name', 'description', 'specie',
                    'created_by', 'created_at', 'updated_at')
    list_filter = ('name', 'specie', 'description', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'specie')
    ordering = ('id',)
    inlines = [PetInline]


class PetPhotoInline(admin.TabularInline):
    model = PetPhoto
    extra = 0


@admin.register(Pet)
class PetAdmin(BaseAdmin):
    list_display = ('id', 'name', 'breed', 'age', 'description',
                    'created_by', 'created_at', 'updated_at')
    list_filter = ('name', 'breed', 'description', 'age', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'breed')
    ordering = ('id',)
    inlines = [PetPhotoInline]


@admin.register(PetPhoto)
class PetPhotoAdmin(BaseAdmin):
    def image_thumbnail(self, obj: PetPhoto):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'No image'
    image_thumbnail.short_description = 'Image Thumbnail'

    list_display = ('id', 'description', 'pet', 'image',
                    'image_thumbnail', 'created_by', 'created_at', 'updated_at')
    list_filter = ('pet', 'description', 'created_by')
    list_display_links = ('id', 'pet')
    search_fields = ('pet',)
    ordering = ('id',)


@admin.register(Owner)
class OwnerAdmin(BaseAdmin):
    list_display = ('id', 'name', 'email', 'first_name',
                    'last_name', 'created_by', 'created_at')
    list_filter = ('name', 'email', 'first_name', 'last_name', 'created_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'bio')
    ordering = ('id',)
    inlines = [PetInline, OwnerPhotoInline]


@admin.register(OwnerPhoto)
class OwnerPhotoAdmin(BaseAdmin):
    def image_thumbnail(self, obj: OwnerPhoto):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        else:
            return 'No image'
    image_thumbnail.short_description = 'Image Thumbnail'

    list_display = ('id', 'description', 'owner', 'image',
                    'image_thumbnail', 'created_by', 'created_at', 'updated_at')
    list_filter = ('owner', 'description', 'created_at')
    list_display_links = ('id', 'owner')
    search_fields = ('owner',)
    ordering = ('id',)
