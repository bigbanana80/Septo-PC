from django.contrib.sitemaps import Sitemap
from .models import blog  

class BlogSitemap(Sitemap):
    changefreq = "weekly"  
    priority = 0.8  
    
    def items(self):
        return blog.objects.all()  

    def lastmod(self, obj: blog):
        return obj.date_updated  
