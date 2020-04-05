from pynamodb import attributes, models


class BaseModel(models.Model):
    @classmethod
    def dict2model(cls, data_dict):
        """
        Converts dict to pynamodb model representation
        :param data_dict: dict, that is to be converted to model instance
        :return: pynamodb model instance
        """

        instance = cls()
        for attribute_name, attribute_obj in cls.get_attributes().items():
            if isinstance(attribute_obj, attributes.MapAttribute):
                obj = attribute_obj.__class__(data_dict.get(attribute_name))
                setattr(instance, attribute_name, obj)
            else:
                setattr(instance, attribute_name, attribute_obj)
        return instance

    def model2dict(self):
        """
        Converts pynamodb model to its dict representation
        :return: dict representation of pynamodb model instance
        """

        def to_primitive(obj_list):
            data = []
            for item in obj_list:
                if isinstance(item, str) or isinstance(item, int):
                    data.append(item)
                else:
                    data.append(item.as_dict())
            return data

        result = {}
        for attribute_name, attribute_obj in self.get_attributes().items():
            if isinstance(attribute_obj, attributes.MapAttribute):
                result[attribute_name] = getattr(self, attribute_name).as_dict()
            elif isinstance(attribute_obj, attributes.ListAttribute):
                result[attribute_name] = to_primitive(getattr(self, attribute_name))
            else:
                result[attribute_name] = getattr(self, attribute_name)
        return result

    class Meta:
        table_name = None
        region = 'us-east-1'
        host = 'http://localhost:4569'
        read_capacity_units = 10
        write_capacity_units = 10
        # read_capacity_units = DYNAMODB_CONFIG['default_read_capacity']
        # write_capacity_units = DYNAMODB_CONFIG['default_write_capacity']


if __name__ == '__main__':
    pass
