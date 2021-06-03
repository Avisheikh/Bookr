from django.contrib import admin
from reviews.models import  Contributor, Book, BookContributor, Review


def initialled_name(obj):
    initials = ''.join([name[0] for name in obj.first_names.split(' ')])
    return "{}, {}".format(obj.last_names, initials)

class ContributorAdmin(admin.ModelAdmin):
    list_display = (initialled_name,)    

class BookAdmin(admin.ModelAdmin):

    date_hierarchy = 'publication_date'
    list_display = ('title','isbn')
    list_filter = ('publisher', 'publication_date')
    search_fields = ('title', 'isbn__exact', 'publisher__name')

    def isbn13(self, obj):

        return "{} - {} - {} - {} - {}".format(obj.isbn[0:3], obj.isbn[3:4], obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13])



# Register your models here.

admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)


