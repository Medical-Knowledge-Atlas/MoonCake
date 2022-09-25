class Filter:
    def __init__(self):
        pass

    def supplier(self, data, context):
        """自定义解析逻辑"""
        print('Filter data')
        return data

    def xx(self, data, context):
        """自定义解析逻辑"""
        return data
