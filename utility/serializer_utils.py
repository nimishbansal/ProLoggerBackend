from rest_framework import serializers


class DisplaySelectedFieldMixin:
    """
    It is a mixin used to show specific keys only for response dict on the basis of keys mentioned in
    kwargs['display_fields'] or exclude the keys mentioned in kwargs['exclude_fields'].

    kwargs can be edited in get_serializer() function of an API View
    """

    def __init__(self, *args, **kwargs):
        self.print_error_messages = True

        if "display_fields" in kwargs and "exclude_fields" in kwargs:
            raise Exception("Cant set both 'display_fields' and 'exclude_fields' together")

        elif "display_fields" not in kwargs and "exclude_fields" not in kwargs:
            if self.print_error_messages:
                print("Not using DisplaySelectedField mixin. Specify either 'display_fields' or 'exclude_fields' ")

        try:
            self.display_fields = kwargs.pop("display_fields")
        except KeyError:
            self.display_fields = None

        try:
            self.exclude_fields = kwargs.pop("exclude_fields")
        except KeyError:
            self.exclude_fields = None

        super().__init__(*args, **kwargs)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.display_fields:
            data_fields = data.keys()
            display_fields = self.display_fields
            fields_to_pop = data_fields - display_fields
            for field in fields_to_pop:
                data.pop(field)

        elif self.exclude_fields:
            for field in self.exclude_fields:
                data.pop(field)

        return data


class CompleteDateTimeSerializer(serializers.Serializer):
    year = serializers.IntegerField()
    month = serializers.IntegerField()
    day = serializers.IntegerField()
    hour = serializers.IntegerField()
    minute = serializers.IntegerField()
    second = serializers.IntegerField()
    microsecond = serializers.IntegerField()
