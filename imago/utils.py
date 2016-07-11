from rest_framework import serializers

def django_obj_to_dict(obj, include=None, exclude=None, children=None, parent=None, depth=1):
    if obj is None:
        return None
    if exclude is None:
        exclude = []
    if children is None:
        children = {}
    if include:
        included_fields = [f for f in obj._meta.get_fields() if f.name in include]
    else:
        included_fields = [f for f in obj._meta.get_fields() if f.name not in exclude]

    objdict = {}
    for f in included_fields:
        if not f.is_relation:
            objdict[f.name] = getattr(obj, f.name)
        else:
            if depth <= 0:
                continue
            if f.one_to_many:
                objdict[f.name] = [django_obj_to_dict(child,
                            children.get(f.name, {}).get('include', []),
                            children.get(f.name, {}).get('exclude', []),
                            children.get(f.name, {}).get('children', {}),
                            obj,
                            depth-1,
                            )
                    for child in getattr(obj, f.name).all()
                    ]
            elif f.many_to_one:
                child = getattr(obj, f.name)
                if child == parent:
                    continue
                objdict[f.name] = django_obj_to_dict(child,
                                children.get(f.name, {}).get('include', []),
                                children.get(f.name, {}).get('exclude', []),
                                children.get(f.name, {}).get('children', {}),
                                obj,
                                depth-1,
                                )
            else:
                raise ValueError('inhandled relation: ' + f.name)

    return objdict


class InlineListField(serializers.ListField):
    def __init__(self, *args, **kwargs):
        self.include = kwargs.pop('include', [])
        self.exclude = kwargs.pop('exclude', [])
        self.children = kwargs.pop('children', {})
        super().__init__(*args, **kwargs)

    def to_representation(self, obj):
        return [django_obj_to_dict(i, self.include, self.exclude, self.children) for i in obj.all()]
