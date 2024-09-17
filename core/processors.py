from .models import About, Linksocial, Category

# ABOUT
def ctx_dic_about(req):
    ctx_about = {}    
    ctx_about['ABOUT'] = About.objects.latest('created')    
    return ctx_about

# CATEGORIES
def ctx_dic_categories(req):
    ctx_categories = {}
    categories = Category.objects.all()
    
    for category in categories:
        ctx_categories[category.id] = {
            'name': category.name,
            'active': category.active,
            'description': category.description,
            'image': category.image
        }
    return {'categories_all': ctx_categories}
    


# LINK SOCIAL
def ctx_dic_linksocial(req):
    ctx_links = {}    
    links = Linksocial.objects.all().exclude(url=None)
    
    
    for link in links:
        ctx_links[link.key] = {
            'name': link.name,
            'url': link.url,
            'icon': link.icon
        }

    return {'link_all':ctx_links}