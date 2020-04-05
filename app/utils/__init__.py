from importlib import import_module


def get_module_from_dotted_path(dotted_module_path):
    try:
        module = import_module(dotted_module_path)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(f'{dotted_module_path} is not a valid dotted path')
    except Exception:
        raise Exception('Something weired happened to the project')
    return module

# def import_from_string(dotted_module_path, item):
#     module = module_from_dotted_path(dotted_module_path)
#     py_obj = getattr(module, item)
#     return py_obj
