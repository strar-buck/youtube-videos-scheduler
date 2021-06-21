from django_filters import rest_framework as filters


def make_model_filter(model, **kwargs):
    """Create a custom model filter

    :param: model: not a model_name , ModelClass
    :param **kwargs: optional , Dictionary of custom filter function 

        Defining a custom model filter
        def search_filter(self, qs, name, value):
            :param search: name of the filter
            :param value: value of filter
            
            :return qs
    :return: Filter Class
    """
    # All internal fileds on model
    fields = model._meta.get_fields()

    fields_of_filter = {}
    for f in fields:
        fields_of_filter[f.name] = ["exact"]

    Meta = type("Meta", (), {model: model, fields: fields_of_filter})
    class_fields = {"Meta": Meta, "__module__": model.__module__}

    # Handling custom filter
    for key, value in kwargs.items():
        filter_name = key + "_filter"
        class_fields[key] = filters.CharFilter(method=filter_name)
        class_fields[filter_name] = value

    Filter = type("Filter", (filters.FilterSet,), class_fields)
    return Filter
