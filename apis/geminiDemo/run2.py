import sys
import absl.logging
from models import interactive
import yaml

absl.logging.set_verbosity(absl.logging.INFO)


class Field(object):
    def __init__(
        self,
        name,
        column_type=str,
        default_value=str(),
        call="func",
        callback_func=lambda x: x
    ):
        self.name = name
        self.column_type = column_type
        self.callback_func = callback_func
        self.default_value = default_value
        self.call = call
        self.call_func = {
            "func": self.callback_func
        }


class ModelMetaclass(type):

    def __new__(cls, name, base, attrs):
        if name == "Model":
            return type.__new__(cls, name, base, attrs)
        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)
            attrs['__mappings__'] = mappings
            attrs['__table__'] = name

        return type.__new__(cls, name, base, attrs)


class Model(dict, metaclass=ModelMetaclass):

    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(
                r"'Model' object has no attribute '%s'" % key
            )

    def __setattr__(self, key, value):
        self.__mappings__[key] = value

    def to_json(self):
        rsp = dict()
        for key, value in self.__mappings__.items():
            rsp[value.name] = value.callback_func(
                getattr(self, key, value.default_value)
            )
        return rsp

    def convert(self):
        rsp = dict()
        for key, value in self.__mappings__.items():
            if isinstance(value, Field):
                rsp[value.name] = value.callback_func(
                    getattr(self, key, value.default_value)
                )
        return rsp


def load_config(filepath="", model=None):
    with open(filepath, 'r') as yamlfile:
        config = yaml.safe_load(yamlfile)

    return model(**config).convert()


class Config(Model):
    api_key = Field("api_key", column_type=str, default_value="")


def main():
    filePath = '/Users/ccxn/Documents/workspace/repositories' \
        '/geminiDemo/conf2.yaml'
    try:
        conf = load_config(filepath=filePath, model=Config)
        genai = interactive.GenAI(**conf)

        if len(sys.argv) < 2:
            absl.logging.error("Usage: python your_script.py <your_query>")
            return

        q_trans = sys.argv[1]
        rsp = genai.gen_content(q_trans)
        print(rsp)

    except FileNotFoundError:
        absl.logging.error("Config file not found.")
    except yaml.YAMLError as e:
        absl.logging.error(f"Error parsing YAML config file: {e}")
    except Exception as e:  # Catch other potential errors
        absl.logging.exception(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
