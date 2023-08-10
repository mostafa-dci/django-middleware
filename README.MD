# Middleware in Django

## Table Of Content

- [What Is Middleware](#what-is-middleware).
- [Usage Of Middleware](#usage-of-middleware).
- [How To Write a Middleware in Django](#how-to-write-a-middleware-in-django).
- [Queries/Params in Django URI](#queries-params-in-django-uri).
- [Delete Records In Django](#delete-records-in-django).
- [Update Record In Django](#update-record-in-django)

---

## What Is Middleware

>It’s a light, low-level “plugin” system for globally altering Django’s input or output. [Official Docs](https://docs.djangoproject.com/en/4.2/topics/http/middleware/).

- Middle Process between `Request` and `Response`.
- It can Kill the process between receiving Request and sending response, according to some conditions.
- The order in `MIDDLEWARE` array in `settings.py` is very **IMPORTANT**.
- Each middleware component is responsible for doing some specific function.

---

## Usage Of Middleware

During the request phase, before calling the view, Django applies middleware in the order it’s defined in MIDDLEWARE, top-down.

You can think of it like an onion: each middleware class is a “layer” that wraps the view, which is in the core of the onion. If the request passes through all the layers of the onion (each one calls get_response to pass the request in to the next layer), all the way to the view at the core, the response will then pass through every layer (in reverse order) on the way back out.

If one of the layers decides to short-circuit and return a response without ever calling its get_response, none of the layers of the onion inside that layer (including the view) will see the request or the response. The response will only return through the same layers that the request passed in through.

---

## How To Write a Middleware in Django

1. Create a folder in Application name it `middlewares`.
2. Create a file in that folder, name it `middleware.py`.
3. In this file, write the middleware, function or class:

```python
def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
```

4. Register this middleware in `settings.py`:

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    ...
    ...
    ...
    'My_MIDDLEWARE_MIDDLEWARE_FUNCTION',
]
```
---

## Queries Params in Django URI

In Django, Uniform Resource Identifiers (URIs) often contain queries or parameters that allow you to dynamically pass information to views and control the behavior of your web application. Queries or parameters are added to the end of a URL and are separated from the base URL by a question mark (?), followed by key-value pairs.

Django uses these queries/params to retrieve specific data or modify the behavior of a view. These parameters are extracted from the URL and can be accessed within your view functions using the request object.

```
https://example.com/products/?category=electronics&page=2
```

In this URL, there are two query parameters: category with the value electronics and page with the value 2. In a Django view function, you can access these parameters like this:

```python
def product_list(request):
    category = request.GET.get('category')
    page = request.GET.get('page')
    # Your logic here
```
### Handling Query Parameters

Django provides a convenient way to handle query parameters through the request.GET attribute. This attribute is a dictionary-like object that allows you to access query parameters and their values. It's important to note that values obtained from request.GET are always strings, so you might need to perform type conversion as needed.

### Optional vs. Required Parameters

Query parameters can be both optional and required. To make a parameter required, your view's logic should include appropriate error handling when the parameter is missing or invalid.

### URL Examples

Here are a few examples of how query parameters can be used in Django URLs:

```
https://example.com/products/?category=electronics
```

Paginating through search results:

```
https://example.com/search/?q=django&page=3
```

Customizing user preferences:

```
https://example.com/settings/?theme=dark&notifications=true
```

### Security Considerations

When working with query parameters, be cautious about security vulnerabilities like SQL injection. Always sanitize and validate user inputs before using them in database queries or other critical operations.

In summary, query parameters in Django URIs provide a flexible way to pass and retrieve information from URLs, enabling dynamic behavior in your web applications. Proper handling and validation of these parameters are essential for maintaining security and functionality.


## Delete Records In Django

In Django, deleting records from a database is a fundamental operation often required when managing your application's data. The process involves removing specific entries from a database table based on certain conditions. Django provides a straightforward way to accomplish this task using its Object-Relational Mapping (ORM) system.

### Deleting Records Using the ORM

To delete records using the Django ORM, you typically follow these steps:

1. Import the Model: Import the model that represents the database table from which you want to delete records.
2. Specify Conditions: Define the conditions that determine which records to delete. You can use filters to narrow down the selection of records.
3. Perform Deletion: Use the delete() method on the queryset obtained from the model to delete the selected records.

```python
from myapp.models import Product

# Delete all products with a certain condition
Product.objects.filter(category='electronics').delete()
```

### Deleting a Single Record

If you want to delete a single record, you can first retrieve the record using a queryset and then call the delete() method on that instance:

```python
product = Product.objects.get(pk=1)  # Assuming 'pk' is the primary key field
product.delete()
```

### Deleting Cascades

Django provides the option to specify cascading deletion, where related records are automatically deleted when the parent record is deleted. This is defined in the model using the on_delete parameter of ForeignKey fields.

```python
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

In this example, when an Author instance is deleted, all related Book instances associated with that author will be automatically deleted.

### Soft Deletion

Sometimes, rather than permanently deleting records, you might want to implement a soft deletion approach where records are marked as deleted but not physically removed from the database. This can be useful for data recovery and audit purposes.

### Caution and Security

When deleting records, exercise caution to avoid accidentally removing important data. Always make sure you have proper backups and implement safety mechanisms when dealing with deletion operations, especially in production environments.

In summary, Django's ORM provides a reliable and efficient way to delete records from your database. Understanding the various methods and options available for deletion will help you manage your application's data effectively.

---

## Update Record In Django

In Django, updating records in a database is a core operation when you need to modify existing data in your application. The process involves locating specific records based on certain conditions and then applying changes to their attributes. Django's Object-Relational Mapping (ORM) system simplifies the process of updating records.

### Updating Records Using the ORM

To update records using the Django ORM, follow these steps:

1. Import the Model: Begin by importing the model that corresponds to the database table you want to update.
2. Specify Conditions: Define the conditions that identify the records you wish to update using filters.
3. Perform Update: Use the update() method on the queryset obtained from the model to apply changes to the selected records.

```python
from myapp.models import Product

# Update the price of all products in a certain category
Product.objects.filter(category='electronics').update(price=1000)
```

### Updating a Single Record

When updating a single record, retrieve the instance using a queryset and then modify its attributes before calling the save() method:

```python
product = Product.objects.get(pk=1)  # Assuming 'pk' is the primary key field
product.price = 1200
product.save()
```

### Updating Related Records

To update related records in a ForeignKey relationship, retrieve the parent instance and update the related field:

```python
author = Author.objects.get(pk=1)
author.name = "New Author Name"
author.save()
```

### Handling Bulk Updates

Django's update() method can also handle bulk updates efficiently without fetching individual records:

```python
Product.objects.filter(category='electronics').update(price=models.F('price') * 1.1)
# In this example, the price of electronics products is increased by 10%.
```




